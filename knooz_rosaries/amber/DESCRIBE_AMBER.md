# Write catalog descriptions: amber stones, artifacts and carvings (Islamic Treasures, Kuwait)

Islamic Treasures (الكنوز الإسلامية) sells rare amber objects. Every piece in the amber catalog now has a code:
- AMB-ST-### is an amber stone;
- AMB-A-### is an amber artifact;
- Amb-dec-### is a carving.

Each piece has a contact sheet of its photos, labelled #1, #2 and so on. Your descriptions go into the catalog sheet.

Read the house style guide first, all of it. Everything in it applies:
/home/user/Mo/knooz_rosaries/amber/STYLE_GUIDE_AMBER.md

It builds on the rosary guide /home/user/Mo/knooz_rosaries/STYLE_GUIDE.md, which you only need for voice and the
no-fabrication rules.

## Input
Your item list is a JSON file (path in your prompt). Each item has:
- code, category (ST/A/DEC). In this round the code is a temporary piece id such as "g3-07" (final codes are assigned
  later); copy it unchanged into your output;
- suggested_hero: the photo number the grouping pass picked as the best full view. Keep it unless another photo clearly
  shows the whole piece better;
- sheet: path to the contact sheet;
- photos: [{n, drive_id}], where n is the #number on the sheet;
- type_en and visual_en: an English observation from the grouping pass. It is helpful but may be wrong; trust the photos.
- notes_en: flags from grouping, for example uncertain material, a lot of several objects, or merged sessions;
- fact (optional): a verified source fact from the owner (his own text from the video sheet). Follow it exactly. It may
  name a factory, origin, date or maker, and you may use those words for THIS piece only.
  - Use only its factual content (origin, factory, era, maker, what the object is). Its promotional words are not
    facts: do not copy «متحفي/متحفيه», «الأسطورة», «شديد الندرة», «استثنائي», «بامتياز» from it.
  - Write factory names as given (for example «مصنع SBM», «مصنع NBJ», «مصنع RK») and person names in Arabic letters
    (for example «جوزيف أوسترمان»).
  - Mention in `notes` that the origin/factory wording comes from the owner's video-sheet text.
- notes_en may contain a "COORDINATOR:" instruction for that piece. Follow it.

## Rules
- **Length:** 20–30 words, hard max 32, in one or two sentences. Modern Standard Arabic, the owner's prestige voice,
  calm.
- **No Latin letters and no digits** in the description, unless a `fact` contains them and you quote it. In that case
  write the factory as given in the fact (for example «مصنع SBM») and the digits in Arabic-Indic.
- **Never state** an origin, factory, age, weight, size, karat or maker unless `fact` gives it.
  - Metals are «ذهبي اللون» / «فضي اللون».
  - Words or inscriptions visible on the object or its box (for example "Ambre véritable", a monogram, a date engraved
    on silver, "SBM" printed on a box) are observations, not facts. Do not put them in the description; put them in
    `notes`, quoted in Latin letters, so the owner can decide.
- **Material.**
  - If notes_en or the photos suggest the piece may not be natural amber (pressed amber, copal, phenolic resin, glass,
    plastic), say «من الكهرمان» only if you are reasonably sure. Otherwise describe colour and finish without naming the
    material, and put the doubt in `notes`, for example «الخامة غير مؤكدة (كهرمان مضغوط محتمل) — يلزم تأكيد».
  - Bronze, silver-colour or brass parts can be named by look: «تمثال معدني برونزي اللون».
- **Lots and sets** (several pins, badges or stones in one piece): say so in the description («مجموعة من …») without a
  count unless the count is certain from the photos, then use words: «خمسة دبابيس».
- **Sensitive symbols.** If an item shows political or military insignia (for example a swastika), describe it
  neutrally as «شارة/دبوس» with its colour and form, without naming the symbol or regime in the description. Name it in
  `notes` and add «يلزم مراجعة قيود العرض والبيع قبل النشر».
- **Vary openings** within your batch: «تحفة …», «قطعة …», «علبة …», «منحوتة …», «حجر …», «من نفائس …».
  - «متحفي» at most once in your batch, and only for something truly exceptional.
  - «نادر» at most about 1 in 4.
- **Item Category** (English, one value): see style guide §5.
  - ST: "Amber Stone".
  - DEC: "Amber Carving".
  - A: the specific type ("Amber Box", "Amber Clock", "Amber Necklace", "Amber Brooch", "Amber Pin", "Amber Badge",
    "Amber Seal", "Amber Pipe", "Amber Cigarette Holder", "Amber Lighter", "Amber Ashtray", "Amber Coaster",
    "Amber Bracelet", "Amber Desk Set", "Amber Antique" as fallback). Use another short English type when none fits
    (for example "Amber Mouthpiece", "Amber Lamp", "Amber Thermometer", "Amber Cigar Cutter", "Amber Letter Rack").

## Method
For each item:
1. View the contact sheet.
2. If a detail matters (an inscription, inclusions, fittings, a crack), fetch high resolution:
   `curl -sS -L -o /tmp/x.jpg "https://lh3.googleusercontent.com/d/<drive_id>=w1600"` and crop with PIL. Save downloads
   under /tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/amb/desc/work_<yourname>/ and delete
   them when done.
3. Choose `hero`: the photo number that best shows the WHOLE piece.

## Output
Write a JSON array to your output path, one entry per item, in the same order:

`{"code": "...", "hero": <n>, "description": "Arabic", "item_category": "Amber …", "notes": "Arabic or empty", "visual": "short English observation"}`

`notes` contains only real flags, in short Arabic:
- material uncertain;
- lot or set;
- inscriptions or marks seen (quoted);
- damage or repair;
- single photo or no full view;
- sensitive insignia.

Self-check with Python before you finish:
- all codes are present;
- every description is 20–32 words;
- there are no Latin letters or Western digits in descriptions, except inside a quoted fact.

Reply with a compact table: code | item_category | first 8 words | notes (short).
