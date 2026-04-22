# Entrepreneurship Wrapper

This wrapper set runs `Video2Book` against the `Entrepreneurship` playlist inside a host repo such as `LazyEarn`.

It customizes:

- the playlist URL
- a dedicated download subdirectory
- a dedicated transcript subtree
- tmux session names for transcription
- a strict 55-lecture unique-video note-writing order
- a dynamic thematic entrepreneurship book
- a 1.2x pocket-size export after the capped unique-note run

Expected host-repo usage from the host repo root:

```bash
./Video2Book/examples/lazyearn/entrepreneurship/download_playlist.sh
./Video2Book/examples/lazyearn/entrepreneurship/start_transcription_tmux.sh
./Video2Book/examples/lazyearn/entrepreneurship/start_transcription_monitor_tmux.sh
```

## Unique Notes Run

The playlist contains many items that are duplicated by earlier LazyEarn School
of Hard Knocks playlists. The course config therefore uses:

- `lecture_order_strict: true`
- a curated `lecture_order` containing the 55 unique Entrepreneurship videos
- `dynamic_book_enabled: true`

The order is not raw playlist order. It is arranged as a smoother book arc:

- business basics and ownership
- founder psychology and life design
- sales, media, and attention
- risk, capital, real estate, and online opportunity
- operations, leadership, and company judgment
- culture, industries, and case-study material

Start the capped unique run and final 1.2x pocket export:

```bash
./Video2Book/examples/lazyearn/entrepreneurship/start_unique_notes_pocket_tmux.sh --no-attach
```

For a normal notes-only run:

```bash
./Video2Book/examples/lazyearn/entrepreneurship/start_course_notes_tmux.sh --no-attach
./Video2Book/examples/lazyearn/entrepreneurship/start_course_notes_monitor_tmux.sh --no-attach
```
