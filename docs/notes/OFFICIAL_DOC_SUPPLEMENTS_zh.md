# 官方 Codex 文档需要补充的落地层

官方文档已经很好地覆盖了这些机制：

- `AGENTS.md` 的发现与覆盖顺序
- skill 的目录结构与触发方式
- skill 中 `scripts/` / `references/` / `assets/` 的组织方式
- subagents 的定义与管理
- hooks 的配置
- MCP 的配置
- rules 的配置

但如果要把 Codex 真正用于一个长期迁移项目，官方文档仍然缺少下面这些“治理层”内容。

## 1. 缺少长期项目的目标函数设计

官方文档告诉你如何配置 Codex，但没有告诉你：

- 怎样避免 agent 被局部 trace / benchmark 奖励带偏
- 怎样把“架构收敛”放到比“局部跑通”更高的优先级

## 2. 缺少 stage-gate 机制

官方文档没有提供：

- 一次长期迁移应该如何分阶段
- 每阶段的入口门、出口门、禁止事项
- agent 什么情况下必须停工回规划

## 3. 缺少证据与奖励分离的方法

官方文档没有强调：

- `trace` 是语义证据，不是架构正确性
- `benchmark` 是资源证据，不是接口设计依据
- `E2E` 是产品证据，不是边界设计依据

## 4. 缺少热/冷上下文治理

官方文档说明了文件如何被发现，但没有告诉你：

- 哪些文档应该是覆盖式 state docs
- 哪些文档应该是保历史的 event docs
- 如何防止长计划、长技能、长变更记录稀释 steering 信号

## 5. 缺少临时例外的治理模型

官方文档没有明确提供：

- temporary bridge 的登记格式
- expiry 与 delete condition 的规则
- 何时把“临时方案”判定为永久噪音

## 6. 缺少面向人类的 steering protocol

官方文档没有给出一个完整的操作者协议，例如：

- 每次任务开始前要强制 agent 回答什么
- 每次任务结束后必须汇报什么
- 什么情况要暂停实现

## 本模板的目标

本模板补上的正是以上这些治理层：

- `AGENTS.md`
- `docs/state/CURRENT_ARCHITECTURE.md`
- `docs/state/ACTIVE_STAGE.md`
- `docs/state/TEMP_EXCEPTIONS.md`
- `docs/state/EVALUATION_LADDER.md`
- `docs/templates/TASK_CARD_TEMPLATE.md`
- `docs/templates/DELETION_REVIEW_TEMPLATE.md`
- `.agents/skills/`
- `.codex/agents/`
- `.codex/hooks.json`
- `codex/rules/default.rules.example`

一句话概括：

官方文档解决“Codex 能做什么”，本模板解决“人类怎样治理 Codex 做事”。

## 额外修正：更贴近真实 Python 工作流

如果团队常用 `uv` 管理 Python 项目，那么模板最好显式体现这一点。

因此本模板额外做了这些落地修正：

- 增加 `pyproject.toml`
- 增加 `.python-version`
- Python hooks 默认通过 `uv run --project ...` 调用
- skills 目录加入 `scripts/` 示例，覆盖 Python 和 shell 两种用法

这部分不是对官方文档的替代，而是把官方推荐能力接到一个更常见的工程习惯上。

## 额外修正：参考实现仓的组织边界

官方文档也没有直接回答一个很常见的迁移问题：

- 原始 Torch 仓库应不应该继续在主项目里被长期修改？
- 它应该作为主战场，还是作为参考源？

本模板对此给出的落地答案是：

- 推荐把原始 Torch 代码作为只读参考实现引入
- 优先使用 `git submodule` 或明确隔离的 `third_party/` 目录
- 将 trace/export/golden/reference benchmark 逻辑放在主项目自己的 `tools/` 中
- 只有在无法通过外围方式获取证据时，才通过显式 patch 方式临时改动参考仓

这部分属于“项目组织治理”，也是官方机制文档之外的补充层。
