"""Round-trip-faithful parser, editor, and serializer for Lexique Pro / SIL MDF
.db files.

The .db file is plain UTF-8 text in Standard Format Marker (SFM) layout: each
line is either ``\\marker value`` or a continuation of the previous field, and a
record begins at every ``\\lx`` line. Lexique Pro writes the file with a UTF-8
BOM and CRLF line endings, both preserved exactly.

Design contract (the whole point of the tool):

    read(path).to_bytes() == original bytes, byte for byte.

We tokenize each record into Units — a field plus the blank-line gap that
follows it — and keep every Unit's text verbatim. Re-emitting an unedited
lexicon is just concatenation, so fidelity is guaranteed by construction. When
you edit a field, only that field's line is regenerated; its gap, and every
other byte of the file, is left untouched. Writes go through save(), which
backs up and swaps atomically.
"""

from __future__ import annotations

import datetime
import os
import re
import shutil
from dataclasses import dataclass, field as dc_field
from pathlib import Path

BOM_BYTES = b"\xef\xbb\xbf"
NL = "\r\n"

# A record starts at a line-initial \lx followed by whitespace or EOL.
_LX_RE = re.compile(r"(?m)^\\lx(?=[ \t\r\n]|$)")
# A field line: \marker optionally followed by one separator and a value.
_FIELD_RE = re.compile(r"^\\(\S+)(?:[ \t](.*))?$")


@dataclass
class Field:
    marker: str
    value: str  # may contain embedded "\n" for fields wrapped over several lines


def _content_lines(marker: str, value: str) -> list[str]:
    """Physical lines for a (marker, value). A multi-line value becomes a marker
    line plus continuation lines, matching how the file wraps long fields."""
    vlines = value.split("\n")
    head = f"\\{marker}" if (vlines[0] == "" and len(vlines) == 1) else f"\\{marker} {vlines[0]}"
    return [head, *vlines[1:]]


@dataclass
class Unit:
    """One field plus the blank-line gap that follows it. ``content_lines[0]`` is
    the marker line; any further content lines are wrapped continuations.
    ``gap_lines`` are the (usually one) blank lines before the next field. Both
    are kept verbatim so an unedited Unit re-emits byte-for-byte."""

    content_lines: list[str]
    gap_lines: list[str]
    edited: bool = False

    @property
    def marker(self) -> str:
        m = _FIELD_RE.match(self.content_lines[0])
        return m.group(1) if m else ""

    @property
    def value(self) -> str:
        m = _FIELD_RE.match(self.content_lines[0])
        head = (m.group(2) or "") if m else self.content_lines[0]
        rest = self.content_lines[1:]
        return "\n".join([head, *rest]) if rest else head

    def set_value(self, value: str) -> None:
        self.content_lines = _content_lines(self.marker, value)
        self.edited = True

    def text(self) -> str:
        return "".join(line + NL for line in (*self.content_lines, *self.gap_lines))


def parse_units(record_text: str) -> list[Unit]:
    phys = record_text.split(NL)
    if phys and phys[-1] == "":
        phys = phys[:-1]  # drop the empty tail left by the record's final CRLF
    units: list[Unit] = []
    i, n = 0, len(phys)
    while i < n:
        content = [phys[i]]
        i += 1
        while i < n and phys[i].strip() != "" and not phys[i].startswith("\\"):
            content.append(phys[i])  # wrapped continuation line
            i += 1
        gap: list[str] = []
        while i < n and phys[i].strip() == "":
            gap.append(phys[i])
            i += 1
        units.append(Unit(content, gap))
    return units


@dataclass
class Entry:
    """One \\lx record. ``raw`` is the exact source text. Units are parsed lazily
    and only consulted for display, search, and editing; an unedited entry emits
    its raw text unchanged."""

    raw: str
    dirty: bool = False
    _units: list[Unit] | None = dc_field(default=None, repr=False)

    @property
    def units(self) -> list[Unit]:
        if self._units is None:
            self._units = parse_units(self.raw)
        return self._units

    @property
    def fields(self) -> list[Field]:
        return [Field(u.marker, u.value) for u in self.units]

    def get(self, marker: str) -> str | None:
        for u in self.units:
            if u.marker == marker:
                return u.value
        return None

    def all(self, marker: str) -> list[str]:
        return [u.value for u in self.units if u.marker == marker]

    @property
    def headword(self) -> str:
        return self.get("lx") or ""

    def current_text(self) -> str:
        return "".join(u.text() for u in self.units) if self.dirty else self.raw

    def apply_fields(self, items: list[dict]) -> None:
        """Rebuild the entry from an ordered list of desired fields. Each item is
        {srcIndex: int|None, marker, value}: a srcIndex maps to an existing unit
        (kept verbatim if unchanged, content-regenerated if changed, gap always
        preserved); srcIndex None is a new field. The record's trailing gap is
        kept on the last unit, and new fields take a sensible separator."""
        olds = self.units
        trailing = list(olds[-1].gap_lines) if olds else [""]
        result: list[Unit] = []
        for it in items:
            si, marker, value = it.get("srcIndex"), it["marker"], it["value"]
            if si is not None and 0 <= si < len(olds):
                old = olds[si]
                if old.marker == marker and old.value == value:
                    result.append(old)  # unchanged: verbatim
                else:
                    result.append(Unit(_content_lines(marker, value), list(old.gap_lines), edited=True))
            else:
                result.append(Unit(_content_lines(marker, value), None, edited=True))  # new; gap below
        for i, u in enumerate(result):
            if u.gap_lines is None:
                nxt = result[i + 1] if i + 1 < len(result) else None
                u.gap_lines = [] if (nxt is not None and nxt.marker == u.marker) else [""]
                if i > 0 and result[i - 1].marker == u.marker and result[i - 1].gap_lines == [""]:
                    result[i - 1].gap_lines = []  # cluster with a same-marker predecessor
        if result:
            result[-1].gap_lines = trailing or [""]
        self._units = result
        self.dirty = True


@dataclass
class Lexicon:
    header: str  # everything before the first \lx (the \_sh MDF header, etc.)
    entries: list[Entry]
    has_bom: bool = True

    def to_text(self) -> str:
        return self.header + "".join(e.current_text() for e in self.entries)

    def to_bytes(self) -> bytes:
        body = self.to_text().encode("utf-8")
        return (BOM_BYTES if self.has_bom else b"") + body


def loads(text: str, has_bom: bool = True) -> Lexicon:
    starts = [m.start() for m in _LX_RE.finditer(text)]
    if not starts:
        return Lexicon(header=text, entries=[], has_bom=has_bom)
    header = text[: starts[0]]
    entries: list[Entry] = []
    for i, start in enumerate(starts):
        end = starts[i + 1] if i + 1 < len(starts) else len(text)
        entries.append(Entry(raw=text[start:end]))
    return Lexicon(header=header, entries=entries, has_bom=has_bom)


def read(path: str | Path) -> Lexicon:
    data = Path(path).read_bytes()
    has_bom = data.startswith(BOM_BYTES)
    if has_bom:
        data = data[len(BOM_BYTES):]
    return loads(data.decode("utf-8"), has_bom=has_bom)


def save(lex: Lexicon, path: str | Path, backup_dir: str | Path | None = None) -> Path | None:
    """Write the lexicon to ``path`` safely: optionally copy the current file
    into ``backup_dir`` (timestamped) first, then write to a temp file and
    atomically replace. Returns the backup path, if one was made."""
    path = Path(path)
    data = lex.to_bytes()
    made_backup: Path | None = None
    if backup_dir is not None and path.exists():
        backup_dir = Path(backup_dir)
        backup_dir.mkdir(parents=True, exist_ok=True)
        stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        made_backup = backup_dir / f"{path.name}.{stamp}.bak"
        shutil.copy2(path, made_backup)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)  # atomic on the same volume
    return made_backup
