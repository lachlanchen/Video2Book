[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![Баннер LazyingArt](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://lazying.art)

# Video2Book от LazyingArt LLC

> **Video2Book от LazyingArt LLC**. Сайты: [lazying.art](https://lazying.art) и [learn.lazying.art](https://learn.lazying.art).

[![LazyingArt](https://img.shields.io/badge/Website-lazying.art-111827?style=for-the-badge&logo=googlechrome&logoColor=white)](https://lazying.art)
[![Learn](https://img.shields.io/badge/Learn-learn.lazying.art-1f2937?style=for-the-badge&logo=bookstack&logoColor=white)](https://learn.lazying.art)

[![Toolkit](https://img.shields.io/badge/toolkit-video__to__book-111827?style=for-the-badge&logo=bookstack&logoColor=white)](#)
[![Downloader](https://img.shields.io/badge/stage_1-playlist2videos-1d4ed8?style=for-the-badge&logo=youtube&logoColor=white)](#-pipeline)
[![Transcription](https://img.shields.io/badge/stage_2-videos2subtitles-0f766e?style=for-the-badge&logo=openai&logoColor=white)](#-pipeline)
[![Notes](https://img.shields.io/badge/stage_3-subtitles2notes-f97316?style=for-the-badge&logo=latex&logoColor=white)](#-pipeline)
[![tmux](https://img.shields.io/badge/runtime-tmux-7c3aed?style=for-the-badge&logo=gnu-bash&logoColor=white)](#-quick-start)

`Video2Book` — это практический конвейер для превращения больших коллекций видео в долговечные учебные материалы: загруженные медиа, расшифровки с временными метками и лекционные конспекты на основе расшифровок со скомпилированными PDF.

## 📚 Флагманские книги

В этих превью используется извлеченная первая страница каждого опубликованного PDF из `LazyEarn`
и `LazyLearn`.

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/wealth-from-first-principles/wealth-from-first-principles.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/wealth-from-first-principles/cover-page-1.png" width="180" alt="Обложка Wealth from First Principles" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/dynamic_book/how-you-got-rich.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-rich/cover-page-1.png" width="180" alt="Обложка How You Got Rich" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/jim-rohn-originals-no-ai/course.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-successful/cover-page-1.png" width="180" alt="Обложка How You Got Successful" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/how-you-got-happiness-publication/how-you-got-happiness.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-happiness/cover-page-1.png" width="180" alt="Обложка How You Got Happiness" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/wealth-from-first-principles/wealth-from-first-principles.pdf"><strong>Wealth from First Principles</strong></a><br />
      деньги, собственность, требования и сложный рост
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/dynamic_book/how-you-got-rich.pdf"><strong>How You Got Rich?</strong></a><br />
      нелинейная книга о богатстве, построенная на свидетельствах из интервью
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/jim-rohn-originals-no-ai/course.pdf"><strong>How You Got Successful?</strong></a><br />
      лекции Джима Рона об успехе, переупорядоченные в более плавную книжную дугу
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/how-you-got-happiness-publication/how-you-got-happiness.pdf"><strong>How You Got Happiness?</strong></a><br />
      беседы Кришнамурти, оформленные в книгу о внимании, страхе, медитации и свободе
    </td>
  </tr>
</table>

`LazyLearn` также публикует многоязычную книгу о письме и завершенную
книгу курса о справедливости:

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write/cover-page-1.png" width="180" alt="Обложка How to Speak and Write English" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-zh.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write-zh/cover-page-1.png" width="180" alt="Обложка How to Speak and Write Traditional Chinese" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-jp.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write-jp/cover-page-1.png" width="180" alt="Обложка How to Speak and Write Japanese" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/justice-with-michael-sandel/cover-page-1.png" width="180" alt="Обложка Justice with Michael Sandel" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write.pdf"><strong>How to Speak and Write</strong></a><br />
      переупорядоченное английское издание
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
      книга курса Майкла Сэндела по политической философии
    </td>
  </tr>
</table>

`leonardsusskind` также публикует базовые книги по физике Theoretical Minimum:

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/quantum_mechanics_theoretical_minimum.png" width="180" alt="Обложка Quantum Mechanics Theoretical Minimum" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/general_relativity_theoretical_minimum.png" width="180" alt="Обложка General Relativity Theoretical Minimum" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/statistical_mechanics_theoretical_minimum_first_page.png" width="180" alt="Обложка Statistical Mechanics Theoretical Minimum" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/cosmology_theoretical_minimum_first_page.png" width="180" alt="Обложка Cosmology Theoretical Minimum" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf"><strong>Quantum Mechanics</strong></a><br />
      базовая книга Theoretical Minimum
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf"><strong>General Relativity</strong></a><br />
      базовая книга Theoretical Minimum
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf"><strong>Statistical Mechanics</strong></a><br />
      базовая книга Theoretical Minimum
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf"><strong>Cosmology</strong></a><br />
      базовая книга Theoretical Minimum
    </td>
  </tr>
</table>

## ✨ Что охватывает

- Загрузка плейлиста в стабильный внешний медиаархив.
- Расшифровка видео в субтитры `.srt` и Markdown с временными метками.
- Преобразование завершенных наборов расшифровок в структурированные TeX-конспекты и объединенные PDF курсов.
- Преобразование упорядоченных папок с Markdown-материалами в TeX/PDF-книги карманного размера.
- Запуск долгих задач в `tmux` с очередями и скриптами мониторинга/защиты.
- Экспорт компактных сопроводительных PDF в карманном формате из готового LaTeX курса.
- Повторное использование одного и того же рабочего процесса с обернутым заголовком и обновлением иллюстраций как для обычных
  полноразмерных PDF, так и для карманных PDF в разных хост-репозиториях.

## 🧪 Рабочие хост-репозитории

`Video2Book` уже используется в нескольких хост-репозиториях с разными формами архивов.

| Хост-репозиторий | Фокус | Пример обертки | Текущие отслеживаемые выходные файлы |
| --- | --- | --- | --- |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Курс Yale `Financial Markets` с Робертом Дж. Шиллером | [examples/lazyearn/yale-financial-markets/](../examples/lazyearn/yale-financial-markets/) | [PDF курса](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf), [PDF лекций](https://github.com/lachlanchen/LazyEarn/tree/main/generated_course_notes/lazyearn/yale-financial-markets/chapters), [Markdown-расшифровки](https://github.com/lachlanchen/LazyEarn/tree/main/markdown/lazyearn/yale-financial-markets), [субтитры](https://github.com/lachlanchen/LazyEarn/tree/main/subtitles/lazyearn/yale-financial-markets) |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | Адаптация курса письма для `How You Speak and Write` | [examples/lazylearn/how-you-speak-and-write/](../examples/lazylearn/how-you-speak-and-write/), [examples/lazylearn/justice-with-michael-sandel/](../examples/lazylearn/justice-with-michael-sandel/) | [PDF курса How You Speak and Write](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf), [PDF курса Justice with Michael Sandel](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/justice-with-michael-sandel/course.pdf), [локальные PDF курса по речи](https://github.com/lachlanchen/LazyLearn/tree/main/how-to-speak-and-write), [локальный PDF о справедливости](https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf), [PDF лекций](https://github.com/lachlanchen/LazyLearn/tree/main/generated_course_notes/lazylearn/how-you-speak-and-write/chapters), [Markdown-расшифровки](https://github.com/lachlanchen/LazyLearn/tree/main/markdown/lazylearn), [субтитры](https://github.com/lachlanchen/LazyLearn/tree/main/subtitles/lazylearn) |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Полный архив лекций Леонарда Сасскинда, конвейер расшифровок и опубликованные книги конспектов | [examples/leonardsusskind/susskind-physics-archive/](../examples/leonardsusskind/susskind-physics-archive/) | [папка опубликованных книг](https://github.com/lachlanchen/leonardsusskind/tree/main), [PDF по продвинутой квантовой механике](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf), [PDF по темам теории струн](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf), [PDF по физике частиц 3](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_particle_physics_3/particle_physics_3_supersymmetry_and_grand_unification.pdf), [Markdown-расшифровки](https://github.com/lachlanchen/leonardsusskind/tree/main/markdown), [субтитры](https://github.com/lachlanchen/leonardsusskind/tree/main/subtitles) |

## 📘 Книги и PDF

Третий этап уже производит настоящие книжные выходные файлы в хост-репозиториях:

- объединенные книги курсов, такие как `course.pdf`, или каноническое имя, опубликованное хостом
- PDF по отдельным лекциям в `generated_course_notes/.../chapters/`
- деревья расшифровок в `markdown/` и деревья субтитров в `subtitles/`

Другие опубликованные книги и выходные файлы курсов:

| Хост-репозиторий | Название | Основной PDF | Примечания |
| --- | --- | --- | --- |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Yale Financial Markets | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf) | книга лекций Роберта Дж. Шиллера с полноразмерной и карманной версиями |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Hard Knocks Interviews | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/course.pdf) | прямая компиляция лекция за лекцией |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | High-Growth Dossier | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/high-growth-stocks/high-growth-stocks.pdf) | устаревшая исследовательская книга с карманными экспортами |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Quod Tango Muto | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/quod-tango-muto/quod-tango-muto.pdf) | исследовательская книга с латинским девизом и карманными экспортами |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | How You Speak and Write | [PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf) | адаптация курса письма |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | Justice with Michael Sandel | [PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/justice-with-michael-sandel/course.pdf) | книга курса по политической философии |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Classical Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/classical_mechanics_theoretical_minimum.pdf) | сводная книга в `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Quantum Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/quantum_mechanics_theoretical_minimum.pdf) | базовая книга TTM в `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Special Relativity (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/special_relativity_theoretical_minimum.pdf) | базовая книга TTM в `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | General Relativity (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/general_relativity_theoretical_minimum.pdf) | базовая книга TTM в `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Statistical Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/statistical_mechanics_theoretical_minimum.pdf) | базовая книга TTM в `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Cosmology (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/cosmology_theoretical_minimum.pdf) | базовая книга TTM в `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Advanced Quantum Mechanics | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf) | дополнительное название по физике |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Topics in String Theory | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf) | дополнительная книга по космологии / струнам |

Другие сводные книги Сасскинда доступны в [all_notes](https://github.com/lachlanchen/leonardsusskind/tree/main/all_notes).

### Указатели на локальные соседние репозитории

Если вы запускаете эти репозитории из общей родительской директории (например, `/home/lachlan/ProjectsLFS`), к тем же книгам также можно обращаться через локальные пути:

- `../LazyLearn/justice-with-michael-sandel/justice-with-michael-sandel.pdf`
- `../LazyLearn/how-to-speak-and-write/how-to-speak-and-write.pdf`
- `../LazyEarn/generated_course_notes/lazyearn/yale-financial-markets/course.pdf`
- `../leonardsusskind/<sibling-folder>/...` (PDF курсов и опубликованных книг в этом репозитории)

## 🧩 Конвейер

| Этап | Модуль | Назначение |
| --- | --- | --- |
| 1 | `playlist2videos/` | Загружает или обновляет плейлист с помощью `yt-dlp`, ведет журналы и пропускает уже заархивированные элементы. |
| 2 | `videos2subtitles/` | Расшифровывает архивные медиа в `subtitles/` и `markdown/`. |
| 3 | `subtitles2notes/` | Превращает завершенные расшифровки в TeX глав, PDF лекций и объединенные PDF курсов. |
| 4 | `scripts/process_markdown_material_book.py` | Превращает упорядоченные папки исходного Markdown в сгенерированные TeX/PDF-книги карманного размера, передавая связанные изображения в Codex. |
| 5 | `scripts/start_markdown_material_book_tmux.sh` | Запускает генератор книги из Markdown-материалов в `tmux` с безопасной для возобновления обработкой по одному источнику за раз. |
| 6 | `scripts/export_course_pocket_pdfs.sh` | Пересобирает готовые выходы `course.tex` в карманные/A5 варианты для публикационных пакетов и выводит сопоставленные отчеты overfull. |
| 7 | `scripts/export_tex_book_pocket_pdf.sh` | Пересобирает одну самостоятельную TeX-книгу/статью в сопроводительный PDF карманного размера и синхронизирует его в дерево документации хост-репозитория. |
| 8 | `subtitles2notes/templates/lecture_notes_common_preamble.tex` | Общий источник заголовка/макета PDF курса обычного размера, используемый сгенерированными книгами. |
| 9 | `scripts/fix_course_pocket_overfulls.sh` | Итерирует один вариант курса: экспорт, отчет, патч Codex и повторный экспорт, пока устранимые overfull не снизятся. |
| 10 | `scripts/fix_latex_project_overfulls.sh` | Универсальный исправитель переполнений LaTeX для любого репозитория/проекта, который можно собрать с `pdflatex` или пользовательской командой компиляции. |
| 11 | `scripts/recheck_course_figures.py` | Повторно проверяет похожие на скриншоты иллюстрации лекций относительно контекста расшифровок и кадров-замен из видео. |
| 12 | `scripts/export_course_epubs.sh` | Пересобирает готовые выходы `course.tex` напрямую в EPUB3. |

## 🚀 Быстрый старт

Клонировать напрямую:

```bash
git clone git@github.com:lachlanchen/Video2Book.git
cd Video2Book
```

Или добавить в другой репозиторий как submodule:

```bash
git submodule add git@github.com:lachlanchen/Video2Book.git Video2Book
git submodule update --init --recursive
```

## 🏗️ Структура хост-репозитория

`Video2Book` ожидает запуск из хост-репозитория, где хранятся рабочие выходные файлы:

- `subtitles/`
- `markdown/`
- `generated_course_notes/`
- `.lecture-notes-work/`

Сами видеофайлы обычно хранятся вне хост-репозитория в медиа-рабочей области, например:

- `/home/lachlan/ProjectsLFS/YoutubeDownloader`

## 🛠️ Типичное использование

Из корня хост-репозитория:

```bash
./Video2Book/scripts/download_susskind_playlist.sh
./Video2Book/scripts/start_transcription_tmux.sh
./Video2Book/scripts/start_transcription_monitor_tmux.sh
./Video2Book/scripts/start_course_notes_tmux.sh
./Video2Book/scripts/start_course_notes_monitor_tmux.sh
```

Сухой прогон загрузчика:

```bash
./Video2Book/scripts/download_susskind_playlist.sh --dry-run
```

Запустить очередь написания конспектов для одного курса:

```bash
./Video2Book/scripts/start_course_notes_tmux.sh --course supplementary/advanced_quantum_mechanics/2013_fall
```

Экспортировать компактные PDF для всех завершенных курсов (например, в `leonardsusskind`):

```bash
./Video2Book/scripts/export_course_pocket_pdfs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
```

Экспортировать одну самостоятельную книгу в `investment_pdfs/` в варианты карманного размера:

```bash
./Video2Book/scripts/export_tex_book_pocket_pdf.sh \
  --repo-root /home/lachlan/ProjectsLFS/LazyEarn \
  --project-root /home/lachlan/ProjectsLFS/LazyEarn/investment_pdfs/wealth-from-first-principles \
  --main-tex wealth-from-first-principles.tex \
  --font-mode onepointtwo \
  --suffix pocket_1_2x
```

Запустить управляемый Codex исправитель переполнений для одного варианта курса с узким макетом:

```bash
./Video2Book/scripts/start_pocket_overflow_fix_tmux.sh \
  --course core/statistical_mechanics/2013_spring_theoretical_minimum \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

Запустить очередь в tmux по всем завершенным курсам Сасскинда, по одному курсу за раз:

```bash
./Video2Book/scripts/start_pocket_overflow_fix_tmux.sh \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

Запустить универсальный исправитель LaTeX на любом проекте:

```bash
./Video2Book/scripts/fix_latex_project_overfulls.sh \
  --repo-root /path/to/repo \
  --project-root /path/to/repo/book \
  --main-tex main.tex \
  --model gpt-5.4 \
  --reasoning medium
```

Экспортировать EPUB3 напрямую из TeX для всех завершенных курсов:

```bash
./Video2Book/scripts/export_course_epubs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
```

Хост-специфичные обертки могут находиться в `examples/`. Текущие включенные шаблоны:

- `examples/lazyearn/yale-financial-markets/`
- `examples/lazylearn/how-you-speak-and-write/`
- `examples/leonardsusskind/susskind-physics-archive/`

## 🎬 Текущий пример по умолчанию

Встроенный загрузчик по умолчанию использует плейлист по физике Леонарда Сасскинда:

- <https://www.youtube.com/playlist?list=PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG>

Это значение по умолчанию — просто рабочий пример. Код устроен так, чтобы другие хост-репозитории могли адаптировать тот же конвейер к другим архивам лекций.

## 📦 Карта модулей

- [playlist2videos](../playlist2videos)
- [videos2subtitles](../videos2subtitles)
- [subtitles2notes](../subtitles2notes)
- [scripts](../scripts)
- [Передача экспорта карманного размера](../references/pocket-size-course-pdfs-handoff.md)
- [Передача макета A4 и карманного формата](../references/a4-and-pocket-pdf-layout-handoff.md)
- [Передача превью книг README](../references/readme-book-preview-handoff.md)
- [Передача исправителя переполнений LaTeX](../references/latex-overflow-fixer-handoff.md)
- [Передача экспорта EPUB](../references/tex-to-epub-handoff.md)

## 📚 Заметки по адаптации хоста

- [references/lazylearn-course-adaptation.md](../references/lazylearn-course-adaptation.md)
- [references/lazyearn-yale-financial-markets-adaptation.md](../references/lazyearn-yale-financial-markets-adaptation.md)
- [references/nanobanana-2-book-cover-handoff.md](../references/nanobanana-2-book-cover-handoff.md)
- [references/readme-book-preview-handoff.md](../references/readme-book-preview-handoff.md)
- [references/a4-and-pocket-pdf-layout-handoff.md](../references/a4-and-pocket-pdf-layout-handoff.md)
- [references/latex-overflow-fixer-handoff.md](../references/latex-overflow-fixer-handoff.md)
- [references/tex-book-translation-workflow.md](../references/tex-book-translation-workflow.md)
- [references/tex-to-epub-handoff.md](../references/tex-to-epub-handoff.md)

## 🎨 Утилита книжной обложки

`Video2Book` также включает локальный помощник Nano Banana 2 для редакторской генерации книжных обложек:

- скрипт: [scripts/book_cover_nanobanana.py](../scripts/book_cover_nanobanana.py)
- руководство: [references/nanobanana-2-book-cover-handoff.md](../references/nanobanana-2-book-cover-handoff.md)
- шаблон env: [.env.example](../.env.example)
- пример промпта для текущей книги: [examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt](../examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt)

Он повторно использует механизм отправки и опроса GRS AI из соседней работы Nano Banana, но заменяет промпты сегментации на промпт книжной обложки и сохраняет чистый след вывода для каждого запуска.

## 🌐 Утилита перевода книг

`Video2Book` также может переводить готовую книгу лекционных конспектов в соседние
языковые папки, такие как `zh/` и `jp/`, сохраняя структуру TeX,
уравнения и изображения без изменений.

- менеджер: [scripts/translate_tex_book.py](../scripts/translate_tex_book.py)
- запускатель цикла: [scripts/process_book_translation_one_by_one.sh](../scripts/process_book_translation_one_by_one.sh)
- стартер tmux: [scripts/start_book_translation_tmux.sh](../scripts/start_book_translation_tmux.sh)
- заметка по рабочему процессу: [references/tex-book-translation-workflow.md](../references/tex-book-translation-workflow.md)

Цикл перевода:

- инициализирует готовое к XeLaTeX переведенное издание
- сначала переводит основной файл книги, затем каждую главу
- поддерживает как книги с разделенными главами, так и однофайловые книги `main.tex` со встроенными блоками `\chapter{...}`
- именует переведенные входные файлы с языковым суффиксом, например `book_zh.tex` или `book_jp.tex`
- перекомпилирует после каждой единицы
- может коммитить и пушить переведенную папку после каждой завершенной единицы

## ⚙️ Требования

- `tmux`
- `ffmpeg`
- `pdflatex`
- `pdfunite`
- `pdftotext`
- `yt-dlp`
- `pandoc` (для `scripts/export_course_epubs.sh`)
- CLI `codex` для конвейера конспектов
- рабочее conda-окружение `whisper` для расшифровки
- `whisper_with_lang_detect`, если вам нужен основной путь субтитров вместо только резервного Whisper
- `rsync` (для необязательной локальной синхронизации публикации карманных PDF)

## 🤝 Когда подходит

`Video2Book` хорошо подходит, когда вам нужны:

- локальный для репозитория конвейер вместо монолитного приложения
- генерация лекционных конспектов с приоритетом расшифровок
- долговременная автоматизация на основе tmux
- воспроизводимая структура архива для учебных материалов

## 🙏 Поддержка

| Пожертвовать | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Лицензия

Этот репозиторий лицензирован по GNU General Public License v3.0.
