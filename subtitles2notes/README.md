# subtitles2notes

This module handles the third stage of the pipeline: turning completed subtitle and Markdown transcript trees into lecture-note source, lecture PDFs, and merged course PDFs.

## What it does

- Reads transcript inputs from a host archive repo:
  - `markdown/`
  - `subtitles/`
- Writes generated note outputs back into that host repo:
  - `generated_course_notes/`
  - `.lecture-notes-work/`
- Uses the current Codex-driven workflow for:
  - chapter analysis
  - figure extraction and validation
  - equation and diagram interpretation
  - chapter drafting and refinement
  - LaTeX compile-fix passes
  - per-step commit and push
- Audits and revises existing books for:
  - transcript and blackboard fidelity
  - AI-shaped prose and internal process leakage
  - verified classroom Q&A and timestamp provenance
  - figure relevance, source maps, and clean front matter

## Main entrypoints

- Note generator:
  - [generate_course_notes.py](/home/lachlan/ProjectsLFS/Video2Book/subtitles2notes/generate_course_notes.py)
- Editorial auditor and reviser:
  - [editorial_revision.py](/home/lachlan/ProjectsLFS/Video2Book/subtitles2notes/editorial_revision.py)
- Queue runner:
  - [process_course_notes_one_by_one.sh](/home/lachlan/ProjectsLFS/Video2Book/scripts/process_course_notes_one_by_one.sh)
- tmux launcher:
  - [start_course_notes_tmux.sh](/home/lachlan/ProjectsLFS/Video2Book/scripts/start_course_notes_tmux.sh)
  - [start_editorial_revision_tmux.sh](/home/lachlan/ProjectsLFS/Video2Book/scripts/start_editorial_revision_tmux.sh)
- monitor / guard:
  - [monitor_course_notes.sh](/home/lachlan/ProjectsLFS/Video2Book/scripts/monitor_course_notes.sh)
  - [start_course_notes_monitor_tmux.sh](/home/lachlan/ProjectsLFS/Video2Book/scripts/start_course_notes_monitor_tmux.sh)
- Codex helpers:
  - [codex_prompt_to_file.sh](/home/lachlan/ProjectsLFS/Video2Book/scripts/codex_prompt_to_file.sh)
  - [codex_commit_push.sh](/home/lachlan/ProjectsLFS/Video2Book/scripts/codex_commit_push.sh)

## Support assets

- prompts:
  - [prompts/lecture_notes](/home/lachlan/ProjectsLFS/Video2Book/subtitles2notes/prompts/lecture_notes)
- common preamble:
  - [lecture_notes_common_preamble.tex](/home/lachlan/ProjectsLFS/Video2Book/subtitles2notes/templates/lecture_notes_common_preamble.tex)

## Typical usage

From the archive repo root:

```bash
./Video2Book/scripts/start_course_notes_tmux.sh
./Video2Book/scripts/start_course_notes_monitor_tmux.sh
```

Or through thin wrappers in `leonardsusskind/scripts/`.

For a source-aware rewrite of an existing course:

```bash
./Video2Book/scripts/start_editorial_revision_tmux.sh \
  --course core/cosmology/2009_winter_legacy_cosmology \
  --reference core_cosmology \
  --model gpt-5.4 \
  --reasoning xhigh
```

See [the editorial revision handoff](../references/editorial-revision-workflow.md) for the provenance schema, acceptance gates, and resumable session behavior.
