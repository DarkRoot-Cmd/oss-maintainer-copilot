from __future__ import annotations

from pathlib import Path

SECTION_MAP = {
    "feat": "Features",
    "feature": "Features",
    "fix": "Fixes",
    "bug": "Fixes",
    "docs": "Documentation",
    "doc": "Documentation",
    "perf": "Performance",
    "security": "Security",
    "chore": "Maintenance",
}


def categorize_line(line: str) -> str:
    lower = line.lower().strip("- *")
    prefix = lower.split(":", 1)[0]
    return SECTION_MAP.get(prefix, "Other")


def draft_release_notes(text: str) -> str:
    sections: dict[str, list[str]] = {name: [] for name in ["Security", "Features", "Fixes", "Performance", "Documentation", "Maintenance", "Other"]}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith(("-", "*")):
            content = line.lstrip("-* ").strip()
            sections[categorize_line(content)].append(content)
    output = ["# Release Notes", ""]
    for section, items in sections.items():
        if items:
            output.extend([f"## {section}", ""])
            output.extend(f"- {item}" for item in items)
            output.append("")
    if len(output) == 2:
        output.append("No release-note items found. Add bullet lines such as `feat: ...` or `fix: ...`.\n")
    return "\n".join(output).rstrip() + "\n"


def draft_release_notes_from_file(path: str | Path) -> str:
    return draft_release_notes(Path(path).read_text(encoding="utf-8"))
