# Cross-check: is any piece photographed twice? (Islamic Treasures jewelry, Kuwait)

311 jewelry pieces (rings, pendants…) were grouped from 1384 photos by 7 people, each working on a range of photo
sessions. Each person merged re-shoots inside their own range, and adjacent re-shoots (S04↔S06) were already merged.
A ring re-photographed in a distant session, or filed in two category folders, may still appear as **two pieces**.
Your job is to find such pairs. Read only; do not touch Google Drive.

## Paths
- **JWL** = /tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/jwl
- **JWL/pieces_m.json**: the pieces: piece id, category (W/B/H/R/RS/HS), photos [#N], hero, type_en, visual_en,
  facts_en (inscriptions read, hallmarks), sessions, notes_en.
- **JWL/hb/<CAT>_k.jpg**: boards of every piece's hero photo, labelled «piece #hero».
- **JWL/timeline.json**: #n → Drive `id`, file name, folder, shot time. Thumbnails JWL/th/<id>.jpg (400 px). High res:
  `curl -sS -L -o x.jpg "https://lh3.googleusercontent.com/d/<id>=w1600"`.
- **JWL/cmp.py**: `python3 JWL/cmp.py out.jpg '#12,13' '#900,901'` makes a side-by-side board of photos.
  Work in JWL/vm/work_dup/ and delete big downloads when done.

## Method
1. Text pass: group pieces whose `facts_en` inscriptions are the same or very close (e.g. «نصر من الله وفتح قريب»,
   Surat al-Ikhlas, Nad-e Ali) and whose type/stone agree. Compare each such cluster visually.
2. Visual pass: go through the hero boards of ALL categories together (a piece may sit in two categories). Shortlist
   pairs that look alike (same stone colour/shape, same mount type) from different sessions.
3. Confirm at high resolution. Same object = same engraving layout (same words at the same places, same flourishes,
   same chips/inclusions) AND the same mount. Jeddi-workshop rings look alike: do not merge on style.

## Output
Write JWL/vm/dup_pairs.json: `[{"keep": "g3-12", "merge": "g6-30", "confidence": "high|medium", "evidence": "..."}]`
(keep = the piece with more/better photos). Also list in your reply the clusters you checked and rejected, briefly.
