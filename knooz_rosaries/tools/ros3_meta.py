import json, re, io, subprocess, os
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
S='/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/ros3/'
inv=json.load(open(S+'inv.json'))
jobs=[]
for e in inv['folders']:
    for x in e['files']: jobs.append(dict(piece=e['title'],id=x['id'],title=x['title']))
for x in inv['loose']: jobs.append(dict(piece=None,id=x['id'],title=x['title']))
os.makedirs(S+'thumbs',exist_ok=True)
def one(j):
    r=dict(j)
    b=subprocess.run(['curl','-sS','-L','-r','0-163839','--max-time','60',f"https://drive.usercontent.google.com/download?id={j['id']}&export=download"],capture_output=True).stdout
    try:
        im=Image.open(io.BytesIO(b)); ex=im.getexif(); sub=ex.get_ifd(0x8769)
        r['dto']=sub.get(36867); r['model']=ex.get(272)
    except Exception as e: r['err']=str(e)[:60]
    m=re.search(rb'aux:ImageNumber="(\d+)"',b); r['imgno']=int(m.group(1)) if m else None
    fn=S+'thumbs/'+j['id']+'.jpg'
    if not os.path.exists(fn): subprocess.run(['curl','-sS','-L','-o',fn,f"https://lh3.googleusercontent.com/d/{j['id']}=w700"])
    return r
with ThreadPoolExecutor(16) as ex: res=list(ex.map(one,jobs))
json.dump(res,open(S+'meta.json','w'),ensure_ascii=False)
print(len(res), 'dto',sum(1 for r in res if r.get('dto')), 'imgno',sum(1 for r in res if r.get('imgno')), 'err',[(r['title'],r['err']) for r in res if r.get('err')])
