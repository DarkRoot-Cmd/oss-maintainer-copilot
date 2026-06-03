.PHONY: test audit triage release-notes

test:
	python -m unittest discover -s tests

audit:
	oss-maintainer-copilot audit --repo .

triage:
	oss-maintainer-copilot triage --input examples/issues.json --output triage-report.md

release-notes:
	oss-maintainer-copilot release-notes --input CHANGELOG.md --output RELEASE_NOTES.md
