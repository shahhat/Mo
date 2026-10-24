# Amber: compare the owner's PC folder with Drive

PC folder: `C:\Users\al-sh\Desktop\جايرو ميديا\الكنوز الإسلامية (عميل)\جلسات تصوير\collect- NOV 25\الكهرمان -AMB`.

## Script
- `knooz_compare_amb.ps1` is the rosary round-4 script with the amber key list (sha256
  060b83a83cc2112153e358faf0c795a78d666bfad2b216b46d630e5992cd3775).
- It embeds 524 unique Drive keys `YYYY:MM:DD HH:MM:SS|frame` (`drive_keys.txt`), taken from the EXIF of all 611 amber
  photos. The 6 video stills have no EXIF and are not included.
- Match rule:
  - same EXIF DateTimeOriginal (0x9003) and the same camera frame number (XMP `aux:ImageNumber`), or no frame number
    on either side → ON_DRIVE;
  - otherwise MISSING;
  - no date → NO_EXIF.
- MISSING and NO_EXIF files are copied into `_missing_on_drive/` with the same sub-folder layout, plus `_manifest.csv`.
- Tested with pwsh 7.4.6 on a folder covering these cases, all classified correctly:
  - Arabic and bracketed folder names;
  - Drive photos with and without a frame number;
  - the same shot with a changed frame number;
  - a changed shot date;
  - a no-EXIF image;
  - non-photo files.

## Delivery
- Upload folder: «_من الجهاز - الكهرمان -AMB (للمقارنة)», id 1pq7X2G9DQUh8jV5p21i4xJSAb5iA-XLF, in the amber root.
- The script was first uploaded there for the one-line download used in round 4. Drive blocked downloading it: 404 for
  the public link and "caller does not have permission" through the API, so it was probably flagged by the scanner.
- That file could not be trashed (internal error), so it was renamed «_ملغي - استخدم النسخة المرسلة في الشات.txt».
- The script was sent to the owner directly in the chat instead.

## Run (owner)
1. Save `knooz_compare_amb.ps1` inside «الكهرمان -AMB».
2. Open that folder in File Explorer, click the address bar, type
   `powershell -ExecutionPolicy Bypass -File .\knooz_compare_amb.ps1` and press Enter.
3. When it prints «Done», upload the folder `_missing_on_drive` into the upload folder above.
