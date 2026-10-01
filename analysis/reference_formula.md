# Reference formula — playlist "الأسلحة الإسلامية" (PL3_HcrEs0UjyYIie9pxNQanieG9qrfVD_)

Measured 2026-10-01 in the Higgsfield cloud sandbox (tools/ref_metrics.py): yt-dlp 1080p + AAC, ffprobe, ffmpeg scdet/signalstats, librosa, OpenCV.
17 playlist entries; **tFtgbamrsW8 is hidden/unavailable on YouTube**, so 16 films were measured. What needed eyes (opening card, text, logo artwork, grade) is marked "visual, unverified" — frames could not be brought into this session (see report.md, blocker).

## Container
| item | value |
|---|---|
| resolution / fps | 1920×1080, 29.97 (30000/1001), H.264 — the channel is not 4K today |
| length | 49.9–50.8 s, all 16 films (music length 50.25 s; the film is cut to the track) |
| music | one track in all 16 films, same start (onset-envelope cross-correlation 0.82–1.00, lag ≈ 0). 129.2 BPM, beat 0.464 s. Three byte-identical audio pairs; 14 films are mastered at −9.9 LUFS integrated / LRA 8.2 LU, the two newest (VgZXOWyRDak, WHyDL7lN57g) at −14.0 LUFS / LRA 4.4 / peak −1.2 dBFS |
| music shape | hit at 0.12 s; quiet intro 1–4 s (−30 dB RMS) with a hit at 4.09 s; quiet 5–7 s; full groove from 7.6–8.6 s; constant −15 dB RMS to 44 s; fade 45–50 s; two strong final onsets at 46.77 s and 48.58 s |
| cuts per film | 4–10 scene changes (scdet ≥ 8), median 7.5 → 8–9 shots, ASL ≈ 5.5–6 s |
| consensus cut points (s) | 1.6 (6 films), 5.4 (5), 7.6 (4), **14.75 (9)**, 16.7 (6), **20.32 (11)**, **23.9 (10)**, **27.43 (9)**, **29.4 (10)**, **34.87 (10)**, **38.44 (9)**, 42.1 (6), 43.95 (5) |
| end | last ~4 s (46–50 s) are a static graphic: Y-max collapses to ≈172 and Y-avg to 16–17 in every film sampled, fading with the music → end card / logo (visual, unverified artwork) |
| open | the first 0.5 s is not black in any film (no fade from black); 3 of 4 sampled start dark (Y-avg 21–46), WHyDL7lN57g starts bright and flat (Y-avg 86, Y-max 159 = a flat graphic / title card, visual, unverified) |
| black frames | none detected anywhere (no fades to black inside the films) |
| exposure | dark backgrounds (Y-avg 20–60 most of the time) with the metal near clipping (Y-max 230–255) — the classic "piece on black" grade |

## Shot structure (from scene changes; which part of the piece is in each shot could not be seen)
Cuts cluster on the track's accents, not on every beat. The common skeleton:
1. 0–1.6 s opener (often a graphic/flat frame), 2. 1.6–7.6 s two or three short shots over the quiet intro, 3. 7.6–14.75 s one long shot (7 s) when the groove starts, 4. 14.75–20.32 s, 5. 20.32–23.9 s, 6. 23.9–27.43 s, 7. 27.43–29.4 s (a short 2 s insert, 10 films), 8. 29.4–34.87 s, 9. 34.87–38.44 s, 10. 38.44–42.1 s, 11. 42.1–44 s, 12. 44–50 s end card over the fade.

## Light sweep (reference WHyDL7lN57g, bright-pixel ≥225 tracking at 854×480, 29.97 fps)
| pass | frames | time (s) | duration | centroid travel | peak | trigger |
|---|---|---|---|---|---|---|
| A | 832–860 | 27.76–28.70 | 0.94 s | x 404 → 509 (+105 px, left→right), hot area 0.27 % → 0.79 % → 0.30 % | 28.1–28.4 s | onset 28.235 s (strength 10.2), 0.3 s after the cut at 27.43 |
| B | 315–342 | 10.51–11.41 | 0.90 s | x 375 → 452 (+77 px, left→right), constant 0.26 % | — | onset 10.403 s (strength 12.1, the first big hit of the groove) |
| (opening) | 73–108 | 2.4–3.6 | 1.2 s | x 416 → 488, hot area 1.0 → 1.4 → 1.15 % | 3.1 s | after the 1.58 s onset — a highlight moving on the metal in the intro (could be the piece turning; visual, unverified) |
Other bright-centroid drifts (14.75–20.3 s, 34.87–38.4 s) move 2–3 px/frame monotonically for 4–5 s: slow camera moves, not sweeps.
So: a pass takes ≈0.9 s, runs left→right along the piece, sits on a strong onset in the first second of a shot, and happens 2–3 times per film, not on every beat. Width/softness could not be measured without seeing the band (centroid spread σx ≈ 20–60 px suggests a band ~5–10 % of frame width).

## Grade / text / logo
Visual, unverified: no frames were viewable in this session. Measurable facts only: dark background, metal near clipping, static end card for the last ~4 s, no black frames.
