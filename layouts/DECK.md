# DECK.md — POF Deck Layouts (PPTX 16:9 LAYOUT_WIDE)

**Version:** 4.0.0 | **Updated:** 2026-04-28
**Status:** Scaffolding v4.0. To be enriched with detailed slide-by-slide spec after master PPTX brand patch (logo, corner brackets, wave watermark in `slideMaster1.xml`).
**Format:** LAYOUT_WIDE 20"×11.25" (508×285.75 mm), coordinate convention mm.
**Master template:** `templates/master-deck-current.pptx` (SHA in `templates/MASTER_SHA.txt`).
**Médium:** Microsoft PowerPoint .pptx via python-pptx, optionally Google Slides via API.

---

## General frame

- Title font: **Poppins** (ExtraBold 36pt cover, 26pt slide title)
- Body font: **Raleway** Regular 22pt (slide reading distance 3m)
- Caption: Raleway Light 18pt
- Background: white `#FFFFFF` default, navy `#1C1F3B` for section dividers and back cover
- Corner bracket TL teal `#80C7C2` mandatory on every slide (default), pair TL+BR on cover only
- Logo POF: bottom-right at 8% opacity except cover (top-left full size) and back cover (centered monogramme)
- Wave watermark: behind section dividers and back cover, opacity 8%

## Canonical layouts (12 from master template)

| ID | Master layout name | Usage | Charts allowed |
|---|---|---|---|
| L01 | TITLE | Cover slide, full-bleed photo + navy_hard overlay | None |
| L02 | SECTION_HEADER | Section divider, navy bg + roman numeral + title | None |
| L03 | TITLE_AND_BODY | Standard content, title top + body region | Optional inline icon from `assets/icons/ecology/` |
| L04 | TITLE_AND_TWO_BODY | Two columns balanced (text or chart + text) | One chart per column max |
| L05 | TITLE_AND_THREE_BODY | Three columns balanced | One small KPI per column |
| L06 | STAT_HERO | Single big stat 120pt + caption | `01-kpi.html` style |
| L07 | CHART_FOCUS | Chart 70% + commentary 30% | Any from `02-15` and `Tableaux-financiers.html` |
| L08 | MAP_FOCUS | Map 70% + legend/data 30% | `16-map.html` + SVG from `assets/maps/svg/` |
| L09 | TABLE_FOCUS | Full-bleed table | `14-table.html`, `14-table-v1.html`, `Tableaux-financiers.html` |
| L10 | QUOTE | Large quote + photo bg with navy_light overlay | None |
| L11 | ENDING | Closing CTA + corner brackets pair | Single KPI optional |
| L12 | BACK_COVER | Contact info + entity tagline + monogramme bottom-right | None |

## Chart usage in deck

**Hard rule:** before generating a slide chart, read in this order:
1. `rules/HARD-LOCKS.md` (palette, typography, overlays)
2. `rules/CHARTS.md` (catalog, palette order, mandatory eyebrow + accent line)
3. `examples/charts/<id>.html` (canonical SVG reference for the selected template)
4. `rules/ASSETS.md` (corner bracket teal, logo placement, wave watermark)
5. Master SHA preflight against `templates/MASTER_SHA.txt`

| Slide layout | Recommended chart templates |
|---|---|
| L06 STAT_HERO | `01-kpi.html` |
| L07 CHART_FOCUS | `02-bar`, `03-stacked`, `04-grouped`, `05-line`, `06-donut`, `07-progress`, `08-funnel`, `11-sankey`, `15-radar` |
| L08 MAP_FOCUS | `16-map.html` + region SVG |
| L09 TABLE_FOCUS | `14-table`, `14-table-v1`, `Tableaux-financiers` |
| L04 / L05 (compact) | `01-kpi`, `12-process`, `09-timeline`, `13-org`, icons from `assets/icons/ecology/` |

## Hard rules per layout

- Inherit from one of L01–L12 only. Custom layouts forbidden.
- One coral element max per slide (highlight).
- Two teal accents max per slide (corner + 1 callout).
- Photo overlays: navy_hard (strong text) or navy_light (ambiance) only, never cumulated. See `rules/PHOTOS.md`.
- Maps: white_fade overlay top + left mandatory on world maps. See `rules/MAPS.md`.
- Wave watermark behind section dividers and back cover only.

## Cross-references

- Master template SSOT: `templates/master-deck-current.pptx` + `templates/MASTER_SHA.txt`
- Hard locks: `rules/HARD-LOCKS.md`
- Charts: `rules/CHARTS.md` + `examples/charts/`
- Maps: `rules/MAPS.md` + `assets/maps/svg/`
- Tables: `rules/TABLES.md`
- Icons: `rules/ICONS.md` + `assets/icons/ecology/` + `assets/icons/`
- Photos: `rules/PHOTOS.md`
- Assets index: `rules/ASSETS.md`
- Brand voice / content: `rules/CONTENT-RULES.md` + `DESIGN.md` (root)

## Pending work (v4.x roadmap)

- [ ] Patch master PPTX `slideMaster1.xml` with logo + corner brackets + wave watermark (risk D, 1h, python-pptx).
- [ ] Generate 12 deck goldens PNG → `examples/deck/<layout>/golden.png` for visual diff QA (1h).
- [ ] Detailed slide-by-slide placeholder spec (positions in mm, font tokens, default content) — to be authored after master patch.
- [ ] Examples: 3 finished marketing slides → `examples/deck/finished/` (15 min).
