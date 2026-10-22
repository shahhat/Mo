#!/usr/bin/env python3
"""Inventory + download a Kunooz Drive category folder (link-shared, no auth needed).
usage: fetch.py ROOT_FOLDER_ID PREFIX WORK_DIR [SHEET_ID]
Writes WORK_DIR/inventory.json  {code: {"folder": id, "files": [{"n":int,"title":str,"id":str}]}}
and downloads originals to WORK_DIR/src/<code>/<n>.jpg (cached by Drive id)."""
import sys, re, os, json, html, urllib.request, concurrent.futures as cf
root, prefix, work = sys.argv[1:4]; sheet = sys.argv[4] if len(sys.argv) > 4 else None
def get(url, tries=6):
    import time
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=180) as r:
                return r.read()
        except Exception as e:
            if i == tries - 1: raise
            time.sleep(2 ** i)
def listing(fid):
    h = get(f"https://drive.google.com/embeddedfolderview?id={fid}").decode("utf-8", "replace")
    out = []
    for m in re.finditer(r'<a href="([^"]+)"[^>]*>.*?flip-entry-title">([^<]+)<', h, re.S):
        href, title = html.unescape(m.group(1)), html.unescape(m.group(2)).strip()
        fm = re.search(r'/folders/([\w-]+)', href) ; dm = re.search(r'/file/d/([\w-]+)', href)
        if fm: out.append(("folder", title, fm.group(1)))
        elif dm: out.append(("file", title, dm.group(1)))
    return out
inv = {}
for kind, title, fid in listing(root):
    if kind == "folder" and re.fullmatch(re.escape(prefix) + r"-\d{3}", title):
        files = []
        for k2, t2, id2 in listing(fid):
            if k2 != "file": continue
            m = re.fullmatch(re.escape(title) + r"-(\d+)", t2)
            files.append({"n": int(m.group(1)) if m else None, "title": t2, "id": id2})
        files.sort(key=lambda f: (f["n"] is None, f["n"] or 0, f["title"]))
        inv[title] = {"folder": fid, "files": files}
os.makedirs(work, exist_ok=True)
json.dump(dict(sorted(inv.items())), open(f"{work}/inventory.json", "w"), ensure_ascii=False, indent=1)
jobs = []
for code, d in inv.items():
    os.makedirs(f"{work}/src/{code}", exist_ok=True)
    for f in d["files"]:
        if f["n"] is None: continue
        p = f"{work}/src/{code}/{f['n']}.jpg"; tag = p + ".id"
        if os.path.exists(p) and os.path.exists(tag) and open(tag).read() == f["id"]: continue
        jobs.append((f["id"], p, tag))
def dl(j):
    fid, p, tag = j
    data = get(f"https://drive.usercontent.google.com/download?id={fid}&export=download")
    open(p, "wb").write(data); open(tag, "w").write(fid); return p, len(data)
with cf.ThreadPoolExecutor(4) as ex:
    for p, n in ex.map(dl, jobs): print("got", p, n)
if sheet:
    open(f"{work}/sheet.csv", "wb").write(get(f"https://docs.google.com/spreadsheets/d/{sheet}/export?format=csv"))
for code, d in sorted(inv.items()):
    odd = [f["title"] for f in d["files"] if f["n"] is None]
    print(code, len(d["files"]), "files", ("UNNUMBERED: " + ", ".join(odd)) if odd else "")
