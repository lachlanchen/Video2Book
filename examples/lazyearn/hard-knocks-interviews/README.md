# Hard Knocks Interviews Wrapper

This wrapper set runs `Video2Book` against the `Hard Knocks Interviews` playlist inside a host repo such as `LazyEarn`.

It customizes:

- the playlist URL
- a dedicated download subdirectory
- a dedicated transcript subtree
- tmux session names for transcription
- tmux session names for course-note writing
- a dynamic nonlinear book mode for the evolving book `How Did You Get Rich?`

Expected host-repo usage from the host repo root:

```bash
./Video2Book/examples/lazyearn/hard-knocks-interviews/download_playlist.sh
./Video2Book/examples/lazyearn/hard-knocks-interviews/start_transcription_tmux.sh
./Video2Book/examples/lazyearn/hard-knocks-interviews/start_transcription_monitor_tmux.sh
./Video2Book/examples/lazyearn/hard-knocks-interviews/start_course_notes_tmux.sh
./Video2Book/examples/lazyearn/hard-knocks-interviews/start_course_notes_monitor_tmux.sh
```
