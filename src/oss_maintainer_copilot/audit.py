from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

REQUIRED_PATHS = {
    "README": ["README.md", "README.rst"],
    "LICENSE": ["LICENSE", "LICENSE.md"],
    "CONTRIBUTING": ["CONTRIBUTING.md", ".github/CONTRIBUTING.md"],
    "CODE_OF_CONDUCT": ["CODE_OF_CONDUCT.md", ".github/CODE_OF_CONDUCT.md"],
    "SECURITY": ["SECURITY.md", ".github/SECURITY.md"],
    "PULL_REQUEST_TEMPLATE": [".github/PULL_REQUEST_TEMPLATE.md", "PULL_REQUEST_TEMPLATE.md"],
    "ISSUE_TEMPLATES": [".github/ISSUE_TEMPLATE"],
    "CI_WORKFLOW": [".github/workflows/ci.yml", ".github/workflows/ci.yaml"],
}


@dataclass(frozen=True)
class AuditItem:
    name: str
    present: bool
    matched_path: str | None


def _exists(repo: Path, candidates: list[str]) -> tuple[bool, str | None]:
    for candidate in candidates:
        path = repo / candidate
        if path.exists():
            return True, candidate
    return False, None


def audit_repository(repo_path: str | Path) -> list[AuditItem]:
    """Return a deterministic maintainer-readiness audit."""
    repo = Path(repo_path).resolve()
    if not repo.exists():
        raise FileNotFoundError(f"Repository path does not exist: {repo}")
    return [
        AuditItem(name=name, present=present, matched_path=matched_path)
        for name, candidates in REQUIRED_PATHS.items()
        for present, matched_path in [_exists(repo, candidates)]
    ]


def audit_markdown(items: list[AuditItem]) -> str:
    lines = ["# Repository Maintainer Readiness Audit", "", "| Check | Status | Path |", "|---|---:|---|"]
    for item in items:
        status = "✅" if item.present else "❌"
        path = item.matched_path or "—"
        lines.append(f"| {item.name} | {status} | `{path}` |")
    score = sum(1 for item in items if item.present)
    lines.extend(["", f"Score: {score}/{len(items)} checks passing."])
    return "\n".join(lines) + "\n"
