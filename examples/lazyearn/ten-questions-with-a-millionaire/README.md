# 10 Questions with a Millionaire Wrapper

This wrapper set runs `Video2Book` against the `10 Questions with a Millionaire` playlist inside a host repo such as `LazyEarn`.

It customizes:

- the playlist URL
- a dedicated download subdirectory
- a dedicated transcript subtree
- tmux session names for transcription
- tmux session names for lecture-note and dynamic-book writing
- a dynamic-book spine organized by the union of recurring millionaire questions rather than by video order

Expected host-repo usage from the host repo root:

```bash
./Video2Book/examples/lazyearn/ten-questions-with-a-millionaire/download_playlist.sh
./Video2Book/examples/lazyearn/ten-questions-with-a-millionaire/start_transcription_tmux.sh
./Video2Book/examples/lazyearn/ten-questions-with-a-millionaire/start_transcription_monitor_tmux.sh
./Video2Book/examples/lazyearn/ten-questions-with-a-millionaire/start_course_notes_tmux.sh --no-attach
./Video2Book/examples/lazyearn/ten-questions-with-a-millionaire/start_course_notes_monitor_tmux.sh --no-attach
```

The dynamic book is titled `Ten Questions That Build Wealth`. It keeps a living
question spine across the 22 transcript/subtitle files and distributes each
lecture into the best-fitting question chapter instead of creating one chapter
per video.
