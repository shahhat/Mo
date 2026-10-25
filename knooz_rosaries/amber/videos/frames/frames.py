import json, subprocess, os, sys
AMB='/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/amb'
plan=json.load(open(f'{AMB}/v9/amb_vid_plan.json'))
plan.append({'src':'phase 12/من_تحف_الكهرمان_المنحوتة.mp4','id':'1QMf6N3V82FMdVOIVcm5D9e4VTg7gFH9H','code':'Amb-dec-003'})
for p in plan:
    code=p['code'].split(' ')[0]
    d=f'{AMB}/v10/{code}'; os.makedirs(d,exist_ok=True)
    if os.path.exists(f'{d}/done'): continue
    mp=f'{d}/v.mp4'
    if p['code']=='AMB-ST-030' and os.path.exists(f'{AMB}/qc/hr/a009.mp4'): os.replace(f'{AMB}/qc/hr/a009.mp4',mp)
    else: subprocess.run(['curl','-sS','-L','-o',mp,f"https://drive.usercontent.google.com/download?id={p['id']}&export=download&confirm=t"])
    info=subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height:format=duration','-of','json',mp],capture_output=True,text=True).stdout
    j=json.loads(info); dur=float(j['format']['duration']); w=j['streams'][0]['width']; h=j['streams'][0]['height']
    n=int(dur/1.0)
    for i in range(n):
        subprocess.run(['ffmpeg','-loglevel','error','-y','-ss',f'{i+0.5}','-i',mp,'-frames:v','1','-q:v','2',f'{d}/f{i:03d}.jpg'])
    json.dump({'code':p['code'],'src':p['src'],'dur':dur,'w':w,'h':h,'frames':n},open(f'{d}/meta.json','w'),ensure_ascii=False)
    os.remove(mp); open(f'{d}/done','w').write('1')
    print(code,w,h,round(dur),n,flush=True)
print('ALL DONE')
