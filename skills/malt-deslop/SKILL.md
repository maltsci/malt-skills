---
name: malt-deslop
description: Rewrites Chinese, English, and bilingual prose to remove predictable LLM writing tells while preserving claims, facts, register, and author voice. Use whenever a user asks to “deslop,” “de-AI,” “humanize,” remove “AI-isms,” “AI cadence,” “GPT-isms,” or text that “sounds like ChatGPT”; or uses Chinese requests such as “去 AI 味”“去AI味儿”“去机感”“像人写的”“去掉一眼 AI”. Apply to drafts, papers, reports, essays, posts, scripts, newsletters, and product copy. Do not use this to promise detector evasion or to flatten deliberate literary or technical writing into casual speech.
---

# malt-deslop

Edit prose so it sounds like a person chose the words, rather than a model completing a familiar pattern. The target is not more decoration or forced informality. Remove formulaic rhetoric, empty emphasis, synthetic certainty, and performative emotion while keeping the writer’s actual point.

**Surface patterns are evidence, not proof.** One em dash, contrast, formal phrase, or marker word does not make text AI-written. Act when patterns cluster, replace real meaning, or produce a conspicuously repetitive cadence.

## Read the right references

Read [references/patterns.md](references/patterns.md) before rewriting. Read [references/lexicon.md](references/lexicon.md) for a Chinese-specific wording pass. For English or bilingual academic prose, also read [references/english-markers.md](references/english-markers.md).

## Workflow

1. **Anchor the meaning.** State in one or two plain sentences what the passage claims and which facts, numbers, names, quotations, citations, and qualifications cannot change.
2. **Choose the register.** Preserve the appropriate register: essay, academic paper, technical documentation, email, script, or product copy. Desloping is not a request to turn every text into chatty prose.
3. **Fix mechanisms before vocabulary.** Remove false contrasts, narrator warm-ups, fake questions, empty triads, unjustified metaphors, and generic conclusions. Use word lists only to catch what remains.
4. **Rebuild from the point.** Do not produce a thesaurus rewrite. Change sentence structure and information order where needed, then make the claim concrete.
5. **Audit once.** Recheck the rewritten text against the relevant reference files. If it can still be read fluently as a generic explainer script with no specific information, rewrite from the anchored meaning again.

## What to target first

| Pattern | Typical signal | Better move |
| --- | --- | --- |
| False contrast | “It is not X; it is Y.” | State the true claim directly, or give a concrete contrast with consequences. |
| Fake dialogue | “But here is the question …” | Use a direct statement or a useful transition. |
| Presenter warm-up | “Let’s unpack this once and for all.” | Start with the substance. |
| Decorative symmetry | “Faster, cheaper, smarter.” | Keep only supported reasons; do not manufacture a three-part list. |
| Empty metaphor | “The scalpel, not the hammer.” | Name the action, constraint, or outcome. |
| Inflated or dramatic close | “This changes everything.” | End with a concrete result, recommendation, or unresolved question. |
| Marker-word cluster | `delve`, `pivotal`, `showcase`, or Chinese formulae in a dense cluster | Use a plainer verb or supply the missing specific information. |

## Boundaries

- Preserve source facts. Do not invent examples, figures, personal reactions, citations, or a fictional “human” backstory.
- Preserve deliberate rhetoric when it performs real work. Do not remove an intentional contrast, a necessary literary scene, or discipline-specific terminology simply because it resembles a listed pattern.
- Do not add typos, slang, emojis, filler, or artificial imperfections to simulate human authorship.
- Do not claim that the output is undetectable, will bypass a detector, or proves human authorship. Writing detectors are unreliable and this skill is an editorial aid, not an authorship test.
- When the user does not request an analysis, return the revised prose first. Add at most three short notes about material edits.

## Output

For a rewrite request, provide the revised text in the original format. Keep headings, citations, quotations, Markdown links, and structured data intact unless the user asks to change them.

For an audit-only request, list only the meaningful patterns, quote the relevant span, explain why it is a problem in context, and offer a concrete revision direction. Do not label harmless isolated phrases as defects.
