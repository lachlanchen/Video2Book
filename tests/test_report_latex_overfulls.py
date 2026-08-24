import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parents[1]


class LatexOverflowReportTests(unittest.TestCase):
    def test_report_includes_underfull_source_location_and_excerpt(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "chapter.tex"
            source.write_text(
                "\n".join(f"line {number}" for number in range(1, 12)) + "\n",
                encoding="utf-8",
            )
            log = root / "pdflatex.log"
            log.write_text(
                "(./chapter.tex\n"
                "Underfull \\hbox (badness 1234) in paragraph at lines 7--9\n"
                ")\n",
                encoding="utf-8",
            )
            report = root / "report.md"

            result = subprocess.run(
                [
                    sys.executable,
                    str(MODULE_ROOT / "scripts" / "report_latex_overfulls.py"),
                    "--log",
                    str(log),
                    "--compile-root",
                    str(root),
                    "--display-root",
                    str(root),
                    "--output",
                    str(report),
                ],
                check=True,
                capture_output=True,
                text=True,
            )

            self.assertIn("underfulls=1", result.stdout)
            rendered = report.read_text(encoding="utf-8")
            self.assertIn("## Underfull Paragraph Warnings", rendered)
            self.assertIn(f"{source}:7-9", rendered)
            self.assertIn("Badness: `1234`", rendered)
            self.assertIn("line 6", rendered)


if __name__ == "__main__":
    unittest.main()
