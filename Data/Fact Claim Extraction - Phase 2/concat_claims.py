"""
Concatenate all *_claims.yaml files into a single all_claims.yaml.

Output format: a single YAML document with a flat list of all claims,
each annotated with its source entry id and title.
Files are sorted numerically by entry id.
"""

import os
import re
import yaml

FOLDER = os.path.dirname(os.path.abspath(__file__))
OUTPUT  = os.path.join(FOLDER, "all_claims.yaml")

def entry_sort_key(filename):
    """Sort by the numeric prefix, e.g. '26.5_claims.yaml' → 26.5"""
    m = re.match(r"^(\d+(?:\.\d+)?)_claims\.yaml$", filename)
    return float(m.group(1)) if m else float("inf")

def load_all():
    files = [f for f in os.listdir(FOLDER)
             if re.match(r"^\d+.*_claims\.yaml$", f)]
    files.sort(key=entry_sort_key)

    all_claims = []
    for fname in files:
        path = os.path.join(FOLDER, fname)
        with open(path, encoding="utf-8") as fh:
            doc = yaml.safe_load(fh)
        if not doc or not doc.get("claims"):
            continue
        entry_id    = doc.get("entry", "")
        title       = doc.get("title", "")
        source_work = doc.get("source_work", None)
        for claim in doc["claims"]:
            row = {
                "entry":  entry_id,
                "title":  title,
            }
            if source_work:
                row["source_work"] = source_work
            row.update(claim)
            all_claims.append(row)
    return all_claims

def main():
    claims = load_all()
    print(f"Loaded {len(claims)} claims from {FOLDER}")

    with open(OUTPUT, "w", encoding="utf-8") as fh:
        fh.write("# Boralverse Phase 2 — All Fact Claims (concatenated)\n")
        fh.write(f"# {len(claims)} claims from all entry files\n\n")
        yaml.dump(
            {"claims": claims},
            fh,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False,
            width=120,
        )
    print(f"Written to {OUTPUT}")

if __name__ == "__main__":
    main()
