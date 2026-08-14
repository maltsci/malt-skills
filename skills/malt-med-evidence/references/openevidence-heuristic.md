# OpenEvidence-style Evidence Grade Heuristic

**Mandatory label on every OE-style output:**

> OpenEvidence-style heuristic (not official OpenEvidence EvidenceGrade)

## Why heuristic

- OpenEvidence publishes a methodology overview: https://www.openevidence.com/evidence-grade
- There is **no** usable public EvidenceGrade API for this skill.
- Cookie/session wrappers around the OpenEvidence website are **out of scope**.

This file approximates OE’s *publicly described* process for optional grading inside `malt-med-evidence`. It is **not** EvidenceGrade™.

## When to use

Only if the user asks for OpenEvidence / EvidenceGrade / “OE” / “all four frameworks,” or explicitly wants an A–D± style quick check.

OE-style grading is closest to grading a **claim / answer**, not stamping journal prestige. In single-study mode, treat the paper as the main (often only) evidence behind the claim.

## Gradeability gate (do this first)

Return **U** (Unable to Grade) when:

- The request is definitional lookup, summarization, or open-ended clinical reasoning without a clear evidentiary claim
- The case is too composite to reduce to one evidence question
- There is no assessable relevant evidence

Distinct from **D**: D = relevant but very weak evidence exists; U = cannot grade.

## Public OE method (summary)

### Phase 1 — Per-paper axes

1. **Quality** — design strength relative to best-achievable design for the question type  
2. **Certainty** — precision/confidence (CI width, sample size, effect clarity)  
3. **Relevance** — directness to PICO  

### Phase 2 — Body-level (GRADE-inspired)

1. Weight toward most relevant papers  
2. Defer to current guideline / high-quality SR evidence ratings when they directly answer the question (override if clearly outdated or contradicted by stronger newer evidence)  
3. Set a **ceiling** from best relevant design (RCT/authoritative → A ceiling; observational often B ceiling; weaker lower; observational may reach A only when it is best-achievable for that question type, e.g. prognosis cohort)  
4. **Upgrades** — large consistent effect; dose–response; convergence across strong independent sources  
5. **Downgrades** — bias/design limits; inconsistency; imprecision; indirectness  
6. Output **A–D** with optional **+/-**, or **U**

## Grade meanings (public OE wording, condensed)

| Grade | Meaning |
| --- | --- |
| A | Strong — best-achievable designs / rigorous SRs / strong current guidelines; precise, consistent, direct |
| B | Moderate — appropriate designs with notable limits (sample, surrogates, observational for therapy, etc.) |
| C | Limited — weaker designs or stronger designs with serious multi-axis limits |
| D | Minimal — case reports/series, preclinical, mechanism-only directional signal |
| U | Unable to grade |
| +/- | Boundary case tied to Quality, Certainty, or Relevance |

## Local heuristic mapping (this skill)

Use this practical mapping when applying OE-style grades without OE’s internal retrieval stack:

| Situation | Suggested OE-style grade |
| --- | --- |
| Current authoritative guideline or high-quality SR directly answers the claim with strong, consistent evidence | A or A- |
| Multiple consistent RCTs / SR of RCTs, direct PICO, adequate precision | A or B+ |
| Single adequate RCT, direct, reasonably precise | B+ to B |
| Observational evidence for a therapy claim, or best-feasible design with clear limits | B to C |
| Small / imprecise / indirect single study | C |
| Case report/series, animal/in vitro, mechanism only | D |
| Not a gradeable single claim, or insufficient assessable evidence | U |

**Modifiers:** use `+` / `-` only when the case clearly sits on a boundary for one named axis (Quality / Certainty / Relevance).

### Single-study OE-style notes

- Ceiling is usually driven by that study’s design vs question type.  
- Without a broader body, prefer **not** to award plain **A** unless the paper itself is a current guideline synthesis or an SR that already grades strong, consistent evidence for the claim.  
- Always keep the non-official label.

### Body-of-evidence OE-style notes

- Prefer anchoring on the most relevant SR/guideline when provided.  
- Do not invent uncited guidelines.

## Non-interchangeability

OE-style A–D letters are **not** the same as:

- GRADE High/Moderate/Low/Very Low  
- Guideline letter codes inside `1A`/`1B` schemes  
- Oxford CEBM Levels 1–5  

Never present a conversion table as equivalence.

## Reporting checklist

1. Gradeability gate → U if needed  
2. Question type + claim  
3. Quality / Certainty / Relevance one-liners  
4. Ceiling + up/down reasons (or “insufficient body”)  
5. Final `A–D±` or `U`  
6. Mandatory non-official disclaimer  
