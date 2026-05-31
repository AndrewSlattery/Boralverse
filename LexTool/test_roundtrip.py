"""Proof of the core contract: parsing the real Borlish.db and re-emitting it
must produce byte-identical output. Read-only on the data file."""

from pathlib import Path

import sfm

DB = Path(
    r"C:\Users\awsla\Documents\GitHub\Boralverse\Borlish\Lexique Pro\Data\Borlish.db"
)


def main() -> None:
    original = DB.read_bytes()
    lex = sfm.read(DB)
    out = lex.to_bytes()

    print(f"Original bytes  : {len(original)}")
    print(f"Re-emitted bytes: {len(out)}")
    print(f"BYTE-IDENTICAL  : {original == out}")
    print(f"Entries parsed  : {len(lex.entries)}  (expected 6403)")
    print(f"Has BOM         : {lex.has_bom}")
    print(f"Header          : {lex.header!r}")

    if original != out:
        for i, (a, b) in enumerate(zip(original, out)):
            if a != b:
                lo = max(0, i - 25)
                print(f"First diff at byte {i}:")
                print(f"  original: {original[lo:i + 25]!r}")
                print(f"  emitted : {out[lo:i + 25]!r}")
                break
        print(f"length delta: {len(original) - len(out)}")

    # Spot-check field parsing on a known rich entry ("a cascun": has xv/xe/et).
    sample = next(e for e in lex.entries if e.headword == "a cascun")
    print("\nParsed fields for entry 'a cascun':")
    for f in sample.fields:
        v = f.value if len(f.value) <= 70 else f.value[:67] + "..."
        print(f"  \\{f.marker:<3} {v!r}")


if __name__ == "__main__":
    main()
