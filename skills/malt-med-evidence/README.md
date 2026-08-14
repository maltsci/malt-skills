# malt-med-evidence

医学证据评价技能：对 DOI / PMID / 摘要 / PICO 或临床主张给出结构化评价。

**所属环节：** 理解与问答（Read & Ask）  
**仓库：** [maltsci/malt-skills](https://github.com/maltsci/malt-skills) · [English](README_EN.md)

## 做什么

- 默认框架：**Oxford CEBM** + **GRADE**
- 可选：证据金字塔、OpenEvidence 风格启发式（A–D± / U）
- **单篇模式**（默认）：设计导航 + GRADE 风格粗评（须带单篇免责）
- **证据体模式**：对某一个命名关键结局做正式 GRADE

报告语言跟随用户提问（中文问→中文报）。聊天输出；**不构成临床诊疗建议**。

## 输入 / 输出

| 输入 | 输出 |
| --- | --- |
| DOI、PMID、摘要、方法片段、PICO、主张 | 一句话结论、等级表、简要理由、边界 |

有 PMID/DOI 时，技能会调用本目录 `scripts/fetch_literature.py` 拉取元数据与摘要。

## 依赖

- Python 3
- 网络（PubMed / Crossref）
- 可选环境变量：`NCBI_EMAIL`

```bash
python3 scripts/fetch_literature.py --pmid 32970396
python3 scripts/fetch_literature.py --doi 10.1056/NEJMoa2024816
```

## 非目标

- 不爬取 OpenEvidence 官网 / 不做 cookie 自动化
- 不把各体系等级当成可互换分数
- 不给出个体化用药或剂量建议
- 不依赖本仓库外的其他技能

## 目录

- `SKILL.md` — Agent 执行说明
- `references/` — Oxford / GRADE / 金字塔 / OE 启发式
- `scripts/fetch_literature.py` — 文献元数据拉取
- `evals/evals.json` — 评测用例

## License

与仓库相同：[Apache-2.0](../../LICENSE)
