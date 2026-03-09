"""
Apply all *_recs.yaml recommendations to all_claims_deduped.yaml.

Produces:
  all_claims_clean.yaml       — deduplicated, with _canon_contradiction annotations
  canon_contradictions.yaml   — summary of all contradictions found
  apply_recs_report.txt       — which recs were matched/unmatched
"""

import os, re, yaml
from glob import glob

FOLDER    = os.path.dirname(os.path.abspath(__file__))
CLUSTERS  = os.path.join(FOLDER, "clusters")
SRC       = os.path.join(FOLDER, "all_claims_deduped.yaml")
OUT       = os.path.join(FOLDER, "all_claims_clean.yaml")
CONTRA    = os.path.join(FOLDER, "canon_contradictions.yaml")
REPORT    = os.path.join(FOLDER, "apply_recs_report.txt")


def norm(s):
    return re.sub(r"\s+", " ", str(s).lower().strip())

def load_claims():
    with open(SRC, encoding="utf-8") as fh:
        return yaml.safe_load(fh)["claims"]

def load_all_recs():
    """Return list of (source_file, entity, group_dict) for every group in every recs file."""
    rows = []
    for path in sorted(glob(os.path.join(CLUSTERS, "*_recs.yaml"))):
        fname = os.path.basename(path)
        with open(path, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        if not data or "entity_reviews" not in data:
            continue
        for review in data["entity_reviews"]:
            for group in (review.get("near_duplicate_groups") or []):
                rows.append((fname, review.get("entity", "?"), group))
    return rows

def main():
    claims    = load_claims()
    all_recs  = load_all_recs()
    print(f"Loaded {len(claims)} claims, {len(all_recs)} recommendation groups from recs files")

    # Build an index of all claim texts for quick lookup
    norm_to_claims = {}  # norm_text → list of claim dicts
    for c in claims:
        nk = norm(c.get("claim", ""))
        norm_to_claims.setdefault(nk, []).append(c)

    # ----------------------------------------------------------------
    # Parse recommendations into action tables
    # ----------------------------------------------------------------
    remove_keys      = set()           # norm(text) → remove claim
    merge_jobs       = []              # list of {entity, original_norms, merged, entries, reason}
    contradiction_map = {}             # norm(text) → note string
    contradictions_list = []

    report_lines = []
    unmatched = []

    for fname, entity, group in all_recs:
        cig   = group.get("claims_in_group") or []
        action = group.get("action", "")

        # Verify all claims in group exist in source
        for c in cig:
            nk = norm(c.get("claim", ""))
            if nk not in norm_to_claims:
                unmatched.append({
                    "source": fname, "entity": entity,
                    "action": action, "missing_claim": c.get("claim", "")
                })

        if action == "remove_duplicates":
            keep_entry = str(group.get("keep_entry", ""))
            for c in cig:
                if str(c.get("entry", "")) != keep_entry:
                    remove_keys.add(norm(c.get("claim", "")))
            report_lines.append(
                f"[remove_dup] {entity} | keep {keep_entry} | "
                f"drop {[str(c.get('entry')) for c in cig if str(c.get('entry')) != keep_entry]}"
            )

        elif action == "merge":
            mc = group.get("merged_claim")
            if mc:
                # Some agents wrote merged_claim as a plain string; normalise to dict
                if isinstance(mc, str):
                    first_nk = norm(cig[0].get("claim", "")) if cig else None
                    first_src = (norm_to_claims.get(first_nk) or [{}])[0]
                    mc = {
                        "category": first_src.get("category", "other"),
                        "claim": mc.strip(),
                        "entities": first_src.get("entities", []),
                    }
                group_norms = {norm(c.get("claim", "")) for c in cig}
                remove_keys.update(group_norms)
                merge_jobs.append({
                    "entity": entity,
                    "original_norms": group_norms,
                    "merged": mc,
                    "entries": [c.get("entry") for c in cig],
                    "reason": group.get("reason", ""),
                })
                report_lines.append(
                    f"[merge]      {entity} | "
                    f"entries {[c.get('entry') for c in cig]} → new merged claim"
                )

        elif action == "flag_contradiction":
            note = group.get("contradiction_note") or group.get("reason") or ""
            contradictions_list.append({
                "entity": entity,
                "source_file": fname,
                "note": note,
                "claims": cig,
            })
            for c in cig:
                nk = norm(c.get("claim", ""))
                contradiction_map[nk] = note
            report_lines.append(
                f"[contradict] {entity} | "
                f"entries {[c.get('entry') for c in cig]}"
            )

    # ----------------------------------------------------------------
    # Apply to claims list
    # ----------------------------------------------------------------
    result  = []
    removed = 0
    flagged = 0

    for c in claims:
        nk = norm(c.get("claim", ""))
        if nk in remove_keys:
            removed += 1
            continue
        if nk in contradiction_map:
            c = dict(c)
            c["_canon_contradiction"] = contradiction_map[nk]
            flagged += 1
        result.append(c)

    # Append merged claims (these are new; no natural position, so append at end)
    for mj in merge_jobs:
        mc = dict(mj["merged"])
        mc["_merged_from_entries"] = mj["entries"]
        mc["_merge_reason"] = mj["reason"]
        result.append(mc)

    # ----------------------------------------------------------------
    # Write outputs
    # ----------------------------------------------------------------
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("# Boralverse Phase 2 — Clean Deduplicated Fact Claims\n")
        fh.write(f"# {len(result)} claims after semantic deduplication\n")
        fh.write("# Claims annotated _canon_contradiction need authorial resolution\n")
        fh.write("# Merged claims are appended at the end and carry _merged_from_entries\n\n")
        yaml.dump({"claims": result}, fh, allow_unicode=True,
                  default_flow_style=False, sort_keys=False, width=120)

    with open(CONTRA, "w", encoding="utf-8") as fh:
        fh.write("# Canon Contradictions — Boralverse Phase 2 Deduplication\n")
        fh.write(f"# {len(contradictions_list)} contradictions requiring authorial resolution\n\n")
        yaml.dump({"contradictions": contradictions_list}, fh, allow_unicode=True,
                  default_flow_style=False, sort_keys=False, width=120)

    with open(REPORT, "w", encoding="utf-8") as fh:
        fh.write(f"=== apply_recs.py report ===\n\n")
        fh.write(f"Input:   {len(claims)} claims\n")
        fh.write(f"Removed: {removed}\n")
        fh.write(f"Merged:  {len(merge_jobs)} groups → {len(merge_jobs)} new merged claims\n")
        fh.write(f"Flagged: {flagged} contradiction-annotated claims\n")
        fh.write(f"Output:  {len(result)} claims\n\n")
        fh.write("--- Actions applied ---\n")
        for l in report_lines:
            fh.write(l + "\n")
        if unmatched:
            fh.write(f"\n--- UNMATCHED recs ({len(unmatched)}) ---\n")
            for u in unmatched:
                fh.write(f"  [{u['source']}] {u['entity']} / {u['action']}: "
                         f"{u['missing_claim'][:80]!r}\n")

    print(f"Removed: {removed}, Merged groups: {len(merge_jobs)}, Flagged: {flagged}")
    print(f"Output: {len(result)} claims")
    if unmatched:
        print(f"WARNING: {len(unmatched)} recommendation entries did not match any claim in source")
    print(f"Written: {OUT}")
    print(f"Written: {CONTRA}")
    print(f"Written: {REPORT}")

if __name__ == "__main__":
    main()
