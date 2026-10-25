"""Build the Drive restructure plan from pieces_final.json (JWL).
Per piece: folder action, photo moves/renames (CODE-k.jpg, hero = 1, rest in shot order), duplicate moves.
Writes plan.json and ops_<k>.json batches for executor agents."""
import json,collections,sys
J='/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/jwl'
pieces=json.load(open(f'{J}/pieces_final.json'))
ids=json.load(open(f'{J}/drive_ids.json'))
tl=json.load(open(f'{J}/timeline.json')); byn={e['n']:e for e in tl}
tree=json.load(open(f'{J}/tree.json'))
path2id={e['path']:e['id'] for e in tree if e['dir']}
parent_of={e['id']:path2id[e['path'].rsplit('/',1)[0]] for e in tree if not e['dir']}
def shot_key(n):
    e=byn[n]; return (e['dto'],e.get('subsec') or 0,e.get('imgno') or 0,n)
plan=[]
for p in pieces:
    code=p['code']; cat=p['final_cat']; parent=ids['cat_folder'][cat]
    if p.get('video_only'):
        plan.append({'code':code,'folder':{'action':'create','name':code,'parent':parent},'photos':[],'dups':[],'video_only':True}); continue
    ex=p.get('existing_code')
    if ex and ex in ids['existing_piece_folder']:
        fid=ids['existing_piece_folder'][ex]
        cur=[e['path'] for e in tree if e['id']==fid][0].rsplit('/',1)[0]
        f={'action':'existing','id':fid,'rename':code}
        if path2id[cur]!=parent: f['move_to']=parent
    else:
        f={'action':'create','name':code,'parent':parent}
    order=[p['hero']]+sorted([n for n in p['photos'] if n!=p['hero']],key=shot_key)
    photos=[]
    for k,n in enumerate(order,1):
        e=byn[n]; new=f'{code}-{k}.jpg'
        photos.append({'n':n,'id':e['id'],'old_name':e['name'],'old_parent':parent_of[e['id']],'new_name':new})
    dups=[]
    for n in p.get('duplicates',[]):
        e=byn[n]; dest=ids['dup_folder'][cat]
        dups.append({'n':n,'id':e['id'],'name':e['name'],'old_parent':parent_of[e['id']],'dest':dest,'move':parent_of[e['id']]!=dest})
    plan.append({'code':code,'folder':f,'photos':photos,'dups':dups})
json.dump(plan,open(f'{J}/plan.json','w'),ensure_ascii=False,indent=1)
# batches of ~40 pieces for executors
nb=int(sys.argv[1]) if len(sys.argv)>1 else 6
k=0; per=(len(plan)+nb-1)//nb
for i in range(0,len(plan),per):
    k+=1; json.dump(plan[i:i+per],open(f'{J}/ops_{k}.json','w'),ensure_ascii=False,indent=1)
c=collections.Counter()
for q in plan:
    c['folders_'+q['folder']['action']]+=1; c['photos']+=len(q['photos']); c['dups']+=len(q['dups'])
print(dict(c),'batches',k)
