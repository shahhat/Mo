# Jewelry & rings catalog (الخواتم والمجوهرات, JWL): rebuilt like the rosary and amber catalogs

Owner's request (verbatim): «كل ما هو نفذ للكهرمان اريد تنفيذه لقسم المجوهرات و الخواتم … بكل التفاصيل التى تناقشنا
فيها و القرارات التى تم بخصوص النص و الاعتماد الاساسي للنصوص هو ما ذكر من ابو على على الفيديوهات باقى النصوص تكون
بنفس الاسلوب و الطريقة ، و قبل البدء يفضل ان تعمل فولدر لفيديوهات الخواتم كمان فعلنا للمسابيح و الكهرمان فى
الفيديوز لتعرف جميع الخواتم المصورة فيديو و تضعها فى مكانها و انت تكود القطع».

JWL root on Drive: 13ArWGSernEYXHNOJ3HLOzBO2AnKkrxqu. All IDs are in `data/drive_ids.json`.

## Starting point (1384 photos, all NIKON D850 with EXIF)
| Folder | Content before |
|---|---|
| «JWL - W القلوب النسائية» | 78 loose + subfolder «كهرمان وانتيكات» (66; jewelry, not amber, despite the name) |
| «JWL-B - مجوهرات بيگلو» | 147 loose + piece folder R050 (3) |
| «JWL-H - مجوهرات حسين جدي» | 134 loose (owner files JWL-0001…0057) + subfolder «خواتم» (2) + the owner's index sheet «فهرس خواتم ومجوهرات - JWL» |
| «JWL-R خواتم عادية» | subfolder «خواتم عادية» (71) |
| «JWL-RS - خواتم نادره منوعه الصاغه» | 233 loose + subfolder «خواتم» (314) |
| «أبناء حسين جدي -JWL-HS» | 113 loose + «خواتم» (215) + piece folders «Ring - 3 - أية الكرسى» (4) and «Ring- 4 - الناس» (4) |

- The owner's index sheet (1QCK8w_LmN0p2nEct0sFxWZbGem6hViF2eHbKGETiqGI, copy in `data/owner_index.csv`) lists
  JWL-0001…0057 with generic visual names («خاتم بحجر كهرماني دائري»). It contains no facts from Abu Ali. It was left
  in place; its codes are kept in Notes as «الأكواد القديمة».
- Other old owner codes found in file names: R002–R013, R024, R043, R050, Ring-3, Ring-4 (`grouping/owner_codes.json`).

## Videos: «JWL - VID»
- New folder «JWL - VID» (15aih4LiBk3d1lC96CZTLEE_qQosOV8ez) in the videos root, next to «ROS - VID» and «AMB - VID».
  It holds server-side copies of the 42 jewelry videos from Phases 01, 02, 06, 07, 08, 09, 11 and 12 (the connector
  cannot make shortcuts). Nothing in the phase folders was moved. After coding, each copy was renamed to its catalog
  code (`videos/video_ops.json`).
- Abu Ali's on-screen texts were read from the frames (`videos/video_captions.json`).
- Two videos appear twice: Phase 08 «Orange-Ring E03» = Phase 09 «Orange-Ring E03 - Final!», and Phase 08
  «Yellow-Ring E02 - Final!» = Phase 09 «Yellow-Ring E02 - Final!» (same footage, caption spacing differs). The Phase 09
  text is used; the Phase 08 copies are named «CODE (Phase 08).mp4».

## Grouping
- EXIF shot time, sub-second and frame number for every photo; sessions split at gaps > 20 min (46 sessions).
- Seven grouping passes over contiguous session ranges (`grouping/GROUP_INSTRUCTIONS.md`, `group_g1…g7.json`).
  Re-shoots were merged: 8 rings photographed in S04 and again in S06 (`grouping/apply_merge.py`).
- A separate cross-check compared every piece against every other range and category (inscription text clusters,
  hero boards, high-resolution engraving and mount). It found no further duplicates (`grouping/DUP_CHECK.md`).
- Duplicates = pixel-identical copies of the same camera frame (hash distance 0, mostly «… (1).jpg»): 426 files.
  Different edits of the same frame were kept.
- Result: **311 photographed pieces** (958 kept photos + 426 duplicates = all 1384) **+ 18 pieces known only from a
  video = 329 catalog rows.**

## Decisions on uncertain grouping/category
| Piece | Decision |
|---|---|
| JWL-W-001, JWL-W-002 | front/back photo pairs accepted as one pendant each (consecutive frames, same bail) |
| JWL-H-003 | one ring although the owner named its photos JWL-0056 and JWL-0057 |
| JWL-H-010 | H (2 of its 3 photos in H; the hallmark photo was in HS) |
| JWL-H-014 | owner codes JWL-0045 + JWL-0046 are one ring |
| JWL-RS-041 | stays RS: front photos filed in RS; its F + oval-cartouche hallmark also occurs on RS rings, so it does not prove HS |
| JWL-RS-033 | modern women's turquoise-and-diamond ring; stays in RS as the owner filed it, Item Category «Women's Ring» |
| JWL-RS-090 | stays RS; hallmark resembles the Hussein Jeddi set (noted, no maker named) |
| JWL-HS-093 | photos were in both HS and RS (files R005); HS because its video names «مهدي جدي» |
| JWL-W-023 | one image of a dinar pendant showing both faces, treated as one pendant |

## Codes
| Category | Codes | Pieces | Photographed | Video only | Kept photos | Duplicates |
|---|---|---|---|---|---|---|
| W «القلوب النسائية» | JWL-W-001 … 049 | 49 | 40 | 9 | 85 | 59 |
| B «مجوهرات بيگلو» | JWL-B-001 … 033 | 33 | 31 | 2 | 94 | 55 |
| H «مجوهرات حسين جدي» | JWL-H-001 … 040 | 40 | 39 | 1 | 132 | 4 |
| R «خواتم عادية» | JWL-R-001 … 013 | 13 | 13 | 0 | 36 | 35 |
| RS «خواتم نادره منوعه الصاغه» | JWL-RS-001 … 097 | 97 | 93 | 4 | 298 | 248 |
| HS «أبناء حسين جدي» | JWL-HS-001 … 097 | 97 | 95 | 2 | 313 | 25 |
| **Total** | | **329** | **311** | **18** | **958** | **426** |

- Photographed pieces are numbered in shooting order; the video-only pieces follow at the end of their category.
- Photos are CODE-N.jpg; -1 is the best full view and the sheet image. Duplicates keep their file names in
  «_Duplicates (مكرر)» inside each category folder.
- The owner's piece folders were renamed in place: R050 → **JWL-B-031**, «Ring - 3 - أية الكرسى» → **JWL-HS-095**,
  «Ring- 4 - الناس» → **JWL-HS-075**. Old codes are in Notes.
- The emptied container subfolders («كهرمان وانتيكات», the three «خواتم», «خواتم عادية») were left in place.

## Videos ↔ pieces (`videos/all_matches.json`)
Each match needs the engraving layout (same words in the same places, same flourishes, chips) and the mount to agree
at high resolution. The maker named in every matched caption agrees with the owner's category of the piece (all
«مهدي جدي» videos → HS, «حسين جدي» → H, «بيكلو» → B), which supports the matches.

**Green (photos + video copy CODE-video.mp4 in the folder), 22 pieces:**
JWL-W-039 (Phase 07 BRACELET), JWL-B-002 (Green Ring), JWL-B-031 (Phase 12 بيكلو-حجر تيموري), JWL-H-028 (Orange-Ring
E03, two edits), JWL-H-036 (Product F), JWL-RS-001 (Product D), JWL-RS-033 (Product 7), JWL-RS-054 (02/13),
JWL-RS-072 (02/05), JWL-RS-074 (Product E), JWL-RS-076 (02/02), JWL-RS-091 (Basmala Ring), JWL-HS-006 (02/06),
JWL-HS-008 (Product 11), JWL-HS-016 (Brown Ring), JWL-HS-064 (Yellow Ring), JWL-HS-077 (K), JWL-HS-080 (Orange
Ring), JWL-HS-081 (Product 3), JWL-HS-091 (Product 8), JWL-HS-093 (Product 9), JWL-HS-095 (Phase 12 آية الكرسي).
- JWL-HS-091 (turquoise) and JWL-HS-093 (jade) match on the mount only: the stones are plain. The mounts agree part for
  part (and on HS-093 the hallmark layout); noted in Notes.

**Red (video only; CODE-1..3 stills from the video + CODE-video.mp4), 18 pieces:**
JWL-W-041 (C016 silver heart with dirham), JWL-W-042 (C017 gold heart with dinar), JWL-W-043 (Go'raan agate),
JWL-W-044 (jade plaque, R021), JWL-W-045 (Heart-Stone), JWL-W-046 (Mughal necklace), JWL-W-047 (Orange-Stone pendant,
R020), JWL-W-048 (Yellow-Stone), JWL-W-049 (Phase 11 agate, AMB1), JWL-B-032 (Al-Ekhlas Ring), JWL-B-033 (Orange-Ring
E02), JWL-H-040 (Phase 11 «يا شفيع المذنبين», RING-1), JWL-RS-094 (Product 10, «آصف»), JWL-RS-095 (Orange Ring with
Lobes), JWL-RS-096 (Yellow-Ring E03), JWL-RS-097 (Yellow-Ring E02, two edits), JWL-HS-096 (02/04), JWL-HS-097
(Orange-Ring E04).
- Category of a video-only piece = the maker in its caption (مهدي جدي → HS, بيكلو → B, حسين جدي → H); rings with no
  maker or another maker → RS; pendants, necklaces and unmounted engraved stones → W (Item Category «Engraved Stone» for
  the four loose stones).
- Stills: square crop around the object, the video watermark painted out, the photographer's logo from a catalog photo
  added in the darkest corner (`videos/frames/compose_jwl.py`, `spec.json`, sha256 in `final_sha256.json`).

**Video sheet** (1hO-BJKp1qb1Usf2MjUXmEgG0zwVVCMRfRxLjeZxQQ5U): the Item Name cell of the 40 jewelry-video rows now
holds the catalog code (`videos/vsheet_updates.json`). The four cells that held an owner code keep it in brackets:
«JWL-B-031 (R050)», «JWL-HS-095 (R3)», «JWL-H-040 (RING-1)», «JWL-W-049 (AMB1)». The two Phase 08 re-edits have no
row of their own. Verified by CSV export: 40/40.

## Descriptions
- **Video pieces (40):** Abu Ali's on-screen text, word for word, with spelling and punctuation fixes only (hamzas,
  ة/ه, ى/ي, tanween alif, spacing, commas; «مديل» → «موديل», «الكولمبي» → «الكولومبي»). `descriptions/captions_fixed.py`.
- **All other pieces (289):** written in Abu Ali's pattern (`descriptions/DESCRIBE_JWL.md`): object + one evaluative
  adjective + «يحمل حجر …» + engraving + maker phrase.
  - Stone named only when visually evident (عقيق، فيروز، جيد, lapis on JWL-RS-048; black opal on JWL-R-005 from its GFCO
    report). Other stones by colour; the likely gem is in Notes.
  - Inscriptions quoted only where read at high resolution (seal engravings flipped to read); partial readings with ؟
    in Notes only.
  - Maker = the owner's filing: B «صياغة الأستاذ الكبير بيكلو», H «صياغة أسطورة المجوهرات الأستاذ حسين جدي», HS «من
    صياغة أبناء الأستاذ حسين جدي»; W, R, RS: none.
  - No metal, era, origin, «متحفي» outside a video text; «ذهبي اللون/فضي اللون» describes colour only.
- Hallmarks seen (e.g. «جدي» + F + «تهران» on the H rings, «بیگلو» on B rings, «شایق / طهران», «آذری», «750», «21K»,
  «925») are quoted in Notes, never in the description.

## Risks flagged in Notes
- **JWL-W-039:** the video text says «قلادة» (necklace); the piece is a bracelet (the video file is named BRACELET).
  Kept as Abu Ali wrote it; the owner may want to correct the word.
- **JWL-HS-016:** the video calls the stone tourmaline; in the photos it looks dark red (garnet-like). Not verified.
- **JWL-B-002:** the video says Colombian emerald; not verifiable from photos.
- Coin pieces (JWL-W-009, 020, 022, 023, 025, 036, 037): authenticity not judged; the coins in the sets W-025 and W-036
  are called «مسكوكة» because they may be replicas.
- JWL-W-012: cracked stone held by two rivets; material uncertain.

## Sheets (one per category, copied from the amber sheet for its format)
| Sheet | ID | Rows |
|---|---|---|
| Knooz (Desc._) Sheet - JWL-W | 1zCn3Um4qw29eph1zYgvddUzjsrnFPO5Gq1jhF5ixz24 | 49 |
| Knooz (Desc._) Sheet - JWL-B | 1krtrmmn8NTK-5ipZNa7ZK6c2mrmUSW6wLVBMY7RfLi8 | 33 |
| Knooz (Desc._) Sheet - JWL-H | 1n1ZTPqRSV0WLzBHN34Lw9N0dt71GWv0JBDNx-avcAeI | 40 |
| Knooz (Desc._) Sheet - JWL-R | 1zqSJrVuzNJIlClUzpkuTZJTPxyeI5rdS2ecC9Y5nQ1k | 13 |
| Knooz (Desc._) Sheet - JWL-RS | 17TlaTWp6WZN9QRnXuwdMTHMn4LV6kQcDIwYncefoZbA | 97 |
| Knooz (Desc._) Sheet - JWL-HS | 17h0kItsnE-_DKKzJf-R856Q8TssiuseOJQU_749Nai8 | 97 |

Columns: [no., IMAGES (=IMAGE of CODE-1, w800), Description, Item Name (code), Item Category, Price (empty), Notes];
column A text; rows 330 px.
- `data/sheet_payload_r1.json` was written to all six sheets and verified by CSV export: 329 rows, 1974 cells, 0
  mismatches.
- New spreadsheets block IMAGE() of external URLs until an owner/editor clicks «Allow access» once in a desktop browser;
  until then column B shows #REF! (the amber sheets were already allowed).

## Drive execution and verification
- 6 executor batches (`tools/EXEC_JWL.md`, logs in `data/exec/`): 326 folders created, 3 renamed in place, 958 photos
  moved and renamed, 426 duplicates moved; 0 failures.
- 40 video copies `CODE-video.mp4` made in the piece folders; 22 folders coloured green, 18 red; the 42 copies in
  «JWL - VID» renamed to codes (`tools/EXEC_VIDEOS.md`, `data/exec/exec_videos_log.json`).
- Re-walk of the JWL root (`data/drive_tree_after.json`): every one of the 958 photos is CODE-N.jpg in its own folder,
  all 426 duplicates are in «_Duplicates (مكرر)», no loose photo, no duplicate folder, nothing lost; the only other files
  are the six new sheets and the owner's index sheet. «JWL - VID» re-listed: 42/42 names correct.

## QC round (independent check of every description against the photos)
Three reviewers re-checked all 311 photographed rows (`qc/QC_JWL.md`, `qc/qc_qc1..3.json`): object type, stone colour
and shape, every quoted inscription re-read at high resolution, mount details, maker phrase, hero photo. All quoted
inscriptions were confirmed. Accepted fixes (`tools/build_final.py`, `data/r2_changes.json`):
| Code | Fix |
|---|---|
| JWL-W-014 | stone is a long oval, not rectangular |
| JWL-W-032 | bail is plain (no stones); notes record the two stamps + F |
| JWL-H-029 | Surat an-Nasr is in six lines, not seven |
| JWL-B-008 | «ذهبي اللون» removed (metal tone doubtful) |
| JWL-B-030 | «(توكلت على الله)» removed from the description: only «على الله» is certain; reading moved to Notes |
| JWL-HS-037 | «فضية اللون» removed (the ring is gold-coloured) |
| JWL-HS-082 | «منقّطاً» removed (the dots are the letters' dots) |
| JWL-HS-076, JWL-HS-079 | Notes: old codes R010/R012 come only from a hallmark photo's file name and are uncertain |
| JWL-W-044, 047, 049, JWL-H-040 | Notes: the owner's video-sheet names R021, R020, AMB1, RING-1 |

Kept as written, with reasons: JWL-RS-048 «اللازورد» (blue with gold flecks, unmistakable); JWL-R-005 «أوبال أسود
طبيعي» (from the GFCO report photographed with the ring). Flag only: JWL-W-039 «قلادة» vs bracelet.

## Owner rule of 29 Oct: Abu Ali's texts are the authority; our texts as close as possible to his way
- **Which Abu Ali text:** for the 40 video pieces the on-screen text (what was published) stays the description. It was
  compared with his text in the video sheet's Description column (`videos/vsheet_vs_onscreen.json`): 24/40 identical,
  the rest differ only in word order, except three with an extra fact, now in Notes: JWL-W-043 «لمطلع القرن الثالث هجري»,
  JWL-H-028 «على الأغلب» (12th century), JWL-B-032 «خاتم متحفي … قطعة بمتحف». Phase 01 «Product (10)» has a template in
  the sheet, not a text.
- The owner's index sheet «فهرس خواتم ومجوهرات - JWL» has generic visual names, not Abu Ali's wording; not used for
  descriptions (pending the owner's confirmation).
- **Restyle of the other 289 descriptions** (`restyle/RESTYLE_JWL.md`, corpus = his 40 captions): same facts, his voice —
  «خاتم نفيس/استثنائي/نادر (بموديل استثنائي) يحمل حجر … منقوش بخط … بعبارة (…)، صياغة …». The itemised mount details
  (claws, bezels, shoulders, shanks, metal colour) were removed; «بموديل استثنائي/رائع» marks an unusual mount (about 1
  ring in 3). Verified inscriptions kept; nothing added. 8–24 words (average 14); no two descriptions identical.
  The 13 QC fixes are included. Written to the six sheets as `data/sheet_payload_r3.json` and verified by CSV export:
  329 rows, 1974 cells, 0 mismatches. The sheets' images now render (the owner opened them in Chrome).

## Stills for the 18 red folders (29 Oct)
- The owner uploaded the 54 stills to the JWL upload folder; all 54 are byte-identical to the originals (sha256 vs
  `videos/frames/final_sha256.json`).
- After the connector was signed in again it no longer offers the move/rename tool, so the stills were **copied**
  server-side into their red folders (`videos/frames/copy_ids.json`; the copies' sha256 also match). Every red folder
  now holds CODE-1..3.jpg + CODE-video.mp4 (re-listed: 18/18).
- The 54 uploaded originals are still in the upload folder «_من الجهاز - JWL (للمقارنة)»; they can be deleted there.
- The sheet image of the 18 video-only rows now shows CODE-1 (`data/sheet_payload_r4.json` = live state); the formulas
  were read back and all 18 render.

## Still open
- PC comparison (`pc/knooz_compare_jwl.ps1`): waiting for the owner to run it and upload `_missing_on_drive` into the JWL
  upload folder.
