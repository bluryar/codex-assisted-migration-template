# third_party

Use this directory for isolated reference sources, such as:

- upstream model repositories
- original Torch inference implementations
- vendor copies or git submodules used as semantic authorities

Recommended default:

- keep these sources read-heavy
- avoid project-specific migration logic inside them
- use project-owned wrappers in `tools/` to gather evidence

If a third-party source must be patched:

- keep the patch explicit
- record it in `docs/state/TEMP_EXCEPTIONS.md`
- define a delete condition
