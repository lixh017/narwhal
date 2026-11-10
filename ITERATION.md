# 迭代与贡献指南

## 版本号规则（SemVer）

- **主版本 X.0.0**：知识库结构变更（目录/模板/frontmatter 不兼容旧库）
- **次版本 X.Y.0**：新增模式/模板/能力，旧库无需迁移
- **修订 X.Y.Z**：修 bug、措辞优化、脚本修复

## 发布流程

1. 开发分支改动 SKILL.md / scripts / templates
2. 更新 `CHANGELOG.md`（新增一个版本区块）
3. `git tag vX.Y.Z && git push origin vX.Y.Z`
4. 重新打包 `dist/narwhal.skill`（供手动导入渠道）
5. 用户侧升级：`npx skills update narwhal`

## 兼容性红线

改动以下内容必须升主版本并提供迁移说明：

- `wiki/` 目录结构与文件名约定
- 条目/案例 frontmatter 必填字段
- `SCHEMA.md` 的一致性规则语义

条目内容永远向前兼容：新增字段可选，删除字段需迁移脚本。
