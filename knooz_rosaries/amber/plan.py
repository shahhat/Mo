"""Build the Drive restructure plan from pieces_final.json.

Per piece: folder action, photo moves/renames (final names CODE-k.jpg), duplicate moves.
Writes plan.json and ops_<k>.json batches for executor agents.
"""
import json, re, collections

AMB = '/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/amb'
pieces = json.load(open(f'{AMB}/pieces_final.json'))
ids = json.load(open(f'{AMB}/drive_ids.json'))
gidx = json.load(open(f'{AMB}/gidx.json'))
inv = {v: k for k, v in gidx.items()}
tl = json.load(open(f'{AMB}/timeline.json'))
byid = {e['id']: e for e in tl}
tree = json.load(open(f'{AMB}/tree.json'))
folder_id = {e['path'].rsplit('/', 1)[1]: e['id'] for e in tree if e['dir']}
parent_of = {}
path2id = {e['path']: e['id'] for e in tree if e['dir']}
for e in tree:
    if not e['dir']:
        parent_of[e['id']] = path2id[e['path'].rsplit('/', 1)[0]]


def shot_key(n):
    e = byid[inv[n]]
    return (e['dto'], e.get('subsec') or 0, e.get('imgno') or 0, n)


def final_order(p):
    """Return list of (n, k) with final number k for every kept photo."""
    code = p['code']
    if code.startswith('Amb-dec') and p['mode'] in ('existing_ok', 'add_to_existing'):
        out, used = [], set()
        extra = []
        for n in p['photos']:
            m = re.match(r'Amb-dec-(\d{3})-(\d+)\.', byid[inv[n]]['name'])
            if m and m.group(1) == code[-3:]:
                out.append((n, int(m.group(2))))
                used.add(int(m.group(2)))
            else:
                extra.append(n)
        k = max(used) if used else 0
        for n in sorted(extra, key=shot_key):
            k += 1
            out.append((n, k))
        return sorted(out, key=lambda t: t[1])
    rest = sorted([n for n in p['photos'] if n != p['hero']], key=shot_key)
    return [(n, k + 1) for k, n in enumerate([p['hero']] + rest)]


def target_parent(p):
    return ids['unclassified_folder'] if p['unclassified'] else ids['cat_folder'][p['final_cat']]


plan = []
for p in pieces:
    code = p['code']
    if p.get('video_only'):
        plan.append({'code': code, 'folder': {'action': 'create', 'name': code, 'parent': target_parent(p)},
                     'photos': [], 'dups': [], 'video_only': True})
        continue
    ex = p.get('existing_code')
    if ex and ex in folder_id:
        fid = folder_id[ex]
        cur_parent = path2id[[e['path'] for e in tree if e['id'] == fid][0].rsplit('/', 1)[0]]
        f = {'action': 'existing', 'id': fid}
        if ex != code:
            f['rename'] = code
        if cur_parent != target_parent(p):
            f['move_to'] = target_parent(p)
    else:
        f = {'action': 'create', 'name': code, 'parent': target_parent(p)}
    photos = []
    for n, k in final_order(p):
        fid_ = inv[n]
        e = byid[fid_]
        new = f'{code}-{k}.jpg'
        photos.append({'n': n, 'id': fid_, 'old_name': e['name'], 'old_parent': parent_of[fid_],
                       'new_name': new, 'rename': e['name'] != new})
    dups = []
    for n in p['duplicates']:
        fid_ = inv[n]
        e = byid[fid_]
        dest = ids['dup_folder'][p['final_cat']]
        dups.append({'n': n, 'id': fid_, 'name': e['name'], 'old_parent': parent_of[fid_], 'dest': dest,
                     'move': parent_of[fid_] != dest})
    plan.append({'code': code, 'folder': f, 'photos': photos, 'dups': dups})

json.dump(plan, open(f'{AMB}/plan.json', 'w'), ensure_ascii=False, indent=1)
c = collections.Counter()
for q in plan:
    c['folders_' + q['folder']['action']] += 1
    c['photo_ops'] += sum(1 for x in q['photos'] if x['rename'] or x['old_parent'] != q['folder'].get('id'))
    c['dup_moves'] += sum(1 for x in q['dups'] if x['move'])
print(dict(c))
