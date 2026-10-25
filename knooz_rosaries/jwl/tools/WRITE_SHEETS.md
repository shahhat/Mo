# Write catalog rows into Google Sheets (verbatim copy job)

Input: `/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/jwl/sheet_payload_r1.json`
= `{CAT: {"sheet": "<spreadsheet id>", "rows": [[A, B, C, D, E, F, G], ...]}}`. Row i of the list goes to sheet row i+1
(row 1 is the header and must not be touched). The tab is named after the category: `JWL-W`, `JWL-B`, `JWL-H`,
`JWL-R`, `JWL-RS`, `JWL-HS`.

Tool: `mcp__Google_Sheets__update_values` (load with ToolSearch `select:mcp__Google_Sheets__update_values` if it is
deferred). Range like `JWL-RS!A2:G26`. Values are written as typed by a user: column B holds `=IMAGE(...)` formulas
and must stay formulas; column A holds the number as a string; empty strings stay empty.

Rules:
- Copy every cell **exactly**, character for character (Arabic text, quotes «» and "", brackets, digits). Do not
  retype from memory: load the JSON with Python, print the chunk as JSON, and paste that JSON into the tool call.
- Write in chunks of at most 20 rows (e.g. A2:G21, A22:G41, …).
- After writing, verify: download
  `https://docs.google.com/spreadsheets/d/<id>/export?format=csv&gid=0` with curl (it is shared by link), parse it
  with Python's csv module, and compare columns A, C, D, E, F, G of rows 2.. with the payload (column B shows the
  image, not the formula, so skip it). Any mismatch → rewrite that row and re-verify. Also confirm no rows exist
  beyond the payload.
- Touch only your categories. Do not change formatting.

Reply briefly: per category rows written, mismatches found/fixed (0 expected at the end).
