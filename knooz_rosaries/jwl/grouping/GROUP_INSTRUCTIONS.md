# Group the jewelry & rings photos into pieces (Islamic Treasures, Kuwait)

The owner sells rare Islamic collectibles. His jewelry root folder «JWL» on Google Drive has 6 category folders. The
category is mostly **who made the piece** (the owner's own filing):

| Code | Folder | Meaning |
|---|---|---|
| W | «JWL - W القلوب النسائية» | women's pendants ("hearts"), necklaces and other women's jewelry. Subfolder «كهرمان وانتيكات» (labelled **K&A** on the sheets) holds more pendants; its name is misleading, treat it as a plain container. |
| B | «JWL-B - مجوهرات بيگلو» | pieces by the master jeweller **Biglou (بيكلو)**. Subfolder «R050» is an existing piece folder (one ring). |
| H | «JWL-H - مجوهرات حسين جدي» | pieces by the legendary jeweller **Hussein Jeddi (حسين جدي)**. Subfolder «خواتم» (RINGS-SUB) is a container. |
| R | «JWL-R خواتم عادية» | ordinary rings. Subfolder «خواتم عادية» (R-SUB) is a container. |
| RS | «JWL-RS - خواتم نادره منوعه الصاغه» | rare rings by various goldsmiths. Subfolder «خواتم» (RINGS-SUB) is a container. |
| HS | «أبناء حسين جدي -JWL-HS» | pieces by **Hussein Jeddi's sons** (e.g. «مهدي جدي»). Subfolders «Ring - 3 - أية الكرسى» (Ring-3) and «Ring- 4 - الناس» (Ring-4) are existing piece folders; «خواتم» (RINGS-SUB) is a container. |

We are rebuilding this catalog the way we did the rosary and amber catalogs:
1. Every physical piece gets its own folder and code, with its photos inside.
2. Every piece gets an Arabic description in a sheet (done later, not by you).
3. Identical duplicate copies are set aside.

Your job is **grouping and classification only**. Do not write Arabic descriptions. Do not touch Google Drive (read only).

## Paths
- **JWL** = /tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/jwl
- **JWL/timeline.json**: every photo in shooting order. Each entry has id (Drive file id), path, cat (W/B/H/R/RS/HS), loc
  (subfolder name or «(loose)»), name (file name), dto (EXIF shot time), imgno (camera frame number) and n (global
  photo number «#N»).
- **JWL/sessions.json**: a list of sessions; each is a list of ids in time order (a gap of more than 20 min starts a new
  session). Session k is drawn on JWL/cs/Sk_*.jpg (36 tiles per page).
  - Tile header: «#N CAT LOCATION». LOCATION is K&A, RINGS-SUB, R-SUB, R050, Ring-3, Ring-4, or empty for loose.
  - Second line: shot time and file name.
- **JWL/th/<id>.jpg**: 400 px thumbnails.
- **High resolution**: `curl -sS -L -o out.jpg "https://lh3.googleusercontent.com/d/<id>=w1600"`. Use it to compare
  close cases (engraving, stone pattern, mount details, hallmarks). Save crops under JWL/work_<yourname>/ and delete big
  files when done.
- **JWL/dupgroups.json**: sets of files sharing the same EXIF frame (shot time + frame no.), each member with a
  perceptual-hash distance "d" to the first member; 0 means a pixel-identical copy. Files named «… (1).jpg» are usually
  exact copies.

## Rules
1. **One piece = one physical object** (one ring, one pendant, one necklace…). A set that is always shown together and
   would be sold as one item (e.g. a necklace with matching earrings in one box) is one piece; say so in "notes_en".
2. **Shot order is the strongest hint.** The photographer shoots one object from several angles, then the next. Confirm
   visually: stone colour and shape, the engraving layout and script, the mount (bezel, shoulders, openwork, prongs),
   the metal colour, hallmarks, damage.
   - Rings look alike. Do not merge two rings unless the stone's engraving/pattern AND the mount match.
   - A close-up of a hallmark or of the inside of the shank belongs to the ring shot just before/after it if the metal
     and shape match; say so.
3. **Re-shoots.** The same object can reappear in another session of yours. Merge it into one piece and list the
   sessions.
4. **Existing piece folders** (R050, Ring-3, Ring-4): if they hold one object, report "existing_ok" with that code; add
   loose photos of the same object with "add_to_existing". If a folder mixes two objects, report the correct photos as
   "existing_ok", put the stray photos in a "new" piece, and explain.
5. **Duplicates.** If several files are the same frame and the dupgroups distance is 0 (or the files look pixel-identical,
   e.g. «X (1).jpg» and «X.jpg»), keep ONE (prefer the name without «(1)») and list the others in "duplicates".
   Different crops or edits of the same frame (distance clearly > 0, visibly different) are NOT duplicates: keep them.
6. **Category.** By default a piece stays in the category of the folder its photos are in.
   - If its photos are split across categories, or it clearly belongs elsewhere (e.g. a pendant among the plain rings,
     or a hallmark that names another maker), propose the category in "category" and explain in "notes_en".
   - If the object is not jewelry at all (a loose engraved stone, a coin, a rosary…), keep the folder's category but set
     "unsure": true and say what it is.
7. **Uncertainty.** Set "unsure": true for uncertain grouping, category or object type, and explain in "notes_en". Do
   not guess silently.
8. **Hero.** "hero" is the global # of the photo that best shows the WHOLE piece (front view preferred), used as the
   sheet image.
9. **Facts to record when visible** (they will feed the descriptions): stone colour and likely material only as a visual
   guess (say "looks like agate/carnelian/turquoise/jade…"), whether the stone is engraved and the script style if
   recognisable, any legible words of the engraving (only if you can actually read them; mark "?" when unsure), the
   metal colour (silver-tone / gold-tone), hallmarks or signatures you can read, and the photo # where you saw each.

## Output
Write JWL/group_<yourname>.json as a JSON list of pieces:

```
{"piece": "<yourname>-01", "mode": "new" | "add_to_existing" | "existing_ok",
 "existing_code": "R050 | Ring-3 | Ring-4 | null",
 "category": "W" | "B" | "H" | "R" | "RS" | "HS",
 "photos": [#N, ...], "duplicates": [#N, ...], "hero": #N,
 "type_en": "e.g. men's ring with engraved carnelian / heart-shaped pendant / jade necklace",
 "visual_en": "1–3 sentences: stone, engraving, mount, metal colour, condition",
 "facts_en": "readable inscriptions, hallmarks, signatures with the photo # where seen; empty if none",
 "sessions": ["S04", ...], "unsure": false, "notes_en": "..."}
```

- Every photo number in your range must appear exactly once, in some "photos" or some "duplicates". Check this with
  Python before you finish.
- In your reply give: the piece count, the uncertain ones, any re-shoot merges, problems with existing folders, and any
  piece you think may also appear outside your range (so the lead can merge across ranges).
