# REFERENCE DIVERGENCE POLICY TEMPLATE

Use this when the target runtime intentionally differs from the reference implementation.

```text
Title:
Status: draft | accepted | superseded
Owner:
Related ADR:
Reference implementation:
Target implementation:
```

## Default Rule

When unsure, choose the safer behavior and record the decision in the spec or ADR before implementation.

Rule of thumb:

- If the user reads the config or public contract expecting X, gets Y instead, and Y is worse for safety, privacy, correctness, ownership, or routing intent, classify as A.
- If the user gets the same destination and the same safety/correctness guarantees but through a slower, larger, deprecated, or less optimal path, classify as B.
- When still unsure, bias toward Class A and escalate to Architect.

## Classes

| Class | Meaning | Default action | Examples |
| --- | --- | --- | --- |
| A | Safety, privacy, correctness, ownership, or user-intent risk | hard error or explicit rejection |  |
| B | Performance, compatibility, legacy behavior, or lower-risk alternate path | warn once or preserve behavior with clear evidence |  |

## Decision Table

| Case | Reference behavior | Target behavior | Class | Rationale | Test annotation |
| --- | --- | --- | --- | --- | --- |
|  |  |  | A/B |  |  |

## Rules

- A divergence must cite a spec or ADR.
- Class A should fail loudly and be covered by negative tests.
- Class B should be visible enough for operators or maintainers to understand the compatibility choice.
- Do not silently add fallbacks to match the reference if the fallback creates ownership ambiguity.
- Do not patch the reference implementation unless the project records an explicit temporary exception.

## Role Consequences

- Specs must include a divergence table when they intentionally differ from the reference.
- Engineer may use the policy as a mid-implementation tie breaker only when the spec is silent; non-obvious cases go back to Architect.
- QA should annotate divergence tests with the class and upstream reference.
- Reviewers should block unclassified intentional divergences.

## Delete Or Revisit Condition

- TBD
