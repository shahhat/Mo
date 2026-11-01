import cv2,json,os,sys,numpy as np
sys.path.insert(0,'/tmp/kw'); from jfuse import grab,sharp
sel=json.load(open('/tmp/kw/jsel.json')); os.makedirs('/tmp/kw/jcrops',exist_ok=True); log={}
def objbox(fr):
    H,W=fr.shape[:2]; g=cv2.cvtColor(fr,cv2.COLOR_BGR2GRAY).astype(np.float32)
    land=W>H; cap=int(H*(0.72 if land else 0.62))
    g[cap:,:]=0; g[:int(H*0.12),int(W*0.85):]=0
    if not land: g[:int(H*0.28),:]=0
    m=(g>70).astype(np.uint8); m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((5,5),np.uint8))
    ys,xs=np.nonzero(m); x0,x1,y0,y1=[np.percentile(a,p) for a,p in ((xs,1),(xs,99),(ys,1),(ys,99))]
    s=int(max(x1-x0,y1-y0)*1.25); s=max(s,420); s=min(s,W,H)
    x=int(np.clip((x0+x1)/2-s/2,0,W-s)); y=int(np.clip((y0+y1)/2-s/2,0,H-s)); return x,y,s
for code,shots in sel.items():
    V=f'/tmp/kw/jv/{code}.mp4'; cap=cv2.VideoCapture(V); fps=cap.get(5); W=int(cap.get(3)); H=int(cap.get(4))
    for k,sh in enumerate(shots,1):
        mode,lo,hi=sh[0],sh[1],sh[2]
        fr=grab(V,int((lo-1)*0.5*fps),int((hi-1)*0.5*fps))
        mid=fr[len(fr)//2][1]
        if mode=='ring': s=560; box=(W//2-s//2,int(H*(0.40 if W>H else 0.43))-s//2,s)
        elif mode=='top': s=min(780,H,W); box=(int(np.clip(sh[3]*W-s/2,0,W-s)),0,s)
        elif mode=='ctr': s=sh[5]; box=(int(np.clip(sh[3]*W-s/2,0,W-s)),int(np.clip(sh[4]*H-s/2,0,H-s)),s)
        else: box=objbox(mid)
        x,y,s=box
        sc=[sharp(f[y:y+s,x:x+s]) for _,f in fr]; i=int(np.argmax(sc)); ref=fr[i][1][y:y+s,x:x+s]
        acc=[ref.astype(np.float32)]; rg=cv2.cvtColor(ref,cv2.COLOR_BGR2GRAY).astype(np.float32)
        for j in range(max(0,i-2),min(len(fr),i+3)):
            if j==i: continue
            c=fr[j][1][y:y+s,x:x+s]; cg=cv2.cvtColor(c,cv2.COLOR_BGR2GRAY).astype(np.float32); w=np.eye(2,3,dtype=np.float32)
            try:
                cc,w=cv2.findTransformECC(rg,cg,w,cv2.MOTION_AFFINE,(3,100,1e-5),None,5)
                if cc>=0.97: acc.append(cv2.warpAffine(c,w,(s,s),flags=cv2.INTER_CUBIC+cv2.WARP_INVERSE_MAP).astype(np.float32))
            except cv2.error: pass
        out=np.clip(np.mean(acc,axis=0),0,255).astype(np.uint8)
        cv2.imwrite(f'/tmp/kw/jcrops/{code}_{k}.png',out)
        log[f'{code}_{k}']={'video_frame':fr[i][0],'time_s':round(fr[i][0]/fps,2),'mode':mode,'box':[int(v) for v in box],'fused':len(acc),'sharpness':round(float(sc[i]),1)}
json.dump(log,open('/tmp/kw/jcrops/log.json','w'),indent=1)
