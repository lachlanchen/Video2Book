# Video2Book

`Video2Book` is a small toolkit for turning long-form video sources into durable study material. The first component in this repo is `playlist2videos`, a practical YouTube playlist downloader built around `yt-dlp`.

## Current component

- `playlist2videos/`
  - Download or refresh a full playlist into a stable on-disk archive.
  - Reuse an existing `yt-dlp` virtualenv when available.
  - Keep a download archive file so reruns only fetch missing videos.
  - Write timestamped logs for each run.

## Susskind workflow

The default wrapper in this repo targets the Leonard Susskind physics playlist:

- <https://www.youtube.com/playlist?list=PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG>

Use:

```bash
./scripts/download_susskind_playlist.sh
```

Dry run:

```bash
./scripts/download_susskind_playlist.sh --dry-run
```

The downloader keeps the media workspace outside this repo by default, so `Video2Book` stores code and documentation rather than large video files.
