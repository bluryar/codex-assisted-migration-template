# SPEC TEMPLATE

Use this when Agent Team Mode or a staged migration task needs a written interface contract.

```text
Title:
Status: draft | reviewed | frozen | superseded
Owner:
Last updated:
Stage:
Tracks roadmap item:
Related task card:
Related ADR:
Related test plan:
Reference source:
Source inputs:
Default runtime path:
Temporary exceptions allowed:
```

## Precedence

- ADR wins for architecture decisions.
- This spec owns implementation contract details not settled by ADR.
- The QA test plan owns test cases; if the test plan contradicts this spec, report the mismatch and update one of the documents.

## Goal

- TBD

## Non-Goals

- TBD

## Scope

### In Scope

- TBD

### Out Of Scope

- TBD

### Forbidden Touches

- public API unless the task explicitly approves it
- default bridges or fallback behavior not listed in `docs/state/TEMP_EXCEPTIONS.md`
- unrelated helper rewrites, benchmark shortcuts, or debug-only runtime paths

## Contract

| Area | Decision | Owner | Notes |
| --- | --- | --- | --- |
| Inputs |  |  |  |
| Outputs |  |  |  |
| Public API |  |  |  |
| Internal API |  |  |  |
| State ownership |  |  |  |
| Output ownership |  |  |  |
| Cache/graph ownership |  |  |  |
| Allowed host visibility |  |  |  |
| Forbidden bridges |  |  |  |

## Data Shapes

Describe only the shapes that define the contract. Do not mirror implementation details that can be inferred from code.

```text
Type/name:
Fields:
Lifetime:
Owner:
Allowed conversions:
Forbidden conversions:
```

## Error And Fallback Semantics

| Case | Behavior | Evidence Required | Notes |
| --- | --- | --- | --- |
|  |  |  |  |

Fallbacks are not allowed unless they are listed in `docs/state/TEMP_EXCEPTIONS.md` with owner, reason, expiry, and delete condition.

## Reference Divergences

| Case | Reference behavior | Target behavior | Class | Rationale | Evidence |
| --- | --- | --- | --- | --- | --- |
|  |  |  | A/B |  |  |

Use `docs/templates/REFERENCE_DIVERGENCE_POLICY_TEMPLATE.md` when the project has not yet defined its divergence classes.

## Implementation Surfaces

| Surface | Allowed? | Owner | Notes |
| --- | --- | --- | --- |
| Public runtime API | no by default |  |  |
| Internal runtime API |  |  |  |
| Test utility |  |  |  |
| Tool/example code |  |  |  |
| Reference implementation patch | no by default |  |  |

## Implementation Slices

| Slice | Goal | Owner | Depends on | Evidence |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Verification

- Test plan:
- P0 veto checks:
- P1 admission checks:
- P2 convergence signal:
- Evidence that is explicitly not required:

## Exit Gate

- TBD

## Deferred

- TBD

## Stop If

- ownership or lifetime becomes ambiguous
- implementation needs a new public API or default bridge
- a temporary path lacks owner, reason, expiry, or delete condition
- this spec expands into more than one stage
