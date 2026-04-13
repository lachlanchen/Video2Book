# Video2Book

`Video2Book` is a small toolkit for turning long-form video sources into durable study material.

## Components

- `playlist2videos/`
  - Download or refresh a full playlist into a stable on-disk archive.
  - Reuse an existing `yt-dlp` virtualenv when available.
  - Keep a download archive file so reruns only fetch missing videos.
  - Write timestamped logs for each run.
- `videos2subtitles/`
  - Transcribe the archived videos into timestamped Markdown and `.srt`.
  - Prefer `whisper_with_lang_detect`, then fall back to direct Whisper when needed.
  - Run lecture-by-lecture in tmux with GPU-memory guarding.
  - Optionally keep a monitor tmux session alive to restart the queue if it dies.

## Susskind workflow

The default wrapper in this repo targets the Leonard Susskind physics playlist:

- <https://www.youtube.com/playlist?list=PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG>

Use:

```bash
./scripts/download_susskind_playlist.sh
./scripts/start_transcription_tmux.sh
./scripts/start_transcription_monitor_tmux.sh
```

Dry run:

```bash
./scripts/download_susskind_playlist.sh --dry-run
```

The downloader keeps the media workspace outside this repo by default, so `Video2Book` stores code and documentation rather than large video files.
