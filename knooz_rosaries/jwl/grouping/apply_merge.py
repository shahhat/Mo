import json,glob,re
J='/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/jwl'
P=[]
for f in sorted(glob.glob(f'{J}/group_g*.json')): P+=json.load(open(f))
byid={p['piece']:p for p in P}
MERGE=[('g1-28','g2-08','re-shoot in S06 (#262/263), confirmed by g1 and g2'),
       ('g1-46','g2-03','re-shoot in S06 (#255/256); lead compared engraving at high res (rotated) - same stone'),
       ('g1-48','g2-07','re-shoot in S06 (#261)'),
       ('g1-50','g2-06','re-shoot in S06 (#259/260)'),
       ('g1-52','g2-04','re-shoot in S06 (#257)'),
       ('g1-53','g2-02','re-shoot in S06 (#251-254)'),
       ('g1-56','g2-05','re-shoot in S06 (#258)'),
       ('g1-47','g2-01','#250 (file DSC_2304, right after #208 DSC_2303) is a view through the shank of this ring: same gold-tone fluted mount; it shows the reverse of the stone')]
for a,b,why in MERGE:
    A,B=byid[a],byid.pop(b)
    A['photos']=sorted(set(A['photos'])|set(B['photos'])); A['duplicates']=sorted(set(A.get('duplicates',[]))|set(B.get('duplicates',[])))
    A['sessions']=sorted(set(A.get('sessions',[]))|set(B.get('sessions',[])))
    A['notes_en']=(A.get('notes_en','')+f' | MERGED {b}: {why}.').strip(' |')
    A['merged_from']=A.get('merged_from',[])+[b]
# decisions on unsure
DEC={'g1-03':'COORDINATOR: front/back pairing accepted (consecutive frames, same bail).',
 'g1-05':'COORDINATOR: front/back pairing accepted (consecutive frames, identical bail).',
 'g2-31':'COORDINATOR: one ring; owner file names JWL-0056 and JWL-0057 both show it.',
 'g2-37':'COORDINATOR: grouping accepted.',
 'g3-30':'COORDINATOR: H accepted (2 of 3 photos in H; #550 was filed in HS).',
 'g3-34':'COORDINATOR: merge of owner codes JWL-0045 + JWL-0046 accepted.',
 'g4-22':'COORDINATOR: kept in RS (front photos filed in RS; the F + oval-cartouche hallmark also occurs on RS rings, so it does not prove HS). Do not name a maker.',
 'g5-13':'COORDINATOR: RS accepted; #859 (file JWL-0053-1 in H) is its hallmark.',
 'g5-18':'COORDINATOR: treated as ONE pendant shown front and back (single photo).',
 'g7-27':'COORDINATOR: kept in RS (owner filing); hallmark resembles the H set. Do not name a maker.'}
P2=[]
for p in P:
    if p['piece'] not in byid: continue
    if p['piece'] in DEC:
        p['notes_en']=(p.get('notes_en','')+' | '+DEC[p['piece']]).strip(' |'); p['unsure']=False
    P2.append(p)
json.dump(P2,open(f'{J}/pieces_m.json','w'),ensure_ascii=False,indent=1)
print(len(P2))
