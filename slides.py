"""New slides of the Sirris deck. Sources of the numbers:
- injection molding: Paldino, Caelen, Oueslati, Ansay, Johanesa, Bontempi, FGCS 2026;
- DTD2C: dtd2c.tex of the Beamer deck (work under review)."""
import custom
from custom import dag, head, divider, _rung

K0 = "Digital twins"
K1 = "Why causality?"
KIM = "Injection molding · with Sirris"
KPT = "Pretrained causal discovery"
GRAD = 'data-background-gradient="linear-gradient(125deg,#0b132b 0%,#1c2541 55%,#5a0f2e 100%)"'

# ---------------------------------------------------------------- title
TITLE = custom.TITLE.replace("From Correlation to Causal Discovery", "From Correlation to Intervention") \
    .replace("An introduction, with a focus on time series", "Causal AI for Trustworthy Digital Twins") \
    .replace("MLG Knowledge Sharing &nbsp;·&nbsp; 17 November 2026", "Sirris &nbsp;·&nbsp; 19 November 2026")
assert "Sirris" in TITLE and "From Correlation to Intervention" in TITLE and "Causal AI for Trustworthy Digital Twins" in TITLE

# ---------------------------------------------------------------- who is talking
# MLG: mlg.ulb.ac.be. EDITS: ulb-mlg.github.io/welt_website. ARIAC: grant 2010235, SPW Recherche.
WHO = """
<section class="s">
""" + head("Who is talking", "A machine learning lab that builds digital twins") + """
<div class="sbody"><div class="fit">
<div class="grid3">
  <div class="card t-blue" style="padding:16px 20px"><span class="tag blue">The lab</span><h3 style="margin-top:.4em">Machine Learning Group, ULB</h3>
    <p class="small" style="margin:0">Founded in 2004 by Gianluca Bontempi, co-headed with Tom Lenaerts.<br>Time series and streaming sensor data, forecasting, anomaly and fraud detection, causal inference.</p></div>
  <div class="card t-gold" style="padding:16px 20px"><span class="tag gold">The project</span><h3 style="margin-top:.4em">EDITS · 2025–2029</h3>
    <p class="small" style="margin:0"><i>Enhancing Digital Twins with Scalable and Interpretable AI</i>, funded by the F.R.S.-FNRS WEL-T programme.<br>Twins of a city's traffic, of a wind farm, of a robotic arm.</p></div>
  <div class="card t-red" style="padding:16px 20px"><span class="tag red">Me</span><h3 style="margin-top:.4em">Gian Marco Paldino</h3>
    <p class="small" style="margin:0">PhD at MLG (2026), within <b>ARIAC</b> by DigitalWallonia4.ai.<br>Now postdoc on EDITS: causal discovery in time series.<br><span class="muted">Not a process engineer, and not a security analyst.</span></p></div>
</div>
<div class="card fragment" style="margin-top:20px;padding:14px 24px"><span class="tag green">We already work together</span>
  <p class="small" style="margin:.5em 0 0 0">The injection molding results of this talk come from ARIAC, on data produced at Sirris, with
  <b>Olivier Caelen</b>, <b>Marouene Oueslati</b> and <b>Marc Ansay</b>, and Tojo Valisoa Andrianandrianina Johanesa (UMONS). A follow-up with <b>Pierre Dagnely</b> is under review.</p></div>
<div class="banner fragment">We bring the methods. <em>The problems and the data are yours.</em></div>
</div></div>
</section>
"""

# ---------------------------------------------------------------- the twin has to answer "what if?"
_LOOP = """
<svg class="dag" viewBox="0 0 520 330" width="520" height="330">
<defs><marker id="ah" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs>
<path class="e" d="M 120,118 C 150,30 370,30 400,118" marker-end="url(#ah)"/>
<path class="e hot" data-from="1" d="M 400,212 C 370,300 150,300 120,212" marker-end="url(#ah)"/>
<text x="260" y="34">measures</text>
<text x="260" y="296" data-from="1" style="fill:var(--accent)">actions</text>
<rect class="n" x="20" y="125" width="200" height="80" rx="14"/><text x="120" y="152">🏭</text><text x="120" y="182">Physical twin</text>
<rect class="n blue" x="300" y="125" width="200" height="80" rx="14"/><text x="400" y="152">💻</text><text x="400" y="182">Digital twin</text>
</svg>"""

DT_WHATIF = """
<section class="s">
""" + head(K0, "A digital twin has to answer “what if?”") + """
<div class="sbody"><div class="fit">
<div class="cols" style="align-items:center">
  <div class="col" style="flex:.95">""" + _LOOP + """</div>
  <div class="col">
    <p class="muted" style="margin-bottom:12px">A twin aims to…</p>
    <div class="verbs">
      <div class="verb"><b>Emulate</b><span>reproduce what the system does</span><i class="tag blue">prediction</i></div>
      <div class="verb"><b>Anticipate</b><span>what happens next, if nothing changes</span><i class="tag blue">prediction</i></div>
      <div class="verb fragment"><b>Explain</b><span>why did this part come out wrong?</span><i class="tag red">causes</i></div>
      <div class="verb" data-from="1"><b>Control</b><span>open a valve, slow a line, change a set-point</span><i class="tag red">causes</i></div>
    </div>
  </div>
</div>
<div class="banner fragment">The moment the twin sends an action back, it stops <em>observing</em> the system and starts <em>changing</em> it. Sensor logs only tell us what moves together.</div>
</div></div>
</section>
"""

# ---------------------------------------------------------------- Simpson's paradox on the shop floor
# Illustrative numbers (1000 parts). Dry granulate: long 95/100, short 360/400. Humid: long 300/400, short 65/100.
DIV_LINE = """
<section class="divider" """ + GRAD + """ data-transition="fade">
<div class="wrap">
  <div class="num">A decision to make</div>
  <div class="big-q">You run the molding line.<br><em>Which drying time do you set?</em></div>
  <p class="sub">1000 parts from the production logs. The granulate was dried for 4 hours or for 2 hours. For each part we know whether it passed quality control.</p>
</div>
</section>
"""


def _cell(pct, frac, ab, cls="", count=True):
    c = f' data-count="{pct}" data-suf="%"' if count else ""
    return f'<div class="cell{cls}"><span class="p"{c}>{pct}%</span><span class="f">{frac}</span><div class="bar {ab}"><i style="--w:{pct}%"></i></div></div>'


CHAT = """
<section class="s top" data-transition="fade">
<div class="sbody"><div class="fit">
<div class="chat">
  <div class="msg me"><div class="bub">Hey Claude, which drying time do I set?</div><div class="av">🏭</div></div>
  <div class="msg me fragment"><div class="bub">Only look at the data. No hallucinations.</div><div class="av">🏭</div></div>
  <div class="msg ai fragment"><div class="av">✳</div><div class="bub">
    <p>Looking only at the data: <b>short drying</b>. More good parts, and it saves two hours and energy on every batch.</p>
    <div class="mini2">
      <div class="cell"><span class="p colA" data-count="79" data-suf="%">79%</span><span class="f"><b class="colA">Long drying</b> · 4 h · 395 / 500 good</span><div class="bar a"><i style="--w:79%"></i></div></div>
      <div class="cell win"><span class="p colB" data-count="85" data-suf="%">85%</span><span class="f"><b class="colB">Short drying</b> · 2 h · 425 / 500 good</span><div class="bar b"><i style="--w:85%"></i></div></div>
    </div>
    <p class="tiny muted" style="margin:.5em 0 0 0">Illustrative numbers.</p></div></div>
  <div class="msg me fragment"><div class="bub">Are you sure?</div><div class="av">🏭</div></div>
  <div class="msg ai fragment"><div class="av">✳</div><div class="bub">Yes.</div></div>
  <div class="msg me fragment"><div class="bub">Gemini would have done a better job.</div><div class="av">🏭</div></div>
  <div class="msg ai fragment"><div class="av">✳</div><div class="bub">
    <p>…fine. Same parts, split by how the granulate arrived:</p>
    <div class="simp mini">
      <div></div><div class="hd colA">Long drying · 4 h</div><div class="hd colB">Short drying · 2 h</div>
      <div class="rl"><span>Arrived dry</span></div>
      """ + _cell(95, "95 / 100", "a", " win") + _cell(90, "360 / 400", "b") + """
      <div class="rl"><span>Arrived humid</span></div>
      """ + _cell(75, "300 / 400", "a", " win") + _cell(65, "65 / 100", "b") + """
      <div class="rl"><span>All parts</span></div>
      """ + _cell(79, "395 / 500", "a", " tot", False) + _cell(85, "425 / 500", "b", " tot win", False) + """
    </div></div></div>
</div>
</div></div>
</section>
"""

CONFOUNDER = """
<section class="s">
""" + head(K1, "Nothing is wrong with the data. The question is wrong.") + """
<div class="sbody"><div class="fit">
<div class="cols" style="align-items:center">
  <div class="col" style="flex:.85">
    """ + dag(440, 300, {"z": (220, 50, "Granulate moisture", "hot", 230), "t": (95, 240, "Drying time", "", 160), "y": (345, 240, "Good part", "", 140)},
              [("z", "t", "hot"), ("z", "y", "hot"), ("t", "y")]) + """
    <p class="center small muted" style="margin-top:10px">Moisture drives both the choice of the drying time and the quality: a <b style="color:var(--accent)">confounder</b>.</p>
  </div>
  <div class="col">
    <p><b>Which parts got the long drying?</b> <span class="muted small">(the expensive one)</span></p>
    <div class="mix"><span class="sm" style="--w:20%">100 dry</span><span class="lg" style="--w:80%">400 from humid granulate</span></div>
    <p><b>Which parts got the short drying?</b></p>
    <div class="mix"><span class="sm" style="--w:80%">400 from dry granulate</span><span class="lg" style="--w:20%">100 humid</span></div>
    <p class="small">Operators dry for longer when the material arrives humid. The short drying mostly got the easy batches.</p>
  </div>
</div>
<div class="two-q fragment" style="margin-top:14px">
  <div class="card t-blue"><span class="tag blue">Seeing · a monitoring twin</span><p style="margin:.5em 0 0 0">Among the parts dried for 2 hours, how many were good?</p><div class="f"><span class="math inline">P(Y \\mid T)</span></div></div>
  <div class="card t-red"><span class="tag red">Doing · a twin that recommends settings</span><p style="margin:.5em 0 0 0">If I set 2 hours for this batch, will the parts be good?</p><div class="f"><span class="math inline">P(Y \\mid do(T))</span></div></div>
</div>
<p class="center fragment" style="margin-top:14px;font-weight:650">A twin that learns from these logs recommends 2 hours, also for the humid batches. Which table to trust is decided by the <span class="alert">causal graph</span>, not by the data.</p>
<p class="center tiny muted" style="margin-top:6px">Illustrative numbers. The medical original: kidney stones, Charig et al., BMJ, 1986 (Simpson’s paradox).</p>
</div></div>
</section>
"""

# ---------------------------------------------------------------- the same trap in security logs (illustrative)
SECURITY = """
<section class="s">
""" + head(K1, "The same trap, in security logs") + """
<div class="sbody"><div class="fit">
<div class="cols" style="align-items:center">
  <div class="col" style="flex:.85">
    """ + dag(440, 300, {"z": (220, 50, "Exposure of the machine", "hot", 270), "t": (95, 240, "Agent installed", "", 180), "y": (345, 240, "Incidents", "", 140)},
              [("z", "t", "hot"), ("z", "y", "hot"), ("t", "y")]) + """
    <p class="center small muted" style="margin-top:10px">The agent goes first on the exposed machines: exposure is the <b style="color:var(--accent)">confounder</b>.</p>
  </div>
  <div class="col">
    <p><b>The logs say:</b> machines with the security agent report <span class="alert">more</span> incidents than machines without it.</p>
    <div class="two-q" style="margin-top:6px">
      <div class="card t-blue"><span class="tag blue">Seeing</span><p class="small" style="margin:.5em 0 0 0">Among the machines with the agent, how many incidents?</p></div>
      <div class="card t-red"><span class="tag red">Doing</span><p class="small" style="margin:.5em 0 0 0">If I install the agent on this machine, will it have fewer incidents?</p></div>
    </div>
  </div>
</div>
<div class="banner fragment"><b>And root cause.</b> One wrong firewall rule, three hundred alerts in an hour: all correlated, <em>one cause</em>.</div>
<p class="center tiny muted" style="margin-top:6px">Illustrative example.</p>
</div></div>
</section>
"""

# ---------------------------------------------------------------- ladder of causation, for a twin
DT_LADDER = """
<section class="s">
""" + head(K1, "Three kinds of twin: the ladder of causation") + """
<div class="sbody"><div class="fit">
""" + _rung(3, "💭", "Root-cause twin", "imagining", "What if I had done otherwise?", "This part was scrapped. Would it have been good with another setting?", "P(y_x \\mid x', y')", 1, 220) \
    + _rung(2, "✋", "What-if twin", "doing", "What if I change it?", "Raise the mold temperature by 5 °C: what happens to scrap?", "P(y \\mid do(x))", 0, 110) \
    + _rung(1, "👁️", "Monitoring twin", "seeing", "What will I see next?", "Predict the quality of the next part from the sensors.", "P(y \\mid x)", None, 0) + """
<p class="fragment" data-fragment-index="2" style="margin-top:16px">Most data-driven twins live on the first rung. To climb, data are not enough: we need <span class="alert">a causal graph</span>. From physics when we have it, from the data when we do not.</p>
<p class="tiny muted">Ladder of causation: Pearl and Mackenzie, <i>The Book of Why</i>, 2018.</p>
</div></div>
</section>
"""

# ---------------------------------------------------------------- the catch, with the DoE
CATCH = custom.CATCH.replace(
    '<div class="ico">🎲</div><h3>Randomizing</h3><p style="margin:0">Often impossible or unethical: we cannot assign smoking, interest rates or CO<sub>2</sub> levels.</p>',
    '<div class="ico">🎲</div><h3>Experimenting</h3><p style="margin:0">A designed experiment (DoE) is the randomized trial of the factory. It answers the question, but it stops the line. Nobody randomizes a power grid.</p>') \
    .replace("The catch: adjust for what?", "Two ways out, and a catch") \
    .replace(">Disease 1<", ">Defect 1<").replace(">Disease 2<", ">Defect 2<").replace("🏥 In hospital", "🔍 Rejected") \
    .replace("Two unrelated diseases both send people to hospital. Look only at hospital patients, and the diseases become correlated.",
             "Two unrelated defects both get a part rejected at inspection. Look only at the rejected parts, and the defects become correlated.")
assert "DoE" in CATCH and "Two ways out" in CATCH and "Defect 2" in CATCH and "Rejected" in CATCH and "hospital" not in CATCH

# ---------------------------------------------------------------- injection molding
DIV_IM = divider("Part 2 · results", "Does it help a real twin?", "Plastic injection molding, on data collected at Sirris. Then what we are building now.")


def _prow(pid, n, mat, mold, note, cls=""):
    return f'<tr class="{cls}"><td><b>{pid}</b></td><td>{n}</td><td>{mat}</td><td>{mold}</td><td class="muted">{note}</td></tr>'


IM_SETUP = """
<section class="s">
""" + head(KIM, "A twin that has to survive a change of production") + """
<div class="sbody"><div class="fit">
<div class="cols" style="align-items:center">
  <div class="col" style="flex:.42">
    <div class="molds"><figure><img src="img/mold_plate.jpg"><figcaption>Test plate</figcaption></figure><figure><img src="img/mold_isoa.jpg"><figcaption>Tensile bar ISO A</figcaption></figure></div>
  </div>
  <div class="col">
    <table class="prod">
      <thead><tr><th>Run</th><th>Parts</th><th>Material</th><th>Mold</th><th>What changes</th></tr></thead>
      <tbody>
      """ + _prow(65, 497, "ABS GP22", "plate", "reference") + _prow(87, 437, "ABS GP22", "plate", "drying intervals") \
          + _prow(88, 498, "ABS GP35", "plate", "material grade") + _prow(89, 510, "PC/ABS T65XF", "plate", "polymer") \
          + _prow(97, 340, "ABS GP22", "ISO A bar", "mold") + """
      </tbody>
    </table>
    <p class="small" style="margin:0"><b>17 process variables</b> per part: heating zones, pressures, times, cushion, ambient conditions.<br><b>Target:</b> a binary quality label, derived from the drying of the material.</p>
  </div>
</div>
<div class="banner fragment"><b>The test.</b> Train on four productions, predict the fifth. A new material or a new mold moves every sensor: <em>domain shift</em>.</div>
<p class="src">Paldino, Caelen, Oueslati, Ansay, Johanesa, Bontempi. <i>PerCom Workshops</i>, 2025, and <i>Future Generation Computer Systems</i>, 2026. Written during my PhD, within ARIAC by DigitalWallonia4.ai. Parts counted after cleaning.</p>
</div></div>
</section>
"""

_VENN = """
<svg class="venn" viewBox="0 0 640 400" width="640" height="400">
<circle class="ve" cx="235" cy="220" r="178"/><circle class="vc" cx="405" cy="220" r="178"/>
<text class="vt" x="150" y="18" style="fill:var(--blue)">Domain expert · 7</text>
<text class="vt" x="490" y="18" style="fill:var(--accent)">Causal discovery · 9</text>
<text x="142" y="192">Integral value</text><text x="142" y="220">Cycle time</text><text x="142" y="248">Dosing time</text>
<text class="vb" x="320" y="140">Both · 4</text>
<text x="320" y="178">Material cushion</text><text x="320" y="206">Max inj. pressure</text><text x="320" y="234">Switch-over press.</text><text x="320" y="262">Mold safety time</text>
<text x="498" y="164">Heating zone 2</text><text x="498" y="192">Heating zone 3</text><text x="498" y="220">Heating zone 4</text><text x="498" y="248">Heating zone 5</text><text x="498" y="276">Injection speed</text>
</svg>"""

IM_FEATURES = """
<section class="s">
""" + head(KIM, "Which sensors should the twin trust?") + """
<div class="sbody"><div class="fit">
<div class="cols" style="align-items:center">
  <div class="col" style="flex:.8">
    <div class="card t-red" style="padding:16px 22px"><span class="tag red">Causal feature selection</span>
      <ol class="small" style="margin:.6em 0 0 1.1em">
        <li>Run PCMCI on <b>each production</b> separately, with delays up to 20 parts.</li>
        <li>Keep a variable only if it is a cause of the target in <b>all five</b>.</li>
      </ol>
      <p class="small muted" style="margin:.5em 0 0 0">What holds in every production is a candidate <i>invariant</i> mechanism, the kind that survives a domain shift.</p></div>
    <p class="small" style="margin-top:14px">Compared with <b>all 17</b> variables, and with the <b>7</b> chosen by the process expert.</p>
  </div>
  <div class="col">""" + _VENN + """</div>
</div>
<div class="banner fragment">Without being told, the algorithm found <em>4 of the 7</em> expert variables, and proposed the thermal ones.</div>
</div></div>
</section>
"""


def _f1(name, sub, v, cls):
    return (f'<div class="brow" style="--lw:230px"><span class="bl">{name}<small>{sub}</small></span>'
            f'<div class="sbar {cls}" data-vals="{v}" data-min="0" data-max="0.5"><i></i></div><b class="bv" data-dec="3"></b></div>')


IM_RESULTS = """
<section class="s">
""" + head(KIM, "What we learned") + """
<div class="sbody"><div class="fit">
<div class="cols" style="align-items:center">
  <div class="col" style="flex:.95">
    <div class="card" style="padding:16px 22px">
      <span class="tag">Mean F1 on the unseen production</span>
      <div style="margin-top:10px">
      """ + _f1("Causal", "9 variables", 0.396, "") + _f1("All", "17 variables", 0.394, "g") + _f1("Domain expert", "7 variables", 0.387, "g") + """
      </div>
      <p class="tiny muted" style="margin:.6em 0 0 0">Averages over nearly 100,000 training runs: 2 models, 14 adaptation settings, 5 held-out productions.</p>
    </div>
  </div>
  <div class="col">
    <div class="lessons">
      <div class="fragment fade-up"><b>Half of the sensors, the same accuracy.</b> Chosen from the data, with no expert in the loop, and close to what the expert would choose.</div>
      <div class="fragment fade-up"><b>Naive adaptation hurts.</b> Rescaling each past production on its own is always worse than doing nothing. The best method (0.431) only matches no adaptation (0.430).</div>
      <div class="fragment fade-up"><b>The graph is only as good as the algorithm.</b> PCMCI gives robust delayed dependencies, not proven physics. It is slow, and every test is a yes/no decision.</div>
    </div>
  </div>
</div>
<p class="center fragment" style="margin-top:14px;font-weight:650">A hard task and small differences: the twin is limited by <span class="alert">how well we can find the graph</span>.</p>
</div></div>
</section>
"""

IM_ADAPT = """
<section class="s">
""" + head("Backup", "Injection molding: domain adaptation in detail") + """
<div class="sbody"><div class="fit">
<div class="cols" style="align-items:center">
  <div class="col" style="flex:1.6"><img src="img/fgcs_scaling.png"></div>
  <div class="col">
    <p class="small"><b>Grouped</b> = each past production rescaled on its own. Always below no adaptation.</p>
    <p class="small"><b>Non-grouped</b> = the past productions rescaled as one. It catches up as more parts of the new production are seen (10, 50, 100).</p>
    <p class="small">Best single configuration: dynamic trend scaling with the expert variables, F1 0.459.</p>
    <p class="small muted" style="margin:0">Friedman test over the 14 configurations: significant. Best adaptation vs none: not significant (p = 0.40).</p>
  </div>
</div>
</div></div>
</section>
"""

# ---------------------------------------------------------------- pretrained causal discovery in one slide
PRETRAINED = """
<section class="s">
""" + head(KPT, "A different idea: learn to read causal structure, once") + """
<div class="sbody"><div class="fit">
<div class="pipe">
  <div class="pb"><div class="pi">📈</div><b>Your time series</b><span>any number of sensors</span></div><div class="pa">⟶</div>
  <div class="pb"><div class="pi">🧮</div><b>Dependence statistics</b><span>8 numbers per pair of sensors and delay</span></div><div class="pa">⟶</div>
  <div class="pb hot"><div class="pi">🧠</div><b>Pretrained network</b><span>trained on simulations only</span></div><div class="pa">⟶</div>
  <div class="pb"><div class="pi">🕸️</div><b>Causal graph</b><span>who → whom, after how long, with a probability</span></div>
</div>
<div class="grid3" style="margin-top:22px">
  <div class="card t-teal fragment fade-up" style="padding:16px 20px"><h3>Learn from simulators</h3><p class="small" style="margin:0">About 60,000 simulated systems whose graph is known. The network learns what cause and effect <i>look like</i> in the data, instead of running hundreds of yes/no tests.</p></div>
  <div class="card t-gold fragment fade-up" style="padding:16px 20px"><h3>No retraining</h3><p class="small" style="margin:0">On new data it is a single pass: no tuning, no GPU, an answer in seconds.</p></div>
  <div class="card t-blue fragment fade-up" style="padding:16px 20px"><h3>Any size</h3><p class="small" style="margin:0">The same weights serve 5 sensors or 1000. The other pretrained models stop at 5 to 12 variables.</p></div>
</div>
<p class="src">TD2C: Paldino and Bontempi, <i>International Journal of Forecasting</i>, 2026. &nbsp;DTD2C: ongoing work, under review.</p>
</div></div>
</section>
"""

# ---------------------------------------------------------------- dashboard
DASHBOARD = """
<section class="s top">
""" + head("From paper to tool", "Upload a CSV, get the causal graph") + """
<div class="sbody"><div class="fit">
<div class="cols" style="align-items:center;gap:26px">
  <div class="col" style="flex:0 0 auto"><div class="shot"><img src="img/dash_upload.png"></div></div>
  <div class="col">
    <p class="small"><b>Input.</b> One row per time step, one column per sensor.</p>
    <p class="small"><b>Output.</b> Every link with its delay and a probability. A slider sets how sure the model must be.</p>
    <p class="small"><b>Speed.</b> 10 sensors, 500 steps: a quarter of a second on a CPU.</p>
    <p class="small"><b>Baseline.</b> Granger causality runs next to it.</p>
    <p class="tiny muted" style="margin:0">Prototype running at ULB. The file in the picture is a demo.</p>
  </div>
</div>
<div class="banner fragment">No code, no install, no GPU. <em>Bring a file.</em></div>
</div></div>
</section>
"""

# ---------------------------------------------------------------- where causality sits in the twin
DT_LOOP = """
<section class="s">
""" + head(K0, "Where causality sits in the twin") + """
<div class="sbody"><div class="fit">
<div class="pipe">
  <div class="pb"><div class="pi">📡</div><b>Sensor logs</b><span>what the plant already records</span></div><div class="pa">⟶</div>
  <div class="pb hot"><div class="pi">🕸️</div><b>Causal graph</b><span>discovered from data, corrected by the expert</span></div><div class="pa">⟶</div>
  <div class="pb wide">
    <div class="use"><i class="tag green">done</i><b>Robust models</b><span>features that survive a new production</span></div>
    <div class="use"><i class="tag gold">next</i><b>What-if</b><span>simulate a change of set-point before making it</span></div>
    <div class="use"><i class="tag gold">next</i><b>Root cause</b><span>explain an alarm to the operator</span></div>
  </div>
</div>
<div class="card t-red fragment" style="margin-top:22px;padding:16px 24px"><span class="tag red">What a university lab is always looking for: data with a ground truth</span>
  <div class="grid3" style="gap:8px 30px;margin-top:10px">
    <p class="small" style="margin:0"><b>Known interventions.</b> Designed experiments (DoE), logged changes of set-point: we check the graph against what you changed on purpose.</p>
    <p class="small" style="margin:0"><b>Tagged events.</b> Faults, alarms or attacks labelled with their root cause, by an operator or an analyst.</p>
    <p class="small" style="margin:0"><b>A known structure.</b> A process diagram or a network topology, on systems with hundreds of sensors.</p>
  </div>
  <p class="small" style="margin:10px 0 0 0"><b>What we bring:</b> the methods, the tool, the computing, and joint papers and projects, as we did in ARIAC.</p>
</div>
</div></div>
</section>
"""

TAKEHOME = """
<section class="s">
""" + head("Wrap-up", "Take-home messages") + """
<div class="sbody"><div class="fit">
<div class="take">
  <div class="fragment fade-up"><span><b>Seeing is not doing.</b> A twin that only predicts tells you what happens if nothing changes. A twin that acts needs the causal graph.</span></div>
  <div class="fragment fade-up"><span><b>The graph can be learned from logged data.</b> By conditioning, one test at a time. It works under assumptions, and tests fail.</span></div>
  <div class="fragment fade-up"><span><b>Injection molding:</b> causal selection recovers most of the expert's choice and keeps the accuracy with half of the sensors. Naive adaptation hurts.</span></div>
  <div class="fragment fade-up"><span><b>Pretrained discovery:</b> any number of sensors, in seconds. Strong on simulated systems, not yet ahead on real ones: we look for real datasets with a ground truth.</span></div>
</div>
</div></div>
</section>
"""

THANKS = """
<section class="hero" """ + GRAD + """ data-transition="zoom">
<div class="wrap" style="align-items:center;text-align:center">
  <h1 style="max-width:none">Thank you.</h1>
  <div class="sub" style="margin-bottom:0">Questions, and data, are welcome.</div>
  <div class="meta" style="margin-top:28px">Gian Marco Paldino · Machine Learning Group, Université Libre de Bruxelles</div>
</div>
</section>
"""

DIV_BACKUP = divider("Backup", "More, if you ask", "Slides kept for the discussion.")

REFS = """
<section class="s">
""" + head("Backup", "References and credits") + """
<div class="sbody"><div class="fit">
<ul class="small">
<li>Paldino, Caelen, Oueslati, Ansay, Andrianandrianina Johanesa, Bontempi. Integrating domain adaptation and causal discovery in digital twins for plastic injection molding. <i>IEEE PerCom Workshops</i>, 2025.</li>
<li>Paldino, Caelen, Oueslati, Ansay, Johanesa, Bontempi. On the integration of domain adaptation and causal discovery in digital twins: a case study for plastic injection molding. <i>Future Generation Computer Systems</i>, 2026.</li>
<li>Oueslati, with Caelen, Dagnely, Andrianandrianina Johanesa, Ansay and Paldino. A follow-up study on the drying data. Submitted, 2026.</li>
<li>Paldino, Bontempi. Causal discovery in multivariate time series through mutual information featurization. <i>International Journal of Forecasting</i>, 2026.</li>
<li>Paldino, Bontempi. DTD2C: ongoing work, under review.</li>
<li>Runge et al. Detecting and quantifying causal associations in large nonlinear time series datasets (PCMCI). <i>Science Advances</i>, 2019.</li>
<li>Charig et al. Comparison of treatment of renal calculi. <i>BMJ</i>, 1986.</li>
<li>Pearl, Mackenzie. <i>The Book of Why</i>. 2018.</li>
</ul>
<p class="tiny muted">The injection molding work was supported by Service Public de Wallonie Recherche, grant 2010235, ARIAC by DigitalWallonia4.ai. EDITS is funded by the F.R.S.-FNRS WEL-T programme.</p>
<p class="tiny muted">Photos. Medicine bottle: Yinan Chen, public domain. Lawn sprinkler: Pixel.la, CC0 (all via Wikimedia Commons). Molded parts: from the FGCS paper, produced at Sirris.</p>
</div></div>
</section>
"""
