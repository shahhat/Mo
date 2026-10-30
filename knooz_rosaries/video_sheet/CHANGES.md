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
