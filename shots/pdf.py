#!/usr/bin/env python3
"""Export the deck to PDF: one page per slide (all fragments shown), from headless-Chromium screenshots.

    python3 shots/pdf.py            # -> causality-for-digital-twins.pdf

(Chromium's own print-to-pdf gives a blank page on this machine, hence the screenshots.)
"""
import os, re, shutil, subprocess, sys, tempfile, time
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "causality-for-digital-twins.pdf")
PORT = 8767
# slides that also get a page at an intermediate step: (text contained in the slide) -> fragment index
EXTRA = {'<div class="chat">': [1]}

os.chdir(ROOT)
html = open("index.html", encoding="utf-8").read()
secs = re.findall(r"<section\b.*?</section>", html, re.S)
js = open("js/deck.js", encoding="utf-8").read()
assert "if (printing || from === to)" in js
open("js/_deck_pdf.js", "w", encoding="utf-8").write(js.replace("if (printing || from === to)", "if (true)"))
open("_pdf.html", "w", encoding="utf-8").write(
    html.replace("js/deck.js", "js/_deck_pdf.js").replace(
        "</head>", "<style>*,*::before,*::after{animation:none!important;transition:none!important}"
                   ".reveal .controls,.reveal .progress{display:none!important}</style></head>"))
srv = subprocess.Popen([sys.executable, "-m", "http.server", str(PORT), "--bind", "127.0.0.1"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
tmp = tempfile.mkdtemp(dir=os.path.join(ROOT, "shots"))
pages = []
try:
    time.sleep(1)
    for i, s in enumerate(secs):
        steps = [f for k, v in EXTRA.items() if k in s for f in v] + [60]
        for f in steps:
            png = os.path.join(tmp, f"s{i:02d}_{f:02d}.png")
            subprocess.run(["chromium", "--headless", "--disable-gpu", "--hide-scrollbars", "--window-size=1280,720",
                            "--force-device-scale-factor=2", "--virtual-time-budget=6000", f"--screenshot={png}",
                            f"http://127.0.0.1:{PORT}/_pdf.html#/{i}/0/{f}"],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)
            pages.append(Image.open(png).convert("RGB"))
            print(f"\r{i + 1}/{len(secs)}", end="", flush=True)
    pages[0].save(OUT, save_all=True, append_images=pages[1:], resolution=192, quality=88)
    print(f"\n{len(pages)} pages -> {OUT}")
finally:
    srv.terminate()
    shutil.rmtree(tmp, ignore_errors=True)
    for f in ("_pdf.html", "js/_deck_pdf.js"):
        os.path.exists(f) and os.remove(f)
