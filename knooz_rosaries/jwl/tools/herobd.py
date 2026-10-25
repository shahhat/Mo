import json,glob,os
from PIL import Image,ImageDraw,ImageFont
J='/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/jwl'
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',15)
tl={e['n']:e for e in json.load(open(f'{J}/timeline.json'))}
P=json.load(open(f'{J}/pieces_m.json'))
os.makedirs(f'{J}/hb',exist_ok=True)
for c in ['W','B','H','R','RS','HS']:
    ps=[p for p in P if p['category']==c]
    T=230; per=48; cols=8
    for pg in range(0,len(ps),per):
        chunk=ps[pg:pg+per]; rows=(len(chunk)+cols-1)//cols
        can=Image.new('RGB',(cols*T,rows*(T+22)),'white'); d=ImageDraw.Draw(can)
        for i,p in enumerate(chunk):
            x=(i%cols)*T; y=(i//cols)*(T+22)
            im=Image.open(f"{J}/th/{tl[p['hero']]['id']}.jpg").convert('RGB'); im.thumbnail((T-4,T-4))
            can.paste(im,(x+2,y+22))
            d.text((x+3,y+2),f"{p['piece']} #{p['hero']}",fill='red',font=F)
        can.save(f'{J}/hb/{c}_{pg//per+1}.jpg',quality=82)
    print(c,len(ps))
