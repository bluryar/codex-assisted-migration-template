---
name: migration-stage-gate
description: Use when implementing or planning a long-horizon migration task. Forces stage classification, entry-gate checks, stop conditions, and exit-gate reporting before and after code work.
---

# Migration Stage Gate

Use this skill before implementation work.

## Before work

First write a five-line working brief:

1. current stage
2. boundary being touched
3. current default path
4. temporary exceptions allowed now
5. success signal

For ordinary implementation work, answer:

1. What stage is this task in?
2. What permanent boundary does it clarify?
3. What is out of scope?
4. What temporary exceptions are allowed?
5. What would force a stop and return to planning?

If those answers are unclear, do not implement yet.

Escalate to strict preflight when the task touches public API, default path
selection, runtime ownership/lifetime, state/output/cache, fallback behavior,
benchmark-driven helpers, or performance optimization.

Strict preflight must answer:

1. What task type is this: diagnosis, stage-gate review, architecture decision, implementation stop-check, or implementation?
2. Where is it in the migration sequence?
3. Why now, rather than earlier or later?
4. What permanent boundary does it clarify?
5. What will this freeze, hide, or delete?
6. If it deletes nothing, why is the addition unavoidable?
7. Will it increase host-visible data, bridges, dual-path synchronization, or ownership ambiguity?
8. Should the result live in public API, internal API, test utility, or example code?
9. If it uses a temporary path, what exact condition deletes it?
10. What metric proves this is global convergence rather than a local patch?
11. What is the smallest reversible slice?
12. What condition forces a stop and return to planning?

## Optional scripts

If you need a deterministic reminder/check, use:

- `scripts/check_stage_state.py`

Run it with:

```bash
uv run --project "$(git rev-parse --show-toplevel)" python \
  "$(git rev-parse --show-toplevel)/.agents/skills/migration-stage-gate/scripts/check_stage_state.py"
```

## During work

Protect these rules:

- one task, one stage, one main claim
- no benchmark helper should reshape the runtime API
- no new default host bridge
- no silent temporary fallback

## After work

For ordinary work, report:

1. what changed
2. what did not change
3. what boundary got clearer
4. temporary debt and delete condition, if any
5. evidence, including what the evidence does not prove
6. what must not be done next

For strict-preflight work, additionally report:

1. whether system complexity went down, stayed flat, or went up
2. unresolved assumptions and risks
3. recommended next step
