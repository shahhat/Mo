import json, sys
from PIL import Image, ImageDraw, ImageFont
S='/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/ros3/'
idx=json.load(open(S+'tl/idx.json')); meta={r['id']:r for r in json.load(open(S+'meta.json'))}
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',18)
def comp(out, rows, T=380):
    W=max(len(r) for r in rows)*T; H=len(rows)*(T+26)
    C=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(C)
    for ri,r in enumerate(rows):
        for ci,n in enumerate(r):
            fid=idx[str(n)]; im=Image.open(S+'thumbs/'+fid+'.jpg').convert('RGB'); im.thumbnail((T-6,T-6))
            x=ci*T; y=ri*(T+26); C.paste(im,(x+3,y+26)); m=meta[fid]
            d.text((x+4,y+3),f"{n} {m['dto'][2:10]} {(m['piece'] or '')[-3:]}",fill='black',font=font)
    C.save(S+'cmp_'+out+'.jpg',quality=82); print(out,C.size)
if __name__=='__main__':
    out=sys.argv[1]; rows=[[int(x) for x in r.split(',')] for r in sys.argv[2:]]
    comp(out,rows)
