from __future__ import annotations


def trim_to_500(text: str) -> str:
    cleaned = " ".join(text.split())
    if len(cleaned) <= 500:
        return cleaned
    return cleaned[:497].rstrip() + "..."


def application_blurb(role: str, ecosystem: str, usage: str) -> str:
    return trim_to_500(
        f"I am the {role} of an open-source project focused on {ecosystem}. "
        f"Current usage/adoption signal: {usage}. "
        "The repository is public, maintained with documented contribution, security, release, and triage workflows, "
        "and API credits would support issue triage, PR review summaries, release automation, and security checklists."
    )
