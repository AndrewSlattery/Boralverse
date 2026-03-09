"""
Extract all claims for one or more named entities from all_claims_deduped.yaml.
Usage: py extract_entity.py EntityName1 "Entity Name 2" ...
Prints as YAML to stdout.
"""

import sys
import yaml

FOLDER = r"C:\Users\awsla\Documents\GitHub\Boralverse\Borlish\Obsidian\.claude\worktrees\romantic-kirch\Borlish\Obsidian\Fact Claim Extraction - Phase 2"

def primary_entity(claim):
    entities = claim.get("entities") or []
    if entities:
        return str(entities[0].get("name", "")).strip()
    return ""

def main():
    targets = set(sys.argv[1:])
    if not targets:
        print("Usage: py extract_entity.py EntityName1 [EntityName2 ...]")
        sys.exit(1)

    with open(f"{FOLDER}/all_claims_deduped.yaml", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)

    result = {}
    for c in data["claims"]:
        pe = primary_entity(c)
        if pe in targets:
            result.setdefault(pe, []).append(c)

    output = {ent: result.get(ent, []) for ent in sorted(targets)}
    sys.stdout.buffer.write(yaml.dump(output, allow_unicode=True, default_flow_style=False, sort_keys=False, width=100).encode("utf-8"))

if __name__ == "__main__":
    main()
