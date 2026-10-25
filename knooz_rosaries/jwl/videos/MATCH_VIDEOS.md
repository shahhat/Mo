# Match promo videos to catalog pieces (Islamic Treasures jewelry, Kuwait)

The owner (Abu Ali) made short promo videos of some rings, pendants, necklaces and engraved stones. The catalog photos
were taken separately (Nov 2025 photo session) and have been grouped into pieces. Your job: for each video assigned to
you, find the catalog piece that is **the same physical object**, or conclude that it is not in the photos.

Many videos are older than the photo session; some pieces were probably sold before the photos were taken, so "not
found" is a normal, acceptable answer. A wrong match is much worse than "not found".

## Paths
- **JWL** = /tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/jwl
- **JWL/video_captions.json**: list of {v, src, id, title, on_screen}. `on_screen` is Abu Ali's caption burned into the
  video (it names stone, inscription, era, maker — use the inscription and maker as search hints).
- **JWL/vb/strip/vNN.jpg**: 8 frames of video NN. **JWL/vf/vNN/fNNN.jpg**: every frame at 1 fps, full resolution
  (portrait 1080×1700, landscape 1920×1080 or 4K portrait). Use the full frames to see the engraving, bezel and shank.
- **JWL/pieces_m.json**: all 311 pieces (merged). Each has piece id, category, photos [#N], hero, type_en,
  visual_en, facts_en (inscriptions read, hallmarks), notes_en.
- **JWL/hb/<CAT>_k.jpg**: boards of every piece's hero photo, labelled «piece #hero», per category
  (W pendants/necklaces, B Biglou, H Hussein Jeddi, R ordinary rings, RS rare rings various makers, HS Jeddi's sons).
- **JWL/timeline.json**: photo #n → Drive id (`id`), file name, folder. Thumbnails: JWL/th/<id>.jpg (400 px).
  High resolution: `curl -sS -L -o x.jpg "https://lh3.googleusercontent.com/d/<id>=w1600"`.
- **JWL/cmp.py**: side-by-side board. `python3 JWL/cmp.py out.jpg v07:3,9,15 '#1230,1231'` puts video 07 frames 3, 9,
  15 next to photos #1230 and #1231. Work under JWL/vm/work_<yourname>/ and delete big downloads when done.

## How to decide
1. Read the caption: the inscription text and maker narrow the search. The maker in the caption is a hint, not a
   rule — the piece may be filed in another category. Search `facts_en` of all pieces for the inscription words.
2. Shortlist by appearance on the hero boards: stone colour and shape, the setting (bezel beads, claws, lobes), the
   shank (fluted, twisted, openwork, chased, plain), metal colour.
3. Confirm at high resolution. **A match needs the engraving layout to agree** (same words in the same places, same
   line breaks, same flourishes, chips or inclusions) **and** the mount to agree. For an unengraved stone: same stone
   pattern/inclusions and same mount. Similar style is not enough — Jeddi workshop rings look alike.
4. Note that two videos can show the same object (re-edits). Say so if you see it.

## Output
Write JWL/vm/match_<yourname>.json: a list, one entry per assigned video:
`{"v": "v07", "piece": "g6-12" | null, "confidence": "high" | "medium" | "low" | "none",
  "evidence": "English: what agrees (engraving words/layout, mount, stone marks) and the photo #s compared",
  "candidates_rejected": "pieces you checked and why they differ", "same_as_video": "vNN or empty",
  "frames_for_folder": [3 frame numbers that best show the whole object clearly, without the caption if possible]}`

Only "high" means you are sure. Reply with a compact table: v | piece | confidence | short evidence.
