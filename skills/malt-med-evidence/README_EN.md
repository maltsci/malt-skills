# malt-med-evidence

Medical evidence appraisal skill: structured grades for a DOI / PMID / abstract / PICO or clinical claim.

**Stage:** Read & Ask  
**Repo:** [maltsci/malt-skills](https://github.com/maltsci/malt-skills) · [中文](README.md)

## What it does

- Default frameworks: **Oxford CEBM** + **GRADE**
- Optional: evidence pyramid, OpenEvidence-style heuristic (A–D± / U)
- **Single-study mode** (default): design navigation + coarse GRADE-style estimate (with disclaimer)
- **Body-of-evidence mode:** formal GRADE for one named critical outcome

Report language follows the user prompt. Chat-only output; **not clinical advice**.

## Inputs / outputs

| Inputs | Outputs |
| --- | --- |
| DOI, PMID, abstract, methods blurb, PICO, claim | One-line verdict, grade table, short rationale, limits |

On DOI/PMID, the skill runs `scripts/fetch_literature.py` in this folder for metadata and abstract.

## Dependencies

- Python 3
- Network (PubMed / Crossref)
- Optional: `NCBI_EMAIL`

```bash
python3 scripts/fetch_literature.py --pmid 32970396
python3 scripts/fetch_literature.py --doi 10.1056/NEJMoa2024816
```

## Non-goals

- No OpenEvidence website / cookie automation
- No treating grades from different systems as interchangeable
- No individualized treatment or dosing advice
- No dependency on other skills outside this package

## Layout

- `SKILL.md` — agent instructions
- `references/` — Oxford / GRADE / pyramid / OE heuristic
- `scripts/fetch_literature.py` — literature fetch
- `evals/evals.json` — evaluation cases

## License

Same as the repo: [Apache-2.0](../../LICENSE)
