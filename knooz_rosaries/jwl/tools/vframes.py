import json, subprocess, os, sys, hashlib
J='/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/jwl'
pick=json.load(open(f'{J}/vid_pick.json'))
for i,p in enumerate(pick,1):
    d=f'{J}/vf/v{i:02d}'; os.makedirs(d,exist_ok=True)
    if os.path.exists(f'{d}/done'): continue
    mp=f'{d}/v.mp4'
    subprocess.run(['curl','-sS','-L','-o',mp,f"https://drive.usercontent.google.com/download?id={p['id']}&export=download&confirm=t"])
    md5=hashlib.md5(open(mp,'rb').read()).hexdigest(); size=os.path.getsize(mp)
    pr=subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height:format=duration','-of','json',mp],capture_output=True,text=True).stdout
    info=json.loads(pr) if pr else {}
    subprocess.run(['ffmpeg','-loglevel','error','-i',mp,'-vf','fps=1','-q:v','2',f'{d}/f%03d.jpg'])
    meta={'i':i,'src':p['src'],'id':p['id'],'md5':md5,'size':size,'info':info}
    json.dump(meta,open(f'{d}/meta.json','w'),ensure_ascii=False)
    os.remove(mp); open(f'{d}/done','w').close()
    print(i,p['src'],size,md5[:8],flush=True)
print('ALL DONE')
