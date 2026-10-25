"""Compose 1080x1080 stills for video-only pieces: square crop around the object, video watermark painted out,
photographer logo (from a catalog photo) alpha-composited in the darkest corner. spec.json: {code: {"v": "v15", "shots": [{"f":3, "box":[cx,cy,S]?, "thr":40, "pad":1.3, "rows":[y0,y1]?, "logo":"tr"?}]}}"""
import json,sys,os
from PIL import Image
import numpy as np
J='/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/jwl'
OUT=f'{J}/red/out'; os.makedirs(OUT,exist_ok=True)
N=1080
L=Image.open(f'{J}/red/logo_src.png').convert('RGB'); la=np.asarray(L).astype(int)
m=la.max(2)>30; ys,xs=np.where(m); L=L.crop((xs.min()-4,ys.min()-4,xs.max()+5,ys.max()+5))
LW=round(0.085*N); LH=round(L.size[1]*LW/L.size[0]); Lr=np.asarray(L.resize((LW,LH),Image.LANCZOS)).astype(float)
spec=json.load(open(f'{J}/red/spec.json')); only=sys.argv[1:]
for code,sp in spec.items():
    if only and code not in only: continue
    for k,s in enumerate(sp['shots'],1):
        g=np.asarray(Image.open(f"{J}/vf/{sp['v']}/f{s['f']:03d}.jpg").convert('RGB')).astype(float); H,W=g.shape[:2]
        # paint out the green watermark in the top-right quarter
        q=g[:H//4, W//2:]
        gm=(q[:,:,1]>q[:,:,0]+25)&(q[:,:,1]>60)
        if gm.sum()>200:
            yy,xx=np.where(gm); pad=int(0.03*W)
            y0,y1=max(0,yy.min()-pad),min(H//4,yy.max()+pad*2); x0,x1=W//2+max(0,xx.min()-pad),min(W,W//2+xx.max()+pad)
            g[y0:y1,x0:x1]=np.median(g[y0:y1,max(0,x0-40):x0].reshape(-1,3),0)
        bgc=np.median(np.concatenate([g[:30,:30].reshape(-1,3),g[-30:,:30].reshape(-1,3)]),0)
        for b0,b1 in s.get('blank',sp.get('blank',[])):
            g[int(b0*H):int(b1*H)]=bgc
        WM={(1920,1080):(1690,1880,0,215),(1080,1700):(900,1065,55,240),(1080,1920):(925,1065,90,280),(2160,3840):(1870,2115,195,535)}.get((W,H))
        if WM:
            x0,x1,y0,y1=WM; g[y0:y1,x0:x1]=np.median(g[y0:y1,max(0,x0-60):x0].reshape(-1,3),0)
        if 'box' in s: cx,cy,S=s['box']
        elif 'S' in s or 'S' in sp:
            r0,r1=[int(x*H) for x in s.get('rows',sp.get('rows',[0,1]))]; lum=g.max(2); mm=np.zeros_like(lum,bool); mm[r0:r1]=lum[r0:r1]>s.get('thr',sp.get('thr',60))
            ys,xs=np.where(mm); cx=np.median(xs); cy=np.median(ys); S=s.get('S',sp.get('S'))*(W if W<H else H)
        else:
            r0,r1=[int(x*H) for x in s.get('rows',sp.get('rows',[0,1]))]; lum=g.max(2); mm=np.zeros_like(lum,bool); mm[r0:r1]=lum[r0:r1]>s.get('thr',sp.get('thr',40))
            ys,xs=np.where(mm); x0,x1=np.percentile(xs,[0.5,99.5]); y0,y1=np.percentile(ys,[0.5,99.5])
            cx=(x0+x1)/2; cy=(y0+y1)/2; S=max(x1-x0,y1-y0)*s.get('pad',sp.get('pad',1.3))
        S=int(round(S)); cx=int(round(cx)); cy=int(round(cy))
        bg=np.median(np.concatenate([g[:30,:30].reshape(-1,3),g[-30:,:30].reshape(-1,3),g[-30:,-30:].reshape(-1,3)]),0)
        P=S; gp=np.pad(g,((P,P),(P,P),(0,0)),mode='edge')
        yy,xx=np.mgrid[0:H+2*P,0:W+2*P]
        dx=np.maximum(np.maximum(P-xx,xx-(P+W-1)),0); dy=np.maximum(np.maximum(P-yy,yy-(P+H-1)),0)
        w=np.clip(np.maximum(dx,dy)/float(s.get('fade',120)),0,1)[...,None]; gp=gp*(1-w)+bg*w
        X0=cx-S//2+P; Y0=cy-S//2+P; can=gp[Y0:Y0+S,X0:X0+S]
        a=np.asarray(Image.fromarray(np.clip(can,0,255).astype(np.uint8)).resize((N,N),Image.LANCZOS)).astype(float)
        mx=round(0.05*N); my=round(0.037*N)
        pos={'tr':(N-mx-LW,my),'tl':(mx,my),'br':(N-mx-LW,N-my-LH),'bl':(mx,N-my-LH)}
        side=s.get('logo') or min(pos,key=lambda kk:a[pos[kk][1]:pos[kk][1]+LH,pos[kk][0]:pos[kk][0]+LW].mean()+(0 if kk[0]=='t' else 6))
        x,y=pos[side]; al=np.clip((Lr.max(2,keepdims=True)-10)/50.0,0,1)
        a[y:y+LH,x:x+LW]=np.clip(Lr+a[y:y+LH,x:x+LW]*(1-al),0,255)
        Image.fromarray(a.astype(np.uint8)).save(f'{OUT}/{code}-{k}.jpg',quality=95,subsampling=0)
        print(code,k,sp['v'],'f%03d'%s['f'],'S',S,'logo',side)
