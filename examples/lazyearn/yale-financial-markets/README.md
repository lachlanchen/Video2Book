# Yale Financial Markets Wrapper

This wrapper set runs `Video2Book` against the Yale `Financial Markets` playlist inside a host repo such as `LazyEarn`.

It customizes:

- playlist URL
- download subdirectory
- tmux session names
- notes metadata so generated books credit Robert J. Shiller instead of Leonard Susskind

Expected host-repo usage from the host repo root:

```bash
./Video2Book/examples/lazyearn/yale-financial-markets/download_playlist.sh
./Video2Book/examples/lazyearn/yale-financial-markets/start_transcription_tmux.sh
./Video2Book/examples/lazyearn/yale-financial-markets/start_transcription_monitor_tmux.sh
./Video2Book/examples/lazyearn/yale-financial-markets/start_course_notes_tmux.sh
./Video2Book/examples/lazyearn/yale-financial-markets/start_course_notes_monitor_tmux.sh
```
