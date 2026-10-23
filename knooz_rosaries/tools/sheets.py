import json,csv,os,re,subprocess,shutil
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageDraw, ImageFont, ImageOps
S='/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/'
st=json.load(open('staging.json'))
D=json.load(open(S+'local_cmp/drive_files.json'))
up={f['title']:f for f in st['files'] if f['path'].startswith('/_missing_on_drive/') and f['title']!='_manifest.csv'}
def get(fid):
    p=f'th/{fid}.jpg'
    if os.path.exists(p) and os.path.getsize(p)>2000: return p
    if os.path.exists(S+f'ros3/thumbs/{fid}.jpg'): shutil.copy(S+f'ros3/thumbs/{fid}.jpg',p); return p
    subprocess.run(['curl','-sS','-L','-o',p,f'https://lh3.googleusercontent.com/d/{fid}=w700'])
    return p
def piece_files(code):
    fs=[f for f in D if len(f['path'].split('/'))>3 and f['path'].split('/')[2]==code]
    def n(f):
        m=re.search(r'-(\d+)\.\w+$',f['title']); return int(m.group(1)) if m else 999
    return sorted(fs,key=n)
font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",20)
def sheet(name, items, T=330, COLS=5):
    ids=[i[1] for i in items]
    with ThreadPoolExecutor(12) as ex: paths=list(ex.map(get,ids))
    rows=(len(items)+COLS-1)//COLS
    im=Image.new('RGB',(COLS*T,rows*(T+26)),(35,35,35)); d=ImageDraw.Draw(im)
    for k,((label,fid),p) in enumerate(zip(items,paths)):
        try: t=ImageOps.exif_transpose(Image.open(p)).convert('RGB')
        except Exception: continue
        t.thumbnail((T-6,T-6)); x=(k%COLS)*T; y=(k//COLS)*(T+26)
        im.paste(t,(x+(T-t.width)//2,y+26+(T-t.height)//2))
        col=(255,120,120) if label.startswith('NEW') else (150,220,255)
        d.text((x+4,y+3),label[:32],fill=col,font=font)
    im.save(f'sheets/{name}.jpg',quality=82)
def new(*titles): return [('NEW '+re.sub(r'(?i)(\.jpe?g| copy)','',t),up[t]['id']) for t in titles]
def ref(code,sel=None):
    fs=piece_files(code)
    if sel: fs=[f for f in fs if any(f['title'].endswith(f'-{s}.jpg') or f['title'].endswith(f'-{s}.JPG') for s in sel)]
    return [(re.sub(r'(?i)\.jpe?g','',f['title']),f['id']) for f in fs]
loose7023=[f for f in D if f['title']=='DSC_7023 copy.jpg'][0]
C={
 'A_KS006': new('cx (67).jpg')+ref('ROS-KS-006'),
 'B_KS008': new('cx (88).JPG')+ref('ROS-KS-008'),
 'C_1582': new('DSC_1582 copy.jpg','DSC_1584 copy.jpg','DSC_1587 copy.jpg','DSC_1592 copy.jpg','DSC_1600 copy.jpg','DSC_1602 copy.jpg')+ref('ROS-021')[-6:]+ref('ROS-057')[9:14]+ref('ROS-018')[:3],
 'D_7021': new('DSC_7021 copy.jpg')+[('loose DSC_7023',loose7023['id'])]+ref('ROS-057')[:9]+ref('ROS-056')[:3],
 'E_031': new('DSC_7073.jpg','DSC_7074.jpg')+ref('ROS-031')+ref('ROS-Amb-G-053')[:2],
 'F_033': new('DSC_7592.jpg','DSC_7593.jpg','DSC_7607.jpg','DSC_7610.jpg')+ref('ROS-033'),
 'G_7821': new('DSC_7821.jpg','DSC_7823.jpg','DSC_7840.jpg','DSC_7853.jpg','DSC_7856.jpg','DSC_7865.jpg','DSC_7866.jpg','DSC_7872.jpg')+ref('ROS-B-016')[:4],
 'H_8789': new('DSC_8789.JPG','DSC_8792.JPG','DSC_8793.JPG','DSC_8796.JPG')+ref('ROS-013'),
 'I_8802': new('DSC_8802.JPG','DSC_8804.JPG','DSC_8806.JPG','DSC_8807.JPG','DSC_8809.JPG')+ref('ROS-KS-109'),
 'J_9393': new('DSC_9393.JPG','DSC_9396.JPG','DSC_9400.JPG','DSC_9403.JPG')+ref('ROS-S-004'),
 'K_9424': new('DSC_9424.JPG','DSC_9431.JPG','DSC_9432.JPG','DSC_9441.JPG')+ref('ROS-KS-112')+ref('ROS-S-004')[-2:],
 'L_DSD': new('DSD (67).jpg','DSD (68).jpg','DSD (69).jpg','JPEG image.jpg')+ref('ROS-KS-122')+ref('ROS-K-021'),
 'M_jj': new('jj (83).jpg','jj (84).jpg','jj (85).jpg','jj (86).jpg','jj (87).jpg')+ref('ROS-KS-149')+ref('ROS-022')[:2],
 'N_012': new('DSC_6749 copy.jpg','DSC_6753 copy.jpg','DSC_6754 copy.jpg','DSC_6759 copy.jpg','DSC_6760 copy.jpg','DSC_6897 copy.jpg','DSC_6898 copy.jpg','DSC_6905 copy.jpg','DSC_6906. copy.jpg','DSC_6908 copy.jpg','DSC_6909 copy.jpg','DSC_6914 copy.jpg','DSC_6921 copy.jpg')+ref('ROS-012'),
}
missing_up=[t for t in ['DSC_7079.jpg'] if t not in up]
print('not in staging:',missing_up)
for k,v in C.items(): sheet(k,v); print(k,len(v))

if __name__=='__main__' and os.environ.get('X'):
    pass
