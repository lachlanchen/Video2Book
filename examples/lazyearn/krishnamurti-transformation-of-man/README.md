# Krishnamurti - The Transformation of Man Wrapper

This wrapper set runs `Video2Book` against the official Krishnamurti Foundation Trust playlist `The transformation of man` inside a host repo such as `LazyEarn`.

It customizes:

- the playlist URL
- a dedicated download subdirectory
- a dedicated transcript subtree
- tmux session names for download and follow-mode transcription
- future course metadata for later book generation

Expected host-repo usage from the host repo root:

```bash
./Video2Book/examples/lazyearn/krishnamurti-transformation-of-man/download_playlist.sh
./Video2Book/examples/lazyearn/krishnamurti-transformation-of-man/start_transcription_follow_tmux.sh
```
