"""Round 2 sheet rows: shortened descriptions, renumbered codes, updated notes.
usage: python3 build2.py CAT            -> JSON rows [no, IMAGE, description, code, "Rosary", notes]
       python3 build2.py CAT cs         -> expected checksum strings (id|text|code) for verify
"""
import json, glob, sys, os
from rows import img
from checksum import cs
S = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

def load_batches():
    d = {}
    for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'desc/batch*.json'))):
        for e in json.load(open(f)): d[e['code']] = e
    return d

D = load_batches()
SHORT = {}
for f in sorted(glob.glob(os.path.join(S, 'short/out*.json'))):
    for e in json.load(open(f)): SHORT[e['code']] = e['description'].strip()
OVR = json.load(open(os.path.join(S, 'short/overrides.json'))) if os.path.exists(os.path.join(S, 'short/overrides.json')) else {}
MAP = json.load(open(os.path.join(S, 'ops/code_mapping.json')))

# old codes per NEW category, in new order
def old_codes():
    K = [f'ROS-K-{i:03d}' for i in range(1, 22)] + ['ROS-B-015', 'ROS-B-017']
    KS = [f'ROS-KS-{i:03d}' for i in range(1, 150)]
    SS = [f'ROS-S-{i:03d}' for i in range(1, 10)]
    B = [f'ROS-B-{i:03d}' for i in range(1, 40) if i not in (15, 17)]
    A = [f'ROS-Amb-G-{i:03d}' for i in range(1, 82) if i not in (68, 77)]
    R = [f'ROS-{i:03d}' for i in range(1, 14)]
    return {'ROS-K': K, 'ROS-KS': KS, 'ROS-S': SS, 'ROS-B': B, 'ROS-Amb-G': A, 'ROS': R}

HERO_FILE = {'ROS-KS-005': '1tiNq0vgl25hLswFzJsrn2F2kGAhD0yHT'}   # new full view (was loose cx (61))

SEMI = {'ROS-KS-005', 'ROS-KS-007', 'ROS-KS-014', 'ROS-KS-016', 'ROS-KS-020', 'ROS-KS-121'}
NOTE = {
    **{c: 'نصف صاك (قرار المالك) — الفولدر مميّز باللون البرتقالي' for c in SEMI},
    'ROS-KS-102': 'صورة واحدة فقط؛ نصف صاك (قرار المالك) — الفولدر مميّز باللون البرتقالي',
    'ROS-KS-004': 'أُضيفت صورتان كانتا متفرقتين في فولدر الفئة (004-4، 004-5)',
    'ROS-KS-008': 'أُضيفت صورة كانت متفرقة في فولدر الفئة (008-6)',
    'ROS-KS-105': 'أُضيفت صورة كانت متفرقة في فولدر الفئة (105-5)',
    'ROS-KS-109': 'أُضيفت صورتان كانتا متفرقتين في فولدر الفئة (109-3، 109-4)',
    'ROS-B-015': 'نُقلت من ROS-B-015 لعدم ظهور حشرات في الصور؛ صورتان فقط',
    'ROS-B-017': 'نُقلت من ROS-B-017 لعدم ظهور حشرات في الصور؛ صورة واحدة فقط',
    'ROS-Amb-G-066': 'صور علبة القلب (كانت ROS-Amb-G-068) أُضيفت هنا كصور 4–6؛ المسباحان ROS-Amb-G-066 و ROS-Amb-G-067 في علبة واحدة — قرّر هل يُباعان كطقم',
    'ROS-Amb-G-067': 'يُحفظ مع ROS-Amb-G-066 في علبة قلب واحدة (صور العلبة في فولدر 066)',
    'ROS-K-004': 'ختم SAiM ظاهر على قاعدة الشاهد (الصورة #1) — أُضيفت «خراطة المبدع صايم» للوصف بتأكيد المالك',
    'ROS-S-003': 'على قاعدة الشاهد ختم معدني يُقرأ RMZN وحرف مخفي تحت الحبل (الصورة #4) — توقيع خرّاط غير صايم؛ لم يُذكر في الوصف حتى يؤكد المالك صاحبه',
}
APPEND = {
    'ROS-KS-005': 'أُضيفت صورة كاملة كانت متفرقة (005-7) وأصبحت صورة العرض',
    'ROS-KS-111': 'أُضيفت صورتان كانتا متفرقتين في فولدر الفئة (111-4، 111-5)',
}

def note(old):
    n = NOTE.get(old, (D[old].get('notes') or '').strip())
    if old in APPEND: n = (n + '؛ ' if n else '') + APPEND[old]
    new = MAP.get(old, old)
    if new != old and old not in ('ROS-B-015', 'ROS-B-017'):
        n = f'الكود السابق: {old}' + ('؛ ' + n if n else '')
    return n

def desc(old):
    return OVR.get(old, SHORT.get(old, '')).strip()

def image(old):
    if old in HERO_FILE:
        return f'=IMAGE("https://drive.google.com/thumbnail?id={HERO_FILE[old]}&sz=w800")'
    hero = int(D[old].get('hero') or 1)
    try: return img(old, hero)
    except KeyError: return img(old, 1)

def rows(cat):
    out = []
    for i, old in enumerate(old_codes()[cat]):
        out.append([str(i + 1), image(old), desc(old), MAP.get(old, old), 'Rosary', note(old)])
    return out

if __name__ == '__main__':
    cat = sys.argv[1]; r = rows(cat)
    if len(sys.argv) > 2 and sys.argv[2] == 'cs':
        import re
        print(json.dumps([f"{cs(re.search(r'id=([^&]+)', x[1]).group(1))}|{cs(x[2])}|{x[3]}" for x in r]))
    else:
        print(json.dumps(r, ensure_ascii=False))
