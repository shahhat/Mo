#!/usr/bin/env python3
"""EDL → render.  Every shot is rendered once to a cached 4K intermediate (keyed by a hash of its EDL entry), light sweeps
are applied by sweep.py on that intermediate, then the timeline is assembled (hard cuts via concat, dissolves via xfade),
music is trimmed/faded/loudness-normalised and the master is encoded.  A change in the EDL re-renders only the shots whose
entry changed.

usage: render.py edl.json --out final/khanjar_4k.mp4 [--preview preview.mp4] [--work work]
EDL schema (all times in seconds):
{
 "fps": "30000/1001", "width": 3840, "height": 2160, "bitrate_mbps": 40,
 "music": {"file": "...", "start": 0.0, "fade_in": 0.0, "fade_out": 2.5, "lufs": -14, "tp": -1},
 "shots": [ {"id":"S01", "src":"raw/10.mp4", "in":21.0, "out":25.5, "speed":1.0,
             "color":"mp4"|"mov", "crop":[x,y,w,h]|null, "stab":false,
             "grade":{"contrast":1.0,"brightness":0.0,"saturation":1.0,"gamma":1.0,"curves":""},
             "fade_in":0.0, "fade_out":0.0, "transition_in":{"type":"dissolve","dur":0.0},
             "sweeps":[{"peak":1.2,"dur":0.9,"dir":"ltr","width":0.10,"soft":0.7,"gain":0.9,"roi":null,"focus":null}] } ],
 "end_card": {"file": null, "dur": 0.0, "fade_in": 0.5},
 "tail_black": 0.0
}"""
import json,subprocess,os,sys,hashlib,argparse,shlex,fractions
ap=argparse.ArgumentParser(); ap.add_argument("edl"); ap.add_argument("--out",required=True); ap.add_argument("--preview",action="store_true")
ap.add_argument("--work",default="work"); ap.add_argument("--force",action="store_true"); a=ap.parse_args()
E=json.load(open(a.edl)); os.makedirs(a.work+"/shots",exist_ok=True); os.makedirs(os.path.dirname(a.out) or ".",exist_ok=True)
FPS=E.get("fps","30000/1001"); fr=fractions.Fraction(FPS); FPSF=float(fr)
W,H=(1920,1080) if a.preview else (E.get("width",3840),E.get("height",2160))
def sh(c,quiet=True):
    r=subprocess.run(c,shell=True,capture_output=True,text=True)
    if r.returncode: print(c,"\n",r.stderr[-3000:]); sys.exit(1)
    return r
def q(p): return shlex.quote(p)
def frames(t): return int(round(t*FPSF))
def snap(t): return frames(t)/FPSF
def shot_filters(s):
    f=[]
    sp=s.get("speed",1.0)
    if sp!=1.0: f.append(f"setpts=PTS/{sp}")
    if s.get("color")=="mov":   # iPhone-style full-range yuvj420p tagged bt470m → limited-range bt709
        f.append("scale=in_range=pc:out_range=tv:in_color_matrix=bt709:out_color_matrix=bt709")
    f.append("setparams=range=tv:color_primaries=bt709:color_trc=bt709:colorspace=bt709")
    if s.get("crop"): x,y,w,h=s["crop"]; f.append(f"crop={w}:{h}:{x}:{y}")
    f.append(f"scale={W}:{H}:flags=lanczos+accurate_rnd+full_chroma_int")
    g=s.get("grade") or {}
    eq=[]
    for k in ("contrast","brightness","saturation","gamma"):
        if k in g and g[k] not in (None,1.0 if k!="brightness" else 0.0): eq.append(f"{k}={g[k]}")
    if eq: f.append("eq="+":".join(eq))
    if g.get("curves"): f.append("curves="+g["curves"])
    dur=snap((s["out"]-s["in"])/sp)
    if s.get("fade_in"): f.append(f"fade=t=in:st=0:d={s['fade_in']}")
    if s.get("fade_out"): f.append(f"fade=t=out:st={dur-s['fade_out']:.4f}:d={s['fade_out']}")
    f.append(f"fps={FPS}"); f.append("format=yuv420p")
    return ",".join(f),dur
def render_shot(s):
    key=hashlib.md5((json.dumps(s,sort_keys=True)+f"{W}x{H}").encode()).hexdigest()[:10]
    base=f"{a.work}/shots/{s['id']}_{key}"; out=base+".mp4"
    if os.path.exists(out) and not a.force: return out
    vf,dur=shot_filters(s); src=s["src"]; pre=""
    if s.get("stab"):
        trf=base+".trf"
        if not os.path.exists(trf):
            sh(f"ffmpeg -y -v error -ss {s['in']} -i {q(src)} -t {s['out']-s['in']} -vf vidstabdetect=shakiness=5:accuracy=15:result={q(trf)} -f null -")
        pre=f"vidstabtransform=input={q(trf)}:smoothing=30:zoom=2:optzoom=0:interpol=bicubic,"
    crf=18 if a.preview else 10
    sh(f"ffmpeg -y -v error -ss {s['in']} -i {q(src)} -t {s['out']-s['in']} -an -vf {q(pre+vf)} -r {FPS} -c:v libx264 -preset {'veryfast' if a.preview else 'medium'} -crf {crf} -pix_fmt yuv420p -color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv {q(base+'_raw.mp4')}")
    if s.get("sweeps"):
        spec=base+"_sweeps.json"; json.dump({"fps":FPSF,"sweeps":s["sweeps"]},open(spec,"w"))
        sh(f"python3 {q(os.path.join(os.path.dirname(__file__),'sweep.py'))} {q(base+'_raw.mp4')} {q(spec)} {q(out)} {'--preview' if a.preview else ''}")
        os.remove(base+"_raw.mp4")
    else: os.replace(base+"_raw.mp4",out)
    return out
# ---- shots
files=[];durs=[];tl=[]  # timeline cut times
t=0.0
for s in E["shots"]:
    f=render_shot(s); d=float(sh(f"ffprobe -v error -show_entries format=duration -of csv=p=0 {q(f)}").stdout.strip())
    files.append(f); durs.append(d)
ec=E.get("end_card") or {}
if ec.get("file") and ec.get("dur",0)>0:
    key=hashlib.md5(json.dumps(ec,sort_keys=True).encode()).hexdigest()[:8]; out=f"{a.work}/shots/END_{key}_{W}.mp4"
    if not os.path.exists(out):
        sh(f"ffmpeg -y -v error -loop 1 -i {q(ec['file'])} -t {ec['dur']} -vf \"scale={W}:{H}:flags=lanczos,format=yuv420p,fade=t=in:st=0:d={ec.get('fade_in',0.5)},fps={FPS}\" -c:v libx264 -crf 10 -pix_fmt yuv420p -color_primaries bt709 -color_trc bt709 -colorspace bt709 {q(out)}")
    files.append(out); durs.append(float(ec["dur"])); E["shots"].append({"id":"END","transition_in":{"type":"dissolve","dur":ec.get("xfade",0.0)}})
# ---- assemble
inputs=" ".join(f"-i {q(f)}" for f in files); fc=[]; cur="[0:v]"; cur_dur=durs[0]; cuts=[]
for i in range(1,len(files)):
    tr=(E["shots"][i].get("transition_in") or {}); d=float(tr.get("dur",0) or 0)
    if d>0:
        off=cur_dur-d; fc.append(f"{cur}[{i}:v]xfade=transition={tr.get('type','fade') if tr.get('type')!='dissolve' else 'fade'}:duration={d}:offset={off:.4f}[v{i}]"); cuts.append(off+d/2); cur_dur=off+durs[i]
    else:
        fc.append(f"{cur}[{i}:v]concat=n=2:v=1:a=0[v{i}]"); cuts.append(cur_dur); cur_dur+=durs[i]
    cur=f"[v{i}]"
tail=float(E.get("tail_black",0) or 0)
if tail>0: fc.append(f"{cur}tpad=stop_mode=add:stop_duration={tail}:color=black[vt]"); cur="[vt]"; cur_dur+=tail
total=cur_dur
# ---- audio: two-pass loudnorm on the trimmed music
m=E["music"]; ad=f"{a.work}/music_trim.wav"
sh(f"ffmpeg -y -v error -ss {m.get('start',0)} -i {q(m['file'])} -t {total:.4f} -af \"afade=t=in:st=0:d={m.get('fade_in',0) or 0.01},afade=t=out:st={total-m.get('fade_out',2):.4f}:d={m.get('fade_out',2)},aresample=48000\" -ac 2 {q(ad)}")
r=subprocess.run(f"ffmpeg -v info -i {q(ad)} -af loudnorm=I={m.get('lufs',-14)}:TP={m.get('tp',-1)}:LRA=11:print_format=json -f null -",shell=True,capture_output=True,text=True)
js=json.loads(r.stderr[r.stderr.rfind("{"):r.stderr.rfind("}")+1])
ln=f"loudnorm=I={m.get('lufs',-14)}:TP={m.get('tp',-1)}:LRA=11:measured_I={js['input_i']}:measured_TP={js['input_tp']}:measured_LRA={js['input_lra']}:measured_thresh={js['input_thresh']}:offset={js['target_offset']}:linear=true:print_format=summary,aresample=48000"
mb=E.get("bitrate_mbps",40)
venc=(f"-c:v libx264 -preset veryfast -crf 18" if a.preview else f"-c:v libx264 -preset slow -profile:v high -level 5.1 -b:v {mb}M -maxrate {int(mb*1.2)}M -bufsize {mb*2}M -x264-params keyint=60:min-keyint=30:aq-mode=3:aq-strength=0.9")
fcs=";".join(fc) if fc else f"{cur}null[vout]"
if fc: fcs+=f";{cur}null[vout]"
sh(f"ffmpeg -y -v error {inputs} -i {q(ad)} -filter_complex {q(fcs)} -map [vout] -map {len(files)}:a -af {q(ln)} {venc} -pix_fmt yuv420p -color_primaries bt709 -color_trc bt709 -colorspace bt709 -color_range tv -r {FPS} -c:a aac -b:a 320k -ar 48000 -movflags +faststart {q(a.out)}")
json.dump({"out":a.out,"total":total,"cuts":[snap(c) for c in cuts],"shot_durs":durs,"files":files},open(a.out+".timeline.json","w"),indent=1)
print("rendered",a.out,"total",round(total,3),"s cuts",[round(c,3) for c in cuts])
