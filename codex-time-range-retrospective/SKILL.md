---
name: codex-time-range-retrospective
description: Review all Codex conversations and execution logs within a user-specified time range, group findings by project folder, and write a reusable Markdown retrospective covering concise lessons, personal UI/product/interaction preferences, and three minimal reusable rules per project. Use when the user asks for a time-range-based retrospective of Codex work.
---

# Codex 指定时间范围复盘

## 任务

阅读并检索用户指定时间范围内的所有 Codex 对话记录与执行日志，按照项目文件夹分别进行系统性复盘，并提炼可复用的经验文档。

只使用当前环境可访问或用户提供的 Codex 对话与执行日志来源，不写死具体用户路径、平台或目录结构。

## 执行步骤

1. 获取并记录用户指定的时间范围；未指定范围时先要求补充，不自行扩大范围。
2. 只检索该时间范围内的 Codex 对话记录与执行日志。
3. 从记录中的工作目录、文件路径和任务上下文识别项目文件夹，并按项目分别归纳。
4. 证据不足时，跳过对应分析，不补猜、不强行下结论。
5. 将完整复盘结果写入 Markdown 文档。

## 输出顺序与内容

严格按照以下优先级输出：

### 1. 可复用规则清单

- 放在文档最前面。
- 每个项目只保留最重要的三条行为准则。
- 每条规则用一句简洁、不可再简化的命令式表达。

### 2. 我的偏好与理念提炼

- 不超过三句话。
- 从对话中归纳 UI 设计偏好、产品设计理念和交互原则，形成结构化个人风格档案。
- 证据不足的维度不分析。

### 3. 执行经验总结

- 按项目文件夹分别总结，每个项目不超过三句话。
- 三句话依次说明：哪些做法导致了问题、最终正确的执行方式是什么、从中得到的教训。
- 证据不足的项目不分析。

## 最小表达约束

- 规则清单优先于个人偏好与理念，个人偏好与理念优先于执行经验总结。
- 删除不能改变后续执行的背景、重复过程和泛泛评价。
- 不把多个项目合并成一条规则，也不为证据不足的项目补写规则。
