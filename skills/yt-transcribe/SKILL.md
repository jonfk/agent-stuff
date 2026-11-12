---
name: yt-transcribe
description: transcribe youtube videos by extracting existing captions or subtitles with a bundled yt-dlp based script. use when the user provides a youtube url and wants a transcript.
---

Use the bundled script to create cleaned Markdown transcripts from YouTube captions/subtitles.

## Workflow

1. Get a YouTube video URL from the user.
2. Run:

```bash
uv run --script ./scripts/yt-transcript.py "<youtube-url>"
```

3. Return or link the generated `.md` transcript file.

## Options

- Save to a specific path:

```bash
uv run --script ./scripts/yt-transcript.py -o transcript.md "<youtube-url>"
```

- Also keep the raw VTT subtitle file:

```bash
uv run --script ./scripts/yt-transcript.py --subtitle -o transcript.md "<youtube-url>"
```

## Notes

- `./scripts/` is relative to this skill's directory, not the user's working directory.
- Requires `uv` to run the script. Do not call it with `python`, which may not exist on the host.
- Uses `yt-dlp` from PATH when installed, otherwise falls back to running it through `uvx`. If the script exits 127, neither is available: tell the user to install yt-dlp or uv.
- Caption priority is fixed by the script: English official, English auto, French official, French auto, any official, any auto. Within each auto group, `<lang>-orig` (the source-language track) is tried before machine-translated tracks, which YouTube often rate-limits with HTTP 429.
- If one candidate fails (for example with a 429), the script tries the next one and gives up after 3 failures.
- If no captions/subtitles are available, report that the skill cannot transcribe that video because it does not include captions.
- Do not claim to transcribe audio. This skill extracts existing captions only.
- Only works for videos that already have official or automatic captions; it does not perform speech-to-text or audio transcription.
