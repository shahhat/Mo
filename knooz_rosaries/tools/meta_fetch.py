"""Fetch first 160KB of every photo, extract EXIF time, image number, model -> meta/meta.json"""
import json, re, io, subprocess, sys, os
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
W=os.path.dirname(os.path.abspath(__file__))
inv=json.load(open(W+'/inventory.json'))
jobs=[]
for f in inv:
    for e in f['entries']:
        if e['kind']=='folder':
            for x in e.get('files',[]): jobs.append(dict(cat=f['prefix'],piece=e['title'],id=x['id'],title=x['title']))
        else: jobs.append(dict(cat=f['prefix'],piece=None,id=e['id'],title=e['title']))
def one(j):
    try:
        b=subprocess.run(['curl','-sS','-L','-r','0-163839','--max-time','60',f"https://drive.usercontent.google.com/download?id={j['id']}&export=download"],capture_output=True).stdout
        r=dict(j)
        r['magic']=b[:4].hex()
        try:
            im=Image.open(io.BytesIO(b)); ex=im.getexif(); sub=ex.get_ifd(0x8769)
            r['dto']=sub.get(36867); r['subsec']=sub.get(37521); r['model']=ex.get(272); r['dt']=ex.get(306)
            r['w']=im.size[0]; r['h']=im.size[1]
        except Exception as e: r['err']=str(e)[:80]
        m=re.search(rb'aux:ImageNumber="(\d+)"',b); r['imgno']=int(m.group(1)) if m else None
        m=re.search(rb'xmpMM:OriginalDocumentID="([^"]+)"',b); r['odid']=m.group(1).decode() if m else None
        m=re.search(rb'crs:RawFileName="([^"]+)"',b); r['raw']=m.group(1).decode() if m else None
        return r
    except Exception as e:
        return dict(j,err=str(e))
with ThreadPoolExecutor(16) as ex: res=list(ex.map(one,jobs))
json.dump(res,open(os.path.join(W,'..','meta','meta.json'),'w'),ensure_ascii=False)
print(len(res), sum(1 for r in res if r.get('dto')), sum(1 for r in res if r.get('imgno')), sum(1 for r in res if r.get('err')))
