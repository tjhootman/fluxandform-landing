#!/usr/bin/env python3
"""Outline the FLUX & FORM wordmark from Inter into vector SVG paths.

The site's header stays live system-sans text; this produces a *distributable*
wordmark asset (letterhead, etc.) traced from Inter (OFL), which sits close to SF.

Needs Inter woff2 (letters 600, ampersand 300). Get them via @fontsource/inter:
  npm pack @fontsource/inter && tar -xzf fontsource-inter-*.tgz
  cp package/files/inter-latin-600-normal.woff2  <FONT_DIR>/inter-600.woff2
  cp package/files/inter-latin-300-normal.woff2  <FONT_DIR>/inter-300.woff2

Usage:  python3 scripts/build-wordmark.py <FONT_DIR> <OUT_DIR>
Writes wordmark.svg + wordmark-knockout.svg into OUT_DIR and prints geometry.
"""
import sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform

INK, PAPER = "#201e1a", "#f3efe6"
TEXT = "FLUX & FORM"
TRACKING_EM = 0.16          # header letter-spacing
AMP_CHAR = "&"
TARGET_CAP = 100.0          # cap height in output units
PAD = 6.0

font_dir = sys.argv[1] if len(sys.argv) > 1 else "public/wmfonts"
out_dir = sys.argv[2] if len(sys.argv) > 2 else "brand"

f600 = TTFont(f"{font_dir}/inter-600.woff2")
f300 = TTFont(f"{font_dir}/inter-300.woff2")

upem = f600["head"].unitsPerEm
cap = getattr(f600["OS/2"], "sCapHeight", 0) or f600["hmtx"]["H"][0]  # fallback
scale = TARGET_CAP / cap
tracking = TRACKING_EM * upem * scale
baseline = TARGET_CAP


def ctx(font):
    return font.getBestCmap(), font.getGlyphSet(), font["hmtx"]


c600 = ctx(f600)
c300 = ctx(f300)

commands = []
bounds = None
penx = 0.0
for ch in TEXT:
    cmap, gs, hmtx = c300 if ch == AMP_CHAR else c600
    gname = cmap[ord(ch)]
    t = Transform(scale, 0, 0, -scale, penx, baseline)
    if ch != " ":
        sp = SVGPathPen(gs, ntos=lambda v: str(round(v, 2)))
        gs[gname].draw(TransformPen(sp, t))
        d = sp.getCommands()
        if d.strip():
            commands.append(d)
        bp = BoundsPen(gs)
        gs[gname].draw(TransformPen(bp, t))
        if bp.bounds:
            x0, y0, x1, y1 = bp.bounds
            bounds = [x0, y0, x1, y1] if bounds is None else [
                min(bounds[0], x0), min(bounds[1], y0),
                max(bounds[2], x1), max(bounds[3], y1)]
    penx += hmtx[gname][0] * scale + tracking

bx0, by0, bx1, by1 = bounds        # wordmark path bounds (cap height = TARGET_CAP)
ww = bx1 - bx0
path_d = " ".join(commands)


def r(v):
    return round(v, 2)


# Geometric F mark (native 32x32 units); returns (rect markup, width, height).
FRECTS = [(11, 7, 4.2, 18), (11, 7, 11, 4.2), (11, 14.3, 8.2, 3.8)]


def fmark(s, ox, oy):
    out = "".join(
        f'<rect x="{r((rx-11)*s+ox)}" y="{r((ry-7)*s+oy)}" '
        f'width="{r(rw*s)}" height="{r(rh*s)}"/>'
        for rx, ry, rw, rh in FRECTS)
    return out, 11 * s, 18 * s


def svg_doc(vb, body, fill):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="{r(vb[0])} {r(vb[1])} {r(vb[2])} {r(vb[3])}" '
            f'role="img" aria-label="Flux and Form">\n'
            f'  <g fill="{fill}">{body}</g>\n</svg>\n')


def writepair(name, vb, body):
    for fill, suffix in ((INK, ""), (PAPER, "-knockout")):
        with open(f"{out_dir}/{name}{suffix}.svg", "w") as fh:
            fh.write(svg_doc(vb, body, fill))
        print(f"  {out_dir}/{name}{suffix}.svg")


# 1 · wordmark alone
writepair("wordmark",
          (bx0 - PAD, by0 - PAD, ww + 2 * PAD, (by1 - by0) + 2 * PAD),
          f'<path d="{path_d}"/>')

# 2 · horizontal lockup — F mark | hairline rule | wordmark (shared baseline).
# The divider stops the mark's F reading as part of "FLUX".
s_h = TARGET_CAP / 18
gap_h = 0.40 * TARGET_CAP
rule_w = 3.0
fm, fw, fh = fmark(s_h, 0, 0)
rule_x = fw + gap_h
rule = f'<rect x="{r(rule_x)}" y="0" width="{rule_w}" height="{TARGET_CAP}"/>'
dx = (rule_x + rule_w + gap_h) - bx0
miny, maxy, maxx = min(0, by0), max(fh, by1), dx + bx1
writepair("lockup-horizontal",
          (-PAD, miny - PAD, maxx + 2 * PAD, (maxy - miny) + 2 * PAD),
          fm + rule + f'<path transform="translate({r(dx)},0)" d="{path_d}"/>')

# 3 · stacked lockup — larger F centred over the wordmark
s_s = 140 / 18
_, fw2, fh2 = fmark(s_s, 0, 0)
ox = (bx0 + ww / 2) - fw2 / 2
fm2, _, _ = fmark(s_s, ox, 0)
dy = fh2 + 0.48 * TARGET_CAP
minx, maxx2, maxy2 = min(ox, bx0), max(ox + fw2, bx1), dy + by1
writepair("lockup-stacked",
          (minx - PAD, -PAD, (maxx2 - minx) + 2 * PAD, maxy2 + 2 * PAD),
          fm2 + f'<path transform="translate(0,{r(dy)})" d="{path_d}"/>')

print(f"wordmark_width_units: {r(ww)}  cap: {TARGET_CAP}")
