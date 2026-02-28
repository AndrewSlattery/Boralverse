"""
Remove exact-duplicate claim texts from all_claims.yaml.
Keeps the version with the most information (most fields filled in).
Writes all_claims_deduped.yaml.
"""

import os
import re
import yaml
from collections import defaultdict

FOLDER = os.path.dirname(os.path.abspath(__file__))
ALL    = os.path.join(FOLDER, "all_claims.yaml")
OUT    = os.path.join(FOLDER, "all_claims_deduped.yaml")

def load():
    with open(ALL, encoding="utf-8") as fh:
        return yaml.safe_load(fh)["claims"]

def normalise(s):
    return re.sub(r"\s+", " ", str(s).lower().strip())

def score(claim):
    """Higher = more information-rich. Used to pick the best copy."""
    s = 0
    if claim.get("dates"):         s += 2
    if claim.get("relationships"): s += 2
    entities = claim.get("entities") or []
    for e in entities:
        s += 1
        if e.get("irl"):  s += 1
    return s

def pick_best(occurrences):
    """Return the occurrence with the highest info score."""
    return max(occurrences, key=score)

def main():
    claims = load()
    print(f"Input: {len(claims)} claims")

    by_text = defaultdict(list)
    for c in claims:
        key = normalise(c.get("claim", ""))
        by_text[key].append(c)

    result = []
    removed = 0
    for key, group in by_text.items():
        if len(group) == 1:
            result.append(group[0])
        else:
            best = pick_best(group)
            result.append(best)
            removed += len(group) - 1
            # Merge source entry references so we don't lose provenance
            all_entries = [g.get("entry", "") for g in group]
            best["_also_in_entries"] = [e for e in all_entries if e != best.get("entry", "")]

    print(f"Removed {removed} exact duplicates.")
    print(f"Output: {len(result)} claims")

    # Sort by entry id then by original order (they come sorted from load)
    def entry_key(c):
        try:
            return float(str(c.get("entry", 0)).replace(" ", ""))
        except Exception:
            return 9999.0

    result.sort(key=entry_key)

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(f"# Boralverse Phase 2 — Deduplicated Fact Claims\n")
        fh.write(f"# {len(result)} claims (exact duplicates removed)\n\n")
        yaml.dump(
            {"claims": result},
            fh,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False,
            width=120,
        )
    print(f"Written to {OUT}")

if __name__ == "__main__":
    main()
