[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![LazyingArt 배너](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://lazying.art)

# LazyingArt LLC의 Video2Book

> **LazyingArt LLC의 Video2Book**. 웹사이트: [lazying.art](https://lazying.art) 및 [learn.lazying.art](https://learn.lazying.art).

[![LazyingArt](https://img.shields.io/badge/Website-lazying.art-111827?style=for-the-badge&logo=googlechrome&logoColor=white)](https://lazying.art)
[![Learn](https://img.shields.io/badge/Learn-learn.lazying.art-1f2937?style=for-the-badge&logo=bookstack&logoColor=white)](https://learn.lazying.art)

[![Toolkit](https://img.shields.io/badge/toolkit-video__to__book-111827?style=for-the-badge&logo=bookstack&logoColor=white)](#)
[![Downloader](https://img.shields.io/badge/stage_1-playlist2videos-1d4ed8?style=for-the-badge&logo=youtube&logoColor=white)](#-pipeline)
[![Transcription](https://img.shields.io/badge/stage_2-videos2subtitles-0f766e?style=for-the-badge&logo=openai&logoColor=white)](#-pipeline)
[![Notes](https://img.shields.io/badge/stage_3-subtitles2notes-f97316?style=for-the-badge&logo=latex&logoColor=white)](#-pipeline)
[![tmux](https://img.shields.io/badge/runtime-tmux-7c3aed?style=for-the-badge&logo=gnu-bash&logoColor=white)](#-quick-start)

`Video2Book`은 긴 형식의 동영상 모음을 오래 보관할 수 있는 학습 자료로 바꾸는 실용적인 파이프라인입니다. 다운로드된 미디어, 타임스탬프가 있는 전사문, 그리고 컴파일된 PDF가 포함된 전사문 기반 강의 노트를 만듭니다.

## 📚 대표 도서

이 미리보기는 `LazyEarn` 및 `LazyLearn`에서 발행된 각 PDF의 추출된 첫 페이지를 사용합니다.

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/wealth-from-first-principles/wealth-from-first-principles.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/wealth-from-first-principles/cover-page-1.png" width="180" alt="첫 원리에서 얻는 부 표지" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/dynamic_book/how-you-got-rich.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-rich/cover-page-1.png" width="180" alt="당신은 어떻게 부자가 되었나 표지" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/jim-rohn-originals-no-ai/course.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-successful/cover-page-1.png" width="180" alt="당신은 어떻게 성공했나 표지" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/how-you-got-happiness-publication/how-you-got-happiness.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-happiness/cover-page-1.png" width="180" alt="당신은 어떻게 행복을 얻었나 표지" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/wealth-from-first-principles/wealth-from-first-principles.pdf"><strong>첫 원리에서 얻는 부</strong></a><br />
      돈, 소유권, 청구권, 그리고 복리
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/dynamic_book/how-you-got-rich.pdf"><strong>당신은 어떻게 부자가 되었나?</strong></a><br />
      인터뷰 증거를 바탕으로 만든 비선형 부의 책
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/jim-rohn-originals-no-ai/course.pdf"><strong>당신은 어떻게 성공했나?</strong></a><br />
      Jim Rohn의 성공 강의를 더 매끄러운 책의 흐름으로 재배열한 책
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/how-you-got-happiness-publication/how-you-got-happiness.pdf"><strong>당신은 어떻게 행복을 얻었나?</strong></a><br />
      주의, 두려움, 명상, 자유에 관한 책으로 다듬은 Krishnamurti 강연
    </td>
  </tr>
</table>

`LazyLearn`은 다국어 글쓰기 책과 완성된 정의 강좌 책도 발행합니다.

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write/cover-page-1.png" width="180" alt="영어 말하기와 쓰기 표지" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-zh.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write-zh/cover-page-1.png" width="180" alt="번체 중국어 말하기와 쓰기 표지" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-jp.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write-jp/cover-page-1.png" width="180" alt="일본어 말하기와 쓰기 표지" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/justice-with-michael-sandel/cover-page-1.png" width="180" alt="Michael Sandel과 함께하는 정의 표지" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write.pdf"><strong>말하기와 쓰기</strong></a><br />
      재배열된 영어판
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-zh.pdf"><strong>如何說話與寫作</strong></a><br />
      번체 중국어판
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-jp.pdf"><strong>話し方と書き方</strong></a><br />
      일본어판
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf"><strong>Michael Sandel과 함께하는 정의</strong></a><br />
      Michael Sandel 정치철학 강좌 책
    </td>
  </tr>
</table>

`leonardsusskind`는 핵심 Theoretical Minimum 물리학 책도 발행합니다.

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/quantum_mechanics_theoretical_minimum.png" width="180" alt="양자역학 Theoretical Minimum 표지" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/general_relativity_theoretical_minimum.png" width="180" alt="일반상대성이론 Theoretical Minimum 표지" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/statistical_mechanics_theoretical_minimum_first_page.png" width="180" alt="통계역학 Theoretical Minimum 표지" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/cosmology_theoretical_minimum_first_page.png" width="180" alt="우주론 Theoretical Minimum 표지" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf"><strong>양자역학</strong></a><br />
      Theoretical Minimum 핵심 도서
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf"><strong>일반상대성이론</strong></a><br />
      Theoretical Minimum 핵심 도서
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf"><strong>통계역학</strong></a><br />
      Theoretical Minimum 핵심 도서
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf"><strong>우주론</strong></a><br />
      Theoretical Minimum 핵심 도서
    </td>
  </tr>
</table>

## ✨ 다루는 내용

- 재생목록을 안정적인 외부 미디어 아카이브로 다운로드합니다.
- 동영상을 `.srt` 자막과 타임스탬프가 있는 Markdown으로 전사합니다.
- 완성된 전사문 세트를 구조화된 TeX 노트와 병합된 강좌 PDF로 변환합니다.
- 순서가 지정된 Markdown 자료 폴더를 포켓 크기 TeX/PDF 책으로 변환합니다.
- 큐 스크립트와 모니터/가드 스크립트를 사용해 긴 작업을 `tmux`에서 실행합니다.
- 완성된 강좌 LaTeX에서 압축된 포켓 형식 동반 PDF를 내보냅니다.
- 호스트 저장소 전반에서 일반 풀사이즈 PDF와 포켓 PDF 모두에 동일한 래핑 헤더 및 그림 새로고침 워크플로를 재사용합니다.

## 🧪 작동 중인 호스트 저장소

`Video2Book`은 이미 서로 다른 아카이브 구조를 가진 여러 호스트 저장소에서 사용되고 있습니다.

| 호스트 저장소 | 초점 | 래퍼 예시 | 현재 추적 중인 출력물 |
| --- | --- | --- | --- |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Robert J. Shiller의 Yale `Financial Markets` 강좌 | [examples/lazyearn/yale-financial-markets/](../examples/lazyearn/yale-financial-markets/) | [강좌 PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf), [강의 PDF](https://github.com/lachlanchen/LazyEarn/tree/main/generated_course_notes/lazyearn/yale-financial-markets/chapters), [markdown 전사문](https://github.com/lachlanchen/LazyEarn/tree/main/markdown/lazyearn/yale-financial-markets), [자막](https://github.com/lachlanchen/LazyEarn/tree/main/subtitles/lazyearn/yale-financial-markets) |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | `How You Speak and Write`를 위한 글쓰기 강좌 각색 | [examples/lazylearn/how-you-speak-and-write/](../examples/lazylearn/how-you-speak-and-write/), [examples/lazylearn/justice-with-michael-sandel/](../examples/lazylearn/justice-with-michael-sandel/) | [How You Speak and Write 강좌 PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf), [Michael Sandel과 함께하는 정의 강좌 PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/justice-with-michael-sandel/course.pdf), [로컬 말하기 강좌 PDF](https://github.com/lachlanchen/LazyLearn/tree/main/how-to-speak-and-write), [로컬 정의 PDF](https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf), [강의 PDF](https://github.com/lachlanchen/LazyLearn/tree/main/generated_course_notes/lazylearn/how-you-speak-and-write/chapters), [markdown 전사문](https://github.com/lachlanchen/LazyLearn/tree/main/markdown/lazylearn), [자막](https://github.com/lachlanchen/LazyLearn/tree/main/subtitles/lazylearn) |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | 전체 Leonard Susskind 강의 아카이브, 전사 파이프라인, 발행된 노트 책 | [examples/leonardsusskind/susskind-physics-archive/](../examples/leonardsusskind/susskind-physics-archive/) | [발행된 책 폴더](https://github.com/lachlanchen/leonardsusskind/tree/main), [고급 양자 PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf), [끈 이론 주제 PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf), [입자물리학 3 PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_particle_physics_3/particle_physics_3_supersymmetry_and_grand_unification.pdf), [markdown 전사문](https://github.com/lachlanchen/leonardsusskind/tree/main/markdown), [자막](https://github.com/lachlanchen/leonardsusskind/tree/main/subtitles) |

## 📘 도서 및 PDF

세 번째 단계는 이미 호스트 저장소에서 실제 책 같은 출력물을 만들고 있습니다.

- `course.pdf` 같은 병합된 강좌 책 또는 호스트가 발행한 표준 이름
- `generated_course_notes/.../chapters/` 아래의 강의별 PDF
- `markdown/`의 전사문 트리와 `subtitles/`의 자막 트리

그 밖의 발행 도서 및 강좌 출력물:

| 호스트 저장소 | 제목 | 주요 PDF | 노트 |
| --- | --- | --- | --- |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Yale 금융시장 | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf) | 풀사이즈 및 포켓 변형이 있는 Robert J. Shiller 강의 책 |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Hard Knocks 인터뷰 | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/course.pdf) | 강의별 직접 컴파일 |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | 고성장 도시에 | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/high-growth-stocks/high-growth-stocks.pdf) | 포켓 내보내기가 포함된 레거시 리서치 책 |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Quod Tango Muto | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/quod-tango-muto/quod-tango-muto.pdf) | 포켓 내보내기가 포함된 라틴어 좌우명 리서치 책 |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | 말하기와 쓰기 | [PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf) | 글쓰기 강좌 각색 |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | Michael Sandel과 함께하는 정의 | [PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/justice-with-michael-sandel/course.pdf) | 정치철학 강좌 책 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | 고전역학 (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/classical_mechanics_theoretical_minimum.pdf) | `all_notes/`의 통합 도서 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | 양자역학 (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/quantum_mechanics_theoretical_minimum.pdf) | `all_notes/`의 핵심 TTM 도서 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | 특수상대성이론 (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/special_relativity_theoretical_minimum.pdf) | `all_notes/`의 핵심 TTM 도서 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | 일반상대성이론 (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/general_relativity_theoretical_minimum.pdf) | `all_notes/`의 핵심 TTM 도서 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | 통계역학 (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/statistical_mechanics_theoretical_minimum.pdf) | `all_notes/`의 핵심 TTM 도서 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | 우주론 (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/cosmology_theoretical_minimum.pdf) | `all_notes/`의 핵심 TTM 도서 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | 고급 양자역학 | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf) | 보충 물리학 제목 |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | 끈 이론 주제 | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf) | 보충 우주론 / 끈 제목 |

그 밖의 Susskind 통합 제목은 [all_notes](https://github.com/lachlanchen/leonardsusskind/tree/main/all_notes)에서 볼 수 있습니다.

### 로컬 형제 저장소 포인터

공유 상위 디렉터리(예: `/home/lachlan/ProjectsLFS`)에서 이 저장소들을 실행하는 경우, 같은 책을 로컬 경로로도 지정할 수 있습니다.

- `../LazyLearn/justice-with-michael-sandel/justice-with-michael-sandel.pdf`
- `../LazyLearn/how-to-speak-and-write/how-to-speak-and-write.pdf`
- `../LazyEarn/generated_course_notes/lazyearn/yale-financial-markets/course.pdf`
- `../leonardsusskind/<sibling-folder>/...` (해당 저장소의 강좌 및 발행 도서 PDF)

## 🧩 파이프라인

| 단계 | 모듈 | 목적 |
| --- | --- | --- |
| 1 | `playlist2videos/` | `yt-dlp`로 재생목록을 다운로드하거나 새로고침하고, 로그를 유지하며, 이미 아카이브된 항목은 건너뜁니다. |
| 2 | `videos2subtitles/` | 아카이브된 미디어를 `subtitles/` 및 `markdown/`으로 전사합니다. |
| 3 | `subtitles2notes/` | 완성된 전사문을 장 TeX, 강의 PDF, 병합된 강좌 PDF로 바꿉니다. |
| 4 | `scripts/process_markdown_material_book.py` | 관련 이미지를 Codex에 전달하면서 순서가 지정된 원본 Markdown 폴더를 생성된 포켓 크기 TeX/PDF 책으로 바꿉니다. |
| 5 | `scripts/start_markdown_material_book_tmux.sh` | 재개에 안전한 한 번에 한 원본 처리 방식으로 Markdown 자료 책 작성기를 `tmux`에서 실행합니다. |
| 6 | `scripts/export_course_pocket_pdfs.sh` | 발행 패키지를 위해 완성된 `course.tex` 출력물을 포켓/A5 변형으로 다시 빌드하고 매핑된 overfull 보고서를 출력합니다. |
| 7 | `scripts/export_tex_book_pocket_pdf.sh` | 독립형 TeX 책/논문 하나를 포켓 크기 동반 PDF로 다시 빌드하고 호스트 저장소 docs 트리로 동기화합니다. |
| 8 | `subtitles2notes/templates/lecture_notes_common_preamble.tex` | 생성된 책에서 사용하는 공유 일반 크기 강좌 PDF 헤더/레이아웃 소스입니다. |
| 9 | `scripts/fix_course_pocket_overfulls.sh` | 강좌 변형 하나에 대해 내보내기, 보고, Codex 패치, 재내보내기를 반복하여 조치 가능한 overfull을 줄입니다. |
| 10 | `scripts/fix_latex_project_overfulls.sh` | `pdflatex` 또는 사용자 지정 컴파일 명령으로 빌드할 수 있는 모든 저장소/프로젝트용 범용 LaTeX 오버플로 수정기입니다. |
| 11 | `scripts/recheck_course_figures.py` | 스크린샷 같은 강의 그림을 전사문 맥락 및 대체 동영상 프레임과 대조해 다시 감사합니다. |
| 12 | `scripts/export_course_epubs.sh` | 완성된 `course.tex` 출력물을 직접 EPUB3로 다시 빌드합니다. |

## 🚀 빠른 시작

직접 클론합니다.

```bash
git clone git@github.com:lachlanchen/Video2Book.git
cd Video2Book
```

또는 다른 저장소에 서브모듈로 추가합니다.

```bash
git submodule add git@github.com:lachlanchen/Video2Book.git Video2Book
git submodule update --init --recursive
```

## 🏗️ 호스트 저장소 레이아웃

`Video2Book`은 작업 출력물을 저장하는 호스트 저장소에서 실행되는 것을 전제로 합니다.

- `subtitles/`
- `markdown/`
- `generated_course_notes/`
- `.lecture-notes-work/`

동영상 파일 자체는 일반적으로 다음과 같은 미디어 작업공간의 호스트 저장소 밖에 보관됩니다.

- `/home/lachlan/ProjectsLFS/YoutubeDownloader`

## 🛠️ 일반적인 사용법

호스트 저장소 루트에서:

```bash
./Video2Book/scripts/download_susskind_playlist.sh
./Video2Book/scripts/start_transcription_tmux.sh
./Video2Book/scripts/start_transcription_monitor_tmux.sh
./Video2Book/scripts/start_course_notes_tmux.sh
./Video2Book/scripts/start_course_notes_monitor_tmux.sh
```

다운로더를 dry-run으로 실행합니다.

```bash
./Video2Book/scripts/download_susskind_playlist.sh --dry-run
```

한 강좌의 노트 작성 큐를 시작합니다.

```bash
./Video2Book/scripts/start_course_notes_tmux.sh --course supplementary/advanced_quantum_mechanics/2013_fall
```

완료된 모든 강좌의 압축 PDF를 내보냅니다(예: `leonardsusskind`에서).

```bash
./Video2Book/scripts/export_course_pocket_pdfs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
```

`investment_pdfs/`의 독립형 책 하나를 포켓 크기 변형으로 내보냅니다.

```bash
./Video2Book/scripts/export_tex_book_pocket_pdf.sh \
  --repo-root /home/lachlan/ProjectsLFS/LazyEarn \
  --project-root /home/lachlan/ProjectsLFS/LazyEarn/investment_pdfs/wealth-from-first-principles \
  --main-tex wealth-from-first-principles.tex \
  --font-mode onepointtwo \
  --suffix pocket_1_2x
```

좁은 레이아웃 강좌 변형 하나에 대해 Codex 기반 오버플로 수정기를 실행합니다.

```bash
./Video2Book/scripts/start_pocket_overflow_fix_tmux.sh \
  --course core/statistical_mechanics/2013_spring_theoretical_minimum \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

완료된 모든 Susskind 강좌에 대해 한 번에 한 강좌씩 tmux에서 큐를 실행합니다.

```bash
./Video2Book/scripts/start_pocket_overflow_fix_tmux.sh \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

어떤 프로젝트에서든 범용 LaTeX 수정기를 실행합니다.

```bash
./Video2Book/scripts/fix_latex_project_overfulls.sh \
  --repo-root /path/to/repo \
  --project-root /path/to/repo/book \
  --main-tex main.tex \
  --model gpt-5.4 \
  --reasoning medium
```

완료된 모든 강좌에 대해 TeX에서 직접 EPUB3를 내보냅니다.

```bash
./Video2Book/scripts/export_course_epubs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
```

호스트별 래퍼는 `examples/` 아래에 둘 수 있습니다. 현재 포함된 패턴:

- `examples/lazyearn/yale-financial-markets/`
- `examples/lazylearn/how-you-speak-and-write/`
- `examples/leonardsusskind/susskind-physics-archive/`

## 🎬 현재 기본 예시

포함된 다운로더는 기본적으로 Leonard Susskind 물리학 재생목록을 사용합니다.

- <https://www.youtube.com/playlist?list=PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG>

이 기본값은 작동 예시일 뿐입니다. 코드는 다른 호스트 저장소가 동일한 파이프라인을 서로 다른 강의 아카이브에 맞게 조정할 수 있도록 구조화되어 있습니다.

## 📦 모듈 맵

- [playlist2videos](../playlist2videos)
- [videos2subtitles](../videos2subtitles)
- [subtitles2notes](../subtitles2notes)
- [scripts](../scripts)
- [포켓 내보내기 인계](../references/pocket-size-course-pdfs-handoff.md)
- [A4 및 포켓 레이아웃 인계](../references/a4-and-pocket-pdf-layout-handoff.md)
- [README 책 미리보기 인계](../references/readme-book-preview-handoff.md)
- [LaTeX 오버플로 수정기 인계](../references/latex-overflow-fixer-handoff.md)
- [EPUB 내보내기 인계](../references/tex-to-epub-handoff.md)

## 📚 호스트 적응 노트

- [references/lazylearn-course-adaptation.md](../references/lazylearn-course-adaptation.md)
- [references/lazyearn-yale-financial-markets-adaptation.md](../references/lazyearn-yale-financial-markets-adaptation.md)
- [references/nanobanana-2-book-cover-handoff.md](../references/nanobanana-2-book-cover-handoff.md)
- [references/readme-book-preview-handoff.md](../references/readme-book-preview-handoff.md)
- [references/a4-and-pocket-pdf-layout-handoff.md](../references/a4-and-pocket-pdf-layout-handoff.md)
- [references/latex-overflow-fixer-handoff.md](../references/latex-overflow-fixer-handoff.md)
- [references/tex-book-translation-workflow.md](../references/tex-book-translation-workflow.md)
- [references/tex-to-epub-handoff.md](../references/tex-to-epub-handoff.md)

## 🎨 책 표지 유틸리티

`Video2Book`에는 편집용 책 표지 생성을 위한 로컬 Nano Banana 2 헬퍼도 포함되어 있습니다.

- 스크립트: [scripts/book_cover_nanobanana.py](../scripts/book_cover_nanobanana.py)
- 가이드: [references/nanobanana-2-book-cover-handoff.md](../references/nanobanana-2-book-cover-handoff.md)
- env 템플릿: [.env.example](../.env.example)
- 현재 책 예시 프롬프트: [examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt](../examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt)

형제 Nano Banana 작업의 GRS AI 제출 및 폴링 메커니즘을 재사용하지만, 세그멘테이션 프롬프트를 책 표지 프롬프트로 바꾸고 실행마다 깔끔한 출력 추적을 저장합니다.

## 🌐 책 번역 유틸리티

`Video2Book`은 완성된 강의 노트 책을 `zh/` 및 `jp/` 같은 형제 언어 폴더로 번역하면서 TeX 구조, 수식, 이미지를 그대로 유지할 수도 있습니다.

- 관리자: [scripts/translate_tex_book.py](../scripts/translate_tex_book.py)
- 루프 실행기: [scripts/process_book_translation_one_by_one.sh](../scripts/process_book_translation_one_by_one.sh)
- tmux 시작기: [scripts/start_book_translation_tmux.sh](../scripts/start_book_translation_tmux.sh)
- 워크플로 노트: [references/tex-book-translation-workflow.md](../references/tex-book-translation-workflow.md)

번역 루프는 다음을 수행합니다.

- XeLaTeX 준비가 된 번역판을 초기화합니다
- 먼저 메인 책 파일을 번역한 다음 각 장을 번역합니다
- 분할 장 책과 인라인 `\chapter{...}` 블록이 있는 단일 파일 `main.tex` 책을 모두 지원합니다
- 번역된 진입 파일에 `book_zh.tex` 또는 `book_jp.tex` 같은 언어 접미사를 붙입니다
- 각 단위 후 다시 컴파일합니다
- 완료된 각 단위 후 번역된 폴더를 커밋하고 푸시할 수 있습니다

## ⚙️ 요구 사항

- `tmux`
- `ffmpeg`
- `pdflatex`
- `pdfunite`
- `pdftotext`
- `yt-dlp`
- `pandoc` (`scripts/export_course_epubs.sh`용)
- 노트 파이프라인용 `codex` CLI
- 전사용으로 작동하는 `whisper` conda env
- fallback 전용 Whisper 대신 기본 자막 경로를 원한다면 `whisper_with_lang_detect`
- `rsync` (포켓 PDF의 선택적 로컬 발행 동기화용)

## 🤝 잘 맞는 경우

`Video2Book`은 다음을 원할 때 잘 맞습니다.

- 모놀리식 앱 대신 저장소 로컬 파이프라인
- 전사문 우선 강의 노트 생성
- tmux 기반 장시간 자동화
- 학습 자료를 위한 재현 가능한 아카이브 구조

## 🙏 후원

| 기부 | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 라이선스

이 저장소는 GNU General Public License v3.0에 따라 라이선스가 부여됩니다.
