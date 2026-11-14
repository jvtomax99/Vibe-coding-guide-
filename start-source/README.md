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

## To render again

1. Install the tools: `pip install bpy pillow`, and `ffmpeg`.
2. Put three font files in `start-source/fonts/`: `BodoniModa.ttf`,
   `InstrumentSans.ttf` and `PinyonScript.ttf`, from Google Fonts (free, SIL Open Font
   License). They are not stored in this repo.
3. From this folder: `bash render_all.sh`. It takes about two hours on 4 CPU cores.
4. Open the site and check the start menu at phone and desktop size.

Nothing about a reader is in the pictures. The name and books read are text the page
puts on top.
