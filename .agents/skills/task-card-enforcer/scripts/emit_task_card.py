#!/usr/bin/env python3
from pathlib import Path


def main() -> None:
    repo_root = Path.cwd()
    template_path = repo_root / "docs/templates/TASK_CARD_TEMPLATE.md"
    if not template_path.exists():
        print(
            "Task card template not found. "
            "Expected: docs/templates/TASK_CARD_TEMPLATE.md"
        )
        raise SystemExit(1)

    print(template_path.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    main()
