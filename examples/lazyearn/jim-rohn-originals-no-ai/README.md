# Jim Rohn - Originals - No Ai Wrapper

This wrapper set runs `Video2Book` against the `Jim Rohn - Originals - No Ai` playlist inside a host repo such as `LazyEarn`.

It customizes:

- the playlist URL
- a dedicated download subdirectory
- a dedicated transcript subtree
- tmux session names for transcription
- tmux session names for course-note writing
- a custom lecture order so the compiled book reads more smoothly than the raw playlist
- the lecture-by-lecture book title `How You Got Successful?`

Expected host-repo usage from the host repo root:

```bash
./Video2Book/examples/lazyearn/jim-rohn-originals-no-ai/download_playlist.sh
./Video2Book/examples/lazyearn/jim-rohn-originals-no-ai/start_transcription_tmux.sh
./Video2Book/examples/lazyearn/jim-rohn-originals-no-ai/start_transcription_monitor_tmux.sh
./Video2Book/examples/lazyearn/jim-rohn-originals-no-ai/start_transcription_follow_tmux.sh
./Video2Book/examples/lazyearn/jim-rohn-originals-no-ai/start_course_notes_tmux.sh
./Video2Book/examples/lazyearn/jim-rohn-originals-no-ai/start_course_notes_monitor_tmux.sh
```
