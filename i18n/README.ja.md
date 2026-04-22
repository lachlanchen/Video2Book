言語: [English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://lazying.art)

# Video2Book by LazyingArt LLC

> **Video2Book by LazyingArt LLC**。ウェブサイト: [lazying.art](https://lazying.art) および [learn.lazying.art](https://learn.lazying.art)。

[![LazyingArt](https://img.shields.io/badge/Website-lazying.art-111827?style=for-the-badge&logo=googlechrome&logoColor=white)](https://lazying.art)
[![Learn](https://img.shields.io/badge/Learn-learn.lazying.art-1f2937?style=for-the-badge&logo=bookstack&logoColor=white)](https://learn.lazying.art)

[![Toolkit](https://img.shields.io/badge/toolkit-video__to__book-111827?style=for-the-badge&logo=bookstack&logoColor=white)](#)
[![Downloader](https://img.shields.io/badge/stage_1-playlist2videos-1d4ed8?style=for-the-badge&logo=youtube&logoColor=white)](#-pipeline)
[![Transcription](https://img.shields.io/badge/stage_2-videos2subtitles-0f766e?style=for-the-badge&logo=openai&logoColor=white)](#-pipeline)
[![Notes](https://img.shields.io/badge/stage_3-subtitles2notes-f97316?style=for-the-badge&logo=latex&logoColor=white)](#-pipeline)
[![tmux](https://img.shields.io/badge/runtime-tmux-7c3aed?style=for-the-badge&logo=gnu-bash&logoColor=white)](#-quick-start)

`Video2Book` は、長尺動画コレクションを、ダウンロード済みメディア、タイムスタンプ付き文字起こし、文字起こしから作成した講義ノートとコンパイル済み PDF という、長く使える学習資料に変換するための実用的なパイプラインです。

## 📚 代表的な書籍

これらのプレビューは、`LazyEarn` と `LazyLearn` で公開されている各 PDF の抽出済み先頭ページを使用しています。

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/wealth-from-first-principles/wealth-from-first-principles.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/wealth-from-first-principles/cover-page-1.png" width="180" alt="Wealth from First Principles の表紙" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/dynamic_book/how-you-got-rich.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-rich/cover-page-1.png" width="180" alt="How You Got Rich の表紙" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/jim-rohn-originals-no-ai/course.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-successful/cover-page-1.png" width="180" alt="How You Got Successful の表紙" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/how-you-got-happiness-publication/how-you-got-happiness.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-happiness/cover-page-1.png" width="180" alt="How You Got Happiness の表紙" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/wealth-from-first-principles/wealth-from-first-principles.pdf"><strong>Wealth from First Principles</strong></a><br />
      お金、所有、請求権、複利
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/dynamic_book/how-you-got-rich.pdf"><strong>How You Got Rich?</strong></a><br />
      インタビューの証拠から構築された非線形の富の本
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/jim-rohn-originals-no-ai/course.pdf"><strong>How You Got Successful?</strong></a><br />
      Jim Rohn の成功講義を、より滑らかな本の流れに並べ替えたもの
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/how-you-got-happiness-publication/how-you-got-happiness.pdf"><strong>How You Got Happiness?</strong></a><br />
      Krishnamurti の講話を、注意、恐れ、瞑想、自由についての本として形にしたもの
    </td>
  </tr>
</table>

`LazyLearn` では、多言語のライティング本と完成済みの正義論コース本も公開しています。

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write/cover-page-1.png" width="180" alt="How to Speak and Write English の表紙" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-zh.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write-zh/cover-page-1.png" width="180" alt="How to Speak and Write Traditional Chinese の表紙" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-jp.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write-jp/cover-page-1.png" width="180" alt="How to Speak and Write Japanese の表紙" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/justice-with-michael-sandel/cover-page-1.png" width="180" alt="Justice with Michael Sandel の表紙" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write.pdf"><strong>How to Speak and Write</strong></a><br />
      並べ替え済み英語版
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-zh.pdf"><strong>如何說話與寫作</strong></a><br />
      繁体字中国語版
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-jp.pdf"><strong>話し方と書き方</strong></a><br />
      日本語版
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf"><strong>Justice with Michael Sandel</strong></a><br />
      Michael Sandel の政治哲学コース本
    </td>
  </tr>
</table>

`leonardsusskind` でも、Theoretical Minimum 物理学の中核書籍を公開しています。

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/quantum_mechanics_theoretical_minimum.png" width="180" alt="Quantum Mechanics Theoretical Minimum の表紙" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/general_relativity_theoretical_minimum.png" width="180" alt="General Relativity Theoretical Minimum の表紙" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/statistical_mechanics_theoretical_minimum_first_page.png" width="180" alt="Statistical Mechanics Theoretical Minimum の表紙" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/cosmology_theoretical_minimum_first_page.png" width="180" alt="Cosmology Theoretical Minimum の表紙" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf"><strong>Quantum Mechanics</strong></a><br />
      Theoretical Minimum 中核書
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf"><strong>General Relativity</strong></a><br />
      Theoretical Minimum 中核書
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf"><strong>Statistical Mechanics</strong></a><br />
      Theoretical Minimum 中核書
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf"><strong>Cosmology</strong></a><br />
      Theoretical Minimum 中核書
    </td>
  </tr>
</table>

## ✨ 対象内容

- プレイリストを安定した外部メディアアーカイブへダウンロードします。
- 動画を `.srt` 字幕とタイムスタンプ付き Markdown に文字起こしします。
- 完成した文字起こし一式を、構造化された TeX ノートと結合済みコース PDF に変換します。
- 順序付き Markdown 素材フォルダを、ポケットサイズの TeX/PDF 書籍に変換します。
- キュースクリプトと監視/ガードスクリプトを使って、長時間ジョブを `tmux` で実行します。
- 完成済みコース LaTeX から、コンパクトなポケット形式の副読 PDF をエクスポートします。
- 通常のフルサイズ PDF とポケット PDF の両方で、ホストリポジトリをまたいで同じラップ済みヘッダーと図の更新ワークフローを再利用します。

## 🧪 稼働中のホストリポジトリ

`Video2Book` は、異なるアーカイブ構造を持つ複数のホストリポジトリですでに使われています。

| ホストリポジトリ | 焦点 | ラッパー例 | 現在追跡中の出力 |
| --- | --- | --- | --- |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Robert J. Shiller による Yale `Financial Markets` コース | [examples/lazyearn/yale-financial-markets/](../examples/lazyearn/yale-financial-markets/) | [course PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf), [lecture PDFs](https://github.com/lachlanchen/LazyEarn/tree/main/generated_course_notes/lazyearn/yale-financial-markets/chapters), [markdown transcripts](https://github.com/lachlanchen/LazyEarn/tree/main/markdown/lazyearn/yale-financial-markets), [subtitles](https://github.com/lachlanchen/LazyEarn/tree/main/subtitles/lazyearn/yale-financial-markets) |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | `How You Speak and Write` 向けライティングコースの翻案 | [examples/lazylearn/how-you-speak-and-write/](../examples/lazylearn/how-you-speak-and-write/), [examples/lazylearn/justice-with-michael-sandel/](../examples/lazylearn/justice-with-michael-sandel/) | [How You Speak and Write course PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf), [Justice with Michael Sandel course PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/justice-with-michael-sandel/course.pdf), [local speaker course PDFs](https://github.com/lachlanchen/LazyLearn/tree/main/how-to-speak-and-write), [local justice PDF](https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf), [lecture PDFs](https://github.com/lachlanchen/LazyLearn/tree/main/generated_course_notes/lazylearn/how-you-speak-and-write/chapters), [markdown transcripts](https://github.com/lachlanchen/LazyLearn/tree/main/markdown/lazylearn), [subtitles](https://github.com/lachlanchen/LazyLearn/tree/main/subtitles/lazylearn) |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Leonard Susskind 講義アーカイブ全体、文字起こしパイプライン、公開済みノート本 | [examples/leonardsusskind/susskind-physics-archive/](../examples/leonardsusskind/susskind-physics-archive/) | [published books folder](https://github.com/lachlanchen/leonardsusskind/tree/main), [advanced quantum PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf), [topics in string theory PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf), [particle physics 3 PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_particle_physics_3/particle_physics_3_supersymmetry_and_grand_unification.pdf), [markdown transcripts](https://github.com/lachlanchen/leonardsusskind/tree/main/markdown), [subtitles](https://github.com/lachlanchen/leonardsusskind/tree/main/subtitles) |

## 📘 書籍と PDF

第 3 段階では、ホストリポジトリ内ですでに本のような実出力を生成しています。

- `course.pdf` などの結合済みコース本、またはホストが公開する正式名称
- `generated_course_notes/.../chapters/` 配下の講義別 PDF
- `markdown/` 内の文字起こしツリーと `subtitles/` 内の字幕ツリー

その他の公開済み書籍とコース出力:

| ホストリポジトリ | タイトル | メイン PDF | ノート |
| --- | --- | --- | --- |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Yale Financial Markets | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf) | フルサイズ版とポケット版を備えた Robert J. Shiller 講義本 |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Hard Knocks Interviews | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/course.pdf) | 講義ごとの直接コンパイル |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | High-Growth Dossier | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/high-growth-stocks/high-growth-stocks.pdf) | ポケット版エクスポートを備えた旧来の調査本 |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Quod Tango Muto | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/quod-tango-muto/quod-tango-muto.pdf) | ポケット版エクスポートを備えたラテン語標語の調査本 |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | How You Speak and Write | [PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf) | ライティングコースの翻案 |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | Justice with Michael Sandel | [PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/justice-with-michael-sandel/course.pdf) | 政治哲学コース本 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Classical Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/classical_mechanics_theoretical_minimum.pdf) | `all_notes/` 内の統合本 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Quantum Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/quantum_mechanics_theoretical_minimum.pdf) | `all_notes/` 内の中核 TTM 本 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Special Relativity (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/special_relativity_theoretical_minimum.pdf) | `all_notes/` 内の中核 TTM 本 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | General Relativity (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/general_relativity_theoretical_minimum.pdf) | `all_notes/` 内の中核 TTM 本 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Statistical Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/statistical_mechanics_theoretical_minimum.pdf) | `all_notes/` 内の中核 TTM 本 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Cosmology (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/cosmology_theoretical_minimum.pdf) | `all_notes/` 内の中核 TTM 本 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Advanced Quantum Mechanics | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf) | 物理学の補足タイトル |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Topics in String Theory | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf) | 宇宙論 / 弦理論の補足タイトル |

その他の Susskind 統合タイトルは [all_notes](https://github.com/lachlanchen/leonardsusskind/tree/main/all_notes) で利用できます。

### ローカルの兄弟リポジトリへのポインタ

これらのリポジトリを共有親ディレクトリ（例: `/home/lachlan/ProjectsLFS`）から実行している場合、同じ書籍はローカルパスからも参照できます。

- `../LazyLearn/justice-with-michael-sandel/justice-with-michael-sandel.pdf`
- `../LazyLearn/how-to-speak-and-write/how-to-speak-and-write.pdf`
- `../LazyEarn/generated_course_notes/lazyearn/yale-financial-markets/course.pdf`
- `../leonardsusskind/<sibling-folder>/...`（そのリポジトリ内のコース PDF と公開本 PDF）

## 🧩 パイプライン

| 段階 | モジュール | 目的 |
| --- | --- | --- |
| 1 | `playlist2videos/` | `yt-dlp` でプレイリストをダウンロードまたは更新し、ログを保持し、すでにアーカイブ済みの項目をスキップします。 |
| 2 | `videos2subtitles/` | アーカイブ済みメディアを `subtitles/` と `markdown/` に文字起こしします。 |
| 3 | `subtitles2notes/` | 完成した文字起こしを章 TeX、講義 PDF、結合済みコース PDF に変換します。 |
| 4 | `scripts/process_markdown_material_book.py` | 順序付きソース Markdown フォルダを、関連画像を Codex に渡しながら、生成済みポケットサイズ TeX/PDF 書籍に変換します。 |
| 5 | `scripts/start_markdown_material_book_tmux.sh` | Markdown 素材の書籍作成を `tmux` で実行し、再開に強い 1 ソースずつの処理を行います。 |
| 6 | `scripts/export_course_pocket_pdfs.sh` | 完成済み `course.tex` 出力を、公開パッケージ向けのポケット/A5 版として再ビルドし、対応付け済み overfull レポートを出力します。 |
| 7 | `scripts/export_tex_book_pocket_pdf.sh` | 単体の TeX 書籍/記事をポケットサイズの副読 PDF として再ビルドし、ホストリポジトリの docs ツリーに同期します。 |
| 8 | `subtitles2notes/templates/lecture_notes_common_preamble.tex` | 生成書籍で使われる共有の通常サイズコース PDF ヘッダー/レイアウトソースです。 |
| 9 | `scripts/fix_course_pocket_overfulls.sh` | 1 つのコース版に対して、エクスポート、レポート、Codex パッチ、再エクスポートを、対応可能な overfull が減るまで繰り返します。 |
| 10 | `scripts/fix_latex_project_overfulls.sh` | `pdflatex` またはカスタムコンパイルコマンドでビルドできる任意のリポジトリ/プロジェクト向けの汎用 LaTeX はみ出し修正ツールです。 |
| 11 | `scripts/recheck_course_figures.py` | スクリーンショット風の講義図を、文字起こしコンテキストと差し替え動画フレームに照らして再監査します。 |
| 12 | `scripts/export_course_epubs.sh` | 完成済み `course.tex` 出力を直接 EPUB3 に再ビルドします。 |

## 🚀 クイックスタート

直接クローンします。

```bash
git clone git@github.com:lachlanchen/Video2Book.git
cd Video2Book
```

または、別のリポジトリにサブモジュールとして追加します。

```bash
git submodule add git@github.com:lachlanchen/Video2Book.git Video2Book
git submodule update --init --recursive
```

## 🏗️ ホストリポジトリのレイアウト

`Video2Book` は、作業出力を保存するホストリポジトリから実行されることを想定しています。

- `subtitles/`
- `markdown/`
- `generated_course_notes/`
- `.lecture-notes-work/`

動画ファイル自体は通常、次のようなメディア用ワークスペース内でホストリポジトリの外に保持されます。

- `/home/lachlan/ProjectsLFS/YoutubeDownloader`

## 🛠️ 一般的な使い方

ホストリポジトリのルートから:

```bash
./Video2Book/scripts/download_susskind_playlist.sh
./Video2Book/scripts/start_transcription_tmux.sh
./Video2Book/scripts/start_transcription_monitor_tmux.sh
./Video2Book/scripts/start_course_notes_tmux.sh
./Video2Book/scripts/start_course_notes_monitor_tmux.sh
```

ダウンローダーをドライランします。

```bash
./Video2Book/scripts/download_susskind_playlist.sh --dry-run
```

1 つのコース向けにノート作成キューを開始します。

```bash
./Video2Book/scripts/start_course_notes_tmux.sh --course supplementary/advanced_quantum_mechanics/2013_fall
```

完成したすべてのコースのコンパクト PDF をエクスポートします（例: `leonardsusskind` 内）。

```bash
./Video2Book/scripts/export_course_pocket_pdfs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
```

`investment_pdfs/` 内の単体書籍をポケットサイズ版としてエクスポートします。

```bash
./Video2Book/scripts/export_tex_book_pocket_pdf.sh \
  --repo-root /home/lachlan/ProjectsLFS/LazyEarn \
  --project-root /home/lachlan/ProjectsLFS/LazyEarn/investment_pdfs/wealth-from-first-principles \
  --main-tex wealth-from-first-principles.tex \
  --font-mode onepointtwo \
  --suffix pocket_1_2x
```

1 つの狭幅レイアウトのコース版に対して、Codex 駆動のはみ出し修正ツールを実行します。

```bash
./Video2Book/scripts/start_pocket_overflow_fix_tmux.sh \
  --course core/statistical_mechanics/2013_spring_theoretical_minimum \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

完成済み Susskind コース全体に対し、1 度に 1 コースずつ tmux でキューを実行します。

```bash
./Video2Book/scripts/start_pocket_overflow_fix_tmux.sh \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

任意のプロジェクトで汎用 LaTeX 修正ツールを実行します。

```bash
./Video2Book/scripts/fix_latex_project_overfulls.sh \
  --repo-root /path/to/repo \
  --project-root /path/to/repo/book \
  --main-tex main.tex \
  --model gpt-5.4 \
  --reasoning medium
```

完成済みの全コースについて、TeX から直接 EPUB3 をエクスポートします。

```bash
./Video2Book/scripts/export_course_epubs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
```

ホスト固有のラッパーは `examples/` 配下に置くことができます。現在同梱されているパターン:

- `examples/lazyearn/yale-financial-markets/`
- `examples/lazylearn/how-you-speak-and-write/`
- `examples/leonardsusskind/susskind-physics-archive/`

## 🎬 現在のデフォルト例

同梱のダウンローダーは、デフォルトで Leonard Susskind の物理学プレイリストを使います。

- <https://www.youtube.com/playlist?list=PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG>

このデフォルトは、動作する例にすぎません。コードは、他のホストリポジトリが同じパイプラインを別の講義アーカイブに適用できるように構成されています。

## 📦 モジュールマップ

- [playlist2videos](../playlist2videos)
- [videos2subtitles](../videos2subtitles)
- [subtitles2notes](../subtitles2notes)
- [scripts](../scripts)
- [Pocket export handoff](../references/pocket-size-course-pdfs-handoff.md)
- [A4 and pocket layout handoff](../references/a4-and-pocket-pdf-layout-handoff.md)
- [README book preview handoff](../references/readme-book-preview-handoff.md)
- [LaTeX overflow fixer handoff](../references/latex-overflow-fixer-handoff.md)
- [EPUB export handoff](../references/tex-to-epub-handoff.md)

## 📚 ホスト適応ノート

- [references/lazylearn-course-adaptation.md](../references/lazylearn-course-adaptation.md)
- [references/lazyearn-yale-financial-markets-adaptation.md](../references/lazyearn-yale-financial-markets-adaptation.md)
- [references/nanobanana-2-book-cover-handoff.md](../references/nanobanana-2-book-cover-handoff.md)
- [references/readme-book-preview-handoff.md](../references/readme-book-preview-handoff.md)
- [references/a4-and-pocket-pdf-layout-handoff.md](../references/a4-and-pocket-pdf-layout-handoff.md)
- [references/latex-overflow-fixer-handoff.md](../references/latex-overflow-fixer-handoff.md)
- [references/tex-book-translation-workflow.md](../references/tex-book-translation-workflow.md)
- [references/tex-to-epub-handoff.md](../references/tex-to-epub-handoff.md)

## 🎨 ブックカバー用ユーティリティ

`Video2Book` には、編集用途のブックカバー生成向けローカル Nano Banana 2 ヘルパーも含まれています。

- script: [scripts/book_cover_nanobanana.py](../scripts/book_cover_nanobanana.py)
- guide: [references/nanobanana-2-book-cover-handoff.md](../references/nanobanana-2-book-cover-handoff.md)
- env template: [.env.example](../.env.example)
- current-book example prompt: [examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt](../examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt)

これは兄弟 Nano Banana 作業から GRS AI の送信・ポーリング機構を再利用しますが、セグメンテーションプロンプトをブックカバープロンプトに差し替え、実行ごとにクリーンな出力トレースを保存します。

## 🌐 書籍翻訳ユーティリティ

`Video2Book` は、完成済み講義ノート本を `zh/` や `jp/` などの兄弟言語フォルダへ翻訳することもできます。その際、TeX 構造、数式、画像はそのまま維持されます。

- manager: [scripts/translate_tex_book.py](../scripts/translate_tex_book.py)
- loop runner: [scripts/process_book_translation_one_by_one.sh](../scripts/process_book_translation_one_by_one.sh)
- tmux starter: [scripts/start_book_translation_tmux.sh](../scripts/start_book_translation_tmux.sh)
- workflow note: [references/tex-book-translation-workflow.md](../references/tex-book-translation-workflow.md)

翻訳ループは次を行います。

- XeLaTeX 対応の翻訳版を初期化します
- まずメインの書籍ファイルを翻訳し、その後各章を翻訳します
- 分割章の本と、インライン `\chapter{...}` ブロックを持つ単一ファイル `main.tex` 本の両方をサポートします
- 翻訳済みエントリファイルに `book_zh.tex` や `book_jp.tex` のような言語サフィックスを付けます
- 各ユニットの後に再コンパイルします
- 完了した各ユニットの後に、翻訳済みフォルダをコミットおよびプッシュできます

## ⚙️ 要件

- `tmux`
- `ffmpeg`
- `pdflatex`
- `pdfunite`
- `pdftotext`
- `yt-dlp`
- `pandoc`（`scripts/export_course_epubs.sh` 用）
- ノートパイプライン用の `codex` CLI
- 文字起こし用の動作する `whisper` conda 環境
- フォールバック専用 Whisper ではなく主要字幕パスを使いたい場合は `whisper_with_lang_detect`
- `rsync`（ポケット PDF の任意のローカル公開同期用）

## 🤝 適した用途

`Video2Book` は、次のような場合に適しています。

- モノリシックなアプリではなく、リポジトリローカルなパイプラインが欲しい
- 文字起こしを起点にした講義ノート生成を行いたい
- tmux ベースの長時間自動処理が必要
- 学習資料向けに再現可能なアーカイブ構造が欲しい

## 🙏 サポート

| 寄付 | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## ライセンス

このリポジトリは GNU General Public License v3.0 の下でライセンスされています。