# DESIGN.md — Plastic Odyssey Factories Design System

**Version:** 3.2.2 | **Updated:** 2026-04-25
**Source of truth:** `tokens/brand-tokens.json` + `tokens/brand-rules-per-format.json`
**Template reference:** `Template_POF_Claude.pptx` (LAYOUT_WIDE 20"×11.25" / 508×285.75 mm)
**Coordinate convention:** mm partout (SSOT). Inches en commentaire pour pptxgenjs.

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
