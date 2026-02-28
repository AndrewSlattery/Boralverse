"""
Apply all 23 canon resolutions to all_claims_clean.yaml.
Produces all_claims_final.yaml with:
  - Specific wrong / superseded claims deleted
  - Claim texts updated to reflect authorial resolution
  - All _canon_contradiction flags cleared (all 23 contradictions resolved)
  - New synthesis / terminology claims appended
"""

import os, re, yaml

FOLDER = os.path.dirname(os.path.abspath(__file__))
SRC    = os.path.join(FOLDER, "all_claims_clean.yaml")
OUT    = os.path.join(FOLDER, "all_claims_final.yaml")


def norm(s):
    """Normalise for matching: lowercase + collapse whitespace."""
    return re.sub(r"\s+", " ", str(s).lower().strip())


# ── 1. Claims to delete entirely (matched by normalised claim text) ─────────
#
# Deletions correspond to:
#   Res 1  – Diocese of Boral (superseded by the correct 195.5 version)
#   Res 4  – "despised Anti-Paradism" (near-dup of "wrote against the Deviance movement"
#              once Anti-Paradism is confirmed = Deviance movement)
#   Res 5  – "At most 200 glyphs" (superseded by the updated 62.5 claim with 180–200 range)
#   Res 9  – 62.5 "mordether vassal" version (content absorbed into updated 5.5 claim)
#   Res 23 – 3-unit dime length claim (the complete 4-unit 183.5 version is correct)
#   Guard  – combined 62.5 population+trade claim that uses the wrong "half" figure
#
DELETE_NORMS = {
    # Res 1
    norm("After the Diocletian reforms, Borland's province became the Diocese of Boral."),
    # Res 4
    norm("Elsebeth Sneider herself despised Anti-Paradism."),
    # Res 5
    norm("At most 200 different glyphs appear throughout the entire Mysarnos Codex."),
    # Res 9
    norm("Mysarnos was the capital of Mystra, a mordether vassal of the Roman Empire."),
    # Res 23
    norm("The three dime bases for length are the inch, the foot (10 inches), and the league (10\u2074 feet)."),
    # Guard (combined 62.5 claim — curly and straight apostrophe variants)
    norm("During the sixteenth century Revitalist movement, Mysarnos received half of all Greece\u2019s imports and had a population of nearly thirty thousand."),
    norm("During the sixteenth century Revitalist movement, Mysarnos received half of all Greece's imports and had a population of nearly thirty thousand."),
}


# ── 2. Claim-text updates: (normalised old text, replacement text) ──────────
#
# Each tuple: (norm(old_claim_text), new_claim_text)
#
UPDATES = [
    # Res 2 – Hawkirch Surrender date 1623 → 1632 (67.5)
    (
        norm("Borland's involvement in the Romantic Wars was restricted to a failed invasion "
             "culminating in the Hawkirch Surrender of 1623 N, along with unstable military aid "
             "arrangements with neighbouring polities."),
        "Borland's involvement in the Romantic Wars was restricted to a failed invasion "
        "culminating in the Hawkirch Surrender of 1632 N, along with unstable military aid "
        "arrangements with neighbouring polities.",
    ),

    # Res 9 – Mysarnos capital: merge principality + vassal + dissolution (5.5)
    (
        norm("Mysarnos is the former capital of the Principality of Mystra."),
        "Mysarnos was the capital of Mystra, which was both a principality and a mordether "
        "vassal of the Second Roman Empire; since Mystra's dissolution, Mysarnos is no longer "
        "the capital of any region.",
    ),

    # Res 10 – Trade share: majority → over half (5.5)
    (
        norm("Mysarnos received the majority of all trade imports in Greece."),
        "Mysarnos received over half of all trade imports in Greece.",
    ),

    # Res 5 – Glyph count: update 62.5 to reflect 180–200 range
    (
        norm("The text of the Mysarnos Codex consists of approximately 180 different glyphs "
             "arranged into words and paragraphs."),
        "The text of the Mysarnos Codex consists of between approximately 180 and 200 different "
        "glyphs arranged into words and paragraphs, with the exact count varying by researcher "
        "depending on whether certain similar pairs are treated as distinct glyphs or as variants "
        "of the same glyph.",
    ),

    # Res 6 – Constant Empire: add retroactive qualifier to 64.5 main claim
    (
        norm("The First Drengot Empire, or Constant Empire, was the westernmost of the four "
             "empires comprising the Second Tetrarchy (also called the Medieval Imperia)."),
        "The First Drengot Empire (retrospectively also called the Constant Empire, a name "
        "coined in the fourteenth century) was the westernmost of the four empires comprising "
        "the Second Tetrarchy (also called the Medieval Imperia).",
    ),

    # Res 6 – Constant Empire: mark 64.5 prestige claim as latter-day
    (
        norm("The lesser-used name 'Constant Empire' claims the prestige of the Classical-era "
             "District of Constantius, which occupied roughly the same geographical extent."),
        "The latter-day name 'Constant Empire', first coined by a fourteenth-century historian, "
        "claims the prestige of the Classical-era District of Constantius, which occupied "
        "roughly the same geographical extent.",
    ),

    # Res 8 – Burgundy: add reliability caveat to 75.5
    (
        norm("Burgundy weathered the Second Great Dying comparatively well due to its lack of "
             "coastal territory, since the principal vector of plague transmission was naval trade."),
        "According to Burgundy's own records (whose full reliability is uncertain), Burgundy "
        "weathered the Second Great Dying comparatively well due to its lack of coastal "
        "territory, since the principal vector of plague transmission was naval trade.",
    ),

    # Res 19 – Jothey floruit: fl. 920 → fl. 898 (26.5)
    (
        norm("Jothey of Borland (fl. 920) fled into exile following the Dane invasion of Borland."),
        "Jothey of Borland (fl. 898) fled into exile following the Dane invasion of Borland.",
    ),

    # Res 12 – Willem → Willemy in 45.5 deployment claim
    (
        norm("The two-arm system for sending steeplepost was first deployed in Willem in the "
             "early nineteenth century."),
        "The two-arm system for sending steeplepost was first deployed in Willemy in the early "
        "nineteenth century.",
    ),

    # Res 13 – Drengot Collusion: remove spurious "established" phrasing in 78.5
    (
        norm("The Drengot Collusion was established during the Good Game period, with its "
             "expansion concluding in 1894 N with the accession of Borland."),
        "The Drengot Collusion's formation reached its conclusion during the Good Game period "
        "of the late nineteenth century, with its final expansion concluding in 1894 N with "
        "the accession of Borland.",
    ),

    # Res 14 – Provence: update 141.5 to reflect 1497 declaration + 1499 war end
    (
        norm("Provence is a polity in the south of Gaul on the Middlesea coast, first "
             "independent in 1499, with its capital city at Marsella."),
        "Provence is a polity in the south of Gaul on the Middlesea coast; its independence "
        "was declared on 21 June 1497 and formally recognised at the end of the War of "
        "Provincial Independence in 1499; its capital city is Marsella.",
    ),

    # Res 17 – Damvath: remove imprecise "on the east coast" in 26.5
    (
        norm("Damvath is a port city on the east coast of Borland."),
        "Damvath is a port city in eastern Borland, situated on the River Dam some way inland "
        "from the coast; the river remains tidal in the city's eastern portions.",
    ),

    # Res 21 – Avosche instability: add temporal qualifier to 69.5 stability/instability claim
    (
        norm("Avosche has at various points been a county, a duchy, and a march, and has seen "
             "both continual territorial instability and major urban development into the modern period."),
        "Avosche has at various points been a county, a duchy, and a march; while unusually "
        "stable during the Revitalist Period of the mid-sixteenth century, it experienced "
        "continual territorial instability in other periods, as well as major urban development "
        "into the modern period.",
    ),

    # Res 21 – Avosche stability: add period specification to 45.5 claim
    (
        norm("The duchy of Avosche in Willemy was unusually stable and held by France for over "
             "a century during the Revitalist Period."),
        "The duchy of Avosche in Willemy was unusually stable and held by France for over a "
        "century during the Revitalist Period of the mid-sixteenth century.",
    ),
]

# Build fast lookup: norm(old) → new text
_update_map = {old_n: new_t for old_n, new_t in UPDATES}


# ── 3. New synthesis / terminology claims to append ─────────────────────────
#
# These encode information that was implicit in the resolution notes but is not
# currently represented by any single surviving claim.
#
NEW_CLAIMS = [
    # Res 4 – Anti-Paradism = Deviance movement (terminology clarification)
    {
        "category": "terminology",
        "claim": "Anti-Paradism (also called Anti-Paradise Thought) is an alternative name for the Deviance movement.",
        "entities": [{"name": "Deviance movement", "type": "organisation"}],
    },

    # Res 3 – Voidtale defined as outer-space sub-genre of parachthon romance
    {
        "category": "terminology",
        "claim": "Voidtale is a sub-genre of parachthon romance concerned with outer space.",
        "entities": [{"name": "voidtale", "type": "terminology"}],
    },

    # Res 15 – Axbane connection sequence: air-steeples 1830s → undersea 1850s
    {
        "category": "technology",
        "claim": ("The Rustigh Strait steeplepost connection between Borland and Willemy was "
                  "initially made via air-steeples in the 1830s N; these were later replaced by "
                  "one of the world's first undersea barric steeplepost lines in the 1850s N."),
        "entities": [
            {"name": "Borland", "type": "place"},
            {"name": "Willemy", "type": "place"},
        ],
        "dates": ["1830s N", "1850s N"],
    },

    # Res 18 – Hasiny: both derivations unified
    {
        "category": "terminology",
        "claim": ("The name Hasiny derives from a confederation of the same name which spanned "
                  "lands now part of Hasiny and Taisha; the confederation's name itself comes "
                  "from the Ractish word Hás\u00edne, meaning 'our people'."),
        "entities": [{"name": "Hasiny", "type": "place"}],
    },
]


def main():
    with open(SRC, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    claims = data["claims"]
    print(f"Loaded {len(claims)} claims from {SRC}")

    result    = []
    deleted   = 0
    updated   = 0
    unflagged = 0

    for c in claims:
        nk = norm(c.get("claim", ""))

        # Step 1 – delete superseded / wrong claims
        if nk in DELETE_NORMS:
            deleted += 1
            continue

        # Step 2 – shallow copy before mutation
        c = dict(c)

        # Step 3 – update claim text where canon resolution changes it
        if nk in _update_map:
            c["claim"] = _update_map[nk]
            updated += 1

        # Step 4 – remove _canon_contradiction annotation (all 23 resolved)
        if "_canon_contradiction" in c:
            del c["_canon_contradiction"]
            unflagged += 1

        result.append(c)

    # Step 5 – append new synthesis claims
    for nc in NEW_CLAIMS:
        result.append(nc)

    # ── Report ────────────────────────────────────────────────────────────
    remaining_flags = sum(1 for c in result if "_canon_contradiction" in c)
    print(f"Deleted:            {deleted} claims")
    print(f"Updated (text):     {updated} claims")
    print(f"Unflagged:          {unflagged} claims")
    print(f"New claims added:   {len(NEW_CLAIMS)}")
    print(f"Output total:       {len(result)} claims")
    if remaining_flags:
        print(f"WARNING: {remaining_flags} claims still carry _canon_contradiction (unexpected)")
    else:
        print("All _canon_contradiction flags cleared.")

    # ── Write ─────────────────────────────────────────────────────────────
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("# Boralverse Phase 2 — Final Consolidated Fact Claims\n")
        fh.write(f"# {len(result)} claims after semantic deduplication and full canon resolution\n")
        fh.write("# All 23 canon contradictions resolved per authorial guidance\n\n")
        yaml.dump({"claims": result}, fh, allow_unicode=True,
                  default_flow_style=False, sort_keys=False, width=120)

    print(f"Written: {OUT}")


if __name__ == "__main__":
    main()
