import sys
import tempfile
import unittest
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_ROOT / "subtitles2notes"))

import generate_course_notes as generator  # noqa: E402


class GenerateCourseNotesNumberingTests(unittest.TestCase):
    def test_combined_lecture_numbers_create_range_slug(self):
        stem = "058 - Lectures 2 & 3 | Quantum Entanglement"
        numbers = generator.parse_explicit_lecture_numbers(stem)
        self.assertEqual(numbers, (2, 3))
        self.assertEqual(generator.lecture_slug_from_numbers(numbers, stem), "lecture_02_03")

    def test_single_unnumbered_transcript_is_lecture_one(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            markdown_root = root / "markdown"
            course = Path("supplementary/higgs/2012")
            transcript_dir = markdown_root / course
            transcript_dir.mkdir(parents=True)
            transcript = transcript_dir / "144 - Demystifying the Higgs Boson.md"
            transcript.write_text(
                "# Transcript\n\nSource: supplementary/higgs/2012/higgs.webm\n",
                encoding="utf-8",
            )
            lecture = generator.lecture_from_transcript_rel(
                repo_root=root,
                source_root=root / "videos",
                markdown_root=markdown_root,
                subtitle_root=root / "subtitles",
                transcript_rel=str(transcript.relative_to(markdown_root)),
                course_config=generator.CourseConfig(),
                resolve_video=False,
            )
            self.assertEqual(lecture.lecture_number, 1)
            self.assertEqual(lecture.lecture_numbers, (1,))
            self.assertEqual(lecture.lecture_slug, "lecture_01")


if __name__ == "__main__":
    unittest.main()
