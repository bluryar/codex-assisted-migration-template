---
name: task-card-enforcer
description: Use when a task is under-specified and needs a compact steering card before implementation. Helps keep Codex from silently expanding scope or mixing stages.
---

# Task Card Enforcer

Before implementation, produce or confirm a task card with these fields:

```text
Working brief:
- Current stage:
- Boundary touched:
- Current default path:
- Temporary exceptions allowed now:
- Success signal:

Stage:
Task type:
Goal:
Permanent boundary clarified:
Allowed surfaces:
Out of scope:
Evidence required:
Temporary exceptions allowed:
Stop if:
Exit gate:
Escalate to strict preflight?:
```

## Optional scripts

Use these helpers when useful:

- `scripts/emit_task_card.py`
- `scripts/new-task-card.sh`

Examples:

```bash
uv run --project "$(git rev-parse --show-toplevel)" python \
  "$(git rev-parse --show-toplevel)/.agents/skills/task-card-enforcer/scripts/emit_task_card.py"
```

```bash
"$(git rev-parse --show-toplevel)/.agents/skills/task-card-enforcer/scripts/new-task-card.sh"
```

## Refuse silent expansion

If the task cannot fit on one card:

- split it
- or return to planning

Do not silently widen the task.

Escalate to strict preflight when the task touches public API, default path
selection, runtime ownership/lifetime, state/output/cache, fallback behavior,
benchmark-driven helpers, or performance optimization.
