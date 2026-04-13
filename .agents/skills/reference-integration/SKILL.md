---
name: reference-integration
description: Use when deciding how to integrate an original or upstream reference implementation into a migration project. Helps keep the reference repo read-heavy, isolated, and focused on evidence production rather than becoming a second migration battlefield.
---

# Reference Integration

Use this skill when the task concerns:

- bringing in an original Torch implementation
- deciding whether to patch a reference repo
- organizing trace/export/golden tooling around a reference source
- preventing migration logic from polluting the upstream model code

## Default bias

- prefer read-only reference integration
- prefer `third_party/` isolation
- prefer project-owned wrappers in `tools/`
- prefer explicit patches over ad-hoc edits

## Ask before acting

1. Is the reference repo being used as a semantic authority or as a work surface?
2. Can the evidence be collected from outside the reference repo?
3. If not, is the patch explicit, temporary, and tracked?
4. Does this change stabilize the reference, or merely make one debugging session easier?

## Good outputs

- a recommendation for `third_party/` layout
- a wrapper/tool ownership split
- a patch policy with expiry
- a clear statement of what should not be modified in the reference source
