# LazyEarn Wrappers

This folder stores host-repo wrappers for running `Video2Book` inside `LazyEarn`.

Pattern:

- one folder per course
- a small shell config for paths and tmux session names
- a small JSON course config for speaker metadata and notes tone
- thin wrappers that call the shared `Video2Book/scripts/*` entrypoints with the right environment

The intent is to keep the pipeline core generic while letting each course customize:

- playlist URL
- download path
- course path under `markdown/` and `subtitles/`
- lecturer credits in generated books
- notes-writing defaults
- optional dedupe sources for sequential playlist ingestion

Current example:

- `yale-financial-markets/`
- `hard-knocks-interviews/`
- `ten-questions-with-a-millionaire/`
- `entrepreneurship/`

All `lazyearn` wrappers now default to:

- a per-course `downloads/` subdirectory
- a per-course `SOURCE_SUBDIR` for transcription scans
- per-course `git add` paths for `subtitles/` and `markdown/`

Sequential playlist feature:

- future wrappers can declare `DEDUP_SOURCE_SUBDIRS=(...)` in `course.env`
- the shared downloader will pre-link duplicate videos from those earlier playlist folders before yt-dlp starts
- the same duplicate IDs are also written into the target playlist archive file so yt-dlp skips re-downloading them
