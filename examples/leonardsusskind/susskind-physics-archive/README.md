# Leonard Susskind Physics Archive Wrapper

This wrapper set runs `Video2Book` against the full Leonard Susskind playlist archive inside a host repo such as `leonardsusskind`.

It preserves the current archive-wide workflow:

- download the full playlist into the external media workspace
- transcribe the full archive into repo-local `subtitles/` and `markdown/`
- generate lecture notes and merged course books under `generated_course_notes/`

Expected host-repo usage from the host repo root:

```bash
./Video2Book/examples/leonardsusskind/susskind-physics-archive/download_playlist.sh
./Video2Book/examples/leonardsusskind/susskind-physics-archive/start_transcription_tmux.sh
./Video2Book/examples/leonardsusskind/susskind-physics-archive/start_transcription_monitor_tmux.sh
./Video2Book/examples/leonardsusskind/susskind-physics-archive/start_course_notes_tmux.sh
./Video2Book/examples/leonardsusskind/susskind-physics-archive/start_course_notes_monitor_tmux.sh
```
