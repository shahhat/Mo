#!/usr/bin/env python3
"""Build a deploy-ready copy of the Kunooz digital catalog with a category's pieces filled in.

usage: build.py WORK_DIR OUT_DIR [--base https://kunooz-catalog.vercel.app]

WORK_DIR is what fetch.py produced (inventory.json, src/, sheet.csv).
Reads selection.json (images per piece, by Drive file id, in display order) and meta_ros_k.json (catalog text).
OUT_DIR receives a full mirror of the live site with the new/updated pieces:
  index.html, qrcode.min.js, data.js, vercel.json, img/*, film/*
Images follow the live catalog's format: long side 1500 px, JPEG q84 progressive 4:2:0, no metadata;
thumbnail <code>-t.jpg = centre square of the first image, 720x720, q82.
"""
import sys, os, json, re, csv, hashlib, subprocess, urllib.request, argparse

ap = argparse.ArgumentParser()
ap.add_argument("work"); ap.add_argument("out")
ap.add_argument("--base", default="https://kunooz-catalog.vercel.app")
ap.add_argument("--meta", default=os.path.join(os.path.dirname(__file__), "meta_ros_k.json"))
ap.add_argument("--selection", default=os.path.join(os.path.dirname(__file__), "selection.json"))
ap.add_argument("--cat", default="k"); ap.add_argument("--name", default="مسباح كهرب شفاف")
a = ap.parse_args()
HERE = os.path.dirname(os.path.abspath(__file__))
PENDING = ["عدد الخرز", "قطر الخرزة", "الوزن", "المنشأ"]

def get(url):
    for i in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=120) as r:
                return r.read()
        except Exception:
            if i == 4: raise
def sh(*cmd): subprocess.run(cmd, check=True)
def size(p): return [int(x) for x in subprocess.run(["identify", "-format", "%w %h", p], capture_output=True, text=True, check=True).stdout.split()]

warn = []
os.makedirs(f"{a.out}/img", exist_ok=True); os.makedirs(f"{a.out}/film", exist_ok=True)

# 1. mirror the live site
for f in ["index.html", "qrcode.min.js", "data.js", "img/logo.png"]:
    open(f"{a.out}/{f}", "wb").write(get(f"{a.base}/{f}"))
# every url(...) / src= / href= asset the page itself references (fonts, logo, scripts)
page = open(f"{a.out}/index.html", encoding="utf-8").read()
for ref in sorted(set(re.findall(r"""url\(["']?([^)"'#]+)""", page))):
    if ref.startswith(("http", "data:")): continue
    os.makedirs(os.path.dirname(f"{a.out}/{ref}") or a.out, exist_ok=True)
    open(f"{a.out}/{ref}", "wb").write(get(f"{a.base}/{ref}"))
js = open(f"{a.out}/data.js", encoding="utf-8").read()
C = json.loads(js[js.index("{"): js.rindex("}") + 1])

inv = json.load(open(f"{a.work}/inventory.json"))
where = {f["id"]: (code, f) for code, d in inv.items() for f in d["files"]}
sel = json.load(open(a.selection)); meta = json.load(open(a.meta))

# 2. sheet change check (catalog text was written from the snapshot)
snap_p = os.path.join(HERE, "sheet_snapshot_" + os.path.basename(a.meta).replace("meta_", "").replace(".json", ".csv"))
def rows(p):
    r = list(csv.reader(open(p, encoding="utf-8")))
    return {row[3].strip(): row[2].strip() for row in r[1:] if len(row) > 3 and row[3].strip()}
cur = rows(f"{a.work}/sheet.csv")
if os.path.exists(snap_p):
    old = rows(snap_p)
    for code in sorted(set(cur) | set(old)):
        if cur.get(code) != old.get(code): warn.append(f"{code}: sheet description changed since the catalog text was written")
else:
    open(snap_p, "w", encoding="utf-8").write(open(f"{a.work}/sheet.csv", encoding="utf-8").read())

# 3. images + entries
new = {}
for code in sorted(meta):
    if code.startswith("_"): continue
    picks = sel.get(code) or []
    imgs = []
    for k, pk in enumerate(picks, 1):
        if pk["id"] not in where:
            warn.append(f"{code}: picked photo {pk['was']} ({pk['id']}) is no longer in the Drive folders - skipped"); continue
        fcode, f = where[pk["id"]]
        if fcode != code: warn.append(f"{code}: picked photo {pk['was']} now sits in {fcode} as {f['title']}")
        src = f"{a.work}/src/{fcode}/{f['n']}.jpg"
        dst = f"img/{code}-{len(imgs) + 1}.jpg"
        sh("convert", src, "-auto-orient", "-resize", "1500x1500>", "-strip", "-interlace", "JPEG",
           "-sampling-factor", "2x2,1x1,1x1", "-quality", "84", f"{a.out}/{dst}")
        w, h = size(f"{a.out}/{dst}")
        imgs.append({"src": dst, "w": w, "h": h})
    if not imgs:
        warn.append(f"{code}: no images - left out"); continue
    thumb = f"img/{code}-t.jpg"
    sh("convert", f"{a.out}/{imgs[0]['src']}", "-gravity", "center", "-extent",
       "%dx%d" % ((min(imgs[0]["w"], imgs[0]["h"]),) * 2), "-resize", "720x720", "-strip", "-interlace", "JPEG",
       "-sampling-factor", "2x2,1x1,1x1", "-quality", "82", f"{a.out}/{thumb}")
    mean = float(subprocess.run(["identify", "-format", "%[fx:mean]", f"{a.out}/{thumb}"], capture_output=True, text=True).stdout)
    m = meta[code]
    known = {k for k, _ in m["specs"]}
    new[code] = {"code": code, "cat": a.cat, "name": m.get("name", a.name), "lead": m["lead"], "thumb": thumb,
                 "light": mean > 0.5, "imgs": imgs, "film": None,
                 "specs": [{"k": k, "v": v} for k, v in m["specs"]],
                 "pending": [p for p in PENDING if p not in known]}

# 4. merge into data.js: replace existing entries in place, keep entries with a film untouched,
#    insert the remaining new codes in code order at the position of the first replaced/related entry
pieces = C["pieces"]; out_list = []; inserted = False
prefix = re.compile(r"^" + re.escape(next(c["prefix"] for c in C["cats"] if c["id"] == a.cat)) + r"-\d{3}$")
for p in pieces:
    if p["code"] in new and p.get("film"):
        warn.append(f"{p['code']}: live entry has a film - kept as is"); new.pop(p["code"]); out_list.append(p); continue
    if prefix.match(p["code"]) and not p.get("film"):
        if not inserted:
            out_list.extend(new[c] for c in sorted(new)); inserted = True
        if p["code"] not in new: out_list.append(p)
        continue
    out_list.append(p)
if not inserted: out_list.extend(new[c] for c in sorted(new))
C["pieces"] = out_list

# 5. mirror every other asset the catalog references
for p in out_list:
    if p["code"] in new: continue
    for path in [p["thumb"]] + [i["src"] for i in p["imgs"]] + ([p["film"]["src"], p["film"]["poster"]] if p.get("film") else []):
        dst = f"{a.out}/{path}"
        if not os.path.exists(dst):
            os.makedirs(os.path.dirname(dst), exist_ok=True); open(dst, "wb").write(get(f"{a.base}/{path}"))

open(f"{a.out}/data.js", "w", encoding="utf-8").write("window.CATALOG = " + json.dumps(C, ensure_ascii=False, indent=1) + ";\n")
json.dump({"redirects": [{"source": "/k/:code", "destination": "/#/p/:code", "permanent": False}]},
          open(f"{a.out}/vercel.json", "w"), indent=1)

print(f"pieces in catalog: {len(out_list)}  built/updated: {len(new)}")
for c in sorted(new): print(f"  {c}: {len(new[c]['imgs'])} images, light={new[c]['light']}")
for w in warn: print("WARNING:", w)
