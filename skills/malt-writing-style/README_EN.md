# malt-writing-style

Distill an editable writing-style guide from sample articles, then apply a specified `style.md` to rewrite or draft prose.

**Stage:** Write & Deliver  
**Repo:** [maltsci/malt-skills](https://github.com/maltsci/malt-skills) · [中文](README.md)

## What it does

- Builds an evidence-backed `style.md` from user-supplied samples (English rules by default; Chinese quotations and phrase examples stay Chinese).
- Rewrites, polishes, or drafts against a supplied guide, transferring structure first and only then cadence or surface signals when the target register allows.
- Supports Chinese and English triggers and samples; for scientific, legal, medical, and other high-precision prose, it defaults to structural transfer only.
- Supports comments-only editing that flags weak reasoning or style departures without rewriting.

## Examples

- “Distill a writing style from these essays and save it as style.md.”
- “Apply this style guide to the methods paragraph; keep every uncertainty claim.”
- “从这几篇文章提炼一个写作风格，输出到 style.md。”
- “按这份 style.md 改写，只要批注不要直接改写。”

## Non-goals

- It does not promise a perfect voice clone, detector evasion, or proof of authorship.
- It does not invent quotations, experiences, or statistics, and it does not transplant sample-specific names, incidents, or slogans into unrelated drafts.
- It does not override a separate guide the user already selected, and it does not turn a pure de-AI request into style transfer.

## Layout

- `SKILL.md` — agent workflow and guardrails
- `references/style-template.md` — shared style-guide section skeleton
- `evals/evals.json` — qualitative evaluation prompts
- `evals/fixtures/` — small sanitized evaluation samples

## License

Same as the repository: [Apache-2.0](../../LICENSE)
