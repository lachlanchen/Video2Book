# Nano Banana 2 Book Cover Handoff

Date: 2026-04-15

This note documents how `Video2Book` adapts the GRS AI Nano Banana workflow for book-cover generation.

It exists because the original Nano Banana work lived in a different local repo and was mostly segmentation-oriented. The goal here is to keep the proven API mechanics, polling, and manifest-writing flow, but swap the prompt and outputs to fit editorial cover design.

## What Was Ported

This `Video2Book` adaptation was derived from the local sibling repo:

- `/home/lachlan/ProjectsLFS/Zhengyu/references/nanobanana_2_code_and_reference_handoff_2026-04-15.md`
- `/home/lachlan/ProjectsLFS/Zhengyu/references/grsai_nano_banana_api_documentation_2026-04-10.md`
- `/home/lachlan/ProjectsLFS/Zhengyu/references/grsai_nano_banana_api_doc.md`
- `/home/lachlan/ProjectsLFS/Zhengyu/analysis-tools/app81_grsai_mask_generation/run_app81_grsai_mask_generation.py`
- `/home/lachlan/ProjectsLFS/Zhengyu/analysis-tools/app81_grsai_mask_generation/run_app81_stitched_replicate1_nanobanana2_batch.py`

Those files provided the working pattern for:

- reading the `GRSAI` API key from environment or `.env`
- submitting to the GRS AI draw endpoint
- polling by task id until completion
- saving request and result artifacts locally

The segmentation-specific parts were intentionally not ported:

- mask cleanup logic
- overlay generation
- stitched-panel postprocessing

## Files Added In `Video2Book`

- `scripts/book_cover_nanobanana.py`
- `references/nanobanana-2-book-cover-handoff.md`
- `.env.example`
- `examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt`

## Local Secret Handling

For this working tree, the sibling repo's `.env` was copied locally into:

- `Video2Book/.env`

This is intentionally local-only. It is ignored by git through:

- `.gitignore`

Ignore rules now include:

- `.env`
- `.env.*`
- `!.env.example`

That means:

- `Video2Book/.env` can hold the real `GRSAI` key locally
- `Video2Book/.env.example` is the safe template for other users or models

## Core API Facts

Preferred host:

- `https://grsaiapi.com`

Submit endpoint:

- `POST /v1/draw/nano-banana`

Poll endpoint:

- `POST /v1/draw/result`

Auth header:

```json
{
  "Authorization": "Bearer <GRSAI_KEY>",
  "Content-Type": "application/json"
}
```

Recommended book-cover settings:

- `model: "nano-banana-2"`
- `aspectRatio: "2:3"`
- `imageSize: "2K"`
- `webHook: "-1"`

Minimal request shape:

```json
{
  "model": "nano-banana-2",
  "prompt": "Design a polished front-cover image for a book titled \"How to Speak and Write\".",
  "urls": [],
  "aspectRatio": "2:3",
  "imageSize": "2K",
  "webHook": "-1",
  "shutProgress": false
}
```

## What The Utility Does

`scripts/book_cover_nanobanana.py` is a standalone runner for a single cover job.

It:

1. builds or loads a prompt
2. reads `GRSAI` from env var or `Video2Book/.env`
3. converts local reference images into data URLs when needed
4. submits a Nano Banana job
5. polls by task id until success or failure
6. downloads the returned image
7. writes a reproducible local trace

Saved artifacts in the output directory:

- `prompt.txt`
- `request_payload.redacted.json`
- `submit_response.json`
- `result_response.json`
- `task_manifest.json`
- `book_cover.png` or `book_cover_01.png`, `book_cover_02.png`, ...

## Prompt Strategy For Covers

The underlying API stays the same, but the prompt should be editorial rather than analytic.

Good cover prompts usually specify:

- exact title
- optional subtitle
- optional author or curator line
- overall tone
- palette
- visual metaphor or composition
- what to avoid

For book covers, this adaptation uses a stronger default prompt structure than the segmentation repo:

- bookstore-ready front cover
- portrait composition
- clear title zone
- instruction to prefer a clean title block over garbled fake text

That last point matters because image generators often produce unstable typography.

## Reference Images

The utility accepts repeated `--reference-image` arguments.

Each reference may be:

- a local file path
- a remote `https://...` URL
- a prebuilt `data:` URL

Useful references for a cover:

- existing book covers with the right editorial feel
- palette references
- illustration references
- publisher marks or logos
- author photo if the cover concept needs it

## Example Commands

Generate a cover using the saved example prompt:

```bash
cd Video2Book
python3 scripts/book_cover_nanobanana.py \
  --prompt-file examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt \
  --output-dir examples/lazylearn/how-you-speak-and-write/book_cover_run \
  --resume
```

Generate a cover by building the prompt from CLI fields:

```bash
cd Video2Book
python3 scripts/book_cover_nanobanana.py \
  --title "How to Speak and Write" \
  --author "LazyingArt" \
  --palette "cream, charcoal, muted teal, brass" \
  --visual-direction "speech becoming lines and pages, elegant abstract editorial design" \
  --output-dir examples/lazylearn/how-you-speak-and-write/book_cover_run \
  --resume
```

Dry-run without spending API calls:

```bash
cd Video2Book
python3 scripts/book_cover_nanobanana.py \
  --prompt-file examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt \
  --output-dir examples/lazylearn/how-you-speak-and-write/book_cover_run \
  --dry-run
```

## Example Prompt For The Current Book

The saved prompt file is:

- `examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt`

It is tuned for:

- `How to Speak and Write`
- a nonfiction/editorial tone
- a restrained academic palette
- a visual transition from spoken rhythm to writing marks

## What Another Model Should Read First

If another model only needs the minimum useful set inside `Video2Book`, start with:

- `references/nanobanana-2-book-cover-handoff.md`
- `.env.example`
- `scripts/book_cover_nanobanana.py`
- `examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt`

If that model also has access to the sibling `Zhengyu` repo, the best upstream implementation references are:

- `/home/lachlan/ProjectsLFS/Zhengyu/references/nanobanana_2_code_and_reference_handoff_2026-04-15.md`
- `/home/lachlan/ProjectsLFS/Zhengyu/analysis-tools/app81_grsai_mask_generation/run_app81_grsai_mask_generation.py`

## Bottom Line

`Video2Book` now has a local Nano Banana 2 cover-generation path.

The port keeps the proven parts from the original GRS AI runners:

- auth loading
- submit and poll mechanics
- result capture

And replaces the segmentation-specific parts with:

- editorial prompt construction
- reference-image support for art direction
- clean book-cover output handling
