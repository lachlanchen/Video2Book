# LazyLearn Course Adaptation

This note documents the `Video2Book` adaptation used to run a course pipeline inside `LazyLearn`, using `How You Speak and Write` as the concrete example.

## Goal

Keep the `Video2Book` core reusable while letting a host repo:

- define one course as a self-contained wrapper
- download either a playlist or an ordered list of individual video URLs
- keep course assets under stable repo-local paths
- run transcription and note generation in `tmux`
- commit only the course-specific outputs instead of sweeping unrelated transcript trees

## What Was Added

### 1. Ordered video-list downloading

New tool:

- `playlist2videos/download_video_list.py`

Why:

- `download_playlist.py` is correct for playlist URLs
- `LazyLearn` needed a curated course assembled from individual YouTube links, not one playlist

Behavior:

- reads one URL per line from a text file
- downloads in the declared order
- prefixes filenames with stable numeric indices
- reuses a shared archive file so repeated URLs are skipped
- writes logs under the configured log root

### 2. LazyLearn example wrapper family

New example tree:

- `examples/lazylearn/`
- `examples/lazylearn/common.sh`
- `examples/lazylearn/how-you-speak-and-write/`

The course example contains:

- `course.env`
  - names the course namespace and slug
  - defines tmux session names
  - defines model defaults
- `course.json`
  - customizes course title, descriptor, lecturer credit, front matter, and notes tone
- `urls.txt`
  - the ordered video list
- `download_videos.sh`
  - uses `download_video_list.py`
- `start_transcription_tmux.sh`
- `start_transcription_monitor_tmux.sh`
- `start_course_notes_tmux.sh`
- `start_course_notes_monitor_tmux.sh`

This follows the same pattern as `examples/lazyearn/`, but for `LazyLearn`.

## Course Layout

The `LazyLearn` adaptation uses a course-relative path:

- `lazylearn/how-you-speak-and-write`

That course-relative path is used consistently in:

- downloads:
  - `downloads/lazylearn/how-you-speak-and-write/`
- subtitles:
  - `subtitles/lazylearn/how-you-speak-and-write/`
- transcript markdown:
  - `markdown/lazylearn/how-you-speak-and-write/`
- generated notes:
  - `generated_course_notes/lazylearn/how-you-speak-and-write/`

Why this matters:

- `subtitles2notes/generate_course_notes.py` expects transcript material to live in per-course subdirectories
- course-relative paths make chapter-by-chapter and per-course PDF generation deterministic

## Shared Core Changes

### 1. Scoped transcript scanning

Updated:

- `videos2subtitles/transcribe_video.py`
- `scripts/process_videos_one_by_one.sh`
- `scripts/start_transcription_tmux.sh`
- `scripts/start_transcription_monitor_tmux.sh`
- `scripts/monitor_transcription.sh`

New behavior:

- supports `SOURCE_SUBDIR`
- lets the worker scan only one course subtree under a larger `downloads/` root

Why:

- `LazyLearn` already had other downloaded videos in `downloads/`
- without a subdir filter, the queue could pick unrelated files first

### 2. Scoped transcript commits

Updated:

- `scripts/process_videos_one_by_one.sh`

New behavior:

- supports `TRANSCRIPTION_GIT_PATHS`
- the transcription queue can `git add` only selected output paths

For the example course this is set to:

- `subtitles/lazylearn/how-you-speak-and-write`
- `markdown/lazylearn/how-you-speak-and-write`

Why:

- avoids staging unrelated `markdown/` or `subtitles/` content in the host repo

### 3. Course-note tmux env propagation

Updated:

- `scripts/start_course_notes_tmux.sh`
- `scripts/start_course_notes_monitor_tmux.sh`

New behavior:

- forwards `NOTE_TMUX_SESSION_NAME`
- forwards `NOTE_CODEX_SESSION_FILE`
- forwards `NOTE_CODEX_SESSION_DOC_FILE`
- forwards course config and reference-pdf env vars into the tmux shell

Why:

- without this, the note queue fell back to the older `susskind-notes` session metadata defaults
- the `LazyLearn` course needs its own session tracking files

## Host-Repo Thin Wrappers

Inside `LazyLearn`, thin wrappers were added under:

- `scripts/how-you-speak-and-write/`

These simply:

- set `HOST_REPO_ROOT`
- delegate into the matching `Video2Book/examples/lazylearn/how-you-speak-and-write/` script

This keeps the host repo ergonomic while preserving the reusable logic in `Video2Book`.

## Migration of Existing Assets

Host helper:

- `scripts/how-you-speak-and-write/migrate_existing_assets.sh`

Purpose:

- move already-downloaded videos from the older flat folder into the course-relative folder
- move already-generated `.srt` and transcript Markdown files into course-relative output trees
- rewrite each transcript `Source:` line so it points at the new course-relative video path

This made it possible to preserve the completed transcription work and immediately start chapter generation without retranscribing.

## Example Usage From `LazyLearn`

From the host repo root:

```bash
./scripts/how-you-speak-and-write/download_videos.sh
./scripts/how-you-speak-and-write/start_transcription_tmux.sh
./scripts/how-you-speak-and-write/start_transcription_monitor_tmux.sh
./scripts/how-you-speak-and-write/start_course_notes_tmux.sh
./scripts/how-you-speak-and-write/start_course_notes_monitor_tmux.sh
```

## Naming

Current course/book name:

- `How You Speak and Write`

Current course path:

- `lazylearn/how-you-speak-and-write`

This is the name used by the wrapper set, the transcript tree, and the generated-note tree.

## Design Outcome

The `LazyLearn` adaptation keeps the `Video2Book` core generic while adding a concrete reusable pattern for:

- non-playlist curated courses
- course-relative transcript trees
- per-course note-generation metadata
- tmux-managed long-running queues
- host-repo-specific thin wrappers without hardcoding `LazyLearn` into the shared pipeline core
