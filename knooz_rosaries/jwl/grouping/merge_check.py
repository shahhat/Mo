import json,sys,glob,collections,itertools
import numpy as np
J='/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/jwl'
tl=json.load(open(f'{J}/timeline.json')); byn={e['n']:e for e in tl}
H=np.load(f'{J}/dh.npy')  # index n-1
pieces=[]
for f in sorted(glob.glob(f'{J}/group_g*.json')):
    g=f.split('_')[-1][:-5]
    for p in json.load(open(f)): p['grp']=g; pieces.append(p)
seen=collections.Counter()
for p in pieces:
    for n in p['photos']+p.get('duplicates',[]): seen[n]+=1
missing=[n for n in range(1,len(tl)+1) if seen[n]==0]; dbl=[n for n,c in seen.items() if c>1]
print('pieces',len(pieces),'missing',len(missing),missing[:20],'double',dbl[:20])
print('by grp',collections.Counter(p['grp'] for p in pieces))
print('by cat',collections.Counter(p['category'] for p in pieces))
print('unsure',sum(1 for p in pieces if p.get('unsure')))
# cross-group nearest pairs
def d(a,b): return int((H[a-1]!=H[b-1]).sum())
cands=[]
for p,q in itertools.combinations(pieces,2):
    if p['grp']==q['grp']: continue
    m=min(d(a,b) for a in p['photos'] for b in q['photos'])
    if m<=40: cands.append((m,p['piece'],q['piece']))
cands.sort()
print('cross-group candidate pairs (dist<=40):',len(cands))
for c in cands[:60]: print(c)
json.dump(cands,open(f'{J}/cross_cands.json','w'))
