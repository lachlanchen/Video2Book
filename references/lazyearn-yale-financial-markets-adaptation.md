# LazyEarn Yale Financial Markets Adaptation

This note documents the `Video2Book` adaptation used to run a course pipeline inside `LazyEarn`, using Yale's `Financial Markets` course as the concrete example.

## Goal

Keep the `Video2Book` core reusable while letting a host repo:

- define a course as a self-contained wrapper
- download a playlist into a stable repo-local subdirectory
- keep transcripts and generated notes under course-relative paths
- run transcription and note generation in `tmux`
- customize lecturer credit and note-writing metadata without forking the core scripts

## What Was Added

### 1. Repo-local playlist download subdirectories

Updated:

- `playlist2videos/download_playlist.py`

New behavior:

- supports `--download-subdir`
- writes the downloaded playlist under a caller-selected subdirectory instead of always using the raw playlist ID

Why:

- `LazyEarn` keeps multiple long-running research and media pipelines in one repo
- the Yale course needed a stable host-relative media path:
  - `downloads/lazyearn/yale-financial-markets/`

### 2. LazyEarn example wrapper family

New example tree:

- `examples/lazyearn/`
- `examples/lazyearn/common.sh`
- `examples/lazyearn/yale-financial-markets/`

The Yale example contains:

- `course.env`
  - names the course namespace and slug
  - defines tmux session names
  - defines model defaults
- `course.json`
  - customizes course title, descriptor, lecturer credit, and notes tone
- `download_playlist.sh`
  - runs the shared playlist downloader with the Yale playlist URL and the LazyEarn download subdirectory
- `start_transcription_tmux.sh`
- `start_transcription_monitor_tmux.sh`
- `start_course_notes_tmux.sh`
- `start_course_notes_monitor_tmux.sh`

This provides the same host-wrapper pattern as the `LazyLearn` example, but for a playlist-backed course instead of a hand-curated video list.

## Course Layout

The `LazyEarn` adaptation uses a course-relative path:

- `lazyearn/yale-financial-markets`

That course-relative path is used consistently in:

- downloads:
  - `downloads/lazyearn/yale-financial-markets/`
- subtitles:
  - `subtitles/lazyearn/yale-financial-markets/`
- transcript markdown:
  - `markdown/lazyearn/yale-financial-markets/`
- generated notes:
  - `generated_course_notes/lazyearn/yale-financial-markets/`

Why this matters:

- transcript scanning stays scoped to the intended course
- generated lecture PDFs and merged course books stay deterministic
- host repos can keep multiple courses without cross-contaminating queues

## Shared Core Changes Used By LazyEarn

### 1. Scoped transcript scanning

Updated:

- `videos2subtitles/transcribe_video.py`
- `scripts/process_videos_one_by_one.sh`
- `scripts/start_transcription_tmux.sh`
- `scripts/start_transcription_monitor_tmux.sh`
- `scripts/monitor_transcription.sh`

New behavior:

- supports `SOURCE_SUBDIR`
- lets the transcription queue scan only one course subtree under a larger `downloads/` root

Why:

- `LazyEarn` stores other downloaded media in the same repo
- the Yale wrapper needed the worker to stay inside `downloads/lazyearn/yale-financial-markets/`

### 2. Scoped transcript commits

Updated:

- `scripts/process_videos_one_by_one.sh`

New behavior:

- supports `TRANSCRIPTION_GIT_PATHS`
- the transcription queue can `git add` only selected output paths

For the Yale wrapper this is set to:

- `subtitles/lazyearn/yale-financial-markets`
- `markdown/lazyearn/yale-financial-markets`

Why:

- avoids staging unrelated transcript trees in the host repo

### 3. Course-specific note metadata

Updated:

- `subtitles2notes/generate_course_notes.py`

New behavior:

- accepts course config metadata from JSON
- overrides default lecturer and descriptor values
- keeps LazyingArt LLC curation credit while swapping course-specific lecturer attribution

Why:

- Yale `Financial Markets` should credit Robert J. Shiller, not the older Susskind defaults

### 4. Course-note tmux env propagation

Updated:

- `scripts/start_course_notes_tmux.sh`
- `scripts/start_course_notes_monitor_tmux.sh`

New behavior:

- forwards `NOTE_TMUX_SESSION_NAME`
- forwards `NOTE_CODEX_SESSION_FILE`
- forwards `NOTE_CODEX_SESSION_DOC_FILE`
- forwards course config and reference-pdf env vars into the tmux shell

Why:

- each course wrapper needs isolated note-session tracking instead of reusing generic session metadata files

### 5. Prompt-path fix for note generation

Updated:

- `scripts/process_course_notes_one_by_one.sh`

New behavior:

- resolves the note prompt relative to the script location instead of assuming a host-repo path

Why:

- wrapper-driven note generation should work from host repos without copying prompt templates out of `Video2Book`

## Host-Repo Outcome in LazyEarn

Inside `LazyEarn`, the Yale pipeline now supports:

- ignored repo-local downloads under `downloads/`
- tracked transcripts under `markdown/lazyearn/yale-financial-markets/`
- tracked subtitles under `subtitles/lazyearn/yale-financial-markets/`
- generated note books under `generated_course_notes/lazyearn/yale-financial-markets/`
- tmux-managed note writing with dedicated session names

The tracked transcript tree was also reorganized so the course-specific path, transcript `Source:` lines, and generated-note inputs all agree.

## Example Usage From `LazyEarn`

From the host repo root:

```bash
./Video2Book/examples/lazyearn/yale-financial-markets/download_playlist.sh
./Video2Book/examples/lazyearn/yale-financial-markets/start_transcription_tmux.sh
./Video2Book/examples/lazyearn/yale-financial-markets/start_transcription_monitor_tmux.sh
./Video2Book/examples/lazyearn/yale-financial-markets/start_course_notes_tmux.sh
./Video2Book/examples/lazyearn/yale-financial-markets/start_course_notes_monitor_tmux.sh
```

## Naming

Current course/book name:

- `Yale Financial Markets`

Current course path:

- `lazyearn/yale-financial-markets`

This is the name used by the wrapper set, the transcript tree, and the generated-note tree.

## Design Outcome

The `LazyEarn` adaptation keeps the `Video2Book` core generic while adding a concrete reusable pattern for:

- playlist-backed course ingestion
- repo-local media subdirectories
- course-relative transcript trees
- per-course note-generation metadata
- tmux-managed long-running queues
- host-repo-specific thin wrappers without hardcoding `LazyEarn` into the pipeline core
