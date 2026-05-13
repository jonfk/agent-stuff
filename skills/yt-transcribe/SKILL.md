---
name: yt-transcript
description: transcribe youtube videos by extracting existing captions or subtitles with a bundled yt-dlp based script. use when the user provides a youtube url and wants a transcript.
---

Use the bundled script to create cleaned Markdown transcripts from YouTube captions/subtitles.

## Workflow

1. Get a YouTube video URL from the user.
2. Run:

```bash
python ./scripts/yt-transcript.py "<youtube-url>"
```

3. Return or link the generated `.md` transcript file.

## Options

- Save to a specific path:

```bash
python ./scripts/yt-transcript.py -o transcript.md "<youtube-url>"
```

- Also keep the raw VTT subtitle file:

```bash
python ./scripts/yt-transcript.py --subtitle -o transcript.md "<youtube-url>"
```

## Notes

- Requires `yt-dlp` in PATH.
- Requires uv to run the script
- Caption priority is fixed by the script: English official, English auto, French official, French auto, any official, any auto.
- If no captions/subtitles are available, report that the skill cannot transcribe that video because it does not include captions.
- Do not claim to transcribe audio. This skill extracts existing captions only.
- Only works for videos that already have official or automatic captions; it does not perform speech-to-text or audio transcription.
