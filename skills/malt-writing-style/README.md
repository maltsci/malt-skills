# malt-writing-style

从若干篇文章提炼可编辑的写作风格指南，再按指定的 `style.md` 改写或起草文本。

**所属环节：** 写作与交付（Write & Deliver）  
**仓库：** [maltsci/malt-skills](https://github.com/maltsci/malt-skills) · [English](README_EN.md)

## 做什么

- 从用户提供的多篇样本提炼证据可回溯的 `style.md`（默认英文规则，中文例句与引文保持中文）。
- 按指定风格指南改写、润色或起草；先迁移论证结构，再按语域决定是否迁移节奏与表面腔调。
- 支持中英文触发与中英样本；科研、法律、医学等高精度文本默认只迁移结构，不硬塞设问、口号或命令腔。
- 可选“只批注、不改写”，在弱论证或不符风格处给修改方向。

## 示例

- “从这几篇文章提炼一个写作风格，输出到 style.md。”
- “按这份 style.md 改写下面的方法学段落，保留全部不确定表述。”
- “Distill a writing style from these essays and save it as style.md.”
- “Apply this style guide to the draft, comments only.”

## 非目标

- 不承诺完美复刻人格、绕过 AI 检测，或不证明文本归属某人。
- 不编造引文、经历、统计数字，也不把样本里的人名、事件、口号搬进无关草稿。
- 不替代用户明确指定的另一份风格指南，也不把单纯“去 AI 味”请求改成风格迁移。

## 目录

- `SKILL.md` — Agent 工作流与边界
- `references/style-template.md` — 风格指南栏目骨架
- `evals/evals.json` — 定性评测提示词
- `evals/fixtures/` — 脱敏后的小体积评测样本

## License

与仓库相同：[Apache-2.0](../../LICENSE)
