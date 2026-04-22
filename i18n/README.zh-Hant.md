語言： [English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![LazyingArt 橫幅](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://lazying.art)

# LazyingArt LLC 的 Video2Book

> **LazyingArt LLC 的 Video2Book**。網站：[lazying.art](https://lazying.art) 與 [learn.lazying.art](https://learn.lazying.art)。

[![LazyingArt](https://img.shields.io/badge/Website-lazying.art-111827?style=for-the-badge&logo=googlechrome&logoColor=white)](https://lazying.art)
[![Learn](https://img.shields.io/badge/Learn-learn.lazying.art-1f2937?style=for-the-badge&logo=bookstack&logoColor=white)](https://learn.lazying.art)

[![Toolkit](https://img.shields.io/badge/toolkit-video__to__book-111827?style=for-the-badge&logo=bookstack&logoColor=white)](#)
[![Downloader](https://img.shields.io/badge/stage_1-playlist2videos-1d4ed8?style=for-the-badge&logo=youtube&logoColor=white)](#-pipeline)
[![Transcription](https://img.shields.io/badge/stage_2-videos2subtitles-0f766e?style=for-the-badge&logo=openai&logoColor=white)](#-pipeline)
[![Notes](https://img.shields.io/badge/stage_3-subtitles2notes-f97316?style=for-the-badge&logo=latex&logoColor=white)](#-pipeline)
[![tmux](https://img.shields.io/badge/runtime-tmux-7c3aed?style=for-the-badge&logo=gnu-bash&logoColor=white)](#-quick-start)

`Video2Book` 是一套實用的管線，用於將長篇影片合集轉換成持久的學習材料：已下載的媒體、帶時間戳的逐字稿，以及由逐字稿生成並編譯成 PDF 的講義筆記。

## 📚 旗艦書籍

這些預覽使用從 `LazyEarn`
與 `LazyLearn` 中每份已發布 PDF 擷取出的第一頁。

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/wealth-from-first-principles/wealth-from-first-principles.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/wealth-from-first-principles/cover-page-1.png" width="180" alt="Wealth from First Principles 封面" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/dynamic_book/how-you-got-rich.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-rich/cover-page-1.png" width="180" alt="How You Got Rich 封面" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/jim-rohn-originals-no-ai/course.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-successful/cover-page-1.png" width="180" alt="How You Got Successful 封面" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/how-you-got-happiness-publication/how-you-got-happiness.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-happiness/cover-page-1.png" width="180" alt="How You Got Happiness 封面" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/wealth-from-first-principles/wealth-from-first-principles.pdf"><strong>Wealth from First Principles</strong></a><br />
      金錢、所有權、請求權與複利
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/dynamic_book/how-you-got-rich.pdf"><strong>How You Got Rich?</strong></a><br />
      一本由訪談證據構建的非線性財富書
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/jim-rohn-originals-no-ai/course.pdf"><strong>How You Got Successful?</strong></a><br />
      將 Jim Rohn 成功學講座重排成更流暢的書籍弧線
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/how-you-got-happiness-publication/how-you-got-happiness.pdf"><strong>How You Got Happiness?</strong></a><br />
      將 Krishnamurti 談話塑造成一本關於注意力、恐懼、冥想與自由的書
    </td>
  </tr>
</table>

`LazyLearn` 也發布一本多語寫作書，以及一本已完成的正義
課程書：

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write/cover-page-1.png" width="180" alt="How to Speak and Write 英文封面" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-zh.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write-zh/cover-page-1.png" width="180" alt="How to Speak and Write 繁體中文封面" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-jp.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write-jp/cover-page-1.png" width="180" alt="How to Speak and Write 日文封面" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/justice-with-michael-sandel/cover-page-1.png" width="180" alt="Justice with Michael Sandel 封面" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write.pdf"><strong>How to Speak and Write</strong></a><br />
      重排序英文版
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-zh.pdf"><strong>如何說話與寫作</strong></a><br />
      繁體中文版
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-jp.pdf"><strong>話し方と書き方</strong></a><br />
      日本語版
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf"><strong>Justice with Michael Sandel</strong></a><br />
      Michael Sandel 政治哲學課程書
    </td>
  </tr>
</table>

`leonardsusskind` 也發布核心 Theoretical Minimum 物理書籍：

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/quantum_mechanics_theoretical_minimum.png" width="180" alt="Quantum Mechanics Theoretical Minimum 封面" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/general_relativity_theoretical_minimum.png" width="180" alt="General Relativity Theoretical Minimum 封面" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/statistical_mechanics_theoretical_minimum_first_page.png" width="180" alt="Statistical Mechanics Theoretical Minimum 封面" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/cosmology_theoretical_minimum_first_page.png" width="180" alt="Cosmology Theoretical Minimum 封面" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf"><strong>Quantum Mechanics</strong></a><br />
      Theoretical Minimum 核心書
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf"><strong>General Relativity</strong></a><br />
      Theoretical Minimum 核心書
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf"><strong>Statistical Mechanics</strong></a><br />
      Theoretical Minimum 核心書
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf"><strong>Cosmology</strong></a><br />
      Theoretical Minimum 核心書
    </td>
  </tr>
</table>

## ✨ 涵蓋內容

- 將播放清單下載到穩定的外部媒體封存區。
- 將影片轉錄成 `.srt` 字幕與帶時間戳的 Markdown。
- 將已完成的逐字稿集合轉換成結構化 TeX 筆記與合併後的課程 PDF。
- 將有序的 Markdown 材料資料夾轉換成口袋尺寸 TeX/PDF 書籍。
- 使用 `tmux` 搭配佇列腳本與監控/防護腳本執行長時間工作。
- 從已完成的課程 LaTeX 匯出精簡口袋格式伴讀 PDF。
- 在各主機 repo 中，為一般
  全尺寸 PDF 與口袋 PDF 重用相同的包裹標頭與圖像重新整理流程。

## 🧪 運作中的主機 Repo

`Video2Book` 已經在多個具有不同封存形態的主機 repo 中使用。

| 主機 repo | 焦點 | 包裝器範例 | 目前追蹤的輸出 |
| --- | --- | --- | --- |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Robert J. Shiller 的 Yale `Financial Markets` 課程 | [examples/lazyearn/yale-financial-markets/](../examples/lazyearn/yale-financial-markets/) | [課程 PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf), [講座 PDF](https://github.com/lachlanchen/LazyEarn/tree/main/generated_course_notes/lazyearn/yale-financial-markets/chapters), [Markdown 逐字稿](https://github.com/lachlanchen/LazyEarn/tree/main/markdown/lazyearn/yale-financial-markets), [字幕](https://github.com/lachlanchen/LazyEarn/tree/main/subtitles/lazyearn/yale-financial-markets) |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | `How You Speak and Write` 的寫作課程改編 | [examples/lazylearn/how-you-speak-and-write/](../examples/lazylearn/how-you-speak-and-write/), [examples/lazylearn/justice-with-michael-sandel/](../examples/lazylearn/justice-with-michael-sandel/) | [How You Speak and Write 課程 PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf), [Justice with Michael Sandel 課程 PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/justice-with-michael-sandel/course.pdf), [本機演講者課程 PDF](https://github.com/lachlanchen/LazyLearn/tree/main/how-to-speak-and-write), [本機正義 PDF](https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf), [講座 PDF](https://github.com/lachlanchen/LazyLearn/tree/main/generated_course_notes/lazylearn/how-you-speak-and-write/chapters), [Markdown 逐字稿](https://github.com/lachlanchen/LazyLearn/tree/main/markdown/lazylearn), [字幕](https://github.com/lachlanchen/LazyLearn/tree/main/subtitles/lazylearn) |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | 完整 Leonard Susskind 講座封存、逐字稿管線與已發布筆記書籍 | [examples/leonardsusskind/susskind-physics-archive/](../examples/leonardsusskind/susskind-physics-archive/) | [已發布書籍資料夾](https://github.com/lachlanchen/leonardsusskind/tree/main), [advanced quantum PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf), [topics in string theory PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf), [particle physics 3 PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_particle_physics_3/particle_physics_3_supersymmetry_and_grand_unification.pdf), [Markdown 逐字稿](https://github.com/lachlanchen/leonardsusskind/tree/main/markdown), [字幕](https://github.com/lachlanchen/leonardsusskind/tree/main/subtitles) |

## 📘 書籍與 PDF

第三階段已經在主機 repo 中產出真正類書籍的輸出：

- 合併課程書，例如 `course.pdf` 或主機發布的規範名稱
- 位於 `generated_course_notes/.../chapters/` 下的逐講 PDF
- 位於 `markdown/` 的逐字稿樹與位於 `subtitles/` 的字幕樹

其他已發布書籍與課程輸出：

| 主機 repo | 標題 | 主要 PDF | 筆記 |
| --- | --- | --- | --- |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Yale Financial Markets | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf) | Robert J. Shiller 講座書，含全尺寸與口袋版本 |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Hard Knocks Interviews | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/course.pdf) | 逐講直接彙編 |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | High-Growth Dossier | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/high-growth-stocks/high-growth-stocks.pdf) | 舊版研究書，含口袋匯出 |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Quod Tango Muto | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/quod-tango-muto/quod-tango-muto.pdf) | 拉丁格言研究書，含口袋匯出 |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | How You Speak and Write | [PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf) | 寫作課程改編 |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | Justice with Michael Sandel | [PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/justice-with-michael-sandel/course.pdf) | 政治哲學課程書 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Classical Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/classical_mechanics_theoretical_minimum.pdf) | `all_notes/` 中的整合書 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Quantum Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/quantum_mechanics_theoretical_minimum.pdf) | `all_notes/` 中的核心 TTM 書 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Special Relativity (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/special_relativity_theoretical_minimum.pdf) | `all_notes/` 中的核心 TTM 書 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | General Relativity (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/general_relativity_theoretical_minimum.pdf) | `all_notes/` 中的核心 TTM 書 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Statistical Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/statistical_mechanics_theoretical_minimum.pdf) | `all_notes/` 中的核心 TTM 書 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Cosmology (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/cosmology_theoretical_minimum.pdf) | `all_notes/` 中的核心 TTM 書 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Advanced Quantum Mechanics | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf) | 補充物理標題 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Topics in String Theory | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf) | 補充宇宙學 / 弦論標題 |

其他 Susskind 整合標題可在 [all_notes](https://github.com/lachlanchen/leonardsusskind/tree/main/all_notes) 取得。

### 本機同層 Repo 指標

如果你從共用父目錄執行這些 repo（例如 `/home/lachlan/ProjectsLFS`），也可以透過本機路徑存取相同書籍：

- `../LazyLearn/justice-with-michael-sandel/justice-with-michael-sandel.pdf`
- `../LazyLearn/how-to-speak-and-write/how-to-speak-and-write.pdf`
- `../LazyEarn/generated_course_notes/lazyearn/yale-financial-markets/course.pdf`
- `../leonardsusskind/<sibling-folder>/...`（該 repo 中的課程與已發布書籍 PDF）

## 🧩 管線

| 階段 | 模組 | 目的 |
| --- | --- | --- |
| 1 | `playlist2videos/` | 使用 `yt-dlp` 下載或更新播放清單，保留日誌，並略過已封存項目。 |
| 2 | `videos2subtitles/` | 將已封存媒體轉錄到 `subtitles/` 與 `markdown/`。 |
| 3 | `subtitles2notes/` | 將已完成逐字稿轉成章節 TeX、講座 PDF 與合併課程 PDF。 |
| 4 | `scripts/process_markdown_material_book.py` | 將有序來源 Markdown 資料夾轉成生成的口袋尺寸 TeX/PDF 書籍，同時將相關圖片傳給 Codex。 |
| 5 | `scripts/start_markdown_material_book_tmux.sh` | 在 `tmux` 中執行 Markdown 材料書籍撰寫器，採用可安全續跑、一次處理一個來源的流程。 |
| 6 | `scripts/export_course_pocket_pdfs.sh` | 將已完成的 `course.tex` 輸出重新建置成供發布套件使用的口袋/A5 版本，並輸出對應的 overfull 報告。 |
| 7 | `scripts/export_tex_book_pocket_pdf.sh` | 將一本獨立 TeX 書籍/文章重新建置成口袋尺寸伴讀 PDF，並同步到主機 repo 的 docs 樹。 |
| 8 | `subtitles2notes/templates/lecture_notes_common_preamble.tex` | 生成書籍所使用的共用一般尺寸課程 PDF 標頭/版面來源。 |
| 9 | `scripts/fix_course_pocket_overfulls.sh` | 針對一個課程版本反覆迭代：匯出、報告、Codex 修補、重新匯出，直到可處理的 overfull 減少。 |
| 10 | `scripts/fix_latex_project_overfulls.sh` | 適用於任何可用 `pdflatex` 或自訂編譯命令建置的 repo/project 的通用 LaTeX 溢出版面修正器。 |
| 11 | `scripts/recheck_course_figures.py` | 依據逐字稿脈絡與替代影片影格，重新稽核類截圖講座圖像。 |
| 12 | `scripts/export_course_epubs.sh` | 直接將已完成的 `course.tex` 輸出重新建置成 EPUB3。 |

## 🚀 快速開始

直接複製：

```bash
git clone git@github.com:lachlanchen/Video2Book.git
cd Video2Book
```

或將它作為 submodule 加入另一個 repo：

```bash
git submodule add git@github.com:lachlanchen/Video2Book.git Video2Book
git submodule update --init --recursive
```

## 🏗️ 主機 Repo 版面

`Video2Book` 預期從存放工作輸出的主機 repo 中執行：

- `subtitles/`
- `markdown/`
- `generated_course_notes/`
- `.lecture-notes-work/`

影片檔本身通常保存在主機 repo 之外的媒體工作區，例如：

- `/home/lachlan/ProjectsLFS/YoutubeDownloader`

## 🛠️ 典型用法

從主機 repo 根目錄：

```bash
./Video2Book/scripts/download_susskind_playlist.sh
./Video2Book/scripts/start_transcription_tmux.sh
./Video2Book/scripts/start_transcription_monitor_tmux.sh
./Video2Book/scripts/start_course_notes_tmux.sh
./Video2Book/scripts/start_course_notes_monitor_tmux.sh
```

乾跑下載器：

```bash
./Video2Book/scripts/download_susskind_playlist.sh --dry-run
```

為一門課程啟動筆記撰寫佇列：

```bash
./Video2Book/scripts/start_course_notes_tmux.sh --course supplementary/advanced_quantum_mechanics/2013_fall
```

為所有已完成課程匯出精簡 PDF（例如在 `leonardsusskind` 中）：

```bash
./Video2Book/scripts/export_course_pocket_pdfs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
```

將 `investment_pdfs/` 中一本獨立書籍匯出成口袋尺寸版本：

```bash
./Video2Book/scripts/export_tex_book_pocket_pdf.sh \
  --repo-root /home/lachlan/ProjectsLFS/LazyEarn \
  --project-root /home/lachlan/ProjectsLFS/LazyEarn/investment_pdfs/wealth-from-first-principles \
  --main-tex wealth-from-first-principles.tex \
  --font-mode onepointtwo \
  --suffix pocket_1_2x
```

針對一個窄版課程版本執行 Codex 驅動的溢出修正器：

```bash
./Video2Book/scripts/start_pocket_overflow_fix_tmux.sh \
  --course core/statistical_mechanics/2013_spring_theoretical_minimum \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

在 tmux 中跨所有已完成 Susskind 課程執行佇列，一次處理一門課：

```bash
./Video2Book/scripts/start_pocket_overflow_fix_tmux.sh \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

在任何專案上執行通用 LaTeX 修正器：

```bash
./Video2Book/scripts/fix_latex_project_overfulls.sh \
  --repo-root /path/to/repo \
  --project-root /path/to/repo/book \
  --main-tex main.tex \
  --model gpt-5.4 \
  --reasoning medium
```

直接從 TeX 為所有已完成課程匯出 EPUB3：

```bash
./Video2Book/scripts/export_course_epubs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
```

主機專用包裝器可放在 `examples/` 下。目前內建模式：

- `examples/lazyearn/yale-financial-markets/`
- `examples/lazylearn/how-you-speak-and-write/`
- `examples/leonardsusskind/susskind-physics-archive/`

## 🎬 目前預設範例

內建下載器預設使用 Leonard Susskind 物理播放清單：

- <https://www.youtube.com/playlist?list=PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG>

該預設值只是一個可運作範例。程式碼的結構讓其他主機 repo 能將同一條管線改用於不同的講座封存。

## 📦 模組地圖

- [playlist2videos](../playlist2videos)
- [videos2subtitles](../videos2subtitles)
- [subtitles2notes](../subtitles2notes)
- [scripts](../scripts)
- [口袋尺寸課程 PDF 交接](../references/pocket-size-course-pdfs-handoff.md)
- [A4 與口袋版面交接](../references/a4-and-pocket-pdf-layout-handoff.md)
- [README 書籍預覽交接](../references/readme-book-preview-handoff.md)
- [LaTeX 溢出修正器交接](../references/latex-overflow-fixer-handoff.md)
- [EPUB 匯出交接](../references/tex-to-epub-handoff.md)

## 📚 主機改編筆記

- [references/lazylearn-course-adaptation.md](../references/lazylearn-course-adaptation.md)
- [references/lazyearn-yale-financial-markets-adaptation.md](../references/lazyearn-yale-financial-markets-adaptation.md)
- [references/nanobanana-2-book-cover-handoff.md](../references/nanobanana-2-book-cover-handoff.md)
- [references/readme-book-preview-handoff.md](../references/readme-book-preview-handoff.md)
- [references/a4-and-pocket-pdf-layout-handoff.md](../references/a4-and-pocket-pdf-layout-handoff.md)
- [references/latex-overflow-fixer-handoff.md](../references/latex-overflow-fixer-handoff.md)
- [references/tex-book-translation-workflow.md](../references/tex-book-translation-workflow.md)
- [references/tex-to-epub-handoff.md](../references/tex-to-epub-handoff.md)

## 🎨 書籍封面工具

`Video2Book` 也包含一個本機 Nano Banana 2 輔助工具，用於生成編輯式書籍封面：

- script: [scripts/book_cover_nanobanana.py](../scripts/book_cover_nanobanana.py)
- guide: [references/nanobanana-2-book-cover-handoff.md](../references/nanobanana-2-book-cover-handoff.md)
- env template: [.env.example](../.env.example)
- current-book example prompt: [examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt](../examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt)

它重用同層 Nano Banana 工作中的 GRS AI submit-and-poll 機制，但將分割提示換成書籍封面提示，並為每次執行保存乾淨的輸出追蹤。

## 🌐 書籍翻譯工具

`Video2Book` 也可以將已完成的講義書籍翻譯到同層
語言資料夾，例如 `zh/` 與 `jp/`，同時保持 TeX 結構、
方程式與圖片完整。

- manager: [scripts/translate_tex_book.py](../scripts/translate_tex_book.py)
- loop runner: [scripts/process_book_translation_one_by_one.sh](../scripts/process_book_translation_one_by_one.sh)
- tmux starter: [scripts/start_book_translation_tmux.sh](../scripts/start_book_translation_tmux.sh)
- workflow note: [references/tex-book-translation-workflow.md](../references/tex-book-translation-workflow.md)

翻譯迴圈：

- 初始化可用 XeLaTeX 的翻譯版本
- 先翻譯主書檔，再翻譯每一章
- 同時支援拆分章節書籍，以及含有內嵌 `\chapter{...}` 區塊的單檔 `main.tex` 書籍
- 使用語言後綴命名翻譯後的入口檔，例如 `book_zh.tex` 或 `book_jp.tex`
- 每個單元完成後重新編譯
- 可在每個已完成單元後提交並推送翻譯資料夾

## ⚙️ 需求

- `tmux`
- `ffmpeg`
- `pdflatex`
- `pdfunite`
- `pdftotext`
- `yt-dlp`
- `pandoc`（用於 `scripts/export_course_epubs.sh`）
- 筆記管線所需的 `codex` CLI
- 用於轉錄的可運作 `whisper` conda env
- 如果你想使用主要字幕路徑而不是僅 fallback 的 Whisper，則需要 `whisper_with_lang_detect`
- `rsync`（用於口袋 PDF 的選用本機發布同步）

## 🤝 適合情境

當你想要以下內容時，`Video2Book` 很適合：

- repo 本機管線，而不是單體式 app
- 逐字稿優先的講義筆記生成
- 基於 tmux 的長時間自動化
- 可重現的學習材料封存結構

## 🙏 支持

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 授權

此儲存庫採用 GNU General Public License v3.0 授權。