# POF Design System — `benoitpof/design-system`

**Version:** 3.3.4 | **Updated:** 2026-04-26
**Slide format:** LAYOUT_WIDE 20 × 11.25" (508 × 285.75 mm), 16:9
**Coordinates:** mm primary (SSOT). Inches in comments for pptxgenjs.

Source of truth for all Plastic Odyssey Factories brand assets, design tokens, and layout specifications. Cross-medium consistent (web / PowerPoint / print).

---

## How to use this repo

Before generating any asset (slide, page, report, chart, map, icon usage, photo selection), read these files in this order:

1. `docs/DESIGN.md` — brand DNA, hard locks (type-scale, weight, gradient, corner marks)
2. `tokens/brand-tokens.json` — colors, typography, spacing, components, entity overrides
3. `tokens/brand-rules-per-format.json` — slides, docs, web, excel, linkedin, charts, maps, icons rules
4. `docs/LAYOUTS.md` — 15 canonical slide layouts L01–L15
5. `docs/CONTENT-RULES.md` — narrative content rules + RAW vs FINAL confirmation step

Specialized references on demand:

- `docs/ASSETS.md` — asset index + Notion Media Assets DB schema and query protocol
- `docs/ICONS.md` — POF curated icons (ecology, environment) + Tabler CDN fallback + brand pictos
- `docs/MAPS.md` — 5 map patterns (heatmap, categorical, neutral dots, data dots, anchored faded) + region overlays
- `docs/CHARTS.md` — 16 chart templates catalog (bar, line, donut, funnel, gantt, sankey, tables, etc.)
- `assets/maps/map-charter.html` — interactive visual charter for map patterns
- `examples/charts/` — 16 ready-to-use chart templates HTML+CSS

---

## Repo structure

```
/tokens/
  brand-tokens.json              ← colors, typography, components (SSOT)
  brand-tokens.css               ← CSS custom properties version
  brand-rules-per-format.json    ← format rules: slides, docs, web, charts, maps, etc.

/assets/
  /logos/                        ← 5 SVG (color, white, navy-bg, variant-1, variant-2)
  /pictos/                       ← 2 SVG brand mark (color, white) — NOT a UI icon
  /icons/
    /ecology/                    ← 8 themes × 4 variants = 32 SVG
    /environment/                ← 46 themes × 3 variants = 138 SVG
  /brand-elements/               ← waves + 4 corner brackets (TL/TR/BL/BR + canonical alias)
  /backgrounds/                  ← 2 SVG full-bleed
  /maps/                         ← world map base + 7 regional crops + interactive charter

/docs/
  DESIGN.md                      ← brand DNA + hard locks v3.2.6
  LAYOUTS.md                     ← 15 canonical slide layouts
  CONTENT-RULES.md               ← narrative rules + RAW vs FINAL mode
  ASSETS.md                      ← asset index + Notion DB schema
  ICONS.md                       ← icon system (3 sources)
  MAPS.md                        ← map system (5 patterns)
  CHARTS.md                      ← chart catalog (16 templates)

/examples/
  /charts/                       ← 16 chart HTML+CSS templates ready to use
```

---

## Cross-medium philosophy

Every asset must render consistently across web (HTML/CSS), PowerPoint (PPTX), and print (PDF). To ensure this:
- Solid fills only on data series (no CSS gradients on bars, country fills, etc.)
- Web fonts Poppins + Raleway with `sans-serif` fallback
- No `backdrop-filter`, no `mix-blend-mode`, no `mask-image`
- Single canonical photo overlay gradient (no other gradients allowed)
- Pre-rasterize SVG to PNG at 2× when alpha channel is used in PPTX export

Detailed cross-medium constraints in each lock block of `tokens/brand-rules-per-format.json` (`charts_lock.cross_medium_constraints`, `maps_lock.cross_medium_constraints`).

---

## Entity scope

POF Factories only (v3.3.3). Academy and Sunu PO removed from the design system per scope decision.

---

## Photos / dynamic media

Stored in Notion (not in this repo). Database: `collection://8ca51a75-2413-4f72-8f2a-c44d445fa1d0`. Schema and query protocol in `docs/ASSETS.md` section 2.

This repo is the **index and protocol** for photos. Notion is the **source**.

---

## Hard locks (v3.2.6 — STRICT)

Summarized here, full details in `docs/DESIGN.md` and `tokens/brand-rules-per-format.json`:

- Sizes (pt) ONLY in `[9, 11, 14, 18, 22, 26, 36]` + stat-only `[72, 120]`
- Weights ONLY in `[300, 400, 600, 700]`. ExtraBold (800) restricted. Black (900) forbidden.
- Photo overlay ONLY: `linear-gradient(135deg, rgba(28,31,59,0.85) 0%, rgba(28,31,59,0.45) 100%)`
- Corner marks: L-brackets only. NO shadow, NO drop-shadow, NO blur, NO opacity reduction.
- Canonical colors only. No `#1A2B4A`, `#1D1E3A`, `#75DBCD`, `#80C8C3`, `#FF5A60`.
- Charts: max 1 legend per chart, no gridlines, no chart borders, no 3D.
- Maps: anchored to slide edge required. 5 canonical patterns. Region overlays from canonical list only.
