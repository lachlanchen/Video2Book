# 10 Questions with a Millionaire Wrapper

This wrapper set runs `Video2Book` against the `10 Questions with a Millionaire` playlist inside a host repo such as `LazyEarn`.

It customizes:

- the playlist URL
- a dedicated download subdirectory
- a dedicated transcript subtree
- tmux session names for transcription

Expected host-repo usage from the host repo root:

```bash
./Video2Book/examples/lazyearn/ten-questions-with-a-millionaire/download_playlist.sh
./Video2Book/examples/lazyearn/ten-questions-with-a-millionaire/start_transcription_tmux.sh
./Video2Book/examples/lazyearn/ten-questions-with-a-millionaire/start_transcription_monitor_tmux.sh
```
