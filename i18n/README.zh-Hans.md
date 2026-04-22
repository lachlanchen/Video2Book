[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![LazyingArt 横幅](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://lazying.art)

# LazyingArt LLC 的 Video2Book

> **LazyingArt LLC 的 Video2Book**。网站：[lazying.art](https://lazying.art) 和 [learn.lazying.art](https://learn.lazying.art)。

[![LazyingArt](https://img.shields.io/badge/Website-lazying.art-111827?style=for-the-badge&logo=googlechrome&logoColor=white)](https://lazying.art)
[![Learn](https://img.shields.io/badge/Learn-learn.lazying.art-1f2937?style=for-the-badge&logo=bookstack&logoColor=white)](https://learn.lazying.art)

[![Toolkit](https://img.shields.io/badge/toolkit-video__to__book-111827?style=for-the-badge&logo=bookstack&logoColor=white)](#)
[![Downloader](https://img.shields.io/badge/stage_1-playlist2videos-1d4ed8?style=for-the-badge&logo=youtube&logoColor=white)](#-pipeline)
[![Transcription](https://img.shields.io/badge/stage_2-videos2subtitles-0f766e?style=for-the-badge&logo=openai&logoColor=white)](#-pipeline)
[![Notes](https://img.shields.io/badge/stage_3-subtitles2notes-f97316?style=for-the-badge&logo=latex&logoColor=white)](#-pipeline)
[![tmux](https://img.shields.io/badge/runtime-tmux-7c3aed?style=for-the-badge&logo=gnu-bash&logoColor=white)](#-quick-start)

`Video2Book` 是一套实用流水线，用于把长篇视频合集转化为可长期使用的学习材料：下载的媒体、带时间戳的转录文本，以及由转录文本生成并编译成 PDF 的讲义笔记。

## 📚 旗舰书籍

这些预览使用从 `LazyEarn`
和 `LazyLearn` 中每个已发布 PDF 提取的第一页。

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/wealth-from-first-principles/wealth-from-first-principles.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/wealth-from-first-principles/cover-page-1.png" width="180" alt="《Wealth from First Principles》封面" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/dynamic_book/how-you-got-rich.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-rich/cover-page-1.png" width="180" alt="《How You Got Rich》封面" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/jim-rohn-originals-no-ai/course.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-successful/cover-page-1.png" width="180" alt="《How You Got Successful》封面" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/how-you-got-happiness-publication/how-you-got-happiness.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-happiness/cover-page-1.png" width="180" alt="《How You Got Happiness》封面" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/wealth-from-first-principles/wealth-from-first-principles.pdf"><strong>Wealth from First Principles</strong></a><br />
      货币、所有权、索取权与复利增长
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/dynamic_book/how-you-got-rich.pdf"><strong>How You Got Rich?</strong></a><br />
      一本基于访谈证据构建的非线性财富书籍
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/jim-rohn-originals-no-ai/course.pdf"><strong>How You Got Successful?</strong></a><br />
      将 Jim Rohn 的成功学讲座重新排序为更流畅的书籍脉络
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/how-you-got-happiness-publication/how-you-got-happiness.pdf"><strong>How You Got Happiness?</strong></a><br />
      将 Krishnamurti 的谈话塑造成一本关于注意力、恐惧、冥想与自由的书
    </td>
  </tr>
</table>

`LazyLearn` 还发布了一本多语言写作书以及一本已完成的正义课程书：

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write/cover-page-1.png" width="180" alt="《How to Speak and Write》英文版封面" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-zh.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write-zh/cover-page-1.png" width="180" alt="《How to Speak and Write》繁体中文版封面" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-jp.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write-jp/cover-page-1.png" width="180" alt="《How to Speak and Write》日文版封面" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/justice-with-michael-sandel/cover-page-1.png" width="180" alt="《Justice with Michael Sandel》封面" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write.pdf"><strong>How to Speak and Write</strong></a><br />
      重新排序的英文版
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
      Michael Sandel 政治哲学课程书
    </td>
  </tr>
</table>

`leonardsusskind` 还发布了核心 Theoretical Minimum 物理书籍：

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/quantum_mechanics_theoretical_minimum.png" width="180" alt="《Quantum Mechanics Theoretical Minimum》封面" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/general_relativity_theoretical_minimum.png" width="180" alt="《General Relativity Theoretical Minimum》封面" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/statistical_mechanics_theoretical_minimum_first_page.png" width="180" alt="《Statistical Mechanics Theoretical Minimum》封面" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/cosmology_theoretical_minimum_first_page.png" width="180" alt="《Cosmology Theoretical Minimum》封面" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf"><strong>Quantum Mechanics</strong></a><br />
      Theoretical Minimum 核心书籍
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf"><strong>General Relativity</strong></a><br />
      Theoretical Minimum 核心书籍
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf"><strong>Statistical Mechanics</strong></a><br />
      Theoretical Minimum 核心书籍
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf"><strong>Cosmology</strong></a><br />
      Theoretical Minimum 核心书籍
    </td>
  </tr>
</table>

## ✨ 覆盖内容

- 将播放列表下载到稳定的外部媒体归档中。
- 将视频转录为 `.srt` 字幕和带时间戳的 Markdown。
- 将已完成的转录文本集合转换为结构化 TeX 笔记和合并后的课程 PDF。
- 将有序的 Markdown 材料文件夹转换为口袋尺寸的 TeX/PDF 书籍。
- 使用 `tmux` 配合队列脚本和监控/守护脚本运行长任务。
- 从完成的课程 LaTeX 导出紧凑的口袋格式伴随 PDF。
- 在各宿主仓库中，对普通全尺寸 PDF 和口袋 PDF 复用相同的包裹式页眉与图像刷新工作流。

## 🧪 可运行的宿主仓库

`Video2Book` 已在多个具有不同归档结构的宿主仓库中使用。

| 宿主仓库 | 重点 | 包装器示例 | 当前跟踪的输出 |
| --- | --- | --- | --- |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Robert J. Shiller 的 Yale `Financial Markets` 课程 | [examples/lazyearn/yale-financial-markets/](../examples/lazyearn/yale-financial-markets/) | [课程 PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf), [讲座 PDF](https://github.com/lachlanchen/LazyEarn/tree/main/generated_course_notes/lazyearn/yale-financial-markets/chapters), [Markdown 转录文本](https://github.com/lachlanchen/LazyEarn/tree/main/markdown/lazyearn/yale-financial-markets), [字幕](https://github.com/lachlanchen/LazyEarn/tree/main/subtitles/lazyearn/yale-financial-markets) |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | `How You Speak and Write` 的写作课程改编 | [examples/lazylearn/how-you-speak-and-write/](../examples/lazylearn/how-you-speak-and-write/), [examples/lazylearn/justice-with-michael-sandel/](../examples/lazylearn/justice-with-michael-sandel/) | [How You Speak and Write 课程 PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf), [Justice with Michael Sandel 课程 PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/justice-with-michael-sandel/course.pdf), [本地主讲人课程 PDF](https://github.com/lachlanchen/LazyLearn/tree/main/how-to-speak-and-write), [本地正义 PDF](https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf), [讲座 PDF](https://github.com/lachlanchen/LazyLearn/tree/main/generated_course_notes/lazylearn/how-you-speak-and-write/chapters), [Markdown 转录文本](https://github.com/lachlanchen/LazyLearn/tree/main/markdown/lazylearn), [字幕](https://github.com/lachlanchen/LazyLearn/tree/main/subtitles/lazylearn) |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | 完整 Leonard Susskind 讲座归档、转录流水线和已发布笔记书籍 | [examples/leonardsusskind/susskind-physics-archive/](../examples/leonardsusskind/susskind-physics-archive/) | [已发布书籍文件夹](https://github.com/lachlanchen/leonardsusskind/tree/main), [advanced quantum PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf), [topics in string theory PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf), [particle physics 3 PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_particle_physics_3/particle_physics_3_supersymmetry_and_grand_unification.pdf), [Markdown 转录文本](https://github.com/lachlanchen/leonardsusskind/tree/main/markdown), [字幕](https://github.com/lachlanchen/leonardsusskind/tree/main/subtitles) |

## 📘 书籍和 PDF

第三阶段已经在宿主仓库中产出真实的类书籍输出：

- 合并后的课程书籍，例如 `course.pdf` 或宿主发布的规范名称
- `generated_course_notes/.../chapters/` 下的逐讲 PDF
- `markdown/` 中的转录文本树和 `subtitles/` 中的字幕树

其他已发布书籍和课程输出：

| 宿主仓库 | 标题 | 主 PDF | 备注 |
| --- | --- | --- | --- |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Yale Financial Markets | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf) | Robert J. Shiller 讲座书，包含全尺寸和口袋版变体 |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Hard Knocks Interviews | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/course.pdf) | 逐讲直接编译 |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | High-Growth Dossier | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/high-growth-stocks/high-growth-stocks.pdf) | 带口袋版导出的旧版研究书籍 |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Quod Tango Muto | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/quod-tango-muto/quod-tango-muto.pdf) | 带口袋版导出的拉丁格言研究书籍 |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | How You Speak and Write | [PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf) | 写作课程改编 |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | Justice with Michael Sandel | [PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/justice-with-michael-sandel/course.pdf) | 政治哲学课程书 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Classical Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/classical_mechanics_theoretical_minimum.pdf) | `all_notes/` 中的整合书籍 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Quantum Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/quantum_mechanics_theoretical_minimum.pdf) | `all_notes/` 中的核心 TTM 书籍 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Special Relativity (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/special_relativity_theoretical_minimum.pdf) | `all_notes/` 中的核心 TTM 书籍 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | General Relativity (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/general_relativity_theoretical_minimum.pdf) | `all_notes/` 中的核心 TTM 书籍 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Statistical Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/statistical_mechanics_theoretical_minimum.pdf) | `all_notes/` 中的核心 TTM 书籍 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Cosmology (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/cosmology_theoretical_minimum.pdf) | `all_notes/` 中的核心 TTM 书籍 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Advanced Quantum Mechanics | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf) | 补充物理标题 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Topics in String Theory | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf) | 补充宇宙学 / 弦理论标题 |

其他 Susskind 整合标题可在 [all_notes](https://github.com/lachlanchen/leonardsusskind/tree/main/all_notes) 中找到。

### 本地同级仓库指针

如果你从共享父目录运行这些仓库（例如 `/home/lachlan/ProjectsLFS`），同样的书籍也可以通过本地路径访问：

- `../LazyLearn/justice-with-michael-sandel/justice-with-michael-sandel.pdf`
- `../LazyLearn/how-to-speak-and-write/how-to-speak-and-write.pdf`
- `../LazyEarn/generated_course_notes/lazyearn/yale-financial-markets/course.pdf`
- `../leonardsusskind/<sibling-folder>/...`（该仓库中的课程和已发布书籍 PDF）

## 🧩 流水线

| 阶段 | 模块 | 用途 |
| --- | --- | --- |
| 1 | `playlist2videos/` | 使用 `yt-dlp` 下载或刷新播放列表，保留日志，并跳过已归档的项目。 |
| 2 | `videos2subtitles/` | 将归档媒体转录到 `subtitles/` 和 `markdown/`。 |
| 3 | `subtitles2notes/` | 将已完成的转录文本转换为章节 TeX、讲座 PDF 和合并后的课程 PDF。 |
| 4 | `scripts/process_markdown_material_book.py` | 将有序的源 Markdown 文件夹转换为生成的口袋尺寸 TeX/PDF 书籍，同时把相关图片传给 Codex。 |
| 5 | `scripts/start_markdown_material_book_tmux.sh` | 在 `tmux` 中运行 Markdown 材料书写器，支持可恢复的单源逐项处理。 |
| 6 | `scripts/export_course_pocket_pdfs.sh` | 将完成的 `course.tex` 输出重建为用于发布包的口袋/A5 变体，并生成映射后的 overfull 报告。 |
| 7 | `scripts/export_tex_book_pocket_pdf.sh` | 将单本独立 TeX 书籍/文章重建为口袋尺寸伴随 PDF，并同步到宿主仓库文档树。 |
| 8 | `subtitles2notes/templates/lecture_notes_common_preamble.tex` | 生成书籍使用的共享普通尺寸课程 PDF 页眉/布局源。 |
| 9 | `scripts/fix_course_pocket_overfulls.sh` | 对单个课程变体进行迭代：导出、报告、Codex 修补并重新导出，直到可处理的 overfull 降低。 |
| 10 | `scripts/fix_latex_project_overfulls.sh` | 通用 LaTeX 溢出修复器，适用于任何可用 `pdflatex` 或自定义编译命令构建的仓库/项目。 |
| 11 | `scripts/recheck_course_figures.py` | 根据转录文本上下文和替换视频帧，重新审计类似截图的讲座图像。 |
| 12 | `scripts/export_course_epubs.sh` | 直接将完成的 `course.tex` 输出重建为 EPUB3。 |

## 🚀 快速开始

直接克隆：

```bash
git clone git@github.com:lachlanchen/Video2Book.git
cd Video2Book
```

或将其作为子模块添加到另一个仓库：

```bash
git submodule add git@github.com:lachlanchen/Video2Book.git Video2Book
git submodule update --init --recursive
```

## 🏗️ 宿主仓库布局

`Video2Book` 预期从存储工作输出的宿主仓库中运行：

- `subtitles/`
- `markdown/`
- `generated_course_notes/`
- `.lecture-notes-work/`

视频文件本身通常保存在宿主仓库之外的媒体工作区中，例如：

- `/home/lachlan/ProjectsLFS/YoutubeDownloader`

## 🛠️ 典型用法

从宿主仓库根目录运行：

```bash
./Video2Book/scripts/download_susskind_playlist.sh
./Video2Book/scripts/start_transcription_tmux.sh
./Video2Book/scripts/start_transcription_monitor_tmux.sh
./Video2Book/scripts/start_course_notes_tmux.sh
./Video2Book/scripts/start_course_notes_monitor_tmux.sh
```

试运行下载器：

```bash
./Video2Book/scripts/download_susskind_playlist.sh --dry-run
```

为一门课程启动笔记写作队列：

```bash
./Video2Book/scripts/start_course_notes_tmux.sh --course supplementary/advanced_quantum_mechanics/2013_fall
```

为所有已完成课程导出紧凑 PDF（例如在 `leonardsusskind` 中）：

```bash
./Video2Book/scripts/export_course_pocket_pdfs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
```

将 `investment_pdfs/` 中的一本独立书籍导出为口袋尺寸变体：

```bash
./Video2Book/scripts/export_tex_book_pocket_pdf.sh \
  --repo-root /home/lachlan/ProjectsLFS/LazyEarn \
  --project-root /home/lachlan/ProjectsLFS/LazyEarn/investment_pdfs/wealth-from-first-principles \
  --main-tex wealth-from-first-principles.tex \
  --font-mode onepointtwo \
  --suffix pocket_1_2x
```

为一个窄版式课程变体运行 Codex 驱动的溢出修复器：

```bash
./Video2Book/scripts/start_pocket_overflow_fix_tmux.sh \
  --course core/statistical_mechanics/2013_spring_theoretical_minimum \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

在 tmux 中跨所有已完成的 Susskind 课程运行队列，每次处理一门课程：

```bash
./Video2Book/scripts/start_pocket_overflow_fix_tmux.sh \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

在任意项目上运行通用 LaTeX 修复器：

```bash
./Video2Book/scripts/fix_latex_project_overfulls.sh \
  --repo-root /path/to/repo \
  --project-root /path/to/repo/book \
  --main-tex main.tex \
  --model gpt-5.4 \
  --reasoning medium
```

直接从 TeX 为所有已完成课程导出 EPUB3：

```bash
./Video2Book/scripts/export_course_epubs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
```

宿主专用包装器可以放在 `examples/` 下。当前内置模式：

- `examples/lazyearn/yale-financial-markets/`
- `examples/lazylearn/how-you-speak-and-write/`
- `examples/leonardsusskind/susskind-physics-archive/`

## 🎬 当前默认示例

内置下载器默认使用 Leonard Susskind 物理播放列表：

- <https://www.youtube.com/playlist?list=PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG>

这个默认值只是一个可运行示例。代码结构支持其他宿主仓库将同一流水线改造用于不同的讲座归档。

## 📦 模块地图

- [playlist2videos](../playlist2videos)
- [videos2subtitles](../videos2subtitles)
- [subtitles2notes](../subtitles2notes)
- [scripts](../scripts)
- [口袋尺寸导出交接说明](../references/pocket-size-course-pdfs-handoff.md)
- [A4 与口袋版式交接说明](../references/a4-and-pocket-pdf-layout-handoff.md)
- [README 书籍预览交接说明](../references/readme-book-preview-handoff.md)
- [LaTeX 溢出修复器交接说明](../references/latex-overflow-fixer-handoff.md)
- [EPUB 导出交接说明](../references/tex-to-epub-handoff.md)

## 📚 宿主适配说明

- [references/lazylearn-course-adaptation.md](../references/lazylearn-course-adaptation.md)
- [references/lazyearn-yale-financial-markets-adaptation.md](../references/lazyearn-yale-financial-markets-adaptation.md)
- [references/nanobanana-2-book-cover-handoff.md](../references/nanobanana-2-book-cover-handoff.md)
- [references/readme-book-preview-handoff.md](../references/readme-book-preview-handoff.md)
- [references/a4-and-pocket-pdf-layout-handoff.md](../references/a4-and-pocket-pdf-layout-handoff.md)
- [references/latex-overflow-fixer-handoff.md](../references/latex-overflow-fixer-handoff.md)
- [references/tex-book-translation-workflow.md](../references/tex-book-translation-workflow.md)
- [references/tex-to-epub-handoff.md](../references/tex-to-epub-handoff.md)

## 🎨 书籍封面工具

`Video2Book` 还包含一个本地 Nano Banana 2 辅助工具，用于编辑类书籍封面生成：

- 脚本：[scripts/book_cover_nanobanana.py](../scripts/book_cover_nanobanana.py)
- 指南：[references/nanobanana-2-book-cover-handoff.md](../references/nanobanana-2-book-cover-handoff.md)
- env 模板：[.env.example](../.env.example)
- 当前书籍示例提示词：[examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt](../examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt)

它复用了同级 Nano Banana 工作中的 GRS AI 提交与轮询机制，但将分割提示词替换为书籍封面提示词，并为每次运行保存干净的输出跟踪。

## 🌐 书籍翻译工具

`Video2Book` 还可以将完成的讲义笔记书翻译到同级
语言文件夹，例如 `zh/` 和 `jp/`，同时保持 TeX 结构、
公式和图片不变。

- 管理器：[scripts/translate_tex_book.py](../scripts/translate_tex_book.py)
- 循环运行器：[scripts/process_book_translation_one_by_one.sh](../scripts/process_book_translation_one_by_one.sh)
- tmux 启动器：[scripts/start_book_translation_tmux.sh](../scripts/start_book_translation_tmux.sh)
- 工作流说明：[references/tex-book-translation-workflow.md](../references/tex-book-translation-workflow.md)

翻译循环：

- 初始化一个可用于 XeLaTeX 的翻译版本
- 先翻译主书文件，然后逐章翻译
- 同时支持拆分章节书籍和带内联 `\chapter{...}` 块的单文件 `main.tex` 书籍
- 使用语言后缀命名翻译后的入口文件，例如 `book_zh.tex` 或 `book_jp.tex`
- 每完成一个单元后重新编译
- 可以在每个单元完成后提交并推送翻译文件夹

## ⚙️ 要求

- `tmux`
- `ffmpeg`
- `pdflatex`
- `pdfunite`
- `pdftotext`
- `yt-dlp`
- `pandoc`（用于 `scripts/export_course_epubs.sh`）
- 用于笔记流水线的 `codex` CLI
- 用于转录的可用 `whisper` conda env
- 如果你希望使用主要字幕路径而不是仅回退 Whisper，则需要 `whisper_with_lang_detect`
- `rsync`（用于口袋 PDF 的可选本地发布同步）

## 🤝 适合场景

当你想要以下内容时，`Video2Book` 很适合：

- 仓库本地流水线，而不是单体应用
- 以转录文本为先的讲义生成
- 基于 tmux 的长时间运行自动化
- 面向学习材料的可复现归档结构

## 🙏 支持

| 捐赠 | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 许可证

本仓库采用 GNU General Public License v3.0 授权。
