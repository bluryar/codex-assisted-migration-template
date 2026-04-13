# EVALUATION_LADDER

## Principle

Evidence and reward are not the same thing.

- `trace` is semantic evidence
- `benchmark` is resource evidence
- `E2E` is product evidence

None of them alone should define the architecture.

## P0 veto

Reject immediately if any of these become true:

- new default host bridge
- new public API added only for trace, benchmark, or debug convenience
- long-lived dual truth for the same state
- unexplained transfer or memory regression

## P1 admission

Must pass before higher-level scoring matters:

- contract correctness
- layout and boundary correctness
- ownership and lifetime correctness

## P2 primary reward

Reward these first:

- narrower public API
- fewer default paths
- fewer temporary bridges
- more backend-resident ownership
- less synchronization burden

## P3 secondary reward

Compare only after P0-P2 are satisfied:

- lower H2D/D2H
- steadier RSS
- less graph rebuild
- better latency

## P4 release checks

- E2E golden cases
- long-run stability
- no semantic regressions

## P5 diagnostic-only

Useful for debugging but not for architecture scoring:

- extra intermediate tensor visibility
- ad-hoc microbenchmarks
- one-off debug paths
