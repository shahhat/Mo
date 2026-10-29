# Execute: video copies, folder colours, video-folder renames (jewelry catalog)

Tools: `mcp__Google_Drive__copy_file`, `mcp__Google_Drive__update_file` (ToolSearch
`select:mcp__Google_Drive__copy_file,mcp__Google_Drive__update_file` if deferred). Never trash or delete anything.

Input: `/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/jwl/video_ops.json`, 40 entries:
`{"code","folder_id","color","video_only","copy_from","copy_title","vid_renames":[{"v","id","old","new"}]}`.

For each entry, in order:
1. `copy_file` with `fileId` = copy_from, `parentId` = folder_id, `title` = copy_title. Check the result's parentId
   and title. (The source is the owner's original phase video; the copy is server-side.)
2. `update_file` with `fileId` = folder_id, `folderColorRgb` = color.
3. For each vid_renames item: `update_file` with `fileId` = id, `title` = new. (These are the copies inside the
   «JWL - VID» folder; do not change their parent.)

Log every call to `/tmp/claude-0/-home-user-Mo/5eb399f8-7842-5917-9708-a745429f0c3f/scratchpad/jwl/exec_videos_log.json`
as a list `{"code","copy_id","copy_ok","color_ok","renames":[{"id","new","ok"}],"error"}`, rewriting the file after each
entry. If the log exists, skip entries already complete and do not copy a video twice (reuse copy_id). Retry a failed
call once; record failures and continue.

Reply briefly: copies made, folders coloured, renames done, failures.
