# English LLM style markers

This reference summarizes English words whose use rose unusually in LLM-associated scientific prose research. It is a corpus-level signal, not a list of forbidden words and not an authorship detector.

The underlying vocabulary is from Kobak et al., *Science Advances* (2025), with an expanded 2024 list reported by Holzwarth, González-Márquez, and Kobak (arXiv:2608.10715). Consult the public lists in [kobaklab/llm-usage-in-pmc](https://github.com/kobaklab/llm-usage-in-pmc) and [berenslab/llm-excess-vocab](https://github.com/berenslab/llm-excess-vocab) when the complete inventory is required.

## How to use it

1. Repair meaning, structure, and argument first. A direct, specific sentence matters more than swapping a word.
2. Look for clusters of high-signal words or repeated word families in a paragraph.
3. Do not rewrite ordinary functional words solely because they occur on a frequency list.
4. Do not replace one marker with another marker. Choose the clearest word for the context.

## High-signal words and plainer options

| Marker | Revision direction |
| --- | --- |
| `delve into` | `examine`, `study`, `look at` |
| `underscore` | `show`, `make clear`, `emphasize` |
| `showcase` | `show`, `present` |
| `intricate` | `complex`, or name the structure |
| `meticulous` | `careful`, `in detail` |
| `pivotal`, `crucial` | `important`, or explain why it matters |
| `comprehensive` | `full`, `complete`, or specify coverage |
| `leverage`, `harness` | `use` |
| `foster` | `support`, `encourage` |
| `elucidate` | `explain` |
| `encompass`, `encapsulate` | `include`, `cover` |
| `groundbreaking`, `transformative`, `unparalleled` | Delete unless the stated change justifies it. |
| `realm` | `field`, `area` |
| `unveil` | `report`, `show` |
| `additionally`, `notably`, `particularly` | `and`, `also`, or delete |
| `findings` | `results` when that is the more direct noun |

Other frequent high-signal examples include: `multifaceted`, `nuanced`, `leveraging`, `harnessing`, `fostering`, `encompassing`, `adept`, `poised`, `seamlessly`, `illuminating`, and `orchestrating`.

## Low-signal words

Do not flag `these`, `this`, `their`, `into`, `like`, `need`, `research`, `both`, `across`, `through`, `while`, `within`, or `using` in isolation. They appear in the corpus list because of changing frequency, not because any one occurrence is unnatural.

Similarly, words such as `exhibited`, `additionally`, `within`, `insights`, `across`, `particularly`, and `enhancing` need contextual judgment. A cluster may merit a rewrite; one ordinary use does not.

## Avoid mechanical cleanup

- Do not remove `research`, `findings`, or `methods` from academic prose merely to lower a style score.
- Do not replace `these` with unnatural alternatives such as “the aforementioned.”
- Do not turn every verb into `do` or `make`; that creates a different kind of flat, translated prose.
- Do not assert that changing these words makes a text human-written or undetectable.
