#!/usr/bin/env python3
from pathlib import Path


REQUIRED_FILES = [
    "docs/state/CURRENT_ARCHITECTURE.md",
    "docs/state/ACTIVE_STAGE.md",
    "docs/state/TEMP_EXCEPTIONS.md",
    "docs/state/EVALUATION_LADDER.md",
]

REQUIRED_ACTIVE_STAGE_SECTIONS = [
    "## Current stage",
    "## Stage goal",
    "## Entry gate",
    "## Exit gate",
    "## Allowed work",
    "## Forbidden work",
    "## Temporary exceptions allowed in this stage",
    "## Blocking unknowns",
    "## Promotion rule",
]

PLACEHOLDER_MARKERS = [
    "- Stage:",
    "- Name:",
    "- Status:",
    "State exactly what must become true",
]


def main() -> None:
    root = Path.cwd()
    missing = []
    for rel in REQUIRED_FILES:
        path = root / rel
        if not path.exists():
            missing.append(rel)

    if missing:
        print("Missing required state docs:")
        for rel in missing:
            print(f"- {rel}")
        raise SystemExit(1)

    active_stage = (root / "docs/state/ACTIVE_STAGE.md").read_text(encoding="utf-8")
    missing_sections = [
        heading for heading in REQUIRED_ACTIVE_STAGE_SECTIONS
        if heading not in active_stage
    ]
    if missing_sections:
        print("docs/state/ACTIVE_STAGE.md is missing required sections:")
        for heading in missing_sections:
            print(f"- {heading}")
        raise SystemExit(1)

    placeholder_hits = [
        marker for marker in PLACEHOLDER_MARKERS
        if marker in active_stage
    ]
    if placeholder_hits:
        print("docs/state/ACTIVE_STAGE.md still looks like an uncustomized template:")
        for marker in placeholder_hits:
            print(f"- {marker}")
        raise SystemExit(1)

    print("Stage state docs are present and initialized. Review them before implementation.")


if __name__ == "__main__":
    main()
