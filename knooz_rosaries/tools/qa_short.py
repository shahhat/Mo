import json, glob, re, sys, collections
orig={}
for i in (1,2,3):
    try:
        for e in json.load(open(f'short/in{i}.json')): orig[e['code']]=e
    except FileNotFoundError: pass
def norm(w):
    w=re.sub(r'[ً-ْـ]','',w)  # strip harakat/tatweel
    w=re.sub(r'^[وفبكل]?(ال)?','',w) if len(w)>4 else w
    return w.strip('،.؛:«»()')
STOP=set('من في على مع إلى الى عن او أو ثم التي الذي هذه هذا كل بين حتى قد كما بها به لها له ما لا'.split())
outs=[]
for f in sorted(glob.glob('short/out*.json')): outs+=json.load(open(f))
issues=0; wc=[]
for e in outs:
    o=orig[e['code']]; src=o['description']+' '+o['special']
    so=set(norm(w) for w in re.findall(r'\S+',src))
    new=[w for w in re.findall(r'\S+',e['description']) if norm(w) not in so and norm(w) not in STOP and len(norm(w))>2]
    n=len(e['description'].split()); wc.append(n)
    if new or n>30 or n<18:
        issues+=1; print(e['code'],n,'NEW:',new)
print('checked',len(outs),'flagged',issues,'words min/mean/max',min(wc),sum(wc)/len(wc),max(wc))
op=collections.Counter(e['description'].split()[0] for e in outs); print(op.most_common(6))
