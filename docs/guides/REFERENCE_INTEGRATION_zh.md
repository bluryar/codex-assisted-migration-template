# 参考实现集成规则

## 目标

当一个项目从 `PyTorch` 迁移到 `GGML`、`C++` 或其他目标运行时时，原始 Torch 代码不应继续作为主迁移战场。

更稳健的做法是：

- 将原始 Torch 代码作为参考实现引入
- 将其视为语义权威源
- 通过项目自有工具获取 trace / export / golden / benchmark 证据
- 尽量不直接修改参考实现

## 推荐组织方式

```text
project/
  AGENTS.md
  docs/state/CURRENT_ARCHITECTURE.md
  docs/state/ACTIVE_STAGE.md

  third_party/
    model-reference-torch/   # git submodule or isolated vendor copy

  tools/
    reference_runner/
    trace_capture/
    exporters/
    golden/
```

## 角色分工

### 参考实现仓负责

- 提供权威语义
- 提供原始模型结构
- 提供 reference inference 行为

### 迁移项目负责

- trace capture wrapper
- exporter
- golden generation
- reference benchmark harness
- 目标 runtime 实现

## 默认规则

- 不要为了 GGML 迁移便利而持续修改参考 Torch 仓
- 不要把迁移辅助逻辑散落进参考实现内部
- 不要把一次性 debug hook 长期写进参考仓主路径
- 不要让目标 runtime 的临时需求反向塑形参考仓

## 允许的做法

- 在 `tools/` 中 import/reference 子模块代码
- 在外围注册 hook 捕捉中间量
- 在外围运行 reference benchmark
- 在外围做 GGUF/export 流程

## 例外情况

以下情况可能允许临时修改参考实现：

- 导出必须的 metadata 无法从外围获取
- trace hook 点无法通过外围注册
- reference 路径本身缺少 deterministic control

即使如此，也应优先：

1. 保持子模块原样
2. 使用显式 patch
3. 在 `docs/state/TEMP_EXCEPTIONS.md` 中登记
4. 写清 delete condition

## 推荐 patch 策略

```text
patches/
  reference-model/
    0001-add-export-metadata.patch
    0002-add-trace-hook.patch
```

规则：

- patch 必须是显式文件
- patch 必须有 owner
- patch 必须有 expiry
- patch 必须说明为什么外围工具做不到

## 证据流

建议把证据流理解成：

```text
reference repo
  -> wrappers/tools
  -> trace / export / golden / benchmark artifacts
  -> target runtime
```

而不是：

```text
reference repo
  -> 继续长出迁移逻辑
  -> 同时变成第二个主战场
```

## 判断标准

如果一个对参考实现的改动主要价值是：

> “让这次调试更方便”

那么它大概率不该进入参考实现主路径。

如果一个改动的价值是：

> “让参考语义更稳定、更可导出、更可验证”

那么它才更可能值得被接受。

## 一句话规则

参考实现仓是：

> 规范仓 / 权威语义仓

而不是：

> 目标 runtime 的第二个并行开发战场
