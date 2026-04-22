Sprachen: [English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![LazyingArt-Banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://lazying.art)

# Video2Book von LazyingArt LLC

> **Video2Book von LazyingArt LLC**. Websites: [lazying.art](https://lazying.art) und [learn.lazying.art](https://learn.lazying.art).

[![LazyingArt](https://img.shields.io/badge/Website-lazying.art-111827?style=for-the-badge&logo=googlechrome&logoColor=white)](https://lazying.art)
[![Lernen](https://img.shields.io/badge/Learn-learn.lazying.art-1f2937?style=for-the-badge&logo=bookstack&logoColor=white)](https://learn.lazying.art)

[![Toolkit](https://img.shields.io/badge/toolkit-video__to__book-111827?style=for-the-badge&logo=bookstack&logoColor=white)](#)
[![Downloader](https://img.shields.io/badge/stage_1-playlist2videos-1d4ed8?style=for-the-badge&logo=youtube&logoColor=white)](#-pipeline)
[![Transkription](https://img.shields.io/badge/stage_2-videos2subtitles-0f766e?style=for-the-badge&logo=openai&logoColor=white)](#-pipeline)
[![Notizen](https://img.shields.io/badge/stage_3-subtitles2notes-f97316?style=for-the-badge&logo=latex&logoColor=white)](#-pipeline)
[![tmux](https://img.shields.io/badge/runtime-tmux-7c3aed?style=for-the-badge&logo=gnu-bash&logoColor=white)](#-schnellstart)

`Video2Book` ist eine praktische Pipeline, um umfangreiche Videosammlungen in dauerhaftes Lernmaterial zu verwandeln: heruntergeladene Medien, Transkripte mit Zeitstempeln und aus Transkripten abgeleitete Vorlesungsnotizen mit kompilierten PDFs.

## 📚 Flaggschiff-Bücher

Diese Vorschauen verwenden die extrahierte erste Seite jedes veröffentlichten PDFs aus `LazyEarn`
und `LazyLearn`.

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/wealth-from-first-principles/wealth-from-first-principles.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/wealth-from-first-principles/cover-page-1.png" width="180" alt="Cover von Wealth from First Principles" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/dynamic_book/how-you-got-rich.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-rich/cover-page-1.png" width="180" alt="Cover von How You Got Rich" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/jim-rohn-originals-no-ai/course.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-successful/cover-page-1.png" width="180" alt="Cover von How You Got Successful" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/how-you-got-happiness-publication/how-you-got-happiness.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-happiness/cover-page-1.png" width="180" alt="Cover von How You Got Happiness" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/wealth-from-first-principles/wealth-from-first-principles.pdf"><strong>Wealth from First Principles</strong></a><br />
      Geld, Eigentum, Ansprüche und Zinseszinseffekt
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/dynamic_book/how-you-got-rich.pdf"><strong>How You Got Rich?</strong></a><br />
      ein nichtlineares Wohlstandsbuch, aufgebaut aus Interviewbelegen
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/jim-rohn-originals-no-ai/course.pdf"><strong>How You Got Successful?</strong></a><br />
      Jim-Rohn-Erfolgsvorträge, neu geordnet zu einem flüssigeren Buchbogen
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/how-you-got-happiness-publication/how-you-got-happiness.pdf"><strong>How You Got Happiness?</strong></a><br />
      Krishnamurti-Gespräche, geformt zu einem Buch über Aufmerksamkeit, Angst, Meditation und Freiheit
    </td>
  </tr>
</table>

`LazyLearn` veröffentlicht außerdem ein mehrsprachiges Schreibbuch sowie ein abgeschlossenes Buch
zum Gerechtigkeitskurs:

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write/cover-page-1.png" width="180" alt="Cover von How to Speak and Write Englisch" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-zh.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write-zh/cover-page-1.png" width="180" alt="Cover von How to Speak and Write Traditionelles Chinesisch" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-jp.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write-jp/cover-page-1.png" width="180" alt="Cover von How to Speak and Write Japanisch" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/justice-with-michael-sandel/cover-page-1.png" width="180" alt="Cover von Justice with Michael Sandel" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write.pdf"><strong>How to Speak and Write</strong></a><br />
      neu geordnete englische Ausgabe
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
      Michael-Sandel-Kursbuch zur politischen Philosophie
    </td>
  </tr>
</table>

`leonardsusskind` veröffentlicht außerdem zentrale Physikbücher des Theoretical Minimum:

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/quantum_mechanics_theoretical_minimum.png" width="180" alt="Cover von Quantum Mechanics Theoretical Minimum" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/general_relativity_theoretical_minimum.png" width="180" alt="Cover von General Relativity Theoretical Minimum" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/statistical_mechanics_theoretical_minimum_first_page.png" width="180" alt="Cover von Statistical Mechanics Theoretical Minimum" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/cosmology_theoretical_minimum_first_page.png" width="180" alt="Cover von Cosmology Theoretical Minimum" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf"><strong>Quantum Mechanics</strong></a><br />
      Kernbuch des Theoretical Minimum
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf"><strong>General Relativity</strong></a><br />
      Kernbuch des Theoretical Minimum
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf"><strong>Statistical Mechanics</strong></a><br />
      Kernbuch des Theoretical Minimum
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf"><strong>Cosmology</strong></a><br />
      Kernbuch des Theoretical Minimum
    </td>
  </tr>
</table>

## ✨ Was es abdeckt

- Eine Playlist in ein stabiles externes Medienarchiv herunterladen.
- Videos in `.srt`-Untertitel und Markdown mit Zeitstempeln transkribieren.
- Abgeschlossene Transkript-Sammlungen in strukturierte TeX-Notizen und zusammengeführte Kurs-PDFs umwandeln.
- Geordnete Markdown-Materialordner in TeX/PDF-Bücher im Taschenformat umwandeln.
- Lange Aufgaben in `tmux` mit Warteschlangen-Skripten sowie Monitor-/Guard-Skripten ausführen.
- Kompakte Begleit-PDFs im Taschenformat aus fertigem Kurs-LaTeX exportieren.
- Denselben Workflow für umschlossene Kopfzeilen und die Aktualisierung von Abbildungen für normale
  PDFs in voller Größe und Pocket-PDFs in Host-Repos wiederverwenden.

## 🧪 Funktionierende Host-Repos

`Video2Book` wird bereits in mehreren Host-Repos mit unterschiedlichen Archivstrukturen verwendet.

| Host-Repo | Schwerpunkt | Wrapper-Beispiel | Aktuell verfolgte Ausgaben |
| --- | --- | --- | --- |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Yale-Kurs `Financial Markets` mit Robert J. Shiller | [examples/lazyearn/yale-financial-markets/](../examples/lazyearn/yale-financial-markets/) | [Kurs-PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf), [Vorlesungs-PDFs](https://github.com/lachlanchen/LazyEarn/tree/main/generated_course_notes/lazyearn/yale-financial-markets/chapters), [Markdown-Transkripte](https://github.com/lachlanchen/LazyEarn/tree/main/markdown/lazyearn/yale-financial-markets), [Untertitel](https://github.com/lachlanchen/LazyEarn/tree/main/subtitles/lazyearn/yale-financial-markets) |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | Schreibkurs-Adaption für `How You Speak and Write` | [examples/lazylearn/how-you-speak-and-write/](../examples/lazylearn/how-you-speak-and-write/), [examples/lazylearn/justice-with-michael-sandel/](../examples/lazylearn/justice-with-michael-sandel/) | [Kurs-PDF How You Speak and Write](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf), [Kurs-PDF Justice with Michael Sandel](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/justice-with-michael-sandel/course.pdf), [lokale Sprecherkurs-PDFs](https://github.com/lachlanchen/LazyLearn/tree/main/how-to-speak-and-write), [lokales Justice-PDF](https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf), [Vorlesungs-PDFs](https://github.com/lachlanchen/LazyLearn/tree/main/generated_course_notes/lazylearn/how-you-speak-and-write/chapters), [Markdown-Transkripte](https://github.com/lachlanchen/LazyLearn/tree/main/markdown/lazylearn), [Untertitel](https://github.com/lachlanchen/LazyLearn/tree/main/subtitles/lazylearn) |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Vollständiges Leonard-Susskind-Vorlesungsarchiv, Transkriptionspipeline und veröffentlichte Notizbücher | [examples/leonardsusskind/susskind-physics-archive/](../examples/leonardsusskind/susskind-physics-archive/) | [Ordner veröffentlichter Bücher](https://github.com/lachlanchen/leonardsusskind/tree/main), [Advanced-Quantum-PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf), [Topics-in-String-Theory-PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf), [Particle-Physics-3-PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_particle_physics_3/particle_physics_3_supersymmetry_and_grand_unification.pdf), [Markdown-Transkripte](https://github.com/lachlanchen/leonardsusskind/tree/main/markdown), [Untertitel](https://github.com/lachlanchen/leonardsusskind/tree/main/subtitles) |

## 📘 Bücher und PDFs

Die dritte Stufe erzeugt in Host-Repos bereits echte buchähnliche Ausgaben:

- zusammengeführte Kursbücher wie `course.pdf` oder ein vom Host veröffentlichtes kanonisches Namensformat
- PDFs pro Vorlesung unter `generated_course_notes/.../chapters/`
- Transkriptbäume in `markdown/` und Untertitelbäume in `subtitles/`

Weitere veröffentlichte Bücher und Kursausgaben:

| Host-Repo | Titel | Haupt-PDF | Notizen |
| --- | --- | --- | --- |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Yale Financial Markets | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf) | Robert-J.-Shiller-Vorlesungsbuch mit Varianten in voller Größe und im Taschenformat |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Hard Knocks Interviews | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/course.pdf) | direkte Zusammenstellung Vorlesung für Vorlesung |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | High-Growth Dossier | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/high-growth-stocks/high-growth-stocks.pdf) | älteres Forschungsbuch mit Pocket-Exporten |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Quod Tango Muto | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/quod-tango-muto/quod-tango-muto.pdf) | Forschungsbuch mit lateinischem Motto und Pocket-Exporten |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | How You Speak and Write | [PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf) | Schreibkurs-Adaption |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | Justice with Michael Sandel | [PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/justice-with-michael-sandel/course.pdf) | Kursbuch zur politischen Philosophie |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Classical Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/classical_mechanics_theoretical_minimum.pdf) | konsolidiertes Buch in `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Quantum Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/quantum_mechanics_theoretical_minimum.pdf) | zentrales TTM-Buch in `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Special Relativity (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/special_relativity_theoretical_minimum.pdf) | zentrales TTM-Buch in `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | General Relativity (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/general_relativity_theoretical_minimum.pdf) | zentrales TTM-Buch in `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Statistical Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/statistical_mechanics_theoretical_minimum.pdf) | zentrales TTM-Buch in `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Cosmology (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/cosmology_theoretical_minimum.pdf) | zentrales TTM-Buch in `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Advanced Quantum Mechanics | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf) | ergänzender Physiktitel |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Topics in String Theory | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf) | ergänzender Kosmologie-/String-Titel |

Weitere konsolidierte Susskind-Titel sind in [all_notes](https://github.com/lachlanchen/leonardsusskind/tree/main/all_notes) verfügbar.

### Verweise auf lokale Geschwister-Repos

Wenn du diese Repos aus einem gemeinsamen übergeordneten Verzeichnis ausführst (zum Beispiel `/home/lachlan/ProjectsLFS`), sind dieselben Bücher auch über lokale Pfade adressierbar:

- `../LazyLearn/justice-with-michael-sandel/justice-with-michael-sandel.pdf`
- `../LazyLearn/how-to-speak-and-write/how-to-speak-and-write.pdf`
- `../LazyEarn/generated_course_notes/lazyearn/yale-financial-markets/course.pdf`
- `../leonardsusskind/<sibling-folder>/...` (Kurs- und veröffentlichte Buch-PDFs in diesem Repo)

## 🧩 Pipeline

| Stufe | Modul | Zweck |
| --- | --- | --- |
| 1 | `playlist2videos/` | Eine Playlist mit `yt-dlp` herunterladen oder aktualisieren, Logs behalten und bereits archivierte Elemente überspringen. |
| 2 | `videos2subtitles/` | Die archivierten Medien in `subtitles/` und `markdown/` transkribieren. |
| 3 | `subtitles2notes/` | Abgeschlossene Transkripte in Kapitel-TeX, Vorlesungs-PDFs und zusammengeführte Kurs-PDFs umwandeln. |
| 4 | `scripts/process_markdown_material_book.py` | Geordnete Quell-Markdown-Ordner in generierte TeX/PDF-Bücher im Taschenformat umwandeln und zugehörige Bilder an Codex übergeben. |
| 5 | `scripts/start_markdown_material_book_tmux.sh` | Den Markdown-Material-Buchschreiber in `tmux` ausführen, mit fortsetzbarer Verarbeitung einer Quelle nach der anderen. |
| 6 | `scripts/export_course_pocket_pdfs.sh` | Fertige `course.tex`-Ausgaben in Pocket-/A5-Varianten für Veröffentlichungspakete neu bauen und zugeordnete Overfull-Berichte ausgeben. |
| 7 | `scripts/export_tex_book_pocket_pdf.sh` | Ein eigenständiges TeX-Buch/einen TeX-Artikel in ein Begleit-PDF im Taschenformat neu bauen und in den Dokumentationsbaum des Host-Repos synchronisieren. |
| 8 | `subtitles2notes/templates/lecture_notes_common_preamble.tex` | Gemeinsame Header-/Layout-Quelle für Kurs-PDFs in Normalgröße, die von generierten Büchern verwendet wird. |
| 9 | `scripts/fix_course_pocket_overfulls.sh` | Eine Kursvariante iterativ bearbeiten: exportieren, berichten, Codex-Patch anwenden und erneut exportieren, bis behebbare Overfulls sinken. |
| 10 | `scripts/fix_latex_project_overfulls.sh` | Generischer LaTeX-Overflow-Fixer für jedes Repo/Projekt, das mit `pdflatex` oder einem benutzerdefinierten Kompilierbefehl gebaut werden kann. |
| 11 | `scripts/recheck_course_figures.py` | Vorlesungsabbildungen mit Screenshot-Charakter erneut gegen Transkriptkontext und Ersatz-Videoframes prüfen. |
| 12 | `scripts/export_course_epubs.sh` | Fertige `course.tex`-Ausgaben direkt in EPUB3 neu bauen. |

## 🚀 Schnellstart

Direkt klonen:

```bash
git clone git@github.com:lachlanchen/Video2Book.git
cd Video2Book
```

Oder als Submodul zu einem anderen Repo hinzufügen:

```bash
git submodule add git@github.com:lachlanchen/Video2Book.git Video2Book
git submodule update --init --recursive
```

## 🏗️ Layout des Host-Repos

`Video2Book` erwartet, aus einem Host-Repo heraus ausgeführt zu werden, das die Arbeitsausgaben speichert:

- `subtitles/`
- `markdown/`
- `generated_course_notes/`
- `.lecture-notes-work/`

Die Videodateien selbst werden normalerweise außerhalb des Host-Repos in einem Medien-Workspace wie diesem abgelegt:

- `/home/lachlan/ProjectsLFS/YoutubeDownloader`

## 🛠️ Typische Verwendung

Aus dem Root des Host-Repos:

```bash
./Video2Book/scripts/download_susskind_playlist.sh
./Video2Book/scripts/start_transcription_tmux.sh
./Video2Book/scripts/start_transcription_monitor_tmux.sh
./Video2Book/scripts/start_course_notes_tmux.sh
./Video2Book/scripts/start_course_notes_monitor_tmux.sh
```

Downloader im Dry-Run ausführen:

```bash
./Video2Book/scripts/download_susskind_playlist.sh --dry-run
```

Eine Warteschlange zum Schreiben von Notizen für einen Kurs starten:

```bash
./Video2Book/scripts/start_course_notes_tmux.sh --course supplementary/advanced_quantum_mechanics/2013_fall
```

Kompakte PDFs für alle abgeschlossenen Kurse exportieren (zum Beispiel in `leonardsusskind`):

```bash
./Video2Book/scripts/export_course_pocket_pdfs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
```

Ein eigenständiges Buch in `investment_pdfs/` in Varianten im Taschenformat exportieren:

```bash
./Video2Book/scripts/export_tex_book_pocket_pdf.sh \
  --repo-root /home/lachlan/ProjectsLFS/LazyEarn \
  --project-root /home/lachlan/ProjectsLFS/LazyEarn/investment_pdfs/wealth-from-first-principles \
  --main-tex wealth-from-first-principles.tex \
  --font-mode onepointtwo \
  --suffix pocket_1_2x
```

Den Codex-gesteuerten Overflow-Fixer für eine Kursvariante mit schmalem Layout ausführen:

```bash
./Video2Book/scripts/start_pocket_overflow_fix_tmux.sh \
  --course core/statistical_mechanics/2013_spring_theoretical_minimum \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

Die Warteschlange in tmux über alle abgeschlossenen Susskind-Kurse hinweg ausführen, jeweils einen Kurs nach dem anderen:

```bash
./Video2Book/scripts/start_pocket_overflow_fix_tmux.sh \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

Den generischen LaTeX-Fixer auf einem beliebigen Projekt ausführen:

```bash
./Video2Book/scripts/fix_latex_project_overfulls.sh \
  --repo-root /path/to/repo \
  --project-root /path/to/repo/book \
  --main-tex main.tex \
  --model gpt-5.4 \
  --reasoning medium
```

EPUB3 direkt aus TeX für alle abgeschlossenen Kurse exportieren:

```bash
./Video2Book/scripts/export_course_epubs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
```

Host-spezifische Wrapper können unter `examples/` liegen. Aktuell enthaltene Muster:

- `examples/lazyearn/yale-financial-markets/`
- `examples/lazylearn/how-you-speak-and-write/`
- `examples/leonardsusskind/susskind-physics-archive/`

## 🎬 Aktuelles Standardbeispiel

Der enthaltene Downloader verwendet standardmäßig die Leonard-Susskind-Physik-Playlist:

- <https://www.youtube.com/playlist?list=PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG>

Dieser Standard ist nur ein funktionierendes Beispiel. Der Code ist so strukturiert, dass andere Host-Repos dieselbe Pipeline an andere Vorlesungsarchive anpassen können.

## 📦 Modulübersicht

- [playlist2videos](../playlist2videos)
- [videos2subtitles](../videos2subtitles)
- [subtitles2notes](../subtitles2notes)
- [scripts](../scripts)
- [Pocket-Export-Handoff](../references/pocket-size-course-pdfs-handoff.md)
- [A4- und Pocket-Layout-Handoff](../references/a4-and-pocket-pdf-layout-handoff.md)
- [README-Buchvorschau-Handoff](../references/readme-book-preview-handoff.md)
- [LaTeX-Overflow-Fixer-Handoff](../references/latex-overflow-fixer-handoff.md)
- [EPUB-Export-Handoff](../references/tex-to-epub-handoff.md)

## 📚 Hinweise zur Host-Anpassung

- [references/lazylearn-course-adaptation.md](../references/lazylearn-course-adaptation.md)
- [references/lazyearn-yale-financial-markets-adaptation.md](../references/lazyearn-yale-financial-markets-adaptation.md)
- [references/nanobanana-2-book-cover-handoff.md](../references/nanobanana-2-book-cover-handoff.md)
- [references/readme-book-preview-handoff.md](../references/readme-book-preview-handoff.md)
- [references/a4-and-pocket-pdf-layout-handoff.md](../references/a4-and-pocket-pdf-layout-handoff.md)
- [references/latex-overflow-fixer-handoff.md](../references/latex-overflow-fixer-handoff.md)
- [references/tex-book-translation-workflow.md](../references/tex-book-translation-workflow.md)
- [references/tex-to-epub-handoff.md](../references/tex-to-epub-handoff.md)

## 🎨 Dienstprogramm für Buchcover

`Video2Book` enthält außerdem einen lokalen Nano-Banana-2-Helfer zur Erstellung redaktioneller Buchcover:

- Skript: [scripts/book_cover_nanobanana.py](../scripts/book_cover_nanobanana.py)
- Anleitung: [references/nanobanana-2-book-cover-handoff.md](../references/nanobanana-2-book-cover-handoff.md)
- env-Vorlage: [.env.example](../.env.example)
- Beispiel-Prompt für das aktuelle Buch: [examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt](../examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt)

Er verwendet die GRS-AI-Submit-and-Poll-Mechanik aus der benachbarten Nano-Banana-Arbeit wieder, ersetzt aber die Segmentierungs-Prompts durch einen Buchcover-Prompt und speichert pro Lauf eine saubere Ausgabespur.

## 🌐 Dienstprogramm für Buchübersetzungen

`Video2Book` kann außerdem ein fertiges Vorlesungsnotizbuch in benachbarte
Sprachordner wie `zh/` und `jp/` übersetzen, während TeX-Struktur,
Gleichungen und Bilder intakt bleiben.

- Manager: [scripts/translate_tex_book.py](../scripts/translate_tex_book.py)
- Loop-Runner: [scripts/process_book_translation_one_by_one.sh](../scripts/process_book_translation_one_by_one.sh)
- tmux-Starter: [scripts/start_book_translation_tmux.sh](../scripts/start_book_translation_tmux.sh)
- Workflow-Notiz: [references/tex-book-translation-workflow.md](../references/tex-book-translation-workflow.md)

Die Übersetzungsschleife:

- initialisiert eine für XeLaTeX bereite übersetzte Ausgabe
- übersetzt zuerst die Hauptbuchdatei, danach jedes Kapitel
- unterstützt sowohl Bücher mit aufgeteilten Kapiteln als auch einteilige `main.tex`-Bücher mit inline gesetzten `\chapter{...}`-Blöcken
- benennt übersetzte Einstiegdateien mit einem Sprachsuffix wie `book_zh.tex` oder `book_jp.tex`
- kompiliert nach jeder Einheit neu
- kann den übersetzten Ordner nach jeder abgeschlossenen Einheit committen und pushen

## ⚙️ Anforderungen

- `tmux`
- `ffmpeg`
- `pdflatex`
- `pdfunite`
- `pdftotext`
- `yt-dlp`
- `pandoc` (für `scripts/export_course_epubs.sh`)
- `codex` CLI für die Notizpipeline
- eine funktionierende `whisper`-conda-Umgebung für die Transkription
- `whisper_with_lang_detect`, wenn du den primären Untertitelpfad statt nur des Fallback-Whisper verwenden möchtest
- `rsync` (für optionale lokale Veröffentlichungssynchronisierung von Pocket-PDFs)

## 🤝 Gute Passung

`Video2Book` passt gut, wenn du Folgendes möchtest:

- eine repo-lokale Pipeline statt einer monolithischen App
- transkriptbasierte Erstellung von Vorlesungsnotizen
- tmux-basierte Automatisierung für lange laufende Aufgaben
- reproduzierbare Archivstruktur für Lernmaterial

## 🙏 Support

| Spenden | PayPal | Stripe |
| --- | --- | --- |
| [![Spenden](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Lizenz

Dieses Repository ist unter der GNU General Public License v3.0 lizenziert.