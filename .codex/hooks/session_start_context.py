#!/usr/bin/env python3
import json


def main() -> None:
    payload = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": (
                "Before implementation, read AGENTS.md, docs/state/CURRENT_ARCHITECTURE.md, "
                "docs/state/ACTIVE_STAGE.md, docs/state/TEMP_EXCEPTIONS.md, and "
                "docs/state/EVALUATION_LADDER.md. "
                "Treat them as hot context. Write the five-line working brief and use task "
                "cards for implementation work. Use strict preflight for public API, default "
                "path, ownership/lifetime, state/output/cache, fallback, benchmark-helper, "
                "or optimization work."
            )
        }
    }
    print(json.dumps(payload))


if __name__ == "__main__":
    main()
