# Rewrite jewelry descriptions to sound like Abu Ali (Islamic Treasures, Kuwait)

The owner's instruction: Abu Ali's own texts are the authority, and every description we write must be **as close as
possible to his way**. The current descriptions are factually checked (a QC pass re-read every inscription at high
resolution), but they read like a cataloguer: they list claws, bezels, shoulders and shank patterns. Abu Ali never does
that. Your job is a **style rewrite only**: same facts, his voice. Read-only on Drive; no new facts.

## Abu Ali's texts (all 40 jewelry video captions, spelling-corrected)
`/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/jwl/restyle/corpus.txt` — read all of it
first and absorb the rhythm.

## His pattern
**[object + one adjective] (+ «بموديل استثنائي/رائع») + «يحمل حجر …» (+ «بلون استثنائي») + «منقوش بخط …» + «بعبارة (…)» / «بمتن (…)» / «بالآية الكريمة (…)» + «، صياغة/عمل الأستاذ …».**
- Openers he uses: «خاتم نفيس» (most), «خاتم استثنائي», «خاتم نادر» / «خاتم نادر جداً» (at most 1 in 6), or just «خاتم».
  Pendants: «قلب نفيس…», «دلّاية…», «قلادة…», «بروش…», «طقم…», «سوار…». Loose stone: «حجر…».
- The mount is never itemised. If the current text shows the mount is unusual, say «بموديل استثنائي» or «بموديل
  رائع» (his words) — at most about 1 ring in 3. Drop claws, beads, shoulders, shank grooves, openwork, «ذهبي اللون»,
  «فضي اللون».
- Stone: «يحمل حجر عقيق …» / «يحمل حجراً من العقيق …» / «يحمل حجر فيروز …» / «يحمل حجر جيد …»; an unnamed stone keeps
  its colour word only: «يحمل حجراً أخضر …», «يحمل حجراً شفافاً …». At most one colour word (عسلي، أحمر، برتقالي، أصفر،
  بني، أبيض…). «بلون استثنائي» only for a striking colour, sparingly. Keep «اللازورد» (JWL-RS-048) and «أوبال أسود
  طبيعي» (JWL-R-005) as they are.
- Engraving: keep «منقوش» and the script name only if the current text has them. A quoted inscription in the current text
  is verified: keep it in brackets, his way: «منقوش بعبارة (…)», «بمتن (ناد علياً مظهر العجائب)», «بالآية الكريمة (…)»,
  «بآية الكرسي», «بسورة الفلق كاملة». Long verses: name the sura/verse instead of quoting the whole of it. Raised/relief
  letters = «بأسلوب النحت». An unread engraving stays without words: «منقوش بخط النستعليق» or «بنقش استثنائي».
- Maker, exactly as now by category (do not add or remove a maker):
  B «صياغة الأستاذ الكبير بيكلو» (or «عمل الأستاذ بيكلو»); H «صياغة أسطورة المجوهرات الأستاذ حسين جدي»;
  HS «صياغة أبناء الأستاذ حسين جدي»; W, R, RS: none. Put it at the end after «،» as he does.
- Never add: metal («فديوم، فضة، ذهب»), era, century, dynasty, origin («يماني»…), «متحفي», «شديد الندرة», weight, size.
  These occur in his captions only as his own claims about specific pieces.

## Form
- One sentence, 8–24 words, Modern Standard Arabic, ends with «.»; no Latin letters, no Western digits.
- **No two descriptions in your batch may be identical.** Where two rings would come out the same, keep one honest
  difference from the current text: the inscription, the stone colour, «بموديل استثنائي», or one plain shape word
  («بيضوي، مستطيل، مستدير، على هيئة قطرة»).

## Examples (current → rewrite)
- «خاتم نفيس يحمل حجر عقيق برتقالي بيضوي منقوش بمتن (ناد علياً مظهر العجائب) كاملاً، بجانبين مخرّمين وكتفين مضلعين،
  صياغة أسطورة المجوهرات الأستاذ حسين جدي.» → «خاتم نفيس بموديل استثنائي يحمل حجر عقيق برتقالي منقوشاً بمتن (ناد علياً
  مظهر العجائب) كاملاً، صياغة أسطورة المجوهرات الأستاذ حسين جدي.»
- «خاتم أنيق يحمل حجر عقيق برتقالي بيضاوياً منقوشاً بخط النستعليق، في إطار مخرز وأكتاف من أخاديد يتوسطها قضيب بارز.»
  → «خاتم نفيس يحمل حجر عقيق برتقالي منقوش بخط النستعليق.»
- «خاتم أنيق يحمل حجراً بنفسجياً شفافاً محدّباً بلون صافٍ، تمسكه مخالب…» → «خاتم نفيس يحمل حجراً بنفسجياً شفافاً بلون
  استثنائي.»
- «قلب رائع يحمل حجر عقيق أحمر منقوش بخط النستعليق بعبارة (وأفوض أمري إلى الله إن الله بصير بالعباد)، في إطار…» →
  «قلب نفيس يحمل حجر عقيق أحمر منقوشاً بخط النستعليق بعبارة (وأفوض أمري إلى الله إن الله بصير بالعباد).»

## Input / output
Input: `restyle/in_<k>.json` (list of {code, category, item_category, current, inscription_read, visual_en, sheet}).
Use `current` as the fact source; `inscription_read` shows what was read (words with «؟» are NOT confirmed — never put
them in the description). Look at `sheet` (contact sheet) only if you need to judge whether a mount is unusual.

Write `restyle/out_<k>.json`: list of `{"code": "...", "description": "..."}` in input order. Self-check with Python:
every code present, 8–24 words, no banned words (فديوم فضة ذهب قرن عهد مغول صفوي قاجار تيمور عباسي يماني متحف),
maker phrase per category as above, no identical descriptions, no «؟». (Exception: «ذهبي» as the colour of a stone, e.g. a golden-yellow faceted stone, is fine.) Reply with counts and 5 sample before/after pairs.
