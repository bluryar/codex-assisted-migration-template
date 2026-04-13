#!/usr/bin/env python3
from pathlib import Path


HOT_DOCS = [
    "AGENTS.md",
    "docs/state/CURRENT_ARCHITECTURE.md",
    "docs/state/ACTIVE_STAGE.md",
    "docs/state/TEMP_EXCEPTIONS.md",
    "docs/state/EVALUATION_LADDER.md",
]

SIZE_BUDGET = {
    "AGENTS.md": 8 * 1024,
    "docs/state/CURRENT_ARCHITECTURE.md": 8 * 1024,
    "docs/state/ACTIVE_STAGE.md": 6 * 1024,
    "docs/state/TEMP_EXCEPTIONS.md": 8 * 1024,
    "docs/state/EVALUATION_LADDER.md": 8 * 1024,
}


def main() -> None:
    root = Path.cwd()
    problems = 0

    for rel in HOT_DOCS:
        path = root / rel
        if not path.exists():
            print(f"MISSING  {rel}")
            problems += 1
            continue

        size = path.stat().st_size
        budget = SIZE_BUDGET[rel]
        status = "OK"
        if size > budget:
            status = "OVER"
            problems += 1
        print(f"{status:6} {rel:28} {size:6d} bytes (budget {budget})")

    if problems:
        print("\nHot context needs cleanup.")
        raise SystemExit(1)

    print("\nHot context looks healthy.")


if __name__ == "__main__":
    main()
