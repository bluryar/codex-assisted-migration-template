# TEST PLAN TEMPLATE

Use this to validate a spec or ADR without letting tests redefine the runtime boundary.

```text
Title:
Status: draft | ready | running | passed | failed | superseded
Owner:
Last updated:
Stage:
Tracks task:
Related spec:
Related ADR:
Related task card:
CI surface:
```

## Precedence

This test plan owns the test cases for the related spec or ADR. If this plan and the spec disagree, this plan wins for test implementation and the mismatch must be reported so the spec can be corrected.

## Claim Under Test

- TBD

## Scope And Guardrails

### In Scope

- TBD

### Out Of Scope

- benchmark or performance claims unless the stage explicitly allows them
- debug-only public APIs or default host bridges
- changing existing integration tests just to make a migration pass

### Red Flags

- a test helper becomes a runtime API
- assertions are relaxed instead of fixing the behavior
- external services are required where an in-process or owned harness would prove the same claim

## Evidence Matrix

| Level | Required evidence | Command/artifact | Owner | Status |
| --- | --- | --- | --- | --- |
| P0 veto | no new default host bridge, debug public API, dual truth, or unexplained transfer/memory regression |  |  |  |
| P1 admission | contract, layout, ownership, and lifetime correctness |  |  |  |
| P2 convergence | fewer default paths, fewer bridges, clearer ownership |  |  |  |
| P3 resource | transfer, memory, graph/cache, latency only after P0-P2 pass |  |  |  |
| P4 product | E2E golden, long-run stability, no semantic regression |  |  |  |

## Test Cases

| ID | Scenario | Expected behavior | Source | Evidence | Status |
| --- | --- | --- | --- | --- | --- |
|  |  |  | spec/ADR/reference |  |  |

## Structural Guardrails

| ID | Guardrail | Evidence |
| --- | --- | --- |
|  | no forbidden dependency direction |  |
|  | no server/client/runtime surface outside scope |  |
|  | no public API added for testing only |  |
|  | feature gates compile in minimal and full configurations |  |

## Negative Cases

| ID | Invalid or divergent case | Expected behavior | Classification | Evidence |
| --- | --- | --- | --- | --- |
|  |  |  | A/B |  |

## Required Commands

```bash
# Fill in project-specific commands.
```

## Evidence Does Not Prove

- TBD

## CI Wiring

| Job/command | Required? | Owner | Notes |
| --- | --- | --- | --- |
|  |  |  |  |

## Reviewer Rules

- Existing integration gates should stay green without being edited unless the task explicitly owns those tests.
- Any byte-exact reference test must cite the upstream file and commit or tag used as the reference.
- Divergence tests should cite the divergence class and ADR when one exists.

## Temporary Test Helpers

| Helper | Owner | Reason | Expiry | Delete condition |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

Temporary test helpers must not become runtime APIs.

## Stop If

- the test plan requires a new public runtime API only for observability
- the test plan requires a default host bridge or debug fallback
- the evidence only proves local trace coverage but not contract ownership
- the plan expands beyond the current stage
