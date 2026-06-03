from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

KEYWORD_LABELS = {
    "bug": ["bug", "error", "exception", "crash", "broken", "regression", "fail"],
    "security": ["security", "vulnerability", "cve", "xss", "csrf", "injection", "secret"],
    "documentation": ["docs", "documentation", "readme", "example", "tutorial"],
    "enhancement": ["feature", "enhancement", "request", "support", "improve"],
    "performance": ["slow", "performance", "latency", "timeout", "memory", "cpu"],
}


@dataclass(frozen=True)
class TriageResult:
    number: int | str
    title: str
    labels: list[str]
    priority: str
    rationale: str


def _text(issue: dict[str, Any]) -> str:
    return f"{issue.get('title', '')}\n{issue.get('body', '')}".lower()


def suggest_labels(issue: dict[str, Any]) -> list[str]:
    text = _text(issue)
    labels = [label for label, words in KEYWORD_LABELS.items() if any(word in text for word in words)]
    return labels or ["needs-triage"]


def suggest_priority(issue: dict[str, Any], labels: list[str]) -> str:
    text = _text(issue)
    if "security" in labels:
        return "P0"
    if any(word in text for word in ["data loss", "production", "crash", "unusable", "regression"]):
        return "P1"
    if "bug" in labels or "performance" in labels:
        return "P2"
    return "P3"


def triage_issues(issues: list[dict[str, Any]]) -> list[TriageResult]:
    results: list[TriageResult] = []
    for index, issue in enumerate(issues, start=1):
        labels = suggest_labels(issue)
        priority = suggest_priority(issue, labels)
        rationale = "Keyword-based first pass; maintainer should confirm before applying labels."
        results.append(
            TriageResult(
                number=issue.get("number", index),
                title=issue.get("title", "Untitled issue"),
                labels=labels,
                priority=priority,
                rationale=rationale,
            )
        )
    return results


def load_issues(path: str | Path) -> list[dict[str, Any]]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(data, dict) and "issues" in data:
        data = data["issues"]
    if not isinstance(data, list):
        raise ValueError("Expected a JSON list of issues or an object with an 'issues' list.")
    return data


def triage_markdown(results: list[TriageResult]) -> str:
    lines = ["# Issue Triage Report", "", "| Issue | Priority | Suggested labels | Rationale |", "|---|---:|---|---|"]
    for result in results:
        labels = ", ".join(f"`{label}`" for label in result.labels)
        lines.append(f"| #{result.number} {result.title} | {result.priority} | {labels} | {result.rationale} |")
    return "\n".join(lines) + "\n"
