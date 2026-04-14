# Agent Team Mode

这是一种可显式启用的四角色协作模式，用于大型、长期、文档驱动的迁移项目。

默认执行路径仍然是单主 agent + stage gate + task card。Agent Team Mode 不是所有任务的默认流程；它只在项目规模、决策层级和验证基础设施都足够复杂时启用。

## 适用场景

启用前应同时满足：

- 项目已经大到单个上下文窗口难以同时保留全局架构和局部实现细节。
- 当前阶段、默认路径、永久边界和退出信号已经能写进 task card。
- 有可执行的测试或评估基础设施，能验证 agent 产出的质量。
- 工作可以通过文件系统文档交接，而不是靠聊天上下文传递状态。
- 人类明确要求使用 Agent Team Mode，或当前 stage 文档明确允许该模式。

不建议启用：

- 小型项目或一次性局部修复。
- 探索性原型，还没有冻结 spec 或 ADR。
- 没有测试基础设施，无法验证实现质量。
- 文件所有权不清楚，多个 agent 可能同时改同一处 runtime 代码。

## 四角色

| Role | Codex agent | Owns | Must not own |
| --- | --- | --- | --- |
| PM | `team_pm` | roadmap, milestone sequencing, active-stage updates, spec status | architecture decisions, runtime code |
| Architect | `team_architect` | ADR, gap analysis, permanent boundaries, reference divergence policy, technical spec review | implementation throughput, CI-only fixes |
| Engineer | `team_engineer` | implementation and tests explicitly assigned by task card | architecture decisions, roadmap, spec ownership |
| QA | `team_qa` | test plans, coverage matrices, CI status, evidence summaries | runtime architecture, debug-only public APIs |

Existing reviewer agents such as `architecture_reviewer`, `context_governor`, and `evaluation_designer` remain useful for read-only reviews. The `team_*` agents are the four-role execution mode.

## Document Ownership

Use documents as the shared state channel.

| Artifact | Owner | Purpose |
| --- | --- | --- |
| `AGENTS.md` | Human + main agent | Stable project operating rules and hot-context entrypoint |
| `docs/templates/HARNESS_CONTEXT_TEMPLATE.md` | Human + main agent | Project-specific commands, architecture skeleton, and extension recipes to fold into the repo entrypoint |
| `docs/state/ACTIVE_STAGE.md` | PM, approved by main agent/human | Current stage, allowed work, exit gate |
| `docs/state/CURRENT_ARCHITECTURE.md` | Architect, approved by main agent/human | Current permanent boundaries and north star |
| `docs/roadmap.md` or `changelog/roadmap-*.md` | PM | Ordered milestones, value/risk grades, spec links, owner handoff |
| `docs/gap-analysis.md` or `evidence/gap-analysis-*.md` | Architect | Reference-vs-target feature matrix and explicit non-goals |
| `docs/ci-status.md` or `evidence/ci-status-*.md` | QA | What CI tests now, baseline counts, gaps by priority |
| `adr/` | Architect | Event log for non-negotiable architecture decisions |
| `docs/specs/*.md` | PM coordinates, Architect approves technical content | Interface contract between roles |
| `docs/specs/*-test-plan.md` | QA | Test matrix that validates the spec |
| `docs/specs/*-status.md` | PM or QA | Cross-session feature status, branch, task table, key decisions, caveats |
| `docs/state/EVALUATION_LADDER.md` | QA + Architect | Evidence priority and anti-Goodhart checks |
| `docs/state/TEMP_EXCEPTIONS.md` | Main agent/human | Temporary bridges, fallbacks, compatibility paths |
| `evidence/` | QA or Engineer | Raw traces, logs, benchmark outputs, experiment records |
| `changelog/` | PM | Stage history when state docs would become too long |

Do not create all optional directories by default. Create `adr/`, `docs/specs/`, `evidence/`, or `changelog/` only when the project needs them.

Document precedence should be explicit:

- ADR wins over spec for architecture decisions.
- The QA test plan wins over the spec for test cases, but the mismatch must be reported so the spec can be updated.
- State docs describe what is true now; roadmap, CI status, feature status, and gap-analysis docs can preserve dated operational history if they are not in hot context.

## Execution Flow

1. PM turns the stage goal into ordered tasks and cites dependencies.
2. Architect decides permanent boundaries and records ADRs only when the decision should outlive the task.
3. Architect produces or updates gap analysis when reference parity is unclear, using `docs/templates/GAP_ANALYSIS_TEMPLATE.md`.
4. PM coordinates roadmap ordering using `docs/templates/ROADMAP_TEMPLATE.md`.
5. PM coordinates a spec using `docs/templates/SPEC_TEMPLATE.md`.
6. QA writes a test plan using `docs/templates/TEST_PLAN_TEMPLATE.md`.
7. QA records CI baseline and gaps using `docs/templates/CI_STATUS_TEMPLATE.md` when validation scope changes.
8. PM or QA tracks long-running feature branches using `docs/templates/FEATURE_STATUS_TEMPLATE.md`.
9. Engineer implements the smallest reversible slice after spec and test plan exist.
10. QA verifies and reports what the evidence proves and does not prove.
11. Main agent integrates results, updates state docs, and closes or respawns subagents at milestone boundaries.

The core rule is: ADR decides architecture, spec fills implementation contract, test plan validates the spec.

## Task Card Additions

When enabling this mode, the task card must include:

```text
Agent Team Mode: enabled
Role ownership:
- PM:
- Architect:
- Engineer:
- QA:
Shared artifacts:
- ADR:
- Spec:
- Test plan:
Stop if:
- any role needs to change another role's owned artifact without approval
- implementation begins before the spec/test-plan contract exists
- a new public API, default bridge, fallback, or dual truth is introduced for convenience
```

## Memory And Context

Keep memory-like rules small and actionable:

- Save only durable feedback such as "do not do X" or "when doing Y, preserve Z".
- Do not save code patterns that can be inferred from code.
- Do not save git history.
- Do not save temporary task status.
- At milestone boundaries, make sure useful state is in files, then close or respawn long-running subagents.

## Stop Conditions

Stop Agent Team Mode and return to planning if:

- role ownership becomes unclear
- the same state is represented by two long-lived documents
- spec or test-plan work expands beyond the current stage
- QA needs a debug-only public API or default host bridge to test
- Engineer needs to invent architecture not recorded by Architect
- the coordination docs grow faster than the system becomes simpler

## References

- Max Lv, "用 Claude Code 将三万行 Go 项目移植到 Rust：Agent Team 实践与 Harness 效率优化" (`https://maxlv.net/blog/porting-mihomo-to-rust-with-claude/`)
- OpenAI Codex subagents documentation (`https://developers.openai.com/codex/subagents`)
- OpenAI Codex skills documentation (`https://developers.openai.com/codex/skills`)
