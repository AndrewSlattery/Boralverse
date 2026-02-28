"""
Extract entity clusters from all_claims_deduped.yaml for agent review.
Writes cluster files to a 'clusters/' subdirectory.
"""

import os
import yaml
from collections import defaultdict

FOLDER = os.path.dirname(os.path.abspath(__file__))
SRC    = os.path.join(FOLDER, "all_claims_deduped.yaml")
OUTDIR = os.path.join(FOLDER, "clusters")
os.makedirs(OUTDIR, exist_ok=True)

def primary_entity(claim):
    entities = claim.get("entities") or []
    if entities:
        return str(entities[0].get("name", "")).strip()
    return "_no_entity"

def load_grouped():
    with open(SRC, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    groups = defaultdict(list)
    for c in data["claims"]:
        groups[primary_entity(c)].append(c)
    return groups

def write_cluster(name, entity_groups):
    """Write a cluster file with claims for a set of entities."""
    safe = name.replace(" ", "_").replace("/", "-").replace(":", "-")
    path = os.path.join(OUTDIR, f"{safe}.yaml")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(f"# Deduplication cluster: {name}\n\n")
        combined = {}
        for ent, claims in entity_groups.items():
            combined[ent] = claims
        yaml.dump(combined, fh, allow_unicode=True, default_flow_style=False,
                  sort_keys=False, width=120)
    print(f"  Written: {path} ({sum(len(v) for v in entity_groups.values())} claims)")

def main():
    groups = load_grouped()

    # --- Cluster assignments (by primary-entity count, descending) ---
    clusters = {
        "A_Borland": ["Borland"],
        "B_Portingale_Borlish_ElsebethSneider": ["Portingale", "Borlish", "Elsebeth Sneider"],
        "C_AmbroseIII_Vascony_MysarnosCodex": ["Ambrose III", "Vascony", "Mysarnos Codex"],
        "D_Brethin_FirstDrengot_Adaille_Burgundy": ["Brethin", "First Drengot Empire",
                                                     "Adaill\u00e9 Nassow", "Burgundy"],
        "E_Mysarnos_steeplepost_DrengotCollusion_Vigo": ["Mysarnos", "steeplepost",
                                                          "Drengot Collusion",
                                                          "Vigo the Magnificent"],
        "F_Morrack_NewProvence_Provence_Axbane": ["Morrack", "New Provence", "Provence",
                                                   "Axbane"],
        "G_Britain_ConvoyAustralier_Damvath_London": ["Britain", "Convoy Australier",
                                                       "Damvath", "London"],
        "H_Markland_Revillon_Southbar_Devon_Kent": ["Markland", "Revillon", "Southbar",
                                                     "Devon", "Kent"],
        "I_Saxony_Hasiny_JotheyOfBorland_LongPeace": ["Saxony", "Hasiny",
                                                        "Jothey of Borland", "Long Peace"],
        "J_MunirAlHamdawi_SecondGreatDying_Absolon_Joseph": [
            "Munir al-Hamdawi", "Second Great Dying", "Absolon Mortenszen", "Joseph III"],
        "K_Avosche_Deviance_dime_Fiellas": ["Avosche", "Deviance movement",
                                            "dime measures", "Fiellas Dimenja"],
    }

    for cluster_name, entities in clusters.items():
        entity_data = {e: groups.get(e, []) for e in entities}
        write_cluster(cluster_name, entity_data)

    # Summary
    print("\nAll clusters written to:", OUTDIR)

if __name__ == "__main__":
    main()
