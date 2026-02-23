#!/usr/bin/env python3
"""
Split 2023–.txt into individual entry files, organised into:
  translations/   — entries x.1
  documents/      — entries x.5
  dictionary/     — entries x.2, x.3, x.4, x.6, x.7
"""

import re
import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "2023–.txt")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "entries")

TRANSLATIONS_DIR = os.path.join(OUTPUT_DIR, "translations")
DOCUMENTS_DIR    = os.path.join(OUTPUT_DIR, "documents")
DICTIONARY_DIR   = os.path.join(OUTPUT_DIR, "dictionary")

HEADER_RE = re.compile(r'^(\d+)\.(\d+):(.*)')

def sanitise_filename(s):
    """Strip characters that are illegal in filenames."""
    s = s.strip()
    # Replace characters Windows/Linux/Mac all disallow
    s = re.sub(r'[\\/:*?"<>|]', '_', s)
    # Collapse runs of whitespace/underscores
    s = re.sub(r'[\s_]+', '_', s)
    return s.strip('_')

def folder_for(sub):
    """Return the output folder based on the sub-entry number."""
    sub = int(sub)
    if sub == 1:
        return TRANSLATIONS_DIR
    elif sub == 5:
        return DOCUMENTS_DIR
    else:
        return DICTIONARY_DIR

def main():
    for d in (TRANSLATIONS_DIR, DOCUMENTS_DIR, DICTIONARY_DIR):
        os.makedirs(d, exist_ok=True)

    with open(INPUT_FILE, encoding="utf-8") as fh:
        text = fh.read()

    # Split on the ## separator; keep content before first ## too
    raw_blocks = re.split(r'\n##\n', text)

    written = 0
    skipped = 0

    for block in raw_blocks:
        block = block.strip()
        if not block:
            continue

        # The first non-empty line should be the header
        first_line = block.splitlines()[0].strip()
        m = HEADER_RE.match(first_line)
        if not m:
            print(f"  [skip] no header found: {first_line!r}")
            skipped += 1
            continue

        major, sub, title = m.group(1), m.group(2), m.group(3)
        title_clean = sanitise_filename(title) if title.strip() else "untitled"
        filename = f"{major}.{sub}_{title_clean}.txt"
        dest_dir = folder_for(sub)
        dest_path = os.path.join(dest_dir, filename)

        with open(dest_path, "w", encoding="utf-8") as out:
            out.write(block + "\n")

        written += 1

    print(f"Done. Wrote {written} files, skipped {skipped} blocks.")

if __name__ == "__main__":
    main()
