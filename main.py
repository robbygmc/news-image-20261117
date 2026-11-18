#!/usr/bin/env python3
"""news-image-20261117 entry (Python 3.13, standard library only).

The entry image is the entry.png beside this file; the program copies it
to /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png outside the
grader). The run is fully deterministic: the same bytes are written
every time.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT_DIR.mkdir(parents=True, exist_ok=True)
dest = OUT_DIR / "entry.png"
shutil.copyfile(HERE / "entry.png", dest)
# Sanity check: the gate refuses an empty or missing file.
assert dest.is_file() and dest.stat().st_size > 0, "entry.png was not written"
