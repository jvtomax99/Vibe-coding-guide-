#!/bin/bash
# Renders everything in start/. Run from this folder. Takes about two hours on 4 CPU cores.
set -e
PY=${PY:-python3}
$PY tex.py
for v in phone desk; do
  $PY scene.py out=out/closed-$v.png view=$v samples=128
  $PY scene.py out=out/glow-$v.png view=$v samples=128 pulse=1.8
  $PY scene.py out=out/open-$v.png view=$v samples=128 mode=openstill
done
$PY scene.py view=phone samples=40 scale=75 mode=open anim=out/fp
$PY scene.py view=desk samples=40 scale=67 mode=open anim=out/fd
# stills to WebP (quality 82), frames to video
for n in closed glow open; do for v in phone desk; do
  $PY -c "from PIL import Image; Image.open('out/$n-$v.png').convert('RGB').save('../start/$n-$v.webp', quality=82, method=6)"
done; done
enc(){ # frames folder, size, name
  ffmpeg -y -loglevel error -framerate 20 -i out/$1/f%04d.png -vf "scale=$2:flags=lanczos" -c:v libx264 -profile:v main -level 3.1 -pix_fmt yuv420p -crf 23 -preset slow -movflags +faststart -an ../start/$3.mp4
  ffmpeg -y -loglevel error -framerate 20 -i out/$1/f%04d.png -vf "scale=$2:flags=lanczos" -c:v libvpx-vp9 -b:v 0 -crf 36 -pix_fmt yuv420p -an ../start/$3.webm
}
enc fp 586:1268 open-phone
enc fd 1280:800 open-desk
