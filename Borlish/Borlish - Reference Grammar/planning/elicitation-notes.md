# Elicitation notes

Answers from the **Borlish Field Notebook** artifact (https://claude.ai/artifact/AsVFahhueS2y7W2X9rPN6N), filed by chapter so they can be collated straight into the grammar. The questions live in `elicitation-bank.json`.

## How a batch is filed

1. The user answers questions in the notebook and presses **Submit**. Each submission is a document in the artifact's `submissions` collection; the answers are in `answers`.
2. Claude reads the new answers and, for each one:
   - copies the Borlish **verbatim** (corrections go in the notebook, not here);
   - adds phonemic IPA and a Leipzig gloss to the RG standard (`glossing-abbreviations.md`);
   - states what the answer **settles**, as rules ready to go into a chapter;
   - lists any **follow-ups** it raises. These become questions in a later round.
3. Claude writes a one- or two-sentence finding back to the notebook (`findings` collection), where it shows on the answered card, and marks the submission filed.
4. If an answer contradicts a drafted chapter or the corpus, the conflict goes under **Conflicts** below rather than being fixed silently.

**Entry format**

```
### E00 · English prompt
- **Borlish:** answer as given  (variants / notes from the user)
- **IPA:** /…/
- **Gloss:** word-by-word, RG abbreviations
- **Settles:** rule statements
- **Follow-up:** questions raised (→ round N)
```

Marks: ✔ the answer states it directly · ? Claude's inference, to confirm in a follow-up.

**Batches filed:**
- S20261012164035 (E01–E10, filed 2026-10-12).
- S20261012165704 (E09 resubmitted with the correction, 2026-10-12).
- S20261012172232 (E11–E20, filed 2026-10-12).
- S20261012212243 (E21–E30, filed 2026-10-12).
- S20261012221000 (E31–E40, filed 2026-10-12). Claude recorded this submission: the user reported submitting, but the answers were still drafts in the store.
- S20261012225004 (E41–E50, filed 2026-10-12).
- S20261013010738 (E51–E60, filed 2026-10-13).
- S20261013022310 (E61–E80, filed 2026-10-13).
- S20261013120138 (E81–E90, filed 2026-10-13).
- S20261013125142 (E91–E100, filed 2026-10-13). The user corrected some forms in chat: E93 *ovreu* → *ovroy*; E98 *scein* → *sceyen*; E100 *accort* → *accordn* and *no's* → *no son*.
- S20261013144712 (E101–E110, filed 2026-10-13).
- S20261017174937 (E111–E120, filed 2026-10-17).
- S20261017184710 (E121–E130, filed 2026-10-17).

## Conflicts with drafted chapters or the corpus

1. **Pronouns after a positive command** (E02; **confirmed by E29**, *Dig lour…*: the 3PL indirect object is oblique *lour*, not disjunctive *lou*). So after a command, 3rd-person pronouns keep their clitic case form (ACC *lo*, OBL *lour*), and only 1st/2nd-person pronouns are disjunctive (*mey*, *tey*). **Restated in the chapters 2026-10-12:**
- `pronouns.tex` §Imperatives (new label `sec:imperative-pronouns`) gives the rule, adds *Deskieð tey noc*, *Da lo mey!* and *Dig lour…*, and carries a CHECK for negative commands and for E33.
- `tam.tex` §Commands and `verb-morphology.tex` §Subjunctive and imperative now refer to it.
- Checked with a scratch build.

The original note follows: `pronouns.tex` §Imperatives and `tam.tex` §Commands say an object pronoun after a command "takes its disjunctive form". *Da lo mey!* keeps the 3rd-person object as the clitic *lo* (there is no neuter disjunctive), and only the 1st-person recipient is disjunctive. Possible restatement: 1st/2nd-person pronouns after a command are disjunctive; 3rd-person direct objects keep their accusative form. E33 (*Give it to them!*) tests the 3PL indirect object, where *lou* (DSJ) and *lour* (OBL) differ.
2. **The 2SG imperative** (E02). **Principle settled by E34** (user: "the set of verbs which use the subjunctive in the singular imperative is actually closed, while verbs generally do use the subjunctive in the plural (*Vinað ac!*)"):
   - The 2SG imperative is normally the **present indicative SG** (*da*, *vien*, *toc*). Only a **closed set** of verbs uses the subjunctive in the singular. Plural and polite commands use the subjunctive.
   - **Closed set confirmed by the user (2026-10-12):** **sey** (*star*), **ay** (*aïr*), **faç** (*fair*), **saif** (*savir*), **remain** (*remanir*).
   - The user chose ***va*** as the 2SG imperative of *eir* (not *vay*). The corpus has no *vay* imperatives.
   - **Restated in the chapters 2026-10-12:** `verb-morphology.tex` (endings table and §Subjunctive and imperative) and `tam.tex` §Commands.
   The original note follows: `verb-morphology.tex` (table, line 91, and §Subjunctive and imperative) says the imperative is identical to the present subjunctive. `tam.tex` §Commands says the 2SG imperative is the bare present stem. The two agree for regular verbs, but not for *dar*: the subjunctive is *day*, and the imperative given is *da*. This supports `tam.tex`. E34 (*Come here!*) tests *venir*, whose indicative *vien* and subjunctive *vin* differ.
3. ~~**Position of *novel*** (E06).~~ **Resolved 2026-10-12.** The user decided that *novel* is prenominal. The corpus was regularised; see *Adjectives*.
4. **Passive auxiliaries** (E13). The user's system is *fo* + PTCP for an event ('was built'), *er* + PTCP for a process in progress ('was being built'), and *sta* + PTCP for a resulting state ('I think' it takes no agent). The corpus doesn't keep to this:
   - *er* + PTCP is often used for a one-off event, e.g. *janthin er descovart ne Zampanagar d'an 1778* (Scaunç 30626) and *Le'r coronnað com Emperour Roger I … d'an 1038* (C2525).
   - *sta* + PTCP takes a *par* agent 4 times, e.g. *sta conservað par*, and *sta corporalleyað par* ('was established by…').
   - Corpus counts (unique sentences): *er/ern/'r* + PTCP about 57, *fo/forn* + PTCP about 24 (many of these are *star* pluperfects such as *fo denuð*), *sta/stan* + PTCP about 19.
   - Decision needed: retcon the event-type *er* passives to *fo*, or allow *er* for events in narrative? E41–E43 test this.
   - **Answered by E41–E43** (see *Voice & Valency*): *fo* for a dated event, *er* for a process, *sta* + *con* for a state.
5. ~~**Mood after *degnant ig*** (E18).~~ **Resolved 2026-10-12.** C166 was a slip: *degnant ig* takes the subjunctive. Scaunç 2333 already read *Degnant ig cous noit la'r…* (the user's own fix); the corpus line was synced to match.
6. ~~**Polite address** (E19).~~ **Resolved 2026-10-12.** The user corrected E19 to *Vos veleð…*: *vos* is the polite address to one person, as `tam.tex` §Commands assumes.
7. **Passives, retcon requested** (E13; supersedes Conflict 4). The user wants every past passive in the corpus regularised to the E13 system. The user's explanation: "English has only 'was' and French tends to use *était* over *fut* in usual speech."    - Item-by-item review: **Borlish Passive Review**, https://claude.ai/artifact/8cbR5kbHdB2WP4XJ5aUqdZ (db collection `decisions`). It has 109 rows: 61 proposed changes, 44 already consistent, and 4 other slips.
   - The rows are built by scratch `passive_review_data.py` from Scaunç line numbers.
   - **Applied 2026-10-12.** The user overrode 4 rows: P005 *no sta reitfiað*, P008 *stan armað*, P106 *sta condoit*. For P073 the user noted that *comtað* is a noun and the verb is *sta … hamtant*, so it became *er … hamtant*, the past progressive. All other rows took the proposal.
   - **66 changes in Scaunç.** The IPA, phonetic and gloss lines of the 10 glossed blocks were edited too: COP.IPFV → be.pst / be.ipfv, and the missing gloss for *plait* was added.
   - The changes were carried to every corpus sentence that has a copy. Four of these were matched through variant spellings (*meyan*, *reluð*, *haubrojoranç*, and no *tan*); three Romantic-period sentences aren't in the corpus at all. Also changed: the `.db` (2 `\xv` lines, one still on the pre-retcon *L'er*) and 47 output files.
   - **Verified.** 46 output files match a regeneration exactly. 70.2 differs only by the user's pending Scaunç spelling *haubrjoranç*, which had already drifted before this edit.
   - Nothing was found in the vault.
   - Grammar updated: the `pronouns.tex` example (*sta adornað*), the `voice.tex` and `copulas.tex` plan comments, and `irregular-verbs.md`.
   - Scripts (scratch): `passive_review_data.py`, `passive_changes.py`, `passive_apply.py`. Backups are in `backup_passive/`.
   - C11467 / Scaunç 11467: *Nell'ec ouvr a Carvallo ern introdoit plusour dy qualtað natural por un racont masquiral.*
     - **User (2026-10-12):** this is a passive with inversion, not an active verb: 'In these works of Carvallo were introduced several of the essential qualities…'. Inverting both the auxiliary *and* the participle before the subject is "a bit literary" but grammatical.
     - Aspect: the user chose ***forn introdoit*** (an event). Applied 2026-10-12 to Scaunç, corpus line 1269 and output 36.1 (verified against a regeneration).
   - **Syntax (→ The Simple Clause / Information Structure):**
     - ✔ After a fronted locative PP, a passive can invert its whole verb group, so AUX + PTCP comes before a heavy subject. This is literary.
     - ? The ordinary V2 order would be AUX + SUBJ + PTCP, as in *Posc pieç minut fo y sar remorcað* (Scaunç 4512).
10. **Present plural of the *-r* class** (E38).
    - The user suggests that *-r* verbs take *-m, -ð, -n* in the present plural (*nos veim*), "which might actually be supposed to be true in all cases".
    - The corpus agrees: 10/10 1PL tokens end in *-m* and none in *-eu*.
    - `appendices/verb-tables.tex` and `verb-morphology.tex` still give *ðureu, ðureð*. *ðureu* is also the preterite singular, so the new endings would remove that clash.
    - **Resolved 2026-10-12:** the user confirmed that all *-r* verbs take *-m, -ð, -n*.
    - Updated: `verb-morphology.tex` (endings table, §Present and imperfect, §Subjunctive and imperative, §Shared forms), `appendices/verb-tables.tex` (*ðurm, ðurð, ðurn*) and `irregular-verbs.md` (*fair* 1PL *faim*; *cair* forms suggested).
    - In the corpus, the one old-pattern form, Camus *Nos creyeu* (Scaunç 1131), became *creim*.
    - *deyeu/deyeð* stay, because *deïr* is *ir1* in the lexicon.
    - The user then confirmed *faim, faið, caim, caið*, and changed *eir* to **vam, vað, van**, so it now fits the pattern. The only exception is *fair* 3PL *faun*. Attested 2PL: *vos comprenð* (Scaunç 1119). The *-ir1* modals *vouð*, *pouð* are their own thing.
8. ~~**Preterite of *scaur* 'write'** (E21).~~ **Resolved 2026-10-12.** The user confirmed ***scavoy*** (an *-oy* preterite: *scavoy*, *scavoim*, *scavoist*, *scavoirn*); their *scavau* in E21 was a slip. The divergent *scavau*/*scaveu* were retconned in Scaunç 21863, 24767 (with its IPA and phonetic lines) and 29435, in corpus lines 2083, 2351 and 2730, and in output 136.1, 163.2 and 208.1.
9. **Preterite of *denir*** (E28). Following the user's instruction, *deneu* → *denoy* and *deneurn* → *denoirn* were changed in Scaunç (6 lines), in the corpus and in output 203.1, 204.1, 209.1, 226.1, 230.1 and 231.1. All touched output files were verified against a regeneration.
11. **Possessor marking: *de* or *a*?** (E15, E46.)
    - The user (E46): "Honestly I'm not actually sure of the distribution of *de* versus *a* in possessive constructions. It's possible that I've been inconsistent."
    - The `nouns.tex` plan comment lists only *de* + NP for possession. E15 and E46 both use *a* for a human possessor, and *de* for part–whole (*y fastig dy majon*).
    - Corpus (unique sentences, sampled by script `poss.py`). Human possessors take both:
      - *a*: *y tablaur a my maðr* 'my mother's worktable', *ogl a Luc* 'Lucas's eyes', *cla a Hector* 'Hector's key', *aur a Hector* 'Hector's money', *ogl a Hector*, *fo stað a Marco* 'had been Marco's'.
      - *de*: *ogl de my fraðr* 'my brother's eyes', *gamblas de sy paðr* 'her father's barge', *orphan de sy fraðr*, *linaç de sy maðr*, *tesoir de Hector* 'Hector's vault' (in the same sentence as *cla a Hector*), *patronisment de Martin*, *soutien de Marc*, *lign de Natagl*.
      - A title or role with the article takes *dy*/*dell'*: *patronisment dy Duc*, *mort dell'Emperour*, *visaç dy segr*.
    - ? A possible system: ***a* for what a person owns or has** (belongings, money, pets, house); ***de* for every other relation** (part–whole, lineage, reign, patronage, support, origin) and for all non-human possessors. Body parts and kin are split both ways in the corpus.
    - **Decision needed** before the Nouns chapter is drafted. E61–E62 ask about ownership and body parts.
12. ~~***megl* → *ottem***~~ (E47). **Resolved 2026-10-13**: the user approved the retcon. The record follows.
    - The user: "*megl* is outdated, yeah. It should be *ottem* throughout for 'better' and 'best' both as an adjective or an adverb."
    - *megl* survives in 8 unique corpus sentences (12 lines, with duplicates): *y megl tarn* 'the best inn' (C38), *sera megl vos ignoreð* (C240, also the example in `pronouns.tex` line 43), *no sta megl* (C295), *Y megl quignou* (C377), *s'accommettr megl* (C731 = C986), *par megl manouvr* (C754 = C1009), *me benoçar megl* (C767 = C1022), *son megl s'aðelent* (C964 = C1219).
    - Not in Scaunç, the output files or the vault; `Data/pre-2022 notes.txt` (frozen) has it too.
    - The `.db` has ***megl*** (adv 'better') and ***meglfacçon*** (n; Scaunç 26435 *scerraun meglfacçon*). *ottem* is listed only as adj 'best, greatest'.
    - **Applied 2026-10-13:**
      - All 12 corpus lines now have *ottem*, with *l'* before it (*l'ottem tarn*, *L'ottem quignou*).
      - The `pronouns.tex` example now reads *Parcanç sera ottem vos ignoreð…*.
      - In the `.db`, *ottem* now has 'better' first and an adverb sense ('better, best'). *megl* is tagged `\ue obsolete`, and its etymology notes that *ottem* displaced it.
      - The bank's old probes and `Data/pre-2022 notes.txt` were left alone.
      - Backups are in scratch `backup_megl/`; the script is `megl_fix.py`.
    - **The user: keep *meglfair* 'improve' and *meglfacçon* 'improvement'** as extant remnants of the obsolete *megl*.
13. **Past counterfactual: imperfect or pluperfect subjunctive?** (E24, E54.)
    - Both answers put the **simple imperfect subjunctive** in the *if* clause: *Ða jo saveus, jo volois ig venir*; *Ða tu me lo rovaus, jo volois te lo digr*.
    - `tam.tex` §Conditional (line 310) gives the **pluperfect subjunctive** *aus* + participle instead, with corpus examples: *Ða l'aus un curtel frivol cossirabr posseïð…*, *…ða y scon femn aus dottr menað*.
    - ? Both may be grammatical, perhaps with the pluperfect more literary or more clearly anterior. **Decision needed** before §Conditional is revised. E71 asks.
    - **E61–E62 (user):** physical possessions one can hold take *a*, more abstract possession perhaps *de*; **body parts take *a***, and "any example in the notes that uses *de* might be worth fixing".
    - **Applied 2026-10-13 (user-approved):** *de* → *a* for body parts and owned objects:
      - C275 *L'eç ogl a my fraðr*; C484 *y visaç ag segr*; C736 = C991 *y pie a Yvet*; C2011 *ag gien a Evangelin*; C2568 *all'oregl a un benoyour*; C1506 *y gamblas a sy paðr*.
      - Carried to Scaunç (3196, 5368, 8005, 14676, 21097, 26873) and output 2.1, 65.1, 128.1, 185.1. These match a scratch regeneration, and their `manifest.tsv` rows and `summary.txt` were updated from it. Backups are in scratch `backup_poss/`; the script is `poss_fix.py`.
      - Kept on the user's instruction: C269 *tesoir de Hector* ("in some sense Hector doesn't own the vault, it just corresponds to him"). Kept as idioms: C820 *sou y man de car Valeria*, C857 *amig a cour dy…*.
    - **E81 confirms:** *l'audaç de my paðr*. The user: "character traits feel like they come 'from' a person".
    - **Working rule:** *a* for body parts and for things a person owns; *de* for what merely corresponds to or relates to a person (*tesoir de Hector*, *patronisment de Martin*, *linaç de sy maðr*), for part–whole, and for non-human possessors. E81 tests an abstract quality.
13b. **Counterfactual, continued.** E71 again has the simple imperfect subjunctive, in both clauses (*Ða nos parteusseu tostessem, nos sceusseu montar…*). The user suggests the `tam.tex` example can be parsed 'If she had had a gown … (that she) possessed', so *aus* there is simply 'had' (IPFV.SBJV of *aïr*). *…ða y scon femn aus dottr menað* can be read the same way. **Applied 2026-10-13 (user-approved):** `tam.tex` §Conditional sentences now gives *ða* + IPFV.SBJV with *volois* + INF, or a modal's own IPFV.SBJV (E24, E54, E71). The *curtel* and *dottr* examples are explained as *aus* 'had' + object + modifying participle. §Perfect no longer claims a pluperfect subjunctive with *aus*; a CHECK asks whether one exists at all (→ E86). Scratch build clean.
14. ***ou* after a verb of knowing** (E64). The user: in *Le reconnosc ou sy fraðr sey tan demastr?* (`tam.tex` line 254) *ou* is the **question particle**, and a questioned verb of knowing governs the subjunctive. The gloss 'whether' should be Q. The CHECK (2) at line 264 dissolves: *instroy* in *Vos saveð ou l'instroy…* is a singular, where subjunctive and indicative coincide.
    - **Applied 2026-10-13:** reglossed as `\Q`, with a sentence on *ou* after questioned and negated verbs of knowing and E64 added as an example. CHECK (2) is closed in the comment.
15. **E68 / C2552.** My question misquoted the corpus: *sta adornað par fylau* is 'decorated with **crows**' (*fylau* 'American crow'), not flowers. The user answered *…sta adornað par con flour*. **User (2026-10-13):** *par* was a leftover; make it ***con flour***. **Applied:** C1297 and the Scaunç 11777 block (IPA */kɔn flur/*, phonetic *[kɔn fluː]*, gloss 'with flower', English 'flowers'), output 39.2 (matches a regeneration), the `pronouns.tex` example and the `voice.tex` plan comment.
16. ***l'eç* as a plain plural 'the'.** E52 *l'eç ivan*, E62 *l'eç ogl*, corpus C275 *L'eç ogl de my fraðr*, *L'eç ogl a Luc*. `determiners.tex` §Demonstratives and number gives *l'ec* for the weak-deixis plural.
    - **User (2026-10-13):** the choice still follows proximity: *l'ec* if the items are near in the context ('these'), *l'eç* if distal ('those'). "If the brother were physically present I would probably have done *L'ec…*". So even in its plain-plural use the demonstrative keeps its deixis. A sentence to add to `determiners.tex` when that section is revised.
17. ~~**Mood after *degnant* for an earlier past event** (E86).~~ **Resolved 2026-10-13:** the user says *fo* was a typo for ***fos***. So *degnant* keeps the subjunctive, and an earlier past event takes the **pluperfect subjunctive** *fos* + PTCP. `tam.tex` §Perfect now says so, with E86 as its example; its earlier claim that there was no pluperfect subjunctive is withdrawn. The original note follows.
    - E86 has *Degnant le fo parsið con nis…*, with **indicative** *fo* (the preterite of *star*) and no *ig*.
    - Elsewhere *degnant* takes the subjunctive, with or without *ig*: E18 *Degnant ig cous tart* (C166 was corrected to match), and corpus *degnant jo lour day*, *degnant alcun hom saif*, *degnant le volois…*.
    - The subjunctive counterpart would be *fos parsið* (*star* IPFV.SBJV + PTCP), the pluperfect subjunctive that the `tam.tex` CHECK asks about.
    - **To ask:** is *fo parsið* right here (a factual pluperfect keeping the indicative), or should it be *fos parsið*?
18. ***orruðar* imperfect** (irregular-verbs Q23). E89 gives ***orruða***, the regular *-ar* form. The corpus has *orruðe* three times (S15880, S23514, S24429). ~~To ask: retcon those to *orruða*?~~ **Applied 2026-10-13 (user-approved):**
    - Scaunç 21953, 23514 and 24429, with their IPA and phonetic lines (24429's phonetic line already had *ða*).
    - Corpus lines 2088, 2225 and 2320; two `.db` example lines; output 137.1, 149.7 and 159.4. The output files, `manifest.tsv` and `summary.txt` match a regeneration.
    - Left alone: `verb-evidence.md` (a dated harvest).
19. ***ovrir* preterite** (E93). E93 had *s'ovreu*. The user (2026-10-13): "go with ovroy then; I just forgot the form."
    - `verb-morphology.tex` and the corpus have *ovroy* (4×, plus *descovroy*).
    - One corpus token has *ovreu*: C2623 = S27406 *Cattridge l'ovreu varsant…*
    - ~~To ask: retcon that one to *l'ovroy*?~~ **Applied 2026-10-13 (user-approved):** S27406, C2623 and output 191.1 now have *l'ovroy*.
20. ***toð gent* agreement** (E100).
    - The user corrected E100 in chat to a plural verb: *accordn*, *no son accordant* (first submitted as 3SG *accort*, *no's*).
    - That fits most of the corpus: *Toð gent saun ig…* (C2335), *toð gent sauraun* (C862), *Casc gent veurn* (C923), *casc gent taçoirn* (C792).
    - Two corpus sentences have 3SG: C693 = S7673 *Toð gent la es hastant…*, and C2970 = S32636 *Toð gent dema l'ig…* (*dema* is the imperfect 3SG of *demar*).
    - ~~To ask: retcon those to *son hastant* and *deman*?~~ **Applied 2026-10-13 (user-approved):**
      - S7673 = C693 now has *son hastant*. It is an early post that never reaches the output folder.
      - S32636 = C2970, the `.db` `\xv` line and output 241.2 now have *deman*, with IPA /deˈman/, phonetic [dɪˈman] and gloss *opine-ipf-3p*.
21. ***-romoy* → *-rompoy*** (Q24). User (2026-10-13): "I think I was basing that on how -ndr verbs behave (usually deleting the -d-), but actually I think the voiceless -p- should resist that and stay." **Applied 2026-10-13** to the whole past stem: *interrompoy*, *interrompoirn*, *interrompois*, *tarrompoy*.
    - Scaunç 4227, 10904, 20243, 20853, 23789, 25027 and 28988, including the IPA and phonetic lines of the three dictionary posts.
    - Corpus 369, 974, 1229, 1942, 1992, 2261, 2379 and 2699; two `.db` `\xv` lines.
    - Output 118.4, 125.2, 152.4, 166.1, 203.1 and 30.1. Their `manifest.tsv` rows were copied from a regeneration, and the output files match it.
    - `verb-morphology.tex` §irregularities now has the *interrompoy* forms, plus the rule: *d* after *n* is usually lost, *p* is kept.
    - Left alone: `verb-tokens.tsv` and `verb-evidence.md` (dated harvests).
22. ***vendr* → *vençar*** (Q24 follow-on). User (2026-10-13): *vendoy* "is an artefact from a previous version; *vendr* is obsolete and the usual word for 'to sell' is *vençar*, a regular -ar verb from Latin *vendicāre*." **Applied 2026-10-13:**
    - S2019 = C114 *ig le vende livr* → *vença* (imperfect).
    - S3686 = C319 *vendoy* → *vençau*, with IPA /vɛnˈtso/. It is an early post that never reaches the output folder.
    - S30177 = C2760, the `.db` `\xv` line and output 216.2: *vendr* → *vençar*, with IPA /vɛnˈtsar/ and phonetic [vɛnˈtsɐː]. Output 216.2 matches a regeneration, and its `manifest.tsv` row was copied from it.
    - With *vendoy* gone, no *-ndr* verb in the corpus keeps its *d* before *-oy*. At the user's request, `verb-morphology.tex` now says the *d* is **always** lost.
23. **Measure phrases: *de* or *a*?** (E108.)
    - E108 has *un cop de tag*, *dou trenc de pan*. The user: "I'm not actually sure whether measure phrases tend to use *a* or *de* in the notes. I'm inclining with retrospect to *de*, as in a piece 'from' the thing."
    - The corpus consistently has ***a***: *un veðr a brandvin* 'a glass of brandy' (C2657), *trenc a lox* 'pizza slices' (C2303; also a `.db` example), *y plat a lox* (C2286), *tre pajot a savon* 'three bars of soap' (C2952). *vray bottel de Vescomb* (C2959) is an origin ('bottles from Vescomb'), not a measure.
    - **Resolved 2026-10-13 (user):** "I'm happy to lean in to that use of *a* possession." Measure phrases take ***a*** + bare noun, so E108 becomes *un cop a tag e dou trenc a pan*. The corpus already agrees, so nothing to retcon.
24. ***querel-* / *kerel-* duplicates** (the user flagged them with E104).
    - The `.db` has two sets. One is *querel* n 'quarrel', *querellar* v, *querellabr* adj and *querellaç* n 'row, spat'. The other is *kerel* n 'feud, dispute', *kerellar* v and *kerel trocar* v.
    - In the corpus *querel-* is commoner (*querel* 3, *querellabr* 4, *querellant* 1, *querellaç* 1) than *kerel-* (*kerel* 2, *inkerellað* 1). E104 has *kerelleu*.
    - ~~To ask: which set to keep~~ **Applied 2026-10-13 (user: "keep kerel-, retcon querel- to kerel-"):**
      - Scaunç: 10 lines, including the whole post 25.3, whose headword is now ***kerellabr*** /ˌke.rɛˈla.br̩/ [ˌke.ʀɪˈla.bɐ]. Its etymology now derives the word from *kerellar* and *kerel*, and still cites Old French *querele* and Latin *querēla*.
      - Corpus: 9 lines.
      - Output: 25.3, renamed to `25.3_kerellabr_controversial.md`, plus 25.1, 40.1, 51.1, 56.1, 88.1 and 175.1. All match a regeneration, and their 7 `manifest.tsv` rows were copied from it.
      - `.db`: *querel* and *querellar* were removed as duplicates of *kerel* and *kerellar*. *kerel* takes over the etymology (*Old Borlish < Latin querēla*). *querellabr* and *querellaç* became ***kerellabr*** and ***kerellaç*** and moved beside *kerellar*.
25. **Intransitive *closir*** (E114). User (2026-10-17): "I think *closir* should be transitive, so I've fixed the cases of intransitive *closir* in the Scaunç file (elsewhere will need aligning)." The user's commit 902c0b7 added *se* in three Scaunç sentences: S19364 *y crescenç den se closisceu*, S21273 *Y port dy cahut se closisceu*, S27341 *y port se closisceus*, the last with its IPA, phonetic and gloss lines. **Aligned 2026-10-17:**
    - Corpus 1871, 2026 and 2493; the `.db` `\xv` line.
    - Output 110.1, 130.1 and 190.3, which match a regeneration; their `manifest.tsv` rows were copied from it.
26. ***soluçon* or *solution*?** (E121.)
    - E121 and the `.db` have *soluçon* 'solution, answer'.
    - The corpus has ***solution*** in five sentences: C291 *L'oc solution effectuar…*, C557 *pog solution a Drico*, C888 = C1143 *descovart de solution*, C916 = C1171 *y bon solution augrimar*, C1446 *n'aun solution yent*. It never has *soluçon*.
    - ~~To ask: retcon those to *soluçon*?~~ **Applied 2026-10-17 (user: "I revised Borlish words ending -Vtion and -Vsion to -Vçon and -Vjon"):**
      - Scaunç 3371 (IPA /ˌso.liˈtsɔn/), 6097, 9665 and 13882. S10005 already had *soluçon*.
      - The 7 corpus tokens.
      - Output 20.1 and 57.1, which match a regeneration; their `manifest.tsv` rows were copied from it.
      - **Follow-on, applied 2026-10-17 (user-approved):** every remaining Borlish *-Vtion*/*-Vsion* is now *-Vçon*/*-Vjon*. Exceptions:
        - *position* → ***posson***, and the stray *-postion* forms (*postion*, *compostion*, *expostion*, *sepostion*) → *-posson*, matching the existing *composson*, *exposson*, *opposson*;
        - the typo *Adminstration* → *Administraçon*.
      - Scope:
        - Scaunç: 82 Borlish lines, including the Lexember headwords *donaçon* and *descujon*, the Lord's Prayer *tentaçon*, the publisher name *Ediçon Cordin*, and the hypothetical *concreçon* in an etymology. Also 13 IPA and phonetic lines (*tsjɔn* → *tsɔn*, *zjɔn* → *ʒɔn*, *posson* /pɔˈsɔn/, *composson* /ˌkɔm.pɔˈsɔn/).
        - The corpus's Borlish column: 89 lines. Two `.db` `\xv` lines.
        - 45 output files, which match a regeneration; their `manifest.tsv` rows were copied from it.
      - Left alone:
        - English text, including six English lines sitting in the corpus's Borlish column (C977, C2215, C2217, C2757, C2839, C2916) and the English typo *prepostion* in the *posc* etymology;
        - *aversion* (post 53.4), which ends in *-rsion*, not *-Vsion*, so the rule doesn't cover it.
      - Not in the `.db`: *naçon*, *humiglaçon*, *normalleyaçon*, *civilleyaçon*, *contaminaçon*, *redefiniçon*, *liberalleyaçon*, *convoluçon*, *tentaçon*.
      - **Second pass, 2026-10-17 (user):**
        - *aversion* → ***averjon***, matching the `.db` headword. This covers the Scaunç post 53.4 title, headword and example, all with IPA /ˌa.vɛrˈʒɔn/ and phonetic [ˌa.vɪːˈʒɔn]. Also the corpus line, six `.db` `\xv` lines, and the output, which was renamed to `53.4_averjon_opposition.md`. The etymology's "Middle Borlish *aversion*" is kept as the historical form.
        - *-isation* nouns take ***-eyaçon***, with a stem-final *l* doubled, like the existing *panelleyaçon* and *corporalleyaçon*: *normalisaçon* → ***normalleyaçon*** (S4631, C405), *liberalisaçon* → ***liberalleyaçon*** (S15921, C1611, output 78.1), *civilisaçon* → ***civilleyaçon*** (C1437). Verbs in *-isar* (*normalisað*, *corporalisað*, *debriscellisar*) are a separate series and are left alone.
        - The English typo *prepostion* → *preposition* in the *posc* etymology: S13059, the `.db` `\et` line and output 50.4.
        - Output 50.4, 53.4 and 78.1 match a regeneration; their `manifest.tsv` rows were copied from it.

---

## The Simple Clause

### E06 · Yesterday Marc bought a new teapot.
- **Borlish:** *Yer accatau Marc un novel ketr a tag.* (also *Yer, Marc accatau un novel ketr a tag.* User: *je ados* is a more familiar way of saying 'yesterday' than formal *yer*.)
- **IPA:** /jɛr ˌa.kaˈto mark ɪn noˈvɛl ˈkɛt.r̩ a tɛj/
- **Gloss:** yesterday buy-PST Marc INDF new kettle to tea
- **Settles:**
  - ✔ A fronted time adverb makes the subject follow the finite verb: *Yer accatau Marc*.
  - ✔ When the adverb is set off by a pause (comma), there is no inversion: *Yer, Marc accatau*.
  - ? Together with wh-questions (*Hour alcot es tu…*), fronted objects (*l'ec bojay … acataust vos ou?*) and *Nuvr so jo…*, this is a **verb-second** pattern. An integrated fronted constituent triggers inversion; a dislocated one doesn't. Polar questions don't invert (E03), which fits.
  - ✔ *novel* precedes the noun here (*un novel ketr*).
  - ✔ *ketr a tag* 'teapot': N + *a* + N compound (lit. 'kettle for tea').
- **Follow-up:** Does a **pronoun** subject invert too? (→ E38 *On Sundays we eat at my grandmother's.*)

### E38 · On Sundays we eat at my grandmother's.
- **Borlish:** *Toð je Sol pascm nos cas my granmaðr.*
- **IPA:** /tɔθ ʒe sɔl ˈpax.m̩ nɔz kaz mi granˈma.ðr̩/ (*pascm* as given; see below)
- **Gloss:** all on.day.of Sunday eat-1PL 1PL at.home.of 1SG.POSS grandmother
- **Settles:**
  - ✔ **Pronoun subjects invert too** after a fronted adverbial (*pascm nos*), so the V2 pattern isn't limited to noun subjects.
  - ✔ 'On Sundays' is *toð je Sol* ('every on-day-of Sunday').
  - ✔ *cas* + NP means 'at someone's house' (*cas my granmaðr*).
- **Answered (user, 2026-10-12):** *-r*-class verbs often end the present plural in *-m, -ð, -n* (*veir* → *nos veim*), and perhaps they should in all cases. See Conflict 10.
- **Corpus (2026-10-12):** every *-r*-class 1PL present after *nos* ends in *-m*: *veim* ×6, *creim* ×2, *faim*, *reconnoscm*. There is no *-eu*, and no 2PL is attested.

### E50 · First we'll eat, then we'll talk.
- **Borlish:** *Primer voum nos pascr, soulor nos voum descorrir.*
- **IPA:** /priˈmɛr vum nɔz ˈpax.r̩ | suˈlɔr nɔz vum ˌde.xɔˈrɪr/
- **Gloss:** first will.1PL 1PL eat.INF | then 1PL will.1PL discuss.INF
- **Settles:**
  - ✔ A fronted ***primer*** triggers inversion. With the *volir* future, the subject comes straight after the auxiliary and the infinitive stays last: *Primer voum nos pascr*.
  - ✔ ***soulor*** does **not** trigger inversion: *soulor nos voum descorrir*. The `.db` lists *soulor* as a conjunction ('then, next, afterward'), so it stands outside the clause like *e* and *ma*.
  - ✔ 'Talk (things over)' is *descorrir* (*ir1*, 'discuss').
- **Follow-up:** Is *Soulor voum nos descorrir* possible too, and does a noun subject behave the same way (→ E66)?

### E66 · We waited an hour, and then the bus finally came.
- **Borlish:** *Nos attenoim un hour, e soulor y vec venoy tandem.* (also *…cos final* 'in the end' rather than 'at long last'; *…e soulor venoy tandem y vec* "somewhat literary or narrator voice"; *…e soulor tandem venoy y vec* "more emphasis on the finally, somewhat more natural in speech than the last variant")
- **IPA:** /nɔz ˌa.teˈnɔjm ɪn ur | e suˈlɔr i vɛk veˈnɔj tanˈdɛm/
- **Gloss:** 1PL wait.PST-1PL INDF hour | and then DEF bus come.PST at.last
- **Settles:**
  - ✔ After *soulor* the plain order is subject–verb. A **literary/narrator inversion** puts the noun subject last (*soulor venoy tandem y vec*).
  - ✔ A fronted ***tandem*** after *soulor* triggers ordinary V2 inversion (*soulor tandem venoy y vec*): *soulor* itself sits outside the clause, as E50 suggested.
  - ✔ *tandem* 'at long last'; *cos final* 'in the end'. Duration is a bare NP (*un hour*).
  - ✔ *attenoim* is the *-oy* preterite 1PL of *attendr*; *vec* 'bus' (corpus 10×, not in the .db).

**Fronted adverbial clauses don't trigger inversion** (✔, three answers): *Cant nos venoim, y majon er pegntað…* (E42), *Ða cay ploy je posc, nos voum remanir…* (E08), *Degnant ig cous tart, y varous remanen yert* (E18). A fronted clause patterns with the comma-set adverb of E06 (*Yer, Marc accatau…*), not with an integrated one. Inside the subordinate clause, the subject comes before the verb (*cant nos venoim*): subordinate clauses are not V2.

### E99 · The government has resigned.
- **Borlish:** *L'administraçon a ombisc soluð.* (also *…ombisc soluð (a cascun)*, "specifying the individuals 'each'")
- **IPA:** /ˌlad.mi.nɪs.traˈtsɔn a ɔmˈbɪx soˈlɪθ (a kaˈxɪn)/
- **Gloss:** DEF=government have.3SG resignation release.PST.PTCP (to each.one)
- **Settles:**
  - ✔ A **collective noun takes singular agreement** (*a*). Distributive *a cascun* 'each' makes the individuals explicit without changing the agreement (compare *un solt a cascun* 'a shilling each', C2952).
  - ✔ 'Resign' is the .db compound ***ombisc souvr*** 'release a resignation'. In the perfect, *ombisc* stands between the auxiliary and the participle like any object (compare *J'oy tu a un religion minour soluð*, C840). *soluð* is the PST.PTCP of *souvr*.

### E115 · Neither of them is ready.
- **Borlish:** *Necun de lou son prest.* (also *Alcun de lou son prest.*, "*alcun* is somewhat proscribed for 'none of two'")
- **IPA:** /neˈkɪn de lu sɔn prɛst/
- **Gloss:** neither of 3PL.DSJ be.3PL ready
- **Settles:**
  - ✔ *necun de* + disjunctive 'neither of' takes a **plural verb** (*son*).
  - ✔ *alcun* 'none' is used for two as well, but that use is somewhat proscribed.

## Questions & Commands

### E02 · Give it to me!  (to one small child)
- **Borlish:** *Da lo mey!*
- **IPA:** /da lo mi/
- **Gloss:** give 3SG.N.ACC 1SG.DSJ
- **Settles:**
  - ✔ The 2SG imperative of *dar* is **da**, identical to the present indicative and not the subjunctive *day*. Added to `irregular-verbs.md`.
  - ✔ In positive commands, the pronouns follow the verb.
  - ✔ The order is direct object then recipient. This reverses the declarative order (*te lo*), as in French *donne-le-moi*.
  - ✔ The 3rd-person direct object keeps its clitic form *lo*; the 1st-person recipient is disjunctive *mey*. See Conflicts 1 and 2.
- **Follow-up:**
  - 3PL recipient: *lou* or *lour*? (→ E33)
  - Is the 2SG imperative of an i-mutating verb the indicative or the subjunctive? (→ E34 *Come here!*)

### E03 · Have you fed the cat?  (to Marc, your brother)
- **Borlish:** *Tu a y cat fait pascr ou?*
- **IPA:** /ti a i kat fet ˈpax.r̩ u/
- **Gloss:** 2SG have DEF cat make.PST.PTCP eat.INF Q
- **Settles:**
  - ✔ A polar question keeps declarative word order and adds clause-final ***ou***. There is no inversion.
  - ✔ 'Feed' is the causative ***fair pascr*** 'make eat'.
  - ✔ In the perfect, the causee stands between the auxiliary and *fait*, like any direct object: *a y cat fait pascr*.
  - ✔ *tu* is used to a brother (T form within the family).
- **Follow-up:** Causatives with a pronoun causee are in round 3 (E27).

### E10 · Don't worry, I'll do it.  (to one friend)
- **Borlish:** *Deskieð tey noc, jo vil lo fair.* (also *Farau, j'oc farray.*)
- **IPA:** /dɛˈskjɛθ ti nɔk | ʒo vɪl lo fɛr/  ·  /faˈro | ʒɔk faˈre/
- **Gloss:** worry 2SG.DSJ NEG 1SG will 3SG.N.ACC do.INF  ·  never.mind 1SG=PROX.SG do-FUT.1SG
- **Settles:**
  - ✔ A negative 2SG command is verb + disjunctive + *noc*. A reflexive verb's reflexive surfaces as the disjunctive: *Deskieð tey noc*.
  - ✔ This matches `tam.tex` §Commands. The other attested strategy is *skig* + infinitive (*Skig aular ag quarf ða cay ploy borjonnant*, Scaunç).
  - ✔ 'I'll do it' is ***vil lo fair***, with the clitic before the infinitive.
  - ✔ The synthetic 1SG future of *fair* is **farray** (added to `irregular-verbs.md`).
  - ✔ *farau* (interj.) 'never mind, no worries' can stand in for 'don't worry'.
- **Morphology (user, 2026-10-12):** *Deskieð* is the imperative of the existing verb ***deskeðar*** 'worry, fret'. So stressed *e* → *ie* in the bare stem, like *venir* → *vien*. This is the stressed-vowel alternation of the present SG/3PL, not i-mutation. ? This implies the present *deskieð*, *deskieðn* and the infinitive *deskeðar*.
- **Follow-up:**
  - When do you use *skig* + infinitive rather than verb + *noc*? (→ E35)
  - In *j'oc farray*, the preverbal *oc* is the demonstrative object pronoun, which the determiner canon (2026-09-29) calls literary/soutenu. **User (2026-10-12), still thinking:** it may be current mainly as the pro-form object of *fair* ('do that/so'), more than in general use. Compare postverbal *oc* as the predicate pro-form with copulas (*Ða la'r oc*). Test later: *I'll do it* / *Who did that?* / *I know that* side by side.
  - **Answered by E84:** *J'oc fey* is the ordinary short answer 'I did (so)', focusing the fact. So preverbal *oc* with *fair* is current.

### E11 · Who did you give the money to?  (to Theo)
- **Borlish:** *A cu dau tu y moneð?*
- **IPA:** /a ki do ti i moˈnɛθ/
- **Gloss:** to who give.PST 2SG DEF money
- **Settles:**
  - ✔ The preposition is fronted with the question word (*A cu…*); there is no stranding.
  - ✔ The subject inverts after the fronted phrase (*dau tu*), as V2 predicts. The object follows the subject.
  - ✔ The preterite of *dar* is **dau**, in the 2SG too.
- **Follow-up:** Is stranding ever possible? (→ E49, with *con*)
- **Answered by E49:** *con* fronts too (*Con cu eu tu…?*).

### E19 · Could you tell me where the station is?  (to a stranger in the street)
- **Borlish:** *Vos veleð me digr ou yon es y quarf?* (Corrected in chat. The first answer was *Tu vel me digr…*; the user had missed that it was a formal situation.)
- **IPA:** /vɔz veˈlɛθ me ˈdaj.r̩ u jɔn ɛz i kwarf/
- **Gloss:** 2PL will.SBJV.2PL 1SG.OBL say.INF Q where be DEF station
- **Settles:**
  - ✔ A polite request is *vel-* + infinitive (the conditional), framed as a yes–no question.
  - ✔ **A stranger is addressed with *vos*** (polite singular, plural agreement: *veleð*).
  - ✔ The clitic goes before the infinitive (*me digr*).
  - ✔ The embedded question is *yon* + verb + subject (*yon es y quarf*). The subject inverts after the wh-word here too, and the verb is indicative.
  - ? The question particle *ou* closes the **main** clause (*Tu vel me digr ou*), and the indirect question follows it. So *ou* is final in its own clause rather than at the end of the sentence. Or is *ou* here 'whether'? (→ E44)
  - ✔ **Answered by E44** (*Tu sa ou yon la hamt?*): *ou* is the question particle, placed straight after the questioned part. See E44.
- *quarf* covers 'station' as well as 'wharf' (lexicon).

### E29 · Tell them I said hello.  (to one friend about to visit your parents)
- **Borlish:** *Dig lour ig jo dis bonjorn* (also *Dig lour jo dis bonjorn*. User: "ig is optional; this ig-less version is somewhat more elegant and consequently somewhat less common in speech." Slangier greetings: *hau*, *hello*, *yera*.)
- **IPA:** /daj lur aj ʒo dɪz bɔnˈʒɔrn/
- **Gloss:** say 3PL.OBL COMP 1SG say.PST hello
- **Settles:**
  - ✔ A positive command puts the 3PL indirect object after the verb **in its oblique form *lour***, not disjunctive *lou*. Combined with *Da lo mey* (E02): after a command, 3rd-person pronouns keep their clitic case, and 1st/2nd-person pronouns are disjunctive. Conflict 1 is resolved this way.
  - ✔ The complementiser *ig* is optional after *digr*. **Leaving it out is the more elegant, written choice**; speech usually keeps it. Compare E21.
  - ✔ *dis* is the 1SG preterite of ***digr*** 'say' (the user notes that the infinitive is *digr*, not *dir*).
  - ✔ Greetings: *bonjorn* (neutral); *hau*, *hello*, *yera* (slangy).

### E33 · Give it to them!  (to one person, handing over a parcel)
- **Borlish:** *Da lo lour!*
- **IPA:** /da lo lur/
- **Gloss:** give 3SG.N.ACC 3PL.OBL
- **Settles:**
  - ✔ With two 3rd-person pronouns after a command, the direct object comes first and the oblique recipient second: *lo lour*.
  - ✔ The recipient keeps its oblique form *lour*, as in *Dig lour*. This answers CHECK (2) in `pronouns.tex` §Imperatives.

### E34 · Come here!  (to one child)
- **Borlish:** *Vien ac!*
- **User:** "I'm realising that the set of verbs which use the subjunctive in the singular imperative is actually closed, while verbs generally do use the subjunctive in the plural (*Vinað ac!* to multiple children)."
- **IPA:** /vjɛn ak/
- **Gloss:** come here
- **Settles:**
  - ✔ The 2SG imperative of *venir* is the indicative *vien*, not the subjunctive *vin*. The plural is the subjunctive *vinað*.
  - ✔ The general rule (see Conflict 2): the singular imperative is the indicative; a closed set of verbs uses the subjunctive in the singular; plural commands are subjunctive.
- **Answered (user, 2026-10-12):** the closed set is *sey* (*star*), *ay* (*aïr*), *faç* (*fair*), *saif* (*savir*), *remain* (*remanir*). *eir* uses the indicative *va*.

### E35 · Don't touch that!  (to one child reaching for the stove)
- **Borlish:** *Toc noc l'oç!*
- **User:** "*Skig l'oç toccar!* ← more informal and likely in modern speech, especially with pronominal objects."
- **IPA:** /tɔk nɔk lɔts/  ·  /skaj lɔts tɔˈkar/
- **Gloss:** touch NEG DEF=DIST.SG  ·  avoid DEF=DIST.SG touch.INF
- **Settles:**
  - ✔ The negative 2SG command is the bare imperative + *noc*, with a full-NP object (demonstrative *l'oç*) after *noc*.
  - ✔ ***skig* + infinitive is the more informal, modern strategy**, and is especially likely with pronominal objects. The object goes before the infinitive, as usual.
  - ? This may explain why a 3rd-person clitic after a negative command is unattested: speakers prefer *skig* there. CHECK (1) in `pronouns.tex` stays open.

### E37 · Is there anyone at home?  (knocking at a friend's door)
- **Borlish:** *Scey un hom acas?*
- **IPA:** /xi ɪn ɔm aˈkaz/
- **Gloss:** there.be INDF person at.home
- **Settles:**
  - ✔ 'Anyone' in a question is the plain indefinite ***un hom***, not *alcun*.
  - ✔ 'At home' with no possessor is the adverb ***acas*** (not in the `.db`).
  - ✔ **User (2026-10-12):** dropping *ou* here "was a lapse". The **question particle *ou* is optional**, but leaving it out is a bit more colloquial. The intended answer is *Scey un hom acas ou?* A yes–no question without *ou* relies on intonation alone.

### E44 · Do you know where she lives?  (to Marc)
- **Borlish:** *Tu sa ou yon la hamt?*
- **IPA:** /ti sa u jɔn la hamt/
- **Gloss:** 2SG know Q where 3SG.F dwell
- **Settles:**
  - ✔ ***ou* comes straight after the questioned verb**, before the indirect question, as in E19. This is what the dictionary entry for *ou* says (post 194.2): the particle goes "directly after the constituent being interrogated". It is clause-final only when the whole clause is questioned (E03).
  - ✔ A **pronoun subject does not invert** in an embedded wh-clause: *yon la hamt*. With a noun subject, E19 had *yon es y quarf*. Main-clause wh-questions invert pronouns too (*A cu dau tu*, E11; *Con cu eu tu*, E49).
  - ? So embedded clauses aren't V2, and the noun-subject order of E19 is an optional stylistic inversion, as with French *où est la gare*.
  - ✔ *sa* is the 2SG present of *savir*, as in the user's paradigm. *tu* is used to a brother.
- **Check:** `tam.tex` line 254 glosses *ou* in *Le reconnosc ou sy fraðr sey tan demastr?* as 'whether', and the comment at line 264 does the same for *Vos saveð ou l'instroy eç stuðant çougr?*. E44 has *ou* in the same slot before a wh-clause, where 'whether' can't be meant, so these are probably the question particle too, with no complementiser. To confirm with the user (→ E64).
- **Follow-up:** Is *yon hamt la* possible? Is *yon y quarf es*? (→ E65)

### E45 · Please sit down, madam.  (to an elderly stranger, offering your seat on a train)
- **Borlish:** *Veleð asseïr, domn.*
- **IPA:** /veˈlɛθ ˌa.siˈjɪr | ˈdɔ.mn̩/
- **Gloss:** will.SBJV-2PL sit.INF | lady
- **Settles:**
  - ✔ A **polite command** is ***veleð* + infinitive**, 'be willing to sit', like French *veuillez*. *veleð* is the 2PL subjunctive of *volir*, which is also its plural imperative. There is no subject pronoun and no separate word for 'please'.
  - ✔ Compare E19, *Vos veleð me digr … ou?*: with *vos* and *ou* the same verb makes a request framed as a question.
  - ✔ *asseïr* 'sit (down)' is intransitive, with no reflexive.
  - ✔ ***domn*** 'lady' is the vocative 'madam'. It follows the command, set off by a comma.
- **Follow-up:** Are the plain plural imperatives used to people you know (→ E67, *Come in and sit down, both of you!*)?

### E49 · Who did you go to the theatre with?  (to Theo)
- **Borlish:** *Con cu eu tu all'odysse?*
- **User's variants:**
  - *Cosogr cu…* ("perhaps implying a date").
  - *Cu galau tu all'odysse?* 'Who did you accompany…'
  - *Cu te galau all'odysse?* 'Who accompanied you…'
- **IPA:** /kɔn ki aw ti ˌa.lo.dɪˈse/  ·  /koˈzɔj.r̩ ki…/  ·  /ki gaˈlo ti…/  ·  /ki te gaˈlo…/
- **Gloss:** with who go.PST 2SG to.DEF=cinema
- **Settles:**
  - ✔ ***con* is fronted with *cu***, just like *a* in E11. There is no stranding.
  - ✔ The pronoun subject inverts after the fronted phrase (*eu tu*).
  - ✔ ***cosogr*** 'together with' is used for a partner, suggesting a date.
  - ✔ Object and subject *cu* are told apart by order: *Cu galau tu…* (object; the subject inverts) against *Cu te galau…* (subject; the object clitic goes before the verb).
  - ✔ *eu* is the preterite 2SG of *eir*. *all'* is *a* + *l'*.
- **Lexicon:** *odysse* is 'cinema', as in the `.db`. The user confirmed they meant the cinema; 'theatre' is *theatr*.

### E58 · What a beautiful house!
- **Borlish:** *Alcot un bel majon!*
- **IPA:** /alˈkɔt ɪn bɛl maˈʒɔn/
- **Gloss:** how.much INDF beautiful house
- **Settles:**
  - ✔ An exclamative 'what a …!' is ***alcot*** 'how much' + an indefinite NP.
  - ✔ ***bel*** goes before the noun, like *veil* and *novel* (see *Adjectives*).
- **Follow-up:** Does *alcot* also take a bare adjective ('how tall!'), and does the subject invert after it? (→ E78)

### E59 · Would you like tea or coffee?  (to a guest)
- **Borlish:** *Vos veleð tag ben caffay cavir?*
- **User:** "*Vos veleð tag ben caffay cavir ou?* would instead read to me like 'is it that you want [tea or coffee], or not?'"
- **IPA:** /vɔz veˈlɛθ tɛj bɛn kaˈfe kaˈvɪr/
- **Gloss:** 2PL will.SBJV-2PL tea or coffee get.INF
- **Settles:**
  - ✔ An **alternative question** joins the options with ***ben*** and has **no *ou***. Adding *ou* makes it a yes–no question about the whole ('do you want tea-or-coffee, or not?'). So *ou* is strictly the polar particle.
  - ✔ 'Would you like' to a guest is ***Vos veleð*** + infinitive, as in E19. 'Have (to drink)' is *cavir* 'get'.
  - ✔ The objects stand before the infinitive (*tag ben caffay cavir*).

### E65 · I wonder where they've gone.
- **Borlish:** *Jo m'entrou yon son ðe eut.* (also *Jo m'entrou yon ðe son eut.* User: "optional inversion with auxiliaries")
- **IPA:** /ʒo mɛnˈtru jɔn sɔn ðe awt/  ·  /…jɔn ðe sɔn awt/
- **Gloss:** 1SG 1SG.REFL=wonder where be.3PL 3PL go.PST.PTCP
- **Settles:**
  - ✔ 'Wonder' is reflexive ***s'entrovar*** (present SG *entrou*, like *trovar* → *trou*).
  - ✔ In an embedded wh-clause a pronoun subject **may** follow an auxiliary (*yon son ðe eut*) or precede it (*yon ðe son eut*). With a lexical verb it precedes (E44 *yon la hamt*). Noun subject + lexical verb is still untested.
  - ✔ **E82:** with a noun subject and a lexical verb the order is subject–verb (*yon ty sour laur*); *yon laur ty sour* is "decidedly unnatural", acceptable perhaps only with a very heavy subject, and hardly ever with a transitive verb.

### E67 · Come in and sit down, both of you!  (to two friends at your door)
- **Borlish:** *Entreð eð asseyað, vos y dou!*
- **IPA:** /ɛnˈtrɛθ eθ ˌa.siˈjaθ | vɔz i du/
- **Gloss:** enter.SBJV-2PL and sit.SBJV-2PL | 2PL DEF two
- **Settles:**
  - ✔ Plural commands are the 2PL subjunctive in both classes: *-ar* *entreð*, *-ir* *asseyað*.
  - ✔ 'Both of you' is ***vos y dou***, set off at the end.

### E76 · Let me help you!  (to a friend with heavy bags)
- **Borlish:** *Ig jo t'aïð!* (also *Parmet mey de t'aïðar!*)
- **IPA:** /aj ʒo tɛˈjɪθ/  ·  /parˈmɛt mi de ˌtɛj.iˈðar/
- **Gloss:** COMP 1SG 2SG=help.SBJV  ·  permit 1SG.DSJ of 2SG=help.INF
- **Settles:**
  - ✔ A **hortative** 'let me…' is ***ig*** + subject + subjunctive (like French *que je…*).
  - ✔ The imperative of *parmettr* is the indicative *parmet*; the 1SG after it is disjunctive *mey*, as the command rule says; the clitic for 'you' stays on the infinitive.

### E78 · How tall you've grown!  (to a nephew)
- **Borlish:** *Alcot es tu denuð haut!* (also *Alcot stu denuð haut!* "with the colloquial inverted copula form"; *Alcot a tu te grandið!* 'how much you've grown!'; *Alcot haut es tu denuð!* "more mannered")
- **IPA:** /alˈkɔt ɛz ti deˈnɪθ hot/
- **Gloss:** how.much be 2SG become.PST.PTCP tall
- **Settles:**
  - ✔ Exclamative *alcot* triggers **inversion** (*es tu*), and the adjective normally stays at the end; fronting it with *alcot* is mannered.
  - ✔ ***stu*** is the colloquial inverted *es tu* (the *sco, stu, zy* paradigm, irregular-verbs Q2).
  - ✔ *denir* takes *star* (*es … denuð*). Reflexive *se grandir* takes ***aïr***, with the reflexive on the participle (*a tu te grandið*).

### E79 · — Didn't you call her? — Yes, I did!
- **Borlish:** *Tu la boðau noc ou? Vis oc fey jo!*
- **IPA:** /ti la boˈðo nɔk u | vɪz ɔk fi ʒo/
- **Gloss:** 2SG 3SG.F.ACC call.PST NEG Q | indeed PROX.SG do.PST 1SG
- **Settles:**
  - ✔ A negative question is the declarative + *noc* + final *ou*.
  - ✔ The contradicting 'yes' is ***vis*** 'indeed, of course' + a pro-verb answer: fronted *oc* + *fair*, with inversion (*oc fey jo* 'I did so'). Relevant to the *j'oc farray* question (E10).

### E82 · I don't know where your sister works.
- **Borlish:** *Jo say noc yon ty sour laur.* (User: "*…yon laur ty sour.* feels decidedly unnatural here; maybe it would feel more natural if the subject was very long and heavy … if the where-clause were transitive with a lexical verb, it would take a *lot* to convince me to use inversion.")
- **IPA:** /ʒo se nɔk jɔn ti sur lor/
- **Gloss:** 1SG know NEG where 2SG.POSS sister work
- **Settles:**
  - ✔ An embedded wh-clause with a lexical verb has **subject–verb order**, for noun subjects as well as pronouns.
  - ✔ Inversion in embedded wh-clauses belongs to the auxiliaries and the copula (E19 *yon es y quarf*, E65 *yon son ðe eut*), or to a very heavy subject. So embedded clauses aren't V2.
  - ✔ 'Work' is *laurar* (*laur*); 'sister' is *sour*.

### E83 · Let's go home!
- **Borlish:** *Fayau repaðr!* (also *Vayau cas nos!*, "although that's more 'Let's go to our house!' (as opposed to someone else's)")
- **IPA:** /feˈjo reˈpa.ðr̩/  ·  /veˈjo kaz nɔz/
- **Gloss:** do.SBJV-1PL homecoming  ·  go.SBJV-1PL at.home.of 1PL.DSJ
- **Settles:**
  - ✔ 'Let's …' is the **1PL subjunctive imperative**, with no pronoun: *fayau*, *vayau*.
  - ✔ 'Go home' is *fair repaðr* 'make the homecoming' (*repaðr* n 'homecoming, return'). *eir cas nos* means our house as against someone else's.

### E85 · Do you know if the bakery is open?  (to a passer-by)
- **Borlish:** *Vos saveð ouð y micrman sey yert ou?* (also *Vos saveð ou, ouð y micrman sey yert?*, "potentially producible in speech, unlikely to be written like this")
- **IPA:** /vɔz saˈvɛθ uθ i ˌmɪ.kr̩ˈman si jɛrt u/
- **Gloss:** 2PL know-2PL whether DEF bakery be.SBJV open Q
- **Settles:**
  - ✔ After a questioned verb of knowing the clause is **subjunctive** (*sey*), as E64 and `tam.tex` say.
  - ✔ 'Whether' is ***ouð*** here, and the question particle *ou* goes at the **end** of the sentence. Putting *ou* straight after *saveð* is a spoken option. Before a wh-clause it stood after the verb (E19, E44).
  - ? *ouð* may be the form of *ou* 'whether' before a vowel, like *eð* for *e*. E64 has *ou l'ay*; this answer and `tam.tex` have *ouð y*; the one corpus *ouð* is also before a vowel.
  - ✔ *micrman* 'bakery' is **not in the .db**.

### E101 · I wonder whether Anna knows, or whether Marc does.
- **Borlish:** *Jo m'entrou ouð Anna lo sa, ben ou Marc lo sa.* (also *…ben ou Marc oc fey.*, "somewhat dispreferred since it's no shorter". User, in chat: *sa* was a mistake for subjunctive ***saif***, and the pro-verb option is *…ben ou Marc oc **faç***. So: *Jo m'entrou ouð Anna lo saif, ben ou Marc lo saif.*)
- **IPA:** /ʒo mɛnˈtru uθ aˈna lo sef | bɛn u mark lo sef/
- **Gloss:** 1SG REFL=wonder whether Anna 3SG.N know.SBJV | or whether Marc 3SG.N know.SBJV
- **Settles:**
  - ✔ **'Whether' is *ouð* before a vowel and *ou* before a consonant** (*ouð Anna*, *ou Marc*), like *eð*/*e*. This settles the E85 question.
  - ✔ 'Or whether' is *ben ou*.
  - ✔ After *s'entrovar* 'wonder' + *ouð* the clause is **subjunctive** (*saif*), as after a questioned *savir* (E85). The submitted *sa* was a slip.
  - ✔ The pro-verb is subjunctive too (*oc faç*). Repeating the verb is preferred, since the pro-verb saves nothing here.

### E104 · Let's not argue about it.
- **Borlish:** *Kerelleu noc dessur.* (also *Kerelleu noc sull'oç.*, "…about that". User: "I've realised that I've got duplicates *querel-* and *kerel-* in the notes; that probably needs retconning to one set of forms or the other.")
- **IPA:** /ˌke.rɛˈlau nɔk dɛˈsɪr/  ·  /…sɪˈlɔts/
- **Gloss:** argue.SBJV-1PL NEG about.it  ·  … on.DEF=DIST.SG
- **Settles:**
  - ✔ The **negative 1PL hortative** is the subjunctive with ***noc* after it**.
  - ✔ 'About it' is the bare adverb ***dessur***, with no pronoun. 'About that' is *sull'oç*.
  - ✔ The verb is ***kerellar***. *querel-* has been retconned to *kerel-* (Conflict 24).

### E111 · Who bought what?
- **Borlish:** *Cu accatau cal?*
- **IPA:** /ki ˌa.kaˈto kal/
- **Gloss:** who buy.PST which
- **Settles:**
  - ✔ A **multiple wh-question** fronts one wh-word, here the subject *cu*. The other stays in place (*cal* 'what').
  - ✔ 'What' as an object can be ***cal***.

## Negation

### E01 · Nobody wants the last egg.
- **Borlish:** *Alcun hom desir l'ou derran.* (also *Stou l'ou derran a alcun hom.* User: "somewhat odd choice of construction in this context, maybe something to do with the sort of wanting here".)
- **IPA:** /aˈgɪn ɔm deˈzɪr lu deˈran/  ·  /stu lu deˈran a aˈgɪn ɔm/
- **Gloss:** no person want DEF=egg last  ·  be.wanted DEF=egg last to no person
- **Settles:**
  - ✔ 'Nobody' is ***alcun hom***. As a preverbal subject it negates the clause on its own: there is no *noc* and no *no* on the verb.
  - ✔ 'Want' (a preference) is ***desirar***.
  - ✔ With *stovir* the wanter is an *a*-phrase after the theme (*Stou l'ou derran a alcun hom*), but *stovir* fits needing or lacking better than preferring.
  - ? *volir* wasn't used as a main verb 'want'. This is weak evidence that it is now purely an auxiliary (irregular-verbs Q18).
- **Follow-up:** The corpus has *alcun hom autr **n'**a se mis a genoil* ('no one else has knelt'), with *n'* after a preverbal *alcun hom*. Is *n'* optional there, or required because *aïr* takes preverbal *no*? (→ E31)

### E05 · There's no milk left.
- **Borlish:** *No scey plu alcun laið.* (also *Reman alcun laið.*)
- **IPA:** /no xi pli aˈgɪn leθ/  ·  /reˈman aˈgɪn leθ/
- **Gloss:** NEG there.be no.more no milk  ·  remain no milk
- **Settles:**
  - ✔ The existential *sceir* is negated with **preverbal *no*** (*No scey*). Compare the corpus *No scerraun alcun imprefait ny brevier je posc*.
  - ✔ **Negative concord:** *no*, *plu* and *alcun* co-occur and reinforce one another; they don't cancel.
  - ✔ A mass noun takes bare *alcun*, with no partitive article.
  - ✔ 'Left' is *plu* 'any more' with *sceir*, or *remanir* with the subject after the verb (*Reman alcun laið*).
  - ? A postverbal *alcun* subject also needs no negator (*Reman alcun laið*). So *alcun* may negate wherever it stands, unlike Spanish/Italian, where a postverbal n-word needs *no*/*non*. Is *No reman alcun laið* also possible?
- **Corpus survey (2026-10-12, `borlish sentences with translations.txt`, unique sentences):**
  - Preverbal *no*/*n'* appears almost only with *star*, *er*, *aïr* and *sceir*: *no's* 41, *no sta* 19, *no'r/no'rn* 16, *n'a/n'ay/n'aye/n'aun/n'au/n'eu* about 50, *no scey/sceye/scein* 14, plus *no son*, *no fo*, *no fos*, *no sera*, *no stant*.
  - It also appears with *poðir* (*no poð* 5, *no se poð* 4), but *poð(e) noc* is commoner (about 20).
  - Every other verb takes postverbal *noc*: *va noc*, *save noc*, *vole noc*, *crey noc*, *fay noc*, *acceptau noc*…
  - ? Hypothesis: **preverbal *no* is the negator of the auxiliary/copula verbs (*star*, *er*, *aïr*, *sceir*); *noc* negates everything else; *poðir* allows both.**
- **Follow-up:** E32 (*She doesn't have a car, and she can't drive either.*) tests *n'a* and *no poð* vs *poð noc*.
- **More support (batch 2):**
  - E17 *jo n'ay jamay lo vis*: *aïr* keeps preverbal *n'* even with *jamay*, whereas lexical *paroln* in E09 has *jamay* alone. So *jamay* replaces *noc*, but not *no*.
  - E12 *Nos poðau noc*: *poðir* with *noc*.
  - E22 *Jo crey noc*: lexical *creir* with *noc*.

### E22 · I don't think he knows the truth.
- **Borlish:** *Jo crey noc ig le saif y vertað.*
- **IPA:** /ʒo kri nɔk aj le sef i vɛrˈtaθ/
- **Gloss:** 1SG believe NEG COMP 3SG.M know.SBJV DEF truth
- **Settles:**
  - ✔ 'Think' is *creir*, negated with postverbal *noc*.
  - ✔ **A negated *creir* takes the subjunctive**: *saif* is the subjunctive, and the 3SG indicative is *sa*. Affirmative *creir* takes the indicative (`tam.tex`).
  - ✔ *saif* = present subjunctive SG of *savir*.
  - ✔ **The *savir* paradigm (user, 2026-10-12), which settles irregular-verbs Q17:**
    - Present: *jo say, tu sa, le/la/lo sa; nos saveu, vos saveð, ðe saun*.
    - Subjunctive: *saif* (all SG), *saivau, saivað, saivn*.
- **Follow-up:** affirmative and negated *creir* side by side (→ E53).
- **Answered by E53:** indicative after affirmative *creir*, *ig* + subjunctive after negated *creir*.

### E31 · Nobody has a key.  (locked out, all of you checking your pockets)
- **Borlish:** *Alcun hom n'a un cla.* (also *Alcun hom n'a cla.* 'Nobody has (any) keys.')
- **IPA:** /aˈgɪn ɔm na ɪn kla/
- **Gloss:** no person NEG=have INDF key
- **Settles:**
  - ✔ With *aïr*, the preverbal *n'* is **kept even after a preverbal *alcun hom***, whereas a lexical verb takes no negator there (E01 *Alcun hom desir…*). This is strong support for the E05 rule: *no*/*n'* belongs to *star*, *er*, *aïr* and *sceir* whenever they are negated.
  - ✔ A bare noun (*cla*) gives the 'any keys' reading; *un cla* is 'a key'.

### E32 · She doesn't have a car, and she can't drive either.
- **Borlish:** *La n'a un car, e la poð noc viglar lon tan.*
- **User:** "…*la sa noc*… 'she doesn't know how to', versus …*la poð noc*… 'she isn't able to (for any reason including not knowing how to, but also permission, opportunity, etc)'."
- **IPA:** /la na ɪn kar | e la pɔθ nɔk vajˈlar lɔn tan/
- **Gloss:** 3SG.F NEG=have INDF car and 3SG.F can NEG drive.INF without also
- **Settles:**
  - ✔ *aïr* takes *n'* (*n'a*), and *poðir* takes *noc* here, which fits the rule.
  - ✔ 'Not … either' is ***lon tan*** at the end of the clause (lit. 'without also').
  - ✔ ***savir* + infinitive** means 'know how to'; ***poðir* + infinitive** means 'be able to' in any sense: ability, permission, opportunity.
  - ✔ 'Drive' is *viglar*.

### E48 · I've never been to Rome.
- **Borlish:** *Jo no's jamay eut a Rom.* (also *Jo no so jamay eut a Rom.* User: "'I have', rather than 'I've'")
- **IPA:** /ʒo nɔz ʒaˈme awt a rɔm/  ·  /ʒo no so ʒaˈme…/
- **Gloss:** 1SG NEG=be.1SG never go.PST.PTCP to Rome
- **Settles:**
  - ✔ A *star* perfect keeps **preverbal *no*** alongside *jamay*, as *aïr* does (E17). So *jamay* replaces *noc*, never *no*.
  - ✔ *jamay* stands between the auxiliary and the participle.
  - ✔ 'Have been to' is ***eut*** 'gone', the *star* perfect of *eir*, not *stað*.
  - ✔ *no so* contracts to ***no's*** in speech ('I've'); the full form is more careful. *no's* therefore serves the 1SG as well as the 3SG (*no es*). Corpus: *Jo no's scur de calun* (C1967), *Jo no's deja satisfait…* (C2472).
  - ✔ A city goal takes *a* (*a Rom*), as in E14.

### E100 · Not everyone agrees.
- **Borlish:** *Noc toð gent accort.* (also *Noc toð gent no's accordant.*, "'Not everyone is agreeing', as a description of the circumstances". User, in chat: "should be *accordn*" and "*no son accordant*". So: *Noc toð gent accordn* / *Noc toð gent no son accordant*.)
- **IPA:** /nɔk tɔθ ʒɛnt aˈkɔrd.n̩/  ·  /nɔk tɔθ ʒɛnt no sɔn ˌa.kɔrˈdant/
- **Gloss:** NEG all people agree-3PL  ·  NEG all people NEG be.3PL agree-PRS.PTCP
- **Settles:**
  - ✔ A quantifier is negated by ***noc* placed before the quantified phrase**. With a lexical verb the verb itself isn't negated.
  - ✔ ***toð gent* 'everyone' takes a 3PL verb** (user correction), as in most of the corpus. Two corpus sentences have 3SG (Conflict 20).
  - ? In the progressive version the auxiliary is negated too (*no son accordant*). This may be negative concord, if *star* needs its preverbal *no* in any negative clause. E112 asks.
  - ✔ *accordar* 3PL **accordn**, PRS.PTCP **accordant**.
- **Follow-up:** E112 (concord with *star*).

### E112 · Not everyone was listening.  (after a long speech)
- **Borlish:** *Noc toð gent no'rn cur dant.* (also *Noc toð gent dan cur.*, *Noc toð gent no'rn lo scoutant.*, *Noc toð gent lo scoutan.*)
- **IPA:** /nɔk tɔθ ʒɛnt nɔrn kɪr dant/  ·  /…dan kɪr/  ·  /…nɔrn lo xuˈtant/  ·  /…lo xuˈtan/
- **Gloss:** NEG all people NEG=be.IPFV.3PL attention give-PRS.PTCP  ·  … give.IPFV.3PL attention  ·  … NEG=be.IPFV.3PL 3SG.ACC listen-PRS.PTCP  ·  … 3SG.ACC listen.IPFV.3PL
- **Settles:**
  - ✔ With the **progressive**, the auxiliary is negated as well (*no'rn*, *no son*), even when *noc* already negates the subject. This is **negative concord on the auxiliary**, as in E100.
  - ✔ With a **simple verb** there is no second negation (*dan cur*, *lo scoutan*).
  - ? The user gave no progressive without *no*, so that is presumably impossible.
  - ✔ *no'rn* is the negative of *ern* (3PL of *er*).
  - ✔ 'Listen' is ***cur dar*** 'pay attention' or ***scoutar*** with an object.

## Relative Clauses

### E07 · The woman who lives next door is a doctor.
- **Borlish:** *Y domn hamtant cas coster es sanat.*
- **IPA:** /i ˈdɔ.mn̩ hamˈtant kaz kɔˈstɛr ɛz saˈnat/
- **Gloss:** DEF woman dwell-PRS.PTCP at side be doctor
- **Settles:**
  - ✔ A **subject relative** is a present participle after the head noun, with no *ig* and no relative word.
  - ✔ 'Next door' is *cas coster* (lit. 'at (the) side').
  - ✔ A profession after the copula takes no article: *es sanat*.
- **Follow-up:**
  - How is past time shown inside a participial subject relative? (→ E39)
  - Non-restrictive relatives (→ E40).
  - Is an *ig*-clause ever possible for a subject relative?

Object relative with a pronoun subject: *toð gent meyon connuð* 'everyone I know' (E16, under *Comparison*). This confirms head + agentive + PST.PTCP.

### E23 · The letter my brother sent me never arrived.
- **Borlish:** *Y lettr m'accaçað de my fraðr me parvenoy jamay.*
- **User:**
  - "…*par my fraðr*… (implies the brother did the sending, and not necessarily the writing); …*de my fraðr*… implies the brother did the writing, and not necessarily the sending; but they are in most contexts interchangeable."
  - "…*venoy jamay*: 'never came' versus 'never reached me'."
- **IPA:** /i ˈlɛ.tr̩ ˌma.kaˈtsaθ de mi ˈfra.ðr̩ me ˌpar.veˈnɔj ʒaˈme/
- **Gloss:** DEF letter 1SG.OBL=send.PST.PTCP of 1SG.POSS brother 1SG.OBL reach.PST never
- **Settles:**
  - ✔ An **object relative with a full-NP subject** is head + PST.PTCP + *de*/*par* + NP. The agent phrase follows the participle, as with the agentive pronouns (*teyon rovað*).
  - ✔ A clitic belonging to the relative attaches to the participle (*m'accaçað* 'sent to me').
  - ✔ ***de*** marks the author or source, and ***par*** the agent of the action itself. They are usually interchangeable.
  - ✔ *parvenir* 'reach' takes an oblique clitic (*me parvenoy*), and its preterite is *parvenoy*, like *venoy*.
  - ✔ *jamay* again stands alone after a lexical verb.

### E30 · It was Jovanna who broke the window.
See *Information Structure*. A cleft uses *l'un* + a participial relative with the perfect participle *ayent … fragnt*.

### E39 · The man who was talking to Halina is my uncle.  (at a party, pointing)
- **Borlish:** *Y segr lor parolant a Halina es mell'yam.*
- **User's variants:**
  - *Y segr parolant paravant a Halina es mell'yam* ('earlier').
  - *Y segr stant parolað a Halina…* 'The man having spoken to Halina…'.
  - *Y segr a mesur lor de parolar a Halina…* 'The man who was then in the course of talking to Halina…'.
- **IPA:** /i ˈsij.r̩ lɔr ˌpa.roˈlant a ˌha.liˈna ɛz mɛˈljam/
- **Gloss:** DEF man then speak-PRS.PTCP to Halina be 1SG.POSS-DEF=uncle
- **Settles:**
  - ✔ The participle in a subject relative is **tenseless**. Past time comes from a time adverb (*lor* 'then', *paravant* 'earlier').
  - ✔ An anterior relative uses the **perfect participle** with *stant* for an intransitive verb (*stant parolað* 'having spoken'), just as transitives use *ayent* (E30).
  - ✔ A progressive periphrasis ***a mesur de* + INF** means 'in the course of'.
  - ✔ *mell'yam*: possessive + article before semivowel *y-*.

### E40 · My neighbour, who is a doctor, has gone to Spain.
- **Borlish:** *My vecin, stant sanat, es eut a Spagn.*
- **IPA:** /mi veˈtsɪn | stant saˈnat | ɛz awt a spɛjn/
- **Gloss:** 1SG.POSS neighbour be-PRS.PTCP doctor be go.PST.PTCP to Spain
- **Settles:**
  - ✔ A **non-restrictive relative** is an appositive participial clause set off by commas (*stant sanat* 'being a doctor'). There is no relative word.
  - ✔ The perfect of *eir* 'go' takes *star*: *es eut*.
  - ✔ A country goal takes *a* with no article (*a Spagn*).

### E96 · That's the man whose dog bit me.
- **Borlish:** *L'oç es y segr dont y can me mordoy.*
- **IPA:** /lɔts ɛz i sijr dɔnt i kan me mɔrˈdɔj/
- **Gloss:** DEF=DIST.SG be.3SG DEF man whose DEF dog 1SG.ACC bite.PST
- **Settles:**
  - ✔ Possessive relative: ***dont* is followed straight away by the possessed noun with its article** (*dont y can*). Here that noun is the subject, so clitic and verb follow in the usual order.
  - ✔ The corpus agrees: *dont y fraðr Lohis fo mort* (C782), *dont y dors caf appoyað* (C674). When the possessed noun is the object it still comes first, and the verb inverts: *dont y lengaç n'ay jo nien* (C719).
  - ✔ 'That's the man' is *L'oç es y segr*, with distal *l'oç*.
  - ✔ *mordr* has the preterite **mordoy**. Corpus *moroy* is *morir* 'die', not this verb.

### E119 · This is the house where I was born.
- **Borlish:** *L'oc es y majon yon jo fo nað.*
- **IPA:** /lɔk ɛz i maˈʒɔn jɔn ʒo fo naθ/
- **Gloss:** DEF=PROX.SG be.3SG DEF house where 1SG be.PST born
- **Settles:**
  - ✔ The locative relative uses ***yon*** 'where', with subject–verb order inside, as in embedded wh-clauses (E82).
  - ✔ 'Was born' is *fo nað* (E63).

## Coordination & Subordination

### E08 · If it rains tomorrow, we'll stay at home.
- **Borlish:** *Ða cay ploy je posc, nos voum remanir cas nos.*
- **IPA:** /ða ke plɔj ʒe pɔx | nɔz vum ˌre.maˈnɪr kaz nɔz/
- **Gloss:** if fall rain on.day.of after 1PL will.1PL remain.INF at.home.of 1PL.DSJ
- **Settles:**
  - ✔ An open condition about the future has the **present** after *ða*.
  - ✔ The main clause uses the *volir* future (*voum remanir*), not the synthetic future.
  - ✔ **Weather** is *cair* 'fall' + noun, with no subject: *cay ploy* 'it rains' (attested: *ða cay ploy borjonnant*).
  - ✔ 'At home' is *cas* + disjunctive: *cas nos*. *cas* is the *chez* preposition.
  - ✔ *je posc* means 'tomorrow' (lexicalised; cf. *je ados* 'yesterday').
- **Follow-up:** *cas* + full noun ('at my aunt's') comes up in E14 and E38.

### E18 · Although it was late, the shops were still open.
- **Borlish:** *Degnant ig cous tart, y varous remanen yert.* (User: *cous* is the imperfect subjunctive of *cair* 'fall, happen'; *cay tart* = 'it is late (in the day)'.)
- **IPA:** /diˈnant aj kus tart | i vaˈruz ˌre.maˈnɛn jɛrt/
- **Gloss:** although COMP fall.IPFV.SBJV late | DEF shop remain-IPFV.3PL open
- **Settles:**
  - ✔ *Degnant ig* 'although' takes the **subjunctive**, here the imperfect subjunctive because the context is past. See Conflict 5 for C166.
  - ✔ 'It is late (in the day)' is *cair* + adjective with no subject (*cay tart*), like the weather in E08.
  - ✔ 'Still open' is said with ***remanir*** + adjective ('remained open') rather than with an adverb.
  - ✔ *yert* means 'open (for business)'.
- **Follow-up:** Where does *ancour* 'still' go when it is used?

### E21 · She wrote that she would arrive on Tuesday.  (about Jovanna)
- **Borlish:** *La scavoy la vole ac yembr je Mart.* (also *La scavoy l'ig la vole…*. User: "particle ig, l'ig introducing complement clauses, optional". The first answer had *scavau*, which the user called a slip.)
- **IPA:** /la xaˈvɔj la voˈle ak ˈjɛm.br̩ ʒe mart/
- **Gloss:** 3SG.F write.PST 3SG.F will.IPFV here reach.INF on.day.of Tuesday
- **Settles:**
  - ✔ **Reported future in the past** is the imperfect of *volir* + infinitive (*la vole … yembr*). There is no tense shift beyond that.
  - ✔ The **complementiser is optional** after verbs of saying and writing. After a vowel-final word it takes the by-form *l'ig*.
  - ✔ 'On Tuesday' is *je Mart* (*je* + day name).
  - ✔ The preterite of *scaur* 'write' is **scavoy** (stem *scav-*, *-oy* type; Conflict 8), and the past participle is *scaut*.
  - ✔ 'Arrive (here)' is *ac yembr*.
- **Follow-up:** a reported pluperfect (→ E57).
- **Answered by E57:** *Le dis le fo ja paut*.

### E24 · If I had known, I would have come.  (on hearing about a party you missed)
- **Borlish:** *Ða jo saveus, jo volois ig venir.* (User: "ig, here meaning 'there', is optional, but *venir* prefers to have some explicit location." Also *…jo volois l'assistr* 'I would have attended it'.)
- **IPA:** /ða ʒo saˈvauz | ʒo voˈlɔjz aj veˈnɪr/
- **Gloss:** if 1SG know.IPFV.SBJV 1SG will.IPFV.SBJV there come.INF
- **Settles:**
  - ✔ **Past counterfactual:** *ða* + **imperfect subjunctive**, then *volois* + infinitive in the main clause.
  - ✔ The imperfect subjunctive of *savir* is 1SG **saveus**.
  - ✔ ***ig* 'there'** is a locative pro-form. It goes before the infinitive in the clitic position (*volois ig venir*), the way French *y* does. *venir* likes an explicit goal.
  - ✔ An object clitic elides before a vowel-initial infinitive: *l'assistr*.
- **Follow-up:**
  - The imperfect subjunctive of *aïr*, and clitic clusters in a counterfactual (→ E54).
  - *ig* 'there' with a finite verb (→ E56).
- **Answered:** E54 again uses the simple imperfect subjunctive (Conflict 13). E56 shows *ig* following the finite verb.

### E54 · If you had asked me, I would have told you.  (to Marc)
- **Borlish:** *Ða tu me lo rovaus, jo volois te lo digr.*
- **IPA:** /ða ti me lo roˈvoz | ʒo voˈlɔjz te lo ˈdaj.r̩/
- **Gloss:** if 2SG 1SG.OBL 3SG.N.ACC ask.IPFV.SBJV | 1SG will.IPFV.SBJV 2SG.OBL 3SG.N.ACC say.INF
- **Settles:**
  - ✔ A past counterfactual again has ***ða* + simple imperfect subjunctive** (*rovaus*: preterite *rovau* + *-s*) and ***volois* + infinitive**, as in E24. This conflicts with `tam.tex` (Conflict 13).
  - ✔ Clitics come before the finite verb in the *if* clause (*me lo rovaus*) and before the infinitive after *volois* (*te lo digr*). The order is 1st/2nd-person oblique before 3rd-person accusative.
  - ✔ *rovar* 'ask (for)' takes the person as oblique and the thing as accusative. 'It' is expressed with both verbs (*me lo rovaus*, *te lo digr*), where English leaves it out.

### E71 · If we had left earlier, we would have caught the train.
- **Borlish:** *Ða nos parteusseu tostessem, nos sceusseu montar ag convey.*
- **IPA:** /ða nɔz ˌpar.tauˈsau tɔˈstɛ.sɛm | nɔz xauˈsau mɔnˈtar ɛj kɔnˈvi/
- **Gloss:** if 1PL leave.IPFV.SBJV-1PL early.CMPR | 1PL can.IPFV.SBJV-1PL board.INF to.DEF train
- **Settles:**
  - ✔ Third past counterfactual with the **simple imperfect subjunctive** after *ða* (Conflicts 13, 13b).
  - ✔ A modal main clause takes the modal's own imperfect subjunctive (*sceusseu montar* 'could have caught'), with no *volois*.
  - ✔ *tostessem* 'earlier'; 'catch the train' is *montar ag convey*.

### E86 · Although he had studied hard, he failed the exam.
- **Borlish:** *Degnant le fos parsið con nis, le disceu ny scitaçon.* (The notebook has *fo*; the user confirmed it was a typo for *fos*. User: "*disceu*, past tense of *disceir* '(intr.) to fail, not make it, to miss a target or standard with ill effect'")
- **IPA:** /dɪjˈnant le fɔz parˈsɪθ kɔn nɪz | le diˈxau ni ˌxi.taˈtsɔn/
- **Gloss:** although 3SG.M be.IPFV.SBJV study.PST.PTCP with effort | 3SG.M fail.PST in.DEF exam
- **Settles:**
  - ✔ After *degnant* an earlier past event takes the **pluperfect subjunctive**: *fos* + PTCP, with *star* because *parsir* has no object here. So a pluperfect subjunctive exists. It is not used in counterfactuals, which take the simple imperfect subjunctive (E71).
  - ✔ 'Hard' is *con nis* 'with effort'. 'Fail (an exam)' is intransitive ***disceir*** + *ne* (*disceu ny scitaçon*).

### E91 · I asked her to wait.
- **Borlish:** *Jo luy peðeu a attendr.* (also *Jo peðeu (l'ig) l'attenois.*, "I asked (that) she wait, with subjunctive"; "I think *peðir* prefers the infinitive construction in normal use.")
- **IPA:** /ʒo laj peˈðau a aˈtɛn.dr̩/  ·  /ʒo peˈðau (laj) ˌla.teˈnɔjz/
- **Gloss:** 1SG 3SG.OBL ask.PST to wait.INF  ·  1SG ask.PST (COMP) 3SG.F=wait.IPFV.SBJV
- **Settles:**
  - ✔ **Object control** with *peðir*: the person asked is an oblique clitic (*luy*), and the action is *a* + infinitive. The corpus has the same: *La peðeu a sabler reuvr dy scitaçon* (C2745).
  - ✔ The finite alternative has the **imperfect subjunctive** after a past *peðir* (*attenois*, from the preterite *attenoy*). The complementiser can be left out.
  - ✔ ***l'ig*** is a **euphonic by-form of *ig***, in any of its senses ('that', 'there'). It may be used after a word ending in a vowel sound but need not be (user, 2026-10-13). `determiners.tex` already said so for the complementiser and now covers both senses.
- **Follow-up:** the user answered the *l'ig* question in chat, so E111 was replaced with a reserve item.

### E92 · I promised to write every week.
- **Borlish:** *Jo promis de scaur a casc semman.*
- **IPA:** /ʒo proˈmɪz de xor a kax sɛˈman/
- **Gloss:** 1SG promise.PST to write.INF at every week
- **Settles:**
  - ✔ ***promettr*** (subject control) takes ***de*** + infinitive, where *peðir* takes *a* (E91).
  - ✔ The preterite is ***promis***, like *mettr* → *mis* (corpus *promis David*, C129).
  - ✔ 'Every week' is *a casc semman*.
  - ? The time phrase follows the infinitive, though objects precede it (*d'un marið trovar*, C23). Adverbial PPs seem free to follow.

### E97 · Before you go, close the window.
- **Borlish:** *Pre tu vay, closisc y fenestr.* (plural: *Pre vos vayað, closiscað y fenestr.*)
- **IPA:** /pre ti ve | kloˈzɪx i feˈnɛs.tr̩/  ·  /pre vɔz veˈjaθ | ˌklo.ziˈxaθ i feˈnɛs.tr̩/
- **Gloss:** before 2SG go.SBJV | close.IMP DEF window  ·  before 2PL go.SBJV-2PL | close.SBJV-2PL DEF window
- **Settles:**
  - ✔ ***pre*** 'before' takes a finite clause directly, with no *ig*, and the verb is **subjunctive**: *vay*, not indicative *va*. The corpus agrees: *pre tu attent uncos novel* (C60), *pre Marc sceus…* (C227).
  - ✔ After the fronted clause the main clause is an ordinary imperative: 2SG *closisc*, the indicative, and 2PL *closiscað*, the subjunctive, as `verb-morphology.tex` says.

### E120 · I saw him leave the house.
- **Borlish:** *Jo le vis y majon salir.* (also *Jo le vis sortir dy majon.*)
- **IPA:** /ʒo le vɪz i maˈʒɔn saˈlɪr/  ·  /…sɔrˈtɪr di maˈʒɔn/
- **Gloss:** 1SG 3SG.M.ACC see.PST DEF house leave.INF  ·  … go.out.INF from.DEF house
- **Settles:**
  - ✔ A **perception verb** takes a **bare infinitive**. The perceived person is a clitic on the perception verb (*le vis*).
  - ✔ The infinitive's object comes before it (*y majon salir*). With *sortir* 'go out' the source follows as a prepositional phrase (*sortir dy majon*).

### E125 · I heard her singing in the kitchen.
- **Borlish:** *Jo l'oyeu cantar ny cocin.* (also *Jo l'oyeu star cantant ny cocin.*, "I heard her be singing…"; *Jo l'oyeu oc cantant ny cocin.*, "I heard her, who was singing…")
- **IPA:** /ʒo lɔˈjau kanˈtar ni koˈtsɪn/  ·  /…star kanˈtant…/  ·  /…ɔk kanˈtant…/
- **Gloss:** 1SG 3SG.F=hear.PST sing.INF in.DEF kitchen
- **Settles:**
  - ✔ Perception verbs take a **bare infinitive** for an ongoing action too (compare E120).
  - ✔ A progressive infinitive (*star cantant*) is possible.
  - ✔ ***oc* + participle** forms a non-restrictive reduced relative ('her, who was singing'). The corpus has the same: *y Çaucr Azur Marian (oc instaurað a Lepcy)*, C2699.

### E126 · Unless you hurry, you'll miss the train.
- **Borlish:** *Preðauc tu quauc, tu kiglara y convey.* ("subjunctive (not visible on *quaucar* 'to proceed with haste')")
- **IPA:** /preˈðok ti kwok | ti ˌkaj.laˈra i kɔnˈvi/
- **Gloss:** unless 2SG hurry.SBJV | 2SG miss-FUT DEF train
- **Settles:**
  - ✔ 'Unless' is ***preðauc*** + **subjunctive**.
  - ✔ A fronted adverbial clause does not trigger inversion (*tu kiglara*), as in E50.
  - ✔ 'Miss (a train)' is *kiglar*.

## Comparison

### E04 · Halina is taller than me, but shorter than her brother.
- **Borlish:** *Halina es hautessem a mey, ma mognessem a sy fraðr.*
- **IPA:** /ˌha.liˈna ɛz hoˈtɛ.sɛm a mi | ma mɔjˈnɛ.sɛm a si ˈfra.ðr̩/
- **Gloss:** Halina be tall.CMPR to 1SG.DSJ but short.CMPR to 3SG.POSS brother
- **Settles:**
  - ✔ The standard of comparison is marked with ***a*** 'than'.
  - ✔ A pronoun standard is **disjunctive**: *a mey*.
  - ✔ 'Tall' is *haut* → *hautessem*.
  - ✔ 'Short' in stature is *mogn* → *mognessem*. *brey* is short in length or time.
  - ✔ The subject and copula are left out of the second conjunct after *ma*: *ma mognessem a sy fraðr*.

### E16 · She sings better than anyone I know.
- **Borlish:** *La cant ottem a toð gent meyon connuð.*
- **IPA:** /la kant ˈɔ.tɛm a tɔθ ʒɛnt miˈjɔn kɔˈnɪθ/
- **Gloss:** 3SG.F sing better to all people 1SG.AGT know.PST.PTCP
- **Settles:**
  - ✔ 'Better' as an adverb is *ottem*, the suppletive comparative of *bon*, used bare.
  - ✔ The standard is marked with *a*.
  - ✔ 'Anyone' in the standard is universal *toð gent* ('than everyone I know'), not *alcun*.
  - ✔ An object relative with a pronoun subject is head + agentive + PST.PTCP: *toð gent meyon connuð*.
- **Follow-up:**
  - The lexicon has *megl* (adv) 'better' and lists *ottem* only as an adjective 'best, greatest'. How do adverbial *ottem* and *megl* divide the work? (→ E47)
  - The *ottem* entry could add 'better'.
- **Answered by E47:** *megl* is obsolete; *ottem* covers both (Conflict 12).

### E47 · She sings well, but he sings better.
- **Borlish:** *La cant fort, ma le cant ottem.* (The notebook has *ottom*, which the user confirmed was a typo.)
- **User:** "*megl* is outdated, yeah. It should be *ottem* throughout for 'better' and 'best' both as an adjective or an adverb."
- **IPA:** /la kant fɔrt | ma le kant ˈɔ.tɛm/
- **Gloss:** 3SG.F sing well | but 3SG.M sing better
- **Settles:**
  - ✔ 'Well' is the adverb ***fort*** (`.db`: 'well, really').
  - ✔ ***ottem*** is the only form for 'better' and 'best', as adjective and adverb. ***megl*** **is obsolete** (Conflict 12, now applied). It survives only in *meglfair* 'improve' and *meglfacçon* 'improvement'.
  - ✔ The verb is repeated in the second conjunct (*ma le cant ottem*). In E04 the subject was shared, so subject and copula could go.

### E60 · The more you read, the more you understand.  (said generally)
- **Borlish:** *Moutessem leir, moutessem comprendr.* (also *Maissem leir, maissem comprendr*, "for a more specific sense of 'greater quantity of the objects of the verbs' over 'doing the thing more'")
- **IPA:** /muˈtɛ.sɛm lir | muˈtɛ.sɛm kɔmˈprɛn.dr̩/  ·  /ˈme.sɛm lir | ˈme.sɛm kɔmˈprɛn.dr̩/
- **Gloss:** more.often read.INF | more.often understand.INF
- **Settles:**
  - ✔ 'The more …, the more …' repeats the comparative at the head of each half, with **bare infinitives**. There is no subject, so the generic 'you' doesn't arise.
  - ✔ ***moutessem*** is the comparative of *mout* 'often'; ***maissem*** is the comparative of ***gran*** 'big' (user, 2026-10-13), so 'greater (amount)'.
- **Follow-up:** a generic 'you' with a finite verb (→ E77).

### E69 · This is the oldest bridge in the city.
- **Borlish:** *L'oc es y pont y veilessem ny citað.*
- **IPA:** /lɔk ɛz i pɔnt i viˈlɛ.sɛm ni tsiˈtaθ/
- **Gloss:** DEF=PROX.SG be DEF bridge DEF old.CMPR in.DEF city
- **Settles:**
  - ✔ The **superlative** follows the noun with its own article (*y pont y veilessem*), even for prenominal *veil*.
  - ✔ The domain is ***ne*** 'in' (*ny citað*).

### E95 · He is as old as my father.
- **Borlish:** *Le's veðr com my paðr.* (also *Le's tan veðr com my paðr.*, "a bit like 'He is just as old as my father', with some emphasis")
- **IPA:** /lez ˈvɛ.ðr̩ kɔm mi ˈpa.ðr̩/  ·  /lez tan ˈvɛ.ðr̩ kɔm mi ˈpa.ðr̩/
- **Gloss:** 3SG.M=be.3SG old as 1SG.POSS father  ·  3SG.M=be.3SG so old as 1SG.POSS father
- **Settles:**
  - ✔ Equative: **adjective + *com* + standard**, with no degree word.
  - ✔ *tan* ADJ *com* is the **emphatic** 'just as … as'.
  - ? The corpus *tan … com* tokens are negated or have a clause as the standard: *no stan … tan retenuð com tu speraus* (C1431), *con tan farvour com tu aye lo vuscað* (C1412). E113 checks negation.
- **Follow-up:** E113 (*tan* under negation).

### E109 · I have more books than you, but fewer friends.
- **Borlish:** *J'ay livr maissem a tey, ma amig men.* ("…*a vos*…" for polite 2SG. User, in chat: *maissem* "would mean 'bigger books', not 'more books'. It should be *livr may a tey*.")
- **IPA:** /ʒe ˈli.vr̩ me a ti | ma aˈmaj mɛn/  (corrected form)
- **Gloss:** 1SG=have book more to 2SG.DSJ | but friend fewer
- **Settles:**
  - ✔ A quantity comparison puts the quantifier **after the noun**: *livr may* 'more books', *amig men* 'fewer friends'. The standard is ***a* + disjunctive**, as with adjectives (E04).
  - ✔ 'More' is ***may*** and 'fewer' is ***men***. ***maissem*** is the comparative of *gran* 'big', so *livr maissem* means 'bigger books'. E123 checks mass nouns.
  - ✔ The second conjunct leaves out the verb and the standard.
- **Follow-up:** E123 ('less' with a mass noun).

### E113 · My car isn't as fast as yours.
- **Borlish:** *My car no's tan veloç com y tien.* (also *…com y vostr.*; *My car no's veloç com y tien / y vostr.*)
- **IPA:** /mi kar nɔz tan veˈlɔts kɔm i tjɛn/  ·  /…i ˈvɔs.tr̩/
- **Gloss:** 1SG.POSS car NEG=be.3SG so fast as DEF yours.SG  ·  … DEF yours.PL
- **Settles:**
  - ✔ ***tan* is optional under negation too**. The user offers both versions.
  - ✔ A **possessive pronoun** is the article + *tien*/*vostr* (*y tien* 'yours').
  - ✔ *no's* is the negative 3SG of the copula.

### E123 · I have less time than you.
- **Borlish:** *J'ay hour men a tey.* (also *…a vos.*)
- **IPA:** /ʒe ur mɛn a ti/
- **Gloss:** 1SG=have time less to 2SG.DSJ
- **Settles:**
  - ✔ ***men*** after the noun is both 'fewer' and 'less'. Comparing quantities works the same way for count and mass nouns (E109).
  - ✔ 'Time' is *hour*.

## Information Structure

### E30 · It was Jovanna who broke the window.  (correcting someone who blamed Theo)
- **Borlish:** *Jovanna sta l'un ayent y fenestr fragnt.*
- **IPA:** /ˌʒo.vaˈna sta lɪn eˈjɛnt i feˈnɛs.tr̩ frɛjnt/
- **Gloss:** Jovanna be.IPFV DEF=one have-PRS.PTCP DEF window break.PST.PTCP
- **Settles:**
  - ✔ The **cleft** is an identificational copular sentence: FOCUS + copula + ***l'un*** 'the one' + participial relative. There is no dummy 'it'. Compare *luy es l'un dont…*.
  - ✔ Past clefts use imperfect *sta*.
  - ✔ The **perfect participle** is *ayent* + object + PST.PTCP ('having broken'), with the object between the two parts as in the finite perfect.
  - ✔ *fragnt* is the past participle of *fragndr* 'shatter'.
- **Follow-up:** clefting an object (→ E55).
- **Answered by E55:** *Y soup es l'oç noc meyon amað*.

### E17 · That film, I've never seen it.
- **Borlish:** *L'oç lasc, jo n'ay jamay lo vis.*
- **IPA:** /lɔts lax | ʒo ne ʒaˈme lo vɪz/
- **Gloss:** DEF=DIST.SG film | 1SG NEG=have.1SG never 3SG.N.ACC see.PST.PTCP
- **Settles:**
  - ✔ **Left dislocation:** the topic NP comes first, set off by a pause, and a resumptive clitic follows (*lo*).
  - ✔ In an *aïr* perfect, *jamay* stands between the auxiliary and the participle, and the clitic stays on the participle (*n'ay jamay lo vis*).
  - ✔ *aïr* keeps its preverbal *n'* alongside *jamay* (see *Negation*, E05).
- **Follow-up:** A *star* perfect with *jamay* (→ E48).
- **Answered by E48:** *Jo no's jamay eut a Rom*: *star* keeps *no* too.

### E20 · Everyone was laughing, even the king.
- **Borlish:** *Toð gent ern ricottant, y rey meðes.*
- **IPA:** /tɔθ ʒɛnt ɛrn ˌri.kɔˈtant | i ri meˈðɛz/
- **Gloss:** all people COP.IPFV-3PL laugh-PRS.PTCP | DEF king even
- **Settles:**
  - ✔ 'Everyone' is *toð gent*, with **plural** agreement (*ern*).
  - ✔ The past progressive is *er* + PRS.PTCP.
  - ✔ 'Even' (*meðes*) **follows** the NP it focuses, as in *y goppietandessem meðes* 'even the most surprising' (C1969).

### E55 · It's the soup that I don't like.  (at dinner, pushing the bowl away)
- **Borlish:** *Y soup es l'oç noc meyon amað.* (also *Y soup es l'oç noc me plagnt*, "using *plagr* 'to please'")
- **IPA:** /i sup ɛz lɔts nɔk miˈjɔn aˈmaθ/  ·  /… nɔk me plɛjnt/
- **Gloss:** DEF soup be DEF=DIST.SG NEG 1SG.AGT love.PST.PTCP  ·  … NEG 1SG.OBL please.PRS.PTCP
- **Settles:**
  - ✔ An **object cleft** is FOCUS + copula + ***l'oç*** 'that one' + an object relative (agentive + PST.PTCP): *l'oç meyon amað* 'the one loved by me'. The present cleft has *es*.
  - ✔ The participle is negated by ***noc* placed before it** (*noc meyon amað*). This is constituent negation; with a finite verb *noc* follows the verb.
  - ✔ 'Like' is ***amar*** ('love, like'), or ***plagr*** 'please' with the experiencer as an oblique clitic: *l'oç noc me plagnt* 'the one not pleasing me' (PRS.PTCP *plagnt*).
  - ? The subject cleft in E30 had *l'un* (*Jovanna sta l'un ayent…*). Is the choice of *l'oç* or *l'un* about a thing against a person, or about object against subject? (→ E74)

### E74 · It was Marc I saw at the station, not Theo.
- **Borlish:** *Marc sta l'un meyon vis ag quarf, noc Theo.*
- **IPA:** /mark sta lɪn miˈjɔn vɪz ɛj kwarf | nɔk θeˈo/
- **Gloss:** Marc be.IPFV DEF=one 1SG.AGT see.PST.PTCP at.DEF station | NEG Theo
- **Settles:**
  - ✔ A clefted **person** takes ***l'un*** even as an object, so *l'un* vs *l'oç* is **person vs thing**, not subject vs object (E30, E55).
  - ✔ Constituent negation puts *noc* before the NP (*noc Theo*).

### E84 · — Who broke this vase? — I did.
- **Borlish:** *Cu rompoy l'oc vas? Mey, j'oc fey.* (User: *Mey.* is just 'It was me.'; "*J'oc fey.*, on its own, is more 'I *did*.' than '*I* did.'; it focuses the fact of having done it, rather than the identity of who did it.")
- **IPA:** /ki rɔmˈpɔj lɔk vaz | mi | ʒɔk fi/
- **Gloss:** who break.PST DEF=PROX.SG vase | 1SG.DSJ | 1SG=PROX.SG do.PST
- **Settles:**
  - ✔ A short answer naming the person is the bare **disjunctive** *Mey*.
  - ✔ ***oc* + *fair*** is the pro-verb 'do so', with *oc* in clitic position (*j'oc fey*). On its own it focuses the fact of doing, not the doer; *Mey, j'oc fey* does both. With fronted *oc* and inversion it contradicts (E79 *Vis oc fey jo!*).
  - ✔ This answers E10: preverbal *oc* as the object of *fair* is current, not just literary.
  - ✔ *rompoy* is the *-oy* preterite of *rompr* 'break'.

### E90 · I only invited Sarah.
- **Borlish:** *Jo convoccau for Sarah.*
- **IPA:** /ʒo ˌkɔn.vɔˈko fɔr saˈra/
- **Gloss:** 1SG invite.PST only Sarah
- **Settles:**
  - ✔ 'Only' is ***for***, placed right before the constituent it restricts (compare corpus *for un inaltour*, *no stant for catr annað*, *Jo no's for hom*).
  - ✔ 'Invite' is *convoccar*.

### E105 · I only wanted to help.
- **Borlish:** *Jo desira for aïðar.* ("if the 'only' restricts 'help' (I wanted to help, and I didn't want anything else)"; also *Soul jo desira aïðar.*, "if the 'only' restricts the 'want' (the only thing I did was want to help)")
- **IPA:** /ʒo ˌde.ziˈra fɔr ˌɛj.iˈðar/  ·  /sul ʒo ˌde.ziˈra ˌɛj.iˈðar/
- **Gloss:** 1SG want.IPFV only help.INF  ·  alone 1SG want.IPFV help.INF
- **Settles:**
  - ✔ ***for*** restricts a verb phrase from just before the infinitive.
  - ✔ To restrict the main verb, ***soul*** goes **before the whole clause**.
  - ? *Soul jo desira* has no inversion, so clause-initial *soul* seems to stand outside the V2 count, like a conjunction (compare *soulor*, E50). E121 asks.
  - ✔ 'Want' is *desirar* (imperfect *desira*).
- **Follow-up:** E121 (*soul* and V2).

### E110 · What I need is a long holiday.
- **Borlish:** *L'oç meyon recas es un cogmað lonc.* (also *L'oç me stovent es…*)
- **IPA:** /lɔts miˈjɔn reˈkaz ɛz ɪn kɔjˈmaθ lɔnk/  ·  /lɔts me stoˈvɛnt ɛz…/
- **Gloss:** DEF=DIST.SG by.me require.PST.PTCP be.3SG INDF holiday long  ·  DEF=DIST.SG 1SG.OBL be.needed-PRS.PTCP be.3SG …
- **Settles:**
  - ✔ A **pseudocleft** is *l'oç* + a participial clause + copula. The experiencer is either the **agentive pronoun** *meyon* with a past participle (*meyon recas*, as in *l'oç seyon rovað*, `determiners.tex`) or an oblique clitic with *stovent* (*me stovent*).
  - ✔ ***recas*** is the **past participle of *recarr*** 'require, need' (user; *recarr* is in the .db). The corpus *aïr recas* (C667 *n'aye recas* 'had needed', C976 *n'aun recas* 'don't need') is therefore the perfect of *recarr*, and *candon recas* (C808) is 'when needed'.
  - ✔ 'Holiday' is *cogmað*, with the adjective after it.

### E121 · Only Marc knew the answer.
- **Borlish:** *For Marc sa y soluçon.* (User: "*For* [subject]… restricts the subject (Marc, and no-one else). *Soul*… restricts the verb (Marc *knew* it, and didn't do anything else to or with it).")
- **IPA:** /fɔr mark sa i ˌso.liˈtsɔn/
- **Gloss:** only Marc know DEF solution
- **Settles:**
  - ✔ ***for*** restricts the constituent that follows it, including a subject (*For Marc sa…*). The verb is still second.
  - ✔ Clause-initial ***soul*** restricts the **predicate**, not the subject (*Soul Marc sa…* 'Marc only *knew* it'). It stands outside the V2 count (E105).
  - ? Whether a fronted *for* + non-subject triggers inversion is still open. E141 asks.
- **Follow-up:** E141 (*for* + fronted non-subject).

## Voice & Valency

Weather verbs: see E08 (*cay ploy*). Causative *fair* + infinitive: see E03.

### E13 · The bridge was built by the Romans.
- **Borlish:** *Y pont fo costroit par y Roman.* (User: "*Y pont er costroit par y Roman.* would be describing an ongoing process at the time of discussion (The bridge was being built...). *Y pont sta costroit* cannot (I think) take an agent, and means 'The bridge was (in the state of having been) built.'")
- **IPA:** /i pɔnt fo koˈstrɔjt par i roˈman/
- **Gloss:** DEF bridge be.PST build.PST.PTCP by DEF Roman
- **Settles:**
  - ✔ The **event passive** is *fo* (the preterite of *star*) + PST.PTCP, with the agent in a ***par***-phrase.
  - ✔ The **progressive passive** is *er* + PST.PTCP ('was being built').
  - ? The **stative/resultative passive** is *sta* + PST.PTCP ('was in a built state'), probably with no agent.
  - ✔ 'The Romans' is *y Roman*: an unmarked plural with the article.
  - So the passive auxiliary follows the same aspect split as the copula itself.
- **Corpus retconned to this system on 2026-10-12** (Conflict 7). E41–E43 test the edges: an agent with a state, and events with a date.

### E41 · The castle was destroyed by the Normans in 1066.
- **Borlish:** *Y castel fo destroit par y Normant d'an 1066.*
- **IPA:** /i kaˈstɛl fo dɛˈstrɔjt par i nɔrˈmant dan …/ (the year isn't read yet)
- **Gloss:** DEF castle be.PST destroy.PST.PTCP by DEF Norman of=year 1066
- **Settles:**
  - ✔ A dated, one-off event takes the **event passive *fo* + PTCP** with a *par* agent, not *er*. This is the system the corpus was retconned to (Conflict 7).
  - ✔ 'In (year)' is ***d'an*** + year, as in the corpus (*d'an 1778*).
  - ✔ *destroit* is the PST.PTCP of *destroir* (*r* class). *Normant* 'Norman' is an unmarked plural after the article (not in the `.db`).
- **Follow-up:** How is a year read aloud? (→ E63 *My grandmother was born in 1931.*)

### E42 · When we arrived, the house was being painted and the door was already locked.
- **Borlish:** *Cant nos venoim, y majon er pegntað eð y port sta ja zamicað.*
- **IPA:** /kant nɔz veˈnɔjm | i maˈʒɔn ɛr pɪjnˈtaθ eθ i pɔrt sta ʒa ˌza.miˈkaθ/
- **Gloss:** when 1PL come.PST-1PL | DEF house COP.IPFV paint.PST.PTCP and DEF door be.IPFV already lock.PST.PTCP
- **Settles:**
  - ✔ Both non-event passives occur in one sentence: ***er* + PTCP** for a process under way (*er pegntað* 'was being painted') and ***sta* + PTCP** for the resulting state (*sta … zamicað* 'was locked'). This confirms E13.
  - ✔ ***ja*** 'already' stands between the auxiliary and the participle, like *jamay* (E17, E48).
  - ✔ *cant* 'when' takes the preterite (*venoim*) for a point in past time.
  - ✔ The fronted *cant* clause doesn't trigger inversion in the main clause (*y majon er…*). See *The Simple Clause*.
  - ✔ 'And' is ***eð*** before a vowel (*eð y port*). Corpus: *eð* + vowel about 243 times, *e* + vowel about 40; *eð y* 95, *e y* 3.
  - ✔ *venoim* is the 1PL preterite of *venir* (*-oy* type, like *scavoim*).

### E43 · The palace was surrounded by soldiers.  (the morning after the coup)
- **Borlish:** *Y palaç sta cercondað con soldart.*
- **IPA:** /i paˈlats sta ˌtsɛr.kɔnˈdaθ kɔn sɔlˈdart/
- **Gloss:** DEF palace be.IPFV surround.PST.PTCP with soldier
- **Settles:**
  - ✔ A state described after the event takes *sta* + PTCP.
  - ✔ What makes up the state is introduced with ***con*** 'with', not *par*: the soldiers are the surrounding, not agents acting. This fits E13 (*sta* takes no agent). Compare French *entouré de*.
  - ? So *sta* … *par* is avoided. The corpus keeps *frugt sta conservað par meyan…* 'preserved by means of' (C512), where *par* is 'by means of'. But *Y sovragl seyon me dað sta adornað par fylau* 'adorned with flowers' (C2552, also in `pronouns.tex`) might want *con* by this answer (→ E68).


### E27 · The captain made them wait outside.
- **Borlish:** *Y capitan lou fey attendr a starn.* (User: "…*tras port* (if outside e.g. a room or building).")
- **IPA:** /i ˌka.piˈtan lu fi aˈtɛn.dr̩ a starn/
- **Gloss:** DEF captain 3PL.ACC do.PST wait.INF at outside
- **Settles:**
  - ✔ The causative is ***fair* + infinitive**.
  - ✔ **The causee pronoun climbs to the causative verb** (*lou fey attendr*). This is unlike modals, where clitics stay on the infinitive (*Jo no poð lou affaçar*). So causative *fair* + infinitive forms a single verbal unit.
  - ✔ The causee of an intransitive infinitive is accusative (*lou*).
  - ✔ *fey* is the preterite of *fair*.
  - ✔ 'Outside' is *a starn* (out of doors) or *tras port* (outside a room or building).
- **Follow-up:**
  - The causee of a transitive infinitive (→ E52).
  - Permissive *laiscar* (→ E51).
- **Answered:** E51 uses *parmettr de* + infinitive, not *laiscar*. E52 shows that only the causee climbs to *fair*.

### E51 · She let us borrow her car.
- **Borlish:** *La nos parmis de sy car emprontar.*
- **IPA:** /la nɔz parˈmɪz de si kar ˌɛm.prɔnˈtar/
- **Gloss:** 3SG.F 1PL.OBL permit.PST of 3SG.POSS car borrow.INF
- **Settles:**
  - ✔ 'Let' is ***parmettr*** 'permit' + ***de*** + infinitive. *laiscar* means only 'leave' in the `.db`, and wasn't used.
  - ✔ The person allowed is a clitic on *parmettr* (*nos parmis*). This is the verb's own indirect object, as in French *nous a permis de*, not climbing.
  - ✔ The infinitive's object goes between *de* and the infinitive (*de sy car emprontar*).
  - ✔ *parmis* is the preterite of *parmettr* (corpus 4×). 'Borrow' is *emprontar*.
- **Follow-up:** the imperative 'Let me help you!' (→ E76).

### E52 · The teacher made the children wash their hands.
- **Borlish:** *L'instroyour fey l'eç ivan y man se landar.* (with pronouns: *L'instroyour lou fey lou landar.*)
- **IPA:** /ˌlɪn.strɔˈjur fi lɛts iˈvan i man se lanˈdar/  ·  /ˌlɪn.strɔˈjur lu fi lu lanˈdar/
- **Gloss:** DEF=teacher make.PST DEF=DIST.PL child DEF hand REFL wash.INF  ·  DEF=teacher 3PL.ACC make.PST 3PL.ACC wash.INF
- **Settles:**
  - ✔ With a transitive infinitive, the **causee is still a plain object**, with no *a*. It comes straight after *fair*, before the infinitive's own object: *fey [l'eç ivan] [y man] se landar*.
  - ✔ **Only the causee's clitic climbs** to *fair* (*lou fey*). The infinitive's object clitic stays on the infinitive (*lou landar*). So E27's 'single verbal unit' needs narrowing: *fair* attracts its own causee, not the infinitive's clitics.
  - ✔ The causee pronoun is accusative *lou* even with a transitive infinitive (French would have *leur*).
  - ✔ A **body part** takes the article, and the possessor is a reflexive *se* on the verb: *y man se landar* 'wash their hands' (like French *se laver les mains*).
  - ? With a pronoun object the reflexive is absent: *lou landar*, not *se lou landar*. Is *se* dropped whenever the body part is a pronoun? (→ E75)
  - ? *l'eç* (DEF + DIST.PL) marks a plain plural definite here ('the children'). `determiners.tex` §Demonstratives and number gives only *l'ec* for weak-deixis plurals.

### E68 · The belt she gave me was decorated with flowers.  (question misquoted the corpus; see Conflict 15)
- **Borlish:** *Y sovragl seyon me dað sta adornað par con flour.* (*par* was a leftover; the intended answer is *…sta adornað con flour*.)
- **IPA:** /i soˈvrɛjl siˈjɔn me daθ sta ˌa.dɔrˈnaθ par kɔn flur/
- **Gloss:** DEF belt 3.AGT 1SG.OBL give.PST.PTCP be.IPFV decorate.PST.PTCP by with flower
- **Settles:**
  - ✔ A decorated state takes ***con*** for the decoration, like E43. The corpus sentence (which had *par fylau* 'with crows') now reads *con flour* (Conflict 15).

### E93 · The door opened by itself.
- **Borlish:** *Y port s'ovreu toð soul.* (User, in chat: "go with *ovroy* then; I just forgot the form". So: *Y port s'ovroy toð soul.*)
- **IPA:** /i pɔrt sɔˈvrɔj tɔθ sul/
- **Gloss:** DEF door REFL=open.PST all alone
- **Settles:**
  - ✔ The **anticausative** takes reflexive ***se***.
  - ✔ 'By itself' is ***toð soul*** 'all alone'.
  - ✔ The preterite of *ovrir* is ***ovroy*** (user), as in `verb-morphology.tex` (Conflict 19).
  - ✔ *closir* likewise needs *se* (E114). The corpus once had a plain intransitive, *Y port dy cahut closisceu* (C2026), but it now reads *Y port dy cahut se closisceu* (Conflict 25).
- **Follow-up:** E114 (is *se* needed?).

### E114 · The door closed.  (nobody touched it)
- **Borlish:** *Y port se closisceu.* (User: "Good catch! I think *closir* should be transitive, so I've fixed the cases of intransitive *closir* in the Scaunç file (elsewhere will need aligning).")
- **IPA:** /i pɔrt se ˌklo.ziˈxau/
- **Gloss:** DEF door REFL close.PST
- **Settles:**
  - ✔ ***closir* is transitive**, so the anticausative needs ***se***, as with *ovrir* (E93). The corpus is aligned (Conflict 25).

## Copulas & Modals

Existential *sceir* under negation: see E05. Experiencer *stovir* with an *a*-phrase: see E01.

### E12 · We couldn't find the station.
- **Borlish:** *Nos poðau noc y quarf trovar.* (also *Nos sceum noc y quarf trovar.* User: "Imperfect for a state of inability; simple past for a punctual event of non-success.")
- **IPA:** /nɔz poˈðo nɔk i kwarf troˈvar/  ·  /nɔz xaum nɔk i kwarf troˈvar/
- **Gloss:** 1PL can-IPFV.1PL NEG DEF station find.INF  ·  1PL can.PST-1PL NEG DEF station find.INF
- **Settles:**
  - ✔ The preterite stem of *poðir* is the suppletive *sceu-*, with 1PL **sceum**. This answers the CHECK in `tam.tex` (line 98).
  - ✔ The imperfect is used for a state of inability and the preterite for a one-off failure. This is the usual aspect split, applied to a modal.
  - ✔ *poðir* takes postverbal *noc* here.
  - ✔ The object comes before the infinitive.

### E26 · We had to wait two hours at the border.  (from a letter home)
- **Borlish:** *Nos eum attendr dou hour ag tarmn.*
- **User:**
  - "*Nos eyau…* (imperfective). Aspect depends on whether it's describing an event that happened and is over, or it's describing a state of affairs (in which case it's cancellable, as in 'We had to wait two hours, so we decided to take the ferry instead')."
  - "…*tras dou hour*… 'for two hours'. Mostly interchangeable; the version with *tras* is perhaps more usual than the version without in speech."
- **IPA:** /nɔz aum aˈtɛn.dr̩ du ur ɛj ˈtar.mn̩/
- **Gloss:** 1PL go.PST-1PL wait.INF two hour at.DEF border
- **Settles:**
  - ✔ This answers the CHECK in `tam.tex` (line 336). The **preterite of *eir* 'have to'** (*eum*) is used for an obligation that was carried out. The **imperfect** (*eyau*) states an obligation as a state of affairs that could still be **cancelled** ('we had to wait, so we took the ferry instead').
  - ✔ A duration is a bare NP (*dou hour*) or *tras* + NP. *tras* is a little more usual in speech.

### E28 · He became a teacher after the war.  (about an old family friend)
- **Borlish:** *Le denoy instroyour posc y var.* (also *…aðelent…*, 'private teacher or tutor')
- **IPA:** /le deˈnɔj ˌɪn.strɔˈjur pɔx i var/
- **Gloss:** 3SG.M become.PST teacher after DEF war
- **Settles:**
  - ✔ The **preterite of *denir* is *denoy*** (irregular-verbs Q21; *deneu* is out).
  - ✔ A profession after 'become' is bare, as after 'be' (E07).
  - ✔ 'After the war' is *posc y var*.
  - ✔ *instroyour* is a teacher, *aðelent* a tutor.

### E70 · I'm cold, and the children are hungry.
- **Borlish:** *J'ay freit, eð y joun famiscn.* (also *…eð y joun aun fam*, "somewhat more current in speech, where *famir* tends to read as 'starve' or childish complaint")
- **IPA:** /ʒe frit | eθ i ʒun faˈmɪx.n̩/  ·  /…eθ i ʒun on fam/
- **Gloss:** 1SG=have.1SG cold | and DEF young be.hungry-3PL
- **Settles:**
  - ✔ Bodily states are ***aïr*** + noun/adjective: *aïr freit* 'be cold', *aïr fam* 'be hungry'. *famir* (ir2) reads as 'starve' or a child's complaint.
  - ✔ *y joun* 'the kids'.

### E89 · He seemed tired.
- **Borlish:** *Le parisce las.* ("direct sensory deduction from his appearance or voice or something"; also *Orruða le fos las.*, "more like 'It seemed like he was tired'; this could include sensory deduction but also indirect surmising")
- **IPA:** /le ˌpa.riˈxe laz/  ·  /ˌɔ.riˈða le fɔz laz/
- **Gloss:** 3SG.M seem-IPFV tired  ·  seem-IPFV 3SG.M be.IPFV.SBJV tired
- **Settles:**
  - ✔ Personal ***parir*** + adjective reports a direct sensory impression. Impersonal ***orruðar*** + subjunctive clause (no *ig*) covers inference and surmise too.
  - ✔ The imperfect of *orruðar* is the regular **orruða**, which settles irregular-verbs Q23 (Conflict 18). *parisce* is the imperfect of *parir* (ir2).

### E103 · — Can you swim? — Yes, I can.  (to Halina)
- **Borlish:** *Tu sa najar ou? Ja, j'oc sa.* (also *Tu poð… j'oc poð*, "if it's about permission or opportunity, rather than knowing how to")
- **IPA:** /ti sa naˈʒar u | ʒa ʒɔk sa/
- **Gloss:** 2SG know swim.INF Q | yes 1SG=PROX.SG know
- **Settles:**
  - ✔ A learned ability is ***savir* + infinitive**. *poðir* is for permission or opportunity.
  - ✔ The short answer keeps the modal with ***oc*** as its object (*j'oc sa*, *j'oc poð*), like *j'oc fey* (E84).
  - ✔ 'Swim' is *najar* ('sail, travel by water' in the .db).

### E106 · He seems to know you.
- **Borlish:** *Le parisc te connoscr.* (also *Orruð (ig) le te connosc.*, "same distinction as before")
- **IPA:** /le paˈrɪx te kɔˈnɔ.xr̩/  ·  /ɔˈrɪθ (aj) le te kɔˈnɔx/
- **Gloss:** 3SG.M seem 2SG.ACC know.INF  ·  seem (COMP) 3SG.M 2SG.ACC know
- **Settles:**
  - ✔ Personal ***parir* + infinitive** reports a direct impression. Impersonal ***orruðar* + clause** covers surmise, as in E89.
  - ✔ With *parir* the clitic object of the infinitive goes before the infinitive (*te connoscr*).
  - ? After *orruðar* the complementiser *ig* is optional. E89 had none.
  - ✔ The mood after *orruðar* is **subjunctive**. *connosc* is ambiguous, but E122 has *l'ay*, and E89 had *fos*.
- **Follow-up:** E122 (mood after *orruðar*).

### E122 · It seems she has a new car.
- **Borlish:** *Orruð l'ay un novel car.* (also *Orruð ig l'ay un novel car.*, "interchangeable, as 'It seems that she…' and 'It seems she…' are")
- **IPA:** /ɔˈrɪθ le ɪn noˈvɛl kar/  ·  /ɔˈrɪθ aj le…/
- **Gloss:** seem 3SG.F=have.SBJV INDF new car
- **Settles:**
  - ✔ *orruðar* takes the **subjunctive** (*ay*). This settles the open question from E106.
  - ✔ ***ig* is optional** after *orruðar*, freely.

## Tense, Aspect & Mood

Present after *ða* for a future condition, and the *volir* future: see E08. *vil lo fair* vs *farray*: see E10.
- Future in the past, *vole* + INF: E21.
- Past counterfactual, *ða* + IPFV.SBJV and *volois* + INF: E24.
- Aspect of *eir* 'have to': E26.
- Subjunctive after a negated *creir*: E22.
- Future subjunctive *vel* + infinitive after a negated *creir*: E53.
- Reported pluperfect *fo* + participle: E57.
- Past counterfactual with the simple imperfect subjunctive: E54 (Conflict 13).

### E25 · We've decided to stay another week.  (from a letter home)
- **Borlish:** *Nos som decis de se tenir par un semman ancour.*
- **User:** "This doesn't do the probe, since the infinitive is in an indirect *de …*. I can't immediately think of an example that would work. 'I've seen him eat an apple' would be *J'ay le vis un pom pascr.*"
- **IPA:** /nɔz sɔm deˈtsɪz de se teˈnɪr par ɪn sɛˈman anˈkur/  ·  /ʒe le vɪz ɪn pɔm ˈpax.r̩/
- **Gloss:** 1PL be.1PL decide.PST.PTCP of REFL hold.INF for INDF week more  ·  1SG=have.1SG 3SG.M.ACC see.PST.PTCP INDF apple eat.INF
- **Settles:**
  - ✔ *decidr* with a *de* + infinitive complement takes ***star*** in the perfect (*som decis*). The complement isn't a direct object, so this fits the rule that the auxiliary follows how the verb is used.
  - ✔ This answers the CHECK in `tam.tex` (line 109). With a perception verb, the **infinitival complement follows the participle**, and the perceived person's clitic stays on the participle: *J'ay le vis [un pom pascr]*. The infinitive's own object goes before the infinitive. Compare *J'ay neyað a y bon solution augrimar*. Only nominal objects sit between the auxiliary and the participle.
  - ✔ 'Stay' is reflexive *se tenir*, and 'another week' is *un semman ancour*.
  - ✔ Duration with *par* (*par un semman*).

### E53 · I think he knows, but I don't think he'll tell us.
- **Borlish:** *Jo crey le sa, ma jo crey noc ig le vel nos lo digr.*
- **IPA:** /ʒo kri le sa | ma ʒo kri nɔk aj le vɛl nɔz lo ˈdaj.r̩/
- **Gloss:** 1SG believe 3SG.M know | but 1SG believe NEG COMP 3SG.M will.SBJV 1PL.OBL 3SG.N.ACC say.INF
- **Settles:**
  - ✔ Affirmative *creir* takes the **indicative** (*le sa*); negated *creir* takes the **subjunctive**. This confirms E22 side by side.
  - ✔ A future in a subjunctive clause is the **subjunctive of *volir*** + infinitive (*le vel … digr*), as `tam.tex` says (line 300).
  - ✔ The clitics go before the infinitive, oblique *nos* before accusative *lo*.
  - ? *ig* is left out after affirmative *creir* but present after negated *creir* (here and in E22). Is *ig* required, or just usual, when the clause is subjunctive?

### E57 · He said he had already eaten.
- **Borlish:** *Le dis le fo ja paut.*
- **IPA:** /le dɪz le fo ʒa pot/
- **Gloss:** 3SG.M say.PST 3SG.M be.PST already eat.PST.PTCP
- **Settles:**
  - ✔ An earlier event in reported speech takes the **pluperfect**, here with the preterite auxiliary: *fo … paut*. There's no complementiser (E29).
  - ✔ *pascr* used without an object takes ***star***, as the auxiliary follows how the verb is used (E25). So *fo* + PTCP is the pluperfect of an intransitive verb but the event passive of a transitive one; the two don't collide.
  - ✔ *ja* 'already' stands between the auxiliary and the participle (E42).
  - ✔ *paut* is the PST.PTCP of *pascr* (corpus: *Nos erau paut ny refectoir*).
  - ? `tam.tex` §The pluperfect says the imperfect auxiliary (*er*) states what had been done by the reference point, and the preterite (*fo*) presents a single event. 'Had already eaten' looks like the first kind, but the user chose *fo*. Is *Le dis le er ja paut* also possible? (→ E72)

### E64 · I don't know whether he has children.
- **Borlish:** *Jo say noc ou l'ay figl.* (User: in *Le reconnosc ou sy fraðr sey tan demastr?* "it's the question particle, where a verb of knowledge (*reconnoscr*), when questioned, governs the subjunctive.")
- **IPA:** /ʒo se nɔk u le fajl/
- **Gloss:** 1SG know NEG whether 3SG.M=have.SBJV child
- **Settles:**
  - ✔ 'Whether' after a negated *savir* is *ou*, and the clause is **subjunctive** (*ay*, not *a*). This settles CHECK tam:260.
  - ✔ A questioned or negated verb of knowing governs the subjunctive (Conflict 14).

### E72 · By the time we arrived, the guests had already left.
- **Borlish:** *All'hour yon nos yemoim ig, l'host ern ja partið.*
- **IPA:** /aˈlur jɔn nɔz jeˈmɔjm aj | lɔst ɛrn ʒa parˈtɪθ/
- **Gloss:** at.DEF=hour where 1PL arrive.PST-1PL there | DEF=guest COP.IPFV-3PL already leave.PST.PTCP
- **Settles:**
  - ✔ A state at the reference point takes the pluperfect with imperfect ***er*** (*ern ja partið*), as `tam.tex` says; E57's *fo* presents an event. Both exist.
  - ✔ 'By the time' is ***all'hour yon***. *ig* follows *yemoim*. No inversion after the fronted clause.

### E87 · They won't help us.
- **Borlish:** *Ðe noun nos aïðar.* ("suggesting that they don't want to"; also *Ðe nos aïðaraun noc.*, "suggesting that they will be unable to")
- **IPA:** /ðe nun nɔz ˌɛj.iˈðar/  ·  /ðe nɔz ˌɛj.i.ðaˈron nɔk/
- **Gloss:** 3PL NEG.FUT.3PL 1PL.ACC help.INF  ·  3PL 1PL.ACC help-FUT.3PL NEG
- **Settles:**
  - ✔ The 3PL of *nolir* is **noun**, which settles CHECK tam:207 (1).
  - ✔ ***nolir*** + infinitive is a **refusal** ('won't' = unwilling). The synthetic future + *noc* is plain prediction ('won't be able to').
  - ✔ The clitic goes before the infinitive with *nolir*, and before the finite verb with the synthetic future.

### E88 · Look, the baby's sleeping!
- **Borlish:** *Vey, y babe dorm!* ("when the fact of sleeping or having gone to sleep is the notable thing"; also *Vey, y babe's dorment!*, "when the currentness of the process of sleeping is the notable thing (e.g. as a backdrop to imply that we should be quiet); this wants some sort of follow-up, implied or explicit")
- **IPA:** /vi | i baˈbe dɔrm/  ·  /…i baˈbez dɔrˈmɛnt/
- **Gloss:** look | DEF baby sleep  ·  … DEF baby=be sleep-PRS.PTCP
- **Settles:**
  - ✔ This answers CHECK tam:50. The **simple present** reports an event in progress when the event itself is the news. The **present progressive** *star* + PRS.PTCP presents the ongoing process as a backdrop and implies a consequence.
  - ✔ The contraction *'s* for *es* also follows a vowel-final noun (*y babe's*), not just the pronouns.
  - ✔ 'Look!' is *Vey*, the indicative 2SG of *veir*.

### E102 · When I came in, the baby was sleeping.
- **Borlish:** *Candon j'entrau, y babe er dorment.* (also *…y babe'r dorment.*, "rather colloquial or informal writing". User: "*er dorment* over *dorme* because it's referring to a continuous process with interior time.")
- **IPA:** /kanˈdɔn ʒɛnˈtro | i baˈbe ɛr dɔrˈmɛnt/  ·  /…i baˈbɛr dɔrˈmɛnt/
- **Gloss:** when 1SG=enter.PST | DEF baby be.IPFV sleep-PRS.PTCP
- **Settles:**
  - ✔ The **past progressive** is ***er* + PRS.PTCP**. It is used for a process with internal duration that frames an event, in preference to the simple imperfect.
  - ✔ This answers CHECK tam:171: the past progressive uses *er*, not *sta*.
  - ✔ *er* contracts to ***'r*** after a vowel (*y babe'r*), in colloquial or informal writing.
  - ✔ 'When' with a past event is ***candon*** + preterite.

### E107 · She wouldn't tell me her name.  (she refused)
- **Borlish:** *La nole sy nom me digr.* (also *La noleu sy nom me digr.*, "usual difference between imperfect and preterite, depending on whether it's a description or an event")
- **IPA:** /la noˈle si nɔm me ˈdaj.r̩/  ·  /la noˈlau…/
- **Gloss:** 3SG.F refuse.IPFV 3SG.POSS name 1SG.OBL say.INF
- **Settles:**
  - ✔ A past refusal is ***nolir*** + infinitive, in either the **imperfect** *nole* (description) or the **preterite** ***noleu*** (event). So *nolir* has a preterite.
  - ✔ In the infinitive phrase the object noun phrase comes first, then the clitic, then the infinitive (*sy nom me digr*).

### E124 · I doubt that he knows.
- **Borlish:** *Jo dout ou le oc saif.*
- **IPA:** /ʒo dut u le ɔk sef/
- **Gloss:** 1SG doubt whether 3SG.M PROX.SG know.SBJV
- **Settles:**
  - ✔ ***doutar*** takes ***ou*** 'whether' (not *ig*) + **subjunctive**, like *s'entrovar* (E101) and a questioned *savir* (E85).
  - ✔ The object is the pronoun ***oc*** 'it', placed before the verb in clitic position.

### E128 · That must be the postman.
- **Borlish:** *L'oç sera l'hom accaç.*
- **IPA:** /lɔts seˈra lɔm aˈkats/
- **Gloss:** DEF=DIST.SG be.FUT DEF=person post
- **Settles:**
  - ✔ The **epistemic future** expresses a present inference: *sera* 'must be'. This answers CHECK tam:192.
  - ✔ 'Postman' is *hom accaç*.

## Verb Morphology

New or confirmed forms (also entered in `irregular-verbs.md`):
- *dar* imperative 2SG **da** (E02).
- *fair* future 1SG **farray** (E10).
- *remanir* present 3SG **reman** (E05). This was already in the table; Q22 (1SG *reman* vs *remain*) is still open.
- *sceir* present 3SG **scey** (E05; already in the table).
- *accatar* preterite 3SG **accatau** (E06; regular).
- *deskeðar* imperative/present SG **deskieð** (E10). The stressed stem vowel *e* → *ie*, as in *venir* → *vien*.
- *dar* preterite 2SG **dau** (E11; already in the table).
- *poðir* imperfect 1PL **poðau**, preterite 1PL **sceum** (E12; table updated).
- *eir* present 1SG **vay** (E14; already in the table).
- *dormir* present 3PL **dormn** (E15).
- *costroir* PST.PTCP **costroit** (E13); *connoscr* PST.PTCP **connuð** (E16).
- *cair* imperfect subjunctive **cous** (E18; user-confirmed, noted under Q19).
- *remanir* imperfect 3PL **remanen** (E18; already in the table).
- *volir* present subjunctive **vel** with a 2SG subject (E19).
- *scaur* 'write': preterite **scavoy, scavoim, scavoist, scavoirn** (user, 2026-10-12; corpus retconned). PST.PTCP *scaut*.
- *denir* preterite 3PL **denoirn** (corpus 4×; the *-oy* preterites form their 3PL in *-oirn*).
- *savir* (user, 2026-10-12):
  - present **say, sa, sa, saveu, saveð, saun**;
  - present subjunctive **saif** (SG), **saivau, saivað, saivn**;
  - imperfect subjunctive 1SG **saveus** (E24).
- *parvenir* preterite **parvenoy** (E23).
- *eir* preterite 1PL **eum**, imperfect 1PL **eyau** (E26; already in the table).
- *fair* preterite **fey** (E27).
- *denir* preterite **denoy** (E28; Q21 settled).
- *digr* 'say' preterite 1SG **dis** (E29).
- *decidr* PST.PTCP **decis**; *fragndr* PST.PTCP **fragnt** (E25, E30).
- 2SG imperatives: *venir* **vien** (indicative; plural *vinað* is subjunctive, E34); *toccar* **toc** (E35). See Conflict 2.
- *sgardar* preterite 3PL **sgardaurn** (E36).
- *pascr* 1PL present **pascm** (E38). **All *-r* verbs:** present plural *-m, -ð, -n* (user, 2026-10-12; Conflict 10).
- Closed set with a subjunctive 2SG imperative: *sey, ay, faç, saif, remain*; *eir* → **va** (Conflict 2).
- *destroir* PST.PTCP **destroit** (E41).
- *venir* preterite 1PL **venoim** (E42).
- *savir* present 2SG **sa** (E44; confirms the paradigm). *hamtar* 3SG **hamt**.
- *volir* present subjunctive 2PL **veleð** as a polite imperative (E45).
- *stovir* present 3SG **stou** (E46).
- *star* 1SG **so**, contracted after *no* to **no's** (E48).
- *eir* preterite 2SG **eu** (E49; already in the table). *galar* preterite 2SG/3SG **galau**.
- *parmettr* preterite 3SG **parmis** (E51; corpus 4×).
- *volir* subjunctive **vel** as a future subjunctive (E53).
- *rovar* imperfect subjunctive 2SG **rovaus** (E54; regular, preterite *rovau* + *-s*).
- *amar* PST.PTCP **amað**; *plagr* PRS.PTCP **plagnt** (E55).
- *eir* present 2SG **va**, 1SG **vay** (E56; in the table).
- *digr* preterite 3SG **dis** (E57). *pascr* PST.PTCP **paut** (E57; corpus 2×).
- E61–E80: *s'entrovar* present SG **entrou**; *attendr* preterite 1PL **attenoim**; plural imperatives **entreð**, **asseyað**; *famir* 3PL **famiscn**; *partir* IPFV.SBJV 1PL **parteusseu**, PST.PTCP **partið**; *poðir* IPFV.SBJV 1PL **sceusseu**, subjunctive SG **pos**; *yembr* preterite 1PL **yemoim**; *nolir* 1SG **nil**; *parmettr* imperative **parmet**; *aïðar* subjunctive SG **aïð**; *landar* **landau**, *darfar* **darfau**, *boðar* **boðau**; *grandir* PST.PTCP **grandið** (reflexive, with *aïr*).
- E81–E90: *admirar* 1SG **admir**; *laurar* 3SG **laur**; 1PL subjunctive imperatives **fayau**, **vayau**; *rompr* preterite **rompoy**; *parsir* PST.PTCP **parsið** (with *star*); *disceir* preterite **disceu**; *nolir* 3PL **noun**; *aïðar* future 3PL **aïðaraun**; *veir* imperative **vey**; *dormir* PRS.PTCP **dorment**; *parir* imperfect **parisce**; *orruðar* imperfect **orruða** (Q23); *convoccar* preterite **convoccau**.
- E91–E100: *peðir* preterite **peðeu**; *attendr* IPFV.SBJV **attenois**; *promettr* preterite **promis**; *ovrir* preterite **ovroy** (user correction); *mordr* preterite **mordoy**; *eir* subjunctive 2SG **vay**, 2PL **vayað**; *closir* imperative **closisc**, 2PL **closiscað**; *teir* imperfect 3PL **teyen**; *sceir* imperfect 3PL **sceyen**; *souvr* PST.PTCP **soluð**; *accordar* 3PL **accordn** (user correction of *accort*), PRS.PTCP **accordant**.
- Q24 (user, 2026-10-13): *p* is kept before *-oy* (*rompoy*, *interrompoy*, *tarrompoy*; corpus retconned, Conflict 21). *d* after *n* is usually lost (*penoy*, *attenoy*, *descenoy*). *vendoy* was an artefact of obsolete *vendr*, retconned to *vençar* (Conflict 22).
- E101–E110: *s'entrovar* 1SG **entrou**; *entrar* preterite 1SG **entrau**; *er* contracted **'r**; *najar* INF; *kerellar* SBJV 1PL **kerelleu**; *desirar* imperfect **desira**; *parir* present 3SG **parisc**; *orruðar* present 3SG **orruð**; *nolir* imperfect **nole**, preterite **noleu** (new); *apportar* imperative **apport**; *stovir* PRS.PTCP **stovent**.
- E111–E120: *er* NEG 3PL **no'rn**; *dar* IPFV 3PL **dan**, PRS.PTCP **dant**; *scoutar* IPFV 3PL **scoutan**, PRS.PTCP **scoutant**; *closir* preterite **closisceu**; *cantar* 3SG **cant**; *eir* preterite **eu**; *remanir* 1SG **remain** (Q22), PRS.PTCP **remanent**; *veir* preterite **vis**.
- E121–E130: *orruðar* 3SG **orruð** + SBJV **ay**; *doutar* 1SG **dout**; *oyir* preterite **oyeu**; *quaucar* SBJV **quauc**; *kiglar* FUT **kiglara**; *surcair* preterite **surcou** (Q19 evidence); *pascr* preterite **pau**; *star* FUT **sera**; *yembr* PST.PTCP **yent** (with *star*).

## Pronouns

### E09 · The twins never speak to each other.
- **Borlish:** *Y jammel se paroln jamay a lou meðes.* (Corrected in chat; the notebook first had *…jamay lou meðes*.)
- **IPA:** /i ʒaˈmɛl se paˈrɔl.n̩ ʒaˈme a lu meˈðɛz/
- **Gloss:** DEF twin REFL speak-3PL never to 3PL.DSJ self
- **Settles:**
  - ✔ A **reciprocal** is *se* on the verb plus ***lou meðes*** 'each other' (the lexicon also lists it as 'themselves').
  - ✔ When the reciprocal is an indirect object, *lou meðes* takes *a*: *a lou meðes*.
  - ✔ When it is a direct object, there is no *a*: *Y scuir sceurn s'ojar lou meðes* (corpus).
  - ✔ ***jamay*** 'never' negates on its own. It follows the finite verb, and there is no *noc*.
- **Follow-up:** How are 'each other' and 'themselves' kept apart when both readings are possible? (→ E36)

### E36 · They looked at each other, and then at themselves in the mirror.
- **Borlish:** *Ðe se sgardaurn lou meðes, e soulor lou a cascun pall'argent.*
- **IPA:** /ðe se zgarˈdorn lu meˈðɛz | e suˈlɔr lu a kaˈxɪn ˌpa.larˈʒɛnt/
- **Gloss:** 3PL REFL look-PST.3PL 3PL.DSJ self and then 3PL.DSJ to each by.DEF=mirror
- **Settles:**
  - ✔ The reciprocal is *se* + verb + ***lou meðes*** (E09).
  - ✔ The **distributive reflexive** 'each … himself/herself' is ***lou a cascun*** ('them, to each'). It keeps the two readings apart.
  - ✔ The verb is left out of the second conjunct (*e soulor lou a cascun…*).
  - ✔ 'In the mirror' is *pall'argent* (*argent* 'silver; mirror').

Also in this batch: pronoun after *a* 'than' is disjunctive (E04); pronoun order and forms after a positive command (E02); reflexive as disjunctive in a negative command (E10); *cas* + disjunctive (E08).

### E56 · — Are you going to the market? — Yes, I'm going there now.  (to Halina)
- **Borlish:** *Tu va ag marcað ou? Ja, jo vay ig par oy.* (also *…oy vay jo ig.* User: "*par oy* is just a stronger form of 'now', like 'right now'.")
- **IPA:** /ti va ɛj marˈkaθ u | ʒa | ʒo ve aj par ɔj/  ·  /ɔj ve ʒo aj/
- **Gloss:** 2SG go to.DEF market Q | yes | 1SG go.1SG there for now  ·  now go.1SG 1SG there
- **Settles:**
  - ✔ ***ig* 'there' follows the finite verb** (*jo vay ig*), unlike the object clitics, which go before it. When the subject is inverted, *ig* follows the subject too (*oy vay jo ig*). So *ig* behaves like a postverbal adverb rather than a clitic. E24's *volois ig venir* fits this, with *ig* straight after the finite verb.
  - ✔ A fronted *oy* 'now' triggers inversion (*oy vay jo*), which is more support for V2.
  - ✔ A bare ***Ja*** answers 'yes', and the clause follows in full.
  - ✔ ***par oy*** 'right now' is a stronger *oy*.
  - ✔ The polar question has final *ou*; *ag* is *a* + *y*.
- **Follow-up:** Where does *ig* go in a perfect: after the auxiliary or after the participle? (→ E73)

### E73 · I've been there twice, but I'm not going back.
- **Borlish:** *Jo's ig eut alcheðr, ma jo nil retornar.*
- **IPA:** /ʒoz aj awt alˈkɛ.ðr̩ | ma ʒo nɪl ˌre.tɔrˈnar/
- **Gloss:** 1SG=be.1SG there go.PST.PTCP twice | but 1SG NEG.FUT return.INF
- **Settles:**
  - ✔ In a perfect, ***ig* follows the auxiliary** (*Jo's ig eut*): it goes after the finite verb (E56).
  - ✔ 'Twice' is *alcheðr*; 'won't' is ***nolir*** + infinitive (1SG *nil*).

### E75 · She washed her hair, and then she dried it.
- **Borlish:** *La se landau y cavel, e soulor la lou darfau.*
- **IPA:** /la se lanˈdo i kaˈvɛl | e suˈlɔr la lu darˈfo/
- **Gloss:** 3SG.F REFL wash.PST DEF hair | and then 3SG.F 3PL.ACC dry.PST
- **Settles:**
  - ✔ Body part = article + reflexive *se*; **the *se* drops when the body part is a pronoun** (*la lou darfau*), as in E52.
  - ✔ *cavel* 'hair' is plural (*lou*).

### E77 · You never know what might happen.
- **Borlish:** *Se poð jamay savir cal pos avenir.*
- **IPA:** /se pɔθ ʒaˈme saˈvɪr kal pɔz ˌa.veˈnɪr/
- **Gloss:** REFL can never know.INF what can.SBJV happen.INF
- **Settles:**
  - ✔ **Generic 'you/one'** is ***se*** with a 3SG verb.
  - ✔ 'Might' is the subjunctive *pos* of *poðir* in the embedded question. *jamay* alone with *poðir*.

### E80 · My brother and I went to the market.
- **Borlish:** *My fraðr e mey eum ag marcað.* (also *My fraðr e mey, nos eum ag marcað*, "more spoken and familiar")
- **IPA:** /mi ˈfra.ðr̩ e mi aum ɛj marˈkaθ/
- **Gloss:** 1SG.POSS brother and 1SG.DSJ go.PST-1PL to.DEF market
- **Settles:**
  - ✔ In a coordinated subject 'I' is **disjunctive *mey***, placed second, with 1PL agreement.
  - ✔ Speech prefers dislocation with resumptive *nos*.

## Nouns & the Noun Phrase

### E15 · My mother's three old cats sleep all day.
- **Borlish:** *Y tre veil cat a my maðr dormn toð y jorn.*
- **IPA:** /i tre vil kat a mi ˈma.ðr̩ ˈdɔr.mn̩ tɔθ i ʒɔrn/
- **Gloss:** DEF three old cat to 1SG.POSS mother sleep-3PL all DEF day
- **Settles:**
  - ✔ NP order: ART + NUM + ADJ + N + possessor phrase.
  - ✔ The article stays with a numeral (*y tre*).
  - ✔ *veil* 'old' goes **before** the noun.
  - ✔ A human possessor is marked with ***a*** (*a my maðr*), not *de*. Compare predicative *fo stað a Marco* 'had been Marco's'.
  - ✔ 'All day' is *toð y jorn*.
- **Follow-up:**
  - Is *a* the general marker for human possessors, with *de* for other relations ('the roof of the house')? (→ E46)
  - **Answered in part by E46:** part–whole takes *de*. The user isn't sure of the general split (Conflict 11).
  - Which other adjectives go before the noun (*bon, gran, picq*…)?

### E46 · The roof of my mother's house needs repairing.
- **Borlish:** *Stou y fastig dy majon a my maðr emendar.*
- **User:** "Honestly I'm not actually sure of the distribution of *de* versus *a* in possessive constructions. It's possible that I've been inconsistent."
- **IPA:** /stu i faˈstaj di maˈʒɔn a mi ˈma.ðr̩ ˌe.mɛnˈdar/
- **Gloss:** need DEF roof of.DEF house to 1SG.POSS mother repair.INF
- **Settles:**
  - ✔ Part–whole takes ***de*** (*y fastig dy majon*), and the human possessor takes ***a*** (*a my maðr*), as in E15.
  - ✔ 'X needs repairing' is ***stovir* + X + infinitive**, with *stovir* first: *Stou [y fastig …] emendar*. X stands before the infinitive like any object.
  - ? *a my maðr* could also be read as *stovir*'s experiencer ('my mother needs the roof of the house repaired'), as in E01 *Stou l'ou derran a alcun hom*. Here the possessor reading is intended.
- **Corpus:** human possessors take both *a* and *de*; see Conflict 11.

### E61 · Is this Hector's key, or his father's?
- **Borlish:** *L'oc es y cla a Hector, ben a sy paðr?* (User: "physical possessions that one can hold use *a* possession, but more abstract possession might use *de*?")
- **IPA:** /lɔk ɛz i kla a hɛkˈtɔr | bɛn a si ˈpa.ðr̩/
- **Gloss:** DEF=PROX.SG be DEF key to Hector | or to 3SG.POSS father
- **Settles:**
  - ✔ Ownership of a physical object takes ***a***; the head noun is left out after *ben* (*ben a sy paðr*).
  - ✔ An alternative question with *ben* and no *ou* (E59).

### E62 · My brother's eyes are blue.
- **Borlish:** *My fraðr es azur d'ogl.* (also *L'eç ogl a my fraðr son azur.* User: body parts should use *a*.)
- **IPA:** /mi ˈfra.ðr̩ ɛz aˈzɪr dɔjl/  ·  /lɛts ɔjl a mi ˈfra.ðr̩ sɔn aˈzɪr/
- **Gloss:** 1SG.POSS brother be blue of=eye
- **Settles:**
  - ✔ 'Blue-eyed' is predicated of the person: ***es* ADJ *de* + body part**.
  - ✔ **Body parts take *a*** (Conflict 11). *l'eç* again marks a plain plural (Conflict 16).

### E81 · I admire my father's courage.
- **Borlish:** *J'admir l'audaç de my paðr.* (User: "character traits feel like they come 'from' a person, which is why I felt drawn to *de* here.")
- **IPA:** /ʒadˈmɪr loˈdats de mi ˈpa.ðr̩/
- **Gloss:** 1SG=admire DEF=courage of 1SG.POSS father
- **Settles:**
  - ✔ A character trait takes ***de***: it comes 'from' the person. This confirms the working rule (Conflict 11): *a* for body parts and owned things, *de* for what relates to or comes from a person.
  - ✔ 'Admire' is *admirar*; 'courage' is *audaç*.

'Everyone' = *toð gent* with plural agreement: E20.

### E94 · Dogs are loyal animals.
- **Borlish:** *Can son animal treu.*
- **IPA:** /kan sɔn ˌa.niˈmal trau/
- **Gloss:** dog be.3PL animal loyal
- **Settles:**
  - ✔ A **generic plural is a bare noun**, as `determiners.tex` says. Nouns have no plural ending, so plurality shows only on the verb (*son*).
  - ✔ The predicate noun is bare too, with the adjective after it.
  - ✔ This answers the `nouns.tex` stub on genericity.

### E108 · Bring me a cup of tea and two slices of bread.
- **Borlish:** *Apport mey un cop de tag e dou trenc de pan.* (Corrected in chat to *un cop a tag e dou trenc a pan*; see Conflict 23. User: "I'm not actually sure whether measure phrases tend to use *a* or *de* in the notes. I'm inclining with retrospect to *de*, as in a piece 'from' the thing.")
- **IPA:** /aˈpɔrt mi ɪn kɔp de tɛj e du trɛnk de pan/
- **Gloss:** bring.IMP 1SG.DSJ INDF cup of tea and two slice of bread
- **Settles:**
  - ✔ The 2SG imperative is the indicative (*apport*), followed by the disjunctive *mey*, as the chapters say.
  - ✔ A measure phrase is **measure noun + *a* + bare noun**: *un cop a tag*, *dou trenc a pan* (user, after Conflict 23), like the corpus *veðr a brandvin*, *trenc a lox*, *pajot a savon*. This is the possessive *a* extended to measures.

### E129 · Not the red one, the green one.
- **Borlish:** *Noc y roug, y vert.*
- **IPA:** /nɔk i ruj | i vɛrt/
- **Gloss:** NEG DEF red | DEF green
- **Settles:**
  - ✔ An adjective with the article stands alone as a noun ('the red one').
  - ✔ ***noc*** comes before the negated constituent.

## Adjectives

### Position of *novel* (from E06; the user's question)
- *novel* occurs about 25 times before the noun and about 16 times after it in the corpus. Excluded: the noun *novel* 'news', and the names *Magl Urban Novel* and *Novel Enterpris*.
- **The same meaning appears in both positions**:
  - 'the new King': *dy Rey novel* (C381/481) vs *Y novel rey Andre II* (C390).
  - 'the new road': *posc y rout novel ovroy* (C647) vs *Y novel rout* (C456).
- So the variation is inconsistency, not a meaning difference.
- Postnominal instances, for reference (corpus line numbers):
  - 13 *un method novel* 'a new recipe'
  - 60 *uncos novel* 'something new'
  - 381 *dy Rey novel*
  - 409 *souject novel* 'new subjects'
  - 522 *Y period trevagl novel* 'his new hours'
  - 647 *y rout novel*
  - 1858 *y stat novel* 'the new states'
  - 1932 *sy cigl novel* 'her new girlfriend'
  - 1969 *un exuberanç novel* 'a new enthusiasm'
  - 2226 *sy lasc novel* 'her new film'
  - 2250 *Ty dois tach novel* 'your new smartphone'
  - 2505 *doctrin novel* 'new thinking'
  - 2708 *un við novel* 'a new life'
  - 2793 *bevis novel*, *y moneð novel* 'new notes, the new currency'
  - 2794 *dy moneð novel*
  - 2815 *corporal novel* 'new elements'
- ✔ **Decision (user, 2026-10-12): *novel* is prenominal.** It stays postnominal only after an indefinite pronoun (*uncos novel* 'something new') and in names (*Magl Urban Novel*).
- **Applied 2026-10-12.** 17 Scaunç sentences were changed, including *y vige novel* → *y novel vige* 'the new rich' and *y reyaum petty novel* → *y novel reyaum petty*. The IPA, phonetic and gloss lines of the four glossed blocks were reordered too. The change was also made in:
  - the corpus file (16 sentences);
  - the `.db` `\xv` lines (4);
  - 11 output files (verified identical to a scratch regeneration);
  - `pronouns.tex` (the *sy novel cigl* example);
  - the `adjectives.tex` plan comment.
- Nothing was found in the vault or the claims file. Left alone: `Data/pre-2022 notes.txt` (frozen) and `planning/verb-tokens.tsv` (a dated harvest).
- The postnominal list above is kept as a record of what changed.

Prenominal adjectives so far: *novel* (decided), *veil* (E15), *bel* (E58).

## Adverbs

*jamay* position: see E09 and E17. *plu* 'any more' in negative concord: see E05.
- **Two adverb formations, two registers (E14):** a bare adjective is neutral (*Jo vay primer…*); *cos* + adjective is slightly more formal (*cos primer*).
- *ottem* 'better' is used as an adverb (E16).
- *meðes* 'even' follows the phrase it focuses (E20).
- 'Still' can be expressed with the verb *remanir* + adjective (E18).
- *fort* 'well' (E47). *ottem* is 'better/best' for adjective and adverb. *megl* is obsolete (E47, Conflict 12); it survives in *meglfair* and *meglfacçon*.
- *ja* 'already' stands between the auxiliary and the participle (E42).
- *primer* fronted triggers inversion; *soulor* is a conjunction and doesn't (E50).
- *oy* 'now' fronted triggers inversion; *par oy* 'right now' (E56).
- *ig* 'there' follows the finite verb (E56).
- *moutessem* 'more (often)' vs *maissem* 'more (in quantity)' in correlatives (E60).

### E116 · She sings beautifully.
- **Borlish:** *La cant bel.* (also *La cant cos bel.*, "less elegant here; some verb-adverb pairs collocate well without *cos*, especially common ones, and especially with intransitive verbs")
- **IPA:** /la kant bɛl/
- **Gloss:** 3SG.F sing beautiful
- **Settles:**
  - ✔ A **bare adjective** serves as a manner adverb in common verb–adverb collocations, especially with intransitive verbs.
  - ✔ ***cos* + adjective** is the general adverb, and is less elegant where a collocation exists (compare E14).

### E117 · He almost fell off the ladder.
- **Borlish:** *L'eu sauf a cair des y scagler.*
- **IPA:** /lau sof a ker dɛz i xɛjˈlɛr/
- **Gloss:** 3SG.M=go.PST safe to fall.INF from DEF ladder
- **Settles:**
  - ✔ 'Almost' with a verb is ***eir sauf a*** + infinitive (a .db phrase). The tense goes on *eir* (*eu*).
  - ✔ 'Off' is ***des*** 'from'.
  - ✔ ***scagler*** 'ladder' is **not in the .db**.
  - ? This sidesteps Q19, the preterite of *cair*. E131 asks it directly.
- **Follow-up:** E131 (preterite of *cair*).

### E130 · He hasn't arrived yet, but his luggage is already here.
- **Borlish:** *Le no's ja ac yent, ma sy carc veyaçour es ac deja.* ("*deja* preferred over *ja* in constituent-final position, I think")
- **IPA:** /le nɔz ʒa ak jɛnt | ma si kark ˌvi.jaˈtsur ɛz ak deˈʒa/
- **Gloss:** 3SG.M NEG=be.3SG yet here arrive.PST.PTCP | but 3SG.POSS load travel be.3SG here already
- **Settles:**
  - ✔ 'Yet' in a negative is ***ja***, between the auxiliary and the participle.
  - ✔ ***deja*** 'already' is preferred at the **end** of a constituent; *ja* is used inside the verb phrase.
  - ✔ *yembr* takes *star* in the perfect (*no's … yent*).
  - ✔ 'Luggage' is *carc veyaçour* 'travel load'.
- **Follow-up:** E142 (*ja* vs *deja*).

## Prepositions

- *cas* + disjunctive/noun 'at the home of' (E08); *cas coster* 'next door' (E07).
- *a* marks the standard of comparison (E04, E16), the experiencer of *stovir* (E01), an indirect reciprocal (E09), a goal city (*a Londr*, E14) and a human possessor (*a my maðr*, E15).
- *cas* + NP also covers motion 'to someone's house' (*cas my morrig*, E14).
- *par* introduces the agent of a passive (E13).
- A preposition is fronted with its wh-object (*A cu…?*, E11; *Con cu…?*, E49).
- *cosogr* 'together with', of a partner or date (E49).
- *con* introduces the material of a state passive (*sta cercondað con soldart*, E43).
- *de* marks part–whole (*y fastig dy majon*); *a* a human possessor (E46; Conflict 11).
- *d'an* + year 'in (year)' (E41).

### E14 · I'm going to London first, and then to my aunt's.
- **Borlish:** *Jo vay primer a Londr, e soulor cas my morrig.* (also *Jo vay cos primer…*, "slightly more formal")
- **IPA:** /ʒo ve priˈmɛr a ˈlɔn.dr̩ | e suˈlɔr kaz mi moˈraj/
- **Gloss:** 1SG go.1SG first to London and then at.home.of 1SG.POSS aunt
- **Settles:**
  - ✔ A goal city takes ***a*** with no article (*a Londr*).
  - ✔ 'To someone's house' is ***cas*** + NP.
  - ✔ 'First … then' is *primer … soulor*.
  - ✔ The verb is left out of the second conjunct.
  - ✔ *cos primer* is a slightly more formal 'first' than bare *primer* (see *Adverbs*).

### E118 · I'm staying here until Friday.
- **Borlish:** *Jo remain ac fin je Viendr.* ("*fin a* 'until' can in some constructions take other prepositional phrases like *je Viendr* 'on Friday'"; also *Jo's remanent ac fin je Viendr.*)
- **IPA:** /ʒo reˈmen ak fɪn ʒe ˈvjɛn.dr̩/  ·  /ʒɔz ˌre.maˈnɛnt…/
- **Gloss:** 1SG stay.1SG here until on Friday
- **Settles:**
  - ✔ The 1SG present of *remanir* is i-mutated ***remain***, which answers **Q22**.
  - ✔ 'Until' is ***fin a***. Before another prepositional phrase the *a* is dropped: *fin je Viendr* 'until (on) Friday'.
  - ✔ The progressive *Jo's remanent* is also possible.
- **Follow-up:** E132 (future of *remanir*).

## Numerals

- 'In 1066' is *d'an 1066* (E41).
- E63 *My granmaðr fo nað d'an 1931*: 'was born' is *fo* + adjective ***nað***. Years are read as hundreds, *novoç cent trent un*, or in full, *mil nouf cent trent un*. 'Thirty-one' is *trent un*.

### E98 · There were about twenty people there.
- **Borlish:** *L'eç hom ig teyen veint atorn.* ("using *teir* 'to number'"; also *Scein atorn de veint hom ig.*, "more direct translation, somewhat less idiomatic". User, in chat: *Scein* should be ***Sceyen***.)
- **IPA:** /lɛts ɔm aj tiˈjɛn vint aˈtɔrn/  ·  /xiˈjɛn aˈtɔrn de vint ɔm aj/
- **Gloss:** DEF=DIST.PL person there number.IPFV.3PL twenty about  ·  there.be.IPFV.3PL about of twenty person there
- **Settles:**
  - ✔ 'About' with a number is *atorn* **after** it (*veint atorn*; compare *par cinqueç minut atorn*, C529), or *atorn de* + numeral before the noun.
  - ✔ The idiomatic way to give a count is ***teir* 'number'**, with the counted group as subject. The corpus has the same: *Y soucorsour … teyen catr* (C2415), *Teyen catorç frend ag tarn* (C1751). Existential *sceir* is the literal version.
  - ✔ *sceir* agrees with the following plural (*sceyen … hom*), and the imperfect 3PL is **sceyen**.
  - ✔ 'There' can follow a noun inside its phrase: *l'eç hom ig* 'the people there'.

### E127 · Our team came second.
- **Borlish:** *Nossy tourm surcou y dovem.* ("*surcou*, past of copulative verb *surcair* 'to end up being, to turn out to be'"; after an ordinary verb, *cos dovem*: *Jo pau y lox cos dovem* 'I ate the pizza second')
- **IPA:** /nɔˈsi turm sɪrˈku i doˈvɛm/  ·  /ʒo po i lɔks kɔz doˈvɛm/
- **Gloss:** 1PL.POSS team turn.out.PST DEF second  ·  1SG eat.PST DEF pizza ADVZ second
- **Settles:**
  - ✔ A predicative ordinal takes the article (*y dovem*) after the copular verb ***surcair*** 'end up, turn out'.
  - ✔ An adverbial ordinal is *cos* + ordinal (*cos dovem*).
  - ✔ The preterite of *surcair* is ***surcou***. The corpus has *surcou* 6× and *surcourn* 4×, against one *surcayeurn*, which bears on Q19.
  - ? *tourm* means 'troop, squadron' in the .db; 'team' would be a new sense.

## Conjunctions & Particles

- Question particle *ou* (E03): it comes straight after the questioned part, so it is clause-final only when the whole clause is questioned (E44, E19).
- *eð* 'and' before a vowel, *e* before a consonant (E42).
- *l'ig* is an optional euphonic by-form of *ig* ('that'; 'there') after a vowel sound (E91, user 2026-10-13).
- *ouð* 'whether' before a vowel, *ou* before a consonant; *ben ou* 'or whether' (E101).
- *candon* 'when' + preterite (E102).
- *soulor* 'then' is a conjunction and doesn't trigger inversion (E50).
- *cant* 'when' + preterite (E42).
- *ben* 'or' in an alternative question, with no *ou* (E59).
- *Ja* 'yes' as a short answer (E56).
- *ma* 'but' with ellipsis of the subject and copula (E04).
- *farau* (interj.) 'never mind' (E10).

## Register & Address

- *tu* to a sibling (E03).
- *vos* to a stranger, with *veleð* + infinitive for a polite request (E19, corrected in chat from *tu vel*). E45 checks a polite command.
- *cos* + adjective adverbs are slightly more formal than bare adjectives (E14).
- A polite command to a stranger is *veleð* + infinitive, with *domn* 'madam' as the vocative (E45).
- *no's* for *no so* is the colloquial contraction (E48).
- 'Would you like…?' to a guest: *Vos veleð* + infinitive (E59).

## Lexicon

New words and senses that came up in answers, for the `.db`:
- ~~deskieðar~~: *Deskieð* is a form of the existing ***deskeðar*** (user correction). Nothing to add; perhaps note the *ie* forms in its entry.
- **ketr** (n) 'kettle'; ***ketr a tag*** 'teapot' (E06). **Not in the .db.**
- *mogn* already covers 'short (in height)' (E04).
- *je ados* 'yesterday' and *je posc* 'tomorrow' are already entries. User: *je ados* is more familiar than *yer* (E06). Worth adding to *yer*'s entry as a usage note.
- The preverbal negator ***no*** is in the .db only as the interjection 'no'. It needs an adverb sense ('not', with *star*, *er*, *aïr* and *sceir*; see E05).
- ***acas*** (adv) 'at home' (E37). **Not in the .db.**
- ***lon tan*** 'not … either' (E32): worth a phrase entry or a usage note under *tan*.
- ***a mesur de* + INF** 'in the course of' (E39): a usage note under *mesur*.
- Spelling: the corpus has one *grandmaðr* (C4 *absoloirn my grandmaðr*). The lexicon and E38 have *granmaðr*.
- ***Normant*** 'Norman' (E41) and ***Rom*** 'Rome' (E48, corpus 15×): **not in the .db.**
- ~~***ottem***: add 'better' and an adverb sense; ***megl*** is obsolete.~~ **Done 2026-10-13** (Conflict 12).
- ***domn***: add the vocative 'madam' (E45).
- ***odysse*** 'cinema' is correct as it stands (E49; the user meant the cinema).
- ***eð*** (conj): note that it is the form before a vowel (E42).
- ***par oy*** 'right now' (E56): **not in the .db.**
- ***moutessem*** 'more (often)' (corpus 5×) and ***maissem*** 'more (in quantity)' (corpus 4×): **neither is in the .db** (E60). The .db has *mout* 'often' and *may* 'more'.
- ***alcot***: add the exclamative 'what a …!' (E58).
- ***maissem*** (CMPR of *gran*) and ***moutessem*** (CMPR of *mout*): user-confirmed 2026-10-13; worth entries like *pessem*.
- ***vec*** 'bus' (E66, corpus 10×): **not in the .db.**
- ***micrman*** 'bakery' (E85; Scaunç 31733): **not in the .db.**
- ***disceir***: add 'fail (an exam), not make it', intransitive with *ne* (E86).
- ***for***: the .db has it as a preposition 'only, just'; it also restricts any constituent (E90).
- ***toð soul*** 'by itself' (E93): a phrase entry, or a usage note under *soul*.
- ***atorn***: note 'about' with numbers, placed after the number or as *atorn de* + numeral (E98).
- ***teir***: note the counting use with the counted group as subject (E98).
- ***cascun***: note distributive *a cascun* 'each' (E99).
- ~~***vençar***: add *vendicāre* to the etymology.~~ **Done 2026-10-13:** `\et Middle Borlish < Vulgar Latin vendicāre “sell”.` *vendr* is obsolete and has no entry (Conflict 22).
- ***recarr***: note the irregular PST.PTCP ***recas*** (E110; corpus about 10×).
- ***najar***: add 'swim' (E103).
- ***dessur*** (adv) 'about it' (E104): a usage note.
- ~~*querel-* / *kerel-*~~: **done** (Conflict 24).
- ***scagler*** 'ladder' (E117): **not in the .db.**
- ***tourm***: add 'team' (E127).
- ***carc veyaçour*** 'luggage' (E130): phrase entry.
- ***deja***: note that it is preferred at the end of a constituent (E130).
- ***fin a***: note that it drops *a* before another prepositional phrase (*fin je Viendr*, E118).
- ***all'hour yon*** 'by the time' (E72); hortative ***ig*** 'let…' (E76): usage notes.
