# Causality for Digital Twins (Sirris, 19 Nov 2026, 40 min)

Online: https://gmpal.github.io/talk-sirris-dt-causality/ (or open `index.html` in a browser, everything is local). `S` = speaker view: every slide of the talk has a
note that starts with the clock time at which the slide should begin.

Built from the knowledge-sharing deck, which must sit next to this folder as `../talk-causal-discovery-reveal`
(not in this repository; `index.html` here is already built):

    python3 build.py        # no pandoc / tectonic needed

- `build.py`: the running order (`PLAN`), with the speaker notes. Existing slides are picked by title from the
  knowledge-sharing `index.html`; drop, add or reorder lines there.
- `slides.py`: the new slides (digital-twin framing, injection molding, pretrained discovery in one slide, dashboard, wrap-up).
- `css/sirris.css`: styles of the new slides.
- `shots/render.sh [n ...]`: screenshots of the slides (0-based) into `shots/tmp`, to check the layout.

PDF export: `python3 shots/pdf.py` writes `causality-for-digital-twins.pdf` (one page per slide, all steps shown; the chat slide gets two pages).
