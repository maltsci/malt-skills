# malt-skills

[![License](https://img.shields.io/badge/license-Apache--2.0-2ea44f)](LICENSE)
[![Install](https://img.shields.io/badge/install-Claude%20Code%20%7C%20Codex%20%7C%20Cursor-111827)](#installation)
[![Skills](https://img.shields.io/badge/skills-1-0ea5e9)](#skill-index)
[![Language](https://img.shields.io/badge/language-中文%20%7C%20English-1f6feb)](README.md)

[MaltSci.com](https://maltsci.com) · [中文](README.md)

## About

`malt-skills` is an open-source collection of research Agent Skills from **MaltSci** ([maltsci.com](https://maltsci.com)). Skills cover multiple stages of the research workflow—topic exploration, reading & evidence appraisal, writing & delivery, and figures. Install via `npx skills` into common coding agents. **The first published skill is `malt-med-evidence` (medical evidence grading).**

## Disclaimer

- Content is for education and research support only. **It is not clinical advice** and does not replace clinician judgment or formal guidelines.
- Evidence grades are not submission, funding, or treatment decisions.
- OpenEvidence-style grades from skills here are **unofficial heuristics**, not official OpenEvidence EvidenceGrade.

## Research stages & skill map

| Stage | Examples | Status |
| --- | --- | --- |
| Topic Exploration | Ideas, funding clues, literature discovery | Coming soon |
| Read & Ask | Deep reading, claim checks, evidence grading | **Available: `malt-med-evidence`** |
| Write & Deliver | Polishing, citations, submission / response | Coming soon |
| Figures & Viz | Mechanism figures, meeting charts | Coming soon |

## Current skill: malt-med-evidence

Path: [`skills/malt-med-evidence/`](skills/malt-med-evidence/)

Appraise a paper or evidence body with **Oxford CEBM** + **GRADE** (optional evidence pyramid and OpenEvidence-style heuristic). Inputs: DOI / PMID / abstract / PICO. Output: a short structured report in the user’s language. Single-study GRADE is a coarse estimate, not a formal body-of-evidence rating.

More detail: [English](skills/malt-med-evidence/README_EN.md) · [中文](skills/malt-med-evidence/README.md)

## Quick start

After install, try prompts like:

| Goal | Example prompt |
| --- | --- |
| Grade therapy evidence by PMID | Use malt-med-evidence to grade PMID 32970396 for therapy (default frameworks). |
| Add pyramid + OE | Also add pyramid and OpenEvidence-style grades. |
| Formal body GRADE | Body-of-evidence mode. PICO: …; critical outcome = …. Formal GRADE for PMID …. |
| Diagnosis question | Diagnosis: can age-adjusted D-dimer rule out PE? Grade PMID 24643601 (Oxford + GRADE). |

## Installation

Each top-level `skills/<name>/` is an installable unit. Install the **full directory** (`references/`, `scripts/`, etc.)—do not copy only `SKILL.md`.

### `npx skills`

Requires Node.js 18+.

```bash
# List skills in this repo
npx skills add maltsci/malt-skills --list

# Install the first skill (add --global / --agent as needed)
npx skills add maltsci/malt-skills --skill malt-med-evidence --yes --copy

# Install all skills
npx skills add maltsci/malt-skills --skill '*' --yes --copy
```

### Prompt a coding agent to install

Paste this into **Claude Code / Codex / Cursor** (change the skill name if needed):

```text
Install malt-med-evidence from this repo:
https://github.com/maltsci/malt-skills

Run: npx skills add maltsci/malt-skills --skill malt-med-evidence --yes --copy
(Add --global and --agent claude-code / codex / cursor when needed.)
Keep the full skill directory (references/, scripts/); do not copy only SKILL.md.
```

### Clone manually

```bash
git clone https://github.com/maltsci/malt-skills.git
```

Copy or symlink `skills/malt-med-evidence/` into your agent’s skills path.

## Skill index

| Skill | Stage | Summary | Path |
| --- | --- | --- | --- |
| `malt-med-evidence` | Read & Ask | Oxford / GRADE medical evidence appraisal | [`skills/malt-med-evidence/`](skills/malt-med-evidence/) |

## Dependencies

- Python 3 (literature fetch script for `malt-med-evidence`)
- Network access to PubMed / Crossref (optional `NCBI_EMAIL`)

## Contributing

PRs welcome. New skills go under `skills/<name>/` with a frontmatter `SKILL.md`. Describe triggers, research stage, and boundaries. You can also open a skill-request issue.

## License

[Apache License 2.0](LICENSE) · Copyright 2026 maltsci
