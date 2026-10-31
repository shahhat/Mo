import json,os,html
sel=json.load(open('/tmp/kw/sel.json')); log=json.load(open('/tmp/kw/crops/log.json')); T=json.load(open('/tmp/kw/targets.json'))
F81='1Ec9b0NtWpat4mny1tf6z7m175mT8j4f8'
pieces=[]
for code,items in sel.items():
    folder=T[code]['folder'] if code in T else F81
    imgs=[]
    for k in range(1,len(items)+1):
        e=log[f'{code}_{k}']
        if not os.path.exists(f'/tmp/kw/site/img/{code}/{code}-{k}.jpg'): continue
        imgs.append({'name':f'{code}-{k}.jpg','full':f'img/{code}/{code}-{k}.jpg','th':f'th/{code}-{k}.jpg',
                     'kind':'whole' if e['mode']=='obj' else 'detail','t':e['time_s']})
    pieces.append({'code':code,'folder':folder,'imgs':imgs})
DATA=json.dumps(pieces,ensure_ascii=False)
total=sum(len(p['imgs']) for p in pieces)
page=open('/tmp/kw/page_tpl.html').read().replace('__DATA__',DATA).replace('__TOTAL__',str(total)).replace('__N__',str(len(pieces)))
open('/tmp/kw/site/index.html','w').write(page); print(total,'images')
