# DESIGN.md — Plastic Odyssey Factories Design System

**Version:** 4.0.0 | **Updated:** 2026-04-28
**Status:** Canonical Source of Truth (SSOT) for Claude Design ingestion.
**Companion files:** `tokens/brand-tokens.json` (machine), `rules/HARD-LOCKS.md` (full enforcement spec), per-medium rules in `rules/`.

This document is the canonical entry point for any AI agent (Claude Design, Claude Code, Cowork) generating brand-aligned visual content for Plastic Odyssey Factories. It compiles tokens and rules into nine sections required by the Claude Design ingestion format.

---

## 1. Visual Theme & Atmosphere

Plastic Odyssey Factories is an industrial impact business. The visual identity is **engineering documentation meets impact report**, not NGO softness. The brand mission is to deploy plastic recycling as a containerized franchise in developing countries; visuals must read as **technical, credible, operational, warm but serious**.

Core atmosphere:
- **Institutional duo navy + teal** as the structural backbone. Navy carries authority. Teal signals progress, technology, water/ocean origin story.
- **Coral as surgical emphasis only**. A single coral element per page draws the eye to the most important datapoint or callout. Never decorative.
- **Wave waveform** is the signature decorative element, used as background watermark or section break. References the Plastic Odyssey expedition origin.
- **Flat geometric**, no drop shadows, no glassmorphism, no AI-generated gradients. Depth is implied through typographic hierarchy and white space, not effects.
- **Photography**: real factory operations, real workers, real machinery. No stock smiles, no pristine green forests, no abstract eco illustrations.

Forbidden moods: greenwashing cliché, NGO softness, corporate jargon visuals, motivational poster aesthetics, generic SaaS gradients.

---

## 2. Color Palette & Roles

### Primary

| Token | Hex | Role |
|---|---|---|
| `navy` | `#1C1F3B` | Primary text on light bg, primary background on dark slides, institutional authority |
| `teal` | `#80C7C2` | Secondary accent (max 2 uses per page), corner brackets, callout borders, decorative pipe |

**Critical rule:** teal is **never the primary title color**. Titles use navy on light, white on dark. Teal is accent only.

### Accent

| Token | Hex | Role |
|---|---|---|
| `coral` | `#E8546C` | Surgical emphasis, single-bar highlight, critical KPI, max 1 use per page |
| `teal_dark` | `#2BA595` | Hover states, interactive elements |
| `teal_deep` | `#3B6F77` | Darker teal for compact sections |
| `steel_blue_gray` | `#435D74` | Secondary text, UI dividers |
| `light_steel` | `#5F7D95` | Non-textual UI only (axes, gridlines), fails WCAG for body text |

### Neutral

| Token | Hex | Role |
|---|---|---|
| `white` | `#FFFFFF` | Primary background light |
| `body_text` | `#2C3543` | Body text on light bg |
| `neutral_light` | `#F9FCFF` | Section background subtle |
| `neutral_mid` | `#CFD9E0` | Disabled bars, secondary chart series |
| `gray_400` | `#A4B4C4` | Tertiary text, captions on light bg |
| `gray_600` | `#6C757D` | Secondary chart labels |

### Semantic

| Token | Role |
|---|---|
| `success` | Green for positive deltas |
| `warning` | Amber for caution |
| `error` | Red for failures (distinct from coral, used in dashboards only) |

### Forbidden combinations (WCAG 2.1 AA)

| Pair | Ratio | Rule |
|---|---|---|
| white on teal `#80C7C2` | 1.64:1 | **NEVER**. Use navy text on teal. |
| white on academy_blue `#8ED1E8` | 1.69:1 | **NEVER**. Use navy text. |
| coral on white | 3.55:1 | Large text only (>18pt). |
| light_steel on white | 4.33:1 | UI elements only, never body text. |

---

## 3. Typography Rules

Two families only. No serif anywhere.

| Family | Use | Weights |
|---|---|---|
| **Poppins** | All headings, titles, button text, navigation, stat numbers, UI labels | 400, 500, 600, 700, 800 (cover only) |
| **Raleway** | Body text only | 300, 400, 600 |

### Size scale (locked, only these are allowed)

**Slides (LAYOUT_WIDE 20"×11.25"):** 9pt · 11pt · 14pt · 18pt · 22pt · 26pt · 28pt · 36pt. Stat-only: 72pt · 120pt.

**Hierarchy slide:**
- Cover title 36pt ExtraBold (800)
- Slide title 26pt ExtraBold
- Slide subtitle 26pt SemiBold (600)
- Slogan 28pt SemiBold
- Body 22pt Regular (400)
- Caption 18pt Light (300)

**Print/A4 body:** 11pt (15px) Raleway 1.5 line-height.

**Weight lock:**
- Allowed: 300, 400, 500, 600, 700.
- ExtraBold (800): cover slide title, section divider title, stat number only.
- Black (900): **forbidden everywhere**.

**Other rules:**
- Max 2 type families per artefact.
- Max 3 heading levels.
- ALL CAPS allowed for titles only, max 2 lines, letter-spacing 1px wide.
- No serif anywhere.

---

## 4. Component Stylings

### Charts (16 templates, locked)

Catalog: KPI · bar (vertical/horizontal) · stacked · grouped · line · donut · progress · funnel · timeline · gantt · sankey · process · org chart · table · radar · map · icons · images.

Reference HTML in `examples/charts/`. Full rules in `rules/CHARTS.md`.

Chart palette order: navy `#1C1F3B` (series 1, lead) · teal `#80C7C2` (series 2) · neutral_mid `#CFD9E0` (series 3, deprioritised). Coral reserved for highlight on a single bar.

Mandatory chart elements: eyebrow label (uppercase, sm size, steel_blue_gray) + horizontal accent line (40px navy 2pt) + chart title (Poppins 600). All charts include POF wave watermark bottom-right at 8% opacity.

### Maps (5 patterns)

Patterns: heatmap · categorical · neutral dots · data dots · anchored faded. Full rules in `rules/MAPS.md`. Source SVGs in `assets/maps/svg/`.

Mandatory overlay on world maps: white_fade top (stops at North Africa latitude) + white_fade left (stops at West Africa coast). Always active. Never overlaps colored country highlights or legend.

### Tables

Header row: navy bg + white text Poppins 600 14pt. Body rows: alternating white / neutral_light backgrounds. Borders: 1px gray_400, only horizontal between rows. Header reads in TitleCase, never ALL CAPS. Logo POF bottom-right at 8% opacity. Full rules in `rules/TABLES.md`.

### Icons

Source: `assets/icons/` (custom POF teal/navy/white sets) + Tabler CDN as fallback. Stroke 1.5px. Color teal `#80C7C2` on light bg, white on dark bg. Size: 24px UI, 48px slide content. Full rules in `rules/ICONS.md`.

### Corner brackets (signature element)

L-brackets in 4 orientations (`assets/brand-elements/corner-bracket-{tl,tr,bl,br}.svg`). Size 12mm. Color teal `#80C7C2`. Stroke 5px square cap. **No shadow, ever.** Pure flat strokes, transparent background.

Default placement: TL only by default (v3.3.2). Pair TL + BR allowed for cover slides. Forbidden: drop-shadow, opacity < 1, blur, PowerPoint shape effect 'Shadow'.

### Buttons / CTAs (web)

Primary: navy bg, white text Poppins 600 14pt, 8mm padding y / 16mm padding x, 4px border-radius. Hover: teal_dark bg.
Secondary: 1px navy border, navy text, transparent bg. Hover: navy bg + white text.

---

## 5. Layout Principles

### Slide format (master)

Slides are **20"×11.25" LAYOUT_WIDE** (508×285.75mm). Coordinate convention: mm everywhere. Margins: 25mm L/R, 20mm T/B. Bleed 3mm if printed.

12 canonical layouts in `templates/master-deck-current.pptx` (SHA in `templates/MASTER_SHA.txt`):
1. TITLE — cover, full bleed photo + navy_hard overlay + teal corner TL
2. SECTION_HEADER — section break, navy bg + white title + wave watermark
3. TITLE_AND_BODY — standard content, title top + body region
4. TITLE_AND_TWO_BODY — two columns balanced
5. TITLE_AND_THREE_BODY — three columns balanced
6. STAT_HERO — single big stat + caption
7. CHART_FOCUS — chart 70% + commentary 30%
8. MAP_FOCUS — map 70% + legend/data 30%
9. TABLE_FOCUS — full-bleed table
10. QUOTE — large quote + photo bg with navy_light overlay
11. ENDING — closing CTA + corner brackets pair
12. BACK_COVER — contact info + entity tagline + monogramme bottom-right

Layout discipline: any slide MUST inherit from one of these 12 layouts. Custom layouts not allowed.

### Report format (A4 portrait)

210×297mm, 25mm L/R, 20mm T/B margins. 1-2 columns max. Heading 1: navy 18pt SemiBold. Heading 2: navy 14pt SemiBold. Body 11pt Raleway 1.5 line-height. Page number bottom-right with monogramme. Full rules in `layouts/REPORT.md`.

### Web format

Max content width 1200px. Hero 80vh max. Section padding 80px y / 24px x desktop, 40px y / 16px x mobile. Full rules in `layouts/WEB.md`.

### Social formats

LinkedIn 1200×627 carousel slide or 1080×1080 single. Instagram 1080×1080 or 1080×1350. Always include teal corner TL + monogramme BR. Full rules in `layouts/SOCIAL.md`.

---

## 6. Depth & Elevation

POF is a **flat design system**. There is no elevation hierarchy via shadows.

Depth is achieved through:
- **Typographic hierarchy** (size + weight + color contrast)
- **White space** (generous margins, never crowded)
- **Color blocking** (full-bleed navy or teal sections)
- **Wave watermarks** at 8% opacity (background only, never foreground)
- **Photo overlays** (navy_hard or navy_light, see overlay system)

### Overlay system (v4.0.0), THREE canonical types only

**Type 1 — `white_fade`** (maps only): linear gradient from 100% opaque white at viewBox edge to 0% transparent. Cumulation allowed across multiple sides. Never overlaps colored country highlights.

**Type 2 — `navy_hard`** (photos with strong text zone): `linear-gradient(<angle>, rgba(28,31,59,0.90) 0%, transparent 100%)` + radial teal flair at bottom-left rgba(128,199,194,0.40) 0% to transparent 50%. Sizes: quarter 25%, half 50%, full 75%. **One direction at a time, never cumulated.**

**Type 3 — `navy_light`** (photos, ambiance): `linear-gradient(<angle>, rgba(28,31,59,0.40) 0%, transparent 100%)`. Same sizes as Type 2. **One direction at a time, never cumulated.** Verify WCAG AA before applying text on top.

**Forbidden:** drop-shadow (CSS or SVG `filter`), PowerPoint Shadow effect, blur, glassmorphism, opacity < 1 on corner brackets or logos, solid uniform overlay fills, non-axial gradient directions, cumulation on photo overlays, hold values outside [25, 50, 75], teal flair outside bottom-left anchor.

---

## 7. Do's and Don'ts

### Do

- Use navy + teal as institutional duo on every artefact.
- Place TL corner bracket teal on every slide by default.
- Use coral exactly once per page, on the most critical KPI or callout.
- Embed POF wave watermark at 8% opacity in all charts and section backgrounds.
- Lead chart series with navy, never teal.
- Apply white_fade overlay top + left on every world map.
- Keep all caps to titles only, with 1px letter-spacing.
- Use Poppins for headings, Raleway for body. Never invert.
- Read `rules/<medium>.md` before generating any artefact in that medium.

### Don't

- Don't use teal as primary title color (it's an accent, max 2 uses per page).
- Don't use coral decoratively or more than once per page.
- Don't add drop shadows, glassmorphism, or blur to any element.
- Don't use weights 800 or 900 outside the explicit cover/section/stat exceptions.
- Don't use serif fonts.
- Don't draw layouts from scratch. Always inherit from one of 12 master layouts.
- Don't ship a chart without reading `rules/CHARTS.md` AND its canonical example in `examples/charts/`.
- Don't use white text on teal or white on academy_blue (WCAG fail).
- Don't apply photo overlays cumulatively (one direction at a time).
- Don't use stock photography. POF photos only.

---

## 8. Responsive Behavior

POF outputs are **medium-locked**, not fluid. Each medium has fixed dimensions:

| Medium | Dimensions | Notes |
|---|---|---|
| Deck | 20"×11.25" (LAYOUT_WIDE) | PPTX only, no responsive logic |
| Report | A4 portrait 210×297mm | DOCX/PDF, fixed |
| Web | Desktop ≥1024px primary, ≥1200px content max | Tablet 768-1023px: stack columns. Mobile <768px: single column, hero 60vh, padding 40/16. |
| Social LinkedIn | 1200×627 or 1080×1080 | Per-format fixed |
| Social Instagram | 1080×1080 or 1080×1350 | Per-format fixed |

Web breakpoints (the only responsive medium):
- Desktop ≥1024px: 12-column grid, content max 1200px, padding 80/24
- Tablet 768-1023px: 8-column grid, padding 60/20, columns stack at 600px
- Mobile <768px: single column, padding 40/16, font sizes -10%

Typography scales identically across breakpoints, no fluid type. Overlays and corner brackets resize proportionally to viewport, but stroke width stays fixed at 5px.

---

## 9. Agent Prompt Guide

When generating POF visual content via an AI agent (Claude Design, Cowork, Claude Code), the agent MUST:

### 1. Read tokens first
- `tokens/brand-tokens.json`, full token registry
- `tokens/brand-rules-per-format.json`, per-medium constraints

### 2. Read the relevant rule file BEFORE generation
- Charts → `rules/CHARTS.md`
- Maps → `rules/MAPS.md`
- Tables → `rules/TABLES.md`
- Icons → `rules/ICONS.md`
- Photos → `rules/PHOTOS.md`
- Assets → `rules/ASSETS.md`
- Hard locks (always) → `rules/HARD-LOCKS.md`
- Content/narrative → `rules/CONTENT-RULES.md`

### 3. Read the canonical example
- Charts → `examples/charts/<id>.html` (18 ready-to-use SVG templates)
- Maps → `assets/maps/svg/<region>.svg` + `examples/maps/`
- Layouts → `layouts/<MEDIUM>.md`
- Memory/Rex → `memory/<medium>.md` (capitalised learnings)

### 4. Use the master template (deck/report)
- `templates/master-deck-current.pptx` (SHA in `templates/MASTER_SHA.txt`)
- Validate SHA preflight. Any drift = fail.
- Inherit from one of 12 canonical layouts. Never invent.

### 5. Apply hard locks
- Palette: only tokens listed in §2.
- Typography: only sizes listed in §3.
- Corner brackets: TL teal mandatory, no shadow.
- Coral: max 1 per page.
- Teal: max 2 accent uses per page, never as title color.

### 6. QA before delivery
- Run `scripts/composition-qa.py` (when available) for hard locks compliance.
- Visual diff vs golden if available (`examples/<medium>/golden.png`).
- Flag any WCAG fail combinations.

### Glossary

- **Factory**, POF containerized recycling unit (mother unit + processing modules).
- **Mother unit**, primary container hosting wash + sort + grind line.
- **Module**, secondary container (extrusion, injection, baling).
- **Franchise**, local entrepreneur operating a POF factory under license.
- **Site**, geographic deployment of one or more factories.

### Brand voice (for any text generated)

Direct, evidence-based, operational, warm but serious. No weak adverbs ("assez", "plutôt", "rather"). No corporate jargon. No AI filler ("indeed", "moreover", "delve"). Never use em dash in body copy.

For full brand voice spec, see `memory/BRAND-VOICE.md` (when populated by ds-iterate).

---

**Repo SSOT:** `github.com/benoitpof/design-system`
**Skills consuming this DS:** `ds-file-assembler`, `ds-dataviz-generator`, `ds-iterate`, `ds-feedback`.
**Maintained by:** Benoît Blancher · benoit@plasticodyssey.org · Plastic Odyssey Factories.
