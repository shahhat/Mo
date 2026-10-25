import json,sys,copy,re
A=sys.argv[1]
sys.path.insert(0,f'{A}/v11')
from new_desc_part1 import D
from new_desc_part2 import D2, V
p=json.load(open(f'{A}/sheet_payload_r10.json'))
q=copy.deepcopy(p)
allnew={**D,**D2}
codes=set(r[3] for t in p for r in t['values'])
assert set(allnew)<=codes, set(allnew)-codes
assert set(V)<=codes
extra={
"AMB-A-050":" اسم الصانع كما كُتب على الفيديو «Josef Osterman»، بينما الختم داخل العلبة «JOSEF OSTERMANN» (بحرفي N) — يُستحسن تصحيحه في الفيديو والشيت معاً.",
"AMB-A-106":" نص شيت الفيديو «مقاسات متنوعه وخامات متنوعه» يختلف عن المكتوب على الفيديو «مقاسات وخامات متنوعه»، واعتُمد نص الفيديو.",
"AMB-A-107":" شيت الفيديو يضيف في آخره «حيث ساهمت في انتشار الكهرمان في جميع دول العالم»، وهذه الجملة غير مكتوبة على الفيديو فلم تُدرج.",
"AMB-A-015":" شيت الفيديو يكرر «تحفه من الكهرمان» مرتين، والفيديو يكتبها مرة واحدة ويضع (NBJ) بين قوسين، واعتُمد نص الفيديو.",
"Amb-dec-049":" «اغدانسك» كما على الفيديو؛ الكتابة الشائعة لاسم المدينة «غدانسك» (Gdańsk) — يُستحسن تصحيحها في الفيديو والشيت معاً.",
"AMB-A-104":" «SBM» بحروف كبيرة كما على الفيديو (شيت الفيديو: sbm).",
"AMB-A-084":" الوصف نفسه مكرر على ميزان الحرارة AMB-A-086 لأن الفيديو واحد للطقم.",
}
pat=re.compile(r'الوصف هو نص المالك في شيت الفيديو \((.*?)\) بتصحيح إملائي فقط\.')
changed=[]
for t in q:
    for r in t['values']:
        c=r[3]; old=r[2]; note=r[6]
        if c in V:
            vid,txt=V[c]; r[2]=txt
            if c=='AMB-A-086':
                note2=note.rstrip()+' الوصف هو النص المكتوب على فيديو A014 المشترك مع AMB-A-084 (طقم واحد)، فالوصف نفسه للقطعتين.'
            else:
                assert pat.search(note), c
                note2=pat.sub(lambda m:f'الوصف هو النص المكتوب على الفيديو ({m.group(1)}) حرفياً، بتصحيح إملائي فقط (ة/ه والهمزات).', note)
            r[6]=note2.rstrip()+extra.get(c,'')
        elif c in allnew:
            r[2]=allnew[c]
        if c=='Amb-dec-003':
            r[6]=note.rstrip()+' نص الفيديو الوحيد هو عنوانه «من تحف الكهرمان المنحوتة» (عنوان سلسلة لا وصف للقطعة)، فكُتب الوصف بأسلوب أبو علي وخُتم بعبارة العنوان.'
        if r[2]!=old: changed.append((c,old,r[2]))
ne={
"AMB-A-003":[("(لم يُذكر في الوصف)","(ذُكر اسم Kant في الوصف)")],
"AMB-A-024":[("لم تُذكر في الوصف","ذُكر الاسم في الوصف")],
"AMB-A-025":[("Reitschulg. 4\"","Reitschulg. 4\" (ذُكر في الوصف)")],
"AMB-A-061":[("\"JOSEF OSTERMANN\"","\"JOSEF OSTERMANN\" (ذُكر في الوصف)")],
"AMB-A-080":[("\"BYDGOSZCZ\"","\"BYDGOSZCZ\" (ذُكر في الوصف)")],
"AMB-A-091":[("SOLINGEN\" مع شعار","SOLINGEN\" مع شعار (ذُكر في الوصف)")],
"AMB-A-095":[("— ملاحظات من الصور لا مصدر موثق، للمالك أن يقرر ذكرها","— ذُكر ختم SBM في الوصف، ولم يُذكر نقش القاعدة (١٩٣٩) لحساسيته")],
"AMB-A-096":[("— ملاحظة من الصورة لا مصدر موثق، للمالك أن يقرر ذكرها.","— ذُكر في الوصف كما هو مطبوع على العلبة.")],
"AMB-A-108":[("نص اللوحة:","نص اللوحة (ذُكر اسم الشركة في الوصف):")],
"Amb-dec-030":[("— ملاحظة من الصورة لا مصدر موثق، للمالك أن يقرر ذكره.","— ذُكر الاسم في الوصف كما هو محفور.")],
}
for t in q:
    for r in t['values']:
        for a,b in ne.get(r[3],[]):
            assert a in r[6], (r[3],a); r[6]=r[6].replace(a,b)
json.dump(q,open(f'{A}/sheet_payload_r11.json','w'),ensure_ascii=False,indent=1)
json.dump(changed,open(f'{A}/v11/changed_desc.json','w'),ensure_ascii=False,indent=1)
print('changed desc:',len(changed))
for c,o,n in changed:
    if c in V: print('V',c,'\n  OLD',o,'\n  NEW',n)
wc=[len(r[2].split()) for t in q for r in t['values']]
print('words min/max/avg',min(wc),max(wc),round(sum(wc)/len(wc),1))
