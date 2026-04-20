# MIT 15.393 Nuts and Bolts of New Ventures Wrapper

This wrapper set runs the `Video2Book` notes pipeline against the MIT OpenCourseWare playlist `15.393 Nuts and Bolts of New Ventures` inside a host repo such as `LazyEarn`.

It customizes:

- the MIT course transcript subtree
- dedicated tmux session names for notes writing
- the lecture-by-lecture book title `Nuts and Bolts of New Ventures`
- course-specific note-writing guidance for venture formation, customer discovery, business models, legal structure, negotiation, and financial projections

Expected host-repo usage from the host repo root:

```bash
./Video2Book/examples/lazyearn/mit-nuts-and-bolts-of-new-ventures/start_course_notes_tmux.sh
./Video2Book/examples/lazyearn/mit-nuts-and-bolts-of-new-ventures/start_course_notes_monitor_tmux.sh
```
