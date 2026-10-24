"""Round 8: QC fixes + descriptions in the owner's style. Builds sheet_payload_r8.json from the r7 payload."""
import json, copy, re
AMB = '/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/amb'
pay = json.load(open(f'{AMB}/sheet_payload_r7.json'))
tree = json.load(open(f'{AMB}/qc/tree_now.json'))
own = json.load(open(f'{AMB}/qc/owner_desc.json'))
qc = {}
for b in ['b1', 'b2', 'b3', 'b4', 'b5']:
    for o in json.load(open(f'{AMB}/qc/out_{b}.json')):
        qc[o['code']] = o
img = lambda fid: f'=IMAGE("https://drive.google.com/thumbnail?id={fid}&sz=w800")'
tabs = {o['tab']: o['values'] for o in pay}
rows = {r[3]: r for v in tabs.values() for r in v}

def rep(code, old, new):
    n = rows[code][6]
    assert n.count(old) == 1, (code, old)
    rows[code][6] = n.replace(old, new)

# 1) descriptions
for code, r in rows.items():
    if code in own:
        r[2] = own[code]['corrected']
    else:
        d = qc[code]['new_description']
        assert d != 'OWNER', code
        r[2] = d

# 2) owner-text notes: the description now IS his text
VQ = re.compile(r'نص شيت الفيديو \(([^)]*(?:\([^)]*\))?[^)]*)\): «[^»]*»\.')
for code in own:
    if code not in rows:
        continue
    n = rows[code][6]
    m = VQ.search(n)
    if m:
        rows[code][6] = n[:m.start()] + f'الوصف هو نص المالك في شيت الفيديو ({m.group(1)}) بتصحيح إملائي فقط.' + n[m.end():]
rep('AMB-A-102', 'عبارة الأصل والمصنع من نص شيت الفيديو للمالك، وفي النص أيضاً «صنعت خصيصا للاتحاد السوفيتي» (لم تُذكر في الوصف)؛ ', '')
rep('AMB-A-057', 'في شيت الفيديو صف (Phase 05 – Amber Faces) بنص: «صندوق يحتوي على منحوتات من الكهرمان الالماني»، ولا يوجد له ملف فيديو',
    'الوصف هو نص المالك في شيت الفيديو (Phase 05 – Amber Faces) بتصحيح إملائي فقط، ولا يوجد له ملف فيديو')

# 3) QC fixes in notes
rows['AMB-ST-024'][6] = ('ثلاثة من ملفاتها كانت باسم A009، لكن فيديو A009 يُظهر حجراً آخر (مصقولاً لامعاً على قاعدة خشبية)، '
                         'فنُقل الفيديو إلى AMB-ST-030 عند التدقيق وأُزيل نصه من وصف هذا الحجر؛ يلزم أن يؤكد المالك أي حجر يخصه الرمز A009.')
rep('AMB-ST-010', 'صورة واحدة فقط؛ الصورة AMB-ST-011-3 (على حامل طويل) قد تكون لهذا الحجر — غير مؤكد.', 'صورة واحدة فقط.')
rep('AMB-ST-011', 'تبدو لهذا الحجر من جانبه العريض، وقد تكون للحجر AMB-ST-010 — غير مؤكد.',
    'تبدو لهذا الحجر من جانبه العريض (الشرخ الداكن أسفل السطح المستوي والتعريق البني) — رجّحه التدقيق دون تأكيد قاطع.')
rep('AMB-A-083', '؛ الصورتان #2 و#3 نسختان متطابقتان.', '.')
rep('AMB-A-084', 'قد تكون طقماً مكتبياً مع ميزان الحرارة AMB-A-086 لكنها صُوّرت منفصلة.',
    'فيديو A014 يُظهرها مع ميزان الحرارة AMB-A-086 طقماً واحداً (صُوّرت القطعتان منفصلتين في الصور)، فقد ينطبق نص المالك على الطقم كله.')
rep('AMB-A-086', 'قد تكون طقماً مكتبياً مع ساعة الكهرمان AMB-A-084 (البناء نفسه) لكنها صُوّرت منفصلة.',
    'تظهر مع ساعة الكهرمان AMB-A-084 طقماً واحداً في فيديو A014 (المحفوظ في فولدر AMB-A-084)؛ صُوّرت منفصلة في الصور.')
rep('AMB-A-117', 'الهيئة توحي بسوار بمفصّلات — يلزم تأكيد.',
    'السوار من عدة ألواح على الأرجح: الصورة ١ تُظهر لوحاً غير لوح الصورتين ٢ و٣ (فص ببعوضة واحدة، وفص بذبابة كبيرة وبعوضة) — يلزم تأكيد.')
rep('AMB-A-118', 'طقم: عقد وزوج أقراط والعلبة الزجاجية؛',
    'طقم: عقد وقطرتان شفافتان والعلبة الزجاجية؛ القطرتان غير متطابقتين ولا تظهر لهما خطافات أذن، فقد تكونان دلّايتين لا زوج أقراط — يلزم تأكيد؛')
rep('AMB-A-110', 'والمبسم متجانس اللون — يُستحسن تأكيد أنه كهرمان.',
    'والمبسم برتقالي متجانس اللون، فلم يُذكر الكهرمان في الوصف ولا في الفئة لحين التأكد من خامته؛ الطوق يبدو ذهبي اللون.')
rep('AMB-A-048', 'صورة واحدة مقرّبة فقط ولا يظهر الصحن كاملاً؛', 'صورة واحدة مقرّبة تُظهر جزءاً من الحافة فقط — يلزم تصوير الصحن كاملاً؛')
rows['AMB-A-110'][4] = 'Pipe'

# 4) AMB-A-001 split: owner's own folder keeps the brown pipe; the cream pipe + box become AMB-A-120
r = rows['AMB-A-001']
r[1] = img('1g6N8KIPyjgeA5nTtMTe1GdHvqBtjryNS')
r[2] = 'غليون برأس منحنٍ يعلوه غطاء مذهّب بمفصلة تزيّنه زهرة بارزة، وطوق مذهّب عند قاعدته، بزخارف متقنة.'
r[4] = 'Pipe'
r[6] = ('صورتا فولدر المالك الأصلي AMB-A-001؛ على الغطاء أربع دمغات صغيرة غير مقروءة. لا يظهر الكهرمان ولا الغليون كاملاً في الصورتين — '
        'يلزم تصوير القطعة كاملة. صورتا الغليون الفاتح في علبة المخمل والعلبة المغلقة كانتا مضافتين لهذه القطعة خطأً، ونُقلتا عند التدقيق إلى AMB-A-120.')
a120 = ['120', img('1pjIMy7Xub6IZVfuPY3wiRSO7RO8TmXuV'),
        'غليون برأس فاتح يطوّقه إطار مذهّب مخرّم، ومبسم من الكهرمان، في علبته المبطّنة بالمخمل الأحمر.',
        'AMB-A-120', 'Amber Pipe', '',
        'الرأس يبدو من الميرشوم (غير مؤكد)، ولا صورة تُظهر الغليون كاملاً. الصورة ٢ علبة مغلقة مطعّمة بالمعدن صُوّرت قبل الغليون بأربع دقائق، '
        'ويُرجَّح أنها علبته — غير مؤكد. كانت الصورتان ضمن AMB-A-001 (غليون آخر) وفُصلتا عند التدقيق.']
tabs['AMB-A'].append(a120)

# 5) AMB-ST-030: A009 stone, video only
st030 = ['30', img('1QakkRwHYMRr7bEyHuZ8d23HJlZQUP0UK'), own['AMB-ST-030']['corrected'], 'AMB-ST-030', 'Amber Stone', '',
         'حجر مصقول بلون كرزي عميق على قاعدة خشبية بلوحة نحاسية صغيرة. قطعة لها فيديو بلا صور (الفولدر أحمر): AMB-ST-030-video.mp4 — '
         'الصورة لقطة مؤقتة من صورة شيت الفيديو، ويلزم تصويرها. الوصف هو نص المالك في شيت الفيديو (Phase 04 – A009) بتصحيح إملائي فقط. '
         'كان الفيديو مربوطاً خطأً بالحجر AMB-ST-024 (بسبب أسماء ملفاته)، وتبيّن عند التدقيق أنه حجر آخر لم يُصوَّر.']
tabs['AMB-ST'].append(st030)

# 6) better sheet image for Amb-dec-003
fid = next(e['id'] for e in tree if e['path'].endswith('/Amb-dec-003/Amb-dec-003-5.jpg'))
rows['Amb-dec-003'][1] = img(fid)

# checks
lat = re.compile(r'[A-Za-z0-9]')
for t, v in tabs.items():
    for r in v:
        if r[3] in own:
            continue
        w = len(r[2].split())
        assert 8 <= w <= 22, (r[3], w)
        assert not lat.search(r[2]), (r[3], r[2])
        for bad in ['نادر', 'متحف', 'ألماني', 'بولندي', 'طبيعي', 'فريد', 'استثنائي', 'الأسطورة', 'القرن الماضي']:
            if bad in r[2] and not (bad == 'القرن' ):
                raise SystemExit(f'forbidden {bad} in {r[3]}: {r[2]}')
json.dump(pay, open(f'{AMB}/sheet_payload_r8.json', 'w'), ensure_ascii=False, indent=1)
print({t: len(v) for t, v in tabs.items()})
