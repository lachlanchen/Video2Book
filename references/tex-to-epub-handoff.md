# EPUB Export Handoff (Video2Book + Susskind Notes)

Date: 2026-04-17

This note documents direct `.tex` → `.epub3` export from completed course LaTeX in
Video2Book pipelines.

## What Changed

- Added `scripts/export_course_epubs.sh`
- Added `.epub` pass directly from `course.tex` (no PDF rasterization step)
- Added optional Nutstore sync for EPUB outputs

## Scope

- input: `generated_course_notes/<scope>/<course>/course.tex`
- output: `all_notes/epub/<canonical-name>.epub` in host root
- optional sync: `/home/lachlan/Nutstore Files/Projects/LazyingArtBooks/epub`

## Files Added for Reuse

- `scripts/export_course_epubs.sh`
- this handoff document: `references/tex-to-epub-handoff.md`

## Why This Matters

Direct source export keeps source math structures and markdown section order closer
to the authored notes than PDF-based EPUB conversion.

## Recommended Workflow

From host repo root (example: `/home/lachlan/ProjectsLFS/leonardsusskind`):

```bash
cd /home/lachlan/ProjectsLFS/Video2Book
./scripts/export_course_epubs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
```

Optional dry run behavior by directory:

```bash
./scripts/export_course_epubs.sh \
  --host-root /home/lachlan/ProjectsLFS/leonardsusskind \
  --course core/classical_mechanics/2011_fall_theoretical_minimum
```

To avoid overwriting the synced distribution in one step:

```bash
./scripts/export_course_epubs.sh \
  --host-root /home/lachlan/ProjectsLFS/leonardsusskind \
  --no-rsync
```

## Naming Logic

`CANONICAL_OUTPUTS` maps known course paths to the publishing filenames used by
`all_notes` and website indexes.

- `core/classical_mechanics/2011_fall_theoretical_minimum` -> `classical_mechanics_theoretical_minimum.epub`
- `core/classical_mechanics/2011_fall_modern_physics_stanford_partial` -> `classical_mechanics_stanford_partial.epub`
- `core/cosmology/2009_winter_legacy_cosmology` -> `cosmology_legacy.epub`
- `core/general_relativity/2012_fall_theoretical_minimum` -> `general_relativity_theoretical_minimum.epub`
- `supplementary/cosmology_and_black_holes/...topics_in_string_theory` -> `topics_in_string_theory.epub`

Unknown paths fall back to `<subject>_<variant>.epub`.

## Success Criteria

- script exits `0`
- `epub_export.log` shows `completed exports=<n> failures=0`
- output `.epub` files exist at expected paths
- optional Nutstore sync completes without error

## Hand-Off for Another Codex Session

If another session continues the process, read:

1. `scripts/export_course_epubs.sh`
2. `references/tex-to-epub-handoff.md`
3. host repo README for book publish folders (`all_notes/epub`)

Then run the full export after course TeX finishes in `generated_course_notes`.
