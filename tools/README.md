# tools

Use this directory for project-owned operational tooling around the migration.

Typical contents:

- `reference_runner/`
- `trace_capture/`
- `exporters/`
- `golden/`
- `benchmark_wrappers/`

These tools should consume the reference implementation, not deform it.

The default policy is:

- wrappers live here
- capture logic lives here
- export logic lives here
- artifact generation lives here

Do not push these concerns into the reference repo unless clearly unavoidable.
