# malt-skills

[![License](https://img.shields.io/badge/license-Apache--2.0-2ea44f)](LICENSE)
[![Install](https://img.shields.io/badge/install-Claude%20Code%20%7C%20Codex%20%7C%20Cursor-111827)](#安装)
[![Skills](https://img.shields.io/badge/skills-1-0ea5e9)](#技能索引)
[![Language](https://img.shields.io/badge/language-中文%20%7C%20English-1f6feb)](README_EN.md)

[MaltSci.com](https://maltsci.com) · [English](README_EN.md)

## 简介

`malt-skills` 由 [MaltSci.com](https://maltsci.com) **麦伴科研** 维护，收录面向科研全流程的开源 Agent Skills：从课题探索、文献理解与证据评价，到写作交付与科研作图。技能按标准 `SKILL.md` 组织，可用 `npx skills` 安装到主流编码助手。本仓库持续扩展；**当前发布的第一个技能是 `malt-med-evidence`（医学证据评级）**。

## 免责声明

- 本仓库内容供教育与科研支持，**不构成临床诊疗建议**，也不能替代医生判断或正式指南结论。
- 证据等级不等于投稿、立项或诊疗决策。
- 技能中的 OpenEvidence 风格评级为**非官方启发式**，不是 OpenEvidence EvidenceGrade。

## 科研环节与技能地图

| 环节 | 英文 | 示例方向 | 当前状态 |
| --- | --- | --- | --- |
| 课题探索 | Topic Exploration | 选题、基金线索、文献发现 | 即将扩展 |
| 理解与问答 | Read & Ask | 精读、证据核查、循证评级 | **已有：`malt-med-evidence`** |
| 写作与交付 | Write & Deliver | 润色、引文、投稿/回复 | 即将扩展 |
| 作图与可视化 | Figures & Viz | 机制图、组会图表 | 即将扩展 |

## 当前技能：malt-med-evidence

路径：[`skills/malt-med-evidence/`](skills/malt-med-evidence/)

用 **Oxford CEBM** + **GRADE**（可选证据金字塔、OpenEvidence 风格启发式）评价单篇文献或证据体的等级。输入 DOI / PMID / 摘要 / PICO；输出短结构化评级报告（语言跟随用户提问）。单篇 GRADE 为粗评，不是正式证据体评级。

详见技能说明：[中文](skills/malt-med-evidence/README.md) · [English](skills/malt-med-evidence/README_EN.md)

## 快速开始

安装完成后，可直接这样说：

| 想做什么 | 直接这样说 |
| --- | --- |
| 按 PMID 做治疗证据评级 | 请用 malt-med-evidence 评估 PMID 32970396 作为治疗证据的等级（默认框架）。 |
| 补金字塔与 OE | 在上一篇基础上补充金字塔和 OpenEvidence 等级。 |
| 证据体正式 GRADE | 证据体模式。PICO：…；关键结局=…。请对 PMID … 做正式 GRADE。 |
| 诊断问题 | 诊断问题：年龄校正 D-dimer 能否排除 PE？请评估 PMID 24643601（Oxford + GRADE）。 |

## 安装

每个顶层 `skills/<name>/` 都是可安装单元。请安装**完整目录**（含 `references/`、`scripts/`），不要只复制 `SKILL.md`。

### `npx skills`

需要 Node.js 18+。

```bash
# 查看可安装技能
npx skills add maltsci/malt-skills --list

# 安装首个技能（按需加 --global / --agent）
npx skills add maltsci/malt-skills --skill malt-med-evidence --yes --copy

# 安装全部技能
npx skills add maltsci/malt-skills --skill '*' --yes --copy
```

### 用 Prompt 让 Coding Agent 安装

把下面这段发给 **Claude Code / Codex / Cursor** 即可（按需改技能名）：

```text
请从这个仓库安装 malt-med-evidence：
https://github.com/maltsci/malt-skills

执行：npx skills add maltsci/malt-skills --skill malt-med-evidence --yes --copy
（需要时加 --global，以及 --agent claude-code / codex / cursor）
必须保留完整目录（含 references/、scripts/），不要只复制 SKILL.md。
```

### Clone 后手动接入

```bash
git clone https://github.com/maltsci/malt-skills.git
```

将 `skills/malt-med-evidence/` 整目录复制或链接到对应 Agent 的 skills 路径。

## 技能索引

| 技能 | 环节 | 说明 | 路径 |
| --- | --- | --- | --- |
| `malt-med-evidence` | 理解与问答 | Oxford / GRADE 等医学证据评级 | [`skills/malt-med-evidence/`](skills/malt-med-evidence/) |

## 依赖

- Python 3（`malt-med-evidence` 的文献拉取脚本）
- 网络访问 PubMed / Crossref（可选设置 `NCBI_EMAIL`）

## 贡献

欢迎 PR：新技能放在 `skills/<name>/`，须包含带 frontmatter 的 `SKILL.md`。请在 PR 中说明触发场景、适用环节与边界。也可用 Issue 模板提出技能需求。

## License

[Apache License 2.0](LICENSE) · Copyright 2026 maltsci
