# malt-deslop

An editorial skill for removing predictable LLM-writing tells from Chinese, English, and bilingual prose while preserving the writer’s meaning, evidence, register, and voice.

**Stage:** Write & Deliver  
**Repo:** [maltsci/malt-skills](https://github.com/maltsci/malt-skills) · [中文](README.md)

## What it does

- Rewrites formulaic AI/LLM cadence, filler, false contrasts, theatrical emphasis, and generic conclusions.
- Supports Chinese-specific patterns and English academic marker-word clusters.
- Preserves facts, names, dates, quotations, citations, Markdown links, and the intended register.
- Returns revised prose by default; supports audit-only requests that identify meaningful patterns without rewriting.

## Examples

- “Deslop this abstract, but retain all citations and technical terms.”
- “This report sounds like ChatGPT. Keep it formal and make it less formulaic.”
- “帮我去 AI 味，保留这段书稿的冷静语气和具体案例。”
- “检查这篇英文论文是否有成簇的 AI-isms，不要直接修改。”

## Non-goals

- It does not promise to bypass AI detectors or verify human authorship.
- It does not invent facts, personal anecdotes, citations, or a new authorial voice.
- It does not make every text casual, remove intentional rhetoric, or replace appropriate discipline-specific terms.

## Layout

- `SKILL.md` — agent workflow and guardrails
- `references/patterns.md` — structural and rhetorical patterns
- `references/lexicon.md` — Chinese AI-writing lexicon
- `references/english-markers.md` — contextual English LLM style markers
- `evals/evals.json` — qualitative evaluation prompts

## License

Same as the repository: [Apache-2.0](../../LICENSE)
