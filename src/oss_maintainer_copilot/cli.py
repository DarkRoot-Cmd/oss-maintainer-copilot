from __future__ import annotations

import argparse
from pathlib import Path

from .application import application_blurb
from .audit import audit_markdown, audit_repository
from .release_notes import draft_release_notes_from_file
from .triage import load_issues, triage_issues, triage_markdown


def _write_or_print(content: str, output: str | None) -> None:
    if output:
        Path(output).write_text(content, encoding="utf-8")
        print(f"Wrote {output}")
    else:
        print(content, end="")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="oss-maintainer-copilot")
    subparsers = parser.add_subparsers(dest="command", required=True)

    audit = subparsers.add_parser("audit", help="Audit repository maintainer readiness.")
    audit.add_argument("--repo", default=".", help="Repository path to audit.")
    audit.add_argument("--output", help="Optional Markdown output path.")

    triage = subparsers.add_parser("triage", help="Triage issues from a GitHub issues JSON export.")
    triage.add_argument("--input", required=True, help="Path to issues JSON.")
    triage.add_argument("--output", help="Optional Markdown output path.")

    release = subparsers.add_parser("release-notes", help="Draft release notes from changelog-style bullets.")
    release.add_argument("--input", required=True, help="Path to changelog or merged PR text.")
    release.add_argument("--output", help="Optional Markdown output path.")

    blurb = subparsers.add_parser("application-blurb", help="Generate an honest 500-character application blurb.")
    blurb.add_argument("--role", required=True)
    blurb.add_argument("--ecosystem", required=True)
    blurb.add_argument("--usage", required=True)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "audit":
        content = audit_markdown(audit_repository(args.repo))
        _write_or_print(content, args.output)
    elif args.command == "triage":
        content = triage_markdown(triage_issues(load_issues(args.input)))
        _write_or_print(content, args.output)
    elif args.command == "release-notes":
        content = draft_release_notes_from_file(args.input)
        _write_or_print(content, args.output)
    elif args.command == "application-blurb":
        print(application_blurb(args.role, args.ecosystem, args.usage))
    else:
        parser.error("Unknown command")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
