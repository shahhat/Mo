"""Merge the five grouping passes into one piece list, apply manual decisions, assign codes.

Usage: python3 merge.py  -> writes pieces_final.json and prints a report.
Decisions live in decisions.json (edited by hand after reviewing galleries).
"""
import json, re, collections, sys

AMB = '/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/amb'
tl = json.load(open(f'{AMB}/timeline.json'))
gidx = json.load(open(f'{AMB}/gidx.json'))
inv = {v: k for k, v in gidx.items()}
byid = {e['id']: e for e in tl}
dec = json.load(open(f'{AMB}/decisions.json'))

pieces = []
for g in ['g1', 'g2', 'g3', 'g4', 'g5']:
    for p in json.load(open(f'{AMB}/group_{g}.json')):
        p['grp'] = g
        pieces.append(p)
P = {p['piece']: p for p in pieces}

# ---- merges: {"keep": "gX-NN", "absorb": ["gY-MM", ...]}
for m in dec.get('merges', []):
    k = P[m['keep']]
    for a in m['absorb']:
        q = P.pop(a)
        k['photos'] += q['photos']
        k['duplicates'] += q['duplicates']
        k['sessions'] = sorted(set(k['sessions'] + q['sessions']))
        k['notes_en'] += f" | merged {a}: {q['notes_en']}"
        pieces.remove(q)

# ---- moves of single photos between pieces: {"photo": N, "from": "gX", "to": "gY"}
for mv in dec.get('photo_moves', []):
    P[mv['from']]['photos'].remove(mv['photo'])
    P[mv['to']]['photos'].append(mv['photo'])

# ---- field overrides per piece
for pid, ov in dec.get('overrides', {}).items():
    P[pid].update(ov)

# ---- coverage check
seen = collections.defaultdict(list)
for p in pieces:
    for n in p['photos'] + p['duplicates']:
        seen[n].append(p['piece'])
missing = [n for n in range(1, len(gidx) + 1) if n not in seen]
multi = {n: v for n, v in seen.items() if len(v) > 1}
assert not missing, f'missing photos {missing}'
assert not multi, f'photos in several pieces {multi}'
for p in pieces:
    assert p['hero'] in p['photos'], (p['piece'], p['hero'])


def t0(p):
    return min(byid[inv[n]]['dto'] + f"{byid[inv[n]].get('subsec') or 0:>03}" for n in p['photos'])


# ---- codes
CAT_PREFIX = {'ST': 'AMB-ST-', 'A': 'AMB-A-', 'DEC': 'Amb-dec-'}
EXISTING_RENAME = {'Amb-S-001': 'AMB-ST-001'}
used = collections.defaultdict(set)
for p in pieces:
    ex = p.get('existing_code')
    if p['mode'] in ('existing_ok', 'add_to_existing') and ex:
        code = EXISTING_RENAME.get(ex, ex)
        p['code'] = code
        cat = 'DEC' if code.startswith('Amb-dec') else ('A' if code.startswith('AMB-A') else 'ST')
        used[cat].add(int(code[-3:]))
for p in pieces:
    if p.get('code'):
        continue
    cat = p.get('code_cat') or p['category']
    assert cat in CAT_PREFIX, (p['piece'], cat)
    p['code_cat'] = cat
nxt = {c: (max(used[c]) + 1 if used[c] else 1) for c in CAT_PREFIX}
# 1) confirmed pieces, time order  2) video-only pieces (A-number order)  3) unclassified pieces, time order
for p in sorted([p for p in pieces if not p.get('code') and not p.get('unclassified')], key=t0):
    c = p['code_cat']
    p['code'] = f"{CAT_PREFIX[c]}{nxt[c]:03d}"
    nxt[c] += 1
for v in dec.get('video_only', []):
    c = v['cat']
    q = {'piece': 'v-' + v['video'], 'mode': 'new', 'existing_code': None, 'category': c, 'code_cat': c,
         'photos': [], 'duplicates': [], 'hero': None, 'type_en': v['type_en'], 'visual_en': v['visual_en'],
         'sessions': [], 'unsure': False, 'notes_en': v.get('notes_en', ''), 'video_only': True,
         'still_path': f"{AMB}/{v['still']}", 'grp': 'video'}
    q['code'] = f"{CAT_PREFIX[c]}{nxt[c]:03d}"
    nxt[c] += 1
    pieces.append(q)
for p in sorted([p for p in pieces if not p.get('code') and p.get('unclassified')], key=t0):
    c = p['code_cat']
    p['code'] = f"{CAT_PREFIX[c]}{nxt[c]:03d}"
    nxt[c] += 1
for p in pieces:
    code = p['code']
    p['final_cat'] = 'DEC' if code.startswith('Amb-dec') else ('A' if code.startswith('AMB-A') else 'ST')
    p['t0'] = t0(p) if p['photos'] else ''
    p['unclassified'] = bool(p.get('unclassified'))

pieces.sort(key=lambda p: (p['final_cat'], p['code']))
json.dump(pieces, open(f'{AMB}/pieces_final.json', 'w'), ensure_ascii=False, indent=1)

cnt = collections.Counter((p['final_cat'], p['unclassified']) for p in pieces)
print('pieces', len(pieces), dict(cnt))
print('photos kept', sum(len(p['photos']) for p in pieces), 'dups', sum(len(p['duplicates']) for p in pieces))
for p in pieces:
    print(f"{p['code']:13} {p['piece']:9} {'U' if p['unclassified'] else ' '} n{len(p['photos']):2} d{len(p['duplicates'])} hero#{str(p['hero']):>4} {p['type_en'][:60]}")
