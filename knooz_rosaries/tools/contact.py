import os, re, json
from PIL import Image, ImageDraw, ImageFont, ImageOps
T=400; COLS=3
font=None
for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]:
    if os.path.exists(p): font=ImageFont.truetype(p,26)
def num(fn):
    m=re.search(r'-(\d+)\.jpg$',fn); return int(m.group(1)) if m else 999
os.makedirs('sheets',exist_ok=True)
for cat in sorted(os.listdir('thumbs')):
    for piece in sorted(os.listdir(f'thumbs/{cat}')):
        files=sorted(os.listdir(f'thumbs/{cat}/{piece}'), key=num)
        if not files: continue
        sel=files if len(files)<=6 else [files[0]]+[files[round(i*(len(files)-1)/5)] for i in range(1,6)]
        sel=list(dict.fromkeys(sel))
        rows=(len(sel)+COLS-1)//COLS
        cols=min(COLS,len(sel))
        sheet=Image.new('RGB',(cols*T,rows*T+40),(40,40,40))
        d=ImageDraw.Draw(sheet)
        d.text((8,6),f"{piece}  ({len(files)} photos)",fill=(255,220,120),font=font)
        for i,f in enumerate(sel):
            im=Image.open(f'thumbs/{cat}/{piece}/{f}'); im=ImageOps.exif_transpose(im).convert('RGB')
            im.thumbnail((T-6,T-6))
            x=(i%COLS)*T+(T-im.width)//2; y=40+(i//COLS)*T+(T-im.height)//2
            sheet.paste(im,(x,y))
            d.rectangle([(i%COLS)*T+4,40+(i//COLS)*T+4,(i%COLS)*T+58,40+(i//COLS)*T+38],fill=(0,0,0))
            d.text(((i%COLS)*T+8,40+(i//COLS)*T+6),f"#{num(f)}",fill=(255,255,255),font=font)
        os.makedirs(f'sheets/{cat}',exist_ok=True)
        sheet.save(f'sheets/{cat}/{piece}.jpg',quality=85)
print('done')
