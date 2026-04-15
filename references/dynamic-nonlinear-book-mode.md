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

The dynamic manuscript is rewritten after each processed lecture using:

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
2. update a course-level memory file that synthesizes the whole processed series into thematic evidence, chapter candidates, frame ideas, and diagram ideas
3. rewrite one separate dynamic book from that course memory plus the accumulated manuscript

This keeps the lecture-by-lecture artifacts intact while the book itself stays nonlinear and series-level.
