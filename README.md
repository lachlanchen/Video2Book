[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://lazying.art)

# Video2Book by LazyingArt LLC

> **Video2Book by LazyingArt LLC**. Websites: [lazying.art](https://lazying.art) and [learn.lazying.art](https://learn.lazying.art).

[![LazyingArt](https://img.shields.io/badge/Website-lazying.art-111827?style=for-the-badge&logo=googlechrome&logoColor=white)](https://lazying.art)
[![Learn](https://img.shields.io/badge/Learn-learn.lazying.art-1f2937?style=for-the-badge&logo=bookstack&logoColor=white)](https://learn.lazying.art)

[![Toolkit](https://img.shields.io/badge/toolkit-video__to__book-111827?style=for-the-badge&logo=bookstack&logoColor=white)](#)
[![Downloader](https://img.shields.io/badge/stage_1-playlist2videos-1d4ed8?style=for-the-badge&logo=youtube&logoColor=white)](#-pipeline)
[![Transcription](https://img.shields.io/badge/stage_2-videos2subtitles-0f766e?style=for-the-badge&logo=openai&logoColor=white)](#-pipeline)
[![Notes](https://img.shields.io/badge/stage_3-subtitles2notes-f97316?style=for-the-badge&logo=latex&logoColor=white)](#-pipeline)
[![tmux](https://img.shields.io/badge/runtime-tmux-7c3aed?style=for-the-badge&logo=gnu-bash&logoColor=white)](#-quick-start)

`Video2Book` is a practical pipeline for turning long-form video collections into durable study material: downloaded media, timestamped transcripts, and transcript-derived lecture notes with compiled PDFs.

## ✨ What It Covers

- Download a playlist into a stable external media archive.
- Transcribe videos into `.srt` subtitles and timestamped Markdown.
- Convert completed transcript sets into structured TeX notes and merged course PDFs.
- Run long jobs in `tmux` with queue scripts and monitor/guard scripts.

## 🧪 Working Host Repos

`Video2Book` is already being used in multiple host repos with different archive shapes.

| Host repo | Focus | Wrapper example | Current tracked outputs |
| --- | --- | --- | --- |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Yale `Financial Markets` course with Robert J. Shiller | [examples/lazyearn/yale-financial-markets/](examples/lazyearn/yale-financial-markets/) | [course PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf), [lecture PDFs](https://github.com/lachlanchen/LazyEarn/tree/main/generated_course_notes/lazyearn/yale-financial-markets/chapters), [markdown transcripts](https://github.com/lachlanchen/LazyEarn/tree/main/markdown/lazyearn/yale-financial-markets), [subtitles](https://github.com/lachlanchen/LazyEarn/tree/main/subtitles/lazyearn/yale-financial-markets) |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | Writing-course adaptation for `How You Speak and Write` | [examples/lazylearn/how-you-speak-and-write/](examples/lazylearn/how-you-speak-and-write/) | [course PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf), [lecture PDFs](https://github.com/lachlanchen/LazyLearn/tree/main/generated_course_notes/lazylearn/how-you-speak-and-write/chapters) |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Full Leonard Susskind lecture archive, transcript pipeline, and published note books | [examples/leonardsusskind/susskind-physics-archive/](examples/leonardsusskind/susskind-physics-archive/) | [published books folder](https://github.com/lachlanchen/leonardsusskind/tree/main), [advanced quantum PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf), [topics in string theory PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf), [particle physics 3 PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_particle_physics_3/particle_physics_3_supersymmetry_and_grand_unification.pdf), [markdown transcripts](https://github.com/lachlanchen/leonardsusskind/tree/main/markdown), [subtitles](https://github.com/lachlanchen/leonardsusskind/tree/main/subtitles) |

## 📘 Books And PDFs

The third stage is already producing real book-like outputs in host repos:

- merged course books such as `course.pdf` or a host-published canonical name
- per-lecture PDFs under `generated_course_notes/.../chapters/`
- transcript trees in `markdown/` and subtitle trees in `subtitles/`

Representative tracked outputs:

- [LazyEarn: Yale Financial Markets course book](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf)
- [LazyLearn: How You Speak and Write course book](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf)
- [Leonard Susskind: Advanced Quantum Mechanics](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf)
- [Leonard Susskind: Topics in String Theory](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf)
- [Leonard Susskind: Particle Physics 1](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_particle_physics_1/particle_physics_1_basic_concepts.pdf)
- [Leonard Susskind: Particle Physics 2](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_particle_physics_2/particle_physics_2_standard_model.pdf)
- [Leonard Susskind: Particle Physics 3](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_particle_physics_3/particle_physics_3_supersymmetry_and_grand_unification.pdf)
- [Leonard Susskind: Quantum Entanglement Part 1](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_quantum_entanglement/quantum_entanglement_part_1.pdf)
- [Leonard Susskind: Demystifying the Higgs Boson](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_higgs_boson/demystifying_the_higgs_boson.pdf)

## 🧩 Pipeline

| Stage | Module | Purpose |
| --- | --- | --- |
| 1 | `playlist2videos/` | Download or refresh a playlist with `yt-dlp`, keep logs, and skip already archived items. |
| 2 | `videos2subtitles/` | Transcribe the archived media into `subtitles/` and `markdown/`. |
| 3 | `subtitles2notes/` | Turn completed transcripts into chapter TeX, lecture PDFs, and merged course PDFs. |

## 🚀 Quick Start

Clone it directly:

```bash
git clone git@github.com:lachlanchen/Video2Book.git
cd Video2Book
```

Or add it to another repo as a submodule:

```bash
git submodule add git@github.com:lachlanchen/Video2Book.git Video2Book
git submodule update --init --recursive
```

## 🏗️ Host Repo Layout

`Video2Book` expects to run from a host repo that stores the working outputs:

- `subtitles/`
- `markdown/`
- `generated_course_notes/`
- `.lecture-notes-work/`

The video files themselves are usually kept outside the host repo in a media workspace such as:

- `/home/lachlan/ProjectsLFS/YoutubeDownloader`

## 🛠️ Typical Usage

From the host repo root:

```bash
./Video2Book/scripts/download_susskind_playlist.sh
./Video2Book/scripts/start_transcription_tmux.sh
./Video2Book/scripts/start_transcription_monitor_tmux.sh
./Video2Book/scripts/start_course_notes_tmux.sh
./Video2Book/scripts/start_course_notes_monitor_tmux.sh
```

Dry-run the downloader:

```bash
./Video2Book/scripts/download_susskind_playlist.sh --dry-run
```

Start a note-writing queue for one course:

```bash
./Video2Book/scripts/start_course_notes_tmux.sh --course supplementary/advanced_quantum_mechanics/2013_fall
```

Export finished course PDFs to EPUB:

```bash
./Video2Book/scripts/export_course_epubs.sh --source-dir /home/lachlan/ProjectsLFS/leonardsusskind/all_notes
```

Host-specific wrappers can live under `examples/`. Current bundled patterns:

- `examples/lazyearn/yale-financial-markets/`
- `examples/lazylearn/how-you-speak-and-write/`
- `examples/leonardsusskind/susskind-physics-archive/`

## 🎬 Current Default Example

The bundled downloader defaults to the Leonard Susskind physics playlist:

- <https://www.youtube.com/playlist?list=PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG>

That default is just a working example. The code is structured so other host repos can adapt the same pipeline to different lecture archives.

## 📦 Module Map

- [playlist2videos](playlist2videos)
- [videos2subtitles](videos2subtitles)
- [subtitles2notes](subtitles2notes)
- [scripts](scripts)

## 📚 Host Adaptation Notes

- [references/lazylearn-course-adaptation.md](references/lazylearn-course-adaptation.md)
- [references/lazyearn-yale-financial-markets-adaptation.md](references/lazyearn-yale-financial-markets-adaptation.md)
- [references/nanobanana-2-book-cover-handoff.md](references/nanobanana-2-book-cover-handoff.md)
- [references/tex-book-translation-workflow.md](references/tex-book-translation-workflow.md)

## 🎨 Book Cover Utility

`Video2Book` also includes a local Nano Banana 2 helper for editorial book-cover generation:

- script: [scripts/book_cover_nanobanana.py](scripts/book_cover_nanobanana.py)
- guide: [references/nanobanana-2-book-cover-handoff.md](references/nanobanana-2-book-cover-handoff.md)
- env template: [.env.example](.env.example)
- current-book example prompt: [examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt](examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt)

It reuses the GRS AI submit-and-poll mechanics from the sibling Nano Banana work, but swaps the segmentation prompts for a book-cover prompt and saves a clean output trace per run.

## 🌐 Book Translation Utility

`Video2Book` can also translate a finished lecture-note book into sibling
language folders such as `zh/` and `jp/`, while keeping the TeX structure,
equations, and images intact.

- manager: [scripts/translate_tex_book.py](scripts/translate_tex_book.py)
- loop runner: [scripts/process_book_translation_one_by_one.sh](scripts/process_book_translation_one_by_one.sh)
- tmux starter: [scripts/start_book_translation_tmux.sh](scripts/start_book_translation_tmux.sh)
- workflow note: [references/tex-book-translation-workflow.md](references/tex-book-translation-workflow.md)

The translation loop:

- initializes a XeLaTeX-ready translated edition
- translates the main book file first, then each chapter
- recompiles after every unit
- can commit and push the translated folder after each completed unit

## ⚙️ Requirements

- `tmux`
- `ffmpeg`
- `pdflatex`
- `pdfunite`
- `pdftotext`
- `yt-dlp`
- `codex` CLI for the notes pipeline
- `pandoc`
- a working `whisper` conda env for transcription
- `whisper_with_lang_detect` if you want the primary subtitle path instead of fallback-only Whisper

## 🤝 Good Fit

`Video2Book` is a good fit when you want:

- a repo-local pipeline instead of a monolithic app
- transcript-first lecture note generation
- tmux-based long-running automation
- reproducible archive structure for study material

## 🙏 Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## License

This repository is licensed under the GNU General Public License v3.0.
