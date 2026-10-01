#!/usr/bin/env python3
"""Reference-film metrics (the version run in the sandbox on 2026-10-01): scene cuts (scdet), luma stats, bright-pixel
centroid tracking for light sweeps (854x480), librosa beat/onset grid, onset-envelope cross-correlation between films.
Usage: ref_metrics.py refs_dir out_dir"""
import json,subprocess,os,re,sys,numpy as np,cv2,librosa
REF,OUT=sys.argv[1],sys.argv[2]; os.makedirs(OUT,exist_ok=True)
ids=[f[4:-4] for f in sorted(os.listdir(REF)) if f.startswith("ref_") and f.endswith(".mp4")]
def run(c): return subprocess.run(c,shell=True,capture_output=True,text=True)
for vid in ids:
    b=f"{REF}/ref_{vid}"; res={"id":vid}
    r=run(f'ffmpeg -v error -i "{b}.mp4" -vf "scale=320:-2,scdet=threshold=5:sc_pass=1,metadata=print:file=-" -f null -')
    frames=[];cur=None
    for line in r.stdout.splitlines():
        m=re.match(r"frame:(\d+)\s+pts:\S+\s+pts_time:([\d.]+)",line)
        if m: cur={"t":float(m.group(2))}; frames.append(cur); continue
        m=re.match(r"lavfi\.scd\.score=([\d.\-]+)",line)
        if m and cur is not None: cur["score"]=float(m.group(1))
    cuts=[(f["t"],f.get("score",0)) for f in frames if f.get("score",0)>=8]; merged=[]
    for t,s in cuts:
        if merged and t-merged[-1][0]<0.25: merged[-1]=(merged[-1][0],max(merged[-1][1],s))
        else: merged.append((t,s))
    res["cuts"]=[[round(t,3),round(s,1)] for t,s in merged]
    cap=cv2.VideoCapture(b+".mp4"); sw=[]; n=0
    while True:
        ok,fr=cap.read()
        if not ok: break
        g=cv2.cvtColor(cv2.resize(fr,(854,480)),cv2.COLOR_BGR2GRAY); m=g>=225
        if m.sum()>30: ys,xs=np.nonzero(m); sw.append([n,round(float(m.mean())*100,2),int(xs.mean()),int(ys.mean()),int(xs.std()),int(ys.std())])
        else: sw.append([n,round(float(m.mean())*100,2),-1,-1,0,0])
        n+=1
    res["sweep_track"]=sw
    y,sr=librosa.load(b+".m4a",sr=22050,mono=True); oenv=librosa.onset.onset_strength(y=y,sr=sr,hop_length=512)
    tempo,beats=librosa.beat.beat_track(y=y,sr=sr,hop_length=512,onset_envelope=oenv)
    pk=librosa.util.peak_pick(oenv,pre_max=10,post_max=10,pre_avg=30,post_avg=30,delta=np.percentile(oenv,90)*0.5,wait=8)
    res["audio"]={"tempo":float(np.atleast_1d(tempo)[0]),"beats":[round(float(t),3) for t in librosa.frames_to_time(beats,sr=sr,hop_length=512)],"onsets":[[round(float(t),3),round(float(oenv[i]),2)] for t,i in zip(librosa.frames_to_time(pk,sr=sr,hop_length=512),pk)]}
    np.save(f"{OUT}/{vid}_oenv.npy",oenv); json.dump(res,open(f"{OUT}/{vid}.json","w")); print(vid,len(res["cuts"]),"cuts")
