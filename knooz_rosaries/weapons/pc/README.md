# Weapons (S): compare the owner's PC folder with Drive

PC folder: `C:\Users\al-sh\Desktop\جايرو ميديا\الكنوز الإسلامية (عميل)\جلسات تصوير\collect- NOV 25\S - الأسلحة الإسلامية`.

`knooz_compare_weapons.ps1` = the tested JWL/amber script with the weapons key list: 330 unique Drive keys
`DateTimeOriginal|ImageNumber` (`drive_keys.txt`) from the 534 photos in the weapons root (1ThD_NurW-FZeo72bE17Cf52YjXNV7su5).
Same match rule; MISSING / NO_EXIF photos are copied to `_missing_on_drive/` with `_manifest.csv`.

## Run (owner)
1. Save `knooz_compare_weapons.ps1` inside «S - الأسلحة الإسلامية».
2. In File Explorer open that folder, click the address bar, replace its text with
   `powershell -NoExit -ExecutionPolicy Bypass -File .\knooz_compare_weapons.ps1` and press Enter.
3. When it prints «Done.», upload the folder `_missing_on_drive` into «_من الجهاز - S (للمقارنة)»
   (1V8pkBb03npV4ClLiT9ladeGhYF5VUCRP) inside the weapons folder.
