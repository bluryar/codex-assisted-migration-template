# Codex 辅助迁移模板

语言：[English](README.md) | 中文

这个目录是一套独立模板，用来运行长期 AI 辅助迁移项目，例如：

- PyTorch -> GGML
- reference runtime -> production runtime
- prototype Python stack -> C++ inference stack

它面向 Codex 设计，并对齐这些官方机制：

- `codex/rules`
- `codex/guides/agents-md`
- `codex/skills`
- `codex/subagents`
- `codex/hooks`
- `codex/mcp`

模板假设 Python 工具链由 `uv` 管理。

它也假设一种推荐的 reference-model 组织方式：

- 原始 Torch 实现作为只读参考源引入
- 优先作为 git submodule 或明确隔离的目录放在 `third_party/`
- trace、export、golden、reference run 通过项目自有的 `tools/` 完成
- 迁移逻辑不要直接长在 reference 实现里

## 官方文档已经覆盖什么

OpenAI Codex 官方文档解释的是平台机制：

- `AGENTS.md` 如何发现和合并
- skills 如何编写和加载
- subagents 如何定义和启动
- hooks 如何配置
- MCP server 如何配置
- rules 如何配置

## 这个模板补充什么

官方文档本身不会给出一套“长期迁移项目操作系统”。

这个模板补上治理层：

- 热/冷上下文分离
- stage-gate 执行
- 五行 working brief
- 高风险迁移任务的 strict preflight
- task card 驱动的任务边界
- temporary exception 跟踪
- deletion review
- evaluation ladder
- 用于架构、评估、上下文治理和可选四角色 Agent Team Mode 的自定义 subagents
- harness context、roadmap、gap analysis、CI status、feature status、spec、test plan、reference divergence 等模板

一句话：

- 官方文档解释“Codex 能做什么”
- 这个模板解释“人类怎样治理 Codex 做事”

## 根目录契约

默认保持仓库根目录尽量小。

- `README.md` 是英文人类入口
- `README_zh.md` 是中文人类入口
- `AGENTS.md` 是 Codex 入口
- 其他说明性文档默认放到 `docs/`

只有真正的顶层控制面才应该提升到根目录。

## 推荐布局

热上下文：

- `AGENTS.md`
- `docs/state/CURRENT_ARCHITECTURE.md`
- `docs/state/ACTIVE_STAGE.md`
- `docs/state/TEMP_EXCEPTIONS.md`
- `docs/state/EVALUATION_LADDER.md`

冷上下文：

- `adr/`：当架构决策开始积累时创建
- `evidence/`：当 raw trace、benchmark log、实验记录需要保留时创建
- `changelog/`：当阶段历史不适合继续写在 state docs 里时创建
- `docs/specs/`：当 Agent Team Mode 需要 spec 和 test-plan artifact 时创建

操作控制面：

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

## 为什么要分热/冷上下文

对 AI agent 来说，默认上下文里的历史太多，常常比上下文太少更危险。

本模板使用一个简单规则：

- 回答“现在什么是真的”的文档要短，并且覆盖式更新
- 回答“以前发生过什么”的文档可以保留历史

这样可以防止旧 workaround、旧 exception、旧计划继续悄悄影响新任务。

## 安装和接入清单

1. 把这个目录放到你希望 Codex 协助迁移的仓库根目录。
2. 如果你只是先在子目录里评估模板，等确认后再把根文件复制到目标仓库根目录。
3. repo-scoped skills 放在 `.agents/skills/`。
4. 自定义 subagents 放在 `.codex/agents/`。
5. Python hooks 和 skill scripts 使用 `uv`。
6. MCP 和 hooks 配置放在 `.codex/config.toml` 与 `.codex/hooks.json`。
7. `codex/rules/` 只作为用户或团队策略示例，不作为主要项目 steering 系统。
8. 原始 Torch reference 放在 `third_party/`，作为只读参考源，不作为主要迁移战场。
9. trace/export/golden wrapper 放在 `tools/`，由迁移项目拥有，不放进 reference submodule。
10. 只有 task card 明确记录 PM、Architect、Engineer、QA 所有权时，才启用 Agent Team Mode。
11. 只有项目确实需要时，才创建 `adr/`、`docs/specs/`、`evidence/`、`changelog/`。

模板里的 hooks 和脚本默认假设模板内容位于仓库根目录。如果你把这个目录嵌套起来评估，要么在该目录里使用 `uv run --project . ...`，要么在启用依赖 `git rev-parse --show-toplevel` 的 hooks 前，把内容复制到目标仓库根目录。

## 最小运行规则

实现前：

- 写五行 working brief
- 按 stage 分类任务
- 填写或引用 task card
- 说明这次任务澄清的 permanent boundary
- 说明哪些事情不做
- 任务触碰 public API、default path、ownership/lifetime、state/output/cache、fallback、benchmark-helper、optimization 时，升级到 strict preflight

实现后：

- 报告改了什么
- 报告没改什么
- 报告哪个边界更清楚了
- 报告引入的 temporary exception 和 delete condition，如果有
- 报告证据证明了什么，以及没证明什么
- 报告下一步不应该做什么

## 推荐使用方式

这个模板最适合：

- 一个人类作为 steering authority
- Codex 负责实现和综合
- subagents 默认只做窄范围、按需的 lens-specific 分析
- Agent Team Mode 只在大型、spec-driven 迁移切片中显式启用
- hooks 只做提醒，不做重型自动治理
- Torch reference 基本保持只读
- target runtime repo 拥有迁移工具和证据流

## 用于 Torch 模型迁移

迁移 Torch 模型时，目标不是实例化所有模板。

先建立能防止漂移的最小控制面：

1. 填写热状态文档：`docs/state/CURRENT_ARCHITECTURE.md`、`docs/state/ACTIVE_STAGE.md`、`docs/state/TEMP_EXCEPTIONS.md`、`docs/state/EVALUATION_LADDER.md`。
2. 用 `docs/templates/HARNESS_CONTEXT_TEMPLATE.md` 作为草稿，记录项目命令、模型输入输出、runtime path、扩展 recipe。只有稳定且高信号的规则才折回 `AGENTS.md` 或 state docs。
3. 把原始 Torch 实现隔离在 `third_party/` 或其他明确标注的 reference 位置。
4. 把 reference runner、trace capture、golden export、comparison tool 放在 `tools/`，不要放进 Torch reference。
5. 只有项目确实需要时，才创建 `docs/gap-analysis.md`、`docs/roadmap.md`、`docs/ci-status.md`、`docs/specs/`。

推荐初始布局：

```text
third_party/original_torch_model/   # 语义权威，基本只读
tools/
  run_reference.py                  # 调用 Torch reference
  export_golden.py                  # 导出 golden inputs/outputs
  compare_outputs.py                # 对比 target 和 reference
docs/
  state/
  specs/                            # 按需创建
src/ or runtime/                    # 目标实现
```

推荐迁移阶段：

1. M0 - Reference grounding。跑通 Torch 模型，识别输入、输出、tokenizer 或 processor、weights、state/cache、golden 生成方式。产物是证据和 gap analysis，不是 target runtime 代码。
2. M1 - Runtime contract。冻结 public API、tensor layout、ownership/lifetime、loader/weights ownership、state/cache ownership、output ownership。长期存在的决策用 ADR 和 spec 记录。
3. M2 - Smallest executable slice。迁移能证明默认 runtime path 的最小路径，例如 embedding + one block + logits，或另一个明确子图。
4. M3 - Full semantic parity。扩展到完整 forward/decode path，并用 golden tests 和 CI gates 保护。
5. M4 - Performance and footprint。只有 contract、ownership、lifetime、evaluation gates 清楚后才做优化。

只有当项目已经有真实的文档交接点时，才启用 Agent Team Mode：

- PM 拥有 roadmap 排序、value/risk 分级、milestone exit criteria、feature status。
- Architect 拥有 ADR、gap analysis、runtime boundary、reference divergence decisions。
- Engineer 只有在 task card、spec、test plan、文件所有权清楚后才实现。
- QA 拥有 test plan、CI status、golden coverage、evidence quality 和“证据没有证明什么”的记录。

第一个 prompt 示例：

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

下一阶段启用 Agent Team Mode 的 prompt 示例：

```text
Enable Agent Team Mode for M1 runtime contract design.

PM owns roadmap ordering.
Architect owns runtime boundary and ADR decisions.
QA owns model-io-test-plan.
Engineer does not write code yet; only identify the smallest implementation slice and file ownership.

Freeze the smallest default path: weights -> runtime state -> forward/decode -> output.
Do not optimize, add debug-only public APIs, or add host-visible intermediates for trace convenience.
```

Torch 迁移最常见的失败模式，是 Torch reference 和 target runtime 两套真相共存太久。本模板的用法是：让 reference 成为语义权威，让 target runtime 成为唯一默认路径，让 golden evidence 成为两者之间的桥。

## 首先定制哪些文件

优先定制：

- `AGENTS.md`
- `docs/state/CURRENT_ARCHITECTURE.md`
- `docs/state/ACTIVE_STAGE.md`
- `docs/state/TEMP_EXCEPTIONS.md`
- `.codex/config.toml`
- `docs/guides/AGENT_TEAM_MODE_zh.md`
- `docs/guides/REFERENCE_INTEGRATION_zh.md`

## Hooks 和 Rules 说明

- Hooks 仍是实验性能力。
- Rules 仍是实验性能力。
- 不要过早自动化。先用提醒和策略示例，再考虑把 hooks 做成强 enforcement。
- 本模板通过 `uv run --project ...` 调用 Python hooks，而不是直接调用 `python3`。
- Skills 可以包含 `scripts/` 目录，放 Python 或 shell helper。模板中两种模式都有示例。

## 目录树

```text
codex-assisted-migration-template/
  README.md
  README_zh.md
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
  # 按需创建：
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
