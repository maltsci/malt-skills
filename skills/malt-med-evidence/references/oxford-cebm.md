# Oxford CEBM Levels of Evidence (2011)

Source of truth: Oxford Centre for Evidence-Based Medicine, **The Oxford 2011 Levels of Evidence**  
https://www.cebm.ox.ac.uk/files/levels-of-evidence/cebm-levels-of-evidence-2-1.pdf

Levels navigate **which study designs are most appropriate for a question type**. They are **not** automatic quality grades and **not** treatment recommendations.

## Required first step

Identify **question type** before assigning a level:

- Therapy / prevention / symptom relief
- Diagnosis (diagnostic accuracy)
- Prognosis
- Etiology / harm (common exposure)
- Screening (if clearly a screening question; otherwise treat as therapy or diagnosis)

If question type remains unclear after one clarification, **omit Oxford** rather than guess.

## Therapy / Prevention / Harm (interventions)

| Level | Typical design |
| --- | --- |
| 1a | Systematic review (SR) of RCTs with homogeneity |
| 1b | Individual RCT with narrow confidence interval |
| 1c | All-or-none case series |
| 2a | SR of cohort studies with homogeneity |
| 2b | Individual cohort (including low-quality RCT; e.g. <80% follow-up) |
| 2c | “Outcomes” research; ecological studies |
| 3a | SR of case-control studies with homogeneity |
| 3b | Individual case-control study |
| 4 | Case series (and poor-quality cohort / case-control) |
| 5 | Expert opinion without explicit critical appraisal, or based on physiology / bench research |

**Notes**

- “All-or-none” (1c): before treatment all died / none had the outcome; after treatment some survive / some develop the outcome (dramatic historical observations).
- A single RCT is typically **1b**, not automatically 1a.
- Poor-quality RCTs may drop toward **2b** per OCEBM footnotes—state the quality concern in rationale.

## Diagnosis (diagnostic accuracy)

| Level | Typical design |
| --- | --- |
| 1a | SR of Level 1 diagnostic studies with homogeneity |
| 1b | Validating cohort study with good reference standards |
| 1c | Absolute SpPins and SnNouts |
| 2a | SR of Level >1 diagnostic studies |
| 2b | Exploratory cohort study with good reference standards |
| 3b | Non-consecutive study; or without consistently applied reference standards |
| 4 | Case-control study; or poor / non-independent reference standard |
| 5 | Expert opinion without explicit critical appraisal |

**Notes**

- Do **not** force therapy-RCT ordering onto diagnostic questions.
- Prefer designs that compare the index test with an appropriate reference standard in a relevant spectrum of patients.

## Prognosis

| Level | Typical design |
| --- | --- |
| 1a | SR of inception cohort studies with homogeneity |
| 1b | Individual inception cohort study with &gt;80% follow-up |
| 1c | All-or-none case series |
| 2a | SR of either retrospective cohort studies or untreated control groups in RCTs |
| 2b | Retrospective cohort study or follow-up of untreated control patients in an RCT |
| 2c | “Outcomes” research |
| 4 | Case series (and poor-quality prognostic cohort studies) |
| 5 | Expert opinion without explicit critical appraisal |

**Notes**

- Prefer **inception cohorts** (patients enrolled at a common, early point in disease).
- Incomplete follow-up and poorly defined start points lower the level.

## Etiology / Harm (common exposures) — condensed

When the question is about etiology or harmful exposure (not treatment benefit):

| Level | Typical design (OCEBM-aligned summary) |
| --- | --- |
| 1a | SR of RCTs (or of prospective cohort studies with homogeneity, depending on feasibility) |
| 1b | Individual RCT (or prospective cohort with dramatic effect when RCT infeasible—use caution and cite OCEBM footnotes) |
| 2a–2b | SR / individual cohort studies |
| 3a–3b | SR / individual case-control |
| 4 | Case series / poor-quality observational |
| 5 | Expert opinion / mechanism only |

If the exact OCEBM etiology cell is ambiguous from the abstract alone, assign the **closest conservative level** and say what information is missing.

## Grades of recommendation (Oxford) — optional only

OCEBM also defines recommendation grades A–D from consistency of levels. **This skill defaults to reporting Levels, not Oxford recommendation grades**, unless the user explicitly asks for Oxford recommendation grading **and** provides a body of evidence consistent enough to support it.

## How to report

- Output form: `Oxford CEBM Level X` (optionally `Xa`/`Xb`/`Xc`).
- Always name the **question type** and the **design matched**.
- State: Levels are design navigation, not proof of low risk of bias.

## Common mistakes to avoid

- Treating every RCT as Level 1 for diagnosis or prognosis questions.
- Equating Level 1 with GRADE High certainty.
- Upgrading a narrative review to Level 1 because it “cites RCTs.”
