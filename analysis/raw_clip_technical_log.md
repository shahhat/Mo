# Raw clip technical log — "خنجر 2" (19 files, Drive folder 1g6bp21G6t8dMu4D3VhRjgV5wEqMJ39k6)

Measured 2026-10-01 with ffprobe + OpenCV in the Higgsfield cloud sandbox (tools/raw_metrics.py).
Sampling: 4 samples/s, frames scaled to 1920 wide, grey.
Metrics: `lap_top` = mean Laplacian variance of the 10 sharpest tiles of an 8×8 grid (proxy for the dagger region, the only detailed object in frame);
`motion` = mean abs frame difference at 240 px wide between consecutive samples (0.25 s apart); `lum` = mean luma 0–255;
`clip%` = share of pixels ≥250; `crush%` = share of pixels ≤8.

## All 19 files present and readable. None is 4K.

| # | file | size MB | codec / profile | res | fps | pix / range / trc | dur s | bitrate Mbps | audio | creation (UTC) | pts Δ min ms |
|---|------|---------|-----------------|-----|-----|-------------------|-------|--------------|-------|----------------|--------------|
| 0 | 1.mp4 | 493 | h264 Main, "AVC Coding" | 1920×1080 | 29.97 | yuv420p, untagged (treat bt709) | 129.6 | 30.4 | aac | 2026-09-28 20:21 | 12.2 (one short gap) |
| 1 | 2.MOV | 340 | h264 High | 1920×1080 | 29.97 | yuvj420p full range, trc bt470m, bt709 prim | 88.2 | 30.8 | none | 2026-09-19 03:42 | 33.4 (CFR) |
| 2 | 3.MOV | 203 | h264 High | 1920×1080 | 29.97 | yuvj420p full range, trc bt470m | 52.1 | 31.2 | none | 2026-09-19 04:13 | 33.4 (CFR) |
| 3 | 4.MOV | 279 | h264 High | 1920×1080 | 29.97 | yuvj420p full range, trc bt470m | 71.9 | 31.0 | none | 2026-09-19 04:12 | 33.4 (CFR) |
| 4 | 5.mp4 | 120 | h264 Main, "AVC Coding" | 1920×1080 | 29.97 | yuv420p untagged | 31.5 | 30.5 | aac | 2026-09-29 18:55 | 25.4 |
| 5 | 6.mp4 | 128 | h264 Main | 1920×1080 | 29.97 | yuv420p untagged | 33.2 | 30.9 | aac | 2026-09-29 20:15 | 2.5 (dropped/dup frame) |
| 6 | 7.mp4 | 107 | h264 Main | 1920×1080 | 29.97 | yuv420p untagged | 28.4 | 30.1 | aac | 2026-09-29 18:58 | 31.6 |
| 7 | 8.mp4 | 19 | h264 Main | 1920×1080 | 29.97 | yuv420p untagged | 5.3 | 29.4 | aac | 2026-09-30 07:34 | 19.7 |
| 8 | 9.mp4 | 201 | h264 Main | 1920×1080 | 29.97 | yuv420p untagged | 57.2 | 28.2 | aac | 2026-09-29 20:11 | 27.4 |
| 9 | 10.mp4 | 230 | h264 Main | 1920×1080 | 29.97 | yuv420p untagged | 63.8 | 28.8 | aac | 2026-09-29 20:13 | 20.7 |
| 10 | g (5).mp4 | 12 | h264 Main | 1920×1080 | 29.97 | yuv420p untagged | 3.8 | 26.2 | aac | 2026-09-29 19:23 | 31.7 |
| 11 | g (6).mp4 | 23 | h264 Main | 1920×1080 | 29.97 | yuv420p untagged | 5.9 | 31.2 | aac | 2026-09-29 20:47 | 17.8 |
| 12 | g (7).mp4 | 41 | h264 Main | 1920×1080 | 29.97 | yuv420p untagged | 10.8 | 30.3 | aac | 2026-09-30 13:18 | 33.4 |
| 13 | g (8).mp4 | 10 | h264 Main | 1920×1080 | 29.97 | yuv420p untagged | 2.8 | 29.0 | aac | 2026-09-30 13:19 | 28.8 |
| 14 | g (9) - Trim.mp4 | 20 | h264 Main | 1920×1080 | 30.00 | yuv420p untagged | 5.3 | 29.8 | aac | 2026-09-30 13:37 | 10.6 |
| 15 | g (10).mp4 | 29 | h264 Main | 1920×1080 | 29.97 | yuv420p untagged | 7.6 | 30.4 | aac | 2026-09-29 20:51 | 33.4 |
| 16 | g (15).mp4 | 15 | h264 Main | 1920×1080 | 29.97 | yuv420p untagged | 4.0 | 30.2 | aac | 2026-09-29 20:57 | 19.7 |
| 17 | g (16).mp4 | 27 | h264 Main | 1920×1080 | 29.97 | yuv420p untagged | 7.0 | 30.6 | aac | 2026-09-29 20:55 | 2.3 (dropped/dup frame) |
| 18 | g (17).mp4 | 158 | h264 Main | 1920×1080 | 29.97 | yuv420p untagged | 42.8 | 29.6 | aac | 2026-09-29 20:27 | 22.8 |

Total duration 651 s (10 min 51 s). Three shooting sessions by creation time: 19 Sep (2.MOV, 3.MOV, 4.MOV, phone, no audio, full-range yuvj420p), 28–29 Sep (1.mp4, 5–7, 9, 10, g(5)(6)(10)(15)(16)(17)) and 30 Sep (8.mp4, g(7)(8)(9)). The "g (9) - Trim" file was trimmed in Windows (30.00 fps re-mux, 10.6 ms pts gap at the trim point).
Rotation flags: none. HDR: none (no HLG/PQ, no bt2020). The MOVs need full-range → limited-range handling and a gamma 2.2 → bt709 interpretation when matched to the mp4s.

## Per-clip sharpness / motion summary (lap_top p50 / p90 / max; motion p50 / p90; mean lum; max clip %; median crush %)

| # | file | lap p50 | p90 | max | mot p50 | p90 | lum | clip% | crush% | reading |
|---|------|---------|-----|-----|---------|-----|-----|-------|--------|---------|
| 0 | 1.mp4 | 312 | 378 | 424 | 1.1 | 1.4 | 16.5 | 0.27 | 40 | very dark, near-static, consistently sharp (slow slider/turntable-type move) |
| 1 | 2.MOV | 390 | 679 | 762 | 4.2 | 6.1 | 68 | 0.55 | 40 | handheld, sharpness ramps 0→600→0 (focus/drift passes), two sharp windows 25–40 s and 48–65 s |
| 2 | 3.MOV | 96 | 188 | 197 | 2.5 | 3.3 | 73 | 0.41 | 52 | soft overall, best 30–43 s |
| 3 | 4.MOV | 79 | 280 | 314 | 2.7 | 3.4 | 69 | 0.02 | 54 | soft except 32–47 s |
| 4 | 5.mp4 | 24 | 33 | 36 | 5.8 | 6.7 | 90 | 0.52 | 29 | soft throughout (wide/defocused or heavy motion blur) |
| 5 | 6.mp4 | 51 | 158 | 189 | 6.1 | 13 | 80 | 0.0 | 47 | soft; sharpens only 26–33 s with fast motion |
| 6 | 7.mp4 | 729 | 1252 | 1314 | 4.9 | 5.5 | 117 | 1.49 | 23 | sharpest clip of the set, bright, slow move, peak 13–22 s; some highlight clipping 15–22 s |
| 7 | 8.mp4 | 40 | 180 | 196 | 23 | 27 | 67 | 0.0 | 28 | fast whip/handheld, only first 1.5 s sharp |
| 8 | 9.mp4 | 683 | 873 | 889 | 7.2 | 8.9 | 56 | 0.03 | 38 | very sharp 15–50 s, continuous medium motion, darker |
| 9 | 10.mp4 | 909 | 990 | 1017 | 8.6 | 9.5 | 64 | 0.02 | 36 | very sharp end-to-end, continuous motion (orbit/slide) |
| 10 | g (5).mp4 | 259 | 274 | 276 | 3.3 | 4.4 | 98 | 0.0 | 29 | short, sharp, steady |
| 11 | g (6).mp4 | 15 | 28 | 60 | 5.0 | 22 | 34 | 0.0 | 71 | dark and soft, fast move at end |
| 12 | g (7).mp4 | 41 | 75 | 80 | 2.3 | 3.7 | 21 | 0.0 | 63 | dark, soft (fade-in from black) |
| 13 | g (8).mp4 | 72 | 81 | 83 | 3.9 | 4.1 | 36 | 0.0 | 58 | dark, moderately soft |
| 14 | g (9) - Trim.mp4 | 47 | 56 | 57 | 2.5 | 3.7 | 28 | 0.0 | 53 | dark, soft, fade-in |
| 15 | g (10).mp4 | 70 | 81 | 84 | 2.6 | 3.7 | 30 | 0.0 | 57 | dark, soft, fade-in |
| 16 | g (15).mp4 | 227 | 286 | 310 | 5.5 | 7.3 | 67 | 0.01 | 33 | short, sharp, brightening |
| 17 | g (16).mp4 | 67 | 307 | 330 | 4.1 | 5.3 | 33 | 0.0 | 40 | fade-in from black, sharp from 5 s |
| 18 | g (17).mp4 | 149 | 171 | 204 | 4.9 | 17 | 52 | 0.0 | 43 | 10 s fade-in from black, moderate sharpness, fast move after 33 s |

The "g (…)" files with fades from black and 26–31 Mbps "AVC Coding" encodes look like exports from a previous edit rather than camera originals; they are the same 1080p source generation. Confirm with frames when footage is local.
