# Phase 2: Worldbuilding Claim Extraction — Instructions

## Overview

You have a directory of markdown files, each containing a single "notes" entry from a conlanging/worldbuilding project called the **Boralverse**. Your task is to process each file and extract every **worldbuilding assertion** — that is, every factual claim about the alternate-history setting — into a structured YAML format.

The output will later be aggregated by entity and topic to populate a wiki, so completeness and atomicity matter more than prose quality.

---

## Background on the Boralverse

The Boralverse is an **alternate history of Earth**. The point of divergence is the existence of **Borland** (Borlish: *Istr Boral*), a large island in the North Sea between Great Britain and Denmark, inspired by the real-world existence of Doggerland. The primary language of Borland is **Borlish** (*Borallesc*), a Romance language descended from Latin but heavily influenced by Old English and Old Norse.

History is broadly identical to IRL until the fall of the Western Roman Empire, then diverges increasingly — first in northwestern Europe, and by 1000 CE across Eurasia and North Africa. The Americas are left identical to IRL until Old World contact (via Basque fishermen reaching Newfoundland in ~1470 CE).

The entries you are processing use a **Translation Convention**: they are mostly written in IRL English, but use Boralverse-specific proper nouns and occasional calques of Boralverse jargon (e.g. "threshold force" for nuclear power, "scitation" for exam, "tallath" for Welsh province). **IRL equivalents** are sometimes given in square brackets, e.g. "Mendeva [North America]", "Pojon [Bratislava]", "Morrack [Morocco]".

Key things to be aware of:
- **Polity names differ from IRL.** Vascony ≈ a polity spanning N Spain and SW France. Markland ≈ a polity based in the Midlands of England. The Drengot Collusion ≈ a late-19th/early-20th century alliance-federacy in NW Europe. Barcelon ≈ a kingdom in NE Spain. And so on. Do not assume a Boralverse polity maps exactly onto any IRL country.
- **Named periods** recur frequently: the Revitalist period (~16th c.), the Long Peace, the Global Workshop (industrialisation), the Good Game (late 19th c.), the Household Renovation (social shift re: marriage/family), the Millstone War (≈ a major early-20th c. conflict), the Intertwining Century (first century after contact with the Americas).
- **In-world works** (books, films, newspapers, academic texts) are frequently cited. These are fictional but internally consistent; treat their titles, authors, publication dates, and languages of composition as factual claims about the setting.
- Some entries are presented as **in-world documents** (newspaper articles, textbook excerpts, encyclopaedia entries, etc.). The framing is fictional, but the facts stated within them are canonical to the setting.

---

## What counts as a worldbuilding claim

A claim is any **atomic factual statement about the Boralverse setting**. This includes:

1. **A named entity exists** — a person, place, polity, organisation, work of writing, institution, technology, species, cultural practice, etc.
2. **An entity has a property** — a city is on a river, a person is a botanist, a book was published in 1991, a polity's capital is X.
3. **A relationship holds between entities** — a person founded an organisation, a polity is vassal to another, a region borders another, a book was written by a person.
4. **An event occurred** — a battle, a voyage, a founding, a discovery, a legislative act, with its date and participants.
5. **A process or trend** — a social movement, a spread of technology, a linguistic shift, a cultural fashion.
6. **A Boralverse-specific term or concept is defined** — "decimation" meaning a currency redenomination, "parachthon" as a narrative genre, "scitation" as an examination, etc.
7. **An IRL equivalent is given** — "Mendeva [North America]", "Brasil [Newfoundland]", "tartover" for potatoes, "threshold force" for nuclear power. These should use the `glossary` category (see below), and both the entity's `name` and `irl` fields must be populated.

**Do not extract:**
- Claims that are true of IRL and are not specific to the Boralverse (e.g. "Latin sacer means sacred" is just real-world etymology, not a worldbuilding claim — unless it's contextualised in a Boralverse-specific way).
- Purely linguistic information about Borlish — phonology (including pronunciation of specific terms), morphology, sound changes — unless it names a historical event, person, or cultural context (e.g. "the 1870 spelling reform" is a worldbuilding claim; "intervocalic lenition of /p/ to /v/" is not, and neither is IPA notation for individual words). Pronunciation data belongs in dedicated language notes.
- Your own inferences or speculations. Only extract what is explicitly stated or very directly implied.

---

## Output format

For each entry file, produce a YAML document with the following structure:

```yaml
entry: "X.Y"
title: "Entry Title"
source_work: "Name of the in-world source, if the entry is presented as an excerpt (otherwise omit)"
claims:
  - category: <category>
    claim: "<A single, self-contained factual sentence in your own words>"
    entities:
      - name: "<Entity name as it appears in the text>"
        irl: "<IRL equivalent, if given in brackets or clearly implied>"
        type: "<person|place|polity|organisation|work|event|period|technology|concept|other>"
    dates: ["<any dates mentioned, as strings>"]
    relationships:
      - subject: "<Entity A>"
        predicate: "<verb phrase>"
        object: "<Entity B>"

  - category: <category>
    claim: "..."
    ...
```

### Field details

**category** — use one of the following:
- `person` — a named individual and their attributes
- `place` — a city, region, geographical feature, or settlement
- `polity` — a state, kingdom, empire, alliance, or political entity
- `event` — a specific happening with a date or period (battle, founding, voyage, legislative act)
- `period` — a named historical era or movement
- `organisation` — a company, guild, institution, school, religious order
- `work` — a book, film, newspaper, academic text, or other creative/scholarly work
- `technology` — an invention, scientific discovery, or technical concept
- `economics` — currency, trade, markets, economic policy
- `culture` — customs, sports, fashion, games, social practices
- `terminology` — a Boralverse-specific term or jargon word defined or explained in setting-internal terms (e.g. "parachthon" as a narrative genre, "decimation" as currency redenomination, "scitation" as an examination, "terrene tax" as a land tax). Use `glossary` instead for any term defined by explicit reference to its IRL equivalent.
- `glossary` — a Boralverse-specific term, name, or concept defined explicitly by its real-world (IRL) equivalent. Use this for any claim of the form "X is the Boralverse term/name/equivalent for [IRL thing]", or when the source gives a bracketed IRL gloss (e.g. "Mendeva [North America]", "tartover" for potatoes, "threshold force" for nuclear power). These are the only claims that explicitly acknowledge IRL as a reference frame. Both the entity's `name` and `irl` fields must be filled for every `glossary` claim.
- `language` — a claim about a language (its history, prestige, speakers, loanwords) as opposed to its internal grammar
- `law` — legal principles, acts of legislation, governance structures
- `religion` — religious movements, institutions, theology
- `military` — armies, battles (as institutions rather than events), strategy

If a claim could fit multiple categories, pick the most specific one. A battle is an `event`; the existence of a standing army is `military`.

**entities** — list every proper noun (person, place, polity, work title, organisation, etc.) mentioned in the claim. Include:
- `name`: as it appears in the source text
- `irl`: the IRL equivalent if one is given or clearly implied (e.g. "Newfoundland" for "Brasil", "Morocco" for "Morrack"). If none, omit this field.
- `type`: one of `person`, `place`, `polity`, `organisation`, `work`, `event`, `period`, `technology`, `concept`, `other`

**dates** — list all dates mentioned in the claim, as strings. Use the forms given in the text: "1471", "c. 16th century", "1810s", "late nineteenth century", etc. If no dates, omit.

**relationships** — if the claim asserts a relationship between two or more entities, express it as subject-predicate-object triples. For example:
```yaml
relationships:
  - subject: "Barcelon"
    predicate: "conquered"
    object: "Tolose"
```
If the claim is a simple property of one entity (e.g. "Florence is the capital of Tuscany"), you can express this as a relationship with the property as object, or simply let the claim text carry it. If no notable relationships, omit.

### Atomicity

Each claim should be **one fact**. If a sentence in the source contains two independent facts, split them. For example, the sentence:

> "Tewis Camigner (fl. c16) was a botanist from Willemy during the Revitalist period, sometimes called the father of farm theory."

yields at least:

```yaml
- category: person
  claim: "Tewis Camigner was a botanist active in approximately the 16th century."
  entities:
    - name: "Tewis Camigner"
      type: person
  dates: ["c. 16th century"]

- category: person
  claim: "Tewis Camigner was from Willemy."
  entities:
    - name: "Tewis Camigner"
      type: person
    - name: "Willemy"
      type: place
  relationships:
    - subject: "Tewis Camigner"
      predicate: "was from"
      object: "Willemy"

- category: person
  claim: "Tewis Camigner is sometimes called the father of farm theory."
  entities:
    - name: "Tewis Camigner"
      type: person
    - name: "farm theory"
      type: concept

- category: period
  claim: "Tewis Camigner was active during the Revitalist period."
  entities:
    - name: "Tewis Camigner"
      type: person
    - name: "Revitalist period"
      type: period
```

You may find it natural to keep two very closely bound facts together (e.g. "X founded Y in [date]" as one claim rather than two), and that's fine — use your judgement. The goal is that each claim can be filed under a wiki article for any of its entities without losing essential context.

---

## Worked example

Given the following entry:

```
171.5: Novomundine Landfall
The Novomundine Landfall (Borlish Abanc Novomondin) occurred in 1471 N, when
a ship that was part of a New Navarre Enterprise fishing expedition in the
North Atlantic sighted and made landfall on the island of Brasil [Newfoundland].
It marks the start of prolonged contact between the Vetomund [Afroeurasia] and
the Novomund [Americas] ...
```

The expected output begins:

```yaml
entry: "171.5"
title: "Novomundine Landfall"
claims:
  - category: event
    claim: "The Novomundine Landfall occurred in 1471, when a New Navarre Enterprise fishing expedition made landfall on Brasil."
    entities:
      - name: "Novomundine Landfall"
        type: event
      - name: "New Navarre Enterprise"
        type: organisation
      - name: "Brasil"
        irl: "Newfoundland"
        type: place
    dates: ["1471"]
    relationships:
      - subject: "New Navarre Enterprise"
        predicate: "conducted the expedition that caused"
        object: "Novomundine Landfall"

  - category: terminology
    claim: "The Borlish term for the Novomundine Landfall is 'Abanc Novomondin'."
    entities:
      - name: "Novomundine Landfall"
        type: event

  - category: glossary
    claim: "Vetomund is the Boralverse name for Afroeurasia (the Old World)."
    entities:
      - name: "Vetomund"
        irl: "Afroeurasia"
        type: place

  - category: glossary
    claim: "Novomund is the Boralverse name for the Americas."
    entities:
      - name: "Novomund"
        irl: "the Americas"
        type: place

  - category: event
    claim: "The Novomundine Landfall marks the start of prolonged contact between the Vetomund and the Novomund."
    entities:
      - name: "Novomundine Landfall"
        type: event
      - name: "Vetomund"
        irl: "Afroeurasia"
        type: place
      - name: "Novomund"
        irl: "the Americas"
        type: place
```

...and so on through the rest of the entry, covering the Intertwining Century, the etymology of "Mendeva", the Vascon Ascendancy, Ambrose III, Munir al-Hamdawi, the New World Company, Princess Alexandra, Paratzon, sandrine/vitamin C, scurvy, and guy-conies.

---

## Processing instructions

### Input

You will be given the notes entry files one at a time (or in small batches if the files are short). Each file contains the full text of one entry, beginning with its header line (e.g. `169.5: Time for T`).

### For each entry, do the following:

1. **Read the entire entry carefully.** Notes entries are dense; almost every sentence contains at least one claim.

2. **Identify all named entities** (proper nouns, titles of works, named periods, coined terms). Make a mental list before you begin writing claims — this helps avoid missing relationships between entities mentioned in different sentences.

3. **Extract claims atomically.** Work through the entry roughly in order, but don't be afraid to split or reorder for clarity. Each claim should be a single, self-contained factual sentence.

4. **Record IRL equivalents.** Whenever square brackets give an IRL equivalent (e.g. "[Bratislava]"), or when the equivalent is clearly implied (e.g. "Gaul" for France is a recurring convention), include it in the entity's `irl` field.

5. **Don't skip "obvious" geography.** If the text says "Tolose is a city and region in the south of Gaul", that's a claim about Tolose's location. Even if you think this is well-established elsewhere in the project, extract it — the aggregation step will handle deduplication.

6. **Preserve uncertainty and hedging.** If the source says "it is unknown why she undertook the voyage", your claim should reflect that uncertainty. Don't invent precision.

7. **Note in-world source framing.** If the entry is presented as an excerpt from a named in-world work (newspaper, textbook, etc.), record that work in the `source_work` field at the top level. The claims within are still canonical facts about the setting.

### Output

Produce one YAML document per entry. Use the filename pattern:

```
{entry_id}_claims.yaml
```

e.g. `169.5_claims.yaml`, `171.5_claims.yaml`.

If an entry contains **no worldbuilding claims** (unlikely for notes, but possible), produce:

```yaml
entry: "X.Y"
title: "Entry Title"
claims: []
```

### Batch size

If you are processing multiple files per conversation turn, aim for roughly **3–5 entries per turn** for notes-type entries, which tend to be dense. Prioritise thoroughness over speed. It is much better to extract one too many claims than to miss one.

---

## Common pitfalls

- **Overlooking relationships.** "Tolose was conquered by Vascony from the west in the fifteenth century" contains a relationship (Vascony conquered Tolose), a date (15th century), and an implicit geographical claim (Vascony is to the west of Tolose). Extract all three.

- **Merging distinct claims.** "Prince Mark of Tolose, heir to the Vascon throne who predeceased his father in 1453" contains: (a) Mark was a prince of Tolose, (b) he was heir to the Vascon throne, (c) he predeceased his father, (d) he died before or in 1453. These are four claims.

- **Ignoring the framing.** If the entry says "excerpt from the 1986 work *Birds Yet Sing* by Ivainchuque fi Cap", then the existence of that work, its author, its date, its original language, and its subject matter are all claims — even before you get to the content of the excerpt.

- **False negatives on terminology.** Boralverse-specific jargon deserves `terminology` claims. If the text uses "parachthon" for a narrative genre, "scitation" for an exam, "astraphor" for electricity, "decimation" for currency redenomination — these are all claims about the setting's vocabulary.

- **Confusing Boralverse polities with IRL countries.** "Britain" in the Boralverse is specifically the Kingdom of Britain (composed of Wales, its tallaths, Kernow, and Sodrick) — not the IRL United Kingdom. Don't add an `irl` gloss unless the text provides one or the equivalence is explicitly established.

- **Conflating `terminology` and `glossary`.** Both involve defining terms, but `terminology` is for in-world definitions (what the term means *within the Boralverse*), while `glossary` is for fourth-wall claims anchoring a Boralverse term to an IRL equivalent. "Parachthon is a narrative genre about..." is `terminology`; "Tartover is the Boralverse term for potatoes" is `glossary`. A useful test: could this claim appear in a Boralverse encyclopedia without breaking the fictional frame? If not — because it explicitly references IRL — it is `glossary`.

- **Extracting IRL etymology as a worldbuilding claim.** When a Boralverse term's origin is traced back through IRL languages (e.g. "French *reveillon* is from Latin *evigilō*"), that is IRL knowledge, not a Boralverse claim. Only extract the Boralverse end of the chain: the fact that a Boralverse term derives from a given source language is a `language` claim; the IRL semantics and history of the source word are not.

- **Filing title translations as `terminology`.** When an entry gives an English translation of a work's title (e.g. "'Et Nous Amerons les Fux' (And We Will Love the Fire)"), this is a property of the work, not a terminology claim. File it as a `work` claim. If the English title itself provides an IRL-equivalent gloss for what the work is about, you may additionally file a `glossary` claim.

---

## Prompt template

If you need a concise system prompt to initialise a session, use the following. The full instructions above should be provided as a reference document alongside it.

```
You are a worldbuilding research assistant. You are helping to process notes
from the Boralverse, an alternate-history conworlding project. Your task is
to extract every worldbuilding assertion from each entry into structured YAML,
following the schema and instructions in the reference document provided.

Be thorough and atomic: one fact per claim. Preserve uncertainty where the
source is uncertain. Record IRL equivalents when given. Do not skip seemingly
minor facts — the output will be aggregated across hundreds of entries, and
completeness matters more than brevity.

Process the following entry:
```

Then paste or attach the entry text.
