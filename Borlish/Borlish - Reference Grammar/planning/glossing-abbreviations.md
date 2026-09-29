# Glossing abbreviations

The standard set for the reference grammar: the Leipzig Glossing Rules plus five Borlish additions (AGT, CMPR, COLL, DSJ, POT), defined in `preamble.tex`. In the tex, write grammatical glosses with the macros, braced so that expex treats each gloss word as a unit, e.g. `{swim-\Inf} {\Def=time} {get-\First\Pl}`. The list in the Conventions chapter is generated automatically and shows only the abbreviations actually used.

The last column of the table records the variants found in Scaunç glosses. Normalising Scaunç to this standard is a separate, later job.

## Principle: gloss only what the form distinguishes

A category is glossed only where it corresponds to a difference in form.

- **Bare verb stems** get the meaning alone: *nað* 'swim', not 'swim.SG'. Endings are glossed as usual: *nascn* 'sail.3PL'.
- **Pronouns** carry a case label only where their form differs from the subject form, and a form shared by two cases takes the less specific label:
  - *jo* 1SG, *me* 1SG.OBL (accusative and oblique are the same form)
  - *le* 3SG.M (subject and accusative are the same form), *luy* 3SG.OBL (all three genders)
  - *ðe* 3PL, *lou* 3PL.ACC, *lour* 3PL.OBL (all three differ, so ACC is needed here)
- **Exception, disjunctive use:** a pronoun in disjunctive use is always glossed DSJ, even when the form is shared with another case. So *mey* 1SG.DSJ, *luy* 3SG.DSJ, *lou* 3PL.DSJ, and *nos* 1PL.DSJ, *vos* 2PL.DSJ (though *nos* and *vos* are the same as the subject forms). The Leipzig list has no standard label for disjunctive pronouns; DSJ is our addition, and DISJ is also seen in the literature.
- **Gender** is glossed on the 3SG pronouns that show it: *le* 3SG.M, *la* 3SG.F, *lo* 3SG.N, but *luy* 3SG.OBL or 3SG.DSJ.

## Personal pronoun paradigm

Forms are from the lexicon and the user's answers of 2026-09-29. Cells marked ? are inferred rather than confirmed. The gloss for each form is in the last column; where two glosses are given, the choice depends on how the form is used.

| | Subject | Accusative | Oblique | Disjunctive | Poss. pronoun | Glosses |
|---|---|---|---|---|---|---|
| 1SG | jo | me | me | mey | mien | jo 1SG, me 1SG.OBL, mey 1SG.DSJ |
| 2SG | tu | te? | te | tey | tien | tu 2SG, te 2SG.OBL, tey 2SG.DSJ |
| 3SG.M | le | le | luy | luy | sien | le 3SG.M, luy 3SG.OBL / 3SG.DSJ |
| 3SG.F | la | la | luy | luy | sien | la 3SG.F |
| 3SG.N | lo | lo? | luy | luy | ? | lo 3SG.N |
| REFL | – | se | se? | sey | – | se REFL, sey REFL.DSJ |
| 1PL | nos | nos | nos | nos | nostr | nos 1PL / 1PL.DSJ |
| 2PL (also formal 2SG) | vos | vos | vos | vos | vostr | vos 2PL / 2PL.DSJ |
| 3PL | ðe | lou | lour | lou | lour | ðe 3PL, lou 3PL.ACC / 3PL.DSJ, lour 3PL.OBL / 3PL.POSS |

Possessive pronouns (*mien* 'mine' …) are glossed POSS, e.g. *mien* 1SG.POSS. *lour* is glossed by function: 3PL.OBL as an oblique pronoun, 3PL.POSS for 'theirs'. The possessive determiners (*my, ty, sy, nossy, vossy, lorry*) are also POSS.

## Table

| Category | Standard | Macro | Scaunç variants |
|---|---|---|---|
| person + number | 1SG … 3PL | `\First\Sg` … `\Third\Pl` | 1s 2s 3s 1p 2p 3p 3pl |
| bare verb stem | *(no gloss)* | – | s (*swim.s*) |
| gender (3SG pronouns) | M, F, N | `\M` `\F` `\N` | 3s.f (masculine was left unmarked) |
| definite article | DEF | `\Def` | def, df, d |
| indefinite article | INDF | `\Indf` | indef, indf |
| demonstratives oc / ec / oç / eç | PROX.SG, PROX.PL, DIST.SG, DIST.PL | `\Prox.\Sg` … | s.px s.prx p.px p.prx prx.p s.dt s.dst p.dt |
| preterite | PST | `\Pst` | pst |
| imperfect | IPFV | `\Ipfv` | ipf, ipfv, impf, imp |
| future | FUT | `\Fut` | fut |
| negative future (nol-) | NEG.FUT | `\Neg.\Fut` | neg.fut, not.fut |
| subjunctive | SBJV | `\Sbjv` | sbj |
| imperfect subjunctive | IPFV.SBJV | `\Ipfv.\Sbjv` | sbj.ipf, ipf.sbj |
| imperative | IMP | `\Imp` | (imp is also used for the imperfect: avoid) |
| infinitive | INF | `\Inf` | inf |
| present participle | PRS.PTCP | `\Prs.\Ptcp` | ptcp.prs, p.prs |
| past participle | PST.PTCP | `\Pst.\Ptcp` | ptcp.pst, p.pst, pts |
| potential (-abr) | POT | `\Pot` | pot |
| 'be' (es, sta …) | glossed lexically: be, be.PST … | – | be, be.pst … |
| er- forms (copula only) | COP.IPFV | `\Cop.\Ipfv` | cop.ipf, cop.imp |
| complementiser (ig) | COMP | `\Comp` | comp |
| comparative (-essem, -errem) | CMPR | `\Cmpr` | comp, cmp (clashes with complementiser) |
| question particle (ou) | Q | `\Q` | q |
| negation | NEG | `\Neg` | neg, not |
| reflexive (se) | REFL | `\Refl` | rfl, refl |
| oblique pronoun | OBL | `\Obl` | obl; acc where it has the oblique form |
| accusative pronoun | ACC, only where it has its own form (so far 3PL *lou*) | `\Acc` | acc |
| disjunctive pronoun (every disjunctive use) | DSJ | `\Dsj` | dsj, dj |
| possessive (my, ty, sy …) | POSS | `\Poss` | gen, gn, ps, poss |
| agentive (meyon 'by me' …; agent nouns in -our) | AGT | `\Agt` | dem, ins (1s.dem, 1s.ins); agt |
| collective (-ary) | COLL | `\Coll` | coll |
| adjectival (-er) | ADJ | `\Adj` | adj |
| adverbial (cos + adj.) | ADV | `\Adv` | adv |

Portmanteau preposition + article forms are glossed with the English preposition plus DEF: *ny* 'in.DEF', *ag* 'to.DEF', *dy* 'of.DEF'.
