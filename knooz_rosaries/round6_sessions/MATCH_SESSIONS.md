# Match unclassified photo-session rosaries to the catalog

Context: Islamic Treasures (Kuwait) sells rare rosaries. Every rosary in the catalog has a Drive folder with photos and a
code. The categories are:
- ROS-K-###: clear amber.
- ROS-KS-###: opaque or semi-opaque amber («كهرب صاك»), including butterscotch, Polish and «Indian» amber.
- ROS-S-###: one-stone.
- ROS-B-###: insect amber.
- ROS-Amb-G-###: German amber.
- ROS-###: mixed materials, including faturan, bakelite, wood, kuk, black coral/يسر and similar.

The owner has a folder of raw, unclassified photo sessions (79–82). Each "session piece" is one rosary. The owner wants
each one filed into the catalog: a new code in the right category, or, if the piece is ALREADY in the catalog, its photos
added to that existing folder. A wrong match merges two different rosaries into one product, and a missed match creates a
duplicate product. So be strict, and look at high resolution when it matters.

Several catalog pieces were created recently from VIDEOS ONLY (no photos yet), so they are prime candidates. Their
photographers' shoot names suggest some links:
- ROS-Amb-G-084: olive-yellow round beads, lens spacers, long-necked gourd شاهد, red cord. The videographer called it «ROS-1».
- ROS-Amb-G-085: capsule beads, cream mottled with honey and red-brown, maroon cord. Called «ROS-2».
- ROS-B-004: insect amber. Called «ROS-4». It already has catalog photos.
- ROS-Amb-G-080..083 and 086: Phase 09 videos.
- ROS-KS-151: «Indian tree amber», butterscotch ovals, 3-bead شاهد, gold braided cord.
See `VID/gal/NEW_video_only.jpg` (stills). The session folder names «ROS - 1», «ROS-2», «ROS-4» are only a hint; verify them
visually. The numbering may restart per session, so the same name can be a different piece.

Paths:
- R6 = /tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/r6
- VID = /tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/vid
- R6/pieces.json: session piece key → files `[{id, name}]`. Thumbnails (400 px) are at R6/th/<id>.jpg, and each piece has
  a board at R6/sp/<key>.jpg (all its photos, numbered). High resolution of any Drive photo:
  `curl -sS -L -o out.jpg "https://lh3.googleusercontent.com/d/<id>=w1600"`. Save crops under R6/work_<yourname>/.
- VID/gal/<CAT>_<n>.jpg: galleries of the main catalog photo of every piece, labelled with the code. 363 pieces, plus
  VID/gal/NEW_video_only.jpg.
- VID/heroes.json: code → {cat, hero (Drive id), desc (Arabic catalog description)}.
- To see more photos of a catalog piece: `cd VID && python3 -c "from cmp import photos, th; ..."`. `photos(code)` lists
  its Drive files (id, title) and `th(id)` downloads a 500 px thumbnail into VID/th/.

Method:
1. Identify by FIXED features first, the ones a restring would not change: bead shape, size, colour and pattern; the شاهد
   (imame) shape; the spacers; the metal fittings.
2. Then check the cord and tassel. These can be replaced, so note it if they differ.
3. Check the rough bead count (33 / 45 / 66 / 99, long strands, and so on).
4. Search the whole relevant gallery or galleries, not only my hints. German-looking multi-colour or مُنمّش amber is
   usually in ROS-Amb-G. Butterscotch, Polish or egg-yolk amber is usually in ROS-KS. Red or cherry beads that may be
   faturan or bakelite are in ROS. Check ROS-K too for transparent pieces.

Output: write R6/match_<yourname>.json as a list of:
`{"key": "...", "code": "ROS-...|NEW", "confidence": "high|medium|low", "category_if_new": "ROS-...", "hero_photo": <1-based index into the piece's files that best shows the WHOLE rosary>, "evidence": "short English", "alternatives": ["..."], "visual": "for NEW: 1–2 English sentences describing beads, شاهد, spacers, tassel/cord, approx bead count, transparency"}`

For NEW, choose the category from the material and look. When the material is uncertain (faturan/bakelite/amber), say so
in the evidence. Reply with a compact table of your results.
