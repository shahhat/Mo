# Execute a Google Drive restructure batch (jewelry catalog)

You apply a pre-computed plan to the owner's Google Drive with the Google Drive connector tools
(`mcp__Google_Drive__create_file`, `mcp__Google_Drive__update_file`; load them with ToolSearch
`select:mcp__Google_Drive__create_file,mcp__Google_Drive__update_file` if they are deferred). The plan was checked;
do not change it and do not make decisions about content. **Never trash, delete or copy anything.**

## Input
`JWL/ops_<k>.json` (JWL = /tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/jwl): a list of
pieces, each:
```
{"code": "JWL-W-001",
 "folder": {"action": "create", "name": "JWL-W-001", "parent": "<category folder id>"}
         | {"action": "existing", "id": "<folder id>", "rename": "JWL-B-031", "move_to"?: "<id>"},
 "photos": [{"n": 9, "id": "<file id>", "old_name": "...", "old_parent": "...", "new_name": "JWL-W-001-1.jpg"}, ...],
 "dups":   [{"n": 8, "id": "<file id>", "name": "...", "old_parent": "...", "dest": "<_Duplicates folder id>", "move": true}, ...],
 "video_only"?: true}
```

## Steps, per piece, in order
1. Folder:
   - "create": `create_file` with `title` = name, `contentMimeType` = `application/vnd.google-apps.folder`,
     `parentId` = parent. Keep the returned `id` as folder_id.
   - "existing": `update_file` with `fileId` = id, `title` = rename (plus `parentId` = move_to if present).
     folder_id = id.
2. Each photo: one `update_file` call with `fileId` = photo id, `parentId` = folder_id, `title` = new_name.
3. Each dup with `"move": true`: `update_file` with `fileId` = id, `parentId` = dest (do not change the title).
4. A "video_only" piece has no photos: only create its folder.

## Log (so the work can resume)
Keep `JWL/exec_log_<k>.json` = list of
`{"code", "folder_id", "folder_created": bool, "photos": [{"id","title","parentId","ok","error"}], "dups": [{"id","parentId","ok","error"}], "done": bool}`.
Write the file after every piece (rewrite the whole JSON). At start, if the log exists, skip pieces with
`"done": true`, and for a piece with a folder_id but not done, reuse that folder_id (do not create a second folder)
and redo only the items not marked ok.

Check each tool result: the returned `parentId` and `title` must equal what you asked for. On an error, retry that
call once; if it fails again, record ok=false with the error text and continue.

## Finish
Reply with: pieces done, folders created, photos moved, dups moved, and every failure (code, file id, error). Be brief.
