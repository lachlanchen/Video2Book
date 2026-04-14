# Lazyearn Wrappers

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

Current example:

- `yale-financial-markets/`
- `hard-knocks-interviews/`
- `ten-questions-with-a-millionaire/`
- `entrepreneurship/`

All `lazyearn` wrappers now default to:

- a per-course `downloads/` subdirectory
- a per-course `SOURCE_SUBDIR` for transcription scans
- per-course `git add` paths for `subtitles/` and `markdown/`
