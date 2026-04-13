# LazyLearn Wrappers

This folder stores host-repo wrappers for running `Video2Book` inside `LazyLearn`.

Pattern:

- one folder per course
- a small shell config for paths and tmux session names
- a small JSON course config for book metadata and notes tone
- thin wrappers that call the shared `Video2Book/scripts/*` entrypoints with the right environment

The intent is to keep the pipeline core generic while letting each course customize:

- playlist URL or ordered URL list
- download path
- course path under `markdown/` and `subtitles/`
- book metadata in generated notes
- notes-writing defaults

Current example:

- `how-you-speak-and-write/`
