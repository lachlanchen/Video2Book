# LaTeX Overflow Fixer Handoff

Date: 2026-04-17

This note documents the Codex-driven overflow-fixing workflow that now lives in
`Video2Book`.

## Goal

The toolchain is designed to fix real, source-mapped LaTeX overfull warnings
without applying unsafe global hacks.

The workflow is:

1. compile a target variant
2. parse the LaTeX log
3. audit the rendered PDF for obvious formatting leaks
4. map actionable warnings back to source files and line numbers
5. ask Codex to patch only the first flagged source file, with the report and flagged PDF page images attached
6. recompile and measure whether the actionable count and audit issue count improved

That loop is intentionally conservative. It is meant to work across different
font sizes and page sizes, not just one Susskind pocket preset.

## Key Scripts

- `scripts/report_latex_overfulls.py`
  - parses a LaTeX log and emits a Markdown report
  - dedupes repeated warnings across multiple `pdflatex` passes
  - separates source-mapped warnings from page-builder noise
- `scripts/audit_pocket_pdf.py`
  - inspects rendered pocket PDFs with `pdftotext -layout`
  - flags obvious TeX token leaks such as `ormalsize` / `ootnotesize`
  - emits a Markdown audit plus machine-readable JSON/page lists
- `scripts/fix_course_pocket_overfulls.sh`
  - Susskind-specific course fixer for `generated_course_notes/.../course.tex`
- `scripts/process_course_pocket_overflow_fixes_one_by_one.sh`
  - runs the Susskind course fixer one course at a time
- `scripts/start_pocket_overflow_fix_tmux.sh`
  - starts the queue in tmux
- `scripts/fix_latex_project_overfulls.sh`
  - generic entry point for any LaTeX project in any repo

## Default Model Policy

The intended unattended default is:

- model: `gpt-5.4`
- reasoning: `high`

That is the current preferred setting for pocket-size cleanup because the prompt
now receives richer context: the source-mapped overflow report, the rendered-PDF
audit, and screenshots of the flagged PDF pages.

## Why The Workflow Is Conservative

Blind global wrapping approaches were tested and rejected:

- automatic display-math rewriting
- broad “wrap everything” TeX patches
- aggressive global fit/resize logic

Those approaches either failed to reduce the real source-mapped warnings or made
them worse. The current workflow therefore edits locally and iteratively.

Preferred local fixes:

- split wide equations into `align`, `split`, or short displays
- move long inline math into display mode
- scale figures or TikZ to `\linewidth`
- shorten unbreakable captions or prose spans
- repair rendered typography artifacts exposed by the PDF audit

## Susskind Queue Usage

Run one specific course:

```bash
./scripts/start_pocket_overflow_fix_tmux.sh \
  --course core/statistical_mechanics/2013_spring_theoretical_minimum \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

Run all completed courses one by one:

```bash
./scripts/start_pocket_overflow_fix_tmux.sh \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

## Generic Project Usage

For another repo:

```bash
./scripts/fix_latex_project_overfulls.sh \
  --repo-root /path/to/repo \
  --project-root /path/to/repo/book \
  --main-tex main.tex \
  --model gpt-5.4 \
  --reasoning medium
```

If the project needs a custom build command, pass `--compile-command`.

## What To Review

After each run, review:

- the generated overflow report
- the patched source file
- the rebuilt PDF for visual regressions

Do not treat “zero warnings” as the only metric. The real target is better
layout without damaging the mathematical content or readability.

## Suggested Reading Order For Another Session

1. this file
2. `references/pocket-size-course-pdfs-handoff.md`
3. `scripts/report_latex_overfulls.py`
4. the relevant fixer script for the target repo
