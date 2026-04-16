# Dynamic nonlinear book mode

`Video2Book` now has a dynamic book path inside the course-notes generator for courses that should become a real book instead of a lecture-by-lecture shell.

## Goal

Keep the standard lecture-note pipeline, including:

- transcript-to-notes generation
- frame extraction
- figure handling
- chapter TeX generation
- lecture PDF generation

But also maintain a second evolving manuscript that:

- is not one chapter per video
- revises earlier chapters when later interviews sharpen the thesis
- keeps thematic chapters instead of lecture order
- stays vivid, source-conscious, and consistent

## How it is enabled

Set these fields in a course config JSON:

- `dynamic_book_enabled`
- `dynamic_book_title`
- `dynamic_book_descriptor`
- `dynamic_book_target`
- `dynamic_book_style_target`
- `dynamic_book_structure_target`

## What it writes

Inside the generated course root:

- `dynamic_book/<book-slug>.tex`
- `dynamic_book/<book-slug>.pdf`

The dynamic manuscript is fed after each processed lecture using:

- the current lecture chapter
- analysis / narrative / visual / math notes
- extracted frame inventory
- the existing dynamic manuscript
- the set of already processed lectures
- the full transcript directory for the course
- the accumulated course-notes/output directory for the course

## Why this exists

Some playlists are better turned into a thematic field book than a linear transcript book.

The first target for this mode is:

- `examples/lazyearn/hard-knocks-interviews/`
- dynamic book title: `How You Got Rich?`

The intended control flow is:

1. process one lecture normally into lecture-specific notes, frames, and chapter TeX
2. append a course-level memory block that records only what this lecture adds to the whole-series map
3. append one separate dynamic-book fragment into the existing manuscript

This keeps the lecture-by-lecture artifacts intact while the book itself stays nonlinear and series-level.

## First-principles append logic

The dynamic-book path is now intentionally simple:

1. the current dynamic book is the canonical book
2. a prompt reads the current lecture plus the current book
3. the prompt writes only the new LaTeX fragment for this lecture
4. the code inserts that fragment before `\end{document}`
5. the book is compiled

The same pattern is used for `course_memory.md`:

- the current memory file is canonical
- the prompt writes only the new Markdown block for this lecture
- the code appends that block if it is not empty

This keeps the logic close to the actual intent: each lecture feeds the current book and memory forward.

## Replay

`scripts/rerun_dynamic_book.py` follows the same lecture-by-lecture append logic.

- normal replay keeps the current dynamic book and appends lecture deltas into it
- `--clean-start` backs up the current dynamic book and rebuilds it from lecture 1 through the requested cutoff using the same incremental append path
