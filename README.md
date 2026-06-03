# OSS Maintainer Copilot

A small, open-source maintainer automation toolkit for GitHub projects. It helps maintainers audit repository health, triage issue exports, and draft release notes without locking the project into a paid service.

> Status: early-stage public project scaffold. Do not claim stars, downloads, or ecosystem adoption until the repository has real usage.

## Why this exists

Open-source maintainers spend a lot of time on repeatable project work: issue triage, pull request review preparation, release note drafting, and repository hygiene. OSS Maintainer Copilot provides a lightweight CLI and GitHub Action pattern that can grow into a Codex-assisted workflow for those tasks.

## Features

- `audit`: check whether a repository has common maintainer files and workflows.
- `triage`: convert a GitHub issues JSON export into a Markdown triage report with suggested labels and priorities.
- `release-notes`: draft release notes from a simple changelog or merged PR list.
- `application-blurb`: generate a short, honest 500-character program-application blurb.
- GitHub Action template for scheduled maintainer audits.

## Install

```bash
python -m pip install .
```

## Usage

Run a repository health audit:

```bash
oss-maintainer-copilot audit --repo .
```

Triage exported issues:

```bash
oss-maintainer-copilot triage --input examples/issues.json --output triage-report.md
```

Generate release notes:

```bash
oss-maintainer-copilot release-notes --input CHANGELOG.md --output RELEASE_NOTES.md
```

Generate a concise application blurb:

```bash
oss-maintainer-copilot application-blurb \
  --role "primary maintainer" \
  --ecosystem "maintainer automation for small OSS projects" \
  --usage "new project; seeking early contributors and pilot repos"
```

## Codex/API credit plan

API credits would be used for optional maintainer workflows:

1. Summarizing large PRs before human review.
2. Suggesting labels and priority for new issues.
3. Drafting release notes from merged pull requests.
4. Producing security-focused review checklists for maintainers.

Human maintainers remain responsible for final decisions.

## Repository readiness checklist

- [x] MIT license
- [x] Code of Conduct
- [x] Contributing guide
- [x] Security policy
- [x] Governance and maintainer files
- [x] Issue templates
- [x] Pull request template
- [x] CI workflow
- [x] Basic tests

## Roadmap

See [ROADMAP.md](ROADMAP.md).

## Contributing

Contributions are welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md), then open an issue or pull request.

## License

MIT. See [LICENSE](LICENSE).
