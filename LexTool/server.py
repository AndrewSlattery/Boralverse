"""LexTool - a local, stdlib-only web app for browsing a Lexique Pro .db lexicon.

Run it (or double-click run.bat):

    py server.py

It loads the .db, serves a browser UI at http://127.0.0.1:8765/, and opens
your browser. Editing writes back to the .db through sfm.save(), which makes a
timestamped backup on the first write of each session and swaps atomically.

Stdlib only - nothing to install.
"""

from __future__ import annotations

import json
import os
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import sfm

# --- Configuration (edit these to point at a different database) -------------
DEFAULT_DB = r"C:\Users\awsla\Documents\GitHub\Boralverse\Borlish\Lexique Pro\Data\Borlish.db"
DB_PATH = Path(os.environ.get("LEXTOOL_DB", DEFAULT_DB))  # env override aids testing
WEB_DIR = Path(__file__).parent / "web"
BACKUP_DIR = Path(__file__).parent / "backups"
HOST = "127.0.0.1"
PORT = 8765

# Markers offered in the editor's "add field" menu, with human labels.
MARKERS = [
    ("lx", "Headword"), ("hm", "Homonym #"), ("ps", "Part of speech"),
    ("ge", "Gloss"), ("de", "Definition (En)"), ("dv", "Definition (Bor)"),
    ("xv", "Example (Bor)"), ("xe", "Example translation"),
    ("et", "Etymology"), ("mn", "Cross-ref (\\mn)"), ("se", "Subentry"),
    ("sd", "Semantic domain"), ("ue", "Usage (En)"), ("uv", "Usage (Bor)"),
]

_backed_up = False  # becomes True once the first save of the session has backed up
_write_lock = threading.Lock()

# Display alphabet for the A-Z bar, from Borlish.lpConfig.
ALPHABET = "a b c ç d ð e f g h i j k l m n o p q r s t u v x y z".split()
# Collation order: æ folds in right after a, œ right after o, ï counts as i.
# '-' '=' apostrophe and '!' are punctuation (ignored); spaces are significant
# and sort before any letter.
_ORDER = "a æ b c ç d ð e f g h i j k l m n o œ p q r s t u v x y z".split()
RANK = {ch: i for i, ch in enumerate(_ORDER)}
RANK["ï"] = RANK["i"]
IGNORE = set("-='!")


def sort_key(headword: str):
    key: list[int] = []
    for ch in headword.casefold():
        if ch in IGNORE:
            continue
        key.append(-1 if ch == " " else RANK.get(ch, 999))
    return (key, headword.casefold())  # secondary key keeps ties deterministic


# --- Data (LEX / INDEX / SORTED are (re)built by load()) ---------------------
LEX: sfm.Lexicon | None = None
INDEX: list[dict] = []
SORTED: list[int] = []


def summary(idx: int, e: sfm.Entry) -> dict:
    return {
        "id": idx,  # stable index into the file (sort order is separate)
        "hw": e.headword,
        "hm": e.get("hm"),
        "ps": "; ".join(e.all("ps")),
        "ge": "; ".join(e.all("ge")[:5]),
    }


def load() -> None:
    """(Re)read the .db from disk and rebuild the browse index and sort order."""
    global LEX, INDEX, SORTED
    LEX = sfm.read(DB_PATH)
    SORTED = sorted(range(len(LEX.entries)), key=lambda i: sort_key(LEX.entries[i].headword))
    INDEX = [summary(i, LEX.entries[i]) for i in SORTED]


load()


def detail(idx: int) -> dict:
    e = LEX.entries[idx]
    return {
        "id": idx,
        "hw": e.headword,
        "fields": [{"idx": k, "marker": u.marker, "value": u.value} for k, u in enumerate(e.units)],
    }


# Which markers each search scope looks in. None means "every field".
SEARCH_FIELDS = {
    "lx": ("lx",),
    "ge": ("ge",),
    "ps": ("ps",),
    "et": ("et",),
    "xv": ("xv", "xe"),
    "all": None,
}


def _snippet(text: str, q: str, before: int = 30, after: int = 60) -> str:
    pos = text.casefold().find(q.casefold())
    if pos < 0:
        return text[: before + after].replace("\n", " ")
    start, end = max(0, pos - before), min(len(text), pos + len(q) + after)
    s = text[start:end].replace("\n", " ")
    return ("…" if start else "") + s + ("…" if end < len(text) else "")


def search(field: str, q: str) -> list[dict]:
    ql = q.casefold()
    markers = SEARCH_FIELDS.get(field, (field,))
    results = []
    for i in SORTED:  # SORTED is already in collation order
        e = LEX.entries[i]
        fields = e.fields if markers is None else [f for f in e.fields if f.marker in markers]
        hit = next((f for f in fields if ql in f.value.casefold()), None)
        if hit:
            s = summary(i, e)
            s["marker"] = hit.marker
            s["snippet"] = _snippet(hit.value, q)
            results.append(s)
    return results


# --- HTTP --------------------------------------------------------------------
CONTENT_TYPES = {
    ".html": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "application/javascript; charset=utf-8",
}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):  # quiet console
        pass

    def _send(self, body: bytes, content_type: str, status: int = 200):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _json(self, obj, status: int = 200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self._send(body, "application/json; charset=utf-8", status)

    def do_GET(self):
        path = self.path.split("?", 1)[0]

        if path == "/api/meta":
            return self._json({
                "count": len(LEX.entries), "alphabet": ALPHABET, "db": str(DB_PATH),
                "markers": [{"marker": m, "label": label} for m, label in MARKERS],
            })
        if path == "/api/entries":
            return self._json(INDEX)
        if path == "/api/search":
            qs = parse_qs(urlparse(self.path).query)
            q = qs.get("q", [""])[0]
            field = qs.get("field", ["lx"])[0]
            return self._json(search(field, q) if q.strip() else [])
        if path.startswith("/api/entry/"):
            try:
                idx = int(path.rsplit("/", 1)[1])
                return self._json(detail(idx))
            except (ValueError, IndexError):
                return self._json({"error": "no such entry"}, 404)

        # Static files from WEB_DIR (with path-traversal protection).
        rel = "index.html" if path == "/" else path.lstrip("/")
        target = (WEB_DIR / rel).resolve()
        if not target.is_relative_to(WEB_DIR.resolve()) or not target.is_file():
            return self._send(b"Not found", "text/plain; charset=utf-8", 404)
        ctype = CONTENT_TYPES.get(target.suffix, "application/octet-stream")
        self._send(target.read_bytes(), ctype)

    def do_POST(self):
        path = self.path.split("?", 1)[0]
        if not path.startswith("/api/entry/"):
            return self._json({"error": "not found"}, 404)
        try:
            idx = int(path.rsplit("/", 1)[1])
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length).decode("utf-8"))
            fields = body["fields"]
            assert isinstance(fields, list)
        except (ValueError, KeyError, AssertionError, json.JSONDecodeError) as e:
            return self._json({"error": f"bad request: {e}"}, 400)
        if not (0 <= idx < len(LEX.entries)):
            return self._json({"error": "no such entry"}, 404)
        if not any(f.get("marker") == "lx" and str(f.get("value", "")).strip() for f in fields):
            return self._json({"error": "entry must keep a non-empty \\lx headword"}, 400)

        global _backed_up
        with _write_lock:
            LEX.entries[idx].apply_fields(fields)
            bak = sfm.save(LEX, DB_PATH, backup_dir=None if _backed_up else BACKUP_DIR)
            if bak:
                _backed_up = True
                print(f"Backup written: {bak}")
            load()  # refresh in-memory copy + indexes from what we just wrote
            result = detail(idx)
        return self._json(result)


def main():
    open_browser = "--no-browser" not in sys.argv
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    url = f"http://{HOST}:{PORT}/"
    print(f"LexTool serving {len(LEX.entries)} entries at {url}")
    print(f"Database: {DB_PATH}")
    print(f"Backups : {BACKUP_DIR} (made on first edit)")
    print("Press Ctrl+C to stop.")
    if open_browser:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
        server.shutdown()


if __name__ == "__main__":
    main()
