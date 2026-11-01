# Amber video stills HQ (1 Nov 2026)

Same procedure and rules as the jewelry round (no blur, no video caption, real frames only, quality not below the
camera photos). Size and logo follow the amber camera photos: 3600×3600, logo bottom-left.

## Pieces (7): folders with a video and only 1080 px no-EXIF stills
AMB-A-102 (Soviet monument), 103 (mermaid mirror), 104 (bead necklace), 105 (barometer), 106 (cigarette-holder set),
107 (clock), AMB-ST-030 (stone on board). The other 8 amber folders with videos hold D850 photos.

## Method
`apick.py` (= jewelry `jpick.py` with amber paths): sharpest frame + up to 5 aligned neighbours averaged; square crop
clear of the caption. `aup.py`: Real-ESRGAN x4plus bf16, input ≤ 900 px. `afinish.py`: 3600 px, logo bottom-left,
JPEG ≤ 730 KB. Ten textured images did not fit at 3600: 102-2, 105-3, 105-5, 107-4 at 3300; 103-6, 105-1, 105-4,
107-5 at 3000; 103-4 (SBM leather) at 2400 (`quality.json`).

## Output: 43 images
102 ×6, 103 ×7, 104 ×6, 105 ×5, 106 ×7, 107 ×7, ST-030 ×5.
Dropped during review: 102 hammer-and-sickle plaque (cut/soft), a duplicate 105 front and a soft 105 dial, ST-030 board
shot (caption or cut stone), ST-030 macro (out of focus in the video itself).

## Drive
7 `صور-قديمة-من-الفيلم` subfolders created; the 22 old stills (incl. the 200 px duplicate AMB-A-107-1) renamed
`…-لقطة-فيديو-قديمة.jpg` and moved there (`ahousekeep.json`). Nothing deleted.
Gallery with the upload button: https://claude.ai/artifact/4Qg6NsdaXFcUfcBnP7zCyt
