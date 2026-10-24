# Group the amber-catalog photos into pieces (Islamic Treasures, Kuwait)

The owner sells rare amber objects. His amber root folder on Google Drive has 3 categories:

- **AMB-ST «أحجار الكهرمان»**: natural amber stones and specimens, raw or polished nuggets that were not made into an
  object. It contains:
  - loose photos;
  - one piece folder «Amb-S-001»;
  - a subfolder «كهرمان وانتيكات» (amber & antiques, mixed content), labelled «K&A» on the sheets.
- **AMB-A «تحف الكهرمان»**: amber artifacts and antiques, meaning objects made of or with amber. Examples: boxes, frames,
  necklaces, pendants, brooches, bracelets, pipes, cigarette holders, seals, desk sets, clocks, snuff bottles, mounted
  pieces. It has 252 loose photos and one piece folder «AMB-A-001».
- **AMB-DEC «تحفيات منحوته»**: sculpted carvings (animals, figures, scenes). It is already organised into folders
  «Amb-dec-001» … «Amb-dec-048» with photos named Amb-dec-NNN-k, plus «_Duplicates (مكرر)»; every file in that folder
  is a verified copy of a DEC piece photo.

We are rebuilding this catalog the way we did the rosary catalog:

1. Every physical piece gets its own folder and code, with its photos inside.
2. Every piece gets an Arabic description in a sheet.
3. Identical duplicate copies are set aside.

Your job is **grouping and classification only**. Do not write Arabic descriptions and do not touch Google Drive (read only).

## Paths
- **AMB** = /tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/amb
- **AMB/timeline.json**: every photo in shooting order. Each entry has id (Drive file id), path, cat (ST/A/DEC),
  loc (piece folder name, «(loose)», «كهرمان وانتيكات» or «_Duplicates (مكرر)»), name (file name), dto (EXIF shot
  time) and imgno (camera frame number).
- **AMB/gidx.json**: Drive id → global photo number «#N». The contact sheets use these numbers.
- **AMB/sessions.json**: a list of sessions; each session is a list of ids in time order, with a gap of more than 20 min
  starting a new session. Session k is drawn on AMB/cs/Sk_*.jpg.
  - Tile header: «#N CAT LOCATION», with K&A = «كهرمان وانتيكات» and DUPS = the DEC duplicates folder.
  - Second line: shot time and file name.
- **AMB/th/<id>.jpg**: 400 px thumbnails.
- **High resolution**: `curl -sS -L -o out.jpg "https://lh3.googleusercontent.com/d/<id>=w1600"`. Save your crops under
  AMB/work_<yourname>/ and delete big files when done.
- **AMB/dupgroups.json**: sets of files that share the same EXIF frame (shot time + frame no.), with a perceptual-hash
  distance; 0 means a pixel-identical copy.

## Rules
1. **One piece = one physical object.** It can also be a set that is always shown together and would be sold as one
   item, such as a box with its fitted contents or a pair of matching items. If items in a set are also photographed
   separately, still make one piece and say so in "notes_en".
2. **Use shot order as the strongest hint.** A photographer shoots one object, then the next. Confirm visually:
   - shape, colour, pattern, inclusions, damage;
   - metal fittings, stands, mounts;
   - the background and stand used.
3. **Re-shoots.** The same object can appear in another session, or on a different date inside your sessions. Merge
   those into one piece and say which sessions it appears in.
4. **Existing DEC pieces.** If a loose ST/A/K&A photo shows the same object as an existing Amb-dec-NNN folder, assign it
   to that DEC code (mode "add_to_existing"). Check the DEC photos in your sessions, and the other DEC folders if
   something looks familiar. Every DEC folder can be listed from timeline.json.
5. **Duplicates.** If several files are the same frame and dupgroups distance is 0, keep ONE (prefer the cleanest name,
   without "(1)" or a double dot) and list the others in "duplicates". Different crops or edits of the same frame
   (distance > 0) are NOT duplicates: keep them all.
6. **Category.** By default, a piece stays in the category of the folder its photos are in, because that is the
   owner's own filing.
   - If a piece clearly belongs elsewhere, put the proposed category in "category" and explain in "notes_en". For
     example, an obvious raw stone among the artifacts, or an obvious figurine carving among AMB-A.
   - K&A items must each be classified (ST, A or DEC). If an item is not amber at all, or you cannot tell, set
     "category": "UNSURE" and explain.
7. **Uncertainty.** Set "unsure": true for:
   - uncertain material (is it amber at all? pressed amber? copal? plastic?);
   - uncertain category;
   - uncertain grouping, meaning you are not sure two photos show the same object.

   Explain in "notes_en". Do not guess silently.
8. **Hero.** "hero" is the global # of the photo that best shows the WHOLE piece, used as the sheet image.

## Output
Write AMB/group_<yourname>.json as a JSON list of pieces:

```
{"piece": "<yourname>-01", "mode": "new" | "add_to_existing" | "existing_ok",
 "existing_code": "Amb-dec-0NN or AMB-A-001 or Amb-S-001 or null",
 "category": "ST" | "A" | "DEC" | "UNSURE",
 "photos": [#N, ...], "duplicates": [#N, ...], "hero": #N,
 "type_en": "e.g. raw amber nugget / amber mosaic box / amber necklace / carved rhino figurine",
 "visual_en": "1–3 sentences: what it is, colour, transparency, pattern, size cues, fittings, condition",
 "sessions": ["S09", ...], "unsure": false, "notes_en": "..."}
```

- **mode**:
  - "existing_ok": you checked an existing DEC (or AMB-A-001 / Amb-S-001) folder in your sessions and it holds exactly
    one object.
  - "add_to_existing": loose photos go into that existing piece.
  - "new": a new piece.

  If an existing folder mixes two objects, report it as "existing_ok" with the correct photos, put the stray photos in a
  "new" piece, and explain.
- Every photo number in your sessions must appear exactly once, either in some "photos" or in some "duplicates". This
  includes the DEC and DUPS photos; the DEC duplicates go in "duplicates" of the matching DEC piece.
  - Check this with Python before you finish.
  - In your reply, give the piece count, the uncertain ones, any re-shoot merges, and any problems with existing
    folders.
