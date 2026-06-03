import unittest

from oss_maintainer_copilot.triage import triage_issues


class TriageTests(unittest.TestCase):
    def test_triage_security_issue_gets_p0(self):
        results = triage_issues([
            {"number": 7, "title": "Potential XSS vulnerability", "body": "HTML is not escaped."}
        ])

        self.assertEqual(results[0].priority, "P0")
        self.assertIn("security", results[0].labels)


if __name__ == "__main__":
    unittest.main()
