# 2000x2000 like the owner's ring examples; logo bottom-left (~12% height); JPEG <= 730 KB; honest EXIF.
import cv2,numpy as np,json,os,io
from PIL import Image
S=2000; log=json.load(open('/tmp/kw/jcrops/log.json')); sel=json.load(open('/tmp/kw/jsel.json'))
L=cv2.imread('/tmp/kw/logo_raw.png').astype(np.float32)
lh=int(S*0.12); lw=int(L.shape[1]*lh/L.shape[0]); L=cv2.resize(L,(lw,lh),interpolation=cv2.INTER_AREA)
A=np.clip((L.max(axis=2,keepdims=True)-18)/55,0,1); QS={}
os.makedirs('/tmp/kw/jfinal',exist_ok=True)
for code,shots in sel.items():
    os.makedirs(f'/tmp/kw/jfinal/{code}',exist_ok=True)
    for k in range(1,len(shots)+1):
        src=f'/tmp/kw/jsr/{code}_{k}.png'
        if not os.path.exists(src): continue
        im=cv2.imread(src); im=cv2.resize(im,(S,S),interpolation=cv2.INTER_AREA if im.shape[0]>S else cv2.INTER_LANCZOS4)
        bl=cv2.GaussianBlur(im,(0,0),1.5); im=cv2.addWeighted(im,1.2,bl,-0.2,0)
        x0=int(S*0.045); y0=S-int(S*0.015)-lh; roi=im[y0:y0+lh,x0:x0+lw].astype(np.float32)
        im[y0:y0+lh,x0:x0+lw]=(roi*(1-A)+L*A).astype(np.uint8)
        e=log[f'{code}_{k}']; pil=Image.fromarray(cv2.cvtColor(im,cv2.COLOR_BGR2RGB)); ex=Image.Exif()
        ex[270]=f"{code} - enhanced still from {code}-video.mp4 at {e['time_s']}s (frame {e['video_frame']}, {e['fused']} frames fused), Real-ESRGAN x4. Not a camera photo."
        ex[305]='Knooz catalog pipeline (video still enhancement)'
        for sub in (0,2):
            for q in range(95,79,-1):
                b=io.BytesIO(); pil.save(b,'JPEG',quality=q,subsampling=sub,exif=ex,optimize=True)
                if b.tell()<=730000: break
            if b.tell()<=730000: break
        open(f'/tmp/kw/jfinal/{code}/{code}-{k}.jpg','wb').write(b.getvalue()); QS[f'{code}-{k}']=[q,sub,b.tell()]
json.dump(QS,open('/tmp/kw/jfinal/quality.json','w'),indent=0); print(len(QS),'done')
