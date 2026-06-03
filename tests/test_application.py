import unittest

from oss_maintainer_copilot.application import application_blurb


class ApplicationTests(unittest.TestCase):
    def test_application_blurb_fits_form_limit(self):
        text = application_blurb("primary maintainer", "OSS maintainer automation", "early-stage")
        self.assertLessEqual(len(text), 500)


if __name__ == "__main__":
    unittest.main()
