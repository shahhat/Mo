import json,os
from PIL import Image,ImageDraw,ImageFont
J='/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/jwl'
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',18)
tl={e['n']:e for e in json.load(open(f'{J}/timeline.json'))}
P=json.load(open(f'{J}/pieces_m.json'))
owner=json.load(open(f'{J}/owner_codes.json'))
items={}
for p in P:
    ph=[p['hero']]+[n for n in sorted(p['photos']) if n!=p['hero']]
    T=400; cols=min(4,len(ph)); rows=(len(ph)+cols-1)//cols
    can=Image.new('RGB',(cols*T,rows*(T+24)),'white'); d=ImageDraw.Draw(can)
    for i,n in enumerate(ph):
        im=Image.open(f"{J}/th/{tl[n]['id']}.jpg").convert('RGB'); im.thumbnail((T-4,T-4))
        x=(i%cols)*T; y=(i//cols)*(T+24); can.paste(im,(x+2,y+24)); d.text((x+3,y+2),f"#{n}"+(' HERO' if n==p['hero'] else ''),fill='red',font=F)
    sp=f"{J}/desc/ps/{p['piece']}.jpg"; can.save(sp,quality=82)
    notes=p.get('notes_en','')
    if owner.get(p['piece']): notes+=f" | Owner's old codes: {', '.join(owner[p['piece']])}."
    items[p['piece']]={'code':p['piece'],'category':p['category'],'suggested_hero':p['hero'],'sheet':sp,
        'photos':[{'n':n,'drive_id':tl[n]['id']} for n in ph],
        'type_en':p.get('type_en',''),'visual_en':p.get('visual_en',''),'facts_en':p.get('facts_en',''),'notes_en':notes.strip(' |')}
json.dump(items,open(f'{J}/desc/items_all.json','w'),ensure_ascii=False,indent=1)
# batches
order={'HS':0,'RS':1,'H':2,'B':3,'R':4,'W':5}
by={}
for p in P: by.setdefault(p['category'],[]).append(p['piece'])
B={'d1':by['HS'][:48],'d2':by['HS'][48:],'d3':by['RS'][:46],'d4':by['RS'][46:],'d5':by['H'],'d6':by['B']+by['R'],'d7':by['W']}
assert sum(len(v) for v in B.values())==len(P)
for k,v in B.items():
    json.dump([items[c] for c in v],open(f'{J}/desc/in_{k}.json','w'),ensure_ascii=False,indent=1)
    print(k,len(v))
