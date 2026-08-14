# GRADE Certainty of Evidence

Primary references:

- GRADE Working Group overview: https://book.gradepro.org/guideline/overview-of-the-grade-approach
- GRADE Handbook: https://gradepro.org/handbook/
- Cochrane Handbook Chapter 14 (completing ‘Summary of findings’ tables / GRADE): https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14

GRADE rates **certainty of a body of evidence for a specific PICO question and outcome**. It does **not** stamp a single paper as “GRADE High” in formal guideline practice.

## Certainty labels

| Certainty | Meaning |
| --- | --- |
| High | Very confident the true effect lies close to the estimate |
| Moderate | Moderately confident; true effect likely close but may differ substantially |
| Low | Limited confidence; true effect may differ substantially |
| Very Low | Very little confidence; true effect likely differs substantially |

High certainty ≠ large benefit. Separate **effect size** from **certainty**.

## Body-of-evidence procedure (formal path)

Use when mode = **Body-of-evidence**, with **one critical outcome** named.

### 1. Starting point (typical intervention questions)

| Evidence base | Usual start |
| --- | --- |
| RCTs | High |
| Observational studies | Low |
| Case reports / case series alone | Not a formal GRADE start for efficacy; treat as signals |

### 2. Downgrade domains (each may −1 or −2)

1. **Risk of bias** — randomization, allocation concealment, blinding, attrition, selective reporting, etc.
2. **Inconsistency** — unexplained heterogeneity of direction/magnitude across studies.
3. **Indirectness** — population, intervention, comparator, or outcome differ from the question.
4. **Imprecision** — wide CIs, small sample / few events, fragile results.
5. **Publication bias** — suspected missing negative/unpublished studies.

If a domain cannot be assessed from available materials, write **Unable to assess** — do not silently assume “no problem.”

### 3. Upgrade factors (observational bodies only; formal path)

- Large magnitude of effect
- Dose–response gradient
- Residual confounding would likely reduce the observed effect (strengthening inference)

Document why an upgrade applies. Do not upgrade casually.

### 4. Recommendation strength (optional; not default)

GRADE separates **certainty** from **recommendation strength** (Strong vs Conditional).  
This skill **defaults to certainty only**. Report Strong/Conditional only if the user supplies recommendation context plus an evidence summary that supports it. Do **not** invent guideline codes like `1B`.

### 5. Guideline codes like `1B`

Many adapted systems encode “1 = strong recommendation, B = moderate evidence,” but coding is **guideline-specific**. If the user only pastes `1B` without PICO/evidence tables:

1. Explain that the code mixes recommendation + evidence quality in that guideline’s scheme.
2. Do **not** reverse-map it into Oxford Levels or a new GRADE rating without the underlying evidence summary.

## Single-study coarse estimate (default single-study mode)

Allowed when only one study (or one abstract) is available. This is a **GRADE-style estimate**, not a formal body-of-evidence rating.

### Allowed

- Set a **starting point** from design (RCT → High start; observational → Low start; case report/series → treat as Very Low / not a formal start and explain).
- Consider **risk of bias**, **indirectness**, and **imprecision** *as far as the abstract/methods allow*.
- Label output explicitly as coarse.

### Forbidden

- Pretending **inconsistency** or **publication bias** were assessed across a body of evidence.
- Applying **formal GRADE upgrading** rules to a single study. If a large effect is noted, mention it **narratively** without raising the certainty label via upgrade machinery.
- Claiming the result is a guideline-panel GRADE rating.

### Mandatory disclaimer (include whenever single-study GRADE is shown)

> Single-study GRADE-style estimate — not a formal GRADE certainty rating of a body of evidence.

### Suggested reporting pattern

1. Starting point from design  
2. Domains applied / unable to assess  
3. Resulting coarse certainty  
4. Disclaimer above  

## Body mode with only one study

Offer to:

- Switch to **single-study coarse** appraisal, or  
- Wait for additional studies / a systematic review summary  

Do not silently run “formal body GRADE” on one paper.

## Multiple outcomes

Formal GRADE is **per outcome**. If several outcomes are listed, ask which **one** critical outcome to grade first.
