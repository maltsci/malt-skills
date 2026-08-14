---
name: malt-med-evidence
description: >-
  Appraises medical evidence with Oxford CEBM Levels and GRADE certainty (default),
  optionally traditional evidence pyramid and OpenEvidence-style A–D±/U heuristics.
  Use whenever the user asks to appraise evidence level/quality/certainty from a
  DOI, PMID, abstract, methods description, clinical claim, or PICO; mentions
  证据等级, 证据质量, 循证分级, Oxford CEBM, GRADE, evidence pyramid, EvidenceGrade,
  or OpenEvidence-style grading; or wants a structured rationale for how strong a
  study or evidence body is. Prefer this skill even if the user does not say
  “malt-med-evidence”. Chat-only output; not clinical advice.
---

# malt-med-evidence

Appraise medical evidence with clear framework boundaries. Default frameworks are **Oxford CEBM** + **GRADE**. Pyramid and OpenEvidence-style grades are optional.

Skill instructions and reference files stay English. **User-facing reports must match the user’s language.**

## Output language (critical)

1. Detect the language of the **user’s prompt** (not the paper’s language).
2. If the prompt is primarily Chinese, write the **entire report in Chinese**: title, one-line verdict, metadata labels, table headers, rationale, and limits.
3. If the prompt is primarily English, write the entire report in English.
4. Keep established framework names as proper nouns: Oxford CEBM, GRADE, OpenEvidence. Grade tokens may stay as `Level 2b`, `Very Low`, `A–D` because those are standard labels—surrounding prose must still follow the user language.
5. Do **not** default to English merely because references or PubMed metadata are English.

## When to read references

| Need | Read |
| --- | --- |
| Oxford (default) | `references/oxford-cebm.md` |
| GRADE (default) | `references/grade.md` |
| Pyramid requested / “all four” | `references/pyramid.md` |
| OpenEvidence / EvidenceGrade / OE / “all four” | `references/openevidence-heuristic.md` |

Load only the refs for selected frameworks. On ambiguity, follow the reference file (and linked official sources), not memory. **Do not paste long reference tables into the user report**—apply them silently and cite the rule in one short clause.

## Modes

| Mode | When | GRADE behavior |
| --- | --- | --- |
| **Single-study** (default) | One paper / DOI / PMID / abstract | Coarse GRADE-style estimate + mandatory disclaimer; **no formal upgrading** |
| **Body-of-evidence** | Claim/PICO, multiple papers, SR/guideline body | Formal GRADE for **one** named critical outcome |

If body mode has only one study: offer single-study coarse path or ask for more evidence / an SR summary.

## Framework selection

| User intent | Frameworks |
| --- | --- |
| Default / unspecified | Oxford + GRADE |
| Names pyramid / OE / EvidenceGrade, or “all four” / 全部 | Add those (or all four) |
| Explicit subset | Only named frameworks |

Never present grades from different systems as convertible equivalents.

## Workflow

### 1. Intake

Accept: DOI, PMID, abstract, methods blurb, pasted text, clinical claim, PICO.

Detect: reply language, mode, frameworks (default Oxford + GRADE).

**Guideline code only (e.g. `1B`):** briefly explain that many systems mix recommendation strength + evidence quality in a guideline-specific code. Do **not** reverse-map into Oxford/GRADE/OE without PICO + evidence summary.

### 2. Enrich (DOI / PMID)

If the user gave only an identifier, run the bundled script (no other skills):

```bash
python3 "{baseDir}/scripts/fetch_literature.py" --pmid <PMID>
python3 "{baseDir}/scripts/fetch_literature.py" --doi <DOI>
```

Optional: set `NCBI_EMAIL` for NCBI politeness.

Prefer PubMed/NCBI; fall back to Crossref for DOI metadata. On failure or missing abstract: ask for abstract + study design; do not invent facts. Title-only grading only if the user insists → mark **low confidence**.

If `publication_types` includes **Retracted Publication**: put a **RETRACTED** banner at the very top, downgrade trust sharply, and do not present the paper as reliable clinical support.

### 3. Gate

Ask only missing critical fields (batch when possible): question type; study design; body-mode PICO + one critical outcome; optional frameworks.

After one failed clarification on question type → omit Oxford rather than guess.

### 4. Appraise

Read selected refs and apply rules. Prefer “Unable to assess” over silent assumptions.

- **Oxford:** question type → Level (design navigation only).
- **GRADE single-study:** design start; RoB / indirectness / imprecision only as supported; inconsistency & publication bias usually unable to assess; **no formal upgrading**; include single-study disclaimer.
- **GRADE body:** five domains for one critical outcome.
- **Pyramid / OE-style:** only if selected; OE always labeled non-official heuristic.

### 5. Report (chat only) — short and front-loaded

Goals from user feedback: **lead with the answer**, **match language**, **avoid textbook dumps**.

Order:

1. Retraction banner (if any)
2. **One-line verdict** (grades in plain words)
3. Compact metadata (mode / question type / frameworks / source)
4. **Summary grades table**
5. **Rationale**: ≤1 short sentence per framework (rule + result). No hierarchy lectures, no full domain essays unless the user asks for detail.
6. **Limits**: 2–4 short bullets max

#### English skeleton

```markdown
## Evidence appraisal

> **RETRACTED** — … (only if needed)

**Verdict:** Oxford Level X; GRADE <certainty> (single-study coarse). …

**Mode:** Single-study | Body-of-evidence  
**Question type:** …  
**Frameworks:** Oxford, GRADE[, Pyramid][, OE-heuristic]  
**Source:** …

### Summary grades
| Framework | Grade | Note |
|---|---|---|
| Oxford CEBM | Level X | … |
| GRADE | … | … |

### Rationale
- **Oxford:** …
- **GRADE:** …

### Limits
- Grades are not interchangeable across systems.
- Not clinical advice.
- [If single-study GRADE:] Single-study GRADE-style estimate — not a formal body-of-evidence GRADE rating.
- [If OE:] OpenEvidence-style heuristic (not official OpenEvidence EvidenceGrade).
```

#### Chinese skeleton (use when the user writes Chinese)

```markdown
## 证据评级

> **已撤稿** — …（仅在需要时）

**结论：** Oxford Level X；GRADE <确定性>（单篇粗评）。…

**模式：** 单篇研究 | 证据体  
**问题类型：** 治疗 / 诊断 / 预后 / 危害 / 病因 / 不明  
**所用体系：** Oxford、GRADE[、金字塔][、OE 启发式]  
**来源：** …

### 等级一览
| 体系 | 等级 | 说明 |
|---|---|---|
| Oxford CEBM | Level X | … |
| GRADE | … | … |

### 简要理由
- **Oxford：** …
- **GRADE：** …

### 边界
- 各体系等级不可直接互换。
- 非临床诊疗建议。
- [单篇 GRADE 时：] 单篇 GRADE 风格粗评，不是正式证据体 GRADE 评级。
- [启用 OE 时：] OpenEvidence 风格启发式（非官方 EvidenceGrade）。
```

For body-of-evidence GRADE, still name which domains moved the rating, but keep each domain to a few words (e.g. “偏倚：多数低风险，不降级”), not paragraphs.

## Non-goals

- No OpenEvidence website / cookie automation
- No equivalence crosswalk across frameworks
- No individualized treatment / dosing advice
- No dependency on other skills
- No dumping full OCEBM/GRADE tables into the chat answer

## Script path note

`{baseDir}` is this skill directory (`Studio/My Skills/malt-med-evidence` or the installed copy). Prefer an absolute path when invoking the script.
