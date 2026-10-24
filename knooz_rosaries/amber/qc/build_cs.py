"""Build one QC contact sheet per catalog row: every photo in the piece folder (live Drive tree),
sheet image outlined in red, plus the owner's video-sheet image and video frames when the piece has a video."""
import json, re, os
from PIL import Image, ImageDraw, ImageFont, ImageOps
AMB = '/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/amb'
os.chdir(AMB)
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)
big = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 22)
tree = json.load(open('qc/tree_now.json'))
pay = json.load(open('sheet_payload_r7.json'))
VID = {'AMB-A-050': ['A003'], 'AMB-ST-024': ['A009'], 'Amb-dec-007': ['A012'], 'AMB-A-084': ['A014'],
       'Amb-dec-008': ['A016'], 'Amb-dec-049': ['A017'], 'AMB-A-015': ['A021'], 'Amb-dec-003': ['phase12'],
       'AMB-A-102': ['A001'], 'AMB-A-103': ['A002'], 'AMB-A-104': ['A004'], 'AMB-A-105': ['A013'],
       'AMB-A-106': ['A015'], 'AMB-A-107': ['A020'], 'AMB-A-057': ['AmberFaces']}
FR = {'A003': 'av04', 'A009': 'av09', 'A012': 'av10', 'A014': 'av12', 'A016': 'av14', 'A017': 'av15', 'A021': 'av17',
      'phase12': 'av00', 'A001': 'av02', 'A002': 'av03', 'A004': 'av05', 'A013': 'av11', 'A015': 'av13', 'A020': 'av16'}


def local(fid):
    for p in (f'th/{fid}.jpg', f'r7/dl/{fid}.jpg'):
        if os.path.exists(p):
            return p
    return None


def nkey(name):
    m = re.search(r'-(\d+)\.\w+$', name)
    return int(m.group(1)) if m else 999


T = 300
items = []
for o in pay:
    for i, r in enumerate(o['values']):
        code = r[3]
        sid = re.search(r'id=([^&"]+)', r[1]).group(1)
        files = [e for e in tree if not e['dir'] and e['path'].split('/')[-2] == code
                 and re.search(r'\.(jpe?g|png)$', e['path'], re.I)]
        files.sort(key=lambda e: nkey(e['path']))
        tiles = []
        for e in files:
            name = e['path'].split('/')[-1]
            p = local(e['id'])
            if p is None and code in VID:
                v = VID[code][0]
                p = f'simg/{v}.png' if os.path.exists(f'simg/{v}.png') else f'simg/{v}.jpg'
            tiles.append((name, p, e['id'] == sid))
        for v in VID.get(code, []):
            p = f'simg/{v}.png' if os.path.exists(f'simg/{v}.png') else f'simg/{v}.jpg'
            if os.path.exists(p):
                tiles.append((f'VIDEO-SHEET {v}', p, False))
        cols = min(4, max(1, len(tiles)))
        rows = (len(tiles) + cols - 1) // cols
        sh = Image.new('RGB', (cols * (T + 10) + 10, rows * (T + 34) + 50), (245, 245, 245))
        d = ImageDraw.Draw(sh)
        d.text((10, 10), f"{o['tab'].encode('ascii','replace').decode()}  row {i+2}  {code}  ({len(files)} photos)", fill=(0, 0, 0), font=big)
        for k, (name, p, is_sheet) in enumerate(tiles):
            x = 10 + (k % cols) * (T + 10); y = 50 + (k // cols) * (T + 34)
            if p and os.path.exists(p):
                im = ImageOps.contain(Image.open(p).convert('RGB'), (T, T))
                sh.paste(im, (x + (T - im.width) // 2, y + (T - im.height) // 2))
            else:
                d.text((x + 10, y + 140), 'NO LOCAL IMAGE', fill=(200, 0, 0), font=font)
            if is_sheet:
                d.rectangle([x - 4, y - 4, x + T + 3, y + T + 3], outline=(230, 0, 0), width=5)
            d.text((x, y + T + 6), (name + ('  <SHEET IMAGE>' if is_sheet else '')), fill=(200, 0, 0) if is_sheet else (0, 0, 0), font=font)
        sh.save(f'qc/cs/{code}.jpg', quality=82)
        frames = [f'vframes/{FR[v]}_sheet.jpg' for v in VID.get(code, []) if v in FR]
        items.append({'tab': o['tab'], 'row': i + 2, 'code': code, 'sheet_image_id': sid,
                      'sheet_image_file': next((n for n, p, s in tiles if s), None),
                      'photos': [n for n, p, s in tiles if not n.startswith('VIDEO')],
                      'contact_sheet': f'{AMB}/qc/cs/{code}.jpg',
                      'video_frames': [f'{AMB}/{f}' for f in frames],
                      'description': r[2], 'item_name': r[3], 'category': r[4], 'notes': r[6],
                      'unc_suggest': r[7] if len(r) > 7 else '', 'unc_question': r[8] if len(r) > 8 else ''})
json.dump(items, open('qc/items.json', 'w'), ensure_ascii=False, indent=1)
print(len(items), 'contact sheets')
print('rows whose sheet image is not in folder:', [x['code'] for x in items if not x['sheet_image_file']])
print('no-photo rows:', [x['code'] for x in items if not x['photos']])
