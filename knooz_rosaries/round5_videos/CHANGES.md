# Round 5: rosary videos linked to the catalog

Sources
- Video folder (shared by the owner): 16bNdRwJzBKCGYDw7rBo527gnEfqE_kma. 162 files; 24 rosary-related videos (v00–v23).
- Video sheet «Knooz (Desc._) Sheet»: 1hO-BJKp1qb1Usf2MjUXmEgG0zwVVCMRfRxLjeZxQQ5U. It holds the videographer's image and
  description for each video.
- Matching: 12 frames per video were compared against every catalog piece's photos (3 matching passes, spot-checked).
  Data in `data/match_*.json` and `data/video_plan.json`.

Rule from the owner: do not move the videos. Every video was **copied** into the piece folder as `CODE-video.mp4`.
The originals stay where they were.

## Green folders: catalog piece that already had photos and now has a video (12)
| Piece | Video (copy) | Video-sheet row | Owner's text in the video sheet |
|---|---|---|---|
| ROS-Amb-G-062 | ROS-Amb-G-062-video.mp4 | Phase 02 A019 | مسباح كهرمان الماني منمش شديد الندره – بوزن ٢٠٠ غرام |
| ROS-Amb-G-053 | ROS-Amb-G-053-video.mp4 | Phase 04 A011 | مسباح كهرمان الماني نادر جدا |
| ROS-Amb-G-038 | owner's shortcut already in the folder | Phase 02 A018 | مسباح كهرمان الماني شجري |
| ROS-Amb-G-037 | owner's shortcut already in the folder | Phase 04 A006 | مسباح كهرمان الماني شجري نادر جدا |
| ROS-KS-082 | ROS-KS-082-video.mp4 | Phase 04 A008 | مسباح كهرمان بولندي نادر من الزمن الجميل |
| ROS-KS-019 | ROS-KS-019-video.mp4 | Phase 04 A010 | مسباح كهرمان بولندي رائع |
| ROS-KS-106 | ROS-KS-106-video.mp4 | Phase 06 A005 | مسباح كهرمان بولندي رائع |
| ROS-021 | ROS-021-video.mp4 | Phase 09 Maroon 26jn | مسباح فاتوران الماني انتيك متحفي خام ( منجم مكحل) … طقم من الذهب عيار ٢٢ |
| ROS-057 | ROS-057-video.mp4 | Phase 09 Maroon sprkld-dots | مسباح ( فاتوران) الماني خراطه الاسطوره العثمانيه ( غالب) خام (منجم) متحفي |
| ROS-B-004 | ROS-B-004-video.mp4 | Phase 11 ROS-4 | مسباح من الكهرمان الحشري (عالم الكهرمان الحشري) |
| ROS-K-005 | ROS-K-005-video.mp4 | no row (file name) | مسباح كهرمان دمنكاني خراطه المبدع صايم |
| ROS-KS-002 | ROS-KS-002-video.mp4 | no row (file name) | مسباح كهرمان رائع |

Each of these rows got a note in its category sheet saying it has a video, plus the video-sheet text. Existing notes
were kept and the new note was appended. For ROS-021 and ROS-057 the owner's text names the material (فاتوران), and for
ROS-057 also the turner (غالب). The descriptions were not changed; this is noted for the owner.

## Red folders: video without catalog photos, so a new piece was created (7, all ROS-Amb-G)
| New code | Source video | Video-sheet row | Sheet image |
|---|---|---|---|
| ROS-Amb-G-080 | Rosary Brown Ph09 | Phase 09 Brown 26jn | frame from the video |
| ROS-Amb-G-081 | Rosary Green-Yellow Ph09 | Phase 09 Green-Yellow 26jn | frame from the video |
| ROS-Amb-G-082 | Rosary Lemon Green Ph09 | Phase 09 Lemon-Green 26jn | frame from the video |
| ROS-Amb-G-083 | Rosary Orange-Yellow Ph09 | Phase 09 Orange Jn01 | frame from the video |
| ROS-Amb-G-084 | مسباح_ROS-1_النسخة_الثانية_قاعدة_دوارة | Phase 10 ROS-1 | copy of P10_ROS1.jpg (video-sheet image) |
| ROS-Amb-G-085 | مسباح كهرمان الماني منمش ( ملتي كلر) نادر جدا | Phase 11 ROS-2 | copy of P11_ROS2.jpg (video-sheet image) |
| ROS-Amb-G-086 | كهرمان ألماني (منمش) مثالي | no row | frame from the video |

- Each folder holds `CODE-video.mp4` plus one image. The frames are small (170–260 px), uploaded inline and checked
  byte-for-byte (sha256) after upload. They are placeholders until the pieces are photographed.
- ROS-Amb-G sheet rows 81–87 (no. 80–86) were written in house style (23–29 words). The owner's wording
  «انتيك/متحفي» was not copied into the descriptions. Each note quotes the video-sheet text in full. Data in
  `data/ambg_new_rows.json` and `data/stills.json`.
- The text for 081 and 084 does not say «ألماني». Their placement in ROS-Amb-G is a judgement from appearance and is
  flagged in the notes. 081 (orange and dark green in the same bead) needs its material confirmed.

## Video sheet: Item Name column set to the catalog code (16 cells)
See `data/video_sheet_renames.json` for the old and new values. Phase 09 previously held colour labels (بني، زيتي…), and
Phase 10 and 11 held ROS-1/ROS-2/ROS-4.

## Not linked (needs the owner)
- Phase 04 A007 «مسباح كهرمان هندي شجري نادر جدا»: closest catalog piece is ROS-Amb-G-033 (same 3-bead شاهد and bead
  look), but the tassel differs and the owner's text says «هندي», not German. No folder was created; awaiting confirmation.
- Phase 09 rows 8–11 (Brown to-Yellow; Green «خراطة المبدع عبدالعزيز كرم»; Maroon Sprkl-Crcls; Orange to-glow-Yellow)
  have **no video file** in the folder (Phase 09 has only "First edit" files for 6 rosaries). Not touched.
- v09 «Broush (Rosary) - Draft»: a graduated strand with a screw clasp and no شاهد (necklace, not a rosary). Not linked.
- v07 A009, v22 A001, v23 A014: amber objects that are not rosaries (raw stone, tower, clock).

## Caveats
- Folder colours (green #16a765, red #f83a22) are a per-user Drive setting of the connected account
  (islamic.treasures.kw@gmail.com).
- The copies use extra Drive storage: 17 videos, about 1.8 GB (10 into green folders + 7 into red folders).
