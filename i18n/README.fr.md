Langues : [English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![Bannière LazyingArt](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://lazying.art)

# Video2Book par LazyingArt LLC

> **Video2Book par LazyingArt LLC**. Sites web : [lazying.art](https://lazying.art) et [learn.lazying.art](https://learn.lazying.art).

[![LazyingArt](https://img.shields.io/badge/Website-lazying.art-111827?style=for-the-badge&logo=googlechrome&logoColor=white)](https://lazying.art)
[![Learn](https://img.shields.io/badge/Learn-learn.lazying.art-1f2937?style=for-the-badge&logo=bookstack&logoColor=white)](https://learn.lazying.art)

[![Toolkit](https://img.shields.io/badge/toolkit-video__to__book-111827?style=for-the-badge&logo=bookstack&logoColor=white)](#)
[![Downloader](https://img.shields.io/badge/stage_1-playlist2videos-1d4ed8?style=for-the-badge&logo=youtube&logoColor=white)](#-pipeline)
[![Transcription](https://img.shields.io/badge/stage_2-videos2subtitles-0f766e?style=for-the-badge&logo=openai&logoColor=white)](#-pipeline)
[![Notes](https://img.shields.io/badge/stage_3-subtitles2notes-f97316?style=for-the-badge&logo=latex&logoColor=white)](#-pipeline)
[![tmux](https://img.shields.io/badge/runtime-tmux-7c3aed?style=for-the-badge&logo=gnu-bash&logoColor=white)](#-quick-start)

`Video2Book` est un pipeline pratique pour transformer des collections vidéo longues en supports d’étude durables : médias téléchargés, transcriptions horodatées et notes de cours dérivées des transcriptions avec PDF compilés.

## 📚 Livres phares

Ces aperçus utilisent la première page extraite de chaque PDF publié depuis `LazyEarn`
et `LazyLearn`.

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/wealth-from-first-principles/wealth-from-first-principles.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/wealth-from-first-principles/cover-page-1.png" width="180" alt="Couverture de Wealth from First Principles" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/dynamic_book/how-you-got-rich.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-rich/cover-page-1.png" width="180" alt="Couverture de How You Got Rich" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/jim-rohn-originals-no-ai/course.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-successful/cover-page-1.png" width="180" alt="Couverture de How You Got Successful" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/how-you-got-happiness-publication/how-you-got-happiness.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-happiness/cover-page-1.png" width="180" alt="Couverture de How You Got Happiness" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/wealth-from-first-principles/wealth-from-first-principles.pdf"><strong>Wealth from First Principles</strong></a><br />
      argent, propriété, créances et capitalisation
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/dynamic_book/how-you-got-rich.pdf"><strong>How You Got Rich?</strong></a><br />
      un livre non linéaire sur la richesse construit à partir de preuves d’entretiens
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/jim-rohn-originals-no-ai/course.pdf"><strong>How You Got Successful?</strong></a><br />
      des conférences de Jim Rohn sur la réussite réordonnées en un arc de livre plus fluide
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/how-you-got-happiness-publication/how-you-got-happiness.pdf"><strong>How You Got Happiness?</strong></a><br />
      des conférences de Krishnamurti mises en forme en livre sur l’attention, la peur, la méditation et la liberté
    </td>
  </tr>
</table>

`LazyLearn` publie aussi un livre d’écriture multilingue ainsi qu’un livre de cours terminé sur la justice :

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write/cover-page-1.png" width="180" alt="Couverture anglaise de How to Speak and Write" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-zh.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write-zh/cover-page-1.png" width="180" alt="Couverture chinoise traditionnelle de How to Speak and Write" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-jp.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write-jp/cover-page-1.png" width="180" alt="Couverture japonaise de How to Speak and Write" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/justice-with-michael-sandel/cover-page-1.png" width="180" alt="Couverture de Justice with Michael Sandel" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write.pdf"><strong>How to Speak and Write</strong></a><br />
      édition anglaise réordonnée
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
      livre de cours de philosophie politique de Michael Sandel
    </td>
  </tr>
</table>

`leonardsusskind` publie aussi les livres de physique fondamentaux du Theoretical Minimum :

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/quantum_mechanics_theoretical_minimum.png" width="180" alt="Couverture de Quantum Mechanics Theoretical Minimum" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/general_relativity_theoretical_minimum.png" width="180" alt="Couverture de General Relativity Theoretical Minimum" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/statistical_mechanics_theoretical_minimum_first_page.png" width="180" alt="Couverture de Statistical Mechanics Theoretical Minimum" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/cosmology_theoretical_minimum_first_page.png" width="180" alt="Couverture de Cosmology Theoretical Minimum" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf"><strong>Quantum Mechanics</strong></a><br />
      livre fondamental du Theoretical Minimum
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf"><strong>General Relativity</strong></a><br />
      livre fondamental du Theoretical Minimum
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf"><strong>Statistical Mechanics</strong></a><br />
      livre fondamental du Theoretical Minimum
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf"><strong>Cosmology</strong></a><br />
      livre fondamental du Theoretical Minimum
    </td>
  </tr>
</table>

## ✨ Ce qu’il couvre

- Télécharger une playlist dans une archive média externe stable.
- Transcrire des vidéos en sous-titres `.srt` et en Markdown horodaté.
- Convertir des ensembles de transcriptions terminés en notes TeX structurées et en PDF de cours fusionnés.
- Convertir des dossiers de matériel Markdown ordonné en livres TeX/PDF au format poche.
- Exécuter de longues tâches dans `tmux` avec des scripts de file d’attente et des scripts de surveillance/protection.
- Exporter des PDF compagnons compacts au format poche à partir de LaTeX de cours terminé.
- Réutiliser le même flux de travail d’en-tête enveloppé et de rafraîchissement des figures pour les PDF normaux
  en taille pleine et les PDF poche dans plusieurs dépôts hôtes.

## 🧪 Dépôts hôtes fonctionnels

`Video2Book` est déjà utilisé dans plusieurs dépôts hôtes avec différentes structures d’archives.

| Dépôt hôte | Focus | Exemple de wrapper | Sorties actuellement suivies |
| --- | --- | --- | --- |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Cours Yale `Financial Markets` avec Robert J. Shiller | [examples/lazyearn/yale-financial-markets/](../examples/lazyearn/yale-financial-markets/) | [PDF du cours](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf), [PDF des conférences](https://github.com/lachlanchen/LazyEarn/tree/main/generated_course_notes/lazyearn/yale-financial-markets/chapters), [transcriptions markdown](https://github.com/lachlanchen/LazyEarn/tree/main/markdown/lazyearn/yale-financial-markets), [sous-titres](https://github.com/lachlanchen/LazyEarn/tree/main/subtitles/lazyearn/yale-financial-markets) |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | Adaptation de cours d’écriture pour `How You Speak and Write` | [examples/lazylearn/how-you-speak-and-write/](../examples/lazylearn/how-you-speak-and-write/), [examples/lazylearn/justice-with-michael-sandel/](../examples/lazylearn/justice-with-michael-sandel/) | [PDF du cours How You Speak and Write](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf), [PDF du cours Justice with Michael Sandel](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/justice-with-michael-sandel/course.pdf), [PDF des cours locaux sur l’expression](https://github.com/lachlanchen/LazyLearn/tree/main/how-to-speak-and-write), [PDF local sur la justice](https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf), [PDF des conférences](https://github.com/lachlanchen/LazyLearn/tree/main/generated_course_notes/lazylearn/how-you-speak-and-write/chapters), [transcriptions markdown](https://github.com/lachlanchen/LazyLearn/tree/main/markdown/lazylearn), [sous-titres](https://github.com/lachlanchen/LazyLearn/tree/main/subtitles/lazylearn) |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Archive complète des conférences de Leonard Susskind, pipeline de transcription et livres de notes publiés | [examples/leonardsusskind/susskind-physics-archive/](../examples/leonardsusskind/susskind-physics-archive/) | [dossier des livres publiés](https://github.com/lachlanchen/leonardsusskind/tree/main), [PDF de mécanique quantique avancée](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf), [PDF de sujets en théorie des cordes](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf), [PDF de physique des particules 3](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_particle_physics_3/particle_physics_3_supersymmetry_and_grand_unification.pdf), [transcriptions markdown](https://github.com/lachlanchen/leonardsusskind/tree/main/markdown), [sous-titres](https://github.com/lachlanchen/leonardsusskind/tree/main/subtitles) |

## 📘 Livres et PDF

La troisième étape produit déjà de véritables sorties de type livre dans les dépôts hôtes :

- livres de cours fusionnés tels que `course.pdf` ou un nom canonique publié par l’hôte
- PDF par conférence sous `generated_course_notes/.../chapters/`
- arbres de transcriptions dans `markdown/` et arbres de sous-titres dans `subtitles/`

Autres livres publiés et sorties de cours :

| Dépôt hôte | Titre | PDF principal | Notes |
| --- | --- | --- | --- |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Yale Financial Markets | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf) | livre de conférences de Robert J. Shiller avec variantes pleine taille et poche |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Hard Knocks Interviews | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/course.pdf) | compilation directe conférence par conférence |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | High-Growth Dossier | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/high-growth-stocks/high-growth-stocks.pdf) | ancien livre de recherche avec exports poche |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Quod Tango Muto | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/quod-tango-muto/quod-tango-muto.pdf) | livre de recherche à devise latine avec exports poche |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | How You Speak and Write | [PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf) | adaptation de cours d’écriture |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | Justice with Michael Sandel | [PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/justice-with-michael-sandel/course.pdf) | livre de cours de philosophie politique |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Classical Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/classical_mechanics_theoretical_minimum.pdf) | livre consolidé dans `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Quantum Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/quantum_mechanics_theoretical_minimum.pdf) | livre TTM fondamental dans `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Special Relativity (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/special_relativity_theoretical_minimum.pdf) | livre TTM fondamental dans `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | General Relativity (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/general_relativity_theoretical_minimum.pdf) | livre TTM fondamental dans `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Statistical Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/statistical_mechanics_theoretical_minimum.pdf) | livre TTM fondamental dans `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Cosmology (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/cosmology_theoretical_minimum.pdf) | livre TTM fondamental dans `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Advanced Quantum Mechanics | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf) | titre de physique complémentaire |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Topics in String Theory | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf) | titre complémentaire de cosmologie / cordes |

D’autres titres consolidés de Susskind sont disponibles dans [all_notes](https://github.com/lachlanchen/leonardsusskind/tree/main/all_notes).

### Pointeurs vers les dépôts frères locaux

Si vous exécutez ces dépôts depuis un répertoire parent partagé (par exemple `/home/lachlan/ProjectsLFS`), les mêmes livres sont aussi accessibles via des chemins locaux :

- `../LazyLearn/justice-with-michael-sandel/justice-with-michael-sandel.pdf`
- `../LazyLearn/how-to-speak-and-write/how-to-speak-and-write.pdf`
- `../LazyEarn/generated_course_notes/lazyearn/yale-financial-markets/course.pdf`
- `../leonardsusskind/<sibling-folder>/...` (PDF de cours et de livres publiés dans ce dépôt)

## 🧩 Pipeline

| Étape | Module | Objectif |
| --- | --- | --- |
| 1 | `playlist2videos/` | Télécharger ou rafraîchir une playlist avec `yt-dlp`, conserver les journaux et ignorer les éléments déjà archivés. |
| 2 | `videos2subtitles/` | Transcrire les médias archivés dans `subtitles/` et `markdown/`. |
| 3 | `subtitles2notes/` | Transformer les transcriptions terminées en TeX de chapitres, PDF de conférences et PDF de cours fusionnés. |
| 4 | `scripts/process_markdown_material_book.py` | Transformer des dossiers Markdown sources ordonnés en livres TeX/PDF générés au format poche tout en transmettant les images associées à Codex. |
| 5 | `scripts/start_markdown_material_book_tmux.sh` | Exécuter le rédacteur de livres à partir de matériel Markdown dans `tmux`, avec un traitement source par source compatible avec la reprise. |
| 6 | `scripts/export_course_pocket_pdfs.sh` | Reconstruire les sorties `course.tex` terminées en variantes poche/A5 pour des packages de publication et émettre des rapports overfull mappés. |
| 7 | `scripts/export_tex_book_pocket_pdf.sh` | Reconstruire un livre/article TeX autonome en PDF compagnon au format poche et le synchroniser dans l’arborescence docs du dépôt hôte. |
| 8 | `subtitles2notes/templates/lecture_notes_common_preamble.tex` | Source partagée d’en-tête/mise en page pour les PDF de cours en taille normale utilisée par les livres générés. |
| 9 | `scripts/fix_course_pocket_overfulls.sh` | Itérer sur une variante de cours : exporter, rapporter, patcher avec Codex, puis réexporter jusqu’à réduction des overfulls exploitables. |
| 10 | `scripts/fix_latex_project_overfulls.sh` | Correcteur générique de débordements LaTeX pour tout dépôt/projet pouvant être construit avec `pdflatex` ou une commande de compilation personnalisée. |
| 11 | `scripts/recheck_course_figures.py` | Réauditer les figures de cours de type capture d’écran par rapport au contexte de transcription et aux images vidéo de remplacement. |
| 12 | `scripts/export_course_epubs.sh` | Reconstruire directement les sorties `course.tex` terminées en EPUB3. |

## 🚀 Démarrage rapide

Clonez-le directement :

```bash
git clone git@github.com:lachlanchen/Video2Book.git
cd Video2Book
```

Ou ajoutez-le à un autre dépôt comme sous-module :

```bash
git submodule add git@github.com:lachlanchen/Video2Book.git Video2Book
git submodule update --init --recursive
```

## 🏗️ Structure du dépôt hôte

`Video2Book` s’attend à s’exécuter depuis un dépôt hôte qui stocke les sorties de travail :

- `subtitles/`
- `markdown/`
- `generated_course_notes/`
- `.lecture-notes-work/`

Les fichiers vidéo eux-mêmes sont généralement conservés hors du dépôt hôte dans un espace de travail média tel que :

- `/home/lachlan/ProjectsLFS/YoutubeDownloader`

## 🛠️ Utilisation typique

Depuis la racine du dépôt hôte :

```bash
./Video2Book/scripts/download_susskind_playlist.sh
./Video2Book/scripts/start_transcription_tmux.sh
./Video2Book/scripts/start_transcription_monitor_tmux.sh
./Video2Book/scripts/start_course_notes_tmux.sh
./Video2Book/scripts/start_course_notes_monitor_tmux.sh
```

Simulation du téléchargeur :

```bash
./Video2Book/scripts/download_susskind_playlist.sh --dry-run
```

Démarrer une file d’écriture de notes pour un cours :

```bash
./Video2Book/scripts/start_course_notes_tmux.sh --course supplementary/advanced_quantum_mechanics/2013_fall
```

Exporter des PDF compacts pour tous les cours terminés (par exemple dans `leonardsusskind`) :

```bash
./Video2Book/scripts/export_course_pocket_pdfs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
```

Exporter un livre autonome dans `investment_pdfs/` en variantes au format poche :

```bash
./Video2Book/scripts/export_tex_book_pocket_pdf.sh \
  --repo-root /home/lachlan/ProjectsLFS/LazyEarn \
  --project-root /home/lachlan/ProjectsLFS/LazyEarn/investment_pdfs/wealth-from-first-principles \
  --main-tex wealth-from-first-principles.tex \
  --font-mode onepointtwo \
  --suffix pocket_1_2x
```

Exécuter le correcteur de débordements piloté par Codex pour une variante de cours à mise en page étroite :

```bash
./Video2Book/scripts/start_pocket_overflow_fix_tmux.sh \
  --course core/statistical_mechanics/2013_spring_theoretical_minimum \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

Exécuter la file dans tmux sur tous les cours Susskind terminés, un cours à la fois :

```bash
./Video2Book/scripts/start_pocket_overflow_fix_tmux.sh \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

Exécuter le correcteur LaTeX générique sur n’importe quel projet :

```bash
./Video2Book/scripts/fix_latex_project_overfulls.sh \
  --repo-root /path/to/repo \
  --project-root /path/to/repo/book \
  --main-tex main.tex \
  --model gpt-5.4 \
  --reasoning medium
```

Exporter EPUB3 directement depuis TeX pour tous les cours terminés :

```bash
./Video2Book/scripts/export_course_epubs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
```

Des wrappers propres à l’hôte peuvent vivre sous `examples/`. Modèles actuellement inclus :

- `examples/lazyearn/yale-financial-markets/`
- `examples/lazylearn/how-you-speak-and-write/`
- `examples/leonardsusskind/susskind-physics-archive/`

## 🎬 Exemple par défaut actuel

Le téléchargeur inclus utilise par défaut la playlist de physique de Leonard Susskind :

- <https://www.youtube.com/playlist?list=PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG>

Ce choix par défaut n’est qu’un exemple fonctionnel. Le code est structuré pour que d’autres dépôts hôtes puissent adapter le même pipeline à différentes archives de conférences.

## 📦 Carte des modules

- [playlist2videos](../playlist2videos)
- [videos2subtitles](../videos2subtitles)
- [subtitles2notes](../subtitles2notes)
- [scripts](../scripts)
- [Relais d’export poche](../references/pocket-size-course-pdfs-handoff.md)
- [Relais de mise en page A4 et poche](../references/a4-and-pocket-pdf-layout-handoff.md)
- [Relais d’aperçu de livre README](../references/readme-book-preview-handoff.md)
- [Relais du correcteur de débordements LaTeX](../references/latex-overflow-fixer-handoff.md)
- [Relais d’export EPUB](../references/tex-to-epub-handoff.md)

## 📚 Notes d’adaptation aux hôtes

- [references/lazylearn-course-adaptation.md](../references/lazylearn-course-adaptation.md)
- [references/lazyearn-yale-financial-markets-adaptation.md](../references/lazyearn-yale-financial-markets-adaptation.md)
- [references/nanobanana-2-book-cover-handoff.md](../references/nanobanana-2-book-cover-handoff.md)
- [references/readme-book-preview-handoff.md](../references/readme-book-preview-handoff.md)
- [references/a4-and-pocket-pdf-layout-handoff.md](../references/a4-and-pocket-pdf-layout-handoff.md)
- [references/latex-overflow-fixer-handoff.md](../references/latex-overflow-fixer-handoff.md)
- [references/tex-book-translation-workflow.md](../references/tex-book-translation-workflow.md)
- [references/tex-to-epub-handoff.md](../references/tex-to-epub-handoff.md)

## 🎨 Utilitaire de couverture de livre

`Video2Book` inclut aussi un assistant local Nano Banana 2 pour la génération éditoriale de couvertures de livres :

- script : [scripts/book_cover_nanobanana.py](../scripts/book_cover_nanobanana.py)
- guide : [references/nanobanana-2-book-cover-handoff.md](../references/nanobanana-2-book-cover-handoff.md)
- modèle d’environnement : [.env.example](../.env.example)
- exemple de prompt de livre actuel : [examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt](../examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt)

Il réutilise la mécanique d’envoi et d’interrogation de GRS AI issue du travail frère Nano Banana, mais remplace les prompts de segmentation par un prompt de couverture de livre et enregistre une trace de sortie propre à chaque exécution.

## 🌐 Utilitaire de traduction de livre

`Video2Book` peut aussi traduire un livre de notes de cours terminé dans des dossiers
linguistiques frères tels que `zh/` et `jp/`, tout en conservant intactes la structure TeX,
les équations et les images.

- gestionnaire : [scripts/translate_tex_book.py](../scripts/translate_tex_book.py)
- exécuteur de boucle : [scripts/process_book_translation_one_by_one.sh](../scripts/process_book_translation_one_by_one.sh)
- démarreur tmux : [scripts/start_book_translation_tmux.sh](../scripts/start_book_translation_tmux.sh)
- note de flux de travail : [references/tex-book-translation-workflow.md](../references/tex-book-translation-workflow.md)

La boucle de traduction :

- initialise une édition traduite prête pour XeLaTeX
- traduit d’abord le fichier principal du livre, puis chaque chapitre
- prend en charge à la fois les livres à chapitres séparés et les livres `main.tex` à fichier unique avec blocs `\chapter{...}` intégrés
- nomme les fichiers d’entrée traduits avec un suffixe de langue tel que `book_zh.tex` ou `book_jp.tex`
- recompile après chaque unité
- peut committer et pousser le dossier traduit après chaque unité terminée

## ⚙️ Prérequis

- `tmux`
- `ffmpeg`
- `pdflatex`
- `pdfunite`
- `pdftotext`
- `yt-dlp`
- `pandoc` (pour `scripts/export_course_epubs.sh`)
- CLI `codex` pour le pipeline de notes
- un environnement conda `whisper` fonctionnel pour la transcription
- `whisper_with_lang_detect` si vous voulez le chemin principal de sous-titres au lieu du chemin Whisper de secours uniquement
- `rsync` (pour la synchronisation locale optionnelle de publication des PDF poche)

## 🤝 Bon cas d’usage

`Video2Book` convient bien lorsque vous voulez :

- un pipeline local au dépôt plutôt qu’une application monolithique
- une génération de notes de cours centrée sur les transcriptions
- une automatisation longue durée basée sur tmux
- une structure d’archive reproductible pour du matériel d’étude

## 🙏 Soutien

| Don | PayPal | Stripe |
| --- | --- | --- |
| [![Don](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Licence

Ce dépôt est sous licence GNU General Public License v3.0.