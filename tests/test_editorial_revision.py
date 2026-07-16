import json
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_ROOT / "subtitles2notes"))

import editorial_revision as revision  # noqa: E402


class EditorialRevisionTests(unittest.TestCase):
    def test_parse_json_text_accepts_fenced_output(self):
        parsed = revision.parse_json_text("```json\n{\"status\": \"pass\"}\n```\n")
        self.assertEqual(parsed, {"status": "pass"})

    def test_scan_flags_process_leaks_but_not_normal_physics(self):
        text = (
            "The notes should mention Video2Book as board evidence.\n"
            "The Hamiltonian generates time translation.\n"
        )
        findings = revision.scan_text(Path("content.tex"), text)
        rules = {item["rule"] for item in findings}
        self.assertIn("editorial_directive", rules)
        self.assertIn("body_credit", rules)
        self.assertIn("production_language", rules)
        self.assertNotIn("internal_tooling", rules)

    def test_preamble_update_is_idempotent(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "common_preamble.tex"
            path.write_text("\\usepackage{amsmath}\n", encoding="utf-8")
            self.assertTrue(revision.ensure_editorial_preamble(path))
            self.assertFalse(revision.ensure_editorial_preamble(path))
            text = path.read_text(encoding="utf-8")
            self.assertEqual(text.count("newenvironment{classroomqa}"), 1)

    def test_course_front_matter_removes_duplicate_maketitle(self):
        source = r"""\documentclass{book}
\begin{document}
\frontmatter
\begin{titlepage}
Leonard Susskind lecture notes
\end{titlepage}
\hypersetup{pageanchor=true}
\title{Cosmology}
\author{Leonard Susskind}
\date{Transcript-derived notes}
\maketitle
\begin{center}
Old duplicate credit
\end{center}
\clearpage
\tableofcontents
\mainmatter
\end{document}
"""
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "course.tex"
            path.write_text(source, encoding="utf-8")
            self.assertTrue(revision.normalize_course_front_matter(path))
            updated = path.read_text(encoding="utf-8")
            self.assertNotIn("\\maketitle", updated)
            self.assertNotIn("\\author{Leonard Susskind}", updated)
            self.assertIn("\\chapter*{About These Notes}", updated)
            self.assertIn("Lectures by Leonard Susskind", updated)
            self.assertEqual(updated.count("\\tableofcontents"), 1)

    def test_course_cover_credit_replacement_does_not_leave_nested_brace_tail(self):
        source = r"""\frontmatter
\begin{titlepage}
{\small\color{black!72} Original lectures by Leonard Susskind. Transcript-derived course notes curated by \href{https://lazying.art}{LazyingArt LLC} with \href{https://github.com/lachlanchen/Video2Book}{Video2Book}.}
\end{titlepage}
\hypersetup{pageanchor=true}
\title{Course}
\author{Leonard Susskind}
\maketitle
\tableofcontents
"""
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "course.tex"
            path.write_text(source, encoding="utf-8")
            revision.normalize_course_front_matter(path)
            updated = path.read_text(encoding="utf-8")
            self.assertIn("Companion edition by", updated)
            self.assertNotIn("{Video2Book}}{LazyingArt LLC}", updated)

    def test_legacy_asset_metadata_is_normalized(self):
        with tempfile.TemporaryDirectory() as temp:
            course_root = Path(temp)
            figures = course_root / "figures"
            figures.mkdir()
            (figures / "frame.png").write_bytes(b"png")
            records, paths = revision.normalized_assets(
                {"assets": ["frame.png"]},
                course_root,
                "\\includegraphics{frame.png}",
            )
            self.assertEqual(records, [{"name": "frame.png"}])
            self.assertEqual(paths, [figures / "frame.png"])

    def test_load_chapter_repairs_missing_metadata_in_memory(self):
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            output_root = repo / "generated_course_notes"
            markdown_root = repo / "markdown"
            course_rel = "core/cosmology/example"
            chapter = output_root / course_rel / "chapters" / "lecture_01"
            transcript_dir = markdown_root / course_rel
            chapter.mkdir(parents=True)
            transcript_dir.mkdir(parents=True)
            (chapter / "content.tex").write_text("\\chapter{Expansion}\nText.\n", encoding="utf-8")
            transcript = transcript_dir / "001 - Cosmology Lecture 1.md"
            transcript.write_text(
                "# Transcript\n\nSource: core/cosmology/example/lecture1.mkv\n",
                encoding="utf-8",
            )
            record = revision.load_chapter(
                repo, markdown_root, output_root, course_rel, chapter
            )
            self.assertEqual(record.metadata["schema_version"], 2)
            self.assertEqual(record.metadata["lecture_number"], 1)
            self.assertEqual(record.video_rel, "core/cosmology/example/lecture1.mkv")
            self.assertFalse(record.metadata_path.exists())

    def test_corpus_scan_reports_duplicate_titles(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "generated_course_notes"
            for course in ("core/a/run", "core/b/run"):
                chapter = output / course / "chapters" / "lecture_01"
                chapter.mkdir(parents=True)
                (chapter / "content.tex").write_text(
                    "\\chapter{The Theoretical Minimum}\nPhysics.\n", encoding="utf-8"
                )
            report = revision.corpus_scan(output)
            self.assertEqual(report["chapters_scanned"], 2)
            self.assertEqual(len(report["duplicate_chapter_titles"]["The Theoretical Minimum"]), 2)

    def test_fidelity_gate_requires_source_map_and_verified_qa(self):
        with tempfile.TemporaryDirectory() as temp:
            candidate = Path(temp) / "content.tex"
            candidate.write_text(
                "\\chapter{Spin}\n"
                "\\begin{classroomqa}\\audiencequestion{Why?}"
                "\\lecturerresponse{Symmetry.}\\end{classroomqa}\n",
                encoding="utf-8",
            )
            report = {
                "status": "pass",
                "unsupported_claims": [],
                "missing_beats": [],
                "style_violations": [],
                "provenance_gaps": [],
                "q_and_a_checks": [],
                "figure_checks": [],
                "source_map": [],
            }
            passed, problems = revision.fidelity_passes(candidate, report)
            self.assertFalse(passed)
            self.assertTrue(any("source_map" in problem for problem in problems))
            self.assertTrue(any("Q&A" in problem for problem in problems))

    def test_formulaic_lecture_choreography_blocks_acceptance(self):
        with tempfile.TemporaryDirectory() as temp:
            candidate = Path(temp) / "content.tex"
            candidate.write_text(
                "\\chapter{Expansion}\nThe lecture begins with geometry.\n",
                encoding="utf-8",
            )
            passed, findings = revision.hard_scan_passes(candidate)
            self.assertFalse(passed)
            self.assertTrue(any(item["rule"] == "formulaic_choreography" for item in findings))

    def test_verified_qa_is_promoted_into_source_map(self):
        record = type(
            "Record",
            (),
            {"transcript_rel": "markdown/course/lecture.md"},
        )()
        report = {
            "source_map": [],
            "q_and_a_checks": [
                {
                    "locator": "Why is the sky dark?",
                    "timestamp": "00:12:34",
                    "verified": True,
                    "reason": "The audience question and response are both present.",
                }
            ],
        }
        revision.complete_verified_qa_source_map(record, report)
        self.assertEqual(report["source_map"][0]["timestamps"], ["00:12:34"])
        self.assertEqual(report["source_map"][0]["source_type"], "transcript")

    def test_prepare_environment_forces_read_only_writer(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            args = type(
                "Args",
                (),
                {
                    "repo_root": root,
                    "markdown_root": None,
                    "output_root": None,
                    "runtime_root": None,
                    "session_file": None,
                    "session_doc": None,
                },
            )()
            revision.prepare_environment(args)
            self.assertEqual(revision.os.environ["CODEX_PROMPT_ACCESS"], "read-only")


if __name__ == "__main__":
    unittest.main()
