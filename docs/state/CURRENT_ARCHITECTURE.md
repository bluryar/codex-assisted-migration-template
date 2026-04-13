# CURRENT_ARCHITECTURE

## Purpose

This file is a state document.

It should describe what is true now about the intended architecture, not how the project evolved historically.

Overwrite it when the current truth changes.

## North Star

Describe the final target shape in 5-10 bullets.

Example prompts:

- What is the single canonical runtime path?
- What is public API vs internal API?
- What data is allowed to be host-visible?
- What are the permanent buffer/state categories?
- What is explicitly not part of the final design?

## Permanent boundaries

Fill in the current permanent boundaries:

- Reference implementation source:
- Reference implementation mutability policy:
- Evidence acquisition surface:
- Public runtime API:
- Internal runtime API:
- State ownership:
- Output ownership:
- Graph/cache ownership:
- Loader/weights ownership:
- Allowed host export boundaries:
- Forbidden default bridges:

## Known non-goals

- 
- 
- 

## Architecture red flags

List the patterns that mean the system is drifting:

- 
- 
- 
