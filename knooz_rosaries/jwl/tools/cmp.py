# usage: cmp.py out.jpg vNN:f1,f2,.. #n1,#n2,...  (mix of video frames and photo numbers)
import sys,json
from PIL import Image,ImageDraw,ImageFont
J='/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/jwl'
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',18)
tl={e['n']:e for e in json.load(open(f'{J}/timeline.json'))}
items=[]
for a in sys.argv[2:]:
    if a.startswith('v'):
        v,fs=a.split(':')
        for f in fs.split(','): items.append((f'{v} f{int(f):03d}',f'{J}/vf/{v}/f{int(f):03d}.jpg'))
    else:
        for n in a.lstrip('#').split(','):
            n=int(n); items.append((f'#{n} {tl[n]["cat"]}',f'{J}/th/{tl[n]["id"]}.jpg'))
T=360; cols=min(5,len(items)); rows=(len(items)+cols-1)//cols
can=Image.new('RGB',(cols*T,rows*(T+24)),'white'); d=ImageDraw.Draw(can)
for i,(lab,p) in enumerate(items):
    im=Image.open(p).convert('RGB'); im.thumbnail((T-4,T-4))
    x=(i%cols)*T; y=(i//cols)*(T+24); can.paste(im,(x+2,y+24)); d.text((x+3,y+2),lab,fill='red',font=F)
can.save(sys.argv[1],quality=85)
