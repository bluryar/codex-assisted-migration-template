# GAP ANALYSIS TEMPLATE

Use this when Architect compares a reference implementation with the target runtime.

```text
Owner: architect
Date:
Reference implementation:
Target implementation:
Source inputs:
```

## Scope

- TBD

## Explicitly Excluded

These are not counted as gaps unless a later product or architecture decision reverses them.

| Feature | Reason excluded | Decision source |
| --- | --- | --- |
|  |  |  |

## Gap Matrix

| Area | Reference behavior | Target behavior | Status | Priority | Notes |
| --- | --- | --- | --- | --- | --- |
|  |  |  | OK/Partial/Gap/Excluded/Divergent | P0/P1/P2/P3 |  |

## Divergences

| Case | Reference behavior | Target behavior | Class | Decision source |
| --- | --- | --- | --- | --- |
|  |  |  | A/B/N/A |  |

## Recommended Roadmap Inputs

| Item | Why now | Dependency | Suggested owner |
| --- | --- | --- | --- |
|  |  |  |  |

## Stop If

- the analysis starts prescribing implementation details without a boundary decision
- local tests or benchmarks start defining the runtime API
- a missing feature is actually an explicit non-goal
