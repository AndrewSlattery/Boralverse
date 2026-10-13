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

**Fronted adverbial clauses don't trigger inversion** (✔, three answers): *Cant nos venoim, y majon er pegntað…* (E42), *Ða cay ploy je posc, nos voum remanir…* (E08), *Degnant ig cous tart, y varous remanen yert* (E18). A fronted clause patterns with the comma-set adverb of E06 (*Yer, Marc accatau…*), not with an integrated one. Inside the subordinate clause, the subject comes before the verb (*cant nos venoim*): subordinate clauses are not V2.

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

## Tense, Aspect & Mood

Present after *ða* for a future condition, and the *volir* future: see E08. *vil lo fair* vs *farray*: see E10.
- Future in the past, *vole* + INF: E21.
- Past counterfactual, *ða* + IPFV.SBJV and *volois* + INF: E24.
- Aspect of *eir* 'have to': E26.
- Subjunctive after a negated *creir*: E22.

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

'Everyone' = *toð gent* with plural agreement: E20.

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

## Adverbs

*jamay* position: see E09 and E17. *plu* 'any more' in negative concord: see E05.
- **Two adverb formations, two registers (E14):** a bare adjective is neutral (*Jo vay primer…*); *cos* + adjective is slightly more formal (*cos primer*).
- *ottem* 'better' is used as an adverb (E16).
- *meðes* 'even' follows the phrase it focuses (E20).
- 'Still' can be expressed with the verb *remanir* + adjective (E18).
- *fort* 'well' (E47). *ottem* is 'better/best' for adjective and adverb. *megl* is obsolete (E47, Conflict 12); it survives in *meglfair* and *meglfacçon*.
- *ja* 'already' stands between the auxiliary and the participle (E42).
- *primer* fronted triggers inversion; *soulor* is a conjunction and doesn't (E50).

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

## Numerals

- 'In 1066' is *d'an 1066* (E41). How years are read aloud is still open (→ E63).

## Conjunctions & Particles

- Question particle *ou* (E03): it comes straight after the questioned part, so it is clause-final only when the whole clause is questioned (E44, E19).
- *eð* 'and' before a vowel, *e* before a consonant (E42).
- *soulor* 'then' is a conjunction and doesn't trigger inversion (E50).
- *cant* 'when' + preterite (E42).
- *ma* 'but' with ellipsis of the subject and copula (E04).
- *farau* (interj.) 'never mind' (E10).

## Register & Address

- *tu* to a sibling (E03).
- *vos* to a stranger, with *veleð* + infinitive for a polite request (E19, corrected in chat from *tu vel*). E45 checks a polite command.
- *cos* + adjective adverbs are slightly more formal than bare adjectives (E14).
- A polite command to a stranger is *veleð* + infinitive, with *domn* 'madam' as the vocative (E45).
- *no's* for *no so* is the colloquial contraction (E48).

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
