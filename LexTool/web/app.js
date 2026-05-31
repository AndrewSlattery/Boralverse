"use strict";

let ENTRIES = [];          // sorted summaries for the browse list
const BY_HW = new Map();   // headword -> id, for resolving \mn cross-references
let activeLetter = null;
let selectedId = null;
let searchSeq = 0;         // guards against out-of-order async search responses
let MARKERS = [];          // {marker, label} options for the "add field" menu
let CURRENT = null;        // the entry detail currently shown

const $ = (sel) => document.querySelector(sel);
const esc = (s) => (s || "").replace(/[&<>"]/g, (c) =>
  ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const lines = (s) => esc(s).replace(/\n/g, "<br>");

// For the A-Z bar: words starting with æ/œ/ï live under a/o/i.
const FOLD = { "æ": "a", "œ": "o", "ï": "i" };
function initial(hw) {
  const c = hw.toLowerCase().replace(/^['!=\- ]+/, "")[0] || "";
  return FOLD[c] || c;
}

async function boot() {
  const meta = await (await fetch("/api/meta")).json();
  $("#count").textContent = `${meta.count.toLocaleString()} entries`;
  MARKERS = meta.markers || [];
  buildAlpha(meta.alphabet);

  ENTRIES = await (await fetch("/api/entries")).json();
  for (const e of ENTRIES) if (!BY_HW.has(e.hw)) BY_HW.set(e.hw, e.id);

  let debounce;
  $("#search").addEventListener("input", () => {
    activeLetter = null;
    clearTimeout(debounce);
    debounce = setTimeout(update, 120);
  });
  $("#field").addEventListener("change", update);
  update();
}

function buildAlpha(alphabet) {
  const box = $("#alpha");
  for (const ch of alphabet) {
    const b = document.createElement("button");
    b.textContent = ch;
    b.onclick = () => {
      activeLetter = ch;
      $("#search").value = "";
      update();
    };
    box.appendChild(b);
  }
}

function update() {
  const q = $("#search").value.trim();
  if (q) return runSearch(q);
  const items = activeLetter
    ? ENTRIES.filter((e) => initial(e.hw) === activeLetter)
    : ENTRIES;
  renderList(items, activeLetter
    ? `${items.length} under “${activeLetter}”`
    : `${items.length} entries`);
}

async function runSearch(q) {
  const seq = ++searchSeq;
  const field = $("#field").value;
  const items = await (await fetch(
    `/api/search?field=${encodeURIComponent(field)}&q=${encodeURIComponent(q)}`)).json();
  if (seq !== searchSeq) return;  // a newer query already fired
  const where = $("#field").selectedOptions[0].textContent.toLowerCase();
  renderList(items, `${items.length} match${items.length === 1 ? "" : "es"} in ${where}`);
}

function renderList(items, label) {
  $("#results").textContent = label;
  const ul = $("#list");
  ul.innerHTML = "";
  const frag = document.createDocumentFragment();
  for (const e of items) {
    const li = document.createElement("li");
    li.dataset.id = e.id;
    if (e.id === selectedId) li.className = "sel";
    li.innerHTML = rowHtml(e);
    li.onclick = () => open(e.id);
    frag.appendChild(li);
  }
  ul.appendChild(frag);
}

function rowHtml(e) {
  const sub = e.snippet !== undefined
    ? `<span class="ge"><b class="mk">\\${esc(e.marker)}</b> ${esc(e.snippet)}</span>`
    : (e.ge ? `<span class="ge">${esc(e.ge)}</span>` : "");
  return `<span class="hw">${esc(e.hw)}</span>` +
    (e.hm ? `<span class="hm">${esc(e.hm)}</span>` : "") +
    (e.ps ? `<span class="ps">${esc(e.ps)}</span>` : "") + sub;
}

function markSel(id) {
  document.querySelectorAll("#list li").forEach((li) =>
    li.classList.toggle("sel", Number(li.dataset.id) === id));
}

function wireXrefs() {
  $("#entry").querySelectorAll("[data-go]").forEach((a) =>
    a.onclick = () => open(Number(a.dataset.go)));
}

async function open(id) {
  selectedId = id;
  markSel(id);
  const data = await (await fetch(`/api/entry/${id}`)).json();
  CURRENT = data;
  $("#entry").innerHTML =
    `<div class="toolbar"><button id="editBtn">Edit</button></div>` + renderEntry(data.fields);
  $("#editBtn").onclick = () => editEntry(id);
  wireXrefs();
  $("#entry").scrollTop = 0;
}

// --- Editing ---------------------------------------------------------------
const LONG = new Set(["et", "de", "dv", "xv", "xe", "ue", "uv"]);  // get a textarea

function fieldInput(marker, value) {
  if (LONG.has(marker) || value.includes("\n")) {
    const rows = Math.min(8, value.split("\n").length + 1);
    return `<textarea class="fval" rows="${rows}">${esc(value)}</textarea>`;
  }
  return `<input class="fval" type="text" value="${esc(value)}">`;
}

function rowEl(f) {
  const div = document.createElement("div");
  div.className = "frow";
  div.dataset.idx = f.idx ?? "";          // "" marks a brand-new field
  div.innerHTML =
    `<span class="fmk">\\${esc(f.marker)}</span>` +
    fieldInput(f.marker, f.value || "") +
    `<button class="fdel" title="Remove this field">×</button>`;
  div.querySelector(".fdel").onclick = () => div.remove();
  return div;
}

function editEntry(id) {
  $("#entry").innerHTML =
    `<div class="toolbar">
       <button id="saveBtn">Save</button>
       <button id="cancelBtn" class="ghost">Cancel</button>
       <span id="saveMsg" class="muted"></span>
     </div>
     <div id="rows"></div>
     <div class="addrow"><select id="newMarker"></select><button id="addFieldBtn">+ Add field</button></div>`;
  const rows = $("#rows");
  for (const f of CURRENT.fields) rows.appendChild(rowEl(f));
  const sel = $("#newMarker");
  for (const m of MARKERS)
    sel.insertAdjacentHTML("beforeend", `<option value="${m.marker}">\\${m.marker} — ${esc(m.label)}</option>`);
  $("#addFieldBtn").onclick = () => {
    rows.appendChild(rowEl({ marker: sel.value, value: "" }));
    rows.lastElementChild.querySelector(".fval").focus();
  };
  $("#cancelBtn").onclick = () => open(id);
  $("#saveBtn").onclick = () => saveEntry(id);
}

async function saveEntry(id) {
  const items = [...document.querySelectorAll("#rows .frow")].map((d) => ({
    srcIndex: d.dataset.idx === "" ? null : Number(d.dataset.idx),
    marker: d.querySelector(".fmk").textContent.slice(1),
    value: d.querySelector(".fval").value,
  }));
  const msg = $("#saveMsg");
  msg.textContent = "Saving…";
  const res = await fetch(`/api/entry/${id}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ fields: items }),
  });
  if (!res.ok) {
    const e = await res.json().catch(() => ({}));
    msg.textContent = "Error: " + (e.error || res.status);
    return;
  }
  CURRENT = await res.json();
  ENTRIES = await (await fetch("/api/entries")).json();   // gloss/headword may have changed
  BY_HW.clear();
  for (const e of ENTRIES) if (!BY_HW.has(e.hw)) BY_HW.set(e.hw, e.id);
  update();
  open(id);
}

// Split a flat field list into the main segment plus any \se subentries.
function segments(fields) {
  const segs = [];
  let cur = [];
  for (const f of fields) {
    if (f.marker === "se") { if (cur.length) segs.push(cur); cur = [f]; }
    else cur.push(f);
  }
  if (cur.length) segs.push(cur);
  return segs;
}

function renderEntry(fields) {
  return segments(fields)
    .map((seg, i) => renderSegment(seg, i > 0 || seg[0].marker === "se"))
    .join("");
}

const KNOWN = new Set(["lx", "se", "hm", "ps", "ge", "de", "dv", "xv", "xe", "et", "mn", "sd", "ue", "uv"]);
const LABELS = { sd: "Semantic domain", ue: "Usage", uv: "Usage (Borlish)", de: "Definition", dv: "Definition (Borlish)" };

function renderSegment(seg, isSub) {
  const g = {};
  for (const f of seg) (g[f.marker] ||= []).push(f.value);
  const hw = (isSub ? g.se : g.lx)?.[0] || "";
  let h = isSub ? '<div class="subentry">' : "";

  h += `<h2 class="entry-hw">${esc(hw)}` +
    (g.hm ? `<span class="hm">${esc(g.hm[0])}</span>` : "") + `</h2>`;
  if (g.ps) h += `<p class="entry-ps">${esc(g.ps.join(", "))}</p>`;

  if (g.ge) {
    h += g.ge.length > 1
      ? `<ol class="senses">${g.ge.map((x) => `<li>${esc(x)}</li>`).join("")}</ol>`
      : `<p class="senses">${esc(g.ge[0])}</p>`;
  }
  for (const m of ["de", "dv"]) if (g[m])
    h += `<div class="block"><div class="label">${LABELS[m]}</div>${lines(g[m].join(" / "))}</div>`;

  const xv = g.xv || [], xe = g.xe || [];
  for (let i = 0; i < Math.max(xv.length, xe.length); i++) {
    h += `<div class="example">` +
      (xv[i] ? `<div class="xv">${esc(xv[i])}</div>` : "") +
      (xe[i] ? `<div class="xe">${esc(xe[i])}</div>` : "") + `</div>`;
  }

  for (const m of ["ue", "uv", "sd"]) if (g[m])
    h += `<div class="block"><div class="label">${LABELS[m]}</div>${esc(g[m].join("; "))}</div>`;

  if (g.et) h += `<div class="block etym"><div class="label">Etymology</div>${lines(g.et.join("\n"))}</div>`;

  if (g.mn) {
    const links = g.mn.map((v) => BY_HW.has(v)
      ? `<a data-go="${BY_HW.get(v)}">${esc(v)}</a>` : esc(v)).join(", ");
    h += `<div class="block xref"><div class="label">See</div>${links}</div>`;
  }

  for (const m of Object.keys(g)) if (!KNOWN.has(m))
    h += `<div class="block generic"><div class="label">\\${esc(m)}</div>${lines(g[m].join("; "))}</div>`;

  if (isSub) h += "</div>";
  return h;
}

boot();
