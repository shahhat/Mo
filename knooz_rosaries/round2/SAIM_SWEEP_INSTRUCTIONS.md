# Find rosaries signed by the turner Saim (صايم) — photo sweep

Context: Islamic Treasures (Kuwait) sells rare amber rosaries. The famous turner **Saim (صايم)** signs his work with a
small **metal disc stamped "SAiM"**, set into the **base of the شاهد/imame** (the long end piece) where the cord comes out.
The owner confirmed that any piece carrying this stamp is Saim's work, and wants every such piece found so its catalog
description can say «خراطة المبدع صايم». This is a high-value attribution: report only what you can actually see.

Reference photo of the stamp (look at it first):
`/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/work/thumbs/ROS-K/ROS-K-004/ROS-K-004-1.jpg`
(silver disc at the imame base, letters "S A i M" around the cord hole).

## Files
- Your piece codes: the JSON list you were given (e.g. `.../scratchpad/saim/codes1.json`).
- Contact sheet per piece (all its photos, labelled #1, #2 …):
  `.../scratchpad/work/sheets/<CAT>/<CODE>.jpg`, where CAT is the code without the last `-NNN` (e.g. ROS-Amb-G-012 → ROS-Amb-G).
- Individual 700px photos: `.../scratchpad/work/thumbs/<CAT>/<CODE>/<CODE>-<N>.jpg`.
- High resolution, when you need to read small lettering: look up the Drive file id in
  `.../scratchpad/saim/title_to_id.json` (key = `<CODE>-<N>`), then
  `curl -sS -L -o /tmp/x.jpg "https://lh3.googleusercontent.com/d/<ID>=w2400"` and crop the area with Python/PIL before viewing.
  (`...` = `/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f`.) Save crops under `.../scratchpad/saim/crops/`.

## Method (be efficient)
1. For each piece, view the contact sheet.
2. If any photo shows the base/underside of the شاهد, the point where the cord leaves it, or a metal disc/cap on the
   شاهد or at the end of the tamlika, open that 700px photo. If a disc is visible but the lettering is not readable, fetch
   the high-res version and crop it.
3. Record any other legible maker's mark or engraved name you see (on a disc, cap or the amber itself), but do not guess.

## Output
Write a JSON array to the output path you were given, one entry per code, same order:
`{"code": "...", "verdict": "SAIM" | "POSSIBLE" | "OTHER_MARK" | "NONE", "photo": <N or null>, "note": "short English"}`
- SAIM = you can read S-A-i-M (or the same stamp design clearly) on that piece.
- POSSIBLE = a stamped disc at the imame base is visible but you cannot read it even at high res.
- OTHER_MARK = a different legible mark (put the text in note).
- NONE = nothing seen.
Reply with a short summary listing the SAIM, POSSIBLE and OTHER_MARK codes.
