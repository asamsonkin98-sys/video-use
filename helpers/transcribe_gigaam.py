"""Transcribe a video locally with GigaAM v2 (Russian) via sherpa-onnx.

Offline Russian ASR with no API key and no blocked hosts: the model is a
GitHub release asset (k2-fsa/sherpa-onnx) and the runtime installs from
PyPI. GigaAM v2 CTC emits per-character timestamps; this helper groups
them into words and writes a Scribe-shaped response to
<edit_dir>/transcripts/<video_stem>.json — the same `words` schema
(types 'word' / 'spacing', per-word start/end) the rest of the pipeline
consumes.

Russian-only. No speaker diarization (speaker_id is null), no audio-event
tags. Long sources are chunked at low-energy points near 25s boundaries.

Cached: if the output file already exists, transcription is skipped.

Usage:
    python helpers/transcribe_gigaam.py <video_path>
    python helpers/transcribe_gigaam.py <video_path> --edit-dir /custom/edit
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
import wave
from functools import lru_cache
from pathlib import Path

import numpy as np


MODEL_NAME = "sherpa-onnx-nemo-ctc-giga-am-v2-russian-2025-04-19"
MODEL_URL = (
    "https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/"
    f"{MODEL_NAME}.tar.bz2"
)
FRAME_S = 0.04          # GigaAM CTC emission step
CHUNK_S = 25.0          # target chunk length for long sources
CHUNK_SEARCH_S = 2.0    # look this far around the boundary for a quiet split


def model_dir() -> Path:
    env = os.environ.get("VIDEO_USE_GIGAAM_DIR")
    if env:
        return Path(env)
    return Path(__file__).resolve().parent.parent / "models" / MODEL_NAME


def ensure_model(verbose: bool = True) -> Path:
    mdir = model_dir()
    if (mdir / "model.int8.onnx").exists():
        return mdir
    mdir.parent.mkdir(parents=True, exist_ok=True)
    if verbose:
        print(f"  downloading GigaAM v2 model (~230 MB) to {mdir.parent}", flush=True)
    tarball = mdir.parent / f"{MODEL_NAME}.tar.bz2"
    subprocess.run(
        ["curl", "-sL", "--fail", "-o", str(tarball), MODEL_URL],
        check=True,
    )
    subprocess.run(["tar", "xjf", str(tarball), "-C", str(mdir.parent)], check=True)
    tarball.unlink()
    if not (mdir / "model.int8.onnx").exists():
        sys.exit(f"model archive did not contain {mdir}")
    return mdir


@lru_cache(maxsize=1)
def load_recognizer():
    try:
        import sherpa_onnx
    except ImportError:
        sys.exit(
            "sherpa-onnx is not installed. Run `uv pip install sherpa-onnx` "
            "(or `pip install sherpa-onnx`) inside the video-use repo."
        )
    mdir = ensure_model()
    return sherpa_onnx.OfflineRecognizer.from_nemo_ctc(
        model=str(mdir / "model.int8.onnx"),
        tokens=str(mdir / "tokens.txt"),
        num_threads=max(1, (os.cpu_count() or 4) - 1),
    )


def extract_audio(video_path: Path, dest: Path) -> None:
    cmd = [
        "ffmpeg", "-y", "-i", str(video_path),
        "-vn", "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le",
        str(dest),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def read_wav(path: Path) -> tuple[np.ndarray, int]:
    with wave.open(str(path)) as w:
        sr = w.getframerate()
        samples = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16)
    return samples.astype(np.float32) / 32768.0, sr


def chunk_boundaries(samples: np.ndarray, sr: int) -> list[tuple[int, int]]:
    """Split long audio into ~CHUNK_S chunks, cutting at the quietest 50ms
    window within ±CHUNK_SEARCH_S of each target boundary."""
    n = len(samples)
    chunk = int(CHUNK_S * sr)
    if n <= chunk + int(CHUNK_SEARCH_S * sr):
        return [(0, n)]
    win = int(0.05 * sr)
    search = int(CHUNK_SEARCH_S * sr)
    bounds = [0]
    pos = chunk
    while pos < n - search:
        lo = max(bounds[-1] + win, pos - search)
        hi = min(n - win, pos + search)
        seg = samples[lo:hi]
        # RMS over 50ms hops; pick the quietest window's center
        hops = max(1, (len(seg) - win) // win)
        rms = [float(np.sqrt(np.mean(seg[i * win:i * win + win] ** 2))) for i in range(hops)]
        cut = lo + int(np.argmin(rms)) * win + win // 2
        bounds.append(cut)
        pos = cut + chunk
    bounds.append(n)
    return list(zip(bounds[:-1], bounds[1:]))


def decode_chunk(rec, samples: np.ndarray, sr: int, offset: float) -> list[tuple[str, float]]:
    """Return [(token, absolute_timestamp)] for one chunk."""
    s = rec.create_stream()
    s.accept_waveform(sr, samples)
    rec.decode_stream(s)
    r = s.result
    return [(tok, ts + offset) for tok, ts in zip(r.tokens, r.timestamps)]


def tokens_to_words(token_ts: list[tuple[str, float]]) -> list[dict]:
    """Group per-character CTC tokens into Scribe-shaped word/spacing entries.

    Word end = the space token's emission time when it directly follows
    (clamped to +0.3s), else last char + 2 frames — CTC end times are
    approximate either way; the EDL's 30–200ms cut padding absorbs it.
    """
    words: list[dict] = []
    chars: list[tuple[str, float]] = []

    def flush(end_hint: float | None) -> None:
        nonlocal chars
        if not chars:
            return
        start = chars[0][1]
        last_ts = chars[-1][1]
        end = last_ts + 2 * FRAME_S
        if end_hint is not None:
            end = min(max(end_hint, last_ts + FRAME_S), last_ts + 0.3)
        text = "".join(c for c, _ in chars)
        if words:
            prev_end = words[-1]["end"]
            if start > prev_end:
                words.append({
                    "text": " ",
                    "start": round(prev_end, 3),
                    "end": round(start, 3),
                    "type": "spacing",
                })
        words.append({
            "text": text,
            "start": round(start, 3),
            "end": round(end, 3),
            "type": "word",
            "speaker_id": None,
        })
        chars = []

    for tok, ts in token_ts:
        if tok.strip() == "":
            flush(end_hint=ts)
        else:
            chars.append((tok, ts))
    flush(end_hint=None)
    return words


def call_gigaam(audio_path: Path, verbose: bool = True) -> dict:
    rec = load_recognizer()
    samples, sr = read_wav(audio_path)
    token_ts: list[tuple[str, float]] = []
    for lo, hi in chunk_boundaries(samples, sr):
        token_ts.extend(decode_chunk(rec, samples[lo:hi], sr, offset=lo / sr))
    words = tokens_to_words(token_ts)
    return {
        "language_code": "ru",
        "text": " ".join(w["text"] for w in words if w["type"] == "word"),
        "words": words,
        "transcriber": f"sherpa-onnx/{MODEL_NAME}",
    }


def transcribe_one(
    video: Path,
    edit_dir: Path,
    language: str | None = None,
    verbose: bool = True,
) -> Path:
    """Transcribe a single video locally with GigaAM. Returns transcript path.

    Cached: returns existing path immediately if the transcript already exists.
    `language` is accepted for interface parity; GigaAM is Russian-only.
    """
    if language not in (None, "ru"):
        print(f"  warning: GigaAM is Russian-only, ignoring language={language}", flush=True)

    transcripts_dir = edit_dir / "transcripts"
    transcripts_dir.mkdir(parents=True, exist_ok=True)
    out_path = transcripts_dir / f"{video.stem}.json"

    if out_path.exists():
        if verbose:
            print(f"cached: {out_path.name}")
        return out_path

    if verbose:
        print(f"  extracting audio from {video.name}", flush=True)

    t0 = time.time()
    with tempfile.TemporaryDirectory() as tmp:
        audio = Path(tmp) / f"{video.stem}.wav"
        extract_audio(video, audio)
        if verbose:
            print(f"  transcribing {video.stem}.wav with GigaAM v2", flush=True)
        payload = call_gigaam(audio, verbose)

    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    dt = time.time() - t0

    if verbose:
        kb = out_path.stat().st_size / 1024
        print(f"  saved: {out_path.name} ({kb:.1f} KB) in {dt:.1f}s")
        n_words = sum(1 for w in payload["words"] if w["type"] == "word")
        print(f"    words: {n_words}")

    return out_path


def main() -> None:
    ap = argparse.ArgumentParser(description="Transcribe a video locally with GigaAM v2 (Russian)")
    ap.add_argument("video", type=Path, help="Path to video file")
    ap.add_argument(
        "--edit-dir",
        type=Path,
        default=None,
        help="Edit output directory (default: <video_parent>/edit)",
    )
    args = ap.parse_args()

    video = args.video.resolve()
    if not video.exists():
        sys.exit(f"video not found: {video}")

    edit_dir = (args.edit_dir or (video.parent / "edit")).resolve()
    transcribe_one(video=video, edit_dir=edit_dir)


if __name__ == "__main__":
    main()
