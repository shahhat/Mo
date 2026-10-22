import json, subprocess, re, html, copy
from concurrent.futures import ThreadPoolExecutor
inv=json.load(open('work/inventory.json')); ops=json.load(open('ops/ops.json'))
ANTIQ='1n0OsStlvIFnPlK6T--Gnp-drLT017uwh'
# expected: parent_id -> {child_id: title}
title={}; parent={}
for f in inv:
    for e in f['entries']:
        title[e['id']]=e['title']; parent[e['id']]=f['folder_id']
        for x in e.get('files',[]): title[x['id']]=x['title']; parent[x['id']]=e['id']
for o in ops:
    if 'title' in o: title[o['fileId']]=o['title']
    if 'parentId' in o: parent[o['fileId']]=o['parentId']
exp={}
for i,p in parent.items(): exp.setdefault(p,{})[i]=title[i]
def live(fid):
    s=subprocess.run(['curl','-sS',f'https://drive.google.com/embeddedfolderview?id={fid}'],capture_output=True,text=True).stdout
    ids=re.findall(r'id="entry-([^"]+)"',s); ts=[html.unescape(t) for t in re.findall(r'flip-entry-title">([^<]*)<',s)]
    return fid,dict(zip(ids,ts))
check=[p for p in exp if p!=ANTIQ]+[ANTIQ]
with ThreadPoolExecutor(16) as ex: L=dict(ex.map(live,check))
bad=0
for p in check:
    e=exp.get(p,{}); l={k:v for k,v in L[p].items() if not v.startswith('Knooz (Desc._) Sheet')}
    if e!=l:
        bad+=1
        miss={k:v for k,v in e.items() if l.get(k)!=v}; extra={k:v for k,v in l.items() if e.get(k)!=v}
        print('MISMATCH folder',p,title.get(p),'| expected-not-live:',list(miss.values())[:5],'| live-not-expected:',list(extra.values())[:5])
print('folders checked',len(check),'mismatches',bad, 'items expected',sum(len(v) for v in exp.values()))
