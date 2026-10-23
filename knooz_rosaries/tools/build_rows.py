"""Round 4 sheet payloads: updated ROS rows (012, 031, 033, 056, 057), new rows ROS-058..065, KS notes."""
import json,sys
items=json.load(open('desc/items.json')); out={o['code']:o for o in json.load(open('desc/out.json'))}
rows=json.load(open('../ros3/rows_ROS.json'))
cur={r[3]:r for r in rows}
img=lambda fid:f'=IMAGE("https://drive.google.com/thumbnail?id={fid}&sz=w800")'
ADD={
 'ROS-012':'أُضيفت ١٣ صورة من جهاز المالك لم تكن على الدرايف (الصور 5–17)',
 'ROS-031':'أُضيفت صورتان مقرّبتان من جهاز المالك (الصور 6–7)؛ صورة ثالثة (DSC_7079) على الجهاز لم تُرفع بعد',
 'ROS-033':'أُضيفت ٤ صور من جهاز المالك (الصور 2–5)',
 'ROS-056':'أُضيفت الصور 11–19: صورتان بإضاءة خلفية (DSC_7023 المتفرقة سابقاً وDSC_7021، طابقتا شكل الخرز ولونه) و٦ صور مقرّبة من جلسة ٣٠ يناير ٢٠٢٦، والصورة 19 كانت مسجّلة خطأً ROS-057-10',
}
upd={}
for code in ['ROS-031','ROS-033','ROS-056']:
    o=out[code]; it=[i for i in items if i['code']==code][0]
    desc=o['description'].strip()
    notes=o['notes'].strip()
    if ADD[code] not in notes: notes=(notes+'؛ ' if notes else '')+ADD[code]
    # keep hero unless agent picked a different whole-piece photo
    hero_id=it['drive_ids'][str(o['hero'])]
    upd[code]=dict(row=int(code[-3:])+1, B=img(hero_id), C=desc, G=notes, old_B=cur[code][1], old_C=cur[code][2])
upd['ROS-057']=dict(row=58, G='الخامة غير مؤكدة (فاتوران محتمل) — يلزم تأكيد قبل النشر؛ أُضيفت ١٠ صور مقرّبة من جلسة ٣٠ يناير ٢٠٢٦ (الصور 10–19) لتطابق الشاهد والخامة؛ الصورة التي كانت ROS-057-10 نُقلت إلى ROS-056 (تُظهر خرز ROS-056)')
new=[]
for k,code in enumerate([f'ROS-0{n}' for n in range(58,66)]):
    o=out[code]; it=[i for i in items if i['code']==code][0]
    notes=o['notes'].strip(); add='قطعة جديدة من صور جهاز المالك لم تكن على الدرايف'
    notes=add+('؛ '+notes if notes else '')
    new.append([str(58+k), img(it['drive_ids'][str(o['hero'])]), o['description'].strip(), code, 'Rosary', '', notes])
ks={'ROS-KS-006':(7,'أُضيفت صورة من جهاز المالك لم تكن على الدرايف (006-6)'),
    'ROS-KS-008':(9,'أُضيفت صورة كانت متفرقة في فولدر الفئة (008-6)؛ أُضيفت صورة من جهاز المالك لم تكن على الدرايف (008-7)')}

upd['ROS-012']=dict(row=13, B=img('1qLm_uOq7pjdZXFtzTn64-gjAyhpVo73L'),
  C='من نفائس المسابيح، خرز برميلي مدوّر الحواف بلون أحمر كرزي تسري في أعماقه تموّجات أدكن، بشاهد مخصّر بحلقة وعقدة حمراء، وحبل ذهبي اللون مضفور.',
  G='الخامة غير مؤكدة (فاتوران محتمل، فالتموجات الداخلية من سماته) — يلزم تأكيد قبل النشر؛ أُضيفت ٥ صور من جهاز المالك وأُعيد ترقيم الصور ١–٧؛ صور جلسة المساء في فولدر الجهاز نفسه تُظهر مسباحاً آخر (شاهد كمثري بحلقة مزدوجة، خرز مفلطح، حبل منسوج بخرزات حمراء) ففُصلت إلى ROS-066 ومعها الصورتان اللتان كانتا ROS-012-1 و-2؛ حُذف من الوصف التوهّج تحت الضوء لأنه من صور ROS-066',
  old_B=cur['ROS-012'][1], old_C=cur['ROS-012'][2])
upd['ROS-024']=dict(row=25, G=cur['ROS-024'][-1]+'؛ يُرجَّح أنه المسباح نفسه المسجّل ROS-059 (صوره تُظهر المسباح كاملاً): الخرز والفواصل الكمثرية والشاهد والكركوشة متطابقة — يُدمجان بعد تأكيد المالك أنها قطعة واحدة')
new.append(['66', img('1Wr3h5MDJaTq8izvS0tnt7CPWWHdMDqvh'),
  'مسباح نفيس بخرز مفلطح بلون أحمر كرزي تتّقد في أعماقه تحت الضوء تموّجات انسيابية كألسنة اللهب. شاهد كمثري بحلقة مزدوجة، وحبل ذهبي اللون مجدول ينتهي بكبوس وخرزات حمراء دقيقة.',
  'ROS-066','Rosary','',
  'قطعة فُصلت من ROS-012: صور جلسة المساء (١٧ نوفمبر ٢٠٢٥) تُظهر مسباحاً مختلفاً عن صور جلسة العصر (شاهد كمثري بحلقة مزدوجة بدل المخصّر، خرز مفلطح، حبل منسوج بكبوس وخرزات حمراء)؛ الصورتان ٧ و٩ كانتا ROS-012-1 و-2؛ المالك وضع الصور كلها في فولدر ROS-012 على الجهاز — يُرجى تأكيد أنهما مسباحان؛ الخامة غير مؤكدة (فاتوران محتمل، فالتموجات الداخلية من سماته) — يلزم تأكيد قبل النشر'])
json.dump(dict(upd=upd,new=new,ks=ks),open('payload.json','w'),ensure_ascii=False,indent=1)
for c,u in upd.items():
    print(c,u['row'],'hero changed' if 'B' in u and u['B']!=u['old_B'] else '', 'desc changed' if 'C' in u and u['C']!=u['old_C'] else '')
for r in new: print(r[3],len(r[2].split()),r[2]); print('   ',r[6])
