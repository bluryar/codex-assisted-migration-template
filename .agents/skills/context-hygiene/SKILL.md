---
name: context-hygiene
description: Use when updating plans, skills, AGENTS files, or project documentation for a long-running migration. Keeps hot context short, current, and high-signal.
---

# Context Hygiene

Treat the document system as control plane, not knowledge warehouse.

## Hot context

Keep short and overwrite when truth changes:

- AGENTS
- current architecture
- active stage
- temporary exceptions
- evaluation ladder

## Cold context

Preserve history here:

- adr
- evidence
- changelog

## Optional scripts

Use `scripts/check_hot_context.py` for a simple size-and-presence audit of hot docs.

```bash
uv run --project "$(git rev-parse --show-toplevel)" python \
  "$(git rev-parse --show-toplevel)/.agents/skills/context-hygiene/scripts/check_hot_context.py"
```

## Rules

- state over story
- add one, delete one
- one rule, one canonical source
- archive history out of hot context
- if a doc answers \"what is true now\", overwrite it
