اللغات: [English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![لافتة LazyingArt](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://lazying.art)

# Video2Book من LazyingArt LLC

> **Video2Book من LazyingArt LLC**. المواقع: [lazying.art](https://lazying.art) و [learn.lazying.art](https://learn.lazying.art).

[![LazyingArt](https://img.shields.io/badge/Website-lazying.art-111827?style=for-the-badge&logo=googlechrome&logoColor=white)](https://lazying.art)
[![Learn](https://img.shields.io/badge/Learn-learn.lazying.art-1f2937?style=for-the-badge&logo=bookstack&logoColor=white)](https://learn.lazying.art)

[![Toolkit](https://img.shields.io/badge/toolkit-video__to__book-111827?style=for-the-badge&logo=bookstack&logoColor=white)](#)
[![Downloader](https://img.shields.io/badge/stage_1-playlist2videos-1d4ed8?style=for-the-badge&logo=youtube&logoColor=white)](#-pipeline)
[![Transcription](https://img.shields.io/badge/stage_2-videos2subtitles-0f766e?style=for-the-badge&logo=openai&logoColor=white)](#-pipeline)
[![Notes](https://img.shields.io/badge/stage_3-subtitles2notes-f97316?style=for-the-badge&logo=latex&logoColor=white)](#-pipeline)
[![tmux](https://img.shields.io/badge/runtime-tmux-7c3aed?style=for-the-badge&logo=gnu-bash&logoColor=white)](#-quick-start)

`Video2Book` هو خط أنابيب عملي لتحويل مجموعات الفيديو الطويلة إلى مواد دراسة دائمة: وسائط محمّلة، ونصوص مفرغة ذات طوابع زمنية، وملاحظات محاضرات مشتقة من التفريغ مع ملفات PDF مجمعة.

## 📚 الكتب الرئيسية

تستخدم هذه المعاينات الصفحة الأولى المستخرجة من كل ملف PDF منشور من `LazyEarn`
و `LazyLearn`.

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/wealth-from-first-principles/wealth-from-first-principles.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/wealth-from-first-principles/cover-page-1.png" width="180" alt="غلاف Wealth from First Principles" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/dynamic_book/how-you-got-rich.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-rich/cover-page-1.png" width="180" alt="غلاف How You Got Rich" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/jim-rohn-originals-no-ai/course.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-successful/cover-page-1.png" width="180" alt="غلاف How You Got Successful" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/how-you-got-happiness-publication/how-you-got-happiness.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyEarn/main/docs/publications/how-you-got-happiness/cover-page-1.png" width="180" alt="غلاف How You Got Happiness" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/wealth-from-first-principles/wealth-from-first-principles.pdf"><strong>Wealth from First Principles</strong></a><br />
      المال، والملكية، والمطالبات، والتراكم المركب
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/dynamic_book/how-you-got-rich.pdf"><strong>How You Got Rich?</strong></a><br />
      كتاب ثروة غير خطي مبني من أدلة المقابلات
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/jim-rohn-originals-no-ai/course.pdf"><strong>How You Got Successful?</strong></a><br />
      محاضرات جيم رون عن النجاح معاد ترتيبها في قوس كتاب أكثر سلاسة
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyEarn/blob/main/how-you-got-happiness-publication/how-you-got-happiness.pdf"><strong>How You Got Happiness?</strong></a><br />
      أحاديث كريشنامورتي مصاغة في كتاب عن الانتباه، والخوف، والتأمل، والحرية
    </td>
  </tr>
</table>

ينشر `LazyLearn` أيضًا كتاب كتابة متعدد اللغات بالإضافة إلى كتاب مقرر مكتمل عن العدالة:

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write/cover-page-1.png" width="180" alt="غلاف How to Speak and Write English" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-zh.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write-zh/cover-page-1.png" width="180" alt="غلاف How to Speak and Write Traditional Chinese" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-jp.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/how-to-speak-and-write-jp/cover-page-1.png" width="180" alt="غلاف How to Speak and Write Japanese" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/LazyLearn/main/docs/publications/justice-with-michael-sandel/cover-page-1.png" width="180" alt="غلاف Justice with Michael Sandel" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write.pdf"><strong>How to Speak and Write</strong></a><br />
      طبعة إنجليزية معاد ترتيبها
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-zh.pdf"><strong>如何說話與寫作</strong></a><br />
      النسخة الصينية التقليدية
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/how-to-speak-and-write/how-to-speak-and-write-jp.pdf"><strong>話し方と書き方</strong></a><br />
      النسخة اليابانية
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf"><strong>Justice with Michael Sandel</strong></a><br />
      كتاب مقرر الفلسفة السياسية لمايكل ساندل
    </td>
  </tr>
</table>

ينشر `leonardsusskind` أيضًا كتب الفيزياء الأساسية Theoretical Minimum:

<table width="100%">
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/quantum_mechanics_theoretical_minimum.png" width="180" alt="غلاف Quantum Mechanics Theoretical Minimum" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/general_relativity_theoretical_minimum.png" width="180" alt="غلاف General Relativity Theoretical Minimum" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/statistical_mechanics_theoretical_minimum_first_page.png" width="180" alt="غلاف Statistical Mechanics Theoretical Minimum" />
      </a>
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf">
        <img src="https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/figs/readme-covers/cosmology_theoretical_minimum_first_page.png" width="180" alt="غلاف Cosmology Theoretical Minimum" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf"><strong>Quantum Mechanics</strong></a><br />
      كتاب أساسي من Theoretical Minimum
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf"><strong>General Relativity</strong></a><br />
      كتاب أساسي من Theoretical Minimum
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf"><strong>Statistical Mechanics</strong></a><br />
      كتاب أساسي من Theoretical Minimum
    </td>
    <td align="center" width="25%" valign="top">
      <a href="https://github.com/lachlanchen/leonardsusskind/blob/main/core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf"><strong>Cosmology</strong></a><br />
      كتاب أساسي من Theoretical Minimum
    </td>
  </tr>
</table>

## ✨ ما الذي يغطيه

- تنزيل قائمة تشغيل إلى أرشيف وسائط خارجي ثابت.
- تفريغ الفيديوهات إلى ترجمات `.srt` وMarkdown بطوابع زمنية.
- تحويل مجموعات التفريغ المكتملة إلى ملاحظات TeX منظمة وملفات PDF مدمجة للمقرر.
- تحويل مجلدات مواد Markdown المرتبة إلى كتب TeX/PDF بحجم الجيب.
- تشغيل المهام الطويلة في `tmux` باستخدام سكربتات الطوابير وسكربتات المراقبة/الحراسة.
- تصدير ملفات PDF مرافقة مدمجة بتنسيق الجيب من LaTeX المقرر المكتمل.
- إعادة استخدام سير عمل الرؤوس الملتفة وتحديث الأشكال نفسه لكل من ملفات PDF العادية
  كاملة الحجم وملفات PDF الجيب عبر مستودعات المضيف.

## 🧪 مستودعات مضيفة عاملة

يُستخدم `Video2Book` بالفعل في عدة مستودعات مضيفة بأشكال أرشفة مختلفة.

| مستودع المضيف | التركيز | مثال الغلاف | المخرجات المتتبعة الحالية |
| --- | --- | --- | --- |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | مقرر Yale `Financial Markets` مع Robert J. Shiller | [examples/lazyearn/yale-financial-markets/](../examples/lazyearn/yale-financial-markets/) | [PDF المقرر](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf)، [ملفات PDF للمحاضرات](https://github.com/lachlanchen/LazyEarn/tree/main/generated_course_notes/lazyearn/yale-financial-markets/chapters)، [تفريغات markdown](https://github.com/lachlanchen/LazyEarn/tree/main/markdown/lazyearn/yale-financial-markets)، [الترجمات](https://github.com/lachlanchen/LazyEarn/tree/main/subtitles/lazyearn/yale-financial-markets) |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | تكييف مقرر كتابة لـ `How You Speak and Write` | [examples/lazylearn/how-you-speak-and-write/](../examples/lazylearn/how-you-speak-and-write/)، [examples/lazylearn/justice-with-michael-sandel/](../examples/lazylearn/justice-with-michael-sandel/) | [ملف PDF لمقرر How You Speak and Write](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf)، [ملف PDF لمقرر Justice with Michael Sandel](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/justice-with-michael-sandel/course.pdf)، [ملفات PDF لمقرر المتحدث المحلي](https://github.com/lachlanchen/LazyLearn/tree/main/how-to-speak-and-write)، [ملف PDF المحلي للعدالة](https://github.com/lachlanchen/LazyLearn/blob/main/justice-with-michael-sandel/justice-with-michael-sandel.pdf)، [ملفات PDF للمحاضرات](https://github.com/lachlanchen/LazyLearn/tree/main/generated_course_notes/lazylearn/how-you-speak-and-write/chapters)، [تفريغات markdown](https://github.com/lachlanchen/LazyLearn/tree/main/markdown/lazylearn)، [الترجمات](https://github.com/lachlanchen/LazyLearn/tree/main/subtitles/lazylearn) |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | أرشيف محاضرات Leonard Susskind الكامل، وخط أنابيب التفريغ، وكتب الملاحظات المنشورة | [examples/leonardsusskind/susskind-physics-archive/](../examples/leonardsusskind/susskind-physics-archive/) | [مجلد الكتب المنشورة](https://github.com/lachlanchen/leonardsusskind/tree/main)، [PDF الكم المتقدم](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf)، [PDF موضوعات في نظرية الأوتار](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf)، [PDF فيزياء الجسيمات 3](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_particle_physics_3/particle_physics_3_supersymmetry_and_grand_unification.pdf)، [تفريغات markdown](https://github.com/lachlanchen/leonardsusskind/tree/main/markdown)، [الترجمات](https://github.com/lachlanchen/leonardsusskind/tree/main/subtitles) |

## 📘 الكتب وملفات PDF

تنتج المرحلة الثالثة بالفعل مخرجات حقيقية شبيهة بالكتب في مستودعات المضيف:

- كتب مقررات مدمجة مثل `course.pdf` أو اسم قانوني منشور من المضيف
- ملفات PDF لكل محاضرة تحت `generated_course_notes/.../chapters/`
- أشجار التفريغ في `markdown/` وأشجار الترجمة في `subtitles/`

كتب منشورة ومخرجات مقررات أخرى:

| مستودع المضيف | العنوان | ملف PDF الرئيسي | ملاحظات |
| --- | --- | --- | --- |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Yale Financial Markets | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/yale-financial-markets/course.pdf) | كتاب محاضرات Robert J. Shiller مع نسخ كاملة الحجم ونسخ جيب |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Hard Knocks Interviews | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/generated_course_notes/lazyearn/school-of-hard-knocks/hard-knocks-interviews/course.pdf) | تجميع مباشر محاضرة بمحاضرة |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | High-Growth Dossier | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/high-growth-stocks/high-growth-stocks.pdf) | كتاب بحثي قديم مع تصديرات جيب |
| [LazyEarn](https://github.com/lachlanchen/LazyEarn) | Quod Tango Muto | [PDF](https://github.com/lachlanchen/LazyEarn/blob/main/investment_pdfs/quod-tango-muto/quod-tango-muto.pdf) | كتاب بحثي بشعار لاتيني مع تصديرات جيب |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | How You Speak and Write | [PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/how-you-speak-and-write/course.pdf) | تكييف مقرر كتابة |
| [LazyLearn](https://github.com/lachlanchen/LazyLearn) | Justice with Michael Sandel | [PDF](https://github.com/lachlanchen/LazyLearn/blob/main/generated_course_notes/lazylearn/justice-with-michael-sandel/course.pdf) | كتاب مقرر فلسفة سياسية |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Classical Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/classical_mechanics_theoretical_minimum.pdf) | كتاب موحد في `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Quantum Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/quantum_mechanics_theoretical_minimum.pdf) | كتاب TTM أساسي في `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Special Relativity (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/special_relativity_theoretical_minimum.pdf) | كتاب TTM أساسي في `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | General Relativity (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/general_relativity_theoretical_minimum.pdf) | كتاب TTM أساسي في `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Statistical Mechanics (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/statistical_mechanics_theoretical_minimum.pdf) | كتاب TTM أساسي في `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Cosmology (Theoretical Minimum) | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/all_notes/cosmology_theoretical_minimum.pdf) | كتاب TTM أساسي في `all_notes/` |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Advanced Quantum Mechanics | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_advanced_quantum/advanced_quantum_mechanics.pdf) | عنوان فيزياء تكميلي |
| [leonardsusskind](https://github.com/lachlanchen/leonardsusskind) | Topics in String Theory | [PDF](https://github.com/lachlanchen/leonardsusskind/blob/main/supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf) | عنوان تكميلي في علم الكونيات / الأوتار |

تتوفر عناوين Susskind الموحدة الأخرى في [all_notes](https://github.com/lachlanchen/leonardsusskind/tree/main/all_notes).

### مؤشرات المستودعات الشقيقة المحلية

إذا كنت تشغل هذه المستودعات من دليل أصل مشترك (مثل `/home/lachlan/ProjectsLFS`)، فيمكن الوصول إلى الكتب نفسها أيضًا عبر مسارات محلية:

- `../LazyLearn/justice-with-michael-sandel/justice-with-michael-sandel.pdf`
- `../LazyLearn/how-to-speak-and-write/how-to-speak-and-write.pdf`
- `../LazyEarn/generated_course_notes/lazyearn/yale-financial-markets/course.pdf`
- `../leonardsusskind/<sibling-folder>/...` (ملفات PDF للمقررات والكتب المنشورة في ذلك المستودع)

## 🧩 خط الأنابيب

| المرحلة | الوحدة | الغرض |
| --- | --- | --- |
| 1 | `playlist2videos/` | تنزيل قائمة تشغيل أو تحديثها باستخدام `yt-dlp`، والاحتفاظ بالسجلات، وتجاوز العناصر المؤرشفة سابقًا. |
| 2 | `videos2subtitles/` | تفريغ الوسائط المؤرشفة إلى `subtitles/` و `markdown/`. |
| 3 | `subtitles2notes/` | تحويل التفريغات المكتملة إلى فصول TeX، وملفات PDF للمحاضرات، وملفات PDF مدمجة للمقرر. |
| 4 | `scripts/process_markdown_material_book.py` | تحويل مجلدات Markdown المصدر المرتبة إلى كتب TeX/PDF منشأة بحجم الجيب مع تمرير الصور ذات الصلة إلى Codex. |
| 5 | `scripts/start_markdown_material_book_tmux.sh` | تشغيل كاتب كتاب مواد Markdown في `tmux`، مع معالجة مصدر واحد في كل مرة بطريقة آمنة للاستئناف. |
| 6 | `scripts/export_course_pocket_pdfs.sh` | إعادة بناء مخرجات `course.tex` المكتملة إلى نسخ جيب/A5 لحزم النشر وإصدار تقارير overfull معيّنة. |
| 7 | `scripts/export_tex_book_pocket_pdf.sh` | إعادة بناء كتاب/مقال TeX مستقل واحد إلى ملف PDF مرافق بحجم الجيب ومزامنته إلى شجرة docs في مستودع المضيف. |
| 8 | `subtitles2notes/templates/lecture_notes_common_preamble.tex` | مصدر الرأس/التخطيط المشترك لملفات PDF للمقررات بالحجم العادي المستخدم في الكتب المنشأة. |
| 9 | `scripts/fix_course_pocket_overfulls.sh` | التكرار على نسخة مقرر واحدة: تصدير، تقرير، تصحيح Codex، وإعادة تصدير حتى تنخفض حالات overfull القابلة للتنفيذ. |
| 10 | `scripts/fix_latex_project_overfulls.sh` | مصحح عام لتجاوزات LaTeX لأي مستودع/مشروع يمكن بناؤه باستخدام `pdflatex` أو أمر تجميع مخصص. |
| 11 | `scripts/recheck_course_figures.py` | إعادة تدقيق الأشكال الشبيهة بلقطات الشاشة للمحاضرات مقابل سياق التفريغ وإطارات الفيديو البديلة. |
| 12 | `scripts/export_course_epubs.sh` | إعادة بناء مخرجات `course.tex` المكتملة مباشرة إلى EPUB3. |

## 🚀 البدء السريع

انسخه مباشرة:

```bash
git clone git@github.com:lachlanchen/Video2Book.git
cd Video2Book
```

أو أضفه إلى مستودع آخر كوحدة فرعية:

```bash
git submodule add git@github.com:lachlanchen/Video2Book.git Video2Book
git submodule update --init --recursive
```

## 🏗️ تخطيط مستودع المضيف

يتوقع `Video2Book` أن يعمل من مستودع مضيف يخزن المخرجات العاملة:

- `subtitles/`
- `markdown/`
- `generated_course_notes/`
- `.lecture-notes-work/`

تُحفظ ملفات الفيديو نفسها عادة خارج مستودع المضيف في مساحة عمل وسائط مثل:

- `/home/lachlan/ProjectsLFS/YoutubeDownloader`

## 🛠️ الاستخدام النموذجي

من جذر مستودع المضيف:

```bash
./Video2Book/scripts/download_susskind_playlist.sh
./Video2Book/scripts/start_transcription_tmux.sh
./Video2Book/scripts/start_transcription_monitor_tmux.sh
./Video2Book/scripts/start_course_notes_tmux.sh
./Video2Book/scripts/start_course_notes_monitor_tmux.sh
```

تشغيل تجريبي للمنزّل:

```bash
./Video2Book/scripts/download_susskind_playlist.sh --dry-run
```

ابدأ طابور كتابة ملاحظات لمقرر واحد:

```bash
./Video2Book/scripts/start_course_notes_tmux.sh --course supplementary/advanced_quantum_mechanics/2013_fall
```

صدّر ملفات PDF مدمجة لكل المقررات المكتملة (مثلًا في `leonardsusskind`):

```bash
./Video2Book/scripts/export_course_pocket_pdfs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
```

صدّر كتابًا مستقلًا واحدًا في `investment_pdfs/` إلى نسخ بحجم الجيب:

```bash
./Video2Book/scripts/export_tex_book_pocket_pdf.sh \
  --repo-root /home/lachlan/ProjectsLFS/LazyEarn \
  --project-root /home/lachlan/ProjectsLFS/LazyEarn/investment_pdfs/wealth-from-first-principles \
  --main-tex wealth-from-first-principles.tex \
  --font-mode onepointtwo \
  --suffix pocket_1_2x
```

شغّل مصحح التجاوزات المدفوع بـ Codex لنسخة مقرر ذات تخطيط ضيق:

```bash
./Video2Book/scripts/start_pocket_overflow_fix_tmux.sh \
  --course core/statistical_mechanics/2013_spring_theoretical_minimum \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

شغّل الطابور في tmux عبر كل مقررات Susskind المكتملة، مقرر واحد في كل مرة:

```bash
./Video2Book/scripts/start_pocket_overflow_fix_tmux.sh \
  --font-mode onepointtwo \
  --model gpt-5.4 \
  --reasoning medium
```

شغّل مصحح LaTeX العام على أي مشروع:

```bash
./Video2Book/scripts/fix_latex_project_overfulls.sh \
  --repo-root /path/to/repo \
  --project-root /path/to/repo/book \
  --main-tex main.tex \
  --model gpt-5.4 \
  --reasoning medium
```

صدّر EPUB3 مباشرة من TeX لكل المقررات المكتملة:

```bash
./Video2Book/scripts/export_course_epubs.sh --host-root /home/lachlan/ProjectsLFS/leonardsusskind
```

يمكن أن تعيش الأغلفة الخاصة بالمضيف تحت `examples/`. الأنماط المضمّنة الحالية:

- `examples/lazyearn/yale-financial-markets/`
- `examples/lazylearn/how-you-speak-and-write/`
- `examples/leonardsusskind/susskind-physics-archive/`

## 🎬 المثال الافتراضي الحالي

يضبط المنزّل المضمّن افتراضيًا قائمة تشغيل الفيزياء لـ Leonard Susskind:

- <https://www.youtube.com/playlist?list=PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG>

هذا الإعداد الافتراضي مجرد مثال عامل. بُنيت الشيفرة بحيث تستطيع مستودعات مضيفة أخرى تكييف خط الأنابيب نفسه مع أرشيفات محاضرات مختلفة.

## 📦 خريطة الوحدات

- [playlist2videos](../playlist2videos)
- [videos2subtitles](../videos2subtitles)
- [subtitles2notes](../subtitles2notes)
- [scripts](../scripts)
- [تسليم تصدير الجيب](../references/pocket-size-course-pdfs-handoff.md)
- [تسليم تخطيط A4 والجيب](../references/a4-and-pocket-pdf-layout-handoff.md)
- [تسليم معاينة كتاب README](../references/readme-book-preview-handoff.md)
- [تسليم مصحح تجاوزات LaTeX](../references/latex-overflow-fixer-handoff.md)
- [تسليم تصدير EPUB](../references/tex-to-epub-handoff.md)

## 📚 ملاحظات تكييف المضيف

- [references/lazylearn-course-adaptation.md](../references/lazylearn-course-adaptation.md)
- [references/lazyearn-yale-financial-markets-adaptation.md](../references/lazyearn-yale-financial-markets-adaptation.md)
- [references/nanobanana-2-book-cover-handoff.md](../references/nanobanana-2-book-cover-handoff.md)
- [references/readme-book-preview-handoff.md](../references/readme-book-preview-handoff.md)
- [references/a4-and-pocket-pdf-layout-handoff.md](../references/a4-and-pocket-pdf-layout-handoff.md)
- [references/latex-overflow-fixer-handoff.md](../references/latex-overflow-fixer-handoff.md)
- [references/tex-book-translation-workflow.md](../references/tex-book-translation-workflow.md)
- [references/tex-to-epub-handoff.md](../references/tex-to-epub-handoff.md)

## 🎨 أداة أغلفة الكتب

يتضمن `Video2Book` أيضًا مساعد Nano Banana 2 محليًا لإنشاء أغلفة كتب تحريرية:

- السكربت: [scripts/book_cover_nanobanana.py](../scripts/book_cover_nanobanana.py)
- الدليل: [references/nanobanana-2-book-cover-handoff.md](../references/nanobanana-2-book-cover-handoff.md)
- قالب البيئة: [.env.example](../.env.example)
- مثال مطالبة الكتاب الحالي: [examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt](../examples/lazylearn/how-you-speak-and-write/book_cover_prompt.txt)

يعيد استخدام آليات الإرسال والاستطلاع الخاصة بـ GRS AI من عمل Nano Banana الشقيق، لكنه يستبدل مطالبات التقسيم بمطالبة غلاف كتاب ويحفظ أثر مخرجات نظيفًا لكل تشغيل.

## 🌐 أداة ترجمة الكتب

يمكن لـ `Video2Book` أيضًا ترجمة كتاب ملاحظات محاضرات مكتمل إلى مجلدات لغات شقيقة
مثل `zh/` و `jp/`، مع الحفاظ على بنية TeX،
والمعادلات، والصور سليمة.

- المدير: [scripts/translate_tex_book.py](../scripts/translate_tex_book.py)
- مشغل الحلقة: [scripts/process_book_translation_one_by_one.sh](../scripts/process_book_translation_one_by_one.sh)
- بادئ tmux: [scripts/start_book_translation_tmux.sh](../scripts/start_book_translation_tmux.sh)
- ملاحظة سير العمل: [references/tex-book-translation-workflow.md](../references/tex-book-translation-workflow.md)

حلقة الترجمة:

- تهيئ طبعة مترجمة جاهزة لـ XeLaTeX
- تترجم ملف الكتاب الرئيسي أولًا، ثم كل فصل
- تدعم كلًا من الكتب ذات الفصول المنفصلة وكتب `main.tex` ذات الملف الواحد مع كتل `\chapter{...}` المضمنة
- تسمي ملفات الدخول المترجمة بلاحقة لغة مثل `book_zh.tex` أو `book_jp.tex`
- تعيد التجميع بعد كل وحدة
- يمكنها تنفيذ commit وpush للمجلد المترجم بعد كل وحدة مكتملة

## ⚙️ المتطلبات

- `tmux`
- `ffmpeg`
- `pdflatex`
- `pdfunite`
- `pdftotext`
- `yt-dlp`
- `pandoc` (من أجل `scripts/export_course_epubs.sh`)
- واجهة سطر أوامر `codex` لخط أنابيب الملاحظات
- بيئة conda عاملة لـ `whisper` للتفريغ
- `whisper_with_lang_detect` إذا كنت تريد مسار الترجمة الأساسي بدل Whisper الاحتياطي فقط
- `rsync` (للمزامنة الاختيارية للنشر المحلي لملفات PDF الجيب)

## 🤝 مناسب لـ

`Video2Book` مناسب عندما تريد:

- خط أنابيب محليًا في المستودع بدل تطبيق أحادي ضخم
- توليد ملاحظات محاضرات يبدأ من التفريغ
- أتمتة طويلة التشغيل قائمة على tmux
- بنية أرشيف قابلة لإعادة الإنتاج لمواد الدراسة

## 🙏 الدعم

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## الترخيص

هذا المستودع مرخّص بموجب رخصة GNU العامة الإصدار 3.0.