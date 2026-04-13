# AGENTS.md

## Mission

This repository uses Codex as a long-horizon migration partner, not as a fast patch generator.

The default goal is:

- reduce architecture entropy
- keep permanent boundaries clear
- move the system toward a single canonical runtime path

The default goal is not:

- maximize short-term throughput
- maximize local trace coverage
- maximize helper count
- maximize compatibility layers

## Instruction priority

Before doing implementation work, always read the hot context documents in this order:

1. `AGENTS.md`
2. `docs/state/CURRENT_ARCHITECTURE.md`
3. `docs/state/ACTIVE_STAGE.md`
4. `docs/state/TEMP_EXCEPTIONS.md`
5. `docs/state/EVALUATION_LADDER.md`

Do not treat historical documents as default steering context.

Keep the repository root minimal by default:

- `README.md` is the human-facing root document
- `AGENTS.md` is the agent-facing root document
- other steering and explanatory docs belong under `docs/` unless they are true top-level control surfaces

## Mandatory workflow

Before any implementation-style task, write a five-line working brief:

1. current stage
2. boundary being touched
3. current default path
4. temporary exceptions allowed now
5. success signal

For ordinary implementation tasks, also confirm:

1. classify the task by stage
2. fill or cite a task card
3. state the permanent boundary being clarified
4. state explicit non-goals
5. state stop conditions

Escalate to strict preflight when the task touches public API, default path
selection, runtime ownership/lifetime, state/output/cache, fallback behavior,
benchmark-driven helpers, or performance optimization.

Strict preflight must answer:

1. task type: diagnosis, stage-gate review, architecture decision, implementation stop-check, or implementation
2. position in the migration sequence
3. why this should happen now rather than earlier or later
4. permanent boundary clarified
5. what will be frozen, hidden, or deleted
6. why any addition is unavoidable if nothing is deleted
7. whether it increases host-visible data, bridges, dual-path synchronization, or ownership ambiguity
8. whether the result belongs in public API, internal API, test utility, or example code
9. delete condition for any temporary path
10. metric proving global convergence rather than local patching
11. smallest reversible slice
12. condition that forces a stop and return to planning

After ordinary implementation:

1. report what changed
2. report what did not change
3. report which boundary became clearer
4. report temporary debt and delete condition, if any
5. report evidence and what the evidence does not prove
6. report what should not be done next

After strict-preflight work, additionally report:

1. whether system complexity went down, stayed flat, or went up
2. unresolved assumptions and risks
3. recommended next step

## Hard constraints

- Do not widen public APIs unless the task is explicitly about API design.
- Do not introduce a new default host bridge to make a local test or trace easier.
- Do not keep two long-lived truths for the same state unless the task explicitly authorizes it and records the expiry.
- Do not let benchmark or debug helpers define the runtime boundary.
- Do not optimize before contract, ownership, and lifetime are clear.
- Do not treat "passes more tests" as proof of architecture quality.
- Do not casually modify the reference Torch implementation when a project-owned wrapper or tool can collect the same evidence.
- Do not let migration-specific helpers accumulate inside the reference submodule by default.

## Preferred bias

- Prefer delete/hide/freeze over add/extend.
- Prefer one narrow default path over several convenient helper paths.
- Prefer backend-resident state over host-visible intermediates.
- Prefer explicit temporary exceptions over hidden fallback behavior.
- Prefer small reversible slices over large mixed-purpose changes.

## Temporary exceptions

Any temporary bridge, fallback, or compatibility path must record:

- owner
- reason
- expiry
- delete condition

If any of those are missing, the exception is not allowed.

## Reference implementation policy

If the project uses an upstream or original Torch implementation:

- place it under `third_party/` or another clearly isolated reference location
- treat it as a semantic authority, not as the main migration work surface
- prefer wrappers in `tools/` for trace capture, export, golden generation, and reference runs
- if a patch to the reference repo is unavoidable, record it as an explicit temporary exception with a delete condition

## Stop and return to planning if

- the easiest next step adds a new host-visible intermediate
- the task starts expanding into multiple stages
- a temporary bridge gains a second caller
- benchmark needs begin to reshape the runtime API
- ownership or lifetime becomes ambiguous
- the write-up grows faster than the system becomes simpler

## Subagents

Use subagents only when explicitly requested, or when a human explicitly asks for a structured discussion with multiple perspectives.

When subagents are used:

- keep each subagent narrow
- do not duplicate work across them
- use them to reduce context pollution, not increase it

## Documents

Treat these as state docs and overwrite them when truth changes:

- `docs/state/CURRENT_ARCHITECTURE.md`
- `docs/state/ACTIVE_STAGE.md`
- `docs/state/TEMP_EXCEPTIONS.md`
- `docs/state/EVALUATION_LADDER.md`

Treat these as event docs and preserve history:

- `adr/` if the repository needs architecture decision records
- `evidence/` if raw traces, benchmarks, or experiment logs need to be retained
- `changelog/` if stage history needs to be preserved outside state docs

These directories are optional and should be created on demand rather than by default.
