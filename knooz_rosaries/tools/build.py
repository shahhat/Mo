"""Merge batch JSONs -> per-category payloads for the Google Sheets writes.
usage: python3 build.py CAT [start end]   -> prints JSON rows for A{start}:F{end} (1-based sheet rows, data starts at row 2)
"""
import json, glob, sys, re
from rows import codes, img
from checksum import cs
def load():
    d={}
    for f in sorted(glob.glob('desc/batch*.json')):
        for e in json.load(open(f)): d[e['code']]=e
    return d
def rows(cat):
    d=load(); out=[]
    for i,c in enumerate(codes(cat)):
        e=d[c]; hero=int(e.get('hero') or 1)
        try: f=img(c,hero)
        except KeyError: f=img(c,1); hero=1
        out.append([str(i+1), f, e['description'].strip(), c, "Rosary", (e.get('notes') or '').strip()])
    return out
if __name__=='__main__':
    cat=sys.argv[1]; r=rows(cat)
    if len(sys.argv)>3:
        s,e=int(sys.argv[2]),int(sys.argv[3]); r=r[s-2:e-1]
    mode=sys.argv[4] if len(sys.argv)>4 else 'rows'
    if mode=='cs':
        print([cs(re.search(r'id=([^&]+)',x[1]).group(1)) for x in r])
    else:
        print(json.dumps(r,ensure_ascii=False))
