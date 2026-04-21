# README Book Preview Handoff

Date: 2026-04-21

This note documents the reusable README pattern now used in `Video2Book` for
showing published books near the top of the page with real first-page PDF
previews.

It exists so sibling host repos such as `LazyLearn` and `leonardsusskind` can
apply the same structure without re-deriving the asset layout or README markup.

## Goal

Show the strongest published books immediately when a reader opens the repo,
without making the README depend on generated HTML, screenshots from a browser,
or unstable external image hosts.

The working pattern is:

1. publish the canonical PDF in the host repo
2. extract page 1 of that PDF as `cover-page-1.png`
3. store that PNG under the repo's `docs/publications/<slug>/`
4. use a small top-of-README HTML table for flagship titles
5. keep the broader catalog in a compact Markdown table lower down

## Why This Pattern Was Chosen

This approach is better than plain PDF bullet links because:

- a reader sees the books immediately
- the preview is derived from the real PDF, not a separate mockup
- the preview stays consistent with the current publication cover
- the asset can be reused by the website and the README
- GitHub README rendering supports this small amount of inline HTML reliably

## Asset Convention

The current convention is:

- published PDF:
  - `docs/publications/<slug>/<book>.pdf`
- first-page preview:
  - `docs/publications/<slug>/cover-page-1.png`

For the current `LazyEarn` examples used by the `Video2Book` README:

- `docs/publications/wealth-from-first-principles/cover-page-1.png`
- `docs/publications/how-you-got-rich/cover-page-1.png`
- `docs/publications/how-you-got-successful/cover-page-1.png`
- `docs/publications/how-you-got-happiness/cover-page-1.png`

## How To Generate The Preview PNG

Use `pdftoppm` against the canonical published PDF:

```bash
mkdir -p docs/publications/<slug>
pdftoppm -f 1 -l 1 -png \
  path/to/book.pdf \
  docs/publications/<slug>/cover-page
```

In practice, `pdftoppm` will already write:

- `cover-page-1.png`

So the important part is the output prefix:

- `docs/publications/<slug>/cover-page`

That produces the stable file:

- `docs/publications/<slug>/cover-page-1.png`

## README Structure

The current pattern intentionally splits the book presentation into two layers.

### 1. Top flagship strip

Put this near the top of the README, after the short repository introduction and
before the longer implementation details.

Use an HTML table because GitHub Markdown handles image alignment more
predictably that way.

The structure is:

- row 1: linked preview images
- row 2: linked titles and one-line descriptions

Current `Video2Book` usage:

- `Wealth from First Principles`
- `How You Got Rich?`
- `How You Got Successful?`
- `How You Got Happiness?`

Important implementation details:

- use `width="180"` or another fixed width for even alignment
- use `<table width="100%">` for four-item preview strips
- use `<td align="center" width="25%" valign="top">` so titles and covers align across repos
- link the image directly to the canonical PDF
- keep the descriptions short
- do not overload the top strip with too many books

### 2. Lower compact catalog

After the flagship strip, keep the broader published list in a Markdown table.

That lower table is where the rest of the books belong:

- other `LazyEarn` books
- `LazyLearn` course books
- `leonardsusskind` published books

This keeps the README scannable:

- visual at the top
- comprehensive below

## Linking Strategy

There are two different link classes in the `Video2Book` README:

### 1. Image source

For README images in `Video2Book`, use a raw GitHub URL because the image file
actually lives in a host repo:

- `https://raw.githubusercontent.com/<owner>/<repo>/main/docs/publications/<slug>/cover-page-1.png`

Example:

- `https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-rich/cover-page-1.png`

### 2. Click target

For the clickable destination, link to the host repo PDF page:

- `https://github.com/<owner>/<repo>/blob/main/<path-to-pdf>`

## What `LazyLearn` Should Do

For `LazyLearn`, use the same pattern:

1. choose a small set of flagship books or course PDFs
2. extract page 1 of each canonical PDF
3. store them under:
   - `docs/publications/<slug>/cover-page-1.png`
4. place an HTML preview strip near the top of `README.md`
5. keep the larger book list below as a table or link list

Good candidates in `LazyLearn`:

- `How You Speak and Write`
- `Justice with Michael Sandel`
- any future flagship reading / speaking books

## What `leonardsusskind` Should Do

For `leonardsusskind`, use the same mechanism but a different editorial filter.

Do not try to preview too many books at the top.

Use a small number of strongest canonical titles, for example:

- `Classical Mechanics (Theoretical Minimum)`
- `Advanced Quantum Mechanics`
- `Topics in String Theory`
- one more flagship physics title if needed

Then keep the broader `all_notes/` and supplemental catalog lower in a compact
table.

## What To Preserve

When another host repo adapts this:

- use the real first page of the current PDF
- store the preview under `docs/publications/<slug>/cover-page-1.png`
- keep the top section visually small and selective
- keep the rest of the catalog lower in a compact table
- avoid duplicating the full catalog as giant image blocks

## What To Avoid

- do not use stale screenshots from a PDF viewer
- do not host the preview in a separate unrelated asset folder if
  `docs/publications/<slug>/` already exists
- do not put every book in the top preview strip
- do not rely on generated textless art if the canonical published PDF already
  has a cover page worth showing

## Related Files

- `README.md`
- `references/readme-book-preview-handoff.md`
- host repo `docs/publications/<slug>/cover-page-1.png`

For cover-generation details, the separate note is:

- `references/nanobanana-2-book-cover-handoff.md`
