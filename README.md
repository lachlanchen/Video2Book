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

Host-specific wrappers can live under `examples/`. For `LazyEarn`, a reusable course wrapper now lives at:

- `examples/lazyearn/yale-financial-markets/`

## 🎬 Current Default Example

The bundled downloader defaults to the Leonard Susskind physics playlist:

- <https://www.youtube.com/playlist?list=PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG>

That default is just a working example. The code is structured so other host repos can adapt the same pipeline to different lecture archives.

## 📦 Module Map

- [playlist2videos](playlist2videos)
- [videos2subtitles](videos2subtitles)
- [subtitles2notes](subtitles2notes)
- [scripts](scripts)

## ⚙️ Requirements

- `tmux`
- `ffmpeg`
- `pdflatex`
- `pdfunite`
- `pdftotext`
- `yt-dlp`
- `codex` CLI for the notes pipeline
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
