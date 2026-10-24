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
| AMB-ST «أحجار الكهرمان» | AMB-ST-001 … 027 (+028, 029 in «غير مصنف») | 27 + 2 | Amb-S-001 renamed **AMB-ST-001** (same folder) |
| AMB-A «تحف الكهرمان» | AMB-A-001 … 107 (+108 … 116 in «غير مصنف») | 107 + 9 | AMB-A-001 kept; 102–107 are video-only |
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
| AMB-A-110 | closed leather pipe case, one photo | separate item or another pipe's case? |
| AMB-A-111 | very dark bead strand, close-up only | amber or faturan? full photos? |
| AMB-A-112 | pair of cherry-orange mouthpieces | amber or faturan? |
| AMB-A-113 | cherry-red bead necklace | cherry amber or faturan? |
| AMB-A-114 | auction-catalogue clipping (meerschaum and amber pipe, melusine bowl, 1914) | which pipe? |
| AMB-A-115 | large old "trade" beads | amber or copal/resin? |
| AMB-A-116 | desk seal with insects | amber or copal? |
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
| Knooz (Desc._) Sheet - AMB-A | 1mMNM0_EEwvTK8bMLmNG4P3ka3tOmhuW2ixrSO-wmDzg | 107 |
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
