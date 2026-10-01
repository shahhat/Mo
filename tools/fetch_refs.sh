#!/usr/bin/env bash
# Download the 16 available playlist films (1080p video-only + AAC audio) into refs/ with yt-dlp.
# Needs HTTPS access to youtube.com and *.googlevideo.com.  tFtgbamrsW8 is hidden/unavailable on the playlist.
set -euo pipefail
OUT="${1:-refs}"; mkdir -p "$OUT"
for v in zbogFazrrDc eTN_z23PXQM rcS_9G48m7A SnWFXN3_5Vc sgcoQP1xOE8 jtq9qQXMAVk lraIieMtNkk n38xRZ8hWkQ NAhjb_wLeBE 5x8uuTsqScM AZU8XgxeDJ4 NFRl0HekN-w ldDOZyoE__U ud5bWwKrWFU VgZXOWyRDak WHyDL7lN57g; do
  [ -s "$OUT/ref_$v.mp4" ] || yt-dlp -q -f "137/136/best[height<=1080]" -o "$OUT/ref_$v.mp4" "https://www.youtube.com/watch?v=$v"
  [ -s "$OUT/ref_$v.m4a" ] || yt-dlp -q -f "140/bestaudio" -o "$OUT/ref_$v.m4a" "https://www.youtube.com/watch?v=$v"
done
