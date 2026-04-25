# ASSETS.md — POF Brand Asset Index

**Version:** 3.1.0 | All paths relative to `/assets/`

---

## Logos

| File | Usage | Background | Notes |
|------|-------|------------|-------|
| `logos/pof-logo-color.svg` | Default — on white/light backgrounds | White, light gray | Primary use |
| `logos/pof-logo-white.svg` | On dark backgrounds (navy, photo) | Navy, dark | Header bars, cover slides |
| `logos/pof-logo-navy-bg.svg` | Reserved / white logo on navy rectangle | Any | For dark placements with padding |
| `logos/pof-logo-variant-1.svg` | Alternate reserved version | Dark | Secondary use |
| `logos/pof-logo-variant-2.svg` | Alternate reserved version | Dark | Secondary use |

**Logo placement rules (MANDATORY):**
- Always top-right on slides (x=224mm, y=4mm, w=26mm, h=12mm per brand-rules-per-format.json)
- Never stretch, rotate, or recolor
- Minimum size: 20mm wide
- Clear space: 5mm on all sides minimum

---

## Pictos (POF mascot mark — waves stacked)

| File | Usage | Color |
|------|-------|-------|
| `pictos/pof-picto-color.svg` | Color version — on white/light | Teal #80C7C2 |
| `pictos/pof-picto-white.svg` | Reversed — on dark/navy | White |

Used as: standalone brand mark, loading states, favicon, corner decoration.
Do NOT use as inline icon in body text. This is a brand symbol, not a UI icon.

---

## Brand Elements (signature wave motif)

| File | Description | Usage |
|------|-------------|-------|
| `brand-elements/wave-teal.svg` | Double wave — teal #80C7C2 | Light bg slides, decorative element |
| `brand-elements/wave-white.svg` | Double wave — white | Dark bg slides, header bar decoration |
| `brand-elements/corner-bracket.svg` | L-shaped corner bracket in teal | Slide corners, section markers |

**Wave placement:** Bottom-left or top-right of content zones. Never centered. Never over text.
**Scale:** 30-60mm wide on slides. Proportional.

---

## Backgrounds (full-bleed SVG)

| File | Dimensions | Description | Usage |
|------|-----------|-------------|-------|
| `backgrounds/bg-wave-01.svg` | 1920×540px | Navy gradient with wave pattern | Hero/cover slides (16:9 or cropped) |
| `backgrounds/bg-wave-02.svg` | 1920×1080px | Full navy gradient + waves | Full-bleed dark slides |

**Usage rules:**
- Always full-bleed (cover entire slide canvas)
- Text on top: white only, never navy or teal
- Add opacity overlay only if photo is layered on top: use `--pof-gradient-navy-overlay`
- Do NOT crop or tile

---

## What belongs here vs. Notion Media Assets

| Asset type | Location |
|-----------|---------|
| Logos, pictos, wave elements, backgrounds | This repo (`/assets/`) |
| Field photos, team photos, product photos | Notion Media Assets DB |
| Video thumbnails | Notion Media Assets DB |
| Illustrations (non-brand) | Notion Media Assets DB |
| UI icons (Tabler) | CDN — see ICONS.md |
