#!/usr/bin/env bash
# End-to-end pipeline test on synthetic clips (a bright textured "blade" on a dark background), no real footage needed.
set -euo pipefail; cd "$(dirname "$0")/.."; mkdir -p work/synth
ffmpeg -y -v error -f lavfi -i "color=c=0x101010:s=1920x1080:r=30000/1001:d=6" -f lavfi -i "color=c=gray:s=1100x120:r=30000/1001:d=6" -filter_complex "[1:v]geq=lum='150+70*sin(X/9)*sin(Y/7)':cb=128:cr=128,pad=1920:1080:400:480:black,format=yuv420p[b];[0:v][b]blend=all_mode=lighten,format=yuv420p" -t 6 -c:v libx264 -crf 12 work/synth/a.mp4
ffmpeg -y -v error -f lavfi -i "testsrc2=s=1920x1080:r=30000/1001:d=5" -vf "eq=brightness=-0.3" -c:v libx264 -crf 12 work/synth/b.mp4
ffmpeg -y -v error -f lavfi -i "sine=frequency=220:duration=12" -f lavfi -i "sine=frequency=440:duration=12" -filter_complex amix -ar 44100 work/synth/music.m4a
cat > work/synth/edl.json <<'J'
{"fps":"30000/1001","width":3840,"height":2160,"bitrate_mbps":40,
 "music":{"file":"work/synth/music.m4a","start":0,"fade_in":0.2,"fade_out":1.5,"lufs":-14,"tp":-1},
 "accents":[0.116,2.0,4.5,7.0],
 "shots":[{"id":"S01","src":"work/synth/a.mp4","in":0.5,"out":5.0,"speed":1.0,"color":"mp4","crop":null,"grade":{"contrast":1.05},
           "sweeps":[{"peak":1.5,"dur":0.9,"dir":"ltr","width":0.10,"soft":0.7,"gain":0.9,"thr":0.35,"sat":0.3}]},
          {"id":"S02","src":"work/synth/b.mp4","in":1.0,"out":3.5,"speed":1.0,"color":"mp4","transition_in":{"type":"dissolve","dur":0.4},"fade_out":0.5}],
 "tail_black":0.5}
J
python3 tools/render.py work/synth/edl.json --out work/synth/out_preview.mp4 --preview
python3 tools/render.py work/synth/edl.json --out work/synth/out_4k.mp4
ffprobe -v error -show_entries stream=codec_name,profile,width,height,r_frame_rate,pix_fmt,color_primaries,color_transfer,color_space,bit_rate,sample_rate,channels:format=duration,bit_rate -of default=nw=1 work/synth/out_4k.mp4
python3 tools/qc_frames.py work/synth/edl.json work/synth/out_4k.mp4 work/synth/qc | head -30
ffmpeg -v info -i work/synth/out_4k.mp4 -af ebur128=peak=true -f null - 2>&1 | grep -A8 Summary | grep -E "I:|Peak:"
