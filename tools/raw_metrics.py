#!/usr/bin/env python3
"""Technical metrics for every raw clip: ffprobe + per-sample sharpness/motion/exposure (4 samples/s at 1920 wide).
Usage: raw_metrics.py raw_dir out_dir   (writes out_dir/raw_<i>.json and raw.log)  — the version run in the sandbox on 2026-10-01."""
import json,subprocess,os,sys,numpy as np,cv2,time
RAW,OUT=sys.argv[1],sys.argv[2]; os.makedirs(OUT,exist_ok=True)
files=sorted(f for f in os.listdir(RAW) if f.lower().endswith((".mp4",".mov")))
log=open(f"{OUT}/raw.log","a")
def L(*a): print(time.strftime("%H:%M:%S"),*a,file=log,flush=True)
def run(c): return subprocess.run(c,shell=True,capture_output=True,text=True)
for i,name in enumerate(files):
    p=os.path.join(RAW,name); res={"name":name}
    pr=json.loads(run(f'ffprobe -v error -print_format json -show_format -show_streams "{p}"').stdout)
    v=[s for s in pr["streams"] if s["codec_type"]=="video"][0]
    rot=None
    for sd in v.get("side_data_list",[]):
        if "rotation" in sd: rot=sd["rotation"]
    res["probe"]={"codec":v.get("codec_name"),"profile":v.get("profile"),"w":v["width"],"h":v["height"],"r_fps":v.get("r_frame_rate"),"avg_fps":v.get("avg_frame_rate"),"pix":v.get("pix_fmt"),"trc":v.get("color_transfer"),"prim":v.get("color_primaries"),"space":v.get("color_space"),"range":v.get("color_range"),"rot":rot,"dur":float(pr["format"]["duration"]),"br":pr["format"].get("bit_rate")}
    W=1920; H=int(round(W*v["height"]/v["width"]/2))*2
    if rot in (90,-90,270): H,W=W,int(round(W*v["height"]/v["width"]/2))*2
    pipe=subprocess.Popen(["ffmpeg","-v","error","-i",p,"-vf",f"fps=4,scale={W}:{H}","-pix_fmt","gray","-f","rawvideo","-"],stdout=subprocess.PIPE)
    samples=[]; prev=None; n=0; fsz=W*H
    while True:
        buf=pipe.stdout.read(fsz)
        if len(buf)<fsz: break
        g=np.frombuffer(buf,np.uint8).reshape(H,W); lap=cv2.Laplacian(g,cv2.CV_64F)
        th,tw=H//8,W//8; tiles=np.array([lap[ty*th:(ty+1)*th,tx*tw:(tx+1)*tw].var() for ty in range(8) for tx in range(8)])
        small=cv2.resize(g,(240,int(240*H/W))).astype(np.float32)
        mot=float(np.abs(small-prev).mean()) if prev is not None else 0.0; prev=small
        samples.append([round(n/4,2),round(float(lap.var()),1),round(float(np.sort(tiles)[-10:].mean()),1),round(mot,2),round(float(g.mean()),1),round(float((g>=250).mean()*100),2),round(float((g<=8).mean()*100),2)])
        n+=1
    pipe.wait(); res["samples"]=samples
    json.dump(res,open(f"{OUT}/raw_{i}.json","w")); L(i,name,res["probe"])
