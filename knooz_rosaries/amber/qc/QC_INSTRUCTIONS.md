# QC of the amber catalog + new descriptions in the owner's style (Islamic Treasures, Kuwait)

The owner's amber catalog was organised into one Google Drive folder per physical piece (code such as AMB-A-014,
AMB-ST-007, Amb-dec-012). Each piece has a row in a Google Sheet with an image (the photo outlined in red on your
contact sheet), a Description, an Item Category and Notes. The owner reports that **some sheet images do not match
their descriptions**. Your job: check every piece in your batch with your own eyes, report every error, and write a
new description in the owner's style.

Be strict. A wrong row costs the owner a sale or his credibility. But do not invent problems: if it matches, say so.

## Input
Your batch is a JSON list (path in your prompt). Each item has:
- `code`, `tab`, `row`;
- `contact_sheet`: an image with every photo in the piece folder, labelled with its file name. The sheet image is
  outlined in red. Tiles labelled `VIDEO-SHEET …` are the owner's own image for that piece's promo video;
- `video_frames`: frame grids from the promo video (if any). A piece with a video must be the SAME physical object in
  the photos and the video: compare shape, inclusions, cracks, base, marks, case;
- `description` (current Arabic text), `category` (English label), `notes` (Arabic notes);
- `owner_text` (only for pieces whose description the owner wrote himself; see below);
- `unc_suggest` and `unc_question` for pieces in the «غير مصنف» (unclassified) sheet.

Open every contact sheet with the Read tool (and every video_frames image). If a tile is too small to judge, say so in
`problems` rather than guessing.

## Checks per piece
1. **Same piece:** do all photos in the folder show one and the same physical piece? List any photo that shows a
   different object (file name + what it shows + which code in your batch it seems to belong to, if any).
2. **Sheet image:** is the red-outlined photo that piece, and a reasonable full view? If another photo is clearly a
   better full view, name it (`better_sheet_image`).
3. **Description vs photos:** does the current description describe what the photos show (object type, what it
   depicts, form, colour, base, case)? Mark `description_ok: false` if it describes a different object or states a
   visible feature that is not there. Quote the wrong part.
4. **Category:** is the English Item Category right for the object? Suggest a better one if not.
5. **Notes:** flag any statement in Notes that the photos contradict.
6. **Video:** if the piece has video frames or a VIDEO-SHEET tile, is it the same physical object? (true / false /
   unsure + why).
7. **Duplicates inside your batch:** if two codes in your batch are the same physical piece, report it.

## New description (owner's style)
The owner (Abu Ali) wants every description close to how he writes. His own texts (spelling corrected):
- «تحفة من الكهرمان الألماني تعود لمصنع الـRK، صُنعت خصيصاً للاتحاد السوفيتي.»
- «صندوق يحتوي على منحوتات من الكهرمان الألماني.»
- «قطعة من نفائس الكهرمان الألماني، تجسد الذروة في تحويل الكهرمان الخام إلى قطع فنية.»
- «حجر كهرمان نادر بنقش احترافي.»
- «تحفة رائعة من الكهرمان تضاف لقائمة روائع إنتاجات مصنع الحكومة الألماني.»
- «قطعة نفيسة من الكهرمان الألماني، وهي نموذج عن الإصدارات الخاصة من خطوط إنتاج الكهرمان لأعرق مصانع التاريخ للكهرمان.»
- «منحوتة استثنائية من الكهرمان البولندي، تجسد المعنى الحقيقي للحرفية في نقش الكهرمان.»
- «تحفة من الكهرمان تحمل نموذج حصان من البرونز، من نفائس مصنع الـNBJ الألماني.»

What makes his style: one short sentence (8 to 22 words); it opens with the object noun and «من الكهرمان»; it names
what the piece IS (and what it depicts) rather than listing colours; it ends with one appreciative phrase. No colour
inventories, no long visual detail.

**Your new descriptions** follow that shape: [object noun] + «من الكهرمان» (or where the amber is) + [the one feature
that identifies this piece, visible in the photos] + [optional appreciative phrase]. 8 to 22 words, MSA, one sentence.
- Openers: تحفة، قطعة، منحوتة، حجر كهرمان، ساعة، علبة، صندوق، عقد، سوار، غليون، مبسم، طقم، ختم، إطار، منفضة، ولاعة،
  مرآة، دبوس… pick what the object is.
- Appreciative phrases you may use (subjective, from his vocabulary; vary them, do not repeat one phrase across many
  rows): «من نفائس الكهرمان»، «تحفة رائعة»، «قطعة نفيسة»، «بنقش احترافي»، «تجسد الحرفية في نقش الكهرمان»،
  «تجسد براعة تحويل الكهرمان الخام إلى قطع فنية»، «بتصميم أنيق»، «بلمسة فنية راقية».
- **Forbidden** (they are facts we cannot source for these pieces): any origin or country (ألماني، بولندي، روسي،
  بلطيقي…), any factory or maker name, any date or era (القرن الماضي، عشرينات، قديم، عتيق، أثري), rarity or museum
  claims (نادر، فريد، شديد الندرة، متحفي، استثنائي، بامتياز، الأسطورة), and «طبيعي». Marks or text seen on the object
  stay in Notes, not in the description.
- Material doubt: if the Notes say the material is uncertain (faturan, copal, bakelite, resin, "may not be amber"),
  do NOT say «من الكهرمان» for that part; describe the object by form and colour only. "Pressed amber possible" is
  still amber: «من الكهرمان» is fine, but never «طبيعي».
- Where amber is only part of the object, say where it is: «حصان من البرونز على قاعدة من الكهرمان»،
  «غليون بمبسم من الكهرمان».
- At most one colour word, and only if it is the defining trait (عسلي، زبدي، كونياكي، كرزي، أحمر).
- No Latin letters, no digits. Correct hamzas (إلى، أنيق) and taa marbuta (ة).
- Describe what the photos show. If the current description is wrong, your new one must be right.

Examples for pieces without owner text:
- «منحوتة من الكهرمان على هيئة فيل، تجسد الحرفية في نقش الكهرمان.»
- «علبة مكسوة بفسيفساء من قطع الكهرمان المصقول، تحفة رائعة بتصميم أنيق.»
- «حجر كهرمان خام بقشرته الأصلية، تتخلله عروق ذهبية لافتة.»
- «عقد من خرز الكهرمان الزيتوني المتدرج، من نفائس حُلي الكهرمان.»
- «زوج من المباسم بلون برتقالي كرزي في علبة سوداء مزخرفة.» (material doubtful, so no «من الكهرمان»)

If an item has `owner_text`, do NOT write a new description (put "OWNER" in `new_description`); still do all checks,
and check that the owner text fits the object in the photos.

## Output
Write a JSON list to the output path in your prompt, one object per piece, in batch order:
```
{"code": "...", "same_piece": true, "foreign_photos": [{"file": "...", "shows": "...", "belongs_to": ""}],
 "sheet_image_ok": true, "better_sheet_image": "", "description_ok": true, "description_problem": "",
 "category_ok": true, "category_suggest": "", "notes_problem": "", "video_match": null, "video_note": "",
 "duplicate_of": "", "new_description": "...", "new_description_words": 0, "what_it_is_en": "one line", "confidence": "high|medium|low"}
```
Write the file incrementally (rewrite it after every 5 pieces) so work survives an interruption; if the file
already exists when you start, continue after the last code in it. When done, check with Python that every code in
your batch is present once and every `new_description` (except OWNER) has 8–22 words and no Latin letters or digits.

Reply with: pieces checked, and a list of every piece with any problem (code + one line), most serious first.
