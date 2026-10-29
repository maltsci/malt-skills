---
name: malt-writing-style
description: "Distill an editable writing-style guide from user-provided articles, then apply a specified style.md to draft prose. Use this whenever the user asks to extract, infer, analyze, distill, summarize, or make a style guide from several writing samples; asks to create writing_style.md/style.md; or asks to rewrite, edit, polish, or draft according to a supplied style guide. Trigger for English and Chinese requests such as “提炼写作风格”, “从这些文章总结文风”, “做一个 style.md”, “按 style.md 改写”, “应用文风”, “distill a writing style”, “create a style guide from these essays”, or “apply this style guide”. Do not override a separate style guide explicitly selected by the user, or a request solely to remove AI-sounding phrasing."
---

# malt-writing-style

Turn representative samples into an editable, evidence-backed `style.md`, then use that guide to steer a new draft or a rewrite. This is an iterative constraints workflow inspired by Paul Goldsmith-Pinkham’s approach: observed patterns become a guide; human revision makes the guide sharper; the guide is supplied in full when writing.

The guide can make a result recognizably closer to a body of work. It cannot capture a person exactly, prove authorship, or justify inventing experiences, facts, or private details.

## Choose the workflow

Use **Distill a style** when the user supplies several sample articles (as files, links already available locally, or pasted text) and wants a reusable guide.

Use **Apply a style** when the user supplies both:

1. a specific style-guide file such as `style.md`; and
2. the text to create, rewrite, or edit.

If either required input is missing, ask for it. Do not substitute a remembered author style or a generic “good writing” checklist.

Read [references/style-template.md](references/style-template.md) before either workflow. It provides the shared dimensions and the expected output structure.

## Workflow 1: Distill a style

### 1. Establish the sample boundary

Read every supplied sample before drafting the guide. Record, at minimum:

- the number of samples;
- their languages;
- their genres and intended situations;
- whether they plausibly belong to one register or several.

Treat the samples as evidence, not as a license to fill gaps with stereotypes about their author or topic. Ignore front matter, navigation, bibliographies, and editorial boilerplate unless they are clearly part of the writer’s repeated practice.

When samples have materially different registers, such as internal directives and public essays, do one of the following:

- keep one guide and clearly state the context for each pattern when the differences are complementary; or
- create separate, named guides when rules conflict enough that applying both would be misleading.

Do not split a guide merely because sentence length or subject matter varies from article to article.

### 2. Extract only supported patterns

Use the template’s sections as a lens, not a quota. Before drafting rules, build a compact source ledger: list each sample’s source label, genre or register, and the short passages that support a possible rule. The ledger is the check against invented coverage claims.

Include a rule only if it is supported by:

- a short quotation with a source label; or
- a careful frequency observation, such as “appears in 7 of 10 sampled pieces.”

Write an exact frequency only after listing the matching sample labels in the ledger. If you did not count it, write “observed in multiple samples,” not a number. In the finished guide, attach an `Evidence:` note with source labels to every core rule. Distinguish stable choices from one-off content:

- “often begins with a concrete conflict before issuing a judgment” can be a style rule;
- “often writes about a particular campaign” is subject matter unless it controls the writing method.

Record stable absences as anti-patterns only when the samples give real evidence of avoidance or explicit contrast. Do not fill the anti-pattern list with generic advice about AI writing.

### 3. Write the guide

Write the guide in English by default. Preserve the original language for quotations, phrase examples, proper nouns, and punctuation examples. For instance:

> 先肯定再转折：“文章本身很好。……只是我隐约觉得有失偏颇。”

Follow the template’s section order, but omit sections without evidence:

- omit **III. Presentation Patterns** unless the samples contain visual presentation material, slide design, or explicit delivery directions;
- omit notation conventions when the samples contain no notation;
- omit a genre-specific subsection when it has no distinct, repeatable pattern.

Every guide must contain:

- **Scope** that names supported and unsupported contexts;
- a compact **Evidence Ledger** that maps core patterns to their source labels;
- evidence-backed **Writing Style Patterns**, **Structural Approach**, **Distinctive Voice**, **Application Checklist**, and **Anti-Patterns**;
- 3 to 6 short **Verbatim Anchors**, in the original language;
- **Draft Notes** for uncertain inferences and sample gaps.

Anchors calibrate choices; they are not a phrase bank. State this directly so a later writer does not transplant source-specific names, incidents, or wording.

### 4. Save and report

The default filename is `style.md`.

- If the user specifies a filename or path, use it.
- If all source files share a directory, save alongside them.
- If the input is pasted text, or files do not share a directory, save in the current workspace.
- If the chosen output already exists, do not overwrite it without the user’s explicit approval.

After saving, give a short report: output path, represented registers, whether a guide was split, and the most important `Draft Notes` for human review. Explain that the guide is an editable constraint set, not a personality clone.

## Workflow 2: Apply a style

### 1. Read and bound the task

Read the entire user-specified guide, including its checklist and anti-patterns. Treat its `Draft Notes` as hypotheses rather than hard requirements.

Before changing prose, anchor the content that cannot change:

- facts, names, numbers, quotations, citations, links, and stated conclusions;
- uncertainty, causality, and scope limits;
- the requested format and target language.

Do not import events, references, catchphrases, names, places, or political positions from the guide’s source samples. A style guide controls how the text moves and sounds, not what facts it may claim.

### 2. Check register fit

Compare the draft’s genre, audience, and stakes with the guide’s Scope section.

- First classify the guide’s instructions:
  - **Structural:** information order, reasoning sequence, paragraph function, and degree of explicitness.
  - **Cadence:** sentence movement, transitions, paragraph length, and reader guidance.
  - **Surface:** catchphrases, rhetorical questions, repetition, idioms, punctuation signatures, historical allusions, and command tone.
- If genres fit, apply structural rules first, then cadence and surface rules that serve the task.
- If they partly fit, transfer structural rules by default. Add cadence only when it suits the target register. Do not transfer surface signals merely to make the result visibly “styled”; give one short note about the limit.
- If they do not fit, ask whether to proceed with the transferable rules or use another guide.

Never turn a cautious scientific paragraph into an assertion of causation just because the source style is forceful. Preserve the source text’s evidentiary status.

For scientific, legal, medical, technical, or other high-precision prose, preserve the discipline’s normal register. Unless already present in the source draft or required by the target genre, do not introduce rhetorical questions, slogans, historical analogies, theatrical contrasts, or a command voice.

### 3. Rewrite from meaning, not from a phrase list

Apply the guide in this order:

1. Rebuild the opening and progression around the guide’s observed structure.
2. Transfer structural choices before cadence or surface choices.
3. Adjust directness, reasoning rhythm, sentence movement, and reader guidance only to the degree the target register supports.
4. Use supported transitions, punctuation, emphasis, and vocabulary patterns where they genuinely fit.
5. Check every relevant item in the Application Checklist and avoid the guide’s Anti-Patterns.
6. Re-read the draft against the content anchors from step 1.

Do not imitate individual anchors word for word. Do not add ornamental “style signals” just to make the result more conspicuous.

For Chinese output, use Chinese double quotation marks “”, unless the supplied style guide has clear contrary evidence or the user requests another convention.

### 4. Deliver the result

By default, return the rewritten text first and preserve headings, Markdown, citations, quotations, and links. Add at most three short notes only when they clarify a material register constraint or a meaningful structural change.

If the user asks for **comments only**, do not rewrite. Give concise inline or section comments that identify weak reasoning or departures from the guide and explain a revision direction. This editing mode is often better when the user wants to retain their own voice.

If the user asks to save the rewritten text, write it to their requested file. Otherwise, do not create a new draft file merely because a rewrite was requested.

## Boundaries

- Do not infer a complete voice from one short sample. Identify the limitation and ask for more material when it changes the reliability of the guide.
- Do not fabricate quotations, sources, metrics, personal experiences, or editorial history.
- Do not promise a perfect voice clone, detector evasion, or proof that a text belongs to a person.
- Do not silently merge samples from unrelated authors. Ask the user whether they want a blended guide and label it as such.
- Do not override a separate writing guide explicitly selected by the user, a translation task, or a request solely for de-AI editing. Combine workflows only when the user clearly asks for both.
