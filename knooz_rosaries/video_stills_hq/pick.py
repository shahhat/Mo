# Stage 1: for each selection, find the sharpest full-fps frame near the chosen moment and save the square crop.
import cv2,json,sys,os,numpy as np
sel=json.load(open('/tmp/kw/sel.json')); os.makedirs('/tmp/kw/crops',exist_ok=True)
TOP=770  # caption band starts ~0.78H; keep crops above it
def crop_box(fr,mode,cx):
    H,W=fr.shape[:2]
    if mode=='obj':
        g=cv2.cvtColor(fr,cv2.COLOR_BGR2GRAY).astype(np.float32)
        g[:, int(W*0.70):]=0  # logo and (085) title panel sit on the right
        m=(g>45).astype(np.uint8); m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((5,5),np.uint8))
        ys,xs=np.nonzero(m); x0,x1,y0,y1=np.percentile(xs,0.5),np.percentile(xs,99.5),np.percentile(ys,0.5),np.percentile(ys,99.5)
        s=int(max(x1-x0,y1-y0)*1.18); s=min(s,H); c=((x0+x1)/2,(y0+y1)/2)
        x=int(np.clip(c[0]-s/2,0,W-s)); y=int(np.clip(c[1]-s/2,0,H-s)); return x,y,s
    s=H if mode=='full' else TOP
    x=int(np.clip(cx*W-s/2,0,W-s)); return x,0,s
def sharp(img): return cv2.Laplacian(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),cv2.CV_64F).var()
log={}
for code,items in sel.items():
    cap=cv2.VideoCapture(f'/tmp/kw/vid/{code}.mp4'); fps=cap.get(cv2.CAP_PROP_FPS)
    for k,it in enumerate(items,1):
        idx,mode=it[0],it[1]; cx=it[2] if len(it)>2 else .5
        tmpl=cv2.resize(cv2.imread(f'/tmp/kw/fr/{code}/{idx:03d}.jpg'),(192,108)).astype(np.float32)
        t=(idx-1)*0.5; a=max(0,int((t-1.0)*fps)); b=int((t+1.0)*fps)
        cap.set(cv2.CAP_PROP_POS_FRAMES,a); frames=[]
        for f in range(a,b+1):
            ok,fr=cap.read()
            if not ok: break
            frames.append((f,fr))
        d=[np.mean((cv2.resize(fr,(192,108)).astype(np.float32)-tmpl)**2) for f,fr in frames]
        m=int(np.argmin(d)); ref=frames[m][1]; box=crop_box(ref,mode,cx); x,y,s=box
        best=None
        for f,fr in frames[max(0,m-6):m+7]:
            c=fr[y:y+s,x:x+s]; v=sharp(c)
            if best is None or v>best[0]: best=(v,f,c)
        cv2.imwrite(f'/tmp/kw/crops/{code}_{k}.png',best[2])
        log[f'{code}_{k}']={'video_frame':best[1],'time_s':round(best[1]/fps,2),'mode':mode,'box':box,'sharpness':round(best[0],1)}
        print(code,k,log[f'{code}_{k}'],flush=True)
json.dump(log,open('/tmp/kw/crops/log.json','w'),indent=1)
