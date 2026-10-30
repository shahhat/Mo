# Video sheet «Knooz (Desc._) Sheet»: every phase tab in the Phase 11 layout (30 Oct)

Owner's request (with a screenshot of Phase 11): «خلى كل الشيتات نفس الطريقة دى تسلسل و صورة و كود و وصف فقط خلى كل
الفيزر زى الفيز ده». Sheet 1hO-BJKp1qb1Usf2MjUXmEgG0zwVVCMRfRxLjeZxQQ5U.

Model = Phase 11 (left untouched): **no. | IMAGES | Description | Item code | Item Category | Notes**, red header
(92 px), cream «no.» column with large red numbers, widths 97/407/376/302/302/302, header row frozen.

Applied to the other 11 tabs (Phase 01–10, 12):
- Header row and data-row formats copied from Phase 11; same widths; data rows 300 px; header frozen.
- Images (column B) untouched: in-cell images in Phases 01–09, IMAGE() formulas in 10 and 12. Phase 12 row 7
  (Amb-dec-003) had no image; it now shows the amber sheet's image of that piece.
- no. = 1…n. Empty rows inside the tables removed: Phase 05 rows 14–15, Phase 07 row 14 (no text, no image).
- Item code = the old «Item Name» (the catalog code) where there was one; otherwise the old «Video File Name»
  (the only identifier those rows had, e.g. S028, CU004, C012).
- Item Category = the old «Item Type/Category» where filled; else the catalog's category (JWL / amber sheets,
  ROS → Rosary); else from the description (سيف → Sword, خنجر → Dagger, روبية ورقية/CU → Banknotes, دينار/درهم → Coin,
  فخار → Pottery, مخطوط → Manuscript, منمنمة → Artboard). Left empty: Phase 03 P015 and Phase 05 P014 (no text).
- Notes = the old Notes. The old «Video File Name» column was removed; where it differed from the code and no video
  file carries the code, it is kept in Notes as «اسم الفيديو القديم في الشيت: …». Phase 01 had a second unlabeled text
  column (two rings); it moved to Notes. Phase 01's description sat in an unlabeled column D; it is now in C.
- Before/after exports: `before/*.csv`, `after/*.csv`; mapping: `plan.json`, `values.json`.

Verification: all 12 tabs exported; the 11 changed tabs match the plan cell for cell (0 mismatches), headers equal
Phase 11's, nothing below the last row or beyond column F; Phase 11 byte-identical to before; images confirmed in
column B on the moved rows.

# Round 16 (30 Oct): codes for rosary and jewelry videos everywhere
- Phase 11 renumbered 1–10.
- JWL: the 42 jewelry videos in the phases renamed to their codes (`round16/jwl_phase_ops.json`); in «JWL - VID»
  JWL-H-040.mp4 → JWL-H-002.mp4 (another editor renumbered H-040 to H-002 in the JWL-H sheet on 30 Oct). Video sheet:
  every JWL row's description = the live JWL catalog sheet; «JWL-H-040 (RING-1)» → «JWL-H-002 (RING-1)»; old-name notes
  dropped where the phase file now carries the code (`round16/vs_log_jwl.json`). Products sheet: 24 JWL rows → code +
  catalog description (`round16/prod_log_jwl.json`). Re-export: 64 JWL cells checked, 0 mismatches.
- ROS: 17 rosary videos in the phases renamed to codes; «ROS - VID»: 8 shortcuts renamed, 5 missing videos copied
  (ROS-KS-082, ROS-KS-151, ROS-K-005, ROS-KS-002, ROS-Amb-G-086). Products rows 39–44 identified by screenshot vs catalog
  photos (39 = ROS-Amb-G-053, 41 = ROS-KS-106, 42 = ROS-KS-019, 44 = ROS-Amb-G-037).
- ROS descriptions: the text written on each of Abu Ali's rosary videos was read frame by frame (`round16/ros_captions.json`)
  and, spelling-fixed only (ة, hamza, final «.»), became the one description for that piece (`round16/ros_canon.json`).
  Written to: the rosary catalog sheets C (18 rows: ROS-KS ×5, ROS-Amb-G ×9, ROS-K-005, ROS-B-004, ROS-021, ROS-057),
  with the old description kept in G Notes as «الوصف السابق: «…»» (`round16/ros_cat_log.json`); the video sheet C (17
  rows), with Phase 09 rows 2–7 old-name notes cleared and Phase 10 F2 → «الفيديو بدون نص؛ الوصف هو وصف الكتالوج»
  (`round16/vs_log_ros.json`); the products sheet rows 19, 20, 39–44 → B code + E description
  (`round16/prod_log_ros.json`). ROS-Amb-G-084's video has no text, so it keeps its catalog description everywhere.
- Re-export of all 6 rosary catalogs, all 12 video-sheet tabs and the products sheet: 25 rosary cells checked against the
  catalog, 0 mismatches; 18/18 catalog notes carry the old description.
- Open: ROS-Amb-G-081 has a video, folder and sheet-video row but no row in the ROS-Amb-G sheet; 4 Phase 09 videos still
  uncoded (Brown to-yellow, Green, Maroon Sprkl-Crcls, Orange to-glow-Yellow); products sheet has no row for Amb-dec-003.
