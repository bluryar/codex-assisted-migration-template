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
