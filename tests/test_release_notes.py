import unittest

from oss_maintainer_copilot.release_notes import draft_release_notes


class ReleaseNotesTests(unittest.TestCase):
    def test_release_notes_groups_fixes(self):
        notes = draft_release_notes("- fix: handle empty issue body\n- docs: update README")

        self.assertIn("## Fixes", notes)
        self.assertIn("## Documentation", notes)


if __name__ == "__main__":
    unittest.main()
