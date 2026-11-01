import cv2,numpy as np
def grab(video,f0,f1):
    cap=cv2.VideoCapture(video); cap.set(1,f0); out=[]
    for f in range(f0,f1+1):
        ok,fr=cap.read()
        if not ok: break
        out.append((f,fr))
    return out
def sharp(c): return cv2.Laplacian(cv2.cvtColor(c,cv2.COLOR_BGR2GRAY),cv2.CV_64F).var()
def best_and_fuse(video,f0,f1,box,k=2):
    x,y,s=box; fr=grab(video,f0,f1)
    sc=[sharp(f[y:y+s,x:x+s]) for _,f in fr]; i=int(np.argmax(sc))
    ref=fr[i][1][y:y+s,x:x+s]; acc=[ref.astype(np.float32)]
    rg=cv2.cvtColor(ref,cv2.COLOR_BGR2GRAY).astype(np.float32)
    for j in range(max(0,i-k),min(len(fr),i+k+1)):
        if j==i: continue
        c=fr[j][1][y:y+s,x:x+s]; cg=cv2.cvtColor(c,cv2.COLOR_BGR2GRAY).astype(np.float32)
        warp=np.eye(2,3,dtype=np.float32)
        try:
            cc,warp=cv2.findTransformECC(rg,cg,warp,cv2.MOTION_AFFINE,(cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT,100,1e-5),None,5)
            if cc<0.97: continue
            acc.append(cv2.warpAffine(c,warp,(s,s),flags=cv2.INTER_CUBIC+cv2.WARP_INVERSE_MAP).astype(np.float32))
        except cv2.error: pass
    fused=np.clip(np.mean(acc,axis=0),0,255).astype(np.uint8)
    return fr[i][0],ref,fused,len(acc)
