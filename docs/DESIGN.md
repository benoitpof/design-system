# DESIGN.md — Plastic Odyssey Factories Design System

**Version:** 3.3.9 | **Updated:** 2026-04-26
**Source of truth:** `tokens/brand-tokens.json` + `tokens/brand-rules-per-format.json`
**Template reference:** `Template_POF_Claude.pptx` (LAYOUT_WIDE 20"×11.25" / 508×285.75 mm)
**Coordinate convention:** mm partout (SSOT). Inches en commentaire pour pptxgenjs.

## Hard locks (v3.2.3) — STRICT ENFORCEMENT

These rules are non-negotiable. Any violation in generated content (deck, web, report) must be flagged red in QA before delivery.

### Type-scale lock (aligned V2 template 2026-04-26)
Only 8 allowed sizes (pt): **9, 11, 14, 18, 22, 26, 28, 36**. Plus stat-only: 72, 120. No other sizes anywhere.

V2 hierarchy : cover_title 36pt ExtraBold · slide_title 26pt ExtraBold · slide_subtitle 26pt SemiBold · slogan 28pt SemiBold · body 22pt Regular · caption 18pt Light.

### Weight lock
Regular weights allowed: **300, 400, 600, 700**. ExtraBold (800) restricted to: cover slide title (L01), section divider title (L02), stat number (L04). Black (900) **forbidden**.

### Overlay system (v3.3.7 — replaces gradient_overlay_lock)

POF photo overlay system has TWO families :

**A. Solid uniform (3 levels)** — full-photo navy wash :
- `light` 30% : `rgba(28,31,59,0.30)` — subtle dim, photo readable
- `medium` 60% : `rgba(28,31,59,0.60)` — photo as ambiance, text readable on top
- `heavy` 90% : `rgba(28,31,59,0.90)` — photo as texture only

**B. Gradient (4 directions × 4 coverages × 2 colors × 3 intensities = 96 valid combinations)** :
- Direction (exclusive, no cumulation) : `from_left` / `from_right` / `from_top` / `from_bottom`
- Coverage extent (hold percentage) : `quarter` 25% · `third` 33% · `half` 50% · `full` 75%
- Color : `navy_pure` OR `navy_with_teal_reflet` (radial teal anchored bottom-left)
- Intensity : `full` (opaque hold → transparent) · **`medium` (75% hold → transparent)** · `soft` (50% hold → transparent)
- Pattern `full` : `linear-gradient(<angle>, #1C1F3B 0%, #1C1F3B <hold_pct>%, transparent 100%)`
- Pattern `soft` : `linear-gradient(<angle>, rgba(28,31,59,0.50) 0%, rgba(28,31,59,0.50) <hold_pct>%, transparent 100%)`

**Always ends 100% transparent.** Forbidden : non-axial directions (45deg etc.), cumulated directions, hold outside [25, 33, 50, 75], final stop not transparent, teal reflet position other than bottom-left.

Selection rules per use case in `tokens/brand-rules-per-format.json` `overlay_system.selection_rules`.

### Corner marks lock
L-brackets in 4 orientations: `assets/brand-elements/corner-bracket-{tl,tr,bl,br}.svg`. Size 12 mm. Color #80C7C2. Stroke 5px square cap. Default pair on every slide = TL + BR. Solid filled squares (deprecated v3.2.2) **forbidden**.

**No shadow, ever.** Corner marks are flat geometric strokes. Forbidden : drop-shadow (CSS or SVG `filter`), PowerPoint shape effect 'Shadow', `opacity < 1`, blur. The L-brackets must render exactly as authored — pure teal strokes on transparent background, zero depth effect. This rule applies whether the rendering target is a slide, a web page, a report, an artifact preview, or any other medium.



### Color hierarchy lock (v3.3.2 — feedback Benoit 2026-04-26)

Titles use NAVY on light bg and WHITE on dark bg. **Teal is a SECONDARY accent color, never the primary title color.**

Allowed teal uses (max 2 per page/slide) :
- 1-2 accent words within a slogan
- Callout block left border (4 mm wide)
- Decorative pipe accent left of title
- Wave watermark / brand element
- Stat number on dark bg only
- Data series in chart palette (series 4+ extended)

Forbidden teal uses :
- Primary slide title (use navy or white)
- Primary section title
- Primary heading on body pages
- All text in back cover (white default)

### Corner marks lock — TL only by default (v3.3.2)

Default pair = `top_left` ONLY. Bottom-right corner mark **forbidden by default** (was TL+BR until v3.3.1, deprecated by user feedback).

Top-right, bottom-left, bottom-right : optional only on explicit request.

### Covers lock (v3.3.2)

Cover slides (L01) and report covers :
- Cover title : Poppins ExtraBold **36pt MAX**. Color = white on dark bg, navy on light bg. Teal forbidden as cover title color.
- Cover subtitle : Raleway SemiBold, **26pt MAX, 22pt recommended**. NEVER 28pt+ for subtitle.
- Cover background : **flat navy `#1C1F3B`**. Navy depth gradient NOT allowed at top of cover (user feedback : « bleu navy trop clair en haut »).
- Cover wave decorative : MUST be fully visible (not clipped at edge).

### Back cover lock (v3.3.2)

4ème de couverture on navy bg :
- Default text color = **white**.
- Teal allowed on **ONE element only** (typically the tagline).
- Forbidden : all text (logo subtitle + address + email + tagline) in teal.

### Wave decorative visibility (v3.3.2)

Wave watermark from `assets/brand-elements/wave-{teal,white}.svg` MUST be fully visible. Never clipped at slide/page edge. Place at least 5 mm margin from any edge.

### Verbatim content mode
When user brief contains `<final_content>...</final_content>` tags or the phrase "this is final content / verbatim / do not edit": preserve wording exactly, only redistribute across layout slots. Never substitute with examples from CONTENT-RULES.md.


### Per-medium typography (v3.3.2 — distinction critique)

Le design system applique des tailles DIFFÉRENTES selon le medium. Cross-medium = couleurs, fonts, assets identiques. Distinct = tailles, grilles.

| Element | Slides 16:9 | Print A4 | Web |
|---|---|---|---|
| Body | **22 pt** Regular (`body_slide`, 30px) | **11 pt** Regular (`body_print`, 15px) | **16 px** Regular (`body_web`) |
| H1 / Title | 26 pt ExtraBold | **22 pt ExtraBold** | 36 px Bold |
| H2 / Subtitle | 26 pt SemiBold | **14 pt SemiBold** | 22 px SemiBold |
| H3 | 22 pt SemiBold | **12 pt SemiBold** | 18 px SemiBold |
| Caption | 18 pt Light | **9 pt Light italic** | 12 px Light |
| Footnote | 11 pt | 8 pt | 11 px |

Slides = lecture à 3 m, gros texte. Print = lecture à 25 cm, texte compact.

**Cover title** = 36pt MAX dans tous les media (slide + print).

Validation print : Rapport v1 (`Couverture rapport.html` + `Rapport-print.html`, 2026-04-26) sert de référence.
---

## 1. Brand DNA

**Plastic Odyssey Factories** deploys containerized plastic recycling units in developing countries via a franchise model.

- **Audience:** institutional partners, industrial investors, government procurement. Secondary: NGO teams, recycling entrepreneurs, press.
- **Tone:** direct, evidence-based, operational, warm but serious.
- **Visual DNA:** engineering documentation meets impact report. Wave waveform as signature element. Navy + teal as institutional duo. Coral as surgical emphasis only.
- **Avoid:** NGO softness, greenwashing clichés, corporate jargon, AI-generated feel.

---

## 2. Colors (canonical — verified from POF template XML)

### Primary
- `#1C1F3B` **navy** — headings, header bars, backgrounds, primary data
- `#80C7C2` **teal** — accent bars, logo waves, highlights, secondary data. **NEVER white text on teal.**

### Supporting
- `#F9FCFF` **light gray** — section backgrounds, card surfaces (POF "Gris POF")
- `#E8546C` **coral** — emphasis keywords ONLY. Max 1–2 per deck. Forbidden as bg fill of text blocks.
- `#435D74` **steel** — chart series 2, subtitles
- `#1C2D2B` **teal-deep** — gradient end, dark emphasis
- `#4BADA5` **teal-dark** — gradient start, hover states

### Background gradients (from SVG assets)
- **Navy gradient:** `#05387B → #1C1F3B` (slides 20–22 in template)
- **Teal gradient:** `#4BADA5 → #80C7C2`

### Semantic
- `#28A745` success · `#E5A100` warning · `#DC3545` error

### Forbidden combinations (WCAG fail)
- White on teal `#80C7C2` (1.64:1)
- White on light gray `#F9FCFF` → use navy
- Coral `#E8546C` as body text on white (3.55:1) — large text only

---

## 3. Typography

- **Heading:** Poppins (ExtraBold, Bold, SemiBold)
- **Body:** Raleway (ExtraBold, SemiBold, Regular, Light)
- **No serif fonts anywhere. Max 2 families. Max 3 heading levels.**

### Size scale (LAYOUT_WIDE 20"×11.25")
| Role | Font | Size | Color |
|------|------|------|-------|
| Slide title | Poppins ExtraBold | 26pt | teal or white |
| Slide subtitle | Raleway SemiBold | 26pt | navy |
| H2 content | Poppins SemiBold | 22pt | navy |
| Body | Raleway Regular | 22pt | navy `#1C1F3B` |
| Big stat number | Raleway ExtraBold | 120pt | white or navy |
| Stat unit | Raleway Black | 41pt | white |
| Caption / source | Raleway Regular | 22pt | navy light |

---

## 4. Slide format

**LAYOUT_WIDE: 20" × 11.25" (508 × 285.75 mm), aspect 16:9** — `pres.layout = 'LAYOUT_WIDE'`

Key anchors (verified from `Template POF - Claude.pptx` XML — `cx=18288000 cy=10287000` EMU):

| Element | mm (SSOT) | inches (pptxgenjs) |
|---|---|---|
| Logo (top-right) | x=421.3 y=20.6 w=64.5 h=16.4 | x=16.587 y=0.810 w=2.541 h=0.645 |
| Corner mark TL | x=19.0 y=16.3 w=7.7 h=7.7 | x=0.748 y=0.642 w=0.303 h=0.303 |
| Corner mark BR | x=483.2 y=265.5 w=7.7 h=7.7 | x=19.025 y=10.454 w=0.303 h=0.303 |
| Pipe accent (left of title) | x=19.0 y=19.05 w=1.4 h=12.2 | x=0.748 y=0.75 w=0.055 h=0.48 |
| Title zone | x=26.7 y=20.6 w=231.3 h=10.3 | x=1.051 y=0.810 w=9.106 h=0.404 |
| Subtitle zone | x=26.7 y=31.4 w=243.1 h=12.0 | x=1.051 y=1.237 w=9.570 h=0.471 |
| **Content zone (zone utile)** | **x=26.7 y=50.8 max_w=454.6 max_h=223.5** | **x=1.051 y=2.0 max_w=17.898 max_h=8.8** |
| Slide number | x=470.7 y=259.1 w=30.5 h=21.9 | x=18.531 y=10.200 w=1.200 h=0.861 |

Marges symétriques L/R = 26.7 mm (1.051"). Top header = 50.8 mm (2.0"). Bottom footer = 11.4 mm (0.45").

---

## 5. Brand elements

See `docs/ASSETS.md` for full index.

- **Wave motif** (`assets/brand-elements/wave-teal.svg`, `wave-white.svg`) — signature element, bottom-left or decorative
- **Corner bracket** (`assets/brand-elements/corner-bracket.svg`) — matches the `grpSp` corner marks in template
- **Logo** (`assets/logos/`) — white version on dark, color version on light
- **Picto** (`assets/pictos/`) — brand mark only, not a UI icon

---

## 6. Icons

See `docs/ICONS.md` — Tabler Icons curated list.
CDN: `https://unpkg.com/@tabler/icons/icons/[name].svg`

---

## 7. Media assets

Notion collection: `collection://8ca51a75-2413-4f72-8f2a-c44d445fa1d0`
Query via MCP. Filter by `Entité (BU)`, `Type`, `Usage recommandé`, `Orientation`. Use `URL fichier` field only.

---

## 8. Color schemes

- **dark** — navy bg, white heading, teal subtitle (covers, section dividers, callouts)
- **light** — white/F9FCFF bg, navy heading (content slides default)
- **teal accent** — teal bg, navy text only (CTA zones, badges)

---

## 9. Forbidden

- Serif fonts
- White text on teal
- Coral as bg fill of text blocks
- Greenwashing imagery
- Hex codes outside the token set
- Header bar accent lines under titles (per PPTX skill guidance)
- Any color not listed in section 2
