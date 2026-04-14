# Codex Assisted Migration Template

This folder is a standalone template for running a long-horizon AI-assisted migration project such as:

- PyTorch -> GGML
- reference runtime -> production runtime
- prototype Python stack -> C++ inference stack

It is designed for Codex specifically, and aligns with these official docs:

- `codex/rules`
- `codex/guides/agents-md`
- `codex/skills`
- `codex/subagents`
- `codex/hooks`
- `codex/mcp`

The template assumes a Python toolchain managed with `uv`.

It also assumes a recommended reference-model pattern:

- the original Torch implementation is brought in as a read-only reference source
- preferably as a git submodule under `third_party/`
- evidence collection happens through project-owned wrappers and tools
- migration logic does not directly grow inside the reference implementation

## What official docs already cover

OpenAI's official Codex docs explain the platform mechanisms:

- how `AGENTS.md` is discovered and merged
- how skills are authored and loaded
- how subagents are defined and spawned
- how hooks are configured
- how MCP servers are configured
- how execution rules work

## What this template adds

The official docs do not, by themselves, give you a full operating system for a months-long migration project.

This template adds the missing governance layer:

- hot vs cold context separation
- stage-gate execution
- five-line working briefs
- strict preflight for high-risk migration work
- task-card based steering
- temporary exception tracking
- deletion review
- evaluation ladder
- custom subagents for architecture, evaluation, context hygiene, and optional four-role Agent Team Mode
- harness-context, roadmap, gap-analysis, CI-status, feature-status, spec, test-plan, and reference-divergence templates for document-driven migration work

In short:

- official docs explain the machinery
- this template explains how to govern the machinery

## Root document contract

Keep the repository root intentionally small.

As a default rule:

- `README.md` is the human entrypoint
- `AGENTS.md` is the Codex entrypoint
- other prose documents should live under `docs/`

Only promote another root-level document if it is a true top-level control surface rather than ordinary documentation.

## Recommended layout

Hot context:

- `AGENTS.md`
- `docs/state/CURRENT_ARCHITECTURE.md`
- `docs/state/ACTIVE_STAGE.md`
- `docs/state/TEMP_EXCEPTIONS.md`
- `docs/state/EVALUATION_LADDER.md`

Cold context:

- `adr/` when architecture decisions start accumulating
- `evidence/` when raw traces, benchmark logs, or experiment artifacts need a home
- `changelog/` when you want to preserve stage-by-stage history outside hot context
- `docs/specs/` when Agent Team Mode needs spec and test-plan artifacts

Operational controls:

- `.agents/skills/`
- `.codex/agents/`
- `.codex/config.toml`
- `.codex/hooks.json`
- `.codex/hooks/`
- `codex/rules/`
- `docs/guides/AGENT_TEAM_MODE_zh.md`
- `docs/templates/HARNESS_CONTEXT_TEMPLATE.md`
- `docs/templates/ROADMAP_TEMPLATE.md`
- `docs/templates/GAP_ANALYSIS_TEMPLATE.md`
- `docs/templates/CI_STATUS_TEMPLATE.md`
- `docs/templates/FEATURE_STATUS_TEMPLATE.md`
- `docs/templates/SPEC_TEMPLATE.md`
- `docs/templates/TEST_PLAN_TEMPLATE.md`
- `docs/templates/REFERENCE_DIVERGENCE_POLICY_TEMPLATE.md`
- `pyproject.toml`
- `.python-version`
- `third_party/`
- `tools/`

## Why the split matters

For AI agents, too much history in default context is often worse than too little context.

This template uses a simple rule:

- documents that answer "what is true now?" must be short and overwritten
- documents that answer "what happened before?" can preserve history

That prevents old workarounds, old exceptions, and old plans from silently steering new work.

## Setup checklist

1. Put this folder at the root of a repository you want Codex to help with.
2. Copy the root files out if you want them to become the repo's canonical top-level docs.
3. Keep repo-scoped skills under `.agents/skills/`.
4. Keep custom subagents under `.codex/agents/`.
5. Use `uv` for Python-based hooks and skill scripts.
6. Use `.codex/config.toml` for MCP and hook configuration.
7. Treat `codex/rules/` as examples for user/team policy, not as the main project steering system.
8. Put the original Torch reference repo under `third_party/` as a read-only source, not as an actively evolving migration surface.
9. Keep trace/export/golden wrappers in `tools/`, owned by the migration project rather than by the reference submodule.
10. Enable Agent Team Mode only when the task card records PM, Architect, Engineer, and QA ownership.
11. Create `adr/`, `docs/specs/`, `evidence/`, and `changelog/` only when the project actually needs them.

The bundled hooks and shell snippets assume the template contents live at the
repository root. If you keep this folder nested while evaluating it, either run
Python helpers from this directory with `uv run --project . ...` or copy the
contents to the target repository root before enabling hooks that use
`git rev-parse --show-toplevel`.

## Minimum operating rules

Before implementation:

- write the five-line working brief
- classify the task by stage
- fill a task card
- state the permanent boundary being clarified
- state what is out of scope
- escalate to strict preflight for public API, default path, ownership/lifetime, state/output/cache, fallback, benchmark-helper, or optimization work

After implementation:

- report what was changed
- report what did not change
- report what boundary became clearer
- report any temporary exceptions introduced and their delete conditions
- report what the evidence does and does not prove
- report what should not be done next

## Suggested use

This template works best when:

- one human acts as the steering authority
- Codex does implementation and synthesis
- subagents do narrow, lens-specific analysis by default
- Agent Team Mode is explicitly enabled for large, spec-driven migration slices
- hooks add reminders, not heavy-handed automation
- the reference Torch repo stays mostly read-only
- the target runtime repo owns the migration tooling and evidence flow

## Using with a Torch model

For a Torch model migration, the goal is not to instantiate every template.
Start with the smallest control plane that prevents drift:

1. Fill the hot state docs: `docs/state/CURRENT_ARCHITECTURE.md`, `docs/state/ACTIVE_STAGE.md`, `docs/state/TEMP_EXCEPTIONS.md`, and `docs/state/EVALUATION_LADDER.md`.
2. Use `docs/templates/HARNESS_CONTEXT_TEMPLATE.md` as a scratchpad for project-specific commands, model I/O, the runtime path, and extension recipes. Fold only stable, high-signal rules back into `AGENTS.md` or state docs.
3. Keep the original Torch implementation isolated under `third_party/` or another clearly marked reference location.
4. Put reference runners, trace capture, golden export, and comparison tools under `tools/`, not inside the Torch reference implementation.
5. Create `docs/gap-analysis.md`, `docs/roadmap.md`, `docs/ci-status.md`, and `docs/specs/` only when the project actually needs those artifacts.

Recommended initial layout:

```text
third_party/original_torch_model/   # semantic authority, mostly read-only
tools/
  run_reference.py                  # calls the Torch reference
  export_golden.py                  # writes golden inputs/outputs
  compare_outputs.py                # compares target vs reference
docs/
  state/
  specs/                            # create on demand
src/ or runtime/                    # target implementation
```

Recommended migration stages:

1. M0 - Reference grounding. Run the Torch model, identify inputs, outputs, tokenizer or processor requirements, weights, state/cache, and golden generation. Produce evidence and gap analysis, not target runtime code.
2. M1 - Runtime contract. Freeze public API, tensor layout, ownership/lifetime, loader/weights ownership, state/cache ownership, and output ownership. Use ADRs and specs when decisions should outlive the task.
3. M2 - Smallest executable slice. Migrate the narrowest path that proves the default runtime path, such as embedding plus one block plus logits, or another explicit subgraph.
4. M3 - Full semantic parity. Expand to the full forward/decode path with golden tests and CI gates.
5. M4 - Performance and footprint. Optimize only after contract, ownership, lifetime, and evaluation gates are clear.

Use Agent Team Mode only after the project has real document handoff points:

- PM owns roadmap ordering, value/risk grades, milestone exit criteria, and feature status.
- Architect owns ADRs, gap analysis, runtime boundaries, and reference divergence decisions.
- Engineer implements only after a task card, spec, test plan, and file ownership are clear.
- QA owns test plans, CI status, golden coverage, evidence quality, and "what this does not prove" notes.

Example first prompt:

```text
We are using this template to migrate a Torch model to a target runtime.
Do not implement code yet.

Read AGENTS.md and docs/state/* hot context, then do M0 reference grounding:
1. Fill or cite a task card.
2. Analyze only the Torch reference inputs, outputs, weights, state/cache, and default inference path.
3. Draft docs/gap-analysis.md.
4. Propose the smallest tools/ reference runner and golden exporter plan.
5. Do not modify the reference implementation or introduce a target runtime API.
```

Example Agent Team Mode prompt for the next stage:

```text
Enable Agent Team Mode for M1 runtime contract design.

PM owns roadmap ordering.
Architect owns runtime boundary and ADR decisions.
QA owns model-io-test-plan.
Engineer does not write code yet; only identify the smallest implementation slice and file ownership.

Freeze the smallest default path: weights -> runtime state -> forward/decode -> output.
Do not optimize, add debug-only public APIs, or add host-visible intermediates for trace convenience.
```

The main failure mode in Torch migrations is keeping two truths alive for too long: the Torch reference and the target runtime. Use this template to make the reference a semantic authority, the target runtime the single canonical default path, and golden evidence the bridge between them.

## Files to customize first

Customize these first:

- `AGENTS.md`
- `docs/state/CURRENT_ARCHITECTURE.md`
- `docs/state/ACTIVE_STAGE.md`
- `docs/state/TEMP_EXCEPTIONS.md`
- `.codex/config.toml`
- `docs/guides/AGENT_TEAM_MODE_zh.md`
- `docs/guides/REFERENCE_INTEGRATION_zh.md`

## Notes on hooks and rules

- Hooks are experimental.
- Rules are experimental.
- Do not over-automate early. Start with reminders and policy examples before turning hooks into hard enforcement.
- This template wires Python hooks through `uv run --project ...` rather than calling `python3` directly.
- Skills can include `scripts/` folders with Python or shell utilities. This template includes both patterns.

## Folder tree

```text
codex-assisted-migration-template/
  AGENTS.md
  docs/
    state/
      CURRENT_ARCHITECTURE.md
      ACTIVE_STAGE.md
      TEMP_EXCEPTIONS.md
      EVALUATION_LADDER.md
    templates/
      TASK_CARD_TEMPLATE.md
      DELETION_REVIEW_TEMPLATE.md
      HARNESS_CONTEXT_TEMPLATE.md
      ROADMAP_TEMPLATE.md
      GAP_ANALYSIS_TEMPLATE.md
      CI_STATUS_TEMPLATE.md
      FEATURE_STATUS_TEMPLATE.md
      SPEC_TEMPLATE.md
      TEST_PLAN_TEMPLATE.md
      REFERENCE_DIVERGENCE_POLICY_TEMPLATE.md
    guides/
      AGENT_TEAM_MODE_zh.md
      REFERENCE_INTEGRATION_zh.md
    notes/
      OFFICIAL_DOC_SUPPLEMENTS_zh.md
  .agents/
    skills/
      architecture-forum/
      migration-stage-gate/
      task-card-enforcer/
      context-hygiene/
      reference-integration/
  .codex/
    config.toml
    hooks.json
    hooks/
    agents/
      team_pm.toml
      team_architect.toml
      team_engineer.toml
      team_qa.toml
  pyproject.toml
  .python-version
  third_party/
  tools/
  # create on demand:
  # adr/
  # docs/roadmap.md
  # docs/gap-analysis.md
  # docs/ci-status.md
  # docs/specs/
  # evidence/
  # changelog/
  codex/
    rules/
```
