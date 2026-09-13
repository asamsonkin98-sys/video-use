"""Transcribe a video locally with faster-whisper — no API key, no network.

Extracts mono 16kHz audio via ffmpeg, runs faster-whisper with word-level
timestamps, and writes a Scribe-shaped response to
<edit_dir>/transcripts/<video_stem>.json — the same `words` schema
(types 'word' / 'spacing', per-word start/end) that pack_transcripts.py
and the rest of the pipeline already consume.

Differences from Scribe: no speaker diarization (speaker_id is null) and
no audio-event tagging beyond what Whisper happens to transcribe.

Cached: if the output file already exists, transcription is skipped.

Usage:
    python helpers/transcribe_whisper.py <video_path>
    python helpers/transcribe_whisper.py <video_path> --model medium
    python helpers/transcribe_whisper.py <video_path> --language ru
    python helpers/transcribe_whisper.py <video_path> --edit-dir /custom/edit
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
from functools import lru_cache
from pathlib import Path


DEFAULT_MODEL = os.environ.get("VIDEO_USE_WHISPER_MODEL", "small")


def extract_audio(video_path: Path, dest: Path) -> None:
    cmd = [
        "ffmpeg", "-y", "-i", str(video_path),
        "-vn", "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le",
        str(dest),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


@lru_cache(maxsize=2)
def load_model(model_size: str):
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        sys.exit(
            "faster-whisper is not installed. Run `uv sync --extra whisper` "
            "(or `pip install faster-whisper`) inside the video-use repo."
        )
    return WhisperModel(model_size, device="cpu", compute_type="int8")


def call_whisper(
    audio_path: Path,
    model_size: str = DEFAULT_MODEL,
    language: str | None = None,
) -> dict:
    """Run faster-whisper and return a Scribe-shaped response dict."""
    model = load_model(model_size)
    segments, info = model.transcribe(
        str(audio_path),
        language=language,
        word_timestamps=True,
        vad_filter=True,
    )

    words: list[dict] = []
    prev_end: float | None = None
    for seg in segments:
        for w in seg.words or []:
            start = round(w.start, 3)
            end = round(w.end, 3)
            if prev_end is not None and start > prev_end:
                words.append({
                    "text": " ",
                    "start": prev_end,
                    "end": start,
                    "type": "spacing",
                })
            words.append({
                "text": w.word.strip(),
                "start": start,
                "end": end,
                "type": "word",
                "speaker_id": None,
            })
            prev_end = end

    return {
        "language_code": info.language,
        "language_probability": round(info.language_probability, 3),
        "text": " ".join(w["text"] for w in words if w["type"] == "word"),
        "words": words,
        "transcriber": f"faster-whisper/{model_size}",
    }


def transcribe_one(
    video: Path,
    edit_dir: Path,
    model_size: str = DEFAULT_MODEL,
    language: str | None = None,
    verbose: bool = True,
) -> Path:
    """Transcribe a single video locally. Returns path to transcript JSON.

    Cached: returns existing path immediately if the transcript already exists.
    """
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
            print(f"  transcribing {video.stem}.wav with faster-whisper/{model_size}", flush=True)
        payload = call_whisper(audio, model_size, language)

    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    dt = time.time() - t0

    if verbose:
        kb = out_path.stat().st_size / 1024
        print(f"  saved: {out_path.name} ({kb:.1f} KB) in {dt:.1f}s")
        n_words = sum(1 for w in payload["words"] if w["type"] == "word")
        print(f"    words: {n_words}")

    return out_path


def main() -> None:
    ap = argparse.ArgumentParser(description="Transcribe a video locally with faster-whisper")
    ap.add_argument("video", type=Path, help="Path to video file")
    ap.add_argument(
        "--edit-dir",
        type=Path,
        default=None,
        help="Edit output directory (default: <video_parent>/edit)",
    )
    ap.add_argument(
        "--model",
        type=str,
        default=DEFAULT_MODEL,
        help=f"Whisper model size: tiny/base/small/medium/large-v3 (default: {DEFAULT_MODEL})",
    )
    ap.add_argument(
        "--language",
        type=str,
        default=None,
        help="Optional ISO language code (e.g., 'ru'). Omit to auto-detect.",
    )
    args = ap.parse_args()

    video = args.video.resolve()
    if not video.exists():
        sys.exit(f"video not found: {video}")

    edit_dir = (args.edit_dir or (video.parent / "edit")).resolve()

    transcribe_one(
        video=video,
        edit_dir=edit_dir,
        model_size=args.model,
        language=args.language,
    )


if __name__ == "__main__":
    main()
