# ROADMAP TEMPLATE

Use this when PM needs to translate architecture and gap analysis into ordered work.

```text
Owner: pm
Last updated:
Source inputs:
Stage or milestone:
```

## Purpose

- TBD

## Legend

- Value: H/M/L — how much user-visible or migration-critical behavior the item unlocks.
- Risk: H/M/L — implementation complexity, ownership ambiguity, security/privacy risk, or hot-path blast radius.
- Spec: link to the spec when drafted.
- Owner: handoff target, not necessarily the person doing the commit.

## Non-Goals Excluded From This Roadmap

- TBD

## Milestones

### M0 — Correctness Cleanup

| ID | Item | Value | Risk | Spec | Owner | Status |
| --- | --- | :---: | :---: | --- | --- | --- |
|  |  |  |  |  |  |  |

Exit criteria:

- TBD

### M1 — Main Migration Slice

| ID | Item | Value | Risk | Spec | Owner | Status |
| --- | --- | :---: | :---: | --- | --- | --- |
|  |  |  |  |  |  |  |

Exit criteria:

- TBD

## Sequencing Rules

- Items move between milestones only with Architect or human steering approval.
- If an item needs a new permanent boundary, create or cite an ADR before Engineer starts.
- If a row is dropped, preserve the rationale until the next milestone rollover.
- Do not add items only because they improve local benchmark or trace convenience.

## Maintenance Rules

- PM owns ordering, value/risk grades, and whether a spec exists.
- Every roadmap item should have one stage, one owner, and one exit signal.
- Long history belongs in `changelog/`, not in the active roadmap.
