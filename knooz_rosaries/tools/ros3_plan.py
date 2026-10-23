import json, datetime, re
S='/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/ros3/'
idx=json.load(open(S+'tl/idx.json')); meta={r['id']:r for r in json.load(open(S+'meta.json'))}
inv=json.load(open(S+'inv.json'))
def ts(fid): r=meta[fid]; return (datetime.datetime.strptime(r['dto'],'%Y:%m:%d %H:%M:%S'), r.get('imgno') or 0)
R=lambda a,b: list(range(a,b+1))
NEW=[R(1,3),R(4,7),R(8,10),R(11,15),R(16,19),R(20,27),R(28,40),R(41,45),R(46,50),R(51,57),[58],
     [66,67,69,70],R(71,78),R(79,90),R(97,104),R(105,109),R(121,124),R(130,134),R(135,140),R(141,144),R(145,154),R(155,159),
     R(169,176),R(184,190),R(193,202),R(203,210),R(211,222),R(223,228),R(229,238),R(239,245),R(246,252),R(253,261),
     R(276,282)+[391],R(283,291)+[392],R(292,296)+R(387,390)]
ADD={'ROS-005':R(115,120),'ROS-010':[265]}
LEAVE=[68,191,192,297]+R(370,380)
plan={}
# existing folders
for e in inv['folders']:
    code=e['title']; files=[x for x in e['files']]
    ids=[x['id'] for x in files]+[idx[str(n)] for n in ADD.get(code,[])]
    keep={x['id']:int(x['title'].rsplit('-',1)[1]) for x in files if re.fullmatch(re.escape(code)+r'-\d+',x['title'])}
    others=sorted([i for i in ids if i not in keep], key=ts)
    if code=='ROS-012':  # exact duplicate of ROS-012-2 goes last
        dup=[i for i in others if meta[i]['title']=='DSC_6922 copy.jpg']; others=[i for i in others if i not in dup]+dup
    nxt=max(keep.values()) if keep else 0
    num=dict(keep)
    for i in others: nxt+=1; num[i]=nxt
    plan[code]=dict(folder_id=e['id'],new=False,photos=sorted(([dict(id=i,n=num[i],old=meta[i]['title'],dto=meta[i]['dto']) for i in ids]),key=lambda p:p['n']))
# new pieces
for k,g in enumerate(NEW):
    code=f'ROS-{23+k:03d}'; ids=sorted([idx[str(n)] for n in g],key=ts)
    plan[code]=dict(folder_id=None,new=True,photos=[dict(id=i,n=j+1,old=meta[i]['title'],dto=meta[i]['dto']) for j,i in enumerate(ids)])
leave=[dict(id=idx[str(n)],old=meta[idx[str(n)]]['title']) for n in LEAVE]
json.dump(dict(plan=plan,leave=leave),open(S+'plan.json','w'),ensure_ascii=False,indent=1)
used=sum(len(v['photos']) for v in plan.values()); allf=sum(len(e['files']) for e in inv['folders'])+len(inv['loose'])
print('pieces',len(plan),'photos placed',used,'left',len(leave),'total',used+len(leave),'expected',allf)
for c,v in plan.items(): print(c,len(v['photos']),'new' if v['new'] else '', v['photos'][0]['dto'][:10])
