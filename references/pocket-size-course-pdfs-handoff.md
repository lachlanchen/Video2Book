# Pocket-Format PDF Handoff (Video2Book + Leonard Susskind)

Date: 2026-04-17

This note documents the handoff flow for generating compact "pocket" PDFs after
course notes are fully authored.

Scope:

- input: `generated_course_notes/<scope>/<course>/course.tex` plus companion figures/assets
- output: compact PDFs such as `..._pocket.pdf`
- optional sync: local Nutstore folder used by LazyingArt publishing flow

## Files Added for Reuse

- `scripts/export_course_pocket_pdfs.sh`
- this handoff document: `references/pocket-size-course-pdfs-handoff.md`

## Why This Matters

The lecture-note pipeline writes large-format `course.pdf` and many per-lecture
PDFs. The pocket export pass creates a second production flavor suitable for:

- smaller-readability devices
- compact sharing
- book-style packaging with stable filenames

The implementation injects geometry options directly into `course.tex` at build
time (`\PassOptionsToPackage{paperwidth=...,paperheight=...,margin=...}{geometry}`),
runs `pdflatex` in an isolated temp copy, then moves the resulting compact PDF
to `pocket_books`.

## Defaults Used for Susskind Books

- preset: `penguin` (6x9 in, 0.55in margins)
- suffix: `pocket`
- default input root: `<host-root>/generated_course_notes`
- default output root: `<host-root>/all_notes/pocket_books` (fallback: `<host-root>/pocket_books`)
- logfile: `<output-dir>/pocket_export.log`
- sync target: `/home/lachlan/Nutstore Files/Projects/LazyingArtBooks/pocket_books`

## Recommended Running Sequence for a Host Repo

From host repo root (example: `/home/lachlan/ProjectsLFS/leonardsusskind`):

```bash
cd /home/lachlan/ProjectsLFS/Video2Book
./scripts/export_course_pocket_pdfs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
```

Optional:

```bash
# use A5-size for a different compact format
./scripts/export_course_pocket_pdfs.sh \
  --host-root /home/lachlan/ProjectsLFS/leonardsusskind \
  --size a5 \
  --suffix a5

# generate but only keep local files (no sync)
./scripts/export_course_pocket_pdfs.sh \
  --host-root /home/lachlan/ProjectsLFS/leonardsusskind \
  --no-rsync
```

## What to Capture in Handoff Logs

When sharing this to another model/session, include:

- `scripts/export_course_pocket_pdfs.sh` output
- location of generated PDFs
- commit that contains the run (`git rev-parse HEAD` in host and Video2Book)
- the final `pocket_export.log`

## Course Naming Logic (Susskind)

`course.tex` directories are mapped to canonical names for publishable outputs.

- `core/classical_mechanics/2011_fall_theoretical_minimum` -> `classical_mechanics_theoretical_minimum_pocket.pdf`
- `core/classical_mechanics/2011_fall_modern_physics_stanford_partial` -> `classical_mechanics_stanford_partial_pocket.pdf`
- `core/general_relativity/2012_fall_theoretical_minimum` -> `general_relativity_theoretical_minimum_pocket.pdf`
- `supplementary/cosmology_and_black_holes/...topics_in_string_theory` -> `topics_in_string_theory_pocket.pdf`

Unknown paths fall back to `<subject>_<variant>.pdf` with `_pocket` suffix.

## Success Criteria

- script exits `0`
- `pocket_export.log` shows `completed exports=<n> failures=0`
- output PDFs exist at expected paths
- optional sync completes without error

## Hand-Off for Another Codex Session

If another session continues this workflow, first read:

1. this file
2. `scripts/export_course_pocket_pdfs.sh`
3. host repo `README` section for generated notes/paths

Then run the pocket export command as part of post-note processing only after
completed `course.pdf` files exist for each target course.
