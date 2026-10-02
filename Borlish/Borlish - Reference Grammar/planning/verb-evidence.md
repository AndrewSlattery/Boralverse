# Verb evidence (draft, machine-harvested)

> **Status 2026-10-01:** you supplied full paradigms for *cantar*, *ðurr*, *dormir* and *finir*, plus a list of complications. These are now written up in `chapters/verb-morphology.tex` and `appendices/verb-tables.tex`. This file remains as corpus evidence for the irregular verbs and the irregularity types, which are still to be written up.

A working document for the Verb Morphology chapter and the Verb Tables appendix. Everything here was harvested automatically from the **glossed** Scaunç sentences (Borlish / IPA / phonetic / gloss / English) as of 2026-10-01, so treat it as evidence to check, not as the grammar.

## How it was made
- 1397 verb tokens were found in the glossed sentences: 580 irregular, 447 *-ar*, 152 *-r*, 85 *-ir* type 1, 52 *-ir* type 2, and 81 that matched no lexicon verb.
- **Category** comes from the gloss tags. The many spellings are merged: *ipf/imp/impf/ipfv* → imperfect, *sbj/sj* → subjunctive, *fut/ft* → future, *p.pst/ptcp.pst/pts* → past participle.
- **Person** comes from the gloss tag, or failing that from a subject pronoun just before the verb (or cliticised onto it, as in *j'ay*). Where the subject is a noun, the person shows as *unknown*.
- A **bare form with no tags** is counted as a present only when a subject pronoun stands right before it, because otherwise nouns glossed with the same English word crept in.
- **Class** comes from matching the form to a lexicon verb (*ar v / r v / ir1 v / ir2 v*). The *ending* is the form minus the lexicon stem. *ø* means no ending. An ending starting *~* means the stem itself changed (e.g. *cav-ir* → *caf*), so the split is approximate there.
- Irregular verbs are grouped by their English gloss and a check on the form's first letters (e.g. 'be' → *es/sta*).
- Some forms may be relics of older stages of the grammar, and a few may be mis-sorted. Every token is listed in `verb-tokens.tsv` (with its Scaunç line number) for checking.

## First reading
Patterns that stand out across the classes. All are open to correction.

- **Person endings** recur across tenses: 1PL in *-m* (*-aum, -eum, -oim, -isceum*; present *yemm*), 2PL in *-ð* or *-st* (*-að, -eð*; preterite *-aust, -oist, -ist*), and 3PL in *-n* (*-n, -an, -en, -aurn, -oirn, -eurn, -iscn*). The present singular is usually the bare stem.
- **Preterite:** *-ar* has *-au, -aum, -aust, -aurn*. *-ir* type 1 has *-eu* or *-oy* in the singular, then *-eum, -eurn*. *-r* verbs vary most, with *-oy, -eu* or strong forms in *-s* in the singular, then *-oim, -oist, -oirn*. *-ir* type 2 has *-isceu, -isceum, -isceurn*.
- **Imperfect:** *-ar* has *-a* (singular) and *-an* (3PL); the other classes have *-e* and *-en*. The 1PL in *-au* looks the same as the *-ar* preterite singular.
- **Future:** synthetic in *-ra*: *-ara*, *-araun* (3PL), *-areu* (1PL). Type 1 *-ir* verbs show *-dra* or *-rra* (*vendra, tendra, porra*).
- **Subjunctive:** 1PL *-eu/-au*, 2PL *-eð/-að*. The imperfect subjunctive ends in *-s*: *-aus, -eus, -ois/-ous, -isceus*.
- **Participles:** present *-ant* (*-ar*), *-ent* (*-ir* type 1, *-r*), *-iscent* (*-ir* type 2). Past *-að* (*-ar*), *-ið* (*-ir*, both types), with strong forms in *-t, -s, -uð* mostly in the *-r* and *-ir* type 1 classes. The potential is *-abr* (*-ar*) and *-br* (*-r*).
- **Type 2 *-ir*** keeps *-isc-* in the present (3PL), preterite, imperfect, subjunctive and present participle, but not in the infinitive or past participle.

## -ar verbs
447 tokens from 295 lemmas. Each cell gives endings with token counts and up to two example forms.

| non-finite | endings |
|---|---|
| infinitive | *ar* 111 (acatar, accatar)<br>*~iar* 1 (monfiar)<br>*~dr* 1 (vendr) |
| present participle | *ant* 74 (abrevant, alleyant)<br>*ettongandessem* 1 (rascettongandessem)<br>*~iant* 1 (roglfiant)<br>*~isant* 1 (debriscellisant) |
| past participle | *að* 57 (adornað, ajoutað)<br>*ant* 4 (augtant, benoçant)<br>*ø* 2 (cors, saut)<br>*~iað* 1 (teurfiað) |
| potential (-abr) | *abr* 2 (benoçabr, broucabr)<br>*~iabr* 1 (confiabr) |

| | 1SG | 2SG | 3SG | 1PL | 2PL | 3PL | person unknown |
|---|---|---|---|---|---|---|---|
| present | *ø* 9 (am, cossir)<br>*~ug* 1 (ploug)<br>*~* 1 (sucq)<br>+1 more | *ø* 5 (ajoutaç, am) | *ø* 3 (brouc, jolley) | *au* 4 (corrogau, depostau)<br>*u* 1 (stu) | *að* 2 (ignorað, souspectað) | *n* 12 (affirmn, amn)<br>*~in* 2 (mestein, ubicqfein)<br>*aust* 1 (blasmaust) | *ant* 1 (follant) |
| preterite | *au* 16 (acatau, ascovau)<br>*~uvau* 1 (trouvau) | *au* 3 (bajau, hoccovau) | *au* 11 (accatau, coutoccau)<br>*avau* 1 (rescavau) | *aum* 20 (accataum, alandaum)<br>*au* 1 (souvolau) | *aust* 2 (acataust, kiglaust) | *aurn* 12 (accataurn, colombaurn) | *au* 30 (ablegau, acavau) |
| imperfect | *a* 7 (ama, azia) |  | *a* 5 (porta, quotta) | *au* 1 (conteyau)<br>*e* 1 (orruðe) |  | *an* 7 (echovan, gliðan) | *a* 10 (azia, dema)<br>*e* 2 (orruðe)<br>*eð* 1 (issaugheð) |
| future |  |  |  |  |  | *araun* 1 (portaraun) | *ara* 3 (commandara, desveyara)<br>*oura* 1 (stoura) |
| subjunctive |  |  |  | *eu* 5 (enombreu, quisteu)<br>*heu* 1 (vancheu) | *eð* 4 (augrimeð, cargeð) |  |  |
| imperfect subjunctive |  |  |  |  |  |  | *aus* 1 (laundaus) |

## -r verbs (syllabic r)
152 tokens from 74 lemmas. Each cell gives endings with token counts and up to two example forms.

| non-finite | endings |
|---|---|
| infinitive | *r* 39 (acceir, accommettr)<br>*r* 1 (car-r) |
| present participle | *nt* 11 (beint, carnt)<br>*~ent* 5 (attenent, rajognent)<br>*ent* 3 (pascent) |
| past participle | *~s* 6 (pars, recas)<br>*~t* 4 (pagnt, pent)<br>*~nt* 2 (interront, irront)<br>*t* 2 (attriboit, costroit)<br>+4 more |
| potential (-abr) | *br* 1 (mesveibr) |

| | 1SG | 2SG | 3SG | 1PL | 2PL | 3PL | person unknown |
|---|---|---|---|---|---|---|---|
| present | *~* 2 (fon, reu)<br>*ø* 1 (admet)<br>*~y* 1 (crey) |  | *~y* 2 (crey, instroy)<br>*~e* 1 (descene)<br>*ø* 1 (reconnosc) | *m* 2 (creim)<br>*~m* 1 (pretenm) |  | *n* 2 (prevein, tein)<br>*~-n* 1 (grin-n) |  |
| preterite | *heu* 1 (enfugheu)<br>*~u* 1 (mesveu)<br>*oy* 1 (soccoðoy)<br>+4 more |  | *~s* 1 (avars)<br>*~y* 1 (reconnoy) | *oim* 1 (targoim) | *~ist* 2 (ignoist, parmist)<br>*~oist* 1 (gimmoloist) | *~oirn* 4 (descenoirn, interromoirn)<br>*oirn* 1 (pardoirn)<br>*~eirn* 1 (entrjeirn)<br>+1 more | *~oy* 2 (interromoy, penoy)<br>*~s* 1 (surcas)<br>*~u* 1 (sceu)<br>+6 more |
| imperfect | *~ye* 5 (creye)<br>*~e* 1 (comprene)<br>*e* 1 (care) | *~ye* 1 (creye) |  | *au* 1 (pascau)<br>*~au* 1 (jognau) | *að* 1 (desmettað) | *en* 1 (assisten)<br>*~en* 1 (accenen)<br>*~yen* 1 (surcayen) | *~e* 1 (souprene)<br>*~ye* 1 (egreye)<br>*e* 1 (souðure)<br>+1 more |
| future |  |  | *ra* 1 (plagra) | *~areu* 1 (rajognareu) |  |  |  |
| subjunctive |  |  |  | *au* 2 (mettau, pascau) | *að* 1 (reuvað)<br>*hað* 1 (affighað)<br>*~að* 1 (attenað) |  |  |
| imperfect subjunctive |  |  | *~ous* 1 (surcous) |  |  |  | *~ois* 2 (interromois, yemois) |

## -ir verbs, type 1
85 tokens from 49 lemmas. Each cell gives endings with token counts and up to two example forms.

| non-finite | endings |
|---|---|
| infinitive | *ir* 13 (agir, conemir)<br>*ïr* 3 (abseïr, asseïr) |
| present participle | *ent* 9 (assovent, contenent)<br>*yent* 1 (asseyent) |
| past participle | *ið* 3 (dormið, sortið)<br>*~art* 2 (covart, descovart)<br>*~ut* 1 (erreut)<br>*~st* 1 (attost)<br>+5 more |

| | 1SG | 2SG | 3SG | 1PL | 2PL | 3PL | person unknown |
|---|---|---|---|---|---|---|---|
| present | *~u* 1 (stou)<br>*~ir* 1 (abhoir) |  | *ø* 1 (parman) | *eu* 1 (condoceu) |  | *~inn* 1 (remainn) |  |
| preterite | *eu* 5 (addoceu, cogleu)<br>*lmau* 1 (calmau)<br>*oy* 1 (parmanoy) |  | *oy* 2 (ovroy, tenoy)<br>*eu* 1 (peðeu) | *eum* 1 (receveum) |  | *eurn* 1 (receveurn) | *oy* 2 (denoy, ovroy)<br>*yeu* 2 (soureyeu, souseyeu)<br>*eu* 2 (deleu, sorteu)<br>+1 more |
| imperfect | *e* 2 (horre, sente)<br>*ye* 1 (asseye) | *e* 1 (dorme) | *e* 1 (intermane) | *au* 1 (corrau)<br>*yau* 1 (asseyau) |  | *en* 2 (harmonen, remanen) | *e* 5 (abrange, contene)<br>*ye* 1 (asseye)<br>*ir* 1 (salir) |
| future |  |  |  |  |  |  | *dra* 2 (intermandra, tendra)<br>*rra* 1 (derra)<br>*~ura* 1 (stoura) |
| subjunctive |  |  |  | *au* 1 (tenau) | *að* 1 (salað) |  |  |
| imperfect subjunctive |  |  |  |  |  |  | *eus* 1 (parceveus) |

## -ir verbs, type 2 (-isc-)
52 tokens from 39 lemmas. Each cell gives endings with token counts and up to two example forms.

| non-finite | endings |
|---|---|
| infinitive | *ir* 11 (beyollir, cambir)<br>*ïr* 2 (luïr, obsequïr) |
| present participle | *iscent* 9 (aplattiscent, enhautiscent) |
| past participle | *ið* 5 (bannið, closið)<br>*ïscent* 1 (luïscent)<br>*iscent* 1 (parsiscent)<br>*iðessem* 1 (extolliðessem) |

| | 1SG | 2SG | 3SG | 1PL | 2PL | 3PL | person unknown |
|---|---|---|---|---|---|---|---|
| present |  |  |  | *ïsceu* 1 (luïsceu) |  | *iscn* 1 (dehiscn) |  |
| preterite | *ið* 1 (emplið) | *isceu* 1 (parsisceu) |  | *isceum* 1 (parsisceum)<br>*ïsceum* 1 (luïsceum) |  | *~isceurn* 1 (sperisceurn)<br>*isceurn* 1 (voltisceurn) | *isceu* 3 (bondisceu, finisceu)<br>*ïsceu* 1 (quïsceu) |
| imperfect | *ïsce* 1 (faïsce) |  |  | *iscau* 1 (moliscau) |  | *iscen* 2 (parsiscen, tanniscen) | *isce* 3 (incombisce, parisce) |
| subjunctive |  |  |  |  | *iscað* 2 (jamiscað, tanniscað) |  |  |
| imperfect subjunctive |  |  |  |  |  |  | *isceus* 1 (closisceus) |

## Irregular and high-frequency verbs
Whole forms rather than endings, with token counts.

### es/sta (be)
- infinitive: *star* 2; past participle: **stað** 1

| | 1SG | 2SG | 3SG | 1PL | 2PL | 3PL | unknown |
|---|---|---|---|---|---|---|---|
| present | *s* 7, *so* 3, *sco* 1 | *es* 1, *s* 1 | *es* 15, *s* 7 | *som* 5 | *soð* 2 | *son* 27 | *es* 27, *s* 6, *interman* 1 |
| preterite | *fo* 2 |  |  | *fom* 1 |  | *forn* 2 | *fo* 1 |
| imperfect | *sta* 4 |  | *sta* 1 |  |  | *ern* 3, *stan* 3, *teyen* 1 | *sta* 10, *er* 1 |
| future |  | *sera* 1 |  | *sereu* 1 |  | *seraun* 1 | *sera* 2 |
| subjunctive | *sey* 1 |  |  | *seim* 1 | *seyað* 1 | *sein* 5 | *sey* 5 |
| imperfect subjunctive |  | *fos* 1 |  |  | *fosseð* 1 |  | *fos* 2 |

### aur (have)
- infinitive: *aïr* 5, *broucar* 1; present participle: *ayent* 1; past participle: *aut* 2

| | 1SG | 2SG | 3SG | 1PL | 2PL | 3PL | unknown |
|---|---|---|---|---|---|---|---|
| present | *ay* 11 | *a* 5 | *a* 4 | *eu* 5, *aum* 1 |  | *aun* 12 | *a* 13 |
| preterite |  |  |  |  |  | *aurn* 1, *ayen* 1 | *au* 1 |
| imperfect | *aye* 2 |  | *aye* 4 | *ayau* 4 |  | *ayen* 5 | *aye* 2 |
| future |  |  | *arra* 1 | *arreu* 1 | *arreð* 1 |  |  |
| subjunctive |  |  |  |  |  | *ain* 2 | *ay* 1 |
| imperfect subjunctive |  | *aus* 2 | *aus* 1 |  |  | *ausn* 1 |  |

### er (COP)
- infinitive: *ern* 1

| | 1SG | 2SG | 3SG | 1PL | 2PL | 3PL | unknown |
|---|---|---|---|---|---|---|---|
| present | *s* 1, *sco* 1 |  |  | *erau* 2 |  |  |  |
| preterite |  |  |  |  |  |  | *er* 1 |
| imperfect | *er* 6 |  | *r* 4 | *erau* 3, *er* 1 | *erað* 1 | *ern* 6 | *er* 10 |

### far (do)
- infinitive: *fair* 5; present participle: *faint* 2, *fayent* 1; past participle: *fait* 4, *faint* 1

| | 1SG | 2SG | 3SG | 1PL | 2PL | 3PL | unknown |
|---|---|---|---|---|---|---|---|
| present |  |  |  |  |  | *faun* 3 | *fay* 1 |
| preterite | *fey* 4 |  |  | *feim* 1 |  | *feirn* 2, *fegrn* 1 | *fey* 5 |
| imperfect |  |  |  |  |  |  | *façað* 1 |
| future |  |  |  | *farreu* 1 |  |  |  |
| subjunctive | *faç* 1 |  |  |  |  |  | *faç* 3 |

### vol- (will, FUT)

| | 1SG | 2SG | 3SG | 1PL | 2PL | 3PL | unknown |
|---|---|---|---|---|---|---|---|
| present | *vil* 2 |  | *vil* 1 | *voum* 2 | *vouð* 2 | *voun* 5 | *vil* 2 |
| imperfect | *vole* 1 |  |  |  |  | *volen* 1 | *vole* 1, *volen* 1 |
| subjunctive | *vel* 1 | *vel* 2 |  | *veleu* 1 | *veleð* 5 |  | *vel* 8 |
| imperfect subjunctive |  |  |  |  |  |  | *volois* 1 |

### cair (fall)
- present participle: *caint* 1

| | 1SG | 2SG | 3SG | 1PL | 2PL | 3PL | unknown |
|---|---|---|---|---|---|---|---|
| present |  |  |  |  | *cay* 1 | *cain* 4 | *cay* 18 |
| imperfect |  |  |  |  |  | *cayen* 2 | *caye* 7 |
| future |  |  |  |  |  |  | *carra* 2 |

### sceir (there is)
- infinitive: *sceir* 1; present participle: *sceint* 3

| | 1SG | 2SG | 3SG | 1PL | 2PL | 3PL | unknown |
|---|---|---|---|---|---|---|---|
| present |  |  |  |  |  | *scein* 1 | *scey* 10 |
| imperfect |  |  |  |  |  | *sceyen* 2 | *sceye* 9 |
| future |  |  |  |  |  | *scerraun* 2 | *scerra* 2 |

### cavir (get)
- infinitive: *cavir* 4; present participle: *cavent* 1; past participle: *caut* 3

| | 1SG | 2SG | 3SG | 1PL | 2PL | 3PL | unknown |
|---|---|---|---|---|---|---|---|
| present |  |  | *caf* 1 |  |  | *caun* 1 |  |
| preterite | *cof* 2 |  |  | *coum* 4 |  | *courn* 2, *coun* 1 | *cof* 4, *cou* 1 |
| imperfect |  |  |  |  |  |  | *cave* 1 |
| future |  |  |  |  | *caurreð* 1 |  |  |
| subjunctive |  | *caif* 1 |  |  |  |  | *caif* 1 |

### poðir (can)
- infinitive: *poðir* 2

| | 1SG | 2SG | 3SG | 1PL | 2PL | 3PL | unknown |
|---|---|---|---|---|---|---|---|
| present | *poð* 3 |  |  |  |  |  | *poð* 4 |
| imperfect | *poðe* 1 |  |  |  |  |  | *poðe* 2 |
| future |  | *porra* 1 |  | *porreu* 2 |  |  | *porra* 2 |
| subjunctive | *pos* 1 | *pos* 2 |  |  |  |  |  |

### dar (give)
- infinitive: *dar* 3; past participle: *dað* 5

| | 1SG | 2SG | 3SG | 1PL | 2PL | 3PL | unknown |
|---|---|---|---|---|---|---|---|
| present |  |  | *da* 1 |  |  |  | *dant* 1, *dar* 1, *da* 1 |
| preterite | *dau* 1 |  | *dau* 1 | *dau* 1 |  |  | *dau* 2 |
| imperfect |  |  |  |  |  | *dan* 1 | *deð* 1 |
| subjunctive |  |  | *day* 1 |  |  |  |  |

### eir (go)
- infinitive: *entrar* 1, *eir* 1; past participle: *eið* 3, *eut* 1

| | 1SG | 2SG | 3SG | 1PL | 2PL | 3PL | unknown |
|---|---|---|---|---|---|---|---|
| present | *vay* 1 |  |  |  |  |  | *va* 2 |
| preterite | *eu* 1 |  |  | *eum* 1 |  | *eurn* 1 |  |
| imperfect | *eye* 1 |  | *eye* 1 | *eyau* 1 |  |  |  |
| future |  |  | *erra* 1 | *erreu* 1 |  |  |  |

### savir (know)
- infinitive: *savir* 1; past participle: *saut* 1

| | 1SG | 2SG | 3SG | 1PL | 2PL | 3PL | unknown |
|---|---|---|---|---|---|---|---|
| present | *sau* 2 |  |  |  | *saveð* 2 | *saun* 1 |  |
| preterite | *saveu* 1 |  |  |  |  |  |  |
| imperfect | *save* 4 |  | *save* 1 |  |  |  |  |
| future |  |  |  |  |  | *sauraun* 1 |  |

### valir (be worth)
- present participle: *valent* 1

| | 1SG | 2SG | 3SG | 1PL | 2PL | 3PL | unknown |
|---|---|---|---|---|---|---|---|
| present |  | *val* 1 | *val* 1 |  | *val* 1 | *vaun* 1 | *val* 3 |
| subjunctive | *vail* 1 |  |  |  |  |  | *vail* 1 |
| imperfect subjunctive |  |  |  |  |  |  | *valois* 1 |

### stovir (be needed)

| | 1SG | 2SG | 3SG | 1PL | 2PL | 3PL | unknown |
|---|---|---|---|---|---|---|---|
| present |  |  |  | *stou* 1 |  | *stoun* 1 | *stou* 3 |
| imperfect |  |  |  |  |  |  | *stove* 4 |
| future |  |  | *storra* 1 |  |  |  | *stoura* 1 |

### venir (come)

| | 1SG | 2SG | 3SG | 1PL | 2PL | 3PL | unknown |
|---|---|---|---|---|---|---|---|
| present |  |  |  |  |  | *vienn* 1 | *vien* 3 |
| preterite | *venoy* 1 |  |  |  |  | *venoirn* 1 |  |
| imperfect |  |  |  | *venau* 1 |  |  | *vene* 1 |
| future |  |  | *vendra* 1 |  |  |  |  |
| subjunctive |  |  | *vin* 1 |  |  |  |  |

### veir (see)
- infinitive: *veir* 2; present participle: *veint* 1; past participle: *vis* 1

| | 1SG | 2SG | 3SG | 1PL | 2PL | 3PL | unknown |
|---|---|---|---|---|---|---|---|
| preterite | *vis* 3 |  |  |  |  | *veurn* 1 |  |
| imperfect |  |  |  | *veyau* 1 |  |  |  |

### dir (say)
- present participle: *dignt* 1

| | 1SG | 2SG | 3SG | 1PL | 2PL | 3PL | unknown |
|---|---|---|---|---|---|---|---|
| present |  |  |  |  |  |  | *dig* 1 |
| preterite | *dis* 2 |  | *dis* 1 |  |  | *disrn* 1 | *dis* 3 |

### nol- (NEG.FUT)

| | 1SG | 2SG | 3SG | 1PL | 2PL | 3PL | unknown |
|---|---|---|---|---|---|---|---|
| present |  |  |  |  | *nuθ* 1 |  | *nil* 3 |
| future-in-past |  |  |  | *nolau* 1 |  |  |  |
| subjunctive |  |  |  |  | *neleð* 1 |  | *nel* 1 |
| imperfect subjunctive | *nolois* 1 |  |  |  |  |  |  |

### deïr (owe, must)

| | 1SG | 2SG | 3SG | 1PL | 2PL | 3PL | unknown |
|---|---|---|---|---|---|---|---|
| present |  |  |  | *deyeu* 1 |  | *dein* 1 |  |

## Forms that matched no lexicon verb
Possibly missing from the lexicon, spelled differently there, or irregular. Grouped by gloss.

- **amount**: *teint* (amount-p.prs, S26913); *teir* (amount.to-inf, S16253); *teir* (amount.to-inf, S16258); *terraun* (amount-fut-3p, S27070)
- **arrive**: *yent* (arrive.p.pst, S13225); *yent* (arrive.p.pst, S15276)
- **be**: *pacentar* (be.patient-ipf, S32277); *pacentar* (be.patient.to-inf, S31091); *taçað* (be.quiet-2p, S10284)
- **become**: *din* (become.sbj, S26043)
- **befall**: *caye* (befall-ipf, S30571)
- **brink**: *beut* (brink.ptcp.pst, S9149)
- **can**: *sceu* (can.pst, S17690); *sceu* (can.pst, S19385); *sceu* (can.pst, S23844); *sceu* (can.pst, S32656); *sceus* (can.sbj.ipf, S23953)
- **card**: *cardonar* (card-inf, S24870)
- **come**: *revin* (come.back.sbj, S12521); *terraun* (come.to-fut.3p, S17343)
- **comeback**: *reloy* (comeback.pst, S27269)
- **compose**: *componoy* (compose-pst, S15752)
- **cook**: *cogt* (cook-ptcp.pst, S9599)
- **cost**: *teyen* (cost-ipf-3p, S28801)
- **discuss**: *kessandar* (discuss-inf, S10604)
- **displease**: *mesplagheu* (displease-pst, S32482)
- **disprefer**: *desfayað* (disprefer-2p.sbj, S8589)
- **eat**: *paut* (eat-p.pst, S17764); *paut* (eat.p.pst, S19946)
- **enclose**: *clojonnað* (enclose-ptcp.pst, S8231)
- **envy**: *groça* (envy-ipf, S13930)
- **extinguish**: *quïsceu* (extinguish-pst, S22526)
- **fall**: *cou* (fall-pst, S26207); *cou* (fall.pst, S14795); *cou* (fall.pst, S22954); *cous* (fall-sbj.ipf, S13187)
- **get**: *receut* (get-p.pst, S18864); *reçoirn* (get-pst.3p, S7641); *yem-m* (get-1p, S25631); *yeme* (get-ipf, S17041); *yeme* (get-ipf, S21335)
- **hear**: *oyau* (hear-ipf.1p, S23158); *oye* (hear-ipf, S23415); *oyeu* (hear-pst, S18140)
- **hold**: *tienn* (hold-3p, S29124); *tienn* (hold-3p, S32367)
- **hurt**: *dourra* (hurt-fut.3s, S7049)
- **leave**: *sail* (leave.1s, S22723)
- **let**: *soloy* (let.go-pst, S15341); *soloy* (let.go-pst, S22440); *soluð* (let.go-p.pst, S17521)
- **make**: *ris* (make.ptcp.pst, S7699)
- **merit**: *valeurn* (merit-pst.3p, S30125)
- **mill**: *molinant* (mill-p.prs, S16661)
- **n**: *indiglað* (n-erase-p.pst, S18174)
- **number**: *teyen* (number-ipf-3p, S17309); *teyen* (number-ipf-3p, S25752); *teyent* (number-p.prs, S32446)
- **outfit**: *vessonnað* (outfit-p.pst, S24482)
- **oversee**: *survism* (oversee-1p.pst, S25130)
- **put**: *mis* (put.p.pst, S14708); *mis* (put.pst, S24314); *ponau* (put-1p.imp, S14012)
- **sag**: *socquau* (sag-pst, S14693)
- **seat**: *asseyeu* (seat-pst, S24500)
- **seen**: *veu* (seen.pst, S21877)
- **serve**: *servið* (serve-p.pst, S15980)
- **spend**: *noiteyar* (spend.night-inf, S21430)
- **start**: *enceð* (start-ipf.p, S22723)
- **support**: *promoun* (support-3p, S10620)
- **take**: *suim* (take.1s, S30880)
- **throw**: *jey* (throw.pst, S30303)
- **trim**: *tos* (trim.p.pst, S13152)
- **un**: *impareïbr* (un-make.equal-pot, S13993); *innogbr* (un-harm-pot, S14101)
- **wobble**: *remiaçant* (wobble-p.pst, S14859)

## Questions for you
1. Is the present singular always the bare stem, for all persons? Does the 2SG differ?
2. The *-ar* preterite singular *-au* and the imperfect 1PL *-au* (e.g. *rovau*, *corrogau*, glossed 1PL present) look identical. Which is which, and is there a present 1PL in *-au*?
3. *-r* verbs: is there a regular preterite (*-oy*? *-eu*?), or is each verb's preterite stem lexical (*dis*, *mis*, *fegrn*…)? The same question applies to past participles (*-t, -s, -uð*).
4. Is the future always synthetic in *-ra* (with *-dra/-rra* after some stems), and how does it relate to the *vol-* + infinitive periphrasis?
5. What is the full present subjunctive? Only 1PL and 2PL are clearly attested for regular verbs.
6. Imperatives: none are tagged as such in the glosses. Is the 2SG imperative the bare stem, and is 2PL the same as the subjunctive (*-að/-eð*)?
7. The 'unknown person' cells mostly come from noun subjects. A full paradigm per class, from you, would fill most gaps.
