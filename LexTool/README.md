# LexTool

A small, dependency-free tool for browsing and (soon) editing a Lexique Pro
lexicon, built to outlive Lexique Pro itself. The `.db` file stays the single
source of truth — LexTool reads and writes that file directly, so the lexicon
remains fully backwards-compatible with Lexique Pro.

## Running it

Requires Python 3 (tested on 3.14). No packages to install.

```
run.bat          # or:  py server.py
```

This serves a browser UI at <http://127.0.0.1:8765/> and opens your browser.
Editing writes back to the `.db` through a safety layer: a timestamped backup
(in `LexTool/backups/`) on the first edit of each session, then an atomic
write-and-swap. Only the entries you actually change are rewritten.

To point at a different database, edit `DEFAULT_DB` near the top of `server.py`
(or set the `LEXTOOL_DB` environment variable).

## The data format

`Borlish.db` is plain UTF-8 text (with a BOM, CRLF line endings) in SIL's
**MDF Standard Format Marker** layout. Each record starts at a `\lx` line:

| Marker | Meaning | | Marker | Meaning |
|---|---|---|---|---|
| `\lx` | lexeme / headword | | `\xv` | example (Borlish) |
| `\hm` | homonym number | | `\xe` | example translation |
| `\ps` | part of speech | | `\et` | etymology |
| `\ge` | gloss (English) | | `\mn` | cross-ref to main entry |
| `\de` / `\dv` | definition (En / Bor) | | `\sd` | semantic domain |
| `\se` | subentry | | `\ue` / `\uv` | usage (En / Bor) |

Sibling files in the LP data folder (`.idx`, `.lpCache-*`) are **derived
indexes/caches** and are regenerable; `.lpConfig` holds LP's display settings,
including the Borlish alphabet `a b c ç d ð e f g h i j k l m n o p q r s t u v
x y z` and sort rules.

## The core contract: faithful round-trips

`sfm.py` parses the file but keeps each record's **raw original text**.
Re-emitting an untouched lexicon is byte-for-byte identical to the input
(verified by `test_roundtrip.py` on all 6,403 entries). When editing lands,
only the records you actually change will be re-serialized — so git diffs stay
clean and Lexique Pro keeps working.

```
py test_roundtrip.py     # proves read -> write is byte-identical
```

## Files

| File | Role |
|---|---|
| `sfm.py` | SFM/MDF parser + round-trip-faithful serializer |
| `server.py` | stdlib HTTP server + JSON API |
| `web/` | browser UI (search, browse, dictionary view) |
| `test_roundtrip.py` | round-trip fidelity proof |
| `test_edit.py` | surgical-write proof (runs on a temp copy) |
| `run.bat` | launcher |

## Roadmap

- [x] Parser + byte-identical round-trip
- [x] Browser app: search, browse (custom sort), dictionary view
- [x] Safety layer: timestamped backups, atomic write-and-swap
- [x] Edit existing entries (surgical, formatting-preserving writes): edit/add/remove fields
- [ ] Create brand-new entries (new `\lx` records)
- [ ] Bulk / maintenance: validation (dangling `\mn`), find-and-replace, index regen
