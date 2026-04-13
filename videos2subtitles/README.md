# videos2subtitles

This module handles the second stage of the pipeline: turning the downloaded lecture archive into subtitles and timestamped Markdown transcripts.

## What it does

- Reads source media from the external organized playlist tree.
- Writes repo-local outputs into:
  - `subtitles/`
  - `markdown/`
- Preserves the source folder structure in both output trees.
- Uses `whisper_with_lang_detect` first and retries with direct Whisper if the primary path fails or produces empty outputs.

## Main entrypoints

- Single-file transcriber:
  - [transcribe_video.py](/home/lachlan/ProjectsLFS/Video2Book/videos2subtitles/transcribe_video.py)
- Direct Whisper fallback:
  - [fallback_whisper_transcribe.py](/home/lachlan/ProjectsLFS/Video2Book/videos2subtitles/fallback_whisper_transcribe.py)
- Queue runner:
  - [process_videos_one_by_one.sh](/home/lachlan/ProjectsLFS/Video2Book/scripts/process_videos_one_by_one.sh)
- tmux launcher:
  - [start_transcription_tmux.sh](/home/lachlan/ProjectsLFS/Video2Book/scripts/start_transcription_tmux.sh)
- monitor / guard:
  - [monitor_transcription.sh](/home/lachlan/ProjectsLFS/Video2Book/scripts/monitor_transcription.sh)
  - [start_transcription_monitor_tmux.sh](/home/lachlan/ProjectsLFS/Video2Book/scripts/start_transcription_monitor_tmux.sh)

## Typical usage

From the archive repo root:

```bash
./Video2Book/scripts/start_transcription_tmux.sh
./Video2Book/scripts/start_transcription_monitor_tmux.sh
```

Or through thin wrappers in `leonardsusskind/scripts/`.
