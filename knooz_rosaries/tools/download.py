import json, os, subprocess, concurrent.futures as cf, re
inv=json.load(open('inventory.json'))
jobs=[]
for c in inv:
    for e in c['entries']:
        if e['kind']!='folder' or not e['files']: continue
        d=os.path.join('thumbs',c['prefix'],e['title']); os.makedirs(d,exist_ok=True)
        for f in e['files']:
            if f['title'].endswith('.mp4'): continue
            jobs.append((f['id'], os.path.join(d, re.sub(r'[^\w\-().]','_',f['title'])+'.jpg')))
def get(j):
    fid,path=j
    if os.path.exists(path) and os.path.getsize(path)>2000: return 'skip'
    for a in range(4):
        r=subprocess.run(['curl','-sS','-L','--max-time','60','-o',path,'-w','%{http_code}',f'https://lh3.googleusercontent.com/d/{fid}=w700'],capture_output=True,text=True)
        if r.stdout.strip()=='200' and os.path.getsize(path)>2000: return 'ok'
    return 'fail '+fid
with cf.ThreadPoolExecutor(16) as ex: res=list(ex.map(get,jobs))
from collections import Counter
print(len(jobs), Counter(r.split()[0] for r in res)); print([r for r in res if r.startswith('fail')][:20])
