# Video stills HQ (31 Oct – 1 Nov 2026)

Request: re-produce the photos of the rosaries whose only images were frames from their video, at the standard of
ROS-Amb-G-013 (Nikon D850, black background, square 3000–4400 px, Islamic Treasures logo), at least 5 angles each.

## Which pieces
The Drive connector does not return folder colours, so the blue folders could not be read directly. The 9 pieces were
identified as the folders that hold `صور-قديمة-من-الفيلم` + CODE-1..3.jpg frames + CODE-video.mp4 and no camera photos:
ROS-Amb-G-080, 081, 082, 083, 085, 098, 099, 100 and ROS-KS-151. (ROS-Amb-G-084/086 and ROS-KS-019/082/106 have camera
photos and were left alone.)

## Method (no generative AI; every image is a real frame of Abu Ali's video)
1. `pick.py`: each video sampled at 2 fps; 7–8 distinct moments chosen by eye per piece (`sel.json`); each choice matched
   back to the full-rate video, and the sharpest frame within ±6 frames taken. Square crop: `obj` = auto-crop of the whole
   piece; `full` = 1080 px square; `top` = 770 px square above the burned-in caption band. `frames_log.json` = frame
   number, time and crop box per output.
2. `up.py`: Real-ESRGAN x4plus (bf16 on CPU), input capped at 900 px.
3. `finish.py`: 3600×3600, light unsharp mask, logo from ROS-Amb-G-013-2 at 11.8 % width top-right (as in the
   reference), JPEG q92. EXIF ImageDescription says it is an enhanced video still, not a camera photo.
4. Output: 65 images (7 per piece; 8 for 085 and 099), 0.9–1.6 MB each. Board: `final_board.jpg`.

## Delivery
- The Drive connector cannot upload multi-MB files from this session, so the images are on a private gallery artifact
  (https://claude.ai/artifact/WrmpuJWegHA3nDA7qhDcFS) with a per-piece «ارفع الصور على فولدر القطعة» button (viewer's
  own Google Drive connector, `create_file` into the piece folder as CODE-1.jpg …) and a ZIP download fallback.
- To free the names, the 33 earlier frame files (CODE-1..3.jpg and CODE-still.jpg) were renamed
  `…-لقطة-فيديو-قديمة.jpg` and moved into each folder's `صور-قديمة-من-الفيلم` subfolder (`housekeep.json`). Nothing was
  deleted; file IDs unchanged, so any sheet image pointing at them still works.

## Limits
- Source is 1920×1080 H.264. Upscaling cleans and sharpens but cannot add detail the video does not hold; frames that
  were out of focus in the film (ROS-KS-151, parts of 099/100) stay soft. A D850 shoot is still needed for the catalog.
- Higgsfield (offered by the owner for generative re-shoots) was disconnected in this session.

## 1 Nov: upload fix
- The page's first upload route (`$file` staging) accepts only pptx/docx/xlsx, so JPEGs were refused
  ("$file.type must be one of …"). The page now sends each image inline as base64, which has a 1 MiB request limit.
- All 65 finals were re-encoded to ≤ 730 KB: highest JPEG quality that fits, 4:4:4 first then 4:2:0
  (`quality.json`). 61 stay at 3600 px (q80–92); ROS-Amb-G-082-2 and 098-1 at 3600 q76/q72; 081-2 at 3300 px;
  081-3 (dense silver detail) at 2400 px q72.

## 1 Nov: upload verified
Owner uploaded from the gallery. Each of the 9 folders re-listed and every image downloaded back: 65/65 files present
as CODE-1 … CODE-7/8.jpg, byte-identical (sha256) to the local finals, no duplicates, no missing or extra images.
Old frames remain in each folder's `صور-قديمة-من-الفيلم` (7 files for 080/081/082/083/085/151, 6 for 098/099/100).
