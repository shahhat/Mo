"""Recursively crawl the rosaries root on Drive (public folder views) and fetch EXIF keys for every photo."""
import json, subprocess, re, html, io, os
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
S='/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/'
ROOT='1U47v5bhvoQIxKyRvOU5B-sPkYeAvJymR'; STAGING='14JQrbkoYfO7ke8VFJzoaNvUIeeG68pNI'
def ls(fid):
    s=subprocess.run(['curl','-sS',f'https://drive.google.com/embeddedfolderview?id={fid}'],capture_output=True,text=True).stdout
    ids=re.findall(r'id="entry-([^"]+)"',s); ts=[html.unescape(t) for t in re.findall(r'flip-entry-title">([^<]*)<',s)]
    out=[]
    for i,t in zip(ids,ts):
        folder = f'/drive/folders/{i}' in s or f'folders/{i}' in s
        out.append(dict(id=i,title=t,folder=folder))
    return out
files=[]; stack=[(ROOT,'')]
while stack:
    fid,path=stack.pop()
    for e in ls(fid):
        if e['id']==STAGING: continue
        p=path+'/'+e['title']
        if e['folder']: stack.append((e['id'],p))
        else: files.append(dict(id=e['id'],title=e['title'],path=p))
print('files found',len(files))
# EXIF cache from earlier rounds
cache={}
for fn in [S+'meta/meta.json',S+'ros3/meta.json']:
    for r in json.load(open(fn)):
        if r.get('dto'): cache[r['id']]=dict(dto=r['dto'],imgno=r.get('imgno'))
need=[f for f in files if f['id'] not in cache and re.search(r'(?i)\.(jpe?g|png)$|^ROS|^DSC|^jj|^cx|^DSD|copy',f['title']) and not f['title'].startswith('Knooz')]
print('need exif',len(need))
def one(f):
    b=subprocess.run(['curl','-sS','-L','-r','0-163839','--max-time','60',f"https://drive.usercontent.google.com/download?id={f['id']}&export=download"],capture_output=True).stdout
    r={}
    try:
        im=Image.open(io.BytesIO(b)); r['dto']=im.getexif().get_ifd(0x8769).get(36867)
    except Exception as e: r['err']=str(e)[:50]
    m=re.search(rb'aux:ImageNumber="(\d+)"',b); r['imgno']=int(m.group(1)) if m else None
    return f['id'],r
with ThreadPoolExecutor(16) as ex:
    for i,r in ex.map(one,need):
        if r.get('dto'): cache[i]=r
for f in files: f.update(cache.get(f['id'],{}))
json.dump(files,open(S+'local_cmp/drive_files.json','w'),ensure_ascii=False)
import collections
cats=collections.Counter(f['path'].split('/')[1] for f in files)
print(cats)
print('with exif',sum(1 for f in files if f.get('dto')),'without',[(f['path']) for f in files if not f.get('dto')][:20])
