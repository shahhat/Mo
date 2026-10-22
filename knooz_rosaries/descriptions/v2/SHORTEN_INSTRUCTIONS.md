# Shorten Knooz rosary descriptions

Context: Islamic Treasures (الكنوز الإسلامية, Kuwait) sells rare amber rosaries (مسابيح). Each piece already has an
approved Arabic catalog description (about 40 words, 2–3 sentences). The owner liked them but asked for them to be
**a bit shorter**. Your job is to condense each one. You are an editor, not a writer: you cut, merge and tighten —
you never add.

Full house style guide (read it once): /tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/work/STYLE_GUIDE.md

## Target
- **18–28 words, hard maximum 30.** One or two sentences. Modern Standard Arabic, refined and calm.
- Keep, in this priority order:
  1. what it is + category (كهرب شفاف / كهرب صاك / حجر واحد / كهرمان حشري / كهرمان ألماني / من نوادر المسابيح) + its prestige qualifier;
  2. the visual identity: bead cut, colour, clarity or pattern, and the visible inclusions/insects (for the insect category);
  3. the شاهد/مئذنة and the single most distinctive fitting (e.g. a coin tassel, an amber drop, a chain).
- Drop first: thread colours, small tail beads, minor spacers, repeated adjectives, and the closing "collector framing" clause
  (e.g. «قطعة تليق بالمقتني الخبير», «تفصيل يمنح القطعة رشاقة لافتة»). Keep a closing clause only if very short and adding real meaning.

## Hard rules
- **No new facts.** Every claim in your version must already be in the original description (or in the item's `special` field).
  Do not add age, origin, turner/maker, weight, size, bead count, karat, or materials. Do not upgrade a qualifier
  (if the original says «مميز», do not write «نادر»). You may soften or drop a superlative.
- Keep «متحفي» / «بمستوى متحفي» only where the original already has it. Never add it.
- Keep source facts exactly where present: ROS-K-005 (الكهرمان الدومينيكاني، خراطة المبدع صايم، ٣٣ خرزة), ROS-KS-002.
  If an original mentions «صايم», keep it.
- Metals stay «ذهبي اللون» / «فضي اللون».
- Digits only if already in the original (Arabic-Indic). No exclamation marks, no emoji, no dialect.
- Vary openings across rows; do not start most rows with the same word. Avoid repeating the same phrase pattern row after row.
- If an item has a non-empty `special` field, follow it (it carries an owner decision). It overrides the original where they conflict.

## Calibration examples
Original (44 words): «بخراطة المبدع صايم، مسباح نفيس من الكهرمان الدومينيكاني الشفاف يضم ٣٣ خرزة كروية صافية بلون ذهبي ليموني تنساب فيه الإضاءة بنقاء لافت. تعلوه مئذنة من الكهرمان نفسه، ويكمله خيط أحمر بثلاث خرزات صغيرة وخرزة طرفية، فتلتقي في القطعة نقاوة الخامة وإحكام الصنعة.»
Short (24 words): «مسباح نفيس من الكهرمان الدومينيكاني الشفاف، بخراطة المبدع صايم. ٣٣ خرزة كروية صافية بلون ذهبي ليموني، تعلوها مئذنة من الكهرمان نفسه على خيط أحمر.»

Original (43 words): «من نفائس الكهرب الصاك، مسباح بخرز كروي كبير أصفر معرّق بالأبيض، تنفتح في بعض حباته مساحات عسلية صافية تزيد اللون عمقاً. مئذنة معرّقة تعلوها عقدة حمراء، وشرّابة من سلسلة ذهبية اللون بعملة منقوشة وخرزتين وقطرتين، قطعة بمستوى متحفي في تناغم خامتها وحليتها.»
Short (26 words): «من نفائس الكهرب الصاك بمستوى متحفي، خرز كروي كبير أصفر معرّق بالأبيض تنفتح فيه مساحات عسلية صافية. مئذنة معرّقة بعقدة حمراء، وشرّابة ذهبية اللون بعملة منقوشة.»

## Output
Write a JSON array to the output path you were given: `[{"code": "...", "description": "..."}]`, one entry for every
input item, same order, same codes. Then self-check with Python: every code present, word count 18–30, no Latin letters,
no digits unless the original had them, «متحف» only where the original had it. Fix anything that fails, then reply with a
one-line summary (count, min/mean/max word count).
