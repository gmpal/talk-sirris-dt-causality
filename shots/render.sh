#!/bin/bash
# Screenshot every slide (all fragments shown) into shots/tmp and make contact sheets.
cd "$(dirname "$0")/.."
N=$(grep -c '<section' index.html)
sed 's#</head>#<style>*,*::before,*::after{animation:none!important;transition:none!important}</style></head>#' index.html > _preview.html
(python3 -m http.server 8766 --bind 127.0.0.1 >/dev/null 2>&1 &) ; sleep 1
mkdir -p shots/tmp; rm -f shots/tmp/*.png
for i in $(seq 0 $((N-1))); do
  [ -n "$1" ] && [[ " $* " != *" $i "* ]] && continue
  timeout 60 chromium --headless --disable-gpu --hide-scrollbars --window-size=1280,720 --virtual-time-budget=5000 \
    --screenshot=shots/tmp/s$(printf %02d $i).png "http://127.0.0.1:8766/_preview.html#/$i/0/30" >/dev/null 2>&1
done
pkill -f 'http.server 8766'; rm -f _preview.html
