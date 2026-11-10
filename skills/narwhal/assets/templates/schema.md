# WIKI SCHEMA — 约定与领域配置

> 本文件定义这座 wiki 的结构与约定。改结构先改这里。

## 领域配置

| 领域 | 说明 | 状态 |
|---|---|---|
| {{领域名}} | {{一句话}} | 活跃 / 待验证 |

## 结构约定

- `raw/`：不可变源材料，永不修改。文件名 `<YYYY-MM-DD>-<来源名>.md`。
- `entries/`：原子条目，frontmatter 必填 title/domain/type/confidence/source/links。
- `cases/`：经验案例，frontmatter 必填 title/domain/date。
- `methods/`：个人方法论与 SOP。
- `moc/`：每领域一张地图，所有条目必须挂进某张地图。
- `log.md`：只追加，格式 `- YYYY-MM-DD | 模式X | 动作摘要`。

## 标签体系

{{列出建议使用的 tags，保持收敛，如：决策、沟通、技术-XX、复盘}}

## 条目类型定义

- **concept**：我对某事物的理解与判断
- **method**：我验证过的做法/SOP
- **pitfall**：我踩过的坑与代价
- **insight**：反直觉的独家认知
- **resource**：值得回头再看的外部资源（仅存链接+一句评价）

## 一致性规则

- 新条目必须至少链接 1 个已有条目（或 1 张地图）。
- 同一结论在两条目中冲突 → 双方互标矛盾注释，待用户裁决。
- 引用源材料一律相对链接到 `raw/`。
