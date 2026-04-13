---
name: architecture-forum
description: Use when the task is discussion, architecture review, stage-gate review, implementation stop-check, or deletion review for a long-horizon migration project. Focus on control-plane clarity, not implementation detail.
---

# Architecture Forum

Use this skill when the task is primarily about steering the project, not directly implementing features.

## Default objective

Reduce architecture entropy while preserving correctness.

## Required output

1. short diagnosis
2. boundaries to keep / freeze / hide / delete
3. stage-aware execution guidance
4. measurable success signals

## Do not do

- do not drift into module-level implementation detail unless the discussion explicitly asks for it
- do not reward local correctness without asking whether the boundary became simpler
- do not end with a long backlog unless explicitly asked

## Default discussion lenses

- architecture convergence
- transfer and residency
- API surface
- validation design
- context hygiene
- deletion review
