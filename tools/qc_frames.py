#!/usr/bin/env python3
"""Pull QC frames from a render: every cut ±2 frames, one frame per 0.5 s, every frame of each sweep; check cut and
sweep-peak times against the accent grid (tolerance 1 frame).  usage: qc_frames.py edl.json render.mp4 outdir"""
import json,subprocess,sys,os,fractions
edl,ren,od=sys.argv[1:4]; os.makedirs(od,exist_ok=True); E=json.load(open(edl)); T=json.load(open(ren+".timeline.json"))
fps=float(fractions.Fraction(E.get("fps","30000/1001"))); fr=lambda t:int(round(t*fps))
def grab(fn,sel): subprocess.run(["ffmpeg","-y","-v","error","-i",ren,"-vf",sel,"-frames:v","1",fn],check=True)
cuts=T["cuts"]; grid=E.get("accents",[]); report=[]
for i,c in enumerate(cuts):
    n=fr(c)
    for d in range(-2,3): grab(f"{od}/cut{i+1:02d}_{n+d:05d}{'' if d else '_CUT'}.png",f"select=eq(n\\,{n+d})")
    near=min(grid,key=lambda g:abs(g-c)) if grid else None
    report.append({"cut":i+1,"t":round(c,3),"frame":n,"nearest_accent":near,"delta_frames":None if near is None else fr(c)-fr(near)})
subprocess.run(["ffmpeg","-y","-v","error","-i",ren,"-vf","fps=2",f"{od}/half_%04d.png"],check=True)
t0=0.0
for s,d in zip(E["shots"],T["shot_durs"]):
    for sw in s.get("sweeps",[]):
        a,b=t0+sw["peak"]-sw["dur"]/2,t0+sw["peak"]+sw["dur"]/2; pk=fr(t0+sw["peak"])
        subprocess.run(["ffmpeg","-y","-v","error","-i",ren,"-vf",f"select=between(n\\,{fr(a)}\\,{fr(b)})","-vsync","0",f"{od}/sweep_{s['id']}_%04d.png"],check=True)
        near=min(grid,key=lambda g:abs(g-(t0+sw['peak']))) if grid else None
        report.append({"sweep":s["id"],"peak_t":round(t0+sw["peak"],3),"peak_frame":pk,"nearest_accent":near,"delta_frames":None if near is None else pk-fr(near)})
    t0+=d-float((s.get("transition_in") or {}).get("dur",0) or 0)
json.dump(report,open(f"{od}/timing_report.json","w"),indent=1); print(json.dumps(report,indent=1))
