# HANDOVER – Knooz Islamic weapons (S): finish the PC side locally

> **For the owner (عربي):** افتح Claude Code على جهازك (local)، واعمل clone للـ repo على الـ branch ده، وابعتله البرومبت اللي في آخر الملف. الدرايف والشيت خلصوا واتراجعوا. الجلسة المحلية هتطابق فولدر الجهاز مع الدرايف: هتغيّر الأسامي للأكواد، وتنزّل الناقص، وترفع الزيادة.

Repo: `shahhat/Mo`, branch `claude/gallant-feynman-hj18ei`, folder `knooz_rosaries/weapons/`.

## 1. Goal (owner's words, summarised)
Every weapons photo must carry **the same code in all three places**:
1. Google Drive weapons folder: `1ThD_NurW-FZeo72bE17Cf52YjXNV7su5`
2. Sheet «Knooz (Desc._) Sheet - S»: `1PaAKozfsazVtAzAP2h8cRtn6PbBeiceXgYwF-M1cEMQ`
3. PC folder `C:\Users\al-sh\Desktop\جايرو ميديا\الكنوز الإسلامية (عميل)\جلسات تصوير\collect- NOV 25\S - الأسلحة الإسلامية`

The PC folder must hold exactly what Drive holds: nothing more, nothing less, with the same codes. Duplicates go to a `للحذف` folder. **Never delete anything.**

## 2. Current state (verified 2026-11-10)
| Item | State |
|---|---|
| Drive weapons folder | **110 pieces / 576 photos**. S-J 001–068 (swords), S-KJ 001–028 (daggers/knives), S-X 001–014 (other). Every file is named `<code>-<n>.jpg` inside `<category>/<code>/`. Verified by walk + EXIF. |
| Category folders | `S-J - سيوف جوهر` (1vsCi6cf2yy8981gDaik7MqEoUpU7A_Sn), `S-KJ - خناجر وسكاكين جوهر` (1Vk-r6ZV8lrfT7AytIW4BRmK2r9OwarKr), `S-X - أسلحة أخرى` (18N8W46Yt8Z5oPV7UrQtmQT5fZzH6Ybio) |
| `للحذف` on Drive | 1zyM__oVHaaCbNdbzfBDto4-n84C7fMDm. Holds the old folders (204 exact duplicates), «25 nov 25» (56 duplicates of ISLAMIC TRESURES 75) and 8 temporary shortcuts. |
| Raw sessions folder | 1LdNIl3uwQaTZOGnzXkX8oeEJ9EsvtKP6. Its 243 weapons originals were **renamed in place** to the same code names; copies are in the weapons folder. Non-weapon photos were left untouched. |
| Sheet | 109 rows. Each row's IMAGE() points to a photo inside that code's folder. The Notes photo count matches each folder. Description is filled only for the 15 pieces that have an old description; the rest are empty **on purpose** (owner's instruction). |
| PC folder | **NOT checked yet**. The cloud session had no access to it. This is the remaining task. |

## 3. Source of truth for the PC side
`pc/drive_map_full.txt` has 573 lines in the form:
```
DateTimeOriginal|aux:ImageNumber|<category folder>|<code>|<file name>|<Drive file id>
```
It was built from the EXIF actually read from the Drive files, not from the plan.

- **Match key:** `DateTimeOriginal` + XMP `aux:ImageNumber`. 40 Drive files have no ImageNumber; fall back to DateTimeOriginal alone.
- **4 keys map to 2 different files each:** S-J-063-7/8, S-J-067-7/8, S-KJ-023-5/6, S-X-010-7/8. These are different crops of one frame, so assign targets in order. If pixel content is ambiguous, compare visually.
- **Download:** every Drive file is public at `https://drive.usercontent.google.com/download?id=<id>&export=download&confirm=t`.

## 4. What to do locally
Ready-made scripts are in `pc/` (also on the Drive weapons root). A local Claude can either run them or do the same steps directly in Python/PowerShell.

1. **Back up the PC folder first** (copy it next to itself). The scripts were never run on Windows.
2. `knooz_rename_weapons.ps1`
   - Preview writes `_rename_plan.csv`; the owner then types YES.
   - It moves each PC photo whose key is in the map to `<category>\<code>\<name>`.
   - Extra copies of the same key go to `_للحذف\`.
   - Unknown photos stay where they are.
   - `-Undo` reverts using `_rename_log.csv`.
3. `knooz_verify_weapons.ps1`
   - Read-only report `_verify_report.csv` with statuses OK / WRONG_NAME / EXTRA_COPY / NOT_ON_DRIVE / MISSING_ON_PC.
   - On YES it downloads MISSING_ON_PC files from Drive into the right place, and copies NOT_ON_DRIVE files to `_missing_on_drive\`.
   - Target end state: it prints `PERFECT`.
4. **If NOT_ON_DRIVE photos exist (the PC has more than Drive):**
   1. Look at them.
   2. If a photo is a weapon, assign it to an existing piece (next index) or a new code: next free codes are S-J-069, S-KJ-029, S-X-015.
   3. Upload it into the piece folder on Drive (Google Drive MCP `create_file` with a file reference, or the owner drags it in).
   4. Rename it on the PC to match.
   5. Add or update the sheet row: columns no. / IMAGES `=IMAGE("https://drive.google.com/thumbnail?id=<id>&sz=w800")` / Description (leave empty) / Item Name / Item Category (Sword | Dagger / Knife | Other) / Price / Notes.
   6. Keep rows sorted S-J, then S-KJ, then S-X.
5. **Expected MISSING_ON_PC:** about 330. The 2021–Feb 2025 photos (S-J-001…047, S-KJ-001…022, S-X-001…005) are probably not in the NOV 25 PC folder. Downloading them (about 1.5 GB) makes the PC equal to Drive. Ask the owner before downloading if bandwidth matters.
6. **Re-run verify until it prints `PERFECT`.** Then report back to the owner in Egyptian Arabic, with tables.

## 5. Open review points for the owner (do not change without approval)
- **S-J-053 vs S-J-060:** possibly one sword. They were kept separate because the lockets differ and S-J-053 has no blade cartouche.
- **No full overview shot:** S-J-058, S-J-061 and S-J-062 have only detail shots, so their sheet cover is a close-up.
- **S-X-006:** the plain iron disc (inside view) is assigned to the koftgari shield, with medium confidence.
- **Medium-confidence groupings from round 1:** S-KJ-001, S-KJ-015, S-KJ-017, S-KJ-018.
- **S-J-019 (old S015):** short sword; confirm sword vs dagger.
- **Pieces with an old description but no photos anywhere:** S006, S007, S008, S019, S021, S066, S071. S014 has no photos at all.
- **Old shortcut folder** 1IvG6udjJpphtdKbvAMOkt7mhQo_l_jiG (S001–S076 shortcuts) still exists. Its shortcuts still resolve to the renamed files.

## 6. Rules
- Never trash or delete. Move to `للحذف` instead.
- Keep codes identical everywhere.
- Commit work to the branch above, with these trailers:
  - `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
  - `Claude-Session: https://claude.ai/code/session_01UzZ4MzziJ1j6YT7Txi8oVf`
- Logs: `CHANGES.md`, `logs/` (round 1), `logs/nov25/` (round 2: plan2.json, groups, done2_*.json).

## 7. Prompt to paste in the local session
```
Read knooz_rosaries/weapons/HANDOVER.md in this repo (branch claude/gallant-feynman-hj18ei) and finish section 4:
make my PC folder "C:\Users\al-sh\Desktop\جايرو ميديا\الكنوز الإسلامية (عميل)\جلسات تصوير\collect- NOV 25\S - الأسلحة الإسلامية"
identical to the Drive weapons folder (same photos, same codes), using pc/drive_map_full.txt as the source of truth.
Back up first, show me the preview numbers before changing anything, never delete, duplicates to للحذف.
Reply in Egyptian Arabic with tables.
```

## 8. Update – weapon videos (2026-11-10)
- 21 weapon videos from «_Knooz Videos (Full-edit)» copied to the new folder **«S - VID»** (1eHYW70hVssgVRFFqS-SjEEjm3NXNC31x). The originals were renamed in place to the same code (see `logs/videos/vplan.json`).
- **New piece S-KJ-028** (Moroccan silver dagger) exists only as a video. Its folder 11l4JhPYRaVQHM6sdYAwNtVY2Oxjjyag9 holds 3 frames extracted from the 4K video. Those frames have no EXIF, so the PC check matches them by path. `drive_map_full.txt` now has 576 lines.
- **Use the repo copy of `pc/knooz_verify_weapons.ps1`.** The copy on the Drive root is the older 573-photo version.
- The video sheet «_Knooz Video Products» now uses weapon codes in column B (rows 30–37, 67–69, 83–87).
