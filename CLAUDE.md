# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

video-use is itself an **agent skill** — a conversation-driven video editor for Claude Code (and Codex, etc.). The "product" is a pair of instruction documents plus a small set of Python helper scripts driven by ffmpeg:

- `SKILL.md` — the runtime spec. This is what an agent reads during an editing session. It contains the 12 Hard Rules (production correctness), the process, the EDL format, and the sub-agent briefs. It is the source of truth for behavior; the helpers implement it.
- `install.md` — first-time install spec (clone, deps, ffmpeg, skill registration, ElevenLabs API key).
- `helpers/` — the executable layer, invoked directly as `python helpers/<name>.py` (there are no console scripts).
- `skills/manim-video/` — a vendored sub-skill for Manim animation slots, with its own SKILL.md and references.

Both `SKILL.md` and `install.md` carry YAML frontmatter (`name`, `description`) — that is skill-registration metadata; keep it valid when editing. The skill is deployed by symlinking the repo into `~/.claude/skills/video-use/`, and it references helpers by bare name — so `SKILL.md` and `helpers/` must stay siblings at the repo root.

There is no test suite, linter config, or CI. Verify changes by running the helpers against a real video file (the install doc's rule: "don't declare success on file-existence checks alone").

## Setup and common commands

```bash
uv sync                  # or: pip install -e .   (deps: requests, librosa, matplotlib, pillow, numpy)
cp .env.example .env     # then set ELEVENLABS_API_KEY=...  (needed only for transcribe*.py)
# ffmpeg + ffprobe must be on PATH; yt-dlp optional
```

Helper invocations:

```bash
python helpers/transcribe.py <video> [--num-speakers N] [--language en]   # ElevenLabs Scribe, cached per source
python helpers/transcribe_batch.py <videos_dir>                           # 4-worker parallel transcription
python helpers/pack_transcripts.py --edit-dir <dir>                       # transcripts/*.json -> takes_packed.md
python helpers/timeline_view.py <video> <start> <end> [-o out.png]        # filmstrip + waveform PNG
python helpers/render.py <edl.json> -o final.mp4 [--preview] [--build-subtitles]
python helpers/grade.py <in> -o <out> [--preset warm_cinematic | --filter '<raw ffmpeg>'] [--analyze <in>]
```

## Architecture

**Core idea: the LLM never watches the video — it reads it.** Two layers:

1. **Packed transcript** (`takes_packed.md`, always loaded): one ElevenLabs Scribe call per source gives word-level timestamps, diarization, and audio events. `pack_transcripts.py` groups words into phrase lines (breaking on silence ≥ 0.5s or speaker change), each prefixed `[start-end]`. This is the primary artifact for choosing cuts.
2. **Visual composite** (on demand): `timeline_view.py` renders filmstrip + waveform + word labels for a specific range. Used only at decision points, never in a scan loop.

**Pipeline:** Transcribe → Pack → LLM reasons → `edl.json` → Render → Self-eval (fix + re-render, max 3 passes).

**Render pipeline order** (`render.py`) is load-bearing and encodes several Hard Rules:

1. Per-segment extract with color grade + 30ms audio fades baked in (fades prevent pops at cuts)
2. Lossless `-c copy` concat into `base.mp4` (avoids double-encoding when overlays are added)
3. If overlays/subtitles: one filter graph — overlays use `setpts=PTS-STARTPTS+T/TB` so frame 0 lands at the window start, and the `subtitles` filter is applied **LAST** so overlays never hide captions

The master SRT uses output-timeline offsets (`word.start - segment_start + segment_offset`), computed against the concatenated timeline, not source timestamps.

`render.py` imports `get_preset` / `auto_grade_for_clip` from `grade.py` in the same directory (with fallbacks if the import fails) — keep those function signatures compatible. `grade.py` defaults to auto mode: mathematical per-clip correction capped at ±8% per axis, no creative shifts; creative looks require an explicit preset or raw filter.

**Session outputs** all live in `<videos_dir>/edit/` next to the user's footage — `project.md` (session memory), `takes_packed.md`, `edl.json`, `transcripts/`, `animations/slot_<id>/`, `clips_graded/`, `master.srt`, `preview.mp4`, `final.mp4`. Nothing is ever written inside the video-use repo during an editing session.

## Key conventions

- **The 12 Hard Rules in `SKILL.md` are correctness, not taste.** Any change to a helper must preserve them: subtitles last, per-segment extract + `-c copy` concat, 30ms fades, PTS-shifted overlays, output-timeline SRT offsets, cuts on word boundaries with 30–200ms padding, word-level verbatim ASR only (never SRT/phrase mode, never normalized fillers), transcript caching (never re-transcribe unchanged sources), parallel sub-agents for animations, strategy confirmation before executing, all outputs in `edit/`.
- Everything in `SKILL.md` outside the Hard Rules is explicitly a *worked example*, not a mandate — preserve that framing when editing the doc (don't turn examples into requirements).
- Transcription helpers cache by output path: if `transcripts/<stem>.json` exists, the upload is skipped. Preserve this idempotency in any changes.
- `.env` (API key) lives at the repo root and is gitignored; helpers resolve `ELEVENLABS_API_KEY` from the environment or that file.
- The `SKILL.md` anti-patterns section lists approaches that were tried and rejected (pre-computed shot codecs, moment-scoring heuristics, local Whisper, single-pass filtergraphs, linear easing) — don't reintroduce them.
