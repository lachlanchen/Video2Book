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

## 📚 Flagship Books

These previews use the extracted first page of each published PDF from `LazyEarn`
and `LazyLearn`.

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/wealth-from-first-principles/wealth-from-first-principles.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/wealth-from-first-principles/cover-page-1.png" width="180" alt="Wealth from First Principles cover" />
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/financial_freedom/financial_freedom.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/financial-freedom/cover-page-1.png" width="180" alt="Financial Freedom Playbook cover" />
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/dynamic_book/how-you-got-rich.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-rich/cover-page-1.png" width="180" alt="How You Got Rich cover" />
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/jim-rohn-originals-no-ai/course.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-successful/cover-page-1.png" width="180" alt="How You Got Successful cover" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/wealth-from-first-principles/wealth-from-first-principles.pdf"><strong>Wealth from First Principles</strong></a><br />
      money, ownership, claims, and compounding
    </td>
    <td align="center">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/financial_freedom/financial_freedom.pdf"><strong>Financial Freedom Playbook</strong></a><br />
      budgeting, optionality, and durable cashflow
    </td>
    <td align="center">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/dynamic_book/how-you-got-rich.pdf"><strong>How You Got Rich?</strong></a><br />
      a nonlinear wealth book built from interview evidence
    </td>
    <td align="center">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/jim-rohn-originals-no-ai/course.pdf"><strong>How You Got Successful?</strong></a><br />
      Jim Rohn success lectures reordered into a smoother book arc
    </td>
  </tr>
</table>

`LazyLearn` also publishes a multilingual writing book plus a finished justice
course book:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write/cover-page-1.png" width="180" alt="How to Speak and Write English cover" />
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-zh.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write-zh/cover-page-1.png" width="180" alt="How to Speak and Write Traditional Chinese cover" />
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-jp.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write-jp/cover-page-1.png" width="180" alt="How to Speak and Write Japanese cover" />
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/justice-with-michael-sandel/cover-page-1.png" width="180" alt="Justice with Michael Sandel cover" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write.pdf"><strong>How to Speak and Write</strong></a><br />
      reordered English edition
    </td>
    <td align="center">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-zh.pdf"><strong>如何說話與寫作</strong></a><br />
      繁體中文版
    </td>
    <td align="center">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-jp.pdf"><strong>話し方と書き方</strong></a><br />
      日本語版
    </td>
    <td align="center">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf"><strong>Justice with Michael Sandel</strong></a><br />
      Michael Sandel political philosophy course book
    </td>
  </tr>
</table>

`leonardsusskind` also publishes core Theoretical Minimum physics books:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/quantum_mechanics_theoretical_minimum.png" width="180" alt="Quantum Mechanics Theoretical Minimum cover" />
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/general_relativity_theoretical_minimum.png" width="180" alt="General Relativity Theoretical Minimum cover" />
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/statistical_mechanics_theoretical_minimum_first_page.png" width="180" alt="Statistical Mechanics Theoretical Minimum cover" />
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/cosmology_theoretical_minimum_first_page.png" width="180" alt="Cosmology Theoretical Minimum cover" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf"><strong>Quantum Mechanics</strong></a><br />
      Theoretical Minimum core book
    </td>
    <td align="center">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf"><strong>General Relativity</strong></a><br />
      Theoretical Minimum core book
    </td>
    <td align="center">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf"><strong>Statistical Mechanics</strong></a><br />
      Theoretical Minimum core book
    </td>
    <td align="center">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf"><strong>Cosmology</strong></a><br />
      Theoretical Minimum core book
    </td>
  </tr>
</table>

## ✨ What It Covers

- Download a playlist into a stable external media archive.
- Transcribe videos into `.srt` subtitles and timestamped Markdown.
- Convert completed transcript sets into structured TeX notes and merged course PDFs.
- Run long jobs in `tmux` with queue scripts and monitor/guard scripts.
- Export compact pocket-format companion PDFs from finished course LaTeX.
- Reuse the same wrapped-header and figure-refresh workflow for both normal
  full-size PDFs and pocket PDFs across host repos.

## 🧪 Working Host Repos

`Video2Book` is already being used in multiple host repos with different archive shapes.

| Host repo | Focus | Wrapper example | Current tracked outputs |
| --- | --- | --- | --- |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Yale `Financial Markets` course with Robert J. Shiller | [examples/lazyearn/yale-financial-markets/](examples/lazyearn/yale-financial-markets/) | [course PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf), [lecture PDFs](https://github.com/lachlanchen/LazyEarn/tree/main/generated_course_notes/lazyearn/yale-financial-markets/chapters), [markdown transcripts](https://github.com/lachlanchen/LazyEarn/tree/main/markdown/lazyearn/yale-financial-markets), [subtitles](https://github.com/lachlanchen/LazyEarn/tree/main/subtitles/lazyearn/yale-financial-markets) |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | Writing-course adaptation for `How You Speak and Write` | [examples/lazylearn/how-you-speak-and-write/](examples/lazylearn/how-you-speak-and-write/), [examples/lazylearn/justice-with-michael-sandel/](examples/lazylearn/justice-with-michael-sandel/) | [How You Speak and Write course PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf), [Justice with Michael Sandel course PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/justice-with-michael-sandel/course.pdf), [local speaker course PDFs](https://github.com/lachlanchen/LazyLearn/tree/main/how-to-speak-and-write), [local justice PDF](https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf), [lecture PDFs](https://github.com/lachlanchen/LazyLearn/tree/main/generated_course_notes/lazylearn/how-you-speak-and-write/chapters), [markdown transcripts](https://github.com/lachlanchen/LazyLearn/tree/main/markdown/lazylearn), [subtitles](https://github.com/lachlanchen/LazyLearn/tree/main/subtitles/lazylearn) |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Full Leonard Susskind lecture archive, transcript pipeline, and published note books | [examples/leonardsusskind/susskind-physics-archive/](examples/leonardsusskind/susskind-physics-archive/) | [published books folder](https://github.com/lachlanchen/leonardsusskind/tree/main), [advanced quantum PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf), [topics in string theory PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf), [particle physics 3 PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_particle_physics_3/particle_physics_3_supersymmetry_and_grand_unification.pdf), [markdown transcripts](https://github.com/lachlanchen/leonardsusskind/tree/main/markdown), [subtitles](https://github.com/lachlanchen/leonardsusskind/tree/main/subtitles) |

## 📘 Books And PDFs

The third stage is already producing real book-like outputs in host repos:

- merged course books such as `course.pdf` or a host-published canonical name
- per-lecture PDFs under `generated_course_notes/.../chapters/`
- transcript trees in `markdown/` and subtitle trees in `subtitles/`

Other published books and course outputs:

| Host repo | Title | Main PDF | Notes |
| --- | --- | --- | --- |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Yale Financial Markets | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf) | Robert J. Shiller lecture book with full-size and pocket variants |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Hard Knocks Interviews | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/course.pdf) | direct lecture-by-lecture compilation |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | High-Growth Dossier | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/high-growth-stocks/high-growth-stocks.pdf) | legacy research book with pocket exports |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Quod Tango Muto | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/quod-tango-muto/quod-tango-muto.pdf) | Latin-motto research book with pocket exports |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Financial Freedom Playbook (Chinese) | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/financial_freedom/zh/financial_freedom_zh.pdf) | translated sibling edition |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | How You Speak and Write | [PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf) | writing-course adaptation |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | Justice with Michael Sandel | [PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/justice-with-michael-sandel/course.pdf) | political philosophy course book |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Classical Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/classical_mechanics_theoretical_minimum.pdf) | consolidated book in `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Quantum Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/quantum_mechanics_theoretical_minimum.pdf) | core TTM book in `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Special Relativity (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/special_relativity_theoretical_minimum.pdf) | core TTM book in `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | General Relativity (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/general_relativity_theoretical_minimum.pdf) | core TTM book in `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Statistical Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/statistical_mechanics_theoretical_minimum.pdf) | core TTM book in `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Cosmology (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/cosmology_theoretical_minimum.pdf) | core TTM book in `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Advanced Quantum Mechanics | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf) | supplemental physics title |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Topics in String Theory | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf) | supplemental cosmology / string title |

Other Susskind consolidated titles are available in [all_notes](https://github.com/lachlanchen/leonardsusskind/tree/main/all_notes).

### Local Sibling Repo Pointers

If you are running these repos from a shared parent directory (for example `/home/lachlan/ProjectsLFS`), the same books are also addressable via local paths:

- `../LazyLearn/justice-with-michael-sandel/justice-with-michael-sandel.pdf`
- `../LazyLearn/how-to-speak-and-write/how-to-speak-and-write.pdf`
- `../LazyEarn/generated_course_notes/lazyearn/yale-financial-markets/course.pdf`
- `../leonardsusskind/<sibling-folder>/...` (course and published-book PDFs in that repo)

## 🧩 Pipeline

| Stage | Module | Purpose |
| --- | --- | --- |
| 1 | `playlist2videos/` | Download or refresh a playlist with `yt-dlp`, keep logs, and skip already archived items. |
| 2 | `videos2subtitles/` | Transcribe the archived media into `subtitles/` and `markdown/`. |
| 3 | `subtitles2notes/` | Turn completed transcripts into chapter TeX, lecture PDFs, and merged course PDFs. |
| 4 | `scripts/export_course_pocket_pdfs.sh` | Rebuild finished `course.tex` outputs into pocket/A5 variants for publishing packages and emit mapped overfull reports. |
| 5 | `scripts/export_tex_book_pocket_pdf.sh` | Rebuild one standalone TeX book/article into a pocket-size companion PDF and sync it into the host repo docs tree. |
| 6 | `subtitles2notes/templates/lecture_notes_common_preamble.tex` | Shared normal-size course-PDF header/layout source used by generated books. |
| 7 | `scripts/fix_course_pocket_overfulls.sh` | Iterate on one course variant: export, report, Codex patch, and re-export until actionable overfulls drop. |
| 8 | `scripts/fix_latex_project_overfulls.sh` | Generic LaTeX overflow fixer for any repo/project that can build with `pdflatex` or a custom compile command. |
| 9 | `scripts/recheck_course_figures.py` | Re-audit screenshot-like lecture figures against transcript context and replacement video frames. |
| 10 | `scripts/export_course_epubs.sh` | Rebuild finished `course.tex` outputs directly into EPUB3. |

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

Export compact PDFs for all completed courses (for example in `leonardsusskind`):

```bash
./Video2Book/scripts/export_course_pocket_pdfs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
```

Export one standalone book in `investment_pdfs/` into pocket-size variants:

```bash
./Video2Book/scripts/export_tex_book_pocket_pdf.sh \
  --repo-root /home/lachlan/ProjectsLFS/LazyEarn \
  --project-root /home/lachlan/ProjectsLFS/LazyEarn/investment_pdfs/wealth-from-first-principles \
  --main-tex wealth-from-first-principles.tex \
  --font-mode onepointtwo \
  --suffix pocket_1_2x
```

Run the Codex-driven overflow fixer for one narrow-layout course variant:

```bash
./Video2Book/scripts/start_pocket_overflow_fix_tmux.sh \
  --course core/statistical_mechanics/2013_spring_theoretical_minimum \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

Run the queue in tmux across all completed Susskind courses, one course at a time:

```bash
./Video2Book/scripts/start_pocket_overflow_fix_tmux.sh \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

Run the generic LaTeX fixer on any project:

```bash
./Video2Book/scripts/fix_latex_project_overfulls.sh \
  --repo-root /path/to/repo \
  --project-root /path/to/repo/book \
  --main-tex main.tex \
  --model gpt-5.4 \
  --reasoning medium
```

Export EPUB3 directly from TeX for all completed courses:

```bash
./Video2Book/scripts/export_course_epubs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
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
- [Pocket export handoff](references/pocket-size-course-pdfs-handoff.md)
- [A4 and pocket layout handoff](references/a4-and-pocket-pdf-layout-handoff.md)
- [README book preview handoff](references/readme-book-preview-handoff.md)
- [LaTeX overflow fixer handoff](references/latex-overflow-fixer-handoff.md)
- [EPUB export handoff](references/tex-to-epub-handoff.md)

## 📚 Host Adaptation Notes

- [references/lazylearn-course-adaptation.md](references/lazylearn-course-adaptation.md)
- [references/lazyearn-yale-financial-markets-adaptation.md](references/lazyearn-yale-financial-markets-adaptation.md)
- [references/nanobanana-2-book-cover-handoff.md](references/nanobanana-2-book-cover-handoff.md)
- [references/readme-book-preview-handoff.md](references/readme-book-preview-handoff.md)
- [references/a4-and-pocket-pdf-layout-handoff.md](references/a4-and-pocket-pdf-layout-handoff.md)
- [references/latex-overflow-fixer-handoff.md](references/latex-overflow-fixer-handoff.md)
- [references/tex-book-translation-workflow.md](references/tex-book-translation-workflow.md)
- [references/tex-to-epub-handoff.md](references/tex-to-epub-handoff.md)

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
- supports both split-chapter books and single-file `main.tex` books with inline `\chapter{...}` blocks
- names translated entry files with a language suffix such as `book_zh.tex` or `book_jp.tex`
- recompiles after every unit
- can commit and push the translated folder after each completed unit

## ⚙️ Requirements

- `tmux`
- `ffmpeg`
- `pdflatex`
- `pdfunite`
- `pdftotext`
- `yt-dlp`
- `pandoc` (for `scripts/export_course_epubs.sh`)
- `codex` CLI for the notes pipeline
- a working `whisper` conda env for transcription
- `whisper_with_lang_detect` if you want the primary subtitle path instead of fallback-only Whisper
- `rsync` (for optional local publishing sync of pocket PDFs)

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
