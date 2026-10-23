# Round 4: compare the owner's PC folder with Drive

The local folder «ROS- مسابح» (collect- NOV 25) is too large to upload whole. Instead the owner runs one script on the
PC; it uploads nothing by itself and copies only the photos that are NOT on Drive into `_missing_on_drive`.

## Script
- `knooz_compare.ps1`: plain ASCII, works in Windows PowerShell 5.1 and PowerShell 7. No modules, no System.Drawing.
- Holds the Drive photo list as gzip+base64: 2,155 unique keys `YYYY:MM:DD HH:MM:SS|frame`, built from a full crawl of
  the rosaries root (2,186 files, 2,178 photos with EXIF; staging folder excluded) by `tools/crawl_all.py`.
- Match rule: EXIF DateTimeOriginal (tag 0x9003) + camera frame number (XMP `aux:ImageNumber`). Same shot time, and
  same frame (or either side has no frame) → ON_DRIVE. Otherwise MISSING. No EXIF date → NO_EXIF (copied, checked by eye).
- Output: `_missing_on_drive/` (same sub-folder layout as the PC) + `_missing_on_drive/_manifest.csv`
  (path, size, dto, imgno, status for every file in the folder).
- On Drive: `knooz_compare.ps1` in the upload folder (id 1h0MHtl-E8DguRw_gQggSsH4kYlLUghUA), sha256 (LF)
  810fc0c7afda2ecbf1991d46d3b5506118bdbdaaa598bad0c8ac056297aea89e — verified identical after download.

## Run (owner)
Open «ROS- مسابح» in File Explorer → type `powershell` in the address bar → Enter → paste:

    [Net.ServicePointManager]::SecurityProtocol="Tls12"; iex ((New-Object Net.WebClient).DownloadString("https://drive.usercontent.google.com/download?id=1h0MHtl-E8DguRw_gQggSsH4kYlLUghUA&export=download&confirm=t"))

`confirm=t` is required: without it Drive answers .ps1 downloads with a "virus scan warning" HTML page.
Tested end to end from the Drive link (pwsh 7.4.6): Arabic and bracketed folder names, little/big-endian EXIF,
no-EXIF photo, non-photo file, nested folders.

## After the upload
Parse `_manifest.csv` → per-category counts PC vs Drive → re-check each MISSING photo against the Drive list and by
image hash → file into existing pieces (extra views) or new codes → descriptions (short style) → sheet rows
[no., IMAGES, Description, Item Name, Item Category, Price (empty), Notes].
