// Deck behaviour: math, auto-fit of dense slides, step-driven diagrams, animated charts.
(function () {
  const H = 720, BOTTOM = 34, NS = 'http://www.w3.org/2000/svg';
  const printing = /print-pdf/.test(location.search);

  function renderMath() {
    document.querySelectorAll('span.math').forEach(el => {
      if (el.dataset.done) return;
      try { katex.render(el.textContent, el, { displayMode: el.classList.contains('display'), throwOnError: false, strict: false }); } catch (e) {}
      el.dataset.done = '1';
    });
  }

  // ---------- fit dense slides ----------
  function fit(sec) {
    const body = sec.querySelector(':scope > .sbody');
    if (!body) return;
    const inner = body.firstElementChild;
    inner.style.transform = 'none'; inner.style.width = '100%'; inner.style.marginTop = '0px';
    const avail = H - body.offsetTop - BOTTOM;
    let h = inner.scrollHeight;
    if (h <= avail) {
      if (!sec.classList.contains('top')) inner.style.marginTop = Math.min((avail - h) * 0.3, 70) + 'px';
      return;
    }
    let r = avail / h;
    for (let i = 0; i < 6; i++) {
      inner.style.width = (100 / r) + '%';
      h = inner.scrollHeight;
      const r2 = Math.min(1, avail / h);
      if (Math.abs(r2 - r) < 0.004) { r = Math.min(r, r2); break; }
      r = (r + r2) / 2;
    }
    r *= 0.985;
    inner.style.width = (100 / r) + '%';
    inner.style.transform = 'scale(' + r + ')';
    body.style.height = avail + 'px';
  }
  function fitAll() { document.querySelectorAll('.reveal .slides section.s').forEach(fit); }

  // ---------- numbers that count ----------
  function fmt(el, v) {
    const dec = +(el.dataset.dec || 0);
    let s = v.toFixed(dec);
    if (el.dataset.lead === '0') s = s.replace(/^0\./, '.');
    return (el.dataset.pre || '') + s + (el.dataset.suf || '');
  }
  function animNum(el, to, dur) {
    const from = el._cur === undefined ? 0 : el._cur;
    el._cur = to;
    if (printing || from === to) { el.textContent = fmt(el, to); return; }
    const t0 = performance.now(); const id = (el._anim = (el._anim || 0) + 1);
    function tick(t) {
      if (el._anim !== id) return;
      const k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 3);
      el.textContent = fmt(el, from + (to - from) * e);
      if (k < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }
  function shown(el) { const f = el.closest('.fragment'); return !f || f.classList.contains('visible'); }
  function counts(sec) {
    sec.querySelectorAll('[data-count]').forEach(el => {
      if (shown(el)) { if (!el._ran) { el._ran = true; el._cur = 0; animNum(el, +el.dataset.count, 1300); } }
      else { el._ran = false; el._cur = 0; el.textContent = fmt(el, 0); }
    });
  }

  // ---------- line charts built from JSON ----------
  function svg(tag, attrs, parent, text) {
    const e = document.createElementNS(NS, tag);
    for (const k in attrs) e.setAttribute(k, attrs[k]);
    if (text !== undefined) e.textContent = text;
    if (parent) parent.appendChild(e);
    return e;
  }
  function buildChart(el) {
    const c = JSON.parse(el.querySelector('script').textContent);
    const W = c.w || 640, Hh = c.h || 400, m = Object.assign({ l: 62, r: 96, t: 16, b: 50 }, c.m || {});
    const pw = W - m.l - m.r, ph = Hh - m.t - m.b;
    const tr = (a, v) => a.log ? Math.log10(v) : v;
    const sx = v => m.l + (tr(c.x, v) - tr(c.x, c.x.min)) / (tr(c.x, c.x.max) - tr(c.x, c.x.min)) * pw;
    const sy = v => m.t + ph - (tr(c.y, v) - tr(c.y, c.y.min)) / (tr(c.y, c.y.max) - tr(c.y, c.y.min)) * ph;
    const s = svg('svg', { viewBox: `0 0 ${W} ${Hh}`, width: W, height: Hh, class: 'lc' }, el);
    if (c.zone) {
      svg('rect', { x: sx(c.zone[0]), y: m.t, width: sx(c.zone[1]) - sx(c.zone[0]), height: ph, class: 'zone' }, s);
      svg('text', { x: sx(c.zone[0]) + 8, y: m.t + 18, class: 'zl' }, s, c.zone[2]);
    }
    c.y.ticks.forEach(t => {
      svg('line', { x1: m.l, x2: m.l + pw, y1: sy(t), y2: sy(t), class: 'grid' }, s);
      svg('text', { x: m.l - 10, y: sy(t), class: 'ty' }, s, c.y.fmt ? c.y.fmt[c.y.ticks.indexOf(t)] : String(t));
    });
    c.x.ticks.forEach(t => {
      svg('line', { x1: sx(t), x2: sx(t), y1: m.t + ph, y2: m.t + ph + 6, class: 'axis' }, s);
      svg('text', { x: sx(t), y: m.t + ph + 22, class: 'tx' }, s, c.x.fmt ? c.x.fmt[c.x.ticks.indexOf(t)] : String(t));
    });
    svg('line', { x1: m.l, x2: m.l + pw, y1: m.t + ph, y2: m.t + ph, class: 'axis' }, s);
    if (c.x.label) svg('text', { x: m.l + pw / 2, y: Hh - 6, class: 'al' }, s, c.x.label);
    if (c.y.label) svg('text', { x: 16, y: m.t + ph / 2, class: 'al', transform: `rotate(-90 16 ${m.t + ph / 2})` }, s, c.y.label);
    if (c.title) svg('text', { x: m.l + pw / 2, y: 12, class: 'ct' }, s, c.title);
    c.series.forEach(se => {
      const st = se.step || 0, d = se.pts.map((p, i) => (i ? 'L' : 'M') + sx(p[0]).toFixed(1) + ',' + sy(p[1]).toFixed(1)).join(' ');
      const p = svg('path', { d: d, class: 'ln' + (se.bold ? ' bold' : ''), stroke: se.color, 'data-from': st }, s);
      const len = p.getTotalLength() || 1000;
      p.style.setProperty('--len', len);
      se.pts.forEach((pt, i) => {
        const dot = svg('circle', { cx: sx(pt[0]), cy: sy(pt[1]), r: se.bold ? 5.5 : 3.6, fill: se.color, class: 'dot', 'data-from': st }, s);
        dot.style.transitionDelay = (0.15 + 1.25 * i / Math.max(1, se.pts.length - 1)) + 's';
      });
      if (se.name && c.labels !== false) {
        const last = se.pts[se.pts.length - 1], o = se.lo || [10, 0];
        const t = svg('text', { x: sx(last[0]) + o[0], y: sy(last[1]) + o[1], class: 'sl' + (se.bold ? ' bold' : ''), fill: se.color, 'data-from': st }, s, se.name);
        t.style.transitionDelay = '1.3s';
      }
    });
  }

  // ---------- one-off preparation ----------
  function prepare() {
    document.querySelectorAll('.lchart').forEach(buildChart);
    document.querySelectorAll('svg.dag').forEach(g => {
      let i = 0;
      g.querySelectorAll('.e').forEach(e => {
        const dashed = e.classList.contains('cut') || e.classList.contains('test');
        if (dashed) return;
        const len = e.getTotalLength ? e.getTotalLength() : 200;
        e.style.setProperty('--len', len);
        if (e.dataset.from === undefined) { e.classList.add('draw'); e.style.setProperty('--d', (0.35 + 0.22 * i++) + 's'); }
        else if (e.classList.contains('hot')) e.classList.add('drawstep');
      });
    });
    document.querySelectorAll('.fit table tbody tr').forEach(tr => tr.style.setProperty('--i', [...tr.parentNode.children].indexOf(tr)));
  }

  // ---------- step-driven elements ----------
  function step(sec) {
    if (!sec) return;
    const n = sec.querySelectorAll('.fragment.visible').length;
    sec.querySelectorAll('[data-from]').forEach(el => {
      const a = +el.dataset.from, b = el.dataset.to === undefined ? 99 : +el.dataset.to;
      el.classList.toggle('on', n >= a && n <= b);
    });
    sec.querySelectorAll('.sbar').forEach(el => {
      const vals = el.dataset.vals.split(',').map(Number), base = +(el.dataset.base || 0);
      const v = vals[Math.max(0, Math.min(vals.length - 1, n - base))];
      const lo = +(el.dataset.min || 0), hi = +(el.dataset.max || 100);
      el.firstElementChild.style.width = Math.max(0, (v - lo) / (hi - lo) * 100) + '%';
      el.classList.toggle('changed', n - base > 0);
      const num = el.parentNode.querySelector('.bv');
      if (num) animNum(num, v, 1100);
    });
    counts(sec);
  }
  // restart the entrance animations of a slide
  function activate(sec) {
    if (!sec) return;
    sec.classList.remove('go');
    sec.querySelectorAll('[data-from]').forEach(el => el.classList.remove('on'));
    sec.querySelectorAll('.sbar > i').forEach(i => { i.style.width = '0%'; });
    sec.querySelectorAll('.bv').forEach(b => { b._cur = 0; });
    sec.querySelectorAll('[data-count]').forEach(el => { el._ran = false; });
    void sec.offsetWidth;
    sec.classList.add('go');
    step(sec);
  }
  function all(fn) { document.querySelectorAll('.reveal .slides section').forEach(fn); }

  Reveal.initialize({
    width: 1280, height: 720, margin: 0.03, center: false, hash: true,
    slideNumber: 'c/t', controls: true, controlsTutorial: false, progress: true,
    transition: 'slide', transitionSpeed: 'default', backgroundTransition: 'fade',
    viewDistance: 400, mobileViewDistance: 400, pdfSeparateFragments: false, pdfMaxPagesPerSlide: 1,
    autoAnimateDuration: 0.8, autoAnimateEasing: 'cubic-bezier(.2,.8,.2,1)',
    plugins: (typeof RevealNotes !== 'undefined') ? [RevealNotes] : []
  }).then(() => {
    if (printing) document.documentElement.classList.add('print-pdf');
    renderMath();
    prepare();
    const go = () => { fitAll(); };
    go();
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(go);
    window.addEventListener('load', go);
    setTimeout(go, 600);
    all(step);
    if (printing) all(s => { s.classList.add('go'); step(s); });
    else activate(Reveal.getCurrentSlide());
  });
  Reveal.on('slidechanged', e => activate(e.currentSlide));
  Reveal.on('fragmentshown', () => step(Reveal.getCurrentSlide()));
  Reveal.on('fragmenthidden', () => step(Reveal.getCurrentSlide()));
  Reveal.on('overviewshown', () => all(s => { s.classList.add('go'); step(s); }));
  Reveal.on('pdf-ready', () => { renderMath(); fitAll(); all(s => { s.classList.add('go'); step(s); }); });
})();
