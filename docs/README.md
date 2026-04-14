# docs

This directory holds project documentation that does not need to live in the repository root.

## Layout

- `state/`
  - hot-context state documents
  - overwrite these when truth changes
- `templates/`
  - operational templates such as task cards and deletion reviews
  - harness-context, roadmap, gap-analysis, CI-status, feature-status, spec, test-plan, and reference-divergence templates for Agent Team Mode
- `guides/`
  - project organization guidance
  - optional Agent Team Mode guidance
- `notes/`
  - supplementary rationale and non-steering notes

## Rule of thumb

- keep repository root as small as possible
- treat `README.md` and `AGENTS.md` as the default root-level docs
- keep hot context easy to find
- keep history and commentary out of default steering paths
- enable multi-agent role ownership explicitly rather than by default
