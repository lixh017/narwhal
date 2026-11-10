# Narwhal 项目记忆（跨对话交接文档）

> 最后更新：2026-11-10 15:26 · 用途：换对话后让新会话快速恢复全部上下文

## 项目是什么

**Narwhal · Dive deep. Stand out.**（独角鲸——深潜，成家）
把散落的个人经验/本地文档/云文档**自动扫描→分诊→按领域聚类→沉淀为多个领域知识库**，并可把领域库**编译输出为工作技能**（SOP/CHECKLIST/PLAYBOOK/BRIEF/skill.md）。
本质：一个 Agent Skill（`narwhal`），模式来自 Karpathy 的 LLM Wiki + 个人专家经验方法论（confidence/画像/深潜循环）。

## 关键文件位置

| 内容 | 路径 |
|---|---|
| GitHub 发布仓库（= 本地 git 仓库） | `/workspace/narwhal-repo/`（含 skills/narwhal、README、LICENSE、CHANGELOG、ITERATION、dist/narwhal.skill） |
| skill 源文件夹（开发目录） | `/root/.codebuddy/artifact/2f8a7d30-9c21-4f0b-1d6b-e860f1d14000/narwhal/` |
| 单文件发布包 | `/workspace/narwhal.skill` 和 `narwhal-repo/dist/narwhal.skill` |
| 验证用 demo 知识库 | `/workspace/demo-wiki/`（模拟数据：私域运营+直播电商两域，勿删，可作 README 演示素材） |
| 体检脚本 | `narwhal/scripts/wiki_tool.py`（doctor/stats 两命令，已修过 2 处规则 bug） |
| skill 打包工具 | `python3 /root/.codebuddy/plugins/cache/codebuddy-plugins-official/hot-skills/unknown/skills/skill-creator/scripts/package_skill.py <文件夹>` |

## GitHub 状态

- 仓库：**https://github.com/lixh017/narwhal**（public，MIT，用户 lixh017 / ethan）
- 已推送：v1.0.0 基础版本（4 个 commit 中的前 4 个）
- **未推送（在本地，等下次授权）**：`docs: 添加 CHANGELOG 与迭代指南` commit + `v1.0.0` 标签。推送命令：`git push github main --tags`
- ⚠️ 推送需要重新认证：CodeBuddy 连接器 Token 是**只读**（建仓/push 均 403），可用方案：
  1. Device Flow（本次成功用过）：`curl -s -X POST https://github.com/login/device/code -H "Accept: application/json" -d "client_id=178c6fc778ccc68e1d6a&scope=repo"` → 给用户用户码 → 轮询 access_token
  2. 用户提供 PAT（勾 repo 权限）
- 只读 Token 获取方式：`source /root/.codebuddy/skills/github-connector/scripts/get_token.sh github`（clone/查看可用）
- Gitee 未配置（用户决定先用 GitHub）；skills CLI 支持任意 git 主机的完整 URL

## SKILL 核心设计（新会话快速理解）

- 三层架构：`raw/`（不可变源材料）→ entries/cases/methods/moc（agent 拥有）→ SCHEMA.md（结构权威）
- 五模式：A 初始化 / B 深潜(ingest) / C 导航(query) / D 体检(lint) / **E 全域扫描(discover)**
- **skill-forge**：领域库 ≥5条目+2案例 后可编译输出到 `wiki/exports/<领域>/`
- 会话恢复仪式（orientation）：SCHEMA → HOME → log.md 末 20-30 行，强制先读后动
- `log.md` 只追加；`confidence: 高/中/低` 分级；质量红线"经验>信息，不搬运通用知识"
- 模板 5 套在 `assets/templates/`（entry/case/moc/expert-profile/schema）

## 变现结论（已讨论定调）

卖文件不成立；正解是**"骨架开源（已做），判断力闭源"**：
1. 先免费铺量（提交 skills.sh/TypingMind/Skillselion 收录）
2. 用 Narwhal 武装自己的领域经验 → 编译领域技能包
3. 卖服务（深潜陪跑/建库咨询 retainer）而非文件
4. 远期：垂直领域付费版（$99-499/月档）或托管应用
保护：wiki 内容永不进公开仓库（建议加 .gitignore `wiki/`）；品牌名 Narwhal 可注册商标；付费版走私有仓库+商业授权。

## 待办清单

- [ ] 重新授权 GitHub → 推送 CHANGELOG commit + v1.0.0 标签
- [ ] README 补效果演示（可用 /workspace/demo-wiki 截图/GIF）
- [ ] 提交 skills.sh、TypingMind、Skillselion 收录
- [ ] narwhal-repo 加 `.gitignore`（含 `wiki/`）
- [ ] **第一次真实深潜**：用户提供自己的散落文档，跑模式 E 建真实领域库
- [ ] （用户曾问 Gitee，暂缓；如需：完整 URL 形式 `npx skills add https://gitee.com/<user>/narwhal`）

## 环境备忘

- 用户身份：GitHub lixh017（ethan）；当前项目：ExpertLoop · Narwhal
- git 仓库身份已配置：`lixh017@users.noreply.github.com` / `lixh017`
- demo 数据在 `/tmp/demo-src/`（临时，可能已丢失，但 raw 副本在 demo-wiki/raw/）
- 用户语言：简体中文；偏好：直接给结论+行动建议，喜欢先对比再决策
