# Changelog

All notable changes to Narwhal will be documented in this file.
Format based on [Keep a Changelog](https://keepachangelog.com/), versioning follows [SemVer](https://semver.org/).

## [1.0.0] - 2026-11-10

### Added

- 三层知识库架构：`raw/`（不可变源材料）+ 条目层（entries/cases/methods/moc）+ `SCHEMA.md`（结构权威）
- 五种工作模式：
  - 模式 A 初始化（cold start）：访谈/素材 → 领域规划 → 建骨架
  - 模式 B 深潜（ingest）：单份经历/文档 → 归档 raw → 确认 → 入库 → 更新画像与问题清单
  - 模式 C 导航（query）：顺 MOC 引用个人判断原文回答
  - 模式 D 体检（lint）：断链/孤儿/frontmatter 脚本检查 + 矛盾检测 + 覆盖缺口
  - 模式 E 全域扫描（discover）：扫描本地/云端散落文档 → 分诊（经验/参考/噪音）→ 聚类分域 → 批量入库
- 领域技能输出（skill-forge）：SOP / CHECKLIST / PLAYBOOK / BRIEF / 可安装 skill.md
- 会话恢复仪式（orientation）：SCHEMA → HOME → log.md 强制预热
- 追加式动作日志 `log.md`
- 专家画像（EXPERT-PROFILE）与待深潜问题清单（OPEN-QUESTIONS）
- 5 套模板：entry / case / moc / expert-profile / schema
- 体检脚本 `scripts/wiki_tool.py`：断链、孤儿条目、缺失元数据、统计
- 差异化机制：confidence 确信度分级、经验>信息质量红线
