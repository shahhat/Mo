import json,re
pieces={p['code']:p for p in json.load(open('pieces_final.json'))}
plan={q['code']:q for q in json.load(open('plan.json'))}
desc=json.load(open('desc_all.json'))
facts=json.load(open('vsheet_facts.json'))
dec=json.load(open('decisions.json'))
still_ids={'AMB-A-102':'1OthGaS03rphwoFHYryRna_hb50UytVFx','AMB-A-103':'17qJJ_68DfLjiNq8uSyVdhEp2dZU4wfcA','AMB-A-104':'1uchUUa6qLv5ERpdMRhKYLX1sQ904FK4g',
 'AMB-A-105':'1fsPYpM4oNYdf_caxqJaSJkkF2kDjQyKk','AMB-A-106':'1WxH5vQDhC5s8pci26nUMV6vC5FaShAtz','AMB-A-107':'10QYPyw9pmgIFQfYeZKGlZPcdaK18oqW7'}
CATMAP={'Amber Sculpture':'Amber Figurine','Amber Statue':'Amber Figurine','Amber Ornament':'Amber Desk Ornament'}
# video links: code -> (video key, copied file title, sheet ref)
vlink={'AMB-A-050':'A003','AMB-ST-024':'A009','Amb-dec-007':'A012','AMB-A-084':'A014','Amb-dec-008':'A016','Amb-dec-049':'A017','AMB-A-015':'A021',
       'AMB-A-102':'A001','AMB-A-103':'A002','AMB-A-104':'A004','AMB-A-105':'A013','AMB-A-106':'A015','AMB-A-107':'A020'}
def vref(k):
    f=facts[k]; return f"{f['tab']} – {f['file']}"
src_name={'(loose)':'صوراً متفرقة','كهرمان وانتيكات':'في فولدر «كهرمان وانتيكات»'}
tl={e['id']:e for e in json.load(open('timeline.json'))}
rows={}
for code,p in pieces.items():
    d=desc[code]; q=plan[code]
    hero=d['hero']
    if p.get('video_only'):
        hid=still_ids[code]
    else:
        m={int(x['new_name'].rsplit('-',1)[1].split('.')[0]):x['id'] for x in q['photos']}
        hid=m.get(hero) or m[min(m)]
    an=d.get('notes','').strip()
    if code in vlink or code in ('Amb-dec-003','AMB-A-057'):
        segs=[x.strip() for x in re.split(r'[؛;]',an) if x.strip()]
        segs=[x for x in segs if not ('لها فيديو بلا صور' in x or ('شيت الفيديو' in x and 'لم ت' not in x))]
        an='؛ '.join(segs)
    notes=[an] if an else []
    if code in vlink:
        k=vlink[code]
        if p.get('video_only'):
            notes.append(f"قطعة لها فيديو بلا صور (الفولدر أحمر): {code}-video.mp4 — الصورة لقطة مؤقتة من صورة شيت الفيديو، ويلزم تصويرها. نص شيت الفيديو ({vref(k)}): «{facts[k]['text']}».")
        else:
            notes.append(f"لها فيديو (الفولدر أخضر): {code}-video.mp4. نص شيت الفيديو ({vref(k)}): «{facts[k]['text']}».")
    if code=='AMB-A-103': notes.append('توجد مسودة فيديو لنفس القطعة «ANTIQUE MERMAID + Logo» في Phase 06/Drafts (لم تُنسخ).')
    if code=='AMB-A-104': notes.append('توجد مسودة فيديو لنفس العقد «Broush (Rosary) - Draft» في Phase 06/Drafts (لم تُنسخ).')
    if code=='Amb-dec-003': notes.append('لها فيديو (الفولدر أخضر): Amb-dec-003-video.mp4 من «phase 12 -photo/من_تحف_الكهرمان_المنحوتة» (النسخة الأعلى جودة؛ توجد نسخة أخف بنفس الاسم لم تُنسخ). لا يوجد لها صف في شيت الفيديو.')
    if code=='AMB-A-057': notes.append(f"في شيت الفيديو صف ({vref('AmberFaces')}) بنص: «{facts['AmberFaces']['text']}»، ولا يوجد له ملف فيديو في فولدر الفيديوهات.")
    if p.get('move_note') and not any(k in an for k in ('نُقلت','صُنّفت','AMB-A')): notes.append(p['move_note'])
    if not p.get('video_only') and p['mode']=='new':
        locs={tl[x['id']]['loc'] for x in q['photos']}
        cats={tl[x['id']]['cat'] for x in q['photos']}
        if 'كهرمان وانتيكات' in locs: notes.append('كانت في فولدر «كهرمان وانتيكات» داخل الأحجار.')
        if p['final_cat']=='DEC' and 'DEC' not in cats: notes.append('مصنّفة منحوتة (كانت ضمن الأحجار).')
    cat=CATMAP.get(d['item_category'],d['item_category'])
    rows[code]={'no':str(int(code[-3:])),'img':f'=IMAGE("https://drive.google.com/thumbnail?id={hid}&sz=w800")','desc':d['description'],'code':code,'cat':cat,'notes':' '.join(notes),
                'final_cat':p['final_cat'],'unc':p['unclassified'],'unc_suggest':p.get('unc_suggest',''),'unc_question':p.get('unc_question',''),'unc_reason':p.get('unc_reason','')}
# g2-16 question placeholder
for r in rows.values():
    r['unc_question']=r['unc_question'].replace('{NEXT}','AMB-ST-014')
    if r['unc'] and r['unc_reason'] and 'غير مصنف' not in r['notes']:
        r['notes']=('سبب وضعها في غير مصنف: '+r['unc_reason']+' '+r['notes']).strip()
json.dump(rows,open('rows.json','w'),ensure_ascii=False,indent=1)
import collections
print(collections.Counter((r['final_cat'],r['unc']) for r in rows.values()))
for c in ['AMB-A-015','AMB-A-102','AMB-ST-028','Amb-dec-003','AMB-ST-005']: print(c,json.dumps(rows[c],ensure_ascii=False)[:900],'\n')
