# Flux and Form — brand marks

Single ink on paper. No gradients, shadows, effects, or additional colour. The
mark and the wordmark are built to the same logic: **a connector set lighter than
what it joins** — the slash between the F's, the ampersand between the words.

## Colour

| Role  | Hex       | Notes                          |
|-------|-----------|--------------------------------|
| Ink   | `#201e1a` | the mark, text                 |
| Paper | `#f3efe6` | the background / reverse mark   |

Only ever ink-on-paper or paper-on-ink (knockout). The per-app accent colours on
the site are the apps' — never the studio's.

## The mark

The mark is `F / F` — two boxy F's joined by a lighter slash (Flux / Form; the
slash is from the site's meta line). Its compact form is the single `F`.

**Two F's, on purpose.** The `F/F` primary mark uses the refined boxy `F`. Every
standalone single-`F` slot — favicon, apple-touch, App Store icon, avatar,
`f-mark.svg` — uses the **original geometric `F`** instead: chunkier, so it holds
at 16px, and it's the `F` we chose to keep. They appear in different contexts and
both read as the studio's `F`.

| File | Use |
|------|-----|
| `ff-mark.svg` | Primary mark, ink on light/paper. |
| `ff-mark-knockout.svg` | Reverse (paper), for dark/ink backgrounds. Transparent bg. |
| `f-mark.svg` | Compact single `F`, ink. For square/small slots where `F/F` crowds. |
| `f-mark-knockout.svg` | Reverse compact `F`. |
| `ff-mark-1100.png` | Raster `F/F`, transparent, 1100×600. |
| `app-icon-1024.png` / `app-icon-512.png` | Single `F` on a paper tile, square — App Store icon / social avatar. |

**Which mark where**

- Wide contexts (lockups, avatars with room, letterhead): **`F/F`**.
- Square / tight / ≤ ~24px (favicon, small avatars): **single `F`**.

## Site icons (in `public/`)

- `favicon.svg` — single `F` on a paper tile (vector, primary).
- `favicon.png` — 48×48 raster fallback.
- `apple-touch-icon.png` — 180×180.

Regenerate the PNGs after any SVG change: `node scripts/build-icons.mjs`.

## Wordmark

On the **site**, the wordmark is live type — it renders in the system sans stack
(SF on Apple) from `src/components/Header.astro`, and is never shipped as a
font/outline. Header spec:

- **Family:** `--font-sans` (system stack)
- **Weight:** 600 · **case/tracking:** uppercase, `letter-spacing: 0.16em`
- **Ampersand:** dropped to weight **300** (the one flourish)
- **Size (header):** `0.95rem`

### Distributable wordmark (letterhead, documents, anything off the site)

System sans can't be exported as a logo — it's not one font, and SF specifically
may not be outlined into a mark. So the fixed wordmark asset is traced from
**Inter** (SIL OFL), set the same way (letters 600, ampersand 300, 0.16em) and
converted to outlined paths — no font dependency. Inter sits close to SF, so it
reads like the live header.

| File | Use |
|------|-----|
| `wordmark.svg` (+ `-knockout`) | Wordmark, ink / reverse. |
| `lockup-horizontal.svg` (+ `-knockout`) | `F` mark │ wordmark, one line (hairline divider so the mark's F doesn't read as part of FLUX). |
| `lockup-stacked.svg` (+ `-knockout`) | `F` mark centred over the wordmark. |
| `wordmark-2400.png`, `lockup-horizontal-2400.png`, `lockup-stacked-1400.png` | Transparent PNGs for Word / Pages / email. |

Regenerate the SVGs (needs Inter woff2 — see the header of
`scripts/build-wordmark.py`): `python3 scripts/build-wordmark.py <font_dir> brand`.
Then rebuild the PNGs: `node scripts/build-icons.mjs`.

## Clear space & minimum size

- **Clear space:** keep free space on all sides equal to at least half the mark's
  height. Nothing (type, rules, edges) intrudes.
- **Minimum size:** single `F` reads down to 16px (favicon). Below ~24px tall,
  use the single `F`, not `F/F`.

## Don't

- Don't recolour beyond ink/paper, or add effects, outlines, or shadows.
- Don't make the slash (or ampersand) the same weight as the letters — the
  connector always stays lighter.
- Don't stretch, rotate, or rearrange the F's (a rotated double-F reads as
  another brand's mark).
- Don't place the ink mark on a busy or low-contrast field — use the knockout on
  dark.
