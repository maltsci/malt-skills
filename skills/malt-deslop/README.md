# malt-deslop

一个用于修改中文、英文和中英双语文本的编辑技能：去除可预测的 LLM 写作痕迹，同时保留作者原意、事实依据、语体与个人声音。

**所属环节：** 写作与交付（Write & Deliver）  
**仓库：** [maltsci/malt-skills](https://github.com/maltsci/malt-skills) · [English](README_EN.md)

## 做什么

- 改掉模板化的 AI / LLM 节奏、空话、假对照、表演性强调和泛化结尾。
- 支持中文特有的“AI 味”表达，以及英文论文中成簇出现的 LLM 风格标记词。
- 保留事实、数字、人名、引文、参考文献、Markdown 链接和原本应有的语体。
- 默认直接给改写稿；也支持只标出有问题的模式、不直接改写。

## 示例

- “请给这段摘要去 AI 味，但保留全部引文和技术术语。”
- “这份报告读起来像 ChatGPT。保持正式语气，改得少一点模板腔。”
- “帮我去 AI 味，保留这段书稿的冷静语气和具体案例。”
- “检查这篇英文论文是否有成簇的 AI-isms，不要直接修改。”

## 非目标

- 不承诺绕过 AI 检测器，也不判断文本是否由人类创作。
- 不编造事实、个人经历、引文，或虚构一种作者声音。
- 不把所有文本都改成口语，不机械删除有意使用的修辞或学科术语。

## 目录

- `SKILL.md` — Agent 工作流与边界
- `references/patterns.md` — 结构与修辞模式
- `references/lexicon.md` — 中文 AI 写作词汇
- `references/english-markers.md` — 需要结合上下文判断的英文 LLM 风格标记
- `evals/evals.json` — 定性评测提示词

## License

与仓库相同：[Apache-2.0](../../LICENSE)
