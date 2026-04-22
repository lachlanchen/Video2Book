[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![Banner de LazyingArt](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://lazying.art)

# Video2Book de LazyingArt LLC

> **Video2Book de LazyingArt LLC**. Sitios web: [lazying.art](https://lazying.art) y [learn.lazying.art](https://learn.lazying.art).

[![LazyingArt](https://img.shields.io/badge/Website-lazying.art-111827?style=for-the-badge&logo=googlechrome&logoColor=white)](https://lazying.art)
[![Learn](https://img.shields.io/badge/Learn-learn.lazying.art-1f2937?style=for-the-badge&logo=bookstack&logoColor=white)](https://learn.lazying.art)

[![Toolkit](https://img.shields.io/badge/toolkit-video__to__book-111827?style=for-the-badge&logo=bookstack&logoColor=white)](#)
[![Downloader](https://img.shields.io/badge/stage_1-playlist2videos-1d4ed8?style=for-the-badge&logo=youtube&logoColor=white)](#-canalizaci%C3%B3n)
[![Transcription](https://img.shields.io/badge/stage_2-videos2subtitles-0f766e?style=for-the-badge&logo=openai&logoColor=white)](#-canalizaci%C3%B3n)
[![Notes](https://img.shields.io/badge/stage_3-subtitles2notes-f97316?style=for-the-badge&logo=latex&logoColor=white)](#-canalizaci%C3%B3n)
[![tmux](https://img.shields.io/badge/runtime-tmux-7c3aed?style=for-the-badge&logo=gnu-bash&logoColor=white)](#-inicio-r%C3%A1pido)

`Video2Book` es una canalización práctica para convertir colecciones de videos de formato largo en material de estudio duradero: medios descargados, transcripciones con marcas de tiempo y apuntes de clase derivados de transcripciones con PDF compilados.

## 📚 Libros insignia

Estas vistas previas usan la primera página extraída de cada PDF publicado de `LazyEarn`
y `LazyLearn`.

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/wealth-from-first-principles/wealth-from-first-principles.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/wealth-from-first-principles/cover-page-1.png" width="180" alt="Portada de Riqueza desde los primeros principios" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/dynamic_book/how-you-got-rich.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-rich/cover-page-1.png" width="180" alt="Portada de Cómo te hiciste rico" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/jim-rohn-originals-no-ai/course.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-successful/cover-page-1.png" width="180" alt="Portada de Cómo tuviste éxito" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/how-you-got-happiness-publication/how-you-got-happiness.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-happiness/cover-page-1.png" width="180" alt="Portada de Cómo obtuviste felicidad" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/wealth-from-first-principles/wealth-from-first-principles.pdf"><strong>Wealth from First Principles</strong></a><br />
      dinero, propiedad, derechos y capitalización compuesta
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/dynamic_book/how-you-got-rich.pdf"><strong>How You Got Rich?</strong></a><br />
      un libro no lineal sobre riqueza construido a partir de evidencia de entrevistas
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/jim-rohn-originals-no-ai/course.pdf"><strong>How You Got Successful?</strong></a><br />
      conferencias de éxito de Jim Rohn reordenadas en un arco de libro más fluido
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/how-you-got-happiness-publication/how-you-got-happiness.pdf"><strong>How You Got Happiness?</strong></a><br />
      charlas de Krishnamurti moldeadas en un libro sobre atención, miedo, meditación y libertad
    </td>
  </tr>
</table>

`LazyLearn` también publica un libro multilingüe de escritura, además de un libro terminado de curso sobre justicia:

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write/cover-page-1.png" width="180" alt="Portada de Cómo hablar y escribir en inglés" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-zh.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write-zh/cover-page-1.png" width="180" alt="Portada de Cómo hablar y escribir en chino tradicional" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-jp.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write-jp/cover-page-1.png" width="180" alt="Portada de Cómo hablar y escribir en japonés" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/justice-with-michael-sandel/cover-page-1.png" width="180" alt="Portada de Justicia con Michael Sandel" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write.pdf"><strong>How to Speak and Write</strong></a><br />
      edición en inglés reordenada
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-zh.pdf"><strong>如何說話與寫作</strong></a><br />
      versión en chino tradicional
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-jp.pdf"><strong>話し方と書き方</strong></a><br />
      versión en japonés
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf"><strong>Justice with Michael Sandel</strong></a><br />
      libro del curso de filosofía política de Michael Sandel
    </td>
  </tr>
</table>

`leonardsusskind` también publica libros básicos de física de Theoretical Minimum:

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/quantum_mechanics_theoretical_minimum.png" width="180" alt="Portada de Mecánica cuántica Theoretical Minimum" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/general_relativity_theoretical_minimum.png" width="180" alt="Portada de Relatividad general Theoretical Minimum" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/statistical_mechanics_theoretical_minimum_first_page.png" width="180" alt="Portada de Mecánica estadística Theoretical Minimum" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/cosmology_theoretical_minimum_first_page.png" width="180" alt="Portada de Cosmología Theoretical Minimum" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf"><strong>Quantum Mechanics</strong></a><br />
      libro básico de Theoretical Minimum
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf"><strong>General Relativity</strong></a><br />
      libro básico de Theoretical Minimum
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf"><strong>Statistical Mechanics</strong></a><br />
      libro básico de Theoretical Minimum
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf"><strong>Cosmology</strong></a><br />
      libro básico de Theoretical Minimum
    </td>
  </tr>
</table>

## ✨ Qué cubre

- Descargar una lista de reproducción en un archivo multimedia externo estable.
- Transcribir videos a subtítulos `.srt` y Markdown con marcas de tiempo.
- Convertir conjuntos de transcripciones completados en apuntes TeX estructurados y PDF de curso combinados.
- Convertir carpetas ordenadas de material Markdown en libros TeX/PDF de tamaño de bolsillo.
- Ejecutar trabajos largos en `tmux` con scripts de cola y scripts de supervisión/protección.
- Exportar PDF complementarios compactos en formato de bolsillo desde LaTeX de cursos terminados.
- Reutilizar el mismo flujo de trabajo de encabezados envueltos y actualización de figuras tanto para PDF normales
  de tamaño completo como para PDF de bolsillo en repositorios anfitriones.

## 🧪 Repositorios anfitriones en funcionamiento

`Video2Book` ya se está usando en varios repositorios anfitriones con distintas formas de archivo.

| Repositorio anfitrión | Enfoque | Ejemplo de envoltorio | Salidas rastreadas actuales |
| --- | --- | --- | --- |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Curso `Financial Markets` de Yale con Robert J. Shiller | [examples/lazyearn/yale-financial-markets/](../examples/lazyearn/yale-financial-markets/) | [PDF del curso](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf), [PDF de clases](https://github.com/lachlanchen/LazyEarn/tree/main/generated_course_notes/lazyearn/yale-financial-markets/chapters), [transcripciones Markdown](https://github.com/lachlanchen/LazyEarn/tree/main/markdown/lazyearn/yale-financial-markets), [subtítulos](https://github.com/lachlanchen/LazyEarn/tree/main/subtitles/lazyearn/yale-financial-markets) |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | Adaptación de curso de escritura para `How You Speak and Write` | [examples/lazylearn/how-you-speak-and-write/](../examples/lazylearn/how-you-speak-and-write/), [examples/lazylearn/justice-with-michael-sandel/](../examples/lazylearn/justice-with-michael-sandel/) | [PDF del curso How You Speak and Write](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf), [PDF del curso Justice with Michael Sandel](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/justice-with-michael-sandel/course.pdf), [PDF locales del curso de oratoria](https://github.com/lachlanchen/LazyLearn/tree/main/how-to-speak-and-write), [PDF local de justicia](https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf), [PDF de clases](https://github.com/lachlanchen/LazyLearn/tree/main/generated_course_notes/lazylearn/how-you-speak-and-write/chapters), [transcripciones Markdown](https://github.com/lachlanchen/LazyLearn/tree/main/markdown/lazylearn), [subtítulos](https://github.com/lachlanchen/LazyLearn/tree/main/subtitles/lazylearn) |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Archivo completo de conferencias de Leonard Susskind, canalización de transcripción y libros de apuntes publicados | [examples/leonardsusskind/susskind-physics-archive/](../examples/leonardsusskind/susskind-physics-archive/) | [carpeta de libros publicados](https://github.com/lachlanchen/leonardsusskind/tree/main), [PDF de cuántica avanzada](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf), [PDF de temas de teoría de cuerdas](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf), [PDF de física de partículas 3](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_particle_physics_3/particle_physics_3_supersymmetry_and_grand_unification.pdf), [transcripciones Markdown](https://github.com/lachlanchen/leonardsusskind/tree/main/markdown), [subtítulos](https://github.com/lachlanchen/leonardsusskind/tree/main/subtitles) |

## 📘 Libros y PDF

La tercera etapa ya está produciendo salidas reales con forma de libro en repositorios anfitriones:

- libros de curso combinados como `course.pdf` o un nombre canónico publicado por el anfitrión
- PDF por clase bajo `generated_course_notes/.../chapters/`
- árboles de transcripciones en `markdown/` y árboles de subtítulos en `subtitles/`

Otros libros publicados y salidas de cursos:

| Repositorio anfitrión | Título | PDF principal | Notas |
| --- | --- | --- | --- |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Yale Financial Markets | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf) | libro de conferencias de Robert J. Shiller con variantes de tamaño completo y de bolsillo |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Hard Knocks Interviews | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/course.pdf) | compilación directa clase por clase |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | High-Growth Dossier | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/high-growth-stocks/high-growth-stocks.pdf) | libro de investigación heredado con exportaciones de bolsillo |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Quod Tango Muto | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/quod-tango-muto/quod-tango-muto.pdf) | libro de investigación con lema latino y exportaciones de bolsillo |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | How You Speak and Write | [PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf) | adaptación de curso de escritura |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | Justice with Michael Sandel | [PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/justice-with-michael-sandel/course.pdf) | libro de curso de filosofía política |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Classical Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/classical_mechanics_theoretical_minimum.pdf) | libro consolidado en `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Quantum Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/quantum_mechanics_theoretical_minimum.pdf) | libro básico TTM en `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Special Relativity (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/special_relativity_theoretical_minimum.pdf) | libro básico TTM en `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | General Relativity (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/general_relativity_theoretical_minimum.pdf) | libro básico TTM en `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Statistical Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/statistical_mechanics_theoretical_minimum.pdf) | libro básico TTM en `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Cosmology (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/cosmology_theoretical_minimum.pdf) | libro básico TTM en `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Advanced Quantum Mechanics | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf) | título complementario de física |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Topics in String Theory | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf) | título complementario de cosmología / cuerdas |

Otros títulos consolidados de Susskind están disponibles en [all_notes](https://github.com/lachlanchen/leonardsusskind/tree/main/all_notes).

### Punteros a repositorios hermanos locales

Si estás ejecutando estos repositorios desde un directorio padre compartido (por ejemplo `/home/lachlan/ProjectsLFS`), también se puede acceder a los mismos libros mediante rutas locales:

- `../LazyLearn/justice-with-michael-sandel/justice-with-michael-sandel.pdf`
- `../LazyLearn/how-to-speak-and-write/how-to-speak-and-write.pdf`
- `../LazyEarn/generated_course_notes/lazyearn/yale-financial-markets/course.pdf`
- `../leonardsusskind/<sibling-folder>/...` (PDF de cursos y libros publicados en ese repositorio)

## 🧩 Canalización

| Etapa | Módulo | Propósito |
| --- | --- | --- |
| 1 | `playlist2videos/` | Descargar o actualizar una lista de reproducción con `yt-dlp`, conservar registros y omitir elementos ya archivados. |
| 2 | `videos2subtitles/` | Transcribir los medios archivados en `subtitles/` y `markdown/`. |
| 3 | `subtitles2notes/` | Convertir transcripciones completadas en TeX de capítulos, PDF de clases y PDF de cursos combinados. |
| 4 | `scripts/process_markdown_material_book.py` | Convertir carpetas Markdown fuente ordenadas en libros TeX/PDF generados de tamaño de bolsillo mientras se pasan imágenes relacionadas a Codex. |
| 5 | `scripts/start_markdown_material_book_tmux.sh` | Ejecutar el escritor de libros de material Markdown en `tmux`, con procesamiento de una fuente a la vez seguro para reanudar. |
| 6 | `scripts/export_course_pocket_pdfs.sh` | Reconstruir salidas `course.tex` terminadas en variantes de bolsillo/A5 para paquetes de publicación y emitir informes overfull mapeados. |
| 7 | `scripts/export_tex_book_pocket_pdf.sh` | Reconstruir un libro/artículo TeX independiente en un PDF complementario de tamaño de bolsillo y sincronizarlo en el árbol de documentación del repositorio anfitrión. |
| 8 | `subtitles2notes/templates/lecture_notes_common_preamble.tex` | Fuente compartida de encabezado/diseño de PDF de curso de tamaño normal usada por libros generados. |
| 9 | `scripts/fix_course_pocket_overfulls.sh` | Iterar sobre una variante de curso: exportar, informar, parchear con Codex y volver a exportar hasta que bajen los overfull accionables. |
| 10 | `scripts/fix_latex_project_overfulls.sh` | Corrector genérico de desbordamientos LaTeX para cualquier repositorio/proyecto que pueda compilar con `pdflatex` o un comando de compilación personalizado. |
| 11 | `scripts/recheck_course_figures.py` | Reauditar figuras de clase tipo captura de pantalla contra el contexto de la transcripción y fotogramas de video de reemplazo. |
| 12 | `scripts/export_course_epubs.sh` | Reconstruir salidas `course.tex` terminadas directamente en EPUB3. |

## 🚀 Inicio rápido

Clónalo directamente:

```bash
git clone git@github.com:lachlanchen/Video2Book.git
cd Video2Book
```

O añádelo a otro repositorio como submódulo:

```bash
git submodule add git@github.com:lachlanchen/Video2Book.git Video2Book
git submodule update --init --recursive
```

## 🏗️ Estructura del repositorio anfitrión

`Video2Book` espera ejecutarse desde un repositorio anfitrión que almacena las salidas de trabajo:

- `subtitles/`
- `markdown/`
- `generated_course_notes/`
- `.lecture-notes-work/`

Los archivos de video en sí suelen mantenerse fuera del repositorio anfitrión, en un espacio de trabajo de medios como:

- `/home/lachlan/ProjectsLFS/YoutubeDownloader`

## 🛠️ Uso típico

Desde la raíz del repositorio anfitrión:

```bash
./Video2Book/scripts/download_susskind_playlist.sh
./Video2Book/scripts/start_transcription_tmux.sh
./Video2Book/scripts/start_transcription_monitor_tmux.sh
./Video2Book/scripts/start_course_notes_tmux.sh
./Video2Book/scripts/start_course_notes_monitor_tmux.sh
```

Ejecutar el descargador en modo de prueba:

```bash
./Video2Book/scripts/download_susskind_playlist.sh --dry-run
```

Iniciar una cola de escritura de apuntes para un curso:

```bash
./Video2Book/scripts/start_course_notes_tmux.sh --course supplementary/advanced_quantum_mechanics/2013_fall
```

Exportar PDF compactos para todos los cursos completados (por ejemplo en `leonardsusskind`):

```bash
./Video2Book/scripts/export_course_pocket_pdfs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
```

Exportar un libro independiente en `investment_pdfs/` a variantes de tamaño de bolsillo:

```bash
./Video2Book/scripts/export_tex_book_pocket_pdf.sh \
  --repo-root /home/lachlan/ProjectsLFS/LazyEarn \
  --project-root /home/lachlan/ProjectsLFS/LazyEarn/investment_pdfs/wealth-from-first-principles \
  --main-tex wealth-from-first-principles.tex \
  --font-mode onepointtwo \
  --suffix pocket_1_2x
```

Ejecutar el corrector de desbordamientos impulsado por Codex para una variante de curso de diseño estrecho:

```bash
./Video2Book/scripts/start_pocket_overflow_fix_tmux.sh \
  --course core/statistical_mechanics/2013_spring_theoretical_minimum \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

Ejecutar la cola en tmux sobre todos los cursos Susskind completados, un curso a la vez:

```bash
./Video2Book/scripts/start_pocket_overflow_fix_tmux.sh \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

Ejecutar el corrector genérico de LaTeX en cualquier proyecto:

```bash
./Video2Book/scripts/fix_latex_project_overfulls.sh \
  --repo-root /path/to/repo \
  --project-root /path/to/repo/book \
  --main-tex main.tex \
  --model gpt-5.4 \
  --reasoning medium
```

Exportar EPUB3 directamente desde TeX para todos los cursos completados:

```bash
./Video2Book/scripts/export_course_epubs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
```

Los envoltorios específicos del anfitrión pueden vivir bajo `examples/`. Patrones incluidos actualmente:

- `examples/lazyearn/yale-financial-markets/`
- `examples/lazylearn/how-you-speak-and-write/`
- `examples/leonardsusskind/susskind-physics-archive/`

## 🎬 Ejemplo predeterminado actual

El descargador incluido usa por defecto la lista de reproducción de física de Leonard Susskind:

- <https://www.youtube.com/playlist?list=PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG>

Ese valor predeterminado es solo un ejemplo funcional. El código está estructurado para que otros repositorios anfitriones puedan adaptar la misma canalización a distintos archivos de clases.

## 📦 Mapa de módulos

- [playlist2videos](../playlist2videos)
- [videos2subtitles](../videos2subtitles)
- [subtitles2notes](../subtitles2notes)
- [scripts](../scripts)
- [Traspaso de exportación de bolsillo](../references/pocket-size-course-pdfs-handoff.md)
- [Traspaso de diseño A4 y de bolsillo](../references/a4-and-pocket-pdf-layout-handoff.md)
- [Traspaso de vista previa de libros en README](../references/readme-book-preview-handoff.md)
- [Traspaso del corrector de desbordamientos LaTeX](../references/latex-overflow-fixer-handoff.md)
- [Traspaso de exportación EPUB](../references/tex-to-epub-handoff.md)

## 📚 Notas de adaptación de anfitriones

- [references/lazylearn-course-adaptation.md](../references/lazylearn-course-adaptation.md)
- [references/lazyearn-yale-financial-markets-adaptation.md](../references/lazyearn-yale-financial-markets-adaptation.md)
- [references/nanobanana-2-book-cover-handoff.md](../references/nanobanana-2-book-cover-handoff.md)
- [references/readme-book-preview-handoff.md](../references/readme-book-preview-handoff.md)
- [references/a4-and-pocket-pdf-layout-handoff.md](../references/a4-and-pocket-pdf-layout-handoff.md)
- [references/latex-overflow-fixer-handoff.md](../references/latex-overflow-fixer-handoff.md)
- [references/tex-book-translation-workflow.md](../references/tex-book-translation-workflow.md)
- [references/tex-to-epub-handoff.md](../references/tex-to-epub-handoff.md)

## 🎨 Utilidad de portadas de libros

`Video2Book` también incluye un asistente local de Nano Banana 2 para la generación editorial de portadas de libros:

- script: [scripts/book_cover_nanobanana.py](../scripts/book_cover_nanobanana.py)
- guía: [references/nanobanana-2-book-cover-handoff.md](../references/nanobanana-2-book-cover-handoff.md)
- plantilla de entorno: [.env.example](../.env.example)
- prompt de ejemplo de libro actual: [examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt](../examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt)

Reutiliza la mecánica de envío y sondeo de GRS AI del trabajo hermano de Nano Banana, pero cambia los prompts de segmentación por un prompt de portada de libro y guarda una traza de salida limpia por ejecución.

## 🌐 Utilidad de traducción de libros

`Video2Book` también puede traducir un libro terminado de apuntes de clase a carpetas hermanas
de idioma como `zh/` y `jp/`, manteniendo intactas la estructura TeX,
las ecuaciones y las imágenes.

- gestor: [scripts/translate_tex_book.py](../scripts/translate_tex_book.py)
- ejecutor de bucle: [scripts/process_book_translation_one_by_one.sh](../scripts/process_book_translation_one_by_one.sh)
- iniciador tmux: [scripts/start_book_translation_tmux.sh](../scripts/start_book_translation_tmux.sh)
- nota de flujo de trabajo: [references/tex-book-translation-workflow.md](../references/tex-book-translation-workflow.md)

El bucle de traducción:

- inicializa una edición traducida lista para XeLaTeX
- traduce primero el archivo principal del libro y luego cada capítulo
- admite tanto libros con capítulos divididos como libros `main.tex` de un solo archivo con bloques `\chapter{...}` en línea
- nombra los archivos de entrada traducidos con un sufijo de idioma como `book_zh.tex` o `book_jp.tex`
- recompila después de cada unidad
- puede confirmar y enviar la carpeta traducida después de cada unidad completada

## ⚙️ Requisitos

- `tmux`
- `ffmpeg`
- `pdflatex`
- `pdfunite`
- `pdftotext`
- `yt-dlp`
- `pandoc` (para `scripts/export_course_epubs.sh`)
- CLI `codex` para la canalización de apuntes
- un entorno conda `whisper` funcional para transcripción
- `whisper_with_lang_detect` si quieres la ruta principal de subtítulos en lugar de Whisper solo como alternativa
- `rsync` (para sincronización opcional de publicación local de PDF de bolsillo)

## 🤝 Buen encaje

`Video2Book` encaja bien cuando quieres:

- una canalización local al repositorio en lugar de una aplicación monolítica
- generación de apuntes de clase centrada primero en transcripciones
- automatización de larga duración basada en tmux
- estructura de archivo reproducible para material de estudio

## 🙏 Apoyo

| Donar | PayPal | Stripe |
| --- | --- | --- |
| [![Donar](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Licencia

Este repositorio tiene licencia GNU General Public License v3.0.
