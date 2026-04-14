# Leonardsusskind Wrappers

This folder stores host-repo wrappers for running `Video2Book` inside the Leonard Susskind archive workflow.

Pattern:

- one wrapper set for the full Susskind playlist archive
- shared shell defaults for playlist URL, downloader workspace, and tmux session names
- thin wrappers that call the generic `Video2Book/scripts/*` entrypoints with the same host-root environment that `leonardsusskind` already uses

This example is intentionally archive-wide rather than course-specific:

- download the full playlist
- transcribe the full archive into `subtitles/` and `markdown/`
- write notes course by course into `generated_course_notes/`

Current example:

- `susskind-physics-archive/`
