# TeX Book Translation Workflow

`Video2Book` can now translate a finished lecture-note book into sibling language
folders such as `zh/` and `jp/`, one unit at a time, while preserving LaTeX,
figures, equations, and chapter order.

It supports both:

- books whose `main.tex` uses `\input{.../content.tex}` chapter files
- books whose chapters are written inline inside a single `main.tex`

## What The Tool Does

- initializes a translated edition next to the source book
- creates a XeLaTeX-ready `translated_common_preamble.tex` with CJK fonts
- copies or extracts each chapter into `zh/chapters/...` or `jp/chapters/...`
- translates one unit at a time with Codex:
  - first the main book TeX file
  - then each chapter `content.tex`
- recompiles after every completed unit
- can commit and push the translated folder after every unit

## Scripts

- manager: [scripts/translate_tex_book.py](../scripts/translate_tex_book.py)
- loop runner: [scripts/process_book_translation_one_by_one.sh](../scripts/process_book_translation_one_by_one.sh)
- tmux starter: [scripts/start_book_translation_tmux.sh](../scripts/start_book_translation_tmux.sh)

## Language Folders

For a book rooted at `how-to-speak-and-write/`, the translated editions live at:

- `how-to-speak-and-write/zh/`
- `how-to-speak-and-write/jp/`

Each folder contains:

- `how-to-speak-and-write.tex`
- `how-to-speak-and-write.pdf`
- `translated_common_preamble.tex`
- `translation_manifest.json`
- `chapters/<chapter-key>/content.tex`

## Translation Quality Rules

The prompts are designed for:

- faithful meaning
- natural target-language syntax
- polished lecture-note prose instead of literal translation

Hard constraints:

- preserve LaTeX commands and structure exactly
- preserve math and figure references
- preserve filenames, URLs, and `\input` targets
- use Traditional Chinese for `zh`
- keep `LazyingArt LLC` and `Video2Book` in English

## Typical Usage

Initialize one language:

```bash
python3 Video2Book/scripts/translate_tex_book.py \
  --book-root how-to-speak-and-write \
  --language zh \
  init
```

Start the long-running translation loop in tmux:

```bash
./Video2Book/scripts/start_book_translation_tmux.sh \
  --book-root how-to-speak-and-write \
  --language zh \
  --session how-to-speak-and-write-zh
```

Do the same for Japanese:

```bash
./Video2Book/scripts/start_book_translation_tmux.sh \
  --book-root how-to-speak-and-write \
  --language jp \
  --session how-to-speak-and-write-jp
```

## Notes

- the translated editions compile with `xelatex`, not `pdflatex`
- the build directory stays under the translated language folder
- the manager is idempotent, so rerunning `init` is safe
- the loop uses one shared Codex session per language so terminology and style
  stay more consistent across chapters
