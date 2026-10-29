# Jewelry (JWL): compare the owner's PC folder with Drive

PC folder: `C:\Users\al-sh\Desktop\جايرو ميديا\الكنوز الإسلامية (عميل)\جلسات تصوير\collect- NOV 25\JWL - خواتم ومجوهرات`.

- `knooz_compare_jwl.ps1` (sha256 6654b8c47c34fe20a3310e0dba6a48ca7385ac77946e86ae463c1d6cf01bc153) is the amber script
  with the JWL key list: 952 unique Drive keys `YYYY:MM:DD HH:MM:SS|frame` (`drive_keys.txt`) from the EXIF of all 1384
  JWL photos. Same match rule as amber (`../../amber/pc/README.md`).
- MISSING and NO_EXIF files are copied into `_missing_on_drive/` with the same sub-folder layout, plus `_manifest.csv`.

## Run (owner)
1. Save `knooz_compare_jwl.ps1` inside «JWL - خواتم ومجوهرات» (next to the six category folders).
2. Open that folder in File Explorer, click the address bar, replace its text with
   `powershell -NoExit -ExecutionPolicy Bypass -File .\knooz_compare_jwl.ps1` and press Enter
   (`-NoExit` keeps the window open so the counts can be read).
3. When it prints «Done.», upload the folder `_missing_on_drive` into the JWL upload folder
   «_من الجهاز - JWL (للمقارنة)» (12z5FGqgqOQYOBNn_rIL3BwRGGbVy9OBM).

On 29 Oct the owner typed only the file name into the address bar, which does not run it; the full command above does.
