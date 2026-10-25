import json, sys, os
from PIL import Image, ImageFilter
import numpy as np
AMB='/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/amb'
OUT=f'{AMB}/v11/out'; os.makedirs(OUT,exist_ok=True)
N=1080
# logo: tight bbox from photographer original
L=Image.open(f'{AMB}/v10/logo_src.png').convert('RGB'); la=np.asarray(L).astype(int)
m=la.max(2)>30; ys,xs=np.where(m)
L=L.crop((xs.min()-4,ys.min()-4,xs.max()+5,ys.max()+5))
LW=round(0.085*N); LH=round(L.size[1]*LW/L.size[0]); Lr=np.asarray(L.resize((LW,LH),Image.LANCZOS)).astype(float)
spec=json.load(open(f'{AMB}/v11/spec.json'))
only=sys.argv[1:]
for code,shots in spec.items():
    if only and code not in only: continue
    for k,s in enumerate(shots,1):
        fr=Image.open(f"{AMB}/v10/{code}/f{s['f']:03d}.jpg").convert('RGB'); g=np.asarray(fr).astype(float)
        H,W=g.shape[:2]
        g[:200,1740:1860]=np.median(g[:200,1700:1740].reshape(-1,3),0)  # video watermark out
        if 'box' in s: cx,cy,S=s['box']
        else:
            lum=g.max(2); mm=lum>s.get('thr',40)
            ys,xs=np.where(mm)
            x0,x1=np.percentile(xs,[0.5,99.5]); y0,y1=np.percentile(ys,[0.5,99.5])
            cx=(x0+x1)/2; cy=(y0+y1)/2; S=max(x1-x0,y1-y0)*s.get('pad',1.3)
        S=int(round(S)); cx=int(round(cx)); cy=int(round(cy))
        bg=np.median(np.concatenate([g[:30,:30].reshape(-1,3),g[:30,-200:-120].reshape(-1,3),g[-30:,:30].reshape(-1,3)]),0)
        P=max(0,S)
        gp=np.pad(g,((P,P),(P,P),(0,0)),mode='edge')
        yy,xx=np.mgrid[0:H+2*P,0:W+2*P]
        dy=np.maximum(np.maximum(P-yy,yy-(P+H-1)),0); dx=np.maximum(np.maximum(P-xx,xx-(P+W-1)),0)
        fd=float(s.get('fade',120)); ft=float(s.get('fade_top',fd))
        dtop=np.maximum(P-yy,0).astype(float); drest=np.maximum(np.maximum(yy-(P+H-1),0),dx).astype(float)
        w=np.clip(np.maximum(dtop/ft,drest/fd),0,1)[...,None]
        gp=gp*(1-w)+bg*w
        X0=cx-S//2+P; Y0=cy-S//2+P
        can=gp[Y0:Y0+S, X0:X0+S]
        im=Image.fromarray(np.clip(can,0,255).astype(np.uint8)).resize((N,N),Image.LANCZOS)
        a=np.asarray(im).astype(float)
        mx=round(0.05*N); my=round(0.037*N)
        side=s.get('logo')
        pos={'tr':(N-mx-LW,my),'tl':(mx,my),'br':(N-mx-LW,N-my-LH),'bl':(mx,N-my-LH)}
        if not side:
            sc={k:a[y:y+LH,x:x+LW].mean()+(0 if k[0]=='t' else 6) for k,(x,y) in pos.items()}
            side=min(sc,key=sc.get)
        x,y=pos[side]
        al=np.clip((Lr.max(2,keepdims=True)-10)/50.0,0,1)
        a[y:y+LH,x:x+LW]=np.clip(Lr+a[y:y+LH,x:x+LW]*(1-al),0,255)
        Image.fromarray(a.astype(np.uint8)).save(f'{OUT}/{code}-{k}.jpg',quality=95,subsampling=0)
        print(code,k,'f%03d'%s['f'],'S',S,'logo',side)
