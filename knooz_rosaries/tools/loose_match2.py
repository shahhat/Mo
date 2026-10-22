import json, datetime, bisect, collections
m=json.load(open('meta/meta.json'))
def ts(r):
    try: return datetime.datetime.strptime(r['dto'],'%Y:%m:%d %H:%M:%S').timestamp()
    except: return None
pieces=[r for r in m if r['piece'] and r.get('dto')]
key=collections.defaultdict(list)
for r in pieces: key[(r['dto'],r.get('imgno'))].append(r)
pieces.sort(key=lambda r:(ts(r), r.get('imgno') or 0))
res=[]
for r in [x for x in m if x['piece'] is None]:
    d=key.get((r['dto'],r.get('imgno')))
    if d:
        res.append(dict(kind='DUP',cat=r['cat'],title=r['title'],id=r['id'],of=[x['title'] for x in d]))
        continue
    t=ts(r)
    before=[p for p in pieces if ts(p)<=t]; after=[p for p in pieces if ts(p)>t]
    pv=before[-1]; nx=after[0] if after else None
    res.append(dict(kind='SAME' if nx and pv['piece']==nx['piece'] else 'SPLIT',cat=r['cat'],title=r['title'],id=r['id'],imgno=r['imgno'],
       prev=pv['title'],prev_piece=pv['piece'],dp=t-ts(pv),ip=r['imgno']-(pv.get('imgno') or 0),
       next=nx['title'] if nx else None,next_piece=nx['piece'] if nx else None,dn=(ts(nx)-t) if nx else None,inn=((nx.get('imgno') or 0)-r['imgno']) if nx else None))
json.dump(res,open('meta/loose_match.json','w'),ensure_ascii=False,indent=0)
c=collections.Counter(x['kind'] for x in res); print(c)
for x in res:
    if x['kind']=='DUP': print('DUP  ',x['cat'],x['title'],'=',x['of'])
for x in res:
    if x['kind']!='DUP': print(f"{x['kind']:5} {x['cat']:6} {x['title']:16} prev {x['prev']} (-{x['dp']:.0f}s,{x['ip']}fr) | next {x['next']} (+{x['dn']:.0f}s,{x['inn']}fr)")
