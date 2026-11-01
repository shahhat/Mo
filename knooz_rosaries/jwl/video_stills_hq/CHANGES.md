# Jewelry video stills HQ (1 Nov 2026)

Request: same procedure as the rosaries for the jewelry/rings whose only images were video frames. Rings: 3 shots only
(front with the inscription clearly readable, side showing the metal, inner hallmark if the video has it). Rules: no
blur, inscription very clear, quality not below the owner's three examples (2000×2000, logo bottom-left).

## Pieces (14): every folder with a video and only 1080 px no-EXIF stills
Rings (8): JWL-B-032, B-033, HS-096, HS-097, RS-094, RS-095, RS-096, RS-097.
Other (6): JWL-W-041, W-042, W-043, W-046, W-048, W-049.
(W-045 and H-002 now also hold D850 photos and were left alone; H-002 still has its three 1080 px stills as -1..-3.)

## Method
- `jpick.py`: per shot, sharpest frame in the chosen window, then up to 5 neighbouring frames aligned (ECC affine,
  correlation ≥ 0.97) and averaged to lower compression noise; square crop kept clear of the burned-in caption.
- `jup.py`: Real-ESRGAN x4plus (bf16), input capped at 700 px. Pilot on B-033 and RS-097 compared raw / fused+Lanczos /
  fused+ESRGAN on the inscription: ESRGAN kept every stroke and dot of the raw frame and was clearest.
- `jfinish.py`: 2000×2000, light unsharp, logo bottom-left (12 % height), JPEG ≤ 730 KB (inline Drive upload limit),
  EXIF says enhanced video still.
- Output 48 images: rings 2 each (‑1 front/inscription, ‑2 side/metal); W-041 4, W-042 5, W-043 5, W-046 6, W-048 5,
  W-049 7. `ringfront_qc.jpg` = inscription zoom of all 8 ring fronts.

## Hallmark (shot 3)
Not available for any ring: the inside of the band appears only at a distance (B-033, HS-097 tested), the stamps are a
few blurred pixels. Not produced rather than shipping an unreadable image.

## Drive
- 14 `صور-قديمة-من-الفيلم` subfolders created; the 42 old stills renamed `…-لقطة-فيديو-قديمة.jpg` and moved there
  (`jhousekeep.json`). Nothing deleted; IDs unchanged.
- New images delivered through the gallery artifact https://claude.ai/artifact/FURaf8FAvFLLfUqv9xZYJ2 (owner uploads
  with one button; names CODE-1.jpg …).

## Dropped
- W-041 shot 5: every late frame has the caption across the pendant; the clean crop cut the pendant off.
