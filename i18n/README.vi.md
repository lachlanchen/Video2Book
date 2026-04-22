[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![Băng rôn LazyingArt](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://lazying.art)

# Video2Book của LazyingArt LLC

> **Video2Book của LazyingArt LLC**. Trang web: [lazying.art](https://lazying.art) và [learn.lazying.art](https://learn.lazying.art).

[![LazyingArt](https://img.shields.io/badge/Website-lazying.art-111827?style=for-the-badge&logo=googlechrome&logoColor=white)](https://lazying.art)
[![Learn](https://img.shields.io/badge/Learn-learn.lazying.art-1f2937?style=for-the-badge&logo=bookstack&logoColor=white)](https://learn.lazying.art)

[![Toolkit](https://img.shields.io/badge/toolkit-video__to__book-111827?style=for-the-badge&logo=bookstack&logoColor=white)](#)
[![Downloader](https://img.shields.io/badge/stage_1-playlist2videos-1d4ed8?style=for-the-badge&logo=youtube&logoColor=white)](#-quy-trình)
[![Transcription](https://img.shields.io/badge/stage_2-videos2subtitles-0f766e?style=for-the-badge&logo=openai&logoColor=white)](#-quy-trình)
[![Notes](https://img.shields.io/badge/stage_3-subtitles2notes-f97316?style=for-the-badge&logo=latex&logoColor=white)](#-quy-trình)
[![tmux](https://img.shields.io/badge/runtime-tmux-7c3aed?style=for-the-badge&logo=gnu-bash&logoColor=white)](#-bắt-đầu-nhanh)

`Video2Book` là một quy trình thực tế để biến các bộ sưu tập video dài thành tài liệu học tập bền vững: media đã tải xuống, bản chép lời có mốc thời gian, và ghi chú bài giảng phái sinh từ bản chép lời với PDF đã biên dịch.

## 📚 Sách chủ lực

Các bản xem trước này dùng trang đầu tiên được trích xuất của từng PDF đã xuất bản từ `LazyEarn`
và `LazyLearn`.

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/wealth-from-first-principles/wealth-from-first-principles.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/wealth-from-first-principles/cover-page-1.png" width="180" alt="Bìa Wealth from First Principles" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/dynamic_book/how-you-got-rich.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-rich/cover-page-1.png" width="180" alt="Bìa How You Got Rich" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/jim-rohn-originals-no-ai/course.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-successful/cover-page-1.png" width="180" alt="Bìa How You Got Successful" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/how-you-got-happiness-publication/how-you-got-happiness.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-happiness/cover-page-1.png" width="180" alt="Bìa How You Got Happiness" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/wealth-from-first-principles/wealth-from-first-principles.pdf"><strong>Wealth from First Principles</strong></a><br />
      tiền bạc, quyền sở hữu, quyền đòi hỏi, và lãi kép
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/dynamic_book/how-you-got-rich.pdf"><strong>How You Got Rich?</strong></a><br />
      một cuốn sách phi tuyến tính về của cải, được xây từ bằng chứng phỏng vấn
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/jim-rohn-originals-no-ai/course.pdf"><strong>How You Got Successful?</strong></a><br />
      các bài giảng thành công của Jim Rohn được sắp xếp lại thành một mạch sách mượt hơn
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/how-you-got-happiness-publication/how-you-got-happiness.pdf"><strong>How You Got Happiness?</strong></a><br />
      các buổi nói chuyện của Krishnamurti được định hình thành một cuốn sách về chú tâm, sợ hãi, thiền định, và tự do
    </td>
  </tr>
</table>

`LazyLearn` cũng xuất bản một cuốn sách viết đa ngôn ngữ cùng một cuốn sách khóa học về công lý
đã hoàn thiện:

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write/cover-page-1.png" width="180" alt="Bìa How to Speak and Write tiếng Anh" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-zh.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write-zh/cover-page-1.png" width="180" alt="Bìa How to Speak and Write tiếng Trung phồn thể" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-jp.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write-jp/cover-page-1.png" width="180" alt="Bìa How to Speak and Write tiếng Nhật" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/justice-with-michael-sandel/cover-page-1.png" width="180" alt="Bìa Justice with Michael Sandel" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write.pdf"><strong>How to Speak and Write</strong></a><br />
      ấn bản tiếng Anh đã sắp xếp lại
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-zh.pdf"><strong>如何說話與寫作</strong></a><br />
      ấn bản tiếng Trung phồn thể
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-jp.pdf"><strong>話し方と書き方</strong></a><br />
      ấn bản tiếng Nhật
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf"><strong>Justice with Michael Sandel</strong></a><br />
      sách khóa học triết học chính trị của Michael Sandel
    </td>
  </tr>
</table>

`leonardsusskind` cũng xuất bản các sách vật lý Theoretical Minimum cốt lõi:

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/quantum_mechanics_theoretical_minimum.png" width="180" alt="Bìa Quantum Mechanics Theoretical Minimum" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/general_relativity_theoretical_minimum.png" width="180" alt="Bìa General Relativity Theoretical Minimum" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/statistical_mechanics_theoretical_minimum_first_page.png" width="180" alt="Bìa Statistical Mechanics Theoretical Minimum" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/cosmology_theoretical_minimum_first_page.png" width="180" alt="Bìa Cosmology Theoretical Minimum" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf"><strong>Quantum Mechanics</strong></a><br />
      sách cốt lõi Theoretical Minimum
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf"><strong>General Relativity</strong></a><br />
      sách cốt lõi Theoretical Minimum
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf"><strong>Statistical Mechanics</strong></a><br />
      sách cốt lõi Theoretical Minimum
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf"><strong>Cosmology</strong></a><br />
      sách cốt lõi Theoretical Minimum
    </td>
  </tr>
</table>

## ✨ Nội dung bao quát

- Tải một playlist vào một kho lưu trữ media bên ngoài ổn định.
- Chép lời video thành phụ đề `.srt` và Markdown có mốc thời gian.
- Chuyển các bộ bản chép lời đã hoàn tất thành ghi chú TeX có cấu trúc và PDF khóa học đã gộp.
- Chuyển các thư mục tài liệu Markdown có thứ tự thành sách TeX/PDF khổ bỏ túi.
- Chạy các tác vụ dài trong `tmux` bằng script hàng đợi và script giám sát/bảo vệ.
- Xuất các PDF đồng hành định dạng bỏ túi gọn từ LaTeX khóa học đã hoàn thiện.
- Tái sử dụng cùng quy trình header bọc và làm mới hình cho cả PDF khổ thường
  kích thước đầy đủ và PDF bỏ túi trên nhiều repo chủ.

## 🧪 Repo chủ đang hoạt động

`Video2Book` đã được dùng trong nhiều repo chủ với các cấu trúc lưu trữ khác nhau.

| Repo chủ | Trọng tâm | Ví dụ wrapper | Đầu ra đang được theo dõi hiện tại |
| --- | --- | --- | --- |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Khóa `Financial Markets` của Yale với Robert J. Shiller | [examples/lazyearn/yale-financial-markets/](../examples/lazyearn/yale-financial-markets/) | [PDF khóa học](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf), [PDF bài giảng](https://github.com/lachlanchen/LazyEarn/tree/main/generated_course_notes/lazyearn/yale-financial-markets/chapters), [bản chép lời markdown](https://github.com/lachlanchen/LazyEarn/tree/main/markdown/lazyearn/yale-financial-markets), [phụ đề](https://github.com/lachlanchen/LazyEarn/tree/main/subtitles/lazyearn/yale-financial-markets) |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | Chuyển thể khóa học viết cho `How You Speak and Write` | [examples/lazylearn/how-you-speak-and-write/](../examples/lazylearn/how-you-speak-and-write/), [examples/lazylearn/justice-with-michael-sandel/](../examples/lazylearn/justice-with-michael-sandel/) | [PDF khóa học How You Speak and Write](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf), [PDF khóa học Justice with Michael Sandel](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/justice-with-michael-sandel/course.pdf), [PDF khóa học speaker cục bộ](https://github.com/lachlanchen/LazyLearn/tree/main/how-to-speak-and-write), [PDF công lý cục bộ](https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf), [PDF bài giảng](https://github.com/lachlanchen/LazyLearn/tree/main/generated_course_notes/lazylearn/how-you-speak-and-write/chapters), [bản chép lời markdown](https://github.com/lachlanchen/LazyLearn/tree/main/markdown/lazylearn), [phụ đề](https://github.com/lachlanchen/LazyLearn/tree/main/subtitles/lazylearn) |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Kho lưu trữ bài giảng Leonard Susskind đầy đủ, quy trình bản chép lời, và sách ghi chú đã xuất bản | [examples/leonardsusskind/susskind-physics-archive/](../examples/leonardsusskind/susskind-physics-archive/) | [thư mục sách đã xuất bản](https://github.com/lachlanchen/leonardsusskind/tree/main), [PDF advanced quantum](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf), [PDF topics in string theory](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf), [PDF particle physics 3](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_particle_physics_3/particle_physics_3_supersymmetry_and_grand_unification.pdf), [bản chép lời markdown](https://github.com/lachlanchen/leonardsusskind/tree/main/markdown), [phụ đề](https://github.com/lachlanchen/leonardsusskind/tree/main/subtitles) |

## 📘 Sách và PDF

Giai đoạn thứ ba đã tạo ra các đầu ra giống sách thật trong các repo chủ:

- sách khóa học đã gộp như `course.pdf` hoặc một tên chuẩn do repo chủ xuất bản
- PDF theo từng bài giảng trong `generated_course_notes/.../chapters/`
- cây bản chép lời trong `markdown/` và cây phụ đề trong `subtitles/`

Các sách và đầu ra khóa học đã xuất bản khác:

| Repo chủ | Tựa đề | PDF chính | Ghi chú |
| --- | --- | --- | --- |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Yale Financial Markets | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf) | sách bài giảng của Robert J. Shiller với biến thể khổ đầy đủ và bỏ túi |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Hard Knocks Interviews | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/course.pdf) | biên dịch trực tiếp từng bài giảng |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | High-Growth Dossier | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/high-growth-stocks/high-growth-stocks.pdf) | sách nghiên cứu legacy với bản xuất bỏ túi |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Quod Tango Muto | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/quod-tango-muto/quod-tango-muto.pdf) | sách nghiên cứu mang châm ngôn Latin với bản xuất bỏ túi |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | How You Speak and Write | [PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf) | chuyển thể khóa học viết |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | Justice with Michael Sandel | [PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/justice-with-michael-sandel/course.pdf) | sách khóa học triết học chính trị |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Classical Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/classical_mechanics_theoretical_minimum.pdf) | sách hợp nhất trong `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Quantum Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/quantum_mechanics_theoretical_minimum.pdf) | sách TTM cốt lõi trong `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Special Relativity (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/special_relativity_theoretical_minimum.pdf) | sách TTM cốt lõi trong `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | General Relativity (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/general_relativity_theoretical_minimum.pdf) | sách TTM cốt lõi trong `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Statistical Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/statistical_mechanics_theoretical_minimum.pdf) | sách TTM cốt lõi trong `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Cosmology (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/cosmology_theoretical_minimum.pdf) | sách TTM cốt lõi trong `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Advanced Quantum Mechanics | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf) | tựa vật lý bổ trợ |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Topics in String Theory | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf) | tựa bổ trợ về vũ trụ học / dây |

Các tựa Susskind hợp nhất khác có trong [all_notes](https://github.com/lachlanchen/leonardsusskind/tree/main/all_notes).

### Con trỏ repo anh em cục bộ

Nếu bạn chạy các repo này từ một thư mục cha dùng chung (ví dụ `/home/lachlan/ProjectsLFS`), cùng các sách đó cũng có thể được truy cập qua đường dẫn cục bộ:

- `../LazyLearn/justice-with-michael-sandel/justice-with-michael-sandel.pdf`
- `../LazyLearn/how-to-speak-and-write/how-to-speak-and-write.pdf`
- `../LazyEarn/generated_course_notes/lazyearn/yale-financial-markets/course.pdf`
- `../leonardsusskind/<sibling-folder>/...` (PDF khóa học và PDF sách đã xuất bản trong repo đó)

## 🧩 Quy trình

| Giai đoạn | Mô-đun | Mục đích |
| --- | --- | --- |
| 1 | `playlist2videos/` | Tải xuống hoặc làm mới một playlist bằng `yt-dlp`, giữ log, và bỏ qua các mục đã được lưu trữ. |
| 2 | `videos2subtitles/` | Chép lời media đã lưu trữ vào `subtitles/` và `markdown/`. |
| 3 | `subtitles2notes/` | Biến các bản chép lời đã hoàn tất thành TeX chương, PDF bài giảng, và PDF khóa học đã gộp. |
| 4 | `scripts/process_markdown_material_book.py` | Biến các thư mục Markdown nguồn có thứ tự thành sách TeX/PDF khổ bỏ túi đã tạo, đồng thời chuyển ảnh liên quan cho Codex. |
| 5 | `scripts/start_markdown_material_book_tmux.sh` | Chạy trình viết sách từ tài liệu Markdown trong `tmux`, với xử lý từng nguồn một an toàn khi tiếp tục. |
| 6 | `scripts/export_course_pocket_pdfs.sh` | Dựng lại các đầu ra `course.tex` đã hoàn thiện thành biến thể bỏ túi/A5 cho gói xuất bản và phát sinh báo cáo overfull đã ánh xạ. |
| 7 | `scripts/export_tex_book_pocket_pdf.sh` | Dựng lại một sách/bài viết TeX độc lập thành PDF đồng hành khổ bỏ túi và đồng bộ nó vào cây docs của repo chủ. |
| 8 | `subtitles2notes/templates/lecture_notes_common_preamble.tex` | Nguồn header/layout PDF khóa học khổ thường dùng chung cho các sách được tạo. |
| 9 | `scripts/fix_course_pocket_overfulls.sh` | Lặp trên một biến thể khóa học: xuất, báo cáo, Codex vá, và xuất lại cho đến khi các overfull có thể xử lý giảm xuống. |
| 10 | `scripts/fix_latex_project_overfulls.sh` | Bộ sửa tràn LaTeX chung cho bất kỳ repo/dự án nào có thể dựng bằng `pdflatex` hoặc lệnh biên dịch tùy chỉnh. |
| 11 | `scripts/recheck_course_figures.py` | Kiểm tra lại các hình bài giảng giống ảnh chụp màn hình dựa trên ngữ cảnh bản chép lời và khung hình video thay thế. |
| 12 | `scripts/export_course_epubs.sh` | Dựng lại các đầu ra `course.tex` đã hoàn thiện trực tiếp thành EPUB3. |

## 🚀 Bắt đầu nhanh

Clone trực tiếp:

```bash
git clone git@github.com:lachlanchen/Video2Book.git
cd Video2Book
```

Hoặc thêm vào repo khác dưới dạng submodule:

```bash
git submodule add git@github.com:lachlanchen/Video2Book.git Video2Book
git submodule update --init --recursive
```

## 🏗️ Bố cục repo chủ

`Video2Book` kỳ vọng chạy từ một repo chủ lưu các đầu ra làm việc:

- `subtitles/`
- `markdown/`
- `generated_course_notes/`
- `.lecture-notes-work/`

Bản thân các tệp video thường được giữ bên ngoài repo chủ trong một workspace media như:

- `/home/lachlan/ProjectsLFS/YoutubeDownloader`

## 🛠️ Cách dùng điển hình

Từ root của repo chủ:

```bash
./Video2Book/scripts/download_susskind_playlist.sh
./Video2Book/scripts/start_transcription_tmux.sh
./Video2Book/scripts/start_transcription_monitor_tmux.sh
./Video2Book/scripts/start_course_notes_tmux.sh
./Video2Book/scripts/start_course_notes_monitor_tmux.sh
```

Chạy thử trình tải xuống:

```bash
./Video2Book/scripts/download_susskind_playlist.sh --dry-run
```

Khởi động hàng đợi viết ghi chú cho một khóa học:

```bash
./Video2Book/scripts/start_course_notes_tmux.sh --course supplementary/advanced_quantum_mechanics/2013_fall
```

Xuất PDF gọn cho tất cả khóa học đã hoàn tất (ví dụ trong `leonardsusskind`):

```bash
./Video2Book/scripts/export_course_pocket_pdfs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
```

Xuất một sách độc lập trong `investment_pdfs/` thành các biến thể khổ bỏ túi:

```bash
./Video2Book/scripts/export_tex_book_pocket_pdf.sh \
  --repo-root /home/lachlan/ProjectsLFS/LazyEarn \
  --project-root /home/lachlan/ProjectsLFS/LazyEarn/investment_pdfs/wealth-from-first-principles \
  --main-tex wealth-from-first-principles.tex \
  --font-mode onepointtwo \
  --suffix pocket_1_2x
```

Chạy bộ sửa tràn do Codex điều khiển cho một biến thể khóa học layout hẹp:

```bash
./Video2Book/scripts/start_pocket_overflow_fix_tmux.sh \
  --course core/statistical_mechanics/2013_spring_theoretical_minimum \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

Chạy hàng đợi trong tmux trên tất cả khóa học Susskind đã hoàn tất, mỗi lần một khóa:

```bash
./Video2Book/scripts/start_pocket_overflow_fix_tmux.sh \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

Chạy bộ sửa LaTeX chung trên bất kỳ dự án nào:

```bash
./Video2Book/scripts/fix_latex_project_overfulls.sh \
  --repo-root /path/to/repo \
  --project-root /path/to/repo/book \
  --main-tex main.tex \
  --model gpt-5.4 \
  --reasoning medium
```

Xuất EPUB3 trực tiếp từ TeX cho tất cả khóa học đã hoàn tất:

```bash
./Video2Book/scripts/export_course_epubs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
```

Các wrapper riêng cho từng repo chủ có thể đặt dưới `examples/`. Các mẫu hiện được đóng gói:

- `examples/lazyearn/yale-financial-markets/`
- `examples/lazylearn/how-you-speak-and-write/`
- `examples/leonardsusskind/susskind-physics-archive/`

## 🎬 Ví dụ mặc định hiện tại

Trình tải xuống đi kèm mặc định dùng playlist vật lý Leonard Susskind:

- <https://www.youtube.com/playlist?list=PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG>

Mặc định đó chỉ là một ví dụ đang hoạt động. Mã được cấu trúc để các repo chủ khác có thể điều chỉnh cùng quy trình này cho các kho bài giảng khác.

## 📦 Bản đồ mô-đun

- [playlist2videos](../playlist2videos)
- [videos2subtitles](../videos2subtitles)
- [subtitles2notes](../subtitles2notes)
- [scripts](../scripts)
- [Bàn giao xuất bỏ túi](../references/pocket-size-course-pdfs-handoff.md)
- [Bàn giao layout A4 và bỏ túi](../references/a4-and-pocket-pdf-layout-handoff.md)
- [Bàn giao xem trước sách trong README](../references/readme-book-preview-handoff.md)
- [Bàn giao bộ sửa tràn LaTeX](../references/latex-overflow-fixer-handoff.md)
- [Bàn giao xuất EPUB](../references/tex-to-epub-handoff.md)

## 📚 Ghi chú thích nghi repo chủ

- [references/lazylearn-course-adaptation.md](../references/lazylearn-course-adaptation.md)
- [references/lazyearn-yale-financial-markets-adaptation.md](../references/lazyearn-yale-financial-markets-adaptation.md)
- [references/nanobanana-2-book-cover-handoff.md](../references/nanobanana-2-book-cover-handoff.md)
- [references/readme-book-preview-handoff.md](../references/readme-book-preview-handoff.md)
- [references/a4-and-pocket-pdf-layout-handoff.md](../references/a4-and-pocket-pdf-layout-handoff.md)
- [references/latex-overflow-fixer-handoff.md](../references/latex-overflow-fixer-handoff.md)
- [references/tex-book-translation-workflow.md](../references/tex-book-translation-workflow.md)
- [references/tex-to-epub-handoff.md](../references/tex-to-epub-handoff.md)

## 🎨 Tiện ích bìa sách

`Video2Book` cũng bao gồm một trợ lý Nano Banana 2 cục bộ để tạo bìa sách biên tập:

- script: [scripts/book_cover_nanobanana.py](../scripts/book_cover_nanobanana.py)
- hướng dẫn: [references/nanobanana-2-book-cover-handoff.md](../references/nanobanana-2-book-cover-handoff.md)
- mẫu env: [.env.example](../.env.example)
- prompt ví dụ cho sách hiện tại: [examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt](../examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt)

Nó tái sử dụng cơ chế gửi-và-thăm-dò GRS AI từ công việc Nano Banana ở repo anh em, nhưng thay prompt phân đoạn bằng prompt bìa sách và lưu một vết đầu ra sạch cho mỗi lần chạy.

## 🌐 Tiện ích dịch sách

`Video2Book` cũng có thể dịch một sách ghi chú bài giảng đã hoàn thiện sang các thư mục
ngôn ngữ anh em như `zh/` và `jp/`, trong khi vẫn giữ nguyên cấu trúc TeX,
phương trình, và hình ảnh.

- trình quản lý: [scripts/translate_tex_book.py](../scripts/translate_tex_book.py)
- trình chạy vòng lặp: [scripts/process_book_translation_one_by_one.sh](../scripts/process_book_translation_one_by_one.sh)
- trình khởi động tmux: [scripts/start_book_translation_tmux.sh](../scripts/start_book_translation_tmux.sh)
- ghi chú quy trình: [references/tex-book-translation-workflow.md](../references/tex-book-translation-workflow.md)

Vòng lặp dịch:

- khởi tạo một ấn bản dịch sẵn sàng cho XeLaTeX
- dịch tệp sách chính trước, rồi đến từng chương
- hỗ trợ cả sách tách chương và sách `main.tex` một tệp với các khối `\chapter{...}` nội tuyến
- đặt tên tệp entry đã dịch bằng hậu tố ngôn ngữ như `book_zh.tex` hoặc `book_jp.tex`
- biên dịch lại sau mỗi đơn vị
- có thể commit và push thư mục đã dịch sau mỗi đơn vị hoàn tất

## ⚙️ Yêu cầu

- `tmux`
- `ffmpeg`
- `pdflatex`
- `pdfunite`
- `pdftotext`
- `yt-dlp`
- `pandoc` (cho `scripts/export_course_epubs.sh`)
- CLI `codex` cho quy trình ghi chú
- một env conda `whisper` hoạt động cho việc chép lời
- `whisper_with_lang_detect` nếu bạn muốn đường dẫn phụ đề chính thay vì Whisper chỉ dự phòng
- `rsync` (cho đồng bộ xuất bản cục bộ tùy chọn của PDF bỏ túi)

## 🤝 Phù hợp với

`Video2Book` phù hợp khi bạn muốn:

- một quy trình cục bộ trong repo thay vì một ứng dụng nguyên khối
- tạo ghi chú bài giảng bắt đầu từ bản chép lời
- tự động hóa tác vụ dài dựa trên tmux
- cấu trúc lưu trữ có thể tái lập cho tài liệu học tập

## 🙏 Hỗ trợ

| Quyên góp | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Giấy phép

Kho này được cấp phép theo GNU General Public License v3.0.
