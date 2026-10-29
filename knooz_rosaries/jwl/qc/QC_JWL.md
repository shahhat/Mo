# QC: check catalog descriptions against the photos (jewelry, Islamic Treasures)

The descriptions were written by several people from the photos. Your job is an independent check: find claims
that the photos do not support, and propose a fix. Read only; do not touch Google Drive or the sheets.

## Paths
- **JWL** = /tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/jwl
- **JWL/catalog_rows.json**: list of rows `{code, cat, piece, hero, desc, ic, notes, photos, videos, video_only}`.
- **JWL/desc/ps/<piece>.jpg**: contact sheet of the piece's photos (hero first, labelled #n).
- **JWL/timeline.json**: #n → Drive `id`. High res: `curl -sS -L -o x.jpg "https://lh3.googleusercontent.com/d/<id>=w1600"`
  (work in JWL/qc/work_<yourname>/, delete big files after).
- **JWL/DESCRIBE_JWL.md**: the rules the writers followed (what may and may not be claimed).

## What to check, per row
1. Object type and Item Category (ring / pendant / brooch / bracelet / set…) agree with the photos.
2. Stone: colour, shape (oval, round, rectangular, pear, cut corners…), cabochon vs flat engraved vs faceted.
3. Engraving: if the description says «منقوش», the stone is engraved; if it quotes an inscription, the words are
   really there (check at high resolution, flip seal engravings horizontally). An inscription quoted but not legible
   = an error.
4. Mount details named (claws, beaded bezel, openwork, fluted shank, colour of metal «ذهبي اللون/فضي اللون»).
5. Maker phrase matches the category: B «بيكلو», H «حسين جدي» (أسطورة المجوهرات), HS «أبناء الأستاذ حسين جدي», none for
   W/R/RS.
6. Hero (`hero`) is a full view of the piece (not a hallmark close-up).
7. Rows with `videos` (not video_only): the description is Abu Ali's video text and must stay as is. Only check that
   the video text is not plainly contradicted by the photos (e.g. it says turquoise and the stone is red). Report a
   contradiction as a flag for the owner, do not rewrite it. Skip video_only rows.

Minor style preferences are not errors. Report only real problems.

## Output
Write JWL/qc/qc_<yourname>.json: a list of problems only:
`{"code": "...", "field": "desc|ic|hero|notes", "problem": "English, specific, with photo #", "fix": "proposed new Arabic
description / value, following DESCRIBE_JWL.md, or empty for a flag only", "severity": "error|flag"}`.
Reply with the count of rows checked, problems found, and a short table.
