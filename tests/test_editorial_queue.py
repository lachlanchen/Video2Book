import json
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_ROOT / "subtitles2notes"))

import editorial_queue as queue  # noqa: E402


class EditorialQueueTests(unittest.TestCase):
    def build_repo(self, root: Path) -> Path:
        course_rel = "supplementary/example/2026"
        course_root = root / "generated_course_notes" / course_rel
        chapter = course_root / "chapters" / "lecture_01"
        transcript = root / "markdown" / course_rel / "001 - Lecture 1.md"
        video = root / "susskind_lecture_videos" / course_rel / "lecture_1.mp4"
        chapter.mkdir(parents=True)
        transcript.parent.mkdir(parents=True)
        video.parent.mkdir(parents=True)
        (chapter / "content.tex").write_text("\\chapter{Example}\n", encoding="utf-8")
        transcript.write_text(
            f"# Transcript\n\nSource: {course_rel}/lecture_1.mp4\n",
            encoding="utf-8",
        )
        video.write_bytes(b"video")
        (chapter / "metadata.json").write_text(
            json.dumps(
                {
                    "course_rel": course_rel,
                    "transcript_rel": f"{course_rel}/001 - Lecture 1.md",
                    "video_rel": f"{course_rel}/lecture_1.mp4",
                    "lecture_number": 1,
                    "lecture_numbers": [1],
                    "lecture_slug": "lecture_01",
                    "lecture_title": "Example",
                    "assets": [],
                }
            ),
            encoding="utf-8",
        )
        (course_root / "course.tex").write_text(
            "\\input{chapters/lecture_01/content.tex}\n", encoding="utf-8"
        )
        manifest = root / "queue.json"
        manifest.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "expected_courses": 1,
                    "expected_chapters": 1,
                    "model": "gpt-5.6-sol",
                    "reasoning": "ultra",
                    "courses": [
                        {
                            "course": course_rel,
                            "expected_chapters": 1,
                            "references": [],
                            "chapter_references": {"lecture_01": []},
                            "publish": False,
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )
        return manifest

    def test_manifest_inventory_accepts_ultra_and_expected_counts(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = self.build_repo(root)
            config = queue.load_manifest(root, manifest)
            inventory, problems = queue.validate_inventory(config)
            self.assertEqual(config.model, "gpt-5.6-sol")
            self.assertEqual(config.reasoning, "ultra")
            self.assertEqual(config.prompt_access, "read-only")
            self.assertEqual(config.courses[0].chapter_references, {"lecture_01": ()})
            self.assertEqual(inventory["supplementary/example/2026"], ["lecture_01"])
            self.assertEqual(problems, [])

    def test_manifest_rejects_generated_note_reference(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = self.build_repo(root)
            generated_reference = root / "generated_course_notes" / "reference.pdf"
            generated_reference.write_bytes(b"pdf")
            payload = json.loads(manifest.read_text(encoding="utf-8"))
            payload["courses"][0]["references"] = [str(generated_reference)]
            manifest.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "generated notes cannot be references"):
                queue.load_manifest(root, manifest)

    def test_layout_repair_uses_requested_model_and_ultra_reasoning(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = self.build_repo(root)
            config = queue.load_manifest(root, manifest)
            command = queue.layout_fix_command(config, config.courses[0], "onepointtwo")
            self.assertIn("gpt-5.6-sol", command)
            self.assertIn("ultra", command)
            self.assertIn("--skip-commit", command)

    def test_revision_command_passes_editable_prompt_access(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = self.build_repo(root)
            config = queue.load_manifest(root, manifest)
            config = queue.QueueConfig(
                **{**config.__dict__, "prompt_access": "workspace-write"}
            )
            command = queue.revision_command(
                config, config.courses[0], "lecture_01", False, 2
            )
            access_index = command.index("--prompt-access")
            self.assertEqual(command[access_index + 1], "workspace-write")


if __name__ == "__main__":
    unittest.main()
