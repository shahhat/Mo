# Write catalog descriptions — مسابيح منوعة (ROS, mixed materials)

Context: Islamic Treasures (الكنوز الإسلامية, Kuwait) sells rare rosaries. The owner just uploaded many more photos to the
"مسابيح منوعة" (mixed-materials) folder. Pieces were grouped from the photos; each piece now has a code (ROS-003 … ROS-057)
and a contact sheet showing every photo labelled #1, #2 … These descriptions go into the website/catalog sheet.

Read the house style guide first:
/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/work/STYLE_GUIDE.md
Everything in it applies (voice, no-fabrication rules, vocabulary, prestige calibration), with these overrides:

## Overrides for this round
- **Length: 18–28 words, hard max 30, one or two sentences.** The owner asked for shorter text than the style guide's
  original 30–55 words. Model the length on these approved examples:
  - «مسباح نفيس من الكهرمان الدومينيكاني الشفاف، بخراطة المبدع صايم. ٣٣ خرزة كروية صافية بلون ذهبي ليموني، تعلوها مئذنة من الكهرمان نفسه على خيط أحمر.»
  - «من نوادر المسابيح، خرز كروي بلون أحمر عنابي عميق تتلألأ في أعماقه ذرات لامعة. شاهد مخروط بحلقات دقيقة على حبل أحمر.»
- **Mixed category: do NOT name the material unless it is certain from the photos.** Faturan, bakelite, amber, coral,
  turquoise, horn, kuk, wood, ivory, bone, agate, glass and resin all look alike in photos. Default to the catalog approach
  («من نوادر المسابيح» / «مسباح نادر» / «قطعة …») and describe what is seen: colour, transparency, speckles, veining, cut, شاهد,
  التمليكة, الشرّابة, metal parts («ذهبي اللون/فضي اللون»), coins (just «عملات», never their country or date).
  Put your best material guess in `notes` (e.g. «الخامة غير مؤكدة (فاتوران/بكلايت محتمل) — يلزم تأكيد قبل النشر»).
  Carved floral wooden-looking beads may be described as «خرز منحوت بزخارف زهرية» without naming wood.
- Vary openings across the batch. «من نوادر المسابيح» at most 3 times in your batch; use other openings
  («مسباح نادر …», «قطعة …», «خرز …», «مسباح أنيق …», etc.).
- «متحفي» at most once in your batch, only for something truly exceptional.
- Every item may carry a `fact` field: follow it exactly (it is a verified source fact or an owner decision).
- Items with `previous_description` were described before from only 1–2 photos; new photos were added. Re-describe from
  the full set: keep what is still right, correct what the new photos contradict, and update the notes (drop
  «صورة واحدة فقط» if there are now several photos, etc.). Keep any previous material caution unless the photos settle it.

## Method
For each item: view the contact sheet (`sheet`). If a detail matters (metal disc, inlay, inclusions), open the individual
700px photo from `photo_files`, or fetch high resolution: `curl -sS -L -o /tmp/x.jpg "https://lh3.googleusercontent.com/d/<drive_id>=w2000"`
(ids in `drive_ids`) and crop with PIL. Save any downloads under
/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/ros3/desc/work/.

## Output
JSON array to your output path, one entry per item, same order:
`{"code": "...", "hero": <photo number that best shows the WHOLE piece>, "description": "Arabic", "notes": "Arabic or empty", "visual": "short English observation"}`
- notes = only real flags (material uncertain, single photo, no full view, damage, stamps/marks seen, duplicates). Short Arabic.
Self-check with Python: all codes present, 18–30 words each, no Latin letters in descriptions, no digits unless a fact gives
them. Reply with a short summary and list any piece you think is wrongly grouped (photos of two different rosaries in one
code, or a code that duplicates another).
