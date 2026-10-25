# Amber catalog (الكهرمان): rebuilt like the rosary catalog

Owner's request: «عاوز كل الى عملته فى فولدر المسابيح تعمله فى الفولدر الكهرمان ده» (amber root
1UpIxhI5FdCapcBoHpZcHEcWHJP05hCOQ).

The work covered the steps done for the rosaries:
- group loose photos into pieces;
- give every piece a coded folder with its photos named CODE-N;
- set duplicates aside;
- write house-style descriptions and one sheet per category;
- link the promo videos (green and red folders);
- write the codes into the video sheet;
- add a «غير مصنف» folder and sheet for what we are not sure about.

## Starting point (611 photos)
| Folder | Content before |
|---|---|
| « AMB-ST- أحجار الكهرمان» | 65 loose photos, folder Amb-S-001 (6), subfolder «كهرمان وانتيكات» (50, mixed) |
| «AMB-A-تحف الكهرمان» | 252 loose photos, folder AMB-A-001 (3) |
| «تحفيات منحوته - AMB-DEC» | Amb-dec-001 … 048 (182 photos, already coded) and «_Duplicates (مكرر)» (53) |

- No description sheet existed in the amber folders.
- The raw-sessions folder (79–82) has no amber items.

## Grouping
- Every photo's EXIF was read (shot time, camera frame number). Sessions were split at gaps of more than 20 minutes.
- Five grouping passes covered S00–S37: `data/group_g1..g5.json`, instructions in `GROUP_INSTRUCTIONS.md`.
- Each piece's photos were confirmed visually, and borderline cases were checked at high resolution.
- Re-shoot merged: the S09 stone (Aug 2021) is the same stone as S29 #251/#252 and the 4-view composite #258
  (Jan 2023), giving **AMB-ST-004** with 7 photos. S29 #253–257 is a second, taller stone (AMB-ST-017).
- Duplicates are 83 pixel-identical copies of the same camera frame (hash distance 0). Different crops of one frame
  were kept.
- Result: **194 pieces** (188 photographed + 6 known only from a video), 528 kept photos, 83 duplicates. Every one of
  the 611 photos is accounted for exactly once (`merge.py` asserts it).

## Codes
| Category | Codes | Pieces | Notes |
|---|---|---|---|
| AMB-ST «أحجار الكهرمان» | AMB-ST-001 … 030 | 30 | Amb-S-001 renamed **AMB-ST-001** (same folder); 028, 029 came out of «غير مصنف» in round 9; 030 = A009 stone, video only (round 8) |
| AMB-A «تحف الكهرمان» | AMB-A-001 … 119 | 119 | AMB-A-001 kept; 102–107 are video-only. Round 10 deleted the old 111 (one photo of a rosary) and renumbered 112–120 → 111–119. |
| AMB-DEC «تحفيات منحوته» | Amb-dec-001 … 049 | 49 | owner's codes kept; **Amb-dec-049** = Gdańsk 997–1997 carved nugget (was in «كهرمان وانتيكات») |

- Confirmed pieces are numbered in shooting order with no gaps. The video-only pieces follow, then the «غير مصنف»
  pieces at the end of their suggested category.
- Photo names are CODE-N.jpg with the best full view as -1, which is also the sheet image. Existing Amb-dec-NNN-k names
  were kept.
- Reclassified:
  - AMB-ST-005 was filed in AMB-A: a natural polished stone on a wooden display base.
  - Amb-dec-049 was a K&A item: a carving.
  - All «كهرمان وانتيكات» items were filed (ST, or DEC for the Gdańsk piece), so that folder is now empty. It was left
    in place.

## «غير مصنف» (folder 1f-Yy6gimcCavkd0VcsYlBVzXGDUXPdwN, sheet 1VpcQmj5mmeG2Jc159xysTBR-_rgRuTikO8nLi63n0OE)
Rule used:
- If the doubt is natural vs pressed amber, the piece stays in its category (it is amber either way) and Notes say so.
- If the piece may not be amber at all, or it is unclear what it is, or it may duplicate another piece, it goes here.

| Code | Why | Question for Abu Ali |
|---|---|---|
| AMB-A-108 | close-up of a Königsberg maker's plate (Norddeutsche Bernstein-Industrie) only | which piece carries it? |
| AMB-A-109 | goblet set: cherry-red stem and mouthpiece | amber or faturan? what is the set? |
| AMB-A-111 | very dark bead strand, close-up only | amber or faturan? full photos? |
| AMB-A-112 | pair of cherry-orange mouthpieces | amber or faturan? |
| AMB-A-113 | cherry-red bead necklace | cherry amber or faturan? |
| AMB-A-114 | auction-catalogue clipping (meerschaum and amber pipe, melusine bowl, 1914) | which pipe? |
| AMB-A-115 | large old "trade" beads | amber or copal/resin? |
| AMB-A-116 | desk seal with insects | amber or copal? |
| AMB-A-119 | closed cube box, Russian «Сила Земли – Дар Солнца» (round 7) | what is in it, and is it a separate item? |
| AMB-ST-028 | lot of sawn orange blocks | natural, pressed or bakelite? |
| AMB-ST-029 | one photo of a polished stone | same stone as AMB-ST-014? |

## Videos (copied, never moved)
| Video | Piece | Folder |
|---|---|---|
| A003 (pipe, «josef osterman») | AMB-A-050 (case stamped JOSEF OSTERMANN WIEN) | green |
| A009 | AMB-ST-024 (its files were named A009-1/2/3) | green |
| A012 | Amb-dec-007 | green |
| A014 | AMB-A-084 (clock in a nugget) | green |
| A016 | Amb-dec-008 | green |
| A017 (Gdańsk 1000 years) | Amb-dec-049 | green |
| A021 (bronze horse, NBJ) | AMB-A-015 | green |
| «من تحف الكهرمان المنحوتة» (phase 12, higher-quality copy) | Amb-dec-003 | green |
| A001 (RK, USSR) | AMB-A-102 | red, video only |
| A002 (+ draft «ANTIQUE MERMAID») | AMB-A-103 | red, video only |
| A004 (+ draft «Broush (Rosary)») | AMB-A-104 | red, video only |
| A013 | AMB-A-105 | red, video only |
| A015 | AMB-A-106 | red, video only |
| A020 | AMB-A-107 | red, video only |

- «Amber Faces» (Phase 05) is the boxed pendant set **AMB-A-057**. It has no video file, so there is no colour.
- «Book holder» (Phase 06) is a painted miniature, not amber; it was not linked.
- Red folders hold CODE-video.mp4 plus a 200 px still copied from the video-sheet image. All six stills were
  sha256-verified after upload.
- Checked and rejected:
  - A020 ≠ #5 (black base);
  - A004 ≠ the necklace in the SBM box (AMB-A-096) and ≠ the bolt-ring necklace (AMB-A-053);
  - A015's crimson case ≠ the maker's plate leather (#30);
  - A013 ≠ the octagonal clock AMB-A-083.

## Video sheet (1hO-BJKp…QxeRt0yvf80gc4N), Item Name set to the code
- Phase 04: E5 AMB-ST-024; E8 Amb-dec-007; E9 AMB-A-105; E10 AMB-A-084; E11 AMB-A-106; E12 Amb-dec-008;
  E13 Amb-dec-049.
- Phase 05: E16 AMB-A-057.
- Phase 06: E2 AMB-A-103; E5 AMB-A-050; E6 AMB-A-104.
- Phase 07: E13 AMB-A-102.
- Phase 01 had no Item Name column, so header «Item Name» was added in F1, with F6 AMB-A-107 (A020) and F7 AMB-A-015
  (A021).

## Sheets (copies of the rosary sheets, same layout)
| Sheet | ID | Rows |
|---|---|---|
| Knooz (Desc._) Sheet - AMB-ST | 1vskrluZD4bPgjTtLkpXTVFmf6L75j6Y9NdoCg9z_H9Q | 27 |
| Knooz (Desc._) Sheet - AMB-A | 1mMNM0_EEwvTK8bMLmNG4P3ka3tOmhuW2ixrSO-wmDzg | 110 |
| Knooz (Desc._) Sheet - AMB-DEC | 1jLtyZVTNW9Bc0FB7YQXkJoP_tPHq6Val3SpYxgW1-x0 | 49 |
| Knooz (Desc._) Sheet - غير مصنف (كهرمان) | 1VpcQmj5mmeG2Jc159xysTBR-_rgRuTikO8nLi63n0OE | 11 (+H «القسم المقترح», I «السؤال لأبو علي») |

- Columns: [no., IMAGES, Description, Item Name, Item Category, Price (empty), Notes]. Column A is text, and row
  height is 330.
- Descriptions follow `STYLE_GUIDE_AMBER.md` and `DESCRIBE_AMBER.md`: 20–32 words, no Latin letters or digits except
  quoted owner facts (RK, SBM, NBJ).
- Origin, factory or maker appears only where the owner's video-sheet text gives it. That covers 102, 103, 104, 105,
  106, 107, 015, 050, 084, ST-024, dec-007, dec-008, dec-049 and 057.
- Marks seen on objects (SBM, Staatliche Bernstein-Manufaktur, NB J, dates, monograms, signatures) are quoted in
  Notes only.

## Risks flagged in Notes
- **Listing restrictions:**
  - AMB-A-097, 099, 101: DAF stick pins with the swastika in the emblem.
  - AMB-A-102: hammer-and-sickle orders.
  - AMB-A-016: «Ostpreussenfahrt 1938» plaque.
  - AMB-A-100: «Luftsport hilft Deutschland» badges.
- **Pressed amber possible** (descriptions never say «طبيعي»): AMB-A-009 column, 040, 045, 056, 062, 070, 082, 093,
  098, 100, AMB-ST-016.
- **Single photo or no full view:** many AMB-A pieces. The single-photo pieces are listed in Notes.

## Drive operations
- 138 folders created, 346 photo moves or renames, 30 duplicate moves into the new «_Duplicates (مكرر)» folders in ST
  and A (DEC duplicates were already there).
- Logged in `data/exec_log_1..5.json`.
- Re-listed publicly afterwards: 528/528 photos have the right name in the right folder, all 83 duplicates are in
  «_Duplicates», there are no duplicate folders, and no loose photo is left.
- Full mapping (old name → new name, Drive IDs, texts): `data/amber_catalog.json`.

## Round 7: photos from the owner's PC (collect- NOV 25)
The owner ran `pc/knooz_compare_amb.ps1` on «الكهرمان -AMB» and uploaded `_missing_on_drive` (see `pc/README.md`).

**Manifest** (`data/round7_pc_manifest.json`): 448 photos on the PC, 0 without EXIF.

| PC folder | On Drive | Missing |
|---|---|---|
| أحجار الكهرمان | 116 | 0 |
| تحف الكهرمان | 231 | 9 |
| تحفيات منحوته | 83 | 9 |

99 kept Drive carving photos are not on the PC. This is information only; nothing was changed for it.

**The 18 missing photos.** Each was checked by eye against the catalog. The carving photos were also checked by
hash: the closest distance to any Drive photo was 43, so none is a duplicate. All 18 were moved out of the upload
folder and renamed (`data/round7_pc_photos.json`).

| Piece | PC files | Result |
|---|---|---|
| AMB-A-110 | fd (52), fd (54), fd (55) | Resolved. The «غير مصنف» pipe case holds a briar pipe with an amber stem: same case, same wear. Folder moved to AMB-A with the same code; the old case photo is now AMB-A-110-4. Category «Amber Pipe». Stamp «PRIMA» and «A.S» quoted in Notes (A. Schulz? unconfirmed). |
| AMB-A-117 (new) | fd (43), fd (44), fd (45) | Silver-tone hinged bracelet with an insect-amber cabochon. Close-ups only. |
| AMB-A-118 (new) | fd (49), fd (51) | Glass box set: necklace and earrings, tags «Natur Bernstein – GENUINE AMBER». |
| AMB-A-119 (new, «غير مصنف») | fd (36) | Closed cube box with «Сила Земли – Дар Солнца». Not the AMB-A-109 goblet box. |
| Amb-dec-010 | DSC_9619 | Amb-dec-010-2 |
| Amb-dec-017 | DSC_4392 | Amb-dec-017-3 |
| Amb-dec-020 | DSC_4463 | Amb-dec-020-3 |
| Amb-dec-023 | DSC_4828, DSC_4841 | Amb-dec-023-2, -3 (the "one photo only" note was removed) |
| Amb-dec-024 | DSC_4851 | Amb-dec-024-5 |
| Amb-dec-025 | DSC_4873 | Amb-dec-025-5 |
| Amb-dec-028 | DSC_5097 | Amb-dec-028-4 |
| Amb-dec-030 | DSC_9722 copy 2 | Amb-dec-030-6 |

**Sheets**
- AMB-A: rows 109–111 added (110, 117, 118), with the hero photo as the image.
- «غير مصنف»: AMB-A-110 removed, AMB-A-119 added, rows renumbered 1–11.
- AMB-DEC: 8 Notes cells name the added files.
- Six Notes cells still used internal grouping ids from before the codes existed. They now use the codes:
  - AMB-ST-010 → AMB-ST-011-3;
  - AMB-ST-011 → AMB-ST-010;
  - AMB-ST-014 → AMB-ST-029;
  - AMB-A-084 → AMB-A-086;
  - AMB-A-086 → AMB-A-084;
  - AMB-ST-029 → AMB-ST-014.
- "#n" in Notes means photo CODE-n. All 528 earlier photos were checked to confirm this.

**Verification**
- All four sheets were exported as CSV and compared cell by cell with `data/sheet_payload.json`, which now holds
  the live state: 0 mismatches.
- The image formulas, text format and 330 px row height of the new rows were read back.
- Drive was re-walked: 865 entries.
  - All 19 file operations are at the right path.
  - 552 photos are named CODE-N inside folder CODE: 528 + 18 + the 6 video stills.
  - 83 duplicates, 14 videos.
- The upload folder now holds only `_missing_on_drive/_manifest.csv` and empty sub-folders. The blocked script
  renamed «_ملغي …» is still there but hidden from the public listing. It can be deleted once the owner approves.

## Round 8: full QC + descriptions in Abu Ali's style
Owner's report: some sheet images had nothing to do with their description, and AMB-A-119 "does not exist". He also
asked for the descriptions to follow Abu Ali's video-sheet style, and for Abu Ali's own texts to be used as-is with
spelling fixes only.

**How it was checked**
- Mechanical: each of the 197 sheet images is the -1 (or chosen) photo inside the folder of its own row code. There
  were 0 mismatches, so every error was in what the photos show.
- Visual: five reviewers opened a contact sheet of every photo in every folder, plus the video frames where a video
  exists (`qc/QC_INSTRUCTIONS.md`, results in `qc/out_b1..b5.json`). The coordinator re-checked every video piece and
  every serious finding at full resolution.

**Errors found and fixed**

| Piece | Error | Fix |
|---|---|---|
| AMB-ST-024 / video A009 | The A009 video was linked by file name only (three photos were named A009). The video shows a different stone: glossy, polished deep red, on a wooden board with a brass plaque. AMB-ST-024 is a matte, pitted stone. Its description had also copied the A009 caption ("special editions of German factories of the last century"). | New code **AMB-ST-030**, a red folder (video only). The video copy was moved there and renamed AMB-ST-030-video.mp4, and a 200 px still was added (sha256-verified). The green colour came off AMB-ST-024. In the video sheet, Phase 04 E5 now reads AMB-ST-030. AMB-ST-024 got a new description and a corrected note. No catalog photo shows the A009 stone (all 29 stones compared). |
| AMB-A-001 | The folder held two different pipes. The owner's two photos show a brown bowl with a hinged gilt lid. Two photos added in round 1 show a cream bowl with a pierced gilt gallery and an amber stem in a red velvet case, plus a closed inlaid box. | The cream pipe and the box became **AMB-A-120** (AMB-A-120-1/-2). The owner's photos are now AMB-A-001-1/-2. Row 2 has a new image, description, «Pipe» category and notes, and row 112 was added. |
| AMB-A-084 / 086 | Notes said "photographed separately". Video A014 shows the clock and the thermometer together as one set. | Notes in both rows updated. |
| AMB-A-117 | The description said one cabochon. The photos show two different stones on two panels. | New description and note. |
| AMB-A-118 | "A pair of earrings" is not supported: the two drops don't match and no ear fittings are visible. | Description and note corrected. |
| AMB-A-110 | The mouthpiece material is doubtful (a very even orange) and the collar is gold-tone. | Category «Pipe», and the amber is not named. |
| AMB-A-083 | Notes said photos #2 and #3 are identical. They are not. | Note fixed. |
| AMB-A-106 | Notes said about 14 mouthpieces. The full video frame shows 15. | Note fixed. |
| Amb-dec-003 | The sheet image was a confusing top view. | Sheet image is now Amb-dec-003-5 (side view). |
| AMB-ST-010 / 011 | Owner-photo AMB-ST-011-3 is more likely ST-011 (crack and banding). | Notes updated (still unconfirmed). |

AMB-A-119 exists: folder «غير مصنف»/AMB-A-119 and row 9 of the «غير مصنف» sheet. It is not in the AMB-A sheet by
design.

**Descriptions**
- **Owner texts:** 14 pieces carry Abu Ali's video-sheet text as the Description, with spelling fixes only
  (`qc/owner_desc.json`): AMB-A-015, 050, 057, 084, 102–107, AMB-ST-030, Amb-dec-007, 008, 049. Their Notes now say
  so instead of quoting the text again.
  - Fixes were limited to:
    - ه→ة, hamzas, punctuation, and «ال RK»→«الـRK»;
    - «انتاح»→«إنتاج», «اغدانسك»→«غدانسك» and «osterman»→«Ostermann», the last per the case stamp;
    - in A021, the repeated phrase removed;
    - in A020, the second «حيث» changed to «والتي».
  - «الشجري» (A004) was kept as his trade term.
- **All other pieces (184):** rewritten in his shape:
  - object noun + «من الكهرمان» + one identifying feature + one appreciative phrase;
  - 8–22 words, MSA.
- **What the new descriptions leave out:** no origin, factory, era, rarity or museum claim and no «طبيعي» unless the
  piece's own source gives it. Where the material is doubtful, «من الكهرمان» is left out. These are checked by
  `qc/build_r8.py`.

**Verification:** all four sheets were exported and compared cell by cell with `data/sheet_payload.json` (0
mismatches). The new image formulas, text format and row heights were read back. The Drive tree was re-walked.

## Round 9: no «غير مصنف» in the amber catalog; rosary check
Owner's request:
- delete the comparison upload folder;
- the amber catalog must have no «غير مصنف»: stones go to أحجار الكهرمان, carved pieces to تحفيات منحوتة, and
  anything else to تحف الكهرمان;
- every amber rosary belongs in the rosary catalog (ROS- مسابح).

**What changed**
- Upload folder «_من الجهاز - الكهرمان -AMB (للمقارنة)» moved to the trash. Its manifest is kept in
  `data/round7_pc_manifest.json`.
- The 11 «غير مصنف» piece folders were moved, keeping their codes:

  | Destination | Pieces |
  |---|---|
  | AMB-A | 108, 109, 111, 112, 113, 114, 115, 116, 119 |
  | AMB-ST | 028, 029 |

  None of them is a carving.
- Their rows were added to the AMB-A and AMB-ST sheets in code order. AMB-A now runs 001–120 with no gaps, and
  AMB-ST runs 001–030.
- In their Notes, the "why unclassified" wording was dropped. Each now ends with «كانت في فولدر «غير مصنف» ونُقلت
  إلى …» and «سؤال لأبو علي: …».
- The empty «غير مصنف» folder and its sheet moved to the trash. The sheet's last content is in
  `data/unclassified_sheet_before_removal.json`.

**Rosary check** (`qc/ROSARY_CHECK.md`, `qc/rosary_check.json`)
- Nine bead strands were checked: AMB-A-046, 053, 058, 064, 065, 081, 111, 113 and 115.
- Each was checked for bead count, clasp, graduation, شاهد and spacers. Each was also searched across all six
  rosary-catalog galleries, the video-only rosaries and the round-6 boards, at high resolution.
- **None is a confirmed rosary, and none is already in the rosary catalog.**

| Code | Verdict | Why |
|---|---|---|
| 053 | necklace | spring-ring clasp |
| 058 | necklace | strongly graduated, fitting opposite the centre bead |
| 065 | necklace | 31 + centre + 31, graduated |
| 081 | necklace | 25 round beads, 2 raw nuggets, raw centrepiece |
| 113 | necklace | 14 + 14 graduated around a large centre bead |
| 115 | bead strand | 11 large beads on a green cord |
| 046 | probably necklace | barrel clasp piece at the back |
| 064 | unsure | 53+ beads, no clasp seen, but no شاهد or spacers; sizes vary about 1.5× |
| 111 | unsure | one close-up of three beads only |

- Nothing was moved into the rosary catalog.
- The Notes of AMB-A-064 and 111 ask the owner whether they are rosaries. If yes: ROS-KS for 064, ROS for 111 (the
  material may be faturan).

**Verification**
- The three sheets were exported and compared cell by cell with `data/sheet_payload.json`: 0 mismatches.
- The new rows' image formulas and row heights were read back.
- The Drive re-walk found only the three category folders at the top. 553 photos are named CODE-N in their own
  folder, there are 83 duplicates and 14 videos, and every sheet image sits in its own row's folder.

## Round 10: AMB-A-111 deleted and renumbered; amber videos gathered (AMB - VID)
Owner's request:
- 064 is not a rosary;
- 111 is one photo of a rosary that already exists in the rosary catalog, so delete it and fix the numbering;
- in the videos folder, gather every amber video from the 12 phases into one folder, without moving anything from
  the phases;
- every amber video must have a code, and the code in the video sheet must equal the code in the amber sheet;
- a piece with photos and a video is green and holds the video; a video-only piece has a code and a sheet row, and is
  red.

**AMB-A-111 and the renumbering**
- Folder AMB-A-111 (one photo) moved to the trash. Its row was deleted from the AMB-A sheet.
- AMB-A-112 … 120 were renamed to 111 … 119: 9 folders and 37 photos (`videos/renumber_ops.json`).
  - Columns A and D of rows 112–120 were updated.
  - The one Note that cited a moved code (AMB-A-001 → AMB-A-119) was updated.
  - None of these codes appears in the video sheet.
- AMB-A now runs 001–119 with no gaps.
- The 064 Notes now say the owner confirmed it is not a rosary.

**Amber videos in the 12 phases** («_Knooz Videos (Full-edit)»)

| Video | Phase | Code | Folder |
|---|---|---|---|
| A020 | 01 | AMB-A-107 | red (video only) |
| A021 | 01 | AMB-A-015 | green |
| A009 | 04 | AMB-ST-030 | red |
| A012 | 04 | Amb-dec-007 | green |
| A013 | 04 | AMB-A-105 | red |
| A014 | 04 | AMB-A-084 + AMB-A-086 (clock and thermometer set) | both green |
| A015 | 04 | AMB-A-106 | red |
| A016 | 04 | Amb-dec-008 | green |
| A017 | 04 | Amb-dec-049 | green |
| A002 | 06 | AMB-A-103 | red |
| A003 | 06 | AMB-A-050 | green |
| A004 | 06 | AMB-A-104 | red |
| A001 | 07 | AMB-A-102 | red |
| من_تحف_الكهرمان_المنحوتة | 12 | Amb-dec-003 | green |

- Amber Faces (Phase 05) = AMB-A-057. It has a sheet row but no video file, so it has no colour.
- The phase-12 amber rosary videos belong to the rosary catalog (ROS-K-005, ROS-Amb-G-086, …).
- None of the other phase videos is an amber catalog piece:
  - rings, coins, banknotes, swords and daggers, Qurans and pottery;
  - engraved agate/jade stones and necklaces (Phases 08, 09, 11);
  - Phase 11's «AMB1» row is an engraved agate (عقيق), not amber.
- Drafts (ANTIQUE MERMAID, Broush (Rosary)) were not copied, matching how «ROS - VID» was done.

**What changed**
- New folder «AMB - VID» in the videos root, next to «ROS - VID». It holds 14 videos named by code, e.g.
  `AMB-A-107.mp4` and `AMB-A-084 + AMB-A-086.mp4` (`videos/amb_vid_plan.json`).
  - The owner's «ROS - VID» holds real Drive shortcuts. The Drive connector cannot create shortcuts (it refuses the
    shortcut MIME type), so these are server-side copies.
  - Nothing in the phases was moved or renamed.
- AMB-A-086 got `AMB-A-086-video.mp4` (a copy of A014) and turned green. Its Notes say so.
- All 15 video piece folders were recoloured: 8 green (015, 050, 084, 086, dec-003, 007, 008, 049) and 7 red (102–107,
  ST-030).
- **Video sheet:**
  - Phase 04 E10 now reads «AMB-A-084 + AMB-A-086».
  - Phase 12 had no row for the carving video, so row 7 was added: file name, a note, «Amb-dec-003» and «Amber
    Carving».

**Verification**
- The three amber sheets were exported and compared cell by cell with `data/sheet_payload.json`: 0 mismatches.
- Every amber code in the video sheet exists in an amber sheet.
- The Drive re-walk:
  - 552 photos named CODE-N in their own folder, and every sheet image in its own row's folder;
  - 15 piece folders hold `CODE-video.mp4`;
  - 14 files in «AMB - VID».
