import json, re, io, subprocess, os
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
t=json.load(open('tree.json'))
jobs=[x for x in t if not x['dir'] and x['path'].lower().endswith(('.jpg','.jpeg','.png'))]
def one(j):
    r=dict(id=j['id'],path=j['path'])
    try:
        b=subprocess.run(['curl','-sS','-L','-r','0-163839','--max-time','90',f"https://drive.usercontent.google.com/download?id={j['id']}&export=download"],capture_output=True).stdout
        try:
            im=Image.open(io.BytesIO(b)); ex=im.getexif(); sub=ex.get_ifd(0x8769)
            r['dto']=sub.get(36867); r['subsec']=sub.get(37521); r['model']=ex.get(272); r['w']=im.size[0]; r['h']=im.size[1]
        except Exception as e: r['err']=str(e)[:60]
        m=re.search(rb'aux:ImageNumber="(\d+)"',b); r['imgno']=int(m.group(1)) if m else None
        m=re.search(rb'crs:RawFileName="([^"]+)"',b); r['raw']=m.group(1).decode() if m else None
        m=re.search(rb'xmpMM:OriginalDocumentID="([^"]+)"',b); r['odid']=m.group(1).decode() if m else None
    except Exception as e: r['err']=str(e)[:60]
    # thumbnail
    p=f"th/{j['id']}.jpg"
    if not os.path.exists(p) or os.path.getsize(p)<1000:
        subprocess.run(['curl','-sS','-L','-o',p,f"https://lh3.googleusercontent.com/d/{j['id']}=w400"])
    return r
with ThreadPoolExecutor(16) as ex: res=list(ex.map(one,jobs))
json.dump(res,open('meta.json','w'),ensure_ascii=False,indent=0)
print(len(res),'dto',sum(1 for r in res if r.get('dto')),'imgno',sum(1 for r in res if r.get('imgno')),'raw',sum(1 for r in res if r.get('raw')),'err',sum(1 for r in res if r.get('err')))
