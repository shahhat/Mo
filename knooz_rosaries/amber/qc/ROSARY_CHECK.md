# Are these amber bead strands rosaries, and are they already in the rosary catalog?

The owner (a Kuwaiti dealer of Islamic collectibles) keeps two separate catalogs on Google Drive:
- the **amber catalog** (stones, amber artifacts, carvings), and
- the **rosary catalog** «ROS- مسابح», with six categories: ROS-K «مسابيح كهرب شفافه» (transparent amber), ROS-KS
  «مسابيح كهرب صاك» (opaque amber), ROS-Amb-G «الكهرمان الالماني» (German amber), ROS-B «مسابيح حشرية» (insect amber),
  ROS-S «مسابيح حجر واحد» (one-stone), ROS «مسابيح منوعه» (various / faturan / other materials).

The owner says every amber **rosary** (مسبحة) must live in the rosary catalog, not in the amber catalog. Some bead
strands were filed in the amber catalog as "necklace" or "bead strand". Your job: for each candidate, decide whether it
is a rosary, and if so whether the same physical rosary is already in the rosary catalog.

## Candidates
`/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/amb/qc/bead_candidates.json`: code →
contact sheet (all its photos), Drive file ids, current description and notes. High resolution of any photo:
`curl -sS -L -o out.jpg "https://lh3.googleusercontent.com/d/<id>=w1600"` (save under
`/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/amb/qc/rwork/`).

## Rosary catalog references
- `/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/vid/gal/<CAT>_<n>.jpg`: galleries of
  the main photo of every rosary (363 pieces), labelled with the code; `NEW_video_only.jpg` = rosaries known only from
  videos. `vid/heroes.json`: code → {cat, hero (Drive id), desc}.
- More photos of a catalog rosary: `cd /tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/vid && python3 -c "from cmp import photos, th; print(photos('ROS-KS-012'))"`
  lists its Drive files; `th(id)` downloads a 500 px thumbnail into vid/th/.
- 20 rosaries added later from raw sessions (ROS-Amb-G-087…097 and others) are on boards
  `/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/r6/sp/<session-key>.jpg`; the
  session→code table is in `/home/user/Mo/knooz_rosaries/round6_sessions/CHANGES.md`.

## Method
1. **Rosary or not?** A rosary has a fixed bead count (commonly 33, 45, 66, 99 or 101 beads), usually a شاهد/imam
   (the long end piece), often فواصل (spacers) and a tassel, and is strung on cord with no clasp. A necklace usually has a
   clasp (spring ring, box clasp, screw clasp), often graduated bead sizes rising to a big centre bead, and no شاهد.
   Count the beads where you can (say how you counted). A strand photographed without its شاهد/tassel can still be a
   rosary: judge from count, uniformity and cord. Say clearly when you cannot tell.
2. **Already in the rosary catalog?** For each rosary, search the whole relevant gallery or galleries (not just one).
   Match on FIXED features that a restring would not change: bead shape, size ratio, colour and pattern of individual
   beads, odd or damaged beads, the شاهد. Background and tassel may differ between shoots. Confirm a match at high
   resolution with at least two independent bead-level features; otherwise call it "no match" or "possible".
3. **If new:** recommend the category: ROS-K if the beads are transparent amber, ROS-KS if opaque/«صاك» amber,
   ROS-Amb-G only if there is real evidence of German amber (the owner's text or a mark), ROS if the material may be
   faturan/resin/copal or is otherwise doubtful. Give your reason.

## Output
Write `/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/amb/qc/rosary_check.json`, a list:
`{"code", "is_rosary": "yes|no|unsure", "bead_count": "...", "evidence": "...", "match": "ROS-...|none|possible:ROS-...",
"match_evidence": "...", "recommended_category": "...", "category_reason": "...", "confidence": "high|medium|low"}`.
Do not use any Google Drive or Sheets tools and do not change anything except files in qc/rwork/ and your output file.
Reply with a short table of your verdicts.
