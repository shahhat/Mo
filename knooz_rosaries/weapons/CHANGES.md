# Knooz – Islamic weapons (S) – Drive restructure (2026-11-10)

Root: https://drive.google.com/drive/folders/1ThD_NurW-FZeo72bE17Cf52YjXNV7su5

- 534 photos = 330 unique shots (key = EXIF DateTimeOriginal + aux:ImageNumber) + 204 exact duplicates.
- 74 pieces: S-J (swords) 47, S-KJ (daggers/knives) 22, S-X (other) 5.
- Every unique shot moved into `<category>/<code>/<code>-n.jpg` (file IDs unchanged). Verified by walk: 330/330.
- Old folders «سيوف الجوهر» (161 dups) and «خناجر وسكاكين جوهر» (43 dups) moved into «للحذف». Nothing trashed.
- Sheet «Knooz (Desc._) Sheet - S»: 74 rows; Description filled only for the 15 pieces described in the old sheet «وصف الاسلحة».
- PC: `pc/knooz_compare_weapons.ps1` (find photos not on Drive), `pc/knooz_rename_weapons.ps1` (rename PC photos to the same codes; preview + YES; -Undo).

Old → new: S001 S-KJ-002 · S002 S-KJ-003 · S003 S-J-026 · S004 S-J-027 · S005 S-J-028 · S009 S-KJ-005 · S010 S-KJ-006 · S011 S-KJ-009 · S012 S-KJ-010 · S013 S-KJ-011 · S015 S-J-019 · S016 S-KJ-012 · S017 S-KJ-013 · S018 S-KJ-016 · S024 S-J-025 · S026 S-J-042 · S027 S-KJ-021 · S043 S-KJ-019 · S070 S-J-038 · S073 S-X-003 · S074 S-X-002 · S075 S-X-001 · S076 S-KJ-014

Described in old sheet but no photos found: S006, S007, S008, S019, S021, S066, S071. No photos for S014.
Logs: `logs/` (plan, groups, done_A/B/C, sheet rows).

## Round 2 – raw sessions folder (1LdNIl3uwQaTZOGnzXkX8oeEJ9EsvtKP6)
- 1,128 photos scanned; 299 are weapons (ISLAMIC TRESURES 73/75/76, جلسة 79, 25 nov 25). None existed in the weapons folder (all old photos are 2021–Feb 2025).
- «25 nov 25» (56 photos) = exact copies of ISLAMIC TRESURES 75 → folder moved to «للحذف».
- 243 unique shots → 36 pieces: 35 new (S-J-048..068, S-KJ-023..027, S-X-006..014) + 8 extra photos for S-J-046.
- Each photo copied into its piece folder under the code name; the original in the sessions folder renamed to the same name (not moved).
- Drive now: 109 pieces, 573 photos (verified by walk). Sheet: 109 rows.
- PC scripts updated to 573 shots (multi-target keys for different exports of one frame). Copies on Drive root for download.

## Round 3 – weapon videos
- 21 weapon videos → copies in «S - VID» (1eHYW70hVssgVRFFqS-SjEEjm3NXNC31x); originals renamed in place to the code.
- Copy `CODE-video.mp4` placed in each of the 20 piece folders (S-J-010 has two: v1 + v2). Folders coloured green #16a765 (photos + video); S-KJ-028 red #f83a22 (video only, 3 frames from the video).
- Video sheet «_Knooz Video Products» column B now holds codes for the weapon rows. Weapons sheet Notes list each video.
