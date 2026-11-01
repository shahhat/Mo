# Stage 3: 3600x3600, gentle sharpening, brand logo (top-right, ~11% width as in ROS-Amb-G-013), honest EXIF note, JPEG.
import cv2,numpy as np,json,os,sys
from PIL import Image
S=3600; log=json.load(open('/tmp/kw/crops/log.json')); sel=json.load(open('/tmp/kw/sel.json'))
L=cv2.imread('/tmp/kw/logo_raw.png').astype(np.float32)
lh=int(S*0.118); lw=int(L.shape[1]*lh/L.shape[0]); L=cv2.resize(L,(lw,lh),interpolation=cv2.INTER_AREA)
A=np.clip((L.max(axis=2,keepdims=True)-18)/55,0,1)
os.makedirs('/tmp/kw/final',exist_ok=True); QS={}
for code,items in sel.items():
    os.makedirs(f'/tmp/kw/final/{code}',exist_ok=True)
    for k in range(1,len(items)+1):
        src=f'/tmp/kw/srout/{code}_{k}.png'
        if not os.path.exists(src): continue
        im=cv2.imread(src); im=cv2.resize(im,(S,S),interpolation=cv2.INTER_LANCZOS4 if im.shape[0]<S else cv2.INTER_AREA)
        bl=cv2.GaussianBlur(im,(0,0),2.0); im=cv2.addWeighted(im,1.25,bl,-0.25,0)
        m=int(S*0.035); x0=S-m-lw; roi=im[m:m+lh,x0:x0+lw].astype(np.float32)
        im[m:m+lh,x0:x0+lw]=(roi*(1-A)+L*A).astype(np.uint8)
        e=log[f'{code}_{k}']
        pil=Image.fromarray(cv2.cvtColor(im,cv2.COLOR_BGR2RGB)); ex=Image.Exif()
        ex[270]=f"{code} - enhanced still from {code}-video.mp4 at {e['time_s']}s (frame {e['video_frame']}), Real-ESRGAN x4. Not a camera photo."
        ex[305]='Knooz catalog pipeline (video still enhancement)'
        out=f'/tmp/kw/final/{code}/{code}-{k}.jpg'
        import io
        for sub in (0,2):
            for q in range(94,79,-2):
                b=io.BytesIO(); pil.save(b,'JPEG',quality=q,subsampling=sub,exif=ex,optimize=True)
                if b.tell()<=730000: break
            if b.tell()<=730000: break
        open(out,'wb').write(b.getvalue()); QS[f'{code}-{k}']=(q,sub)
        print(out,os.path.getsize(out)//1024,'KB',flush=True)

json.dump(QS,open('/tmp/kw/final/quality.json','w'))
