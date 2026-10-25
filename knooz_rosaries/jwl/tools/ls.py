import re,html,subprocess,json,sys
def ls(fid):
    s=subprocess.run(['curl','-sSL',f'https://drive.google.com/embeddedfolderview?id={fid}'],capture_output=True,text=True).stdout
    ents=re.findall(r'<div class="flip-entry" id="entry-([^"]+)".*?<a href="([^"]*)".*?<div class="flip-entry-title">([^<]*)</div>',s,re.S)
    out=[]
    for i,href,t in ents:
        isdir='/folders/' in href
        out.append({'id':i,'title':html.unescape(t),'dir':isdir})
    return out
def walk(fid,path=''):
    res=[]
    for e in ls(fid):
        p=path+'/'+e['title']
        if e['dir']:
            res.append({'id':e['id'],'path':p,'dir':True})
            res+=walk(e['id'],p)
        else:
            res.append({'id':e['id'],'path':p,'dir':False})
    return res
if __name__=='__main__':
    r=walk(sys.argv[1])
    json.dump(r,open(sys.argv[2],'w'),ensure_ascii=False,indent=1)
    print(len(r),'entries;',sum(1 for x in r if x['dir']),'dirs')
