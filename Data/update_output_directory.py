#!/usr/bin/env python3
"""
Regenerate Data/output_directory/ from Scaunç.txt.

Routes entries by sub-number:
  .1            -> excerpt/
  .5            -> notes/
  .2/.3/.4/.6/.7 -> dictionary/

Writes manifest.tsv and summary.txt alongside the folders.

Source: Scaunç.txt in the repo root (contains the newest drafts, a superset
of Data/2023–.txt at time of writing).
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE = REPO_ROOT / "Scaunç.txt"
OUT = REPO_ROOT / "Data" / "output_directory"

NOTES_DIR = OUT / "notes"
EXCERPT_DIR = OUT / "excerpt"
DICT_DIR = OUT / "dictionary"

HEADER_RE = re.compile(r'^(\d+)\.(\d+):\s*(.*)$')
# Dictionary title shape: headword "gloss" — headword may be a multi-word phrase
DICT_TITLE_RE = re.compile(r'^(?P<hw>.+?)\s+"(?P<gloss>[^"]*)"\s*$')


def sanitise(s: str) -> str:
    s = s.strip()
    s = re.sub(r'[\\/:*?"<>|]', '_', s)
    s = re.sub(r'[\s_]+', '_', s)
    return s.strip('_')


def folder_for(sub: int) -> tuple[Path, str]:
    if sub == 1:
        return EXCERPT_DIR, "excerpt"
    if sub == 5:
        return NOTES_DIR, "notes"
    return DICT_DIR, "dictionary"


def clear_folder(p: Path) -> None:
    if not p.exists():
        p.mkdir(parents=True, exist_ok=True)
        return
    for f in p.iterdir():
        if f.is_file():
            f.unlink()


def main() -> int:
    if not SOURCE.exists():
        print(f"ERROR: source not found: {SOURCE}", file=sys.stderr)
        return 1

    for d in (NOTES_DIR, EXCERPT_DIR, DICT_DIR):
        clear_folder(d)

    text = SOURCE.read_text(encoding="utf-8")
    raw_blocks = re.split(r'\n##\n', text)

    manifest_rows: list[dict] = []
    counts = {"excerpt": 0, "notes": 0, "dictionary": 0, "unknown": 0}
    words_by_type = {"excerpt": 0, "notes": 0, "dictionary": 0, "unknown": 0}
    posts_seen: set[int] = set()
    written = 0
    skipped_unheaded = 0
    skipped_empty_body = 0

    for block in raw_blocks:
        block = block.strip()
        if not block:
            continue

        lines = block.splitlines()
        first = lines[0].strip()
        m = HEADER_RE.match(first)
        if not m:
            skipped_unheaded += 1
            continue

        major, sub, title = int(m.group(1)), int(m.group(2)), m.group(3).strip()
        body = "\n".join(lines[1:]).strip()

        # Skip placeholder entries: header present but no content below.
        if not body:
            skipped_empty_body += 1
            continue

        dest_dir, type_label = folder_for(sub)
        counts[type_label] += 1
        posts_seen.add(major)

        # Build filename.
        if type_label == "dictionary":
            dm = DICT_TITLE_RE.match(title)
            if dm:
                headword = dm.group("hw").strip()
                gloss = dm.group("gloss").strip()
                name_part = sanitise(f"{headword} {gloss}")
                pretty_title = f'{headword} "{gloss}"'
            else:
                headword = ""
                gloss = ""
                name_part = sanitise(title) if title else "untitled"
                pretty_title = title
        else:
            headword = ""
            gloss = ""
            name_part = sanitise(title) if title else "untitled"
            pretty_title = title

        filename = f"{major}.{sub}_{name_part}.md"
        dest = dest_dir / filename

        # Entry file contains the original header line plus the body, matching the
        # pre-existing format (e.g. the first line is "206.5: The Scathe of Saint Sophia").
        header_line = f"{major}.{sub}: {title}".rstrip()
        content = header_line + "\n\n" + body + "\n"
        dest.write_text(content, encoding="utf-8")
        written += 1

        word_count = len(body.split())
        char_count = len(body)
        has_etym = bool(re.search(r'^Etymology:', body, flags=re.MULTILINE))
        sense_count = len(re.findall(r'^\s*-\s', body, flags=re.MULTILINE))

        words_by_type[type_label] += word_count

        manifest_rows.append({
            "entry_id": f"{major}.{sub}",
            "type": type_label,
            "title": pretty_title,
            "headword": headword,
            "gloss": gloss,
            "has_etymology": has_etym,
            "sense_count": sense_count,
            "word_count": word_count,
            "char_count": char_count,
            "filename": f"{type_label}/{filename}",
        })

    # Sort manifest by (major, sub) numerically.
    def _key(row: dict) -> tuple[int, int]:
        a, b = row["entry_id"].split(".")
        return int(a), int(b)

    manifest_rows.sort(key=_key)

    manifest_path = OUT / "manifest.tsv"
    with manifest_path.open("w", encoding="utf-8", newline="") as fh:
        cols = ["entry_id", "type", "title", "headword", "gloss",
                "has_etymology", "sense_count", "word_count", "char_count", "filename"]
        fh.write("\t".join(cols) + "\n")
        for r in manifest_rows:
            row = [
                r["entry_id"],
                r["type"],
                tsv_escape(r["title"]),
                r["headword"],
                r["gloss"],
                str(r["has_etymology"]),
                str(r["sense_count"]),
                str(r["word_count"]),
                str(r["char_count"]),
                r["filename"],
            ]
            fh.write("\t".join(row) + "\n")

    # Summary.
    total_entries = sum(counts.values())
    total_words = sum(words_by_type.values())
    post_range = (min(posts_seen), max(posts_seen)) if posts_seen else (0, 0)

    summary = [
        "Phase 1 Split & Classify — Summary",
        "=" * 40,
        "",
        f"Total entries:      {total_entries}",
        f"Distinct posts:     {len(posts_seen)}",
        "",
        "By type:",
        f"  excerpt       {counts['excerpt']:>5}",
        f"  dictionary    {counts['dictionary']:>5}",
        f"  notes         {counts['notes']:>5}",
        "",
        "Word count by type:",
        f"  excerpt       {words_by_type['excerpt']:>7,} words",
        f"  dictionary    {words_by_type['dictionary']:>7,} words",
        f"  notes         {words_by_type['notes']:>7,} words",
        f"  total         {total_words:>7,} words",
        "",
        f"Post range:         {post_range[0]} – {post_range[1]}",
        "",
        f"Source: {SOURCE.name}",
        f"Blocks without header skipped: {skipped_unheaded}",
        f"Blocks with header but empty body skipped: {skipped_empty_body}",
    ]
    (OUT / "summary.txt").write_text("\n".join(summary) + "\n", encoding="utf-8")

    print(f"Wrote {written} entry files.")
    print(f"  excerpt:    {counts['excerpt']}")
    print(f"  dictionary: {counts['dictionary']}")
    print(f"  notes:      {counts['notes']}")
    print(f"Posts: {len(posts_seen)} (range {post_range[0]}–{post_range[1]})")
    print(f"Skipped: {skipped_unheaded} unheaded, {skipped_empty_body} empty-body")
    return 0


def tsv_escape(s: str) -> str:
    return s.replace("\t", " ").replace("\n", " ").strip()


if __name__ == "__main__":
    raise SystemExit(main())
