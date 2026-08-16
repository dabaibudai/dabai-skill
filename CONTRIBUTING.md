# Skill 上传规范

本规范适用于向 `dabai-skill` 新增或更新 Agent Skill。

## 1. 目录结构

每个 Skill 使用一个独立的、同级目录：

```text
dabai-skill/
├── README.md
├── CONTRIBUTING.md
└── <skill-name>/
    ├── SKILL.md
    ├── references/   # 可选：详细规则、评分标准、背景资料
    ├── scripts/      # 可选：可执行脚本
    ├── assets/       # 可选：模板、图片等资源
    └── examples/     # 可选：示例输入与输出
```

规则：

- 一个目录只对应一个 Skill；不要把多个 Skill 合并到同一个 `SKILL.md`。
- 目录名使用小写 kebab-case，例如 `agents-md-doctor`。
- 目录名必须与 `SKILL.md` frontmatter 中的 `name` 完全一致。
- 所有被 `SKILL.md` 直接引用的本地文件都必须随 Skill 一起提交。

## 2. `SKILL.md` 最低要求

文件必须以 YAML frontmatter 开头：

```yaml
---
name: example-skill
description: Describe when the skill should be used and what it does.
---
```

正文至少应说明：

- **用途与触发条件**：什么请求应该使用这个 Skill。
- **输入与输出**：需要什么输入，交付什么结果。
- **执行流程**：按什么顺序操作，哪些步骤是必须的。
- **验证标准**：如何判断结果真的完成，而不是只完成配置或静态检查。
- **安全边界**：权限、敏感信息、破坏性操作和需要用户确认的事项。

写作要求：

- 使用可执行、无歧义的指令；明确区分“必须”“应该”和“可选”。
- 保留必要的质量与安全闸门，不为了简短而删除验证要求。
- 详细规则放入 `references/`，`SKILL.md` 只保留路由和执行所需的核心内容。
- 不提交 API Key、Token、密码、Cookie、私有账号信息或真实本机敏感路径。

## 3. 配套文件规范

- `references/`：存放被 `SKILL.md` 直接引用的详细规范；引用路径必须正确。
- `scripts/`：脚本应有明确入口、失败时返回非零状态，并避免把凭据写入日志。
- `assets/`：只提交运行或理解 Skill 所必需的资源，并说明用途。
- 外部依赖必须在文档中写明安装方式、版本要求和无法安装时的替代方案。

## 4. 提交前检查

提交前至少完成以下检查：

```bash
# 目录与入口
test -f <skill-name>/SKILL.md

# 检查本地引用是否存在
find <skill-name> -type f -print

# 检查差异与潜在敏感信息
git diff --check
git diff --stat
```

另外确认：

- `SKILL.md` 的 `name` 与目录名一致。
- 所有直接引用文件都能找到并可读取。
- 脚本至少完成语法检查或一次安全的 --help / dry-run。
- 根目录 `README.md` 已加入 Skill 简介和链接。
- 只提交本次 Skill 相关文件，没有混入临时文件、缓存或生成物。

## 5. GitHub 上传流程

推荐通过分支和 Pull Request 提交：

```bash
git checkout -b skill/<skill-name>
git add <skill-name> README.md
git diff --cached --check
git commit -m "Add <skill-name> skill"
git push -u origin skill/<skill-name>
gh pr create --draft --fill
```

Pull Request 描述应包含：Skill 解决的问题、触发方式、主要文件、验证结果和已知限制。

## 6. 最小模板

```markdown
---
name: example-skill
description: State when to use this skill and the outcome it produces.
---

# Example Skill

## Use when

## Inputs

## Workflow

## Validation

## Safety and boundaries
```
