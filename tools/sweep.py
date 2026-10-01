#!/usr/bin/env python3
"""Light sweep on real metal.  Per frame: a blade matte (bright, neutral, textured region, optionally limited to a tracked
ROI polygon), the blade axis from the matte's PCA, and a soft band of light that travels along that axis.  The band
multiplies the metal's own luminance and local detail (so pattern and engraving flare), is confined by the feathered
matte (no spill on background/hilt/fingers), and is soft-clipped below video white.  The band centre crosses the focus
point exactly on the peak frame.
usage: sweep.py in.mp4 spec.json out.mp4 [--preview] [--debug-matte]
spec: {"fps":29.97,"sweeps":[{"peak":1.20,"dur":0.9,"dir":"ltr"|"rtl","width":0.10,"soft":0.7,"gain":0.9,
       "roi":[[x,y],...] (fractions of frame, tracked with optical flow) or null, "focus":[fx,fy] or null,
       "thr":0.45,"sat":0.25}]}"""
import json,subprocess,sys,numpy as np,cv2
src,spec,out=sys.argv[1],sys.argv[2],sys.argv[3]; PREVIEW="--preview" in sys.argv; DEBUG="--debug-matte" in sys.argv
S=json.load(open(spec)); fps=S["fps"]
pr=json.loads(subprocess.run(["ffprobe","-v","error","-print_format","json","-show_streams",src],capture_output=True,text=True).stdout)
v=[s for s in pr["streams"] if s["codec_type"]=="video"][0]; W,H=v["width"],v["height"]; n=int(v.get("nb_frames") or 0)
dec=subprocess.Popen(["ffmpeg","-v","error","-i",src,"-f","rawvideo","-pix_fmt","rgb24","-"],stdout=subprocess.PIPE)
enc=subprocess.Popen(["ffmpeg","-y","-v","error","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(fps),"-i","-","-c:v","libx264","-preset","veryfast" if PREVIEW else "medium","-crf","18" if PREVIEW else "10","-pix_fmt","yuv420p","-color_primaries","bt709","-color_trc","bt709","-colorspace","bt709","-color_range","tv",out],stdin=subprocess.PIPE)
def ease(p): return p*p*(3-2*p)
def band_profile(coord,centre,width,soft):   # coord: 0..1 along axis; gaussian core with wider soft skirt
    s=max(1e-3,width*(0.35+0.65*soft)); d=(coord-centre)/s
    return np.exp(-0.5*d*d)
sweeps=S["sweeps"]; prev_gray=None; roi_pts={}
for sw in sweeps:
    if sw.get("roi"): roi_pts[id(sw)]=np.array([[p[0]*W,p[1]*H] for p in sw["roi"]],np.float32)
fi=0; fsz=W*H*3
while True:
    buf=dec.stdout.read(fsz)
    if len(buf)<fsz: break
    img=np.frombuffer(buf,np.uint8).reshape(H,W,3); t=fi/fps; outimg=img
    gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    small=cv2.resize(gray,(W//4,H//4))
    active=[sw for sw in sweeps if sw["peak"]-sw["dur"]*0.6<=t<=sw["peak"]+sw["dur"]*0.6]
    # track ROI polygons every frame (so they stay valid when the sweep starts)
    if prev_gray is not None and roi_pts:
        flow=cv2.calcOpticalFlowFarneback(prev_gray,small,None,0.5,3,21,3,5,1.2,0)
        for k,pts in roi_pts.items():
            for p in pts:
                x,y=int(np.clip(p[0]/4,0,W//4-1)),int(np.clip(p[1]/4,0,H//4-1)); p[0]+=flow[y,x,0]*4; p[1]+=flow[y,x,1]*4
    prev_gray=small
    if active:
        f=img.astype(np.float32)/255.0
        L=0.2126*f[...,0]+0.7152*f[...,1]+0.0722*f[...,2]
        mx=f.max(2); mn=f.min(2); sat=(mx-mn)/(mx+1e-4)
        for sw in active:
            thr=sw.get("thr",0.45); satmax=sw.get("sat",0.25)
            m=((L>thr)&(sat<satmax)).astype(np.uint8)
            if id(sw) in roi_pts:
                poly=np.zeros((H,W),np.uint8); cv2.fillPoly(poly,[roi_pts[id(sw)].astype(np.int32)],1); m=m*poly
            k=max(3,W//240)|1; m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((k,k),np.uint8)); m=cv2.morphologyEx(m,cv2.MORPH_CLOSE,np.ones((k*2+1,k*2+1),np.uint8))
            nlab,lab,stats,_=cv2.connectedComponentsWithStats(m)
            if nlab<=1: continue
            keep=np.zeros_like(m); big=stats[1:,cv2.CC_STAT_AREA]; order=np.argsort(big)[::-1]
            for j in order[:3]:
                if big[j]>=0.15*big[order[0]]: keep[lab==j+1]=1
            feather=cv2.GaussianBlur(keep.astype(np.float32),(0,0),max(2,W/400))
            ys,xs=np.nonzero(keep)
            if len(xs)<50: continue
            pts=np.stack([xs,ys],1).astype(np.float32); c=pts.mean(0); u,s_,vt=np.linalg.svd(pts-c,full_matrices=False); axis=vt[0]
            if axis[0]<0: axis=-axis
            proj=(pts-c)@axis; lo,hi=np.percentile(proj,1),np.percentile(proj,99)
            fx,fy=(sw["focus"][0]*W,sw["focus"][1]*H) if sw.get("focus") else (c[0],c[1])
            focus_coord=((np.array([fx,fy])-c)@axis-lo)/(hi-lo+1e-6)
            p=(t-(sw["peak"]-sw["dur"]/2))/sw["dur"]            # 0..1 across the pass, 0.5 at the peak
            start,end=(-0.15,1.15) if sw.get("dir","ltr")=="ltr" else (1.15,-0.15)
            centre=start+(end-start)*ease(np.clip(p,0,1))
            centre=centre+(focus_coord-0.5)                        # shift so the band crosses the focus point at the peak
            yy,xx=np.mgrid[0:H,0:W]; coord=(((xx-c[0])*axis[0]+(yy-c[1])*axis[1])-lo)/(hi-lo+1e-6)
            band=band_profile(coord,centre,sw.get("width",0.10),sw.get("soft",0.7))
            hp=np.abs(L-cv2.GaussianBlur(L,(0,0),W/300)); detail=np.clip(hp/(np.percentile(hp[keep>0],95)+1e-4),0,1)
            gain=sw.get("gain",0.9)*band*feather*(0.55+0.9*detail)*(0.4+0.6*L)
            Lnew=L*(1+gain); knee=0.80; over=Lnew>knee; Lnew[over]=knee+(1-knee)*np.tanh((Lnew[over]-knee)/(1-knee)); Lnew=np.minimum(Lnew,0.92)
            ratio=(Lnew/(L+1e-4))[...,None]; f=np.clip(f*ratio,0,1)
            if DEBUG: f[...,1]=np.maximum(f[...,1],feather*0.5)
        outimg=(f*255+0.5).astype(np.uint8)
    enc.stdin.write(np.ascontiguousarray(outimg).tobytes()); fi+=1
enc.stdin.close(); enc.wait(); dec.wait(); print("sweep frames",fi)
