# How You Speak and Write Wrapper

This wrapper set runs `Video2Book` against the curated `How You Speak and Write` video set inside a host repo such as `LazyLearn`.

It customizes:

- an ordered list of video URLs instead of a single playlist
- nested download and transcript paths under `lazylearn/how-you-speak-and-write`
- tmux session names
- notes metadata for a curated multi-speaker writing and speaking book

Expected host-repo usage from the host repo root:

```bash
./Video2Book/examples/lazylearn/how-you-speak-and-write/download_videos.sh
./Video2Book/examples/lazylearn/how-you-speak-and-write/start_transcription_tmux.sh
./Video2Book/examples/lazylearn/how-you-speak-and-write/start_transcription_monitor_tmux.sh
./Video2Book/examples/lazylearn/how-you-speak-and-write/start_course_notes_tmux.sh
./Video2Book/examples/lazylearn/how-you-speak-and-write/start_course_notes_monitor_tmux.sh
```
