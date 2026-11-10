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
