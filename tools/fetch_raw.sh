#!/usr/bin/env bash
# Download the 19 raw clips of Drive folder "خنجر 2" (link-shared, reader=anyone) into raw/.
# Needs HTTPS access to drive.google.com and drive.usercontent.google.com.
set -euo pipefail
RAW="${1:-raw}"; mkdir -p "$RAW"
while IFS='|' read -r name id; do
  [ -s "$RAW/$name" ] && { echo "have $name"; continue; }
  echo "fetching $name"
  curl -sS -L -o "$RAW/$name" "https://drive.usercontent.google.com/download?id=${id}&export=download&confirm=t"
  if [ "$(stat -c %s "$RAW/$name")" -lt 100000 ]; then
    curl -sS -L -o "$RAW/$name" "https://drive.google.com/uc?export=download&confirm=t&id=${id}"
  fi
done <<'LIST'
1.mp4|1Bd7Z5gsQliAnhscTq-NgRZZ0Ws8zZXYU
2.MOV|1GsPDO4F0FJg-cGTx_jeBjBrNasRHAApr
3.MOV|1VE99Uvlwh26BNbodC73B_Q76dqmwuwma
4.MOV|1HhhbjKrefjsSxipse39sMQfQyUjlQn0b
5.mp4|1dOSdkASKOzqSpFj29H7P1LU3Gv5HIx8v
6.mp4|11C05uOoJUo-9CRGk9nOItF6yixv6OZVu
7.mp4|1N3LufIwoY-lV-MYuvNhsjbG7HjlYKOTO
8.mp4|1nZu66vv9kE4wl-Aw1zvlNUhTC2pMFAHD
9.mp4|1x9qSv98AXhDDBptt6HTzEqh29_nKGCZ0
10.mp4|1Qh3L0KLlCQ9KEVtGaRQXsthrQayZrMTC
g (5).mp4|1oVVmapB3AgkF-XYbfZ3nVDm3Hjyho2nP
g (6).mp4|1_rBEfoicZBM5piQ58M5vOB9v4CEFF_Rb
g (7).mp4|1c3YoAyiPVBWfWGDnmdEb-9EpThEKhtKT
g (8).mp4|1KEohOY0GJArjHp0axCYPtqrrVvgNf1Xi
g (9) - Trim.mp4|1mn_8YEpgd96zML-CVMPVanXnW8GLAn7r
g (10).mp4|1nE4J_M0yx6ONruQqtd0BehsaTOFyLsrI
g (15).mp4|1Ndvi5pYefkY03-KikIhT_5u947uV669M
g (16).mp4|1YVl9A3GSKVM7ztFyZsOK_xHPXIZuW5p6
g (17).mp4|1g0FhhO37Cv5PDJMa4TxIeRrnTRWFLb-e
LIST
ls -la "$RAW"
