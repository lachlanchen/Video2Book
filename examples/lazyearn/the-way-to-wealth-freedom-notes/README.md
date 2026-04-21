# LazyEarn: The Way To Wealth Freedom Notes

This example adapts `Video2Book` for a non-video source: an ordered Markdown
material corpus under a host repo's `materials/` directory.

Default host source:

- `materials/the-way-to-wealth-freedom-notes`

Default generated output:

- `generated_course_notes/lazyearn/the-way-to-wealth-freedom-notes/course.tex`
- `generated_course_notes/lazyearn/the-way-to-wealth-freedom-notes/course_pocket_1_2x.pdf`

Run from the host repo root:

```bash
./Video2Book/examples/lazyearn/the-way-to-wealth-freedom-notes/start_material_book_tmux.sh --no-attach
```

The writer processes source markdown files one by one. Each prompt still points
Codex to the complete `SUMMARY.md`, source `README.md`, generated
`source_manifest.tsv`, `book_plan.md`, and existing generated chapters so the
current chapter keeps the whole book arc in mind.

The canonical TeX is generated as a 6x9 pocket book with 1.2x typography by
default.
