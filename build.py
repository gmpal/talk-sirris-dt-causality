#!/usr/bin/env python3
"""Build the Sirris deck (40 minutes) from the knowledge-sharing reveal deck.

    python3 build.py

Slides that already exist are taken as they are from ../talk-causal-discovery-reveal/index.html
(picked by title); the new ones are in slides.py. No pandoc or tectonic needed.
Edit PLAN below to add, drop or reorder slides.
"""
import html, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
KS = os.path.join(HERE, "..", "talk-causal-discovery-reveal")
sys.path.insert(0, KS)
import slides as S  # noqa: E402

src = open(os.path.join(KS, "index.html"), encoding="utf-8").read()
SECTIONS = re.findall(r"<section\b.*?</section>", src, re.S)


def norm(t):
    return html.unescape(t).replace("’", "'").replace("“", '"').replace("”", '"').strip()


def ks(title, rename=None, kicker=None, edits=()):
    """The knowledge-sharing slide whose title starts with `title`."""
    for s in SECTIONS:
        m = re.search(r"<h2>(.*?)</h2>", s, re.S)
        if m and norm(re.sub(r"<[^>]+>", "", m.group(1))).startswith(norm(title)) and 'class="divider"' not in s:
            if rename:
                s = s.replace(m.group(0), f"<h2>{rename}</h2>", 1)
            if kicker:
                s = re.sub(r'<div class="kicker">.*?</div>', f'<div class="kicker">{kicker}</div>', s, count=1)
            for a, b in edits:
                if a not in s:
                    sys.exit(f"edit not applicable on '{title}': {a[:60]}")
                s = s.replace(a, b)
            return s
    sys.exit("no slide titled: " + title)


def ks_class(cls, contains):
    for s in SECTIONS:
        if f'class="{cls}"' in s and contains in s:
            return s
    sys.exit("no section: " + contains)


RES = "Pretrained causal discovery"
BK = "Backup"

# (slide, speaker note). The note opens with the clock time at which the slide should START.
PLAN = [
    (S.TITLE, "0:00. Thank Henrique and Nicolas for the invitation. Then next slide."),
    (S.WHO, "0:30. One minute. MLG, EDITS (WEL-T), me. Name the Sirris co-authors: the room knows them. The injection molding work comes back in the second half."),
    (S.PROJECTS, "0:30. 45 seconds. Three twins we build at MLG: traffic, energy communities, robotic hand. Do not read the cards."),
    (S.DT_WHATIF, "0:30. The definition is Gianluca's. Emulate and anticipate = prediction. Explain and control = the twin has to know what happens when IT changes something. That is the thread of the whole talk."),
    (ks_class("divider", "You are the doctor"), "2:00. Ask the room, wait for an answer. Do not explain anything yet."),
    (ks_class("s top", "Hey Claude, what do I do?"), "2:30. Click through quickly (6 clicks). The point: the same data give two opposite answers. Real data: kidney stones, Charig et al., 1986."),
    (ks("Nothing is wrong with the data"), "4:30. Stone size is the confounder: doctors gave the heavy treatment to the hard cases. Seeing vs doing is the one concept to keep. This is Simpson's paradox."),
    (S.SECURITY, "7:00. 75 seconds. The same structure in your own logs: drying time on the molding line, the security agent on the machines. Both illustrative."),
    (ks("When correlations made the decision"), "8:30. 75 seconds. Three real cases where an accurate prediction led to a wrong decision. Pick two, do not read all three."),
    (S.CATCH, "8:30. DoE = the factory's randomized trial (you ran one for our dataset). Otherwise we adjust, and then we need to know for what: confounder yes, collider no."),
    (ks("Conditioning is also how we find the graph"), "11:00. Four structures, one question asked many times: is X independent of Y given Z?"),
    (ks("Let's discover a graph by hand"), "12:30. Six clicks. In 40 minutes: answer the questions yourself if the room is slow. Must be out by 17:00."),
    (ks("It worked. What did we assume"), "17:00. Four cards, 15 seconds each. SKIP IF LATE."),
    (ks("What changes with time", kicker="Time series"), "18:00. Sensors are time series: the arrow of time helps, the number of lags hurts."),
    (ks("The traditional toolbox, in one slide", rename="The classical toolbox, in one slide", kicker="Time series",
        edits=[(" Let’s look at them one by one.", "")]),
     "19:00. Do not read the table. One sentence: every family bets on one assumption. PCMCI is the one we used with you. SKIP IF LATE."),
    (S.DIV_IM, "20:30. Breathe. Second half: results."),
    (S.IM_SETUP, "21:00. Data collected at Sirris. Five productions = five domains. Train on four, predict the fifth."),
    (S.IM_FEATURES, "22:30. PCMCI on each production, keep what is a cause of the target in all five. It finds 4 of the 7 expert variables on its own, and adds the thermal ones."),
    (S.IM_RESULTS, "24:00. Be honest: the differences are small. The message is: same accuracy with half of the sensors, chosen without an expert, and naive adaptation hurts. Third card is the bridge to the next part."),
    (S.PRETRAINED, "26:30. The weak point above was the discovery algorithm. Our research: replace hundreds of tests with a network trained once on simulated systems."),
    (ks("Result 1: trained up to 40", rename="Trained up to 40 variables, tested up to 1000", kicker=RES),
     "29:00. Left: accuracy stays flat far beyond the training sizes. Right (next click or just say it): 7 s at 200 variables, 2 min at 1000; PCMCI+ does not finish at 160."),
    (S.DASHBOARD, "34:00. The tool exists. Offer: send a CSV, or we run it together."),
    (S.TAKEHOME, "37:00. Four sentences, then the collaboration slide."),
    (S.COLLAB, "38:00. One minute, said plainly. We look for data (a lot), expert knowledge and a ground truth (DoE = design of experiments). Then what we bring and how to start: a first test on one dataset."),
    (S.THANKS, "38:00. Questions."),
    # ------------------------------------------------------------------ backup
    (S.DIV_BACKUP, ""),
    (S.DT_LADDER, ""),
    (S.DT_LOOP, ""),
    (ks("Where it breaks, and why", kicker=BK), ""),
    (ks("A real case: 42 river stations", kicker=BK), ""),
    (ks("Two different problems", edits=[
        ("Kidney stones: we knew stone size was the confounder, and computed the effect of the treatment.",
         "Drying time: we knew that moisture was the confounder, and computed the effect of the drying time."),
        ("Kidney stones: who told us that stone size comes before treatment, and not after?",
         "Drying time: who told us that moisture comes before the choice of the drying time, and not after?")]), ""),
    (ks("How do we break a spurious correlation", kicker=BK), ""),
    (ks("Predicting at a new", kicker=BK), ""),
    (S.IM_ADAPT, ""),
    (ks("The Traditional Toolbox: Approach 1", kicker=BK), ""),
    (ks("The Traditional Toolbox: Approach 2", kicker=BK), ""),
    (ks("The Traditional Toolbox: Approach 3", kicker=BK), ""),
    (ks("The Traditional Toolbox: Approach 4", kicker=BK), ""),
    (ks("Cause and effect do not look the same", kicker=BK), ""),
    (ks("Result 1: Dominating", rename="TD2C: unseen synthetic dynamics", kicker=BK), ""),
    (ks("The descriptor tensor", kicker=BK), ""),
    (ks("What goes in a cell", kicker=BK), ""),
    (ks("The network: variables talk", kicker=BK), ""),
    (ks("Training: a bigger flight simulator", kicker=BK), ""),
    (ks("And it is fast", kicker=BK), ""),
    (ks("Result 2: it needs less", rename="It needs less training data", kicker=BK), ""),
    (ks("Result 3: other simulators", rename="Other simulators and real data, zero-shot", kicker=BK), ""),
    (ks("Does talking help", kicker=BK), ""),
    (S.REFS, ""),
]

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>From Correlation to Intervention: Causal AI for Trustworthy Digital Twins</title>
<link rel="stylesheet" href="vendor/reveal/dist/reset.css">
<link rel="stylesheet" href="vendor/reveal/dist/reveal.css">
<link rel="stylesheet" href="vendor/katex/katex.min.css">
<link rel="stylesheet" href="css/theme.css">
<link rel="stylesheet" href="css/sirris.css">
</head>
<body>
<div class="reveal"><div class="slides">

{{SLIDES}}

</div></div>
<script src="vendor/reveal/dist/reveal.js"></script>
<script src="vendor/reveal/plugin/notes/notes.js"></script>
<script src="vendor/katex/katex.min.js"></script>
<script src="js/deck.js"></script>
</body>
</html>
"""


# Changes made after the notes were timed: seconds by which every clock time AFTER the slide with that title is shifted.
# Added: who is talking (60 s), MLG projects (45 s), the slide with the drying and security examples (75 s), the medical cases (75 s), the collaboration slide (60 s).
# Moved to the backup: the ladder (90 s, came after the security slide), inference vs discovery (60 s), the rivers (90 s), where it breaks (90 s), where causality sits in the twin (90 s).
SHIFT_AFTER = {
    "A machine learning lab that builds digital twins": 60,
    "from the grid to the hand": 45,
    "The same trap, in your logs": 75 - 90,
    "When correlations made the decision": 75,
    "Two ways out, and a catch": -60,
    "When this is on the table, we are interested": 60,
    "Trained up to 40 variables, tested up to 1000": -90 - 90,
    "Upload a CSV, get the causal graph": -90,
}


def clock(note, shift):
    def f(m):
        t = int(m.group(1)) * 60 + int(m.group(2)) + shift
        return f"{t // 60}:{t % 60:02d}"
    return re.sub(r"\b(\d{1,2}):(\d{2})\b", f, note)


def timed(plan):
    shift = 0
    for h, n in plan:
        yield h, clock(n, shift)
        if n:  # backup slides have no note and do not count
            shift += sum(v for k, v in SHIFT_AFTER.items() if k in h)


def with_note(html, note):
    html = html.strip()
    if not note:
        return html
    i = html.rindex("</section>")
    return html[:i] + f'<aside class="notes">{note}</aside>\n' + html[i:]


if __name__ == "__main__":
    out = "\n\n".join(with_note(h, n) for h, n in timed(PLAN))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(TEMPLATE.replace("{{SLIDES}}", out))
    for kind in ("img", "fig", "figures"):
        for f in set(re.findall(rf'(?:src|data-background-image)="{kind}/([^"]+)"', out)):
            if not os.path.exists(os.path.join(HERE, kind, f)):
                sys.exit(f"missing file: {kind}/{f}")
    main = next(i for i, (h, _) in enumerate(PLAN) if h is S.DIV_BACKUP)
    print(f"{out.count('<section')} slides: {main} in the talk, {len(PLAN) - main} backup -> index.html")
