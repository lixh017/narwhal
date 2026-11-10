# Narwhal 🐋

> **Dive deep. Stand out.** · 中文副标：独角鲸 —— 深潜，成家。
>
> 把散落的个人经验、对话、笔记、文档**自动扫描、按领域聚类**，沉淀为多个结构化领域知识库，并可将领域知识库**编译输出为该领域的工作技能**（SOP / 检查清单 / 实战手册 / 可安装的 Agent Skill）。
>
> 这不是建百科——是把你验证过的经验编译成可复用的专家资产。

## 核心能力

| 模式 | 触发语 | 做什么 |
|---|---|---|
| 🌊 全域扫描 (discover) | "扫描我的资料，建领域库" | 扫描本地/云端散落文档 → 分诊（经验/参考/噪音）→ 聚类分域 → 批量入库 |
| 🔍 深潜 (ingest) | "帮我把这个沉淀下来" | 单份经历/对话/文档 → 确认 → 入库 → 更新地图与专家画像 |
| 🧭 导航 (query) | "我关于 X 积累了什么" | 顺知识地图引用你的个人判断原文回答 |
| 🩺 体检 (lint) | "体检/检查知识库" | 断链、孤儿条目、矛盾检测、覆盖缺口 |
| ⚒️ 技能输出 (skill-forge) | "输出这个领域的工作技能" | 编译 SOP / CHECKLIST / PLAYBOOK / BRIEF / 可安装 skill.md |

灵感来源：[Karpathy 的 LLM Wiki 模式](https://x.com/karpathy)（三层架构：不可变 raw 层 / agent 拥有的条目层 / SCHEMA 约定层）+ 追加式 log.md + 会话恢复仪式（orientation）。

差异化：**面向个人专家经验**——confidence 确信度分级、专家画像（EXPERT-PROFILE）、待深潜问题反哺（OPEN-QUESTIONS）、"经验 > 信息，不搬运通用知识"质量红线。

## 安装

```bash
# 通用（skills 生态）
npx skills add https://github.com/<你的用户名>/narwhal --skill narwhal

# Claude Code
git clone --depth 1 https://github.com/<你的用户名>/narwhal.git /tmp/narwhal
mkdir -p ~/.claude/skills && cp -r /tmp/narwhal/skills/narwhal ~/.claude/skills/narwhal

# Codebuddy / 其他读取 skills 目录的 agent
# 把 skills/narwhal/ 整个目录复制进对应 skills 目录即可
```

## 快速开始

安装后对 agent 说：

1. `扫描我的资料，帮我建领域知识库` —— 指定要扫描的目录（本地或云端）
2. 确认聚类出的领域清单，等待批量入库
3. 之后随时：`深潜这段经历` / `我关于X积累了什么` / `知识库体检` / `输出XX领域的工作技能`

知识库默认生成在 `<工作区>/wiki/`，纯 Markdown，可用 Obsidian / VS Code 直接打开编辑。

## 目录

```
skills/narwhal/
├── SKILL.md              # 技能主指令（触发、五种模式、质量红线）
├── scripts/wiki_tool.py  # 知识库体检：断链 / 孤儿条目 / 缺失元数据 / 统计
└── assets/templates/     # 条目、案例、MOC、专家画像、SCHEMA 模板
```

## License

MIT
