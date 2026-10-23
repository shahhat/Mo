import json, subprocess, re, html
STAGING='14JQrbkoYfO7ke8VFJzoaNvUIeeG68pNI'
def ls(fid):
    s=subprocess.run(['curl','-sS',f'https://drive.google.com/embeddedfolderview?id={fid}'],capture_output=True,text=True).stdout
    ids=re.findall(r'id="entry-([^"]+)"',s); ts=[html.unescape(t) for t in re.findall(r'flip-entry-title">([^<]*)<',s)]
    return [dict(id=i,title=t,folder=(f'folders/{i}' in s)) for i,t in zip(ids,ts)]
files=[]; folders=[]; stack=[(STAGING,'')]
while stack:
    fid,path=stack.pop()
    for e in ls(fid):
        p=path+'/'+e['title']
        if e['folder']: folders.append(dict(id=e['id'],path=p)); stack.append((e['id'],p))
        else: files.append(dict(id=e['id'],title=e['title'],path=p))
json.dump(dict(files=files,folders=folders),open('staging.json','w'),ensure_ascii=False,indent=0)
print(len(files),'files',len(folders),'folders')
for f in folders: print('D',f['path'])
import collections
print(collections.Counter(f['path'].rsplit('/',1)[0] for f in files))
