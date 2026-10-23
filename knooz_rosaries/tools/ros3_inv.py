import json, subprocess, re, html
from concurrent.futures import ThreadPoolExecutor
ROOT='16sGXBEoaSm1NtyyGsAaaIvM9iGaQvHQF'
def ls(fid):
    s=subprocess.run(['curl','-sS',f'https://drive.google.com/embeddedfolderview?id={fid}'],capture_output=True,text=True).stdout
    ids=re.findall(r'id="entry-([^"]+)"',s); ts=[html.unescape(t) for t in re.findall(r'flip-entry-title">([^<]*)<',s)]
    hrefs=re.findall(r'<a href="([^"]+)" target="_blank"><div class="flip-entry-info"',s) or re.findall(r'<a href="([^"]+)"',s)
    out=[]
    for i,t in zip(ids,ts):
        h=[x for x in hrefs if i in x]
        kind='folder' if (h and '/folders/' in h[0]) else 'file'
        out.append(dict(id=i,title=t,kind=kind))
    return out
top=ls(ROOT)
folders=[e for e in top if re.fullmatch(r'ROS-\d{3}',e['title'])]
with ThreadPoolExecutor(12) as ex: subs=list(ex.map(lambda e:ls(e['id']),folders))
for e,s in zip(folders,subs): e['kind']='folder'; e['files']=s
loose=[e for e in top if e not in folders and not e['title'].startswith('Knooz')]
inv=dict(folders=folders,loose=loose)
json.dump(inv,open('ros3/inv.json','w'),ensure_ascii=False,indent=0)
old=json.load(open('work/inventory.json')); OF={e['title']:e for f in old if f['prefix']=='ROS' for e in f['entries']}
for e in folders:
    o=OF.get(e['title']); oldn=len(o['files']) if o else 0
    print(e['title'], 'photos',len(e['files']), 'was',oldn, [x['title'] for x in e['files']][:3], '...' if len(e['files'])>3 else '')
print('loose',len(loose))
