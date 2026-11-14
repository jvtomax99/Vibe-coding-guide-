# Start menu source

How the pictures and clips in `start/` were made. The site does not use this folder.

The scene is built and rendered with Blender from Python: a dark book with gold
lettering on a ship's console, three glowing light pillars, a glass orb, and a planet
outside the window. Every object is made in `scene.py`; nothing was bought or
downloaded.

- `tex.py` draws the book cover (title, frame, glowing lines) and the first page
  ("Welcome aboard"). **To change the title, change the words here**, then render again.
- `scene.py` builds the scene and renders it. `view=phone` or `view=desk` picks the
  camera, `pulse=1.8` turns the lights up (the "glow" picture), `mode=open` renders the
  cover opening as 50 frames at 20 frames a second, `mode=openstill` its last frame.
- `render_all.sh` runs all of it and writes the web files into `start/`.

## The site icon

`icons/` holds the site's icon: the same scene from a low, close camera, with the
emblem drawn large on the cover so it still reads when small. `icons/source.png` is
the master picture (1024 by 1024); every other size is shrunk from it. Tab icons
(`favicon-*.png`, `favicon.ico`) have rounded corners; `apple-touch-icon.png` (phone
home screen) and `icon-512.png` (link previews) are full squares.

To render it again: `python3 tex.py`, `python3 tex_icon.py`, then
`python3 scene_icon.py out=icon/icon.png view=icon icon=3 samples=160`, and shrink the
result to each size.

## To render again

1. Install the tools: `pip install bpy pillow`, and `ffmpeg`.
2. Put three font files in `start-source/fonts/`: `BodoniModa.ttf`,
   `InstrumentSans.ttf` and `PinyonScript.ttf`, from Google Fonts (free, SIL Open Font
   License). They are not stored in this repo.
3. From this folder: `bash render_all.sh`. It takes about two hours on 4 CPU cores.
4. Open the site and check the start menu at phone and desktop size.

Nothing about a reader is in the pictures. The name and books read are text the page
puts on top.
