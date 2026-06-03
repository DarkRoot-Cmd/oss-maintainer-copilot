import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from oss_maintainer_copilot.audit import audit_repository


class AuditTests(unittest.TestCase):
    def test_audit_detects_core_files(self):
        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            (tmp_path / "README.md").write_text("# Test\n", encoding="utf-8")
            (tmp_path / "LICENSE").write_text("MIT\n", encoding="utf-8")

            results = {item.name: item.present for item in audit_repository(tmp_path)}

            self.assertTrue(results["README"])
            self.assertTrue(results["LICENSE"])
            self.assertFalse(results["CONTRIBUTING"])


if __name__ == "__main__":
    unittest.main()
