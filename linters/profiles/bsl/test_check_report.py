"""Contract checks for the CI gate; no 1C platform or Java runtime required."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class ReportGateTests(unittest.TestCase):
    def run_gate(self, text: str | None) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as directory:
            report = Path(directory) / "bsl-json.json"
            if text is not None:
                report.write_text(text, encoding="utf-8")
            return subprocess.run(
                [
                    sys.executable,
                    str(Path(__file__).with_name("check_report.py")),
                    str(report),
                ],
                capture_output=True,
                text=True,
                check=False,
            )

    def test_analyzed_file_without_diagnostics_passes(self) -> None:
        result = self.run_gate(
            json.dumps({"fileinfos": [{"path": "Module.bsl", "diagnostics": []}]})
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_every_severity_is_blocking(self) -> None:
        for severity in ("Error", "Warning", "Information", "Hint"):
            with self.subTest(severity=severity):
                report = {
                    "fileinfos": [
                        {
                            "path": "Module.bsl",
                            "diagnostics": [
                                {"severity": severity, "message": "Example diagnostic"}
                            ],
                        }
                    ]
                }
                result = self.run_gate(json.dumps(report))
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertIn("Example diagnostic", result.stdout)

    def test_missing_or_invalid_report_fails_closed(self) -> None:
        for text in (None, "", "{", "null", "[]", "{}", '{"fileinfos": []}'):
            with self.subTest(text=text):
                self.assertEqual(self.run_gate(text).returncode, 2)

    def test_malformed_file_or_diagnostic_fails_closed(self) -> None:
        for item in (
            None,
            {"path": "Module.bsl"},
            {"path": "", "diagnostics": []},
            {"path": "Module.bsl", "diagnostics": None},
            {"path": "Module.bsl", "diagnostics": {}},
            {"path": "Module.bsl", "diagnostics": [None]},
            {"path": "Module.bsl", "diagnostics": [{}]},
            {
                "path": "Module.bsl",
                "diagnostics": [{"severity": "Warning", "message": None}],
            },
        ):
            with self.subTest(item=item):
                result = self.run_gate(json.dumps({"fileinfos": [item]}))
                self.assertEqual(result.returncode, 2, result.stderr)


if __name__ == "__main__":
    unittest.main()
