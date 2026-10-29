#!/usr/bin/env python3
"""Draws the JM Electrical Solutions logo as pure vector SVG (text converted to outlines,
so it looks identical everywhere). Run: python3 logo.py  ->  ../jm-electrical-logo/"""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "jm-electrical-logo")
FONT = "/usr/share/fonts/opentype/inter/Inter-BlackItalic.otf"
NAVY, BLUE, AMBER, WHITE = "#0f2a44", "#1f6fd1", "#f2a900", "#ffffff"

# Monogram drawn on a 0-100 cap height grid (y down), then slanted like the van lettering.
# As on the van: the J's stem is the M's first leg, one bar runs across the top,
# and the M's middle stroke IS the lightning bolt, dropping below the baseline.
# All subpaths run clockwise so they merge into one solid shape.
MARK = ("M0 60H16V82H24V0H140V100H122V18H91L88 58H106L72 142L78 84H63L73 18H42V100H0Z")

def text_path(s, size, tracking=0.0):
    f = TTFont(FONT); gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f["head"].unitsPerEm
    sc = size / upm; x = 0; pen = SVGPathPen(gs, ntos=lambda v: ("%.1f" % v).rstrip("0").rstrip("."))
    for ch in s:
        g = cmap.get(ord(ch))
        if g is None: x += size * .3; continue
        gs[g].draw(TransformPen(pen, (sc, 0, 0, -sc, x, 0)))
        x += gs[g].width * sc + tracking * size
    return pen.getCommands(), x - tracking * size

def mark(fill, *_):
    return f'<g transform="skewX(-12)"><path d="{MARK}" fill="{fill}"/></g>'

def grad():
    return f'<defs><linearGradient id="jmg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{BLUE}"/><stop offset=".75" stop-color="{NAVY}"/></linearGradient></defs>'

def svg(w, h, body, bg=None, title="JM Electrical Solutions"):
    rect = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}"><title>{title}</title>{rect}{body}</svg>\n'

def horizontal(letters, bolt, words, bg=None, knock=WHITE):
    l1, w1 = text_path("ELECTRICAL", 46, .04)
    l2, w2 = text_path("SOLUTIONS", 46, .04)
    tw = max(w1, w2)
    pad = 20; mx = 40  # monogram offset (skew pushes bottom left)
    body = grad() + f'<g transform="translate({mx},{pad})">{mark(letters, bolt, knock)}</g>'
    body += f'<g fill="{words}"><path transform="translate(190,{pad+44})" d="{l1}"/><path transform="translate(190,{pad+100})" d="{l2}"/></g>'
    body += f'<rect x="190" y="{pad+58}" width="{tw:.0f}" height="5" fill="{bolt}"/>'
    return svg(int(190 + tw + pad), 186, body, bg)

def sign(pad=10):
    # Matches the lit building sign: everything in bright blue with a soft glow, no amber underline
    l1, w1 = text_path("ELECTRICAL", 46, .04)
    l2, w2 = text_path("SOLUTIONS", 46, .04)
    tw = max(w1, w2)
    defs = (f'<defs><linearGradient id="jms" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3d8bff"/><stop offset="1" stop-color="#1450b8"/></linearGradient>'
            f'<filter id="glow" x="-10%" y="-10%" width="120%" height="130%"><feGaussianBlur stdDeviation="2.5" result="b"/><feFlood flood-color="#3d8bff" flood-opacity=".55"/><feComposite in2="b" operator="in"/><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>')
    body = defs + f'<g filter="url(#glow)"><g transform="translate(40,{pad})">{mark("url(#jms)")}</g>'
    body += f'<g fill="url(#jms)"><path transform="translate(186,{pad+50})" d="{l1}"/><path transform="translate(186,{pad+104})" d="{l2}"/></g></g>'
    return svg(int(186 + tw + 14), 166, body)

# Traced from Tim's close-up photo of the van door decal: chunky J with a low hooked foot,
# thick top bar, wide bolt shoulder under the M, slit beside the right leg. Already slanted.
VAN_MARK = "M44.8 6.1 L143.6 0 L144.6 74.8 L115.5 78.8 L121.5 19.5 L104 20.5 L103 58 L110 59.5 L104.5 84.1 L78.4 142 L86.2 86.6 L71.9 85 L77.4 80.9 L83.5 24.5 L66.5 24.5 L59 82.9 L54.4 89.6 L5.1 93.7 L0 85 L4.1 63.2 L26.5 62.1 L28.5 71.3 L38.7 70.3Z"

def van(pad=12, depth=3.5):
    # Matches the van decal: blue fading dark-to-light top to bottom, with a dark navy 3D edge
    # dropping down and to the left. No amber underline.
    l1, w1 = text_path("ELECTRICAL", 46, .04)
    l2, w2 = text_path("SOLUTIONS", 46, .04)
    tw = max(w1, w2)
    defs = ('<defs><linearGradient id="jmv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1c3d9c"/>'
            '<stop offset=".55" stop-color="#2a6fd6"/><stop offset="1" stop-color="#5ab4f0"/></linearGradient>'
            '<linearGradient id="jmt" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1c3d9c"/><stop offset="1" stop-color="#2f7fe0"/></linearGradient>'
            f'<path id="jmm" d="{VAN_MARK}"/>'
            f'<path id="jl1" d="{l1}"/><path id="jl2" d="{l2}"/></defs>')
    edge = "#0a1a40"
    mx, my = depth + 4, pad
    body = defs + f'<g transform="translate({mx},{my})">'
    body += "".join(f'<use href="#jmm" x="{-i}" y="{i}" fill="{edge}" stroke="{edge}" stroke-width="2.5" stroke-linejoin="round"/>' for i in [k / 2 for k in range(int(depth * 2), 0, -1)])
    body += '<use href="#jmm" fill="url(#jmv)" stroke="url(#jmv)" stroke-width="2.5" stroke-linejoin="round"/></g>'
    tx = mx + 145 + 20
    for ref, ty in (("jl1", pad + 50), ("jl2", pad + 104)):
        body += f'<g transform="translate({tx},{ty})">'
        body += "".join(f'<use href="#{ref}" x="{-i}" y="{i}" fill="{edge}"/>' for i in (3, 2.5, 2, 1.5, 1, .5))
        body += f'<use href="#{ref}" fill="url(#jmt)"/></g>'
    return svg(int(tx + tw + 12), pad + 104 + 44 + depth, body)

def stacked(letters, bolt, words, bg=None, knock=WHITE):
    l1, w1 = text_path("ELECTRICAL", 34, .04)
    l2, w2 = text_path("SOLUTIONS", 34, .04)
    W = int(max(w1, w2) + 60)
    body = grad() + f'<g transform="translate({(W-130)/2+14:.0f},20)">{mark(letters, bolt, knock)}</g>'
    body += f'<g fill="{words}"><path transform="translate({(W-w1)/2:.0f},210)" d="{l1}"/><path transform="translate({(W-w2)/2:.0f},252)" d="{l2}"/></g>'
    return svg(W, 276, body, bg)

def icon(letters, bolt, bg, rounded=True):
    r = 36 if rounded else 0
    body = grad() + f'<rect width="200" height="200" rx="{r}" fill="{bg}"/><g transform="translate(42,34) scale(.92)">{mark(letters, bolt, bg)}</g>'
    return svg(200, 200, body)

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    files = {
      "jm-logo-horizontal.svg": horizontal("url(#jmg)", AMBER, NAVY),
      "jm-logo-horizontal-white.svg": horizontal(WHITE, AMBER, WHITE, bg=NAVY, knock=NAVY),
      "jm-logo-stacked.svg": stacked("url(#jmg)", AMBER, NAVY),
      "jm-logo-stacked-white.svg": stacked(WHITE, AMBER, WHITE, bg=NAVY, knock=NAVY),
      "jm-logo-mono-black.svg": horizontal("#111", "#111", "#111"),
      "jm-icon.svg": icon(WHITE, AMBER, NAVY),
      "jm-logo-sign.svg": sign(),
      "jm-logo-van.svg": van(),
    }
    for n, s in files.items():
        open(os.path.join(OUT, n), "w").write(s)
    print("wrote", list(files))
