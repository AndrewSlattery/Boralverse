"""
Analyze all_claims.yaml for:
1. Exact duplicate claim strings
2. Claims grouped by their primary entity name
   (to help find semantic near-duplicates)

Outputs:
  - exact_dupes.yaml   : claims whose claim-text appears more than once
  - by_entity.yaml     : claims grouped by the first entity name in each claim,
                         sorted alphabetically; only groups with >1 claim
"""

import os
import re
import yaml
from collections import defaultdict

FOLDER = os.path.dirname(os.path.abspath(__file__))
ALL    = os.path.join(FOLDER, "all_claims.yaml")

def load():
    with open(ALL, encoding="utf-8") as fh:
        return yaml.safe_load(fh)["claims"]

def normalise(s):
    """Lowercase and collapse whitespace for fuzzy matching."""
    return re.sub(r"\s+", " ", str(s).lower().strip())

def primary_entity(claim):
    entities = claim.get("entities") or []
    if entities:
        return str(entities[0].get("name", "")).strip()
    return ""

def main():
    claims = load()
    print(f"Total claims: {len(claims)}")

    # --- 1. Exact duplicates (by normalised claim text) ---
    by_text = defaultdict(list)
    for c in claims:
        key = normalise(c.get("claim", ""))
        by_text[key].append(c)

    exact_dupes = {k: v for k, v in by_text.items() if len(v) > 1}
    print(f"Claim texts that appear >1 time: {len(exact_dupes)}")

    dupe_list = [
        {
            "normalised_text": k,
            "count": len(v),
            "occurrences": v,
        }
        for k, v in sorted(exact_dupes.items(), key=lambda x: -len(x[1]))
    ]
    with open(os.path.join(FOLDER, "exact_dupes.yaml"), "w", encoding="utf-8") as fh:
        fh.write(f"# {len(dupe_list)} normalised claim texts appearing in >1 entry\n\n")
        yaml.dump({"duplicates": dupe_list}, fh, allow_unicode=True,
                  default_flow_style=False, sort_keys=False, width=120)

    # --- 2. Group by primary entity ---
    by_entity = defaultdict(list)
    for c in claims:
        ent = primary_entity(c)
        if not ent:
            ent = "_no_entity"
        by_entity[ent].append(c)

    # Only emit groups with more than one claim (the interesting ones)
    multi = {k: v for k, v in by_entity.items() if len(v) > 1}
    print(f"Entities with >1 claim: {len(multi)}")

    entity_groups = [
        {
            "entity": k,
            "count": len(v),
            "claims": v,
        }
        for k, v in sorted(multi.items(), key=lambda x: x[0].lower())
    ]

    with open(os.path.join(FOLDER, "by_entity.yaml"), "w", encoding="utf-8") as fh:
        total_in_groups = sum(g["count"] for g in entity_groups)
        fh.write(f"# Claims grouped by primary entity — {len(entity_groups)} entities, "
                 f"{total_in_groups} claims\n\n")
        yaml.dump({"entity_groups": entity_groups}, fh, allow_unicode=True,
                  default_flow_style=False, sort_keys=False, width=120)

    print("Done. See exact_dupes.yaml and by_entity.yaml")

if __name__ == "__main__":
    main()
