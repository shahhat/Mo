import json, sys, re, collections
f=sys.argv[1]; d=json.load(open(f))
banned=['انتيك','أنتيك','قديم','عيار','غرام','جرام','وزن','مصنع','ملم','مم ','بولندي','بلطيق','دومينيك','دمنكان','روسي','ألماني' if 'Amb-G' not in f else '@@','قرن','عثماني','SBM','خراطة','الأستاذ','المبدع','متحف']
for e in d:
    w=len(e['description'].split())
    flags=[b for b in banned if b in e['description']]
    if re.search(r'[0-9٠-٩]',e['description']): flags.append('digit')
    print(f"{e['code']} hero={e['hero']} words={w} flags={flags}\n  D: {e['description']}\n  N: {e.get('notes','')}\n  V: {e.get('visual','')}")
# repeated sentence fragments (5-gram)
grams=collections.Counter()
for e in d:
    t=re.sub(r'[،.]',' ',e['description']).split()
    for i in range(len(t)-4): grams[' '.join(t[i:i+5])]+=1
rep=[(g,c) for g,c in grams.items() if c>2]
print('repeated 5-grams (>2):',sorted(rep,key=lambda x:-x[1])[:15])
openers=collections.Counter(' '.join(e['description'].split()[:2]) for e in d)
print('openers:',openers.most_common(8))
