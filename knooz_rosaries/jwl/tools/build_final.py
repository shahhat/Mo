import json,re,sys,collections
J='/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/jwl'
sys.path.insert(0,J); from captions_fixed import CAP
P=json.load(open(f'{J}/pieces_m.json')); tl={e['n']:e for e in json.load(open(f'{J}/timeline.json'))}
owner=json.load(open(f'{J}/owner_codes.json')); M=json.load(open(f'{J}/vm/all_matches.json'))
vrows=json.load(open(f'{J}/vsheet_rows.json')); pick={p['v']:p for p in json.load(open(f'{J}/vid_pick.json'))}
D={}
for k in range(1,8):
    for e in json.load(open(f'{J}/desc/out_d{k}.json')): D[e['code']]=e
assert len(D)==len(P),(len(D),len(P))
def shot_key(n):
    e=tl[n]; return (e['dto'],e.get('subsec') or 0,e.get('imgno') or 0,n)
PREF={'W':'JWL-W','B':'JWL-B','H':'JWL-H','R':'JWL-R','RS':'JWL-RS','HS':'JWL-HS'}
# videos per piece
vid_of=collections.defaultdict(list)
for v,e in M.items():
    if e.get('piece'): vid_of[e['piece']].append(v)
VONLY={'v01':'RS','v11':'HS','v15':'W','v16':'W','v17':'W','v23':'RS','v24':'B','v27':'W','v28':'W','v29':'W','v30':'B','v32':'HS','v33':'W','v35':'RS','v36':'W','v38':'RS','v39':'W','v40':'H'}
VONLY_IC={'v01':'Ring','v11':'Ring','v15':'Pendant','v16':'Pendant','v17':'Engraved Stone','v23':'Ring','v24':'Ring','v27':'Pendant','v28':'Engraved Stone','v29':'Necklace','v30':'Ring','v32':'Ring','v33':'Pendant','v35':'Ring','v36':'Engraved Stone','v38':'Ring','v39':'Engraved Stone','v40':'Ring'}
SAME={'v31':'v37','v34':'v38'}
SPECIAL={'g7-21':'تنبيه: النص على الفيديو يقول «قلادة» والقطعة سوار (اسم ملف الفيديو BRACELET)، والنص مُبقى كما كتبه أبو علي.',
 'g1-54':'الفيديو يسمّي الحجر تورمالين؛ من الصور يبدو أحمر داكناً ولم يُتحقق من نوعه.',
 'g2-40':'خاتم نسائي حديث الطراز؛ مُبقى في قسم RS كما صنّفه المالك.',
 'g6-12':'',
 'g7-07':'نص أبو علي في شيت الفيديو (Phase 09) يذكر القرن الثاني عشر «على الأغلب»؛ النص على الفيديو حذف كلمة «على الأغلب».',
 'g7-25':'صور القطعة كانت في مجلدَي HS وRS (ملفات R005)، واعتُمد قسم HS لأن فيديو الخاتم ينسبه للأستاذ مهدي جدي.'}
SPECIAL={k:v for k,v in SPECIAL.items() if v}
REPL=[('ولم يُسمَّ لعدم اليقين','ولم يُتحقق من نوعه'),('ولم يُسمَّ','ولم يُتحقق من نوعه'),('فلا يُسمّى فيروزاً','فليس فيروزاً'),
 ('لكنه لا يُسمّى دون إثبات','ولم يُتحقق من نوعه'),
 ('أُبقي في الخواتم النادرة فلم يُذكر صانع.','أُبقي في قسم الخواتم النادرة كما صنّفه المالك.'),
 ('صُوّر ضمن سلسلة حسين جدي لكنه مصنّف في الخواتم النادرة، فلم يُذكر صانع.','صُوّر ضمن سلسلة خواتم حسين جدي، لكنه مصنّف عند المالك في الخواتم النادرة.'),
 ('، لكن القطعة في الخواتم النادرة فلم يُذكر صانع.','، والقطعة مصنّفة عند المالك في الخواتم النادرة.'),
 ('بحسب المنسّق بقي الخاتم في فئة الخواتم النادرة المنوعة (RS) لأن صور الواجهة محفوظة هناك، والعلامة لا تثبت نسبته، فلم يُذكر الصانع؛','بقي الخاتم في قسم الخواتم النادرة لأن صور الواجهة محفوظة هناك، ودمغة F مع الخراطيش البيضاوية تظهر أيضاً على خواتم هذا القسم؛')]   # Phase 08 edit -> Phase 09 Final edit (caption used)
# order and codes
items=[]
for p in P:
    items.append({'piece':p['piece'],'cat':p['category'],'key':min(shot_key(n) for n in p['photos']),'p':p})
codes={}
for c in PREF:
    ps=sorted([i for i in items if i['cat']==c],key=lambda i:i['key'])
    for k,i in enumerate(ps,1): codes[i['piece']]=f'{PREF[c]}-{k:03d}'
    vo=[v for v in sorted(VONLY) if VONLY[v]==c]
    for j,v in enumerate(vo,len(ps)+1): codes[v]=f'{PREF[c]}-{j:03d}'
# owner code -> new code (for cross references)
oc2code={}
for pc,lst in owner.items():
    for o in lst: oc2code.setdefault(o,[]).append(codes[pc])
def src_label(v):
    s=re.sub(r'\s*\+\s*Logo( v2| 02)?','',pick[v]['src'].replace('.mp4',''))
    s=re.sub(r'\s+',' ',s).replace('/',' – ',1).replace(' – -',' – ').strip()
    return s
def fix_refs(txt,self_piece):
    def rp(m):
        g=m.group(0); return codes.get(g,g) if g!=self_piece else 'هذه القطعة'
    txt=re.sub(r'\bg\d-\d\d\b',rp,txt)
    def ro(m):
        o=m.group(0); tgt=[c for c in oc2code.get(o,[]) if c!=codes.get(self_piece)]
        mine=codes.get(self_piece) in oc2code.get(o,[])
        if tgt and not mine: return f'{"/".join(sorted(set(tgt)))} ({o})'
        return o
    txt=re.sub(r'\b(JWL-00\d\d|R0\d\d)\b',ro,txt)
    txt=txt.replace('صورة الدمغات كانت في مجلد أبناء حسين جدي، والمنسق اعتمد الفئة H.','صورة الدمغات كانت في مجلد أبناء حسين جدي، واعتُمد قسم H لأن صورتين من الثلاث فيه.')
    txt=txt.replace('دمج المنسق ملفي المالك JWL-0045 وJWL-0046.','دُمج ملفا المالك JWL-0045 وJWL-0046 لأنهما الخاتم نفسه.')
    txt=txt.replace('المنسق','المراجعة').replace('المنسّق','المراجعة')
    return txt
rows=[]
for i in items:
    pc=i['piece']; p=i['p']; d=D[pc]; code=codes[pc]
    vids=sorted(vid_of.get(pc,[]))
    notes=[]
    if vids:
        cv=[SAME.get(v,v) for v in vids]; cv=sorted(set(cv)); assert len(cv)==1,(pc,vids)
        desc=CAP[cv[0]]
        labs='، '.join(src_label(v) for v in vids)
        notes.append(f'الوصف هو النص المكتوب على فيديو أبو علي ({src_label(cv[0])}) حرفياً، بتصحيح إملائي فقط. نسخة الفيديو في فولدر القطعة: {code}-video.mp4.')
        if len(vids)>1: notes.append(f'للقطعة نسختان من الفيديو: {labs}؛ الوصف من نسخة Phase 09 (Final).')
        conf=[M[v].get('confidence') for v in vids]
        if 'medium' in conf: notes.append('مطابقة الفيديو بالقطعة قائمة على الصياغة (الحجر سادة بلا علامات مميزة).')
        ic=d['item_category']
    else:
        desc=d['description']; ic=d['item_category']
    raw=(d.get('notes','') or '').replace('JWL-0036/0037','JWL-0036').replace(' (garnet)','')
    if vids:  # describer remarks about naming/category/possible video match are superseded by the video text
        parts=re.split(r'(?<=[.؛])\s*',raw)
        raw=' '.join(x for x in parts if x.strip() and not re.search(r'فيديو|v\d\d|يُسمَّ|يُسمّى|الفئة|فئة|الصانع|يُذكر|حديث الطراز|يُنقل إلى',x)).strip()
        raw=raw.rstrip('؛ ')+('.' if raw and not raw.endswith('.') else '')
    for a,b in REPL: raw=raw.replace(a,b)
    dn=fix_refs(raw,pc).strip()
    if pc in SPECIAL: notes.append(SPECIAL[pc])
    if dn: notes.append(dn)
    oc=[o for o in owner.get(pc,[])]
    if oc and not any(o in dn for o in oc): notes.append('الأكواد القديمة: '+'، '.join(oc)+'.')
    rows.append({'code':code,'cat':i['cat'],'piece':pc,'hero':d['hero'] if not vids else p['hero'],'desc':desc,'ic':ic,'notes':' '.join(notes),
                 'photos':p['photos'],'duplicates':p.get('duplicates',[]),'existing_code':p.get('existing_code'),'videos':vids,'video_only':False})
for v,c in VONLY.items():
    code=codes[v]; vids=[v]+[k for k,t in SAME.items() if t==v]
    notes=[f'قطعة معروفة من الفيديو فقط ولا توجد لها صور في جلسة التصوير. الوصف هو النص المكتوب على فيديو أبو علي ({src_label(v)}) حرفياً، بتصحيح إملائي فقط. الصور {code}-1..3 لقطات من الفيديو، ونسخة الفيديو {code}-video.mp4.']
    if len(vids)>1: notes.append('للقطعة نسختان من الفيديو: '+'، '.join(src_label(x) for x in sorted(vids))+'؛ الوصف من نسخة Phase 09 (Final).')
    rows.append({'code':code,'cat':c,'piece':v,'hero':None,'desc':CAP[v],'ic':VONLY_IC[v],'notes':' '.join(notes),'photos':[],'duplicates':[],'existing_code':None,'videos':sorted(vids),'video_only':True})
# QC round (qc/qc_qc1..3.json): accepted fixes, applied by code
QC=[]
for f in ('qc_qc1','qc_qc2','qc_qc3'): QC+=json.load(open(f'{J}/qc/{f}.json'))
ACCEPT={('JWL-W-014','desc'),('JWL-W-032','desc'),('JWL-W-032','notes'),('JWL-H-029','desc'),('JWL-B-008','desc'),('JWL-B-030','desc'),
        ('JWL-HS-037','desc'),('JWL-HS-082','desc'),('JWL-HS-076','notes'),('JWL-HS-079','notes')}
QC_FIX={}
for e in QC:
    if (e['code'],e['field']) in ACCEPT and e['fix']: QC_FIX[(e['code'],e['field'])]=e['fix']
assert len(QC_FIX)==len(ACCEPT),(len(QC_FIX),ACCEPT-set(QC_FIX))
VO_EXTRA={'v17':'نص أبو علي في شيت الفيديو يضيف: «لمطلع القرن الثالث هجري».',
          'v24':'نص أبو علي في شيت الفيديو يبدأ «خاتم متحفي» ويضيف «قطعة بمتحف»؛ المعتمد هنا هو النص على الفيديو.',
          'v39':'رمز المالك لهذا الفيديو في شيت الفيديو: AMB1 (حجر عقيق، ليس كهرماناً).','v40':'رمز المالك لهذا الفيديو في شيت الفيديو: RING-1.',
          'v33':'اسم الفيديو في شيت الفيديو: R020.','v27':'اسم الفيديو في شيت الفيديو: R021.'}
for r in rows:
    for fld,key in (('desc','desc'),('notes','notes')):
        if (r['code'],fld) in QC_FIX:
            new=QC_FIX[(r['code'],fld)]
            if fld=='notes':
                oc=[o for o in owner.get(r['piece'],[]) if o not in new and r['code'] not in ('JWL-HS-076','JWL-HS-079')]
                if oc: new+=' الأكواد القديمة: '+'، '.join(oc)+'.'
            r[key]=new
    if r['video_only'] and r['piece'] in VO_EXTRA: r['notes']+=' '+VO_EXTRA[r['piece']]
# Restyle round (29 Oct): owner rule - our texts as close as possible to Abu Ali's way (restyle/out_r1..3.json)
RESTYLE={}
for k in ('r1','r2','r3'):
    for e in json.load(open(f'{J}/restyle/out_{k}.json')): RESTYLE[e['code']]=e['description']
for r in rows:
    if not r['videos']: r['desc']=RESTYLE[r['code']]
assert len(RESTYLE)==sum(1 for r in rows if not r['videos'])
B030='قراءة جزئية للنقش: «… على الله» مؤكدة، والكلمة الأولى قد تكون «التوكل» أو «توكلت» (؟).'
for r in rows:
    if r['code']=='JWL-B-030' and B030 not in r['notes']: r['notes']=(B030+' '+r['notes']).strip()
rows.sort(key=lambda r:(list(PREF).index(r['cat']),r['code']))
json.dump(rows,open(f'{J}/catalog_rows.json','w'),ensure_ascii=False,indent=1)
json.dump(codes,open(f'{J}/codes.json','w'),ensure_ascii=False,indent=1)
print(collections.Counter(r['cat'] for r in rows), len(rows), 'video pieces',sum(1 for r in rows if r['videos']))
