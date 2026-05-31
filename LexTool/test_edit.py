"""Validate the surgical write path on a TEMP COPY only -- never the real .db.

For each edit we save, reload from disk, and assert (a) the file still
round-trips byte-for-byte and (b) only the edited entry's text changed.
"""

import os
import shutil
import sys
import tempfile
from pathlib import Path

import sfm

sys.stdout.reconfigure(encoding="utf-8")

REAL = Path(r"C:\Users\awsla\Documents\GitHub\Boralverse\Borlish\Lexique Pro\Data\Borlish.db")
BASE = sfm.read(REAL)
BASE_RAWS = [e.raw for e in BASE.entries]
HW = {e.headword: i for i, e in enumerate(BASE.entries)}


def fresh_copy() -> Path:
    fd, tmp = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    shutil.copy2(REAL, tmp)
    return Path(tmp)


def items_of(entry):
    return [{"srcIndex": i, "marker": u.marker, "value": u.value} for i, u in enumerate(entry.units)]


def verify(tmp: Path, changed_idx: int):
    data = tmp.read_bytes()
    lex2 = sfm.read(tmp)
    assert lex2.to_bytes() == data, "round-trip broken after save!"
    diffs = [i for i, e in enumerate(lex2.entries) if e.raw != BASE_RAWS[i]]
    assert diffs == [changed_idx], f"expected only entry {changed_idx} to change, got {diffs}"
    return lex2


def edit_value(lex):
    i = HW["a cascun"]
    items = items_of(lex.entries[i])
    for it in items:
        if it["marker"] == "ge":
            it["value"] += " (TEST)"
            break
    lex.entries[i].apply_fields(items)
    return i


def add_gloss(lex):
    i = HW["a cascun"]
    items = items_of(lex.entries[i])
    last_ge = max(k for k, it in enumerate(items) if it["marker"] == "ge")
    items.insert(last_ge + 1, {"srcIndex": None, "marker": "ge", "value": "ZZNEWGLOSS"})
    lex.entries[i].apply_fields(items)
    return i


def delete_mn(lex):
    i = HW["a cascun"]
    items = [it for it in items_of(lex.entries[i]) if it["marker"] != "mn"]
    lex.entries[i].apply_fields(items)
    return i


def add_et_group(lex):
    i = next(j for j, e in enumerate(BASE.entries) if e.get("et") is None and e.get("xv") is None)
    items = items_of(lex.entries[i])
    items.append({"srcIndex": None, "marker": "et", "value": "test etymology"})
    lex.entries[i].apply_fields(items)
    return i


def main():
    bad = sum(1 for e in BASE.entries if "".join(u.text() for u in e.units) != e.raw)
    print(f"GATE  unit reconstruction mismatches : {bad} of {len(BASE.entries)}")
    print(f"GATE  no-edit round-trip identical   : {sfm.read(REAL).to_bytes() == REAL.read_bytes()}")

    for name, fn in [("edit a gloss", edit_value), ("add a gloss", add_gloss),
                     ("delete \\mn", delete_mn), ("add \\et to an entry without one", add_et_group)]:
        tmp = fresh_copy()
        try:
            lex = sfm.read(tmp)
            idx = fn(lex)
            sfm.save(lex, tmp)
            lex2 = verify(tmp, idx)
            print(f"\n=== {name}  ->  entry {idx} '{lex2.entries[idx].headword}'  OK ===")
            print(lex2.entries[idx].raw.replace("\r\n", "\n").rstrip())
        finally:
            tmp.unlink(missing_ok=True)

    print("\nAll edit scenarios passed.")


if __name__ == "__main__":
    main()
