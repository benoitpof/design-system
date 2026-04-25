# POF Design System — `benoitpof/design-system`

**Version:** 3.2.1 | **Updated:** 2026-04-25
**Format slides :** LAYOUT_WIDE 20×11.25" (508×285.75 mm), 16:9
**Coordonnées :** mm partout (SSOT). Inches en commentaire pour pptxgenjs.

Source of truth for all Plastic Odyssey Factories brand assets, design tokens, and layout specifications.

---

## How to use this repo

Claude Design loads this repo at each session. Before generating any asset, Claude MUST:

1. Read `docs/DESIGN.md` — brand DNA, constraints, forbidden patterns
2. Load `tokens/brand-tokens.json` — all color/type/spacing values
3. Apply `tokens/brand-rules-per-format.json` — format-specific specs (mm, pt, px)
4. For layouts: reference `docs/LAYOUTS.md` — do not improvise layouts
5. For icons: reference `docs/ICONS.md` — use only listed Tabler icons
6. For media: query Notion collection `8ca51a75-2413-4f72-8f2a-c44d445fa1d0` via MCP, filter by `Usage recommandé` and `Type`, use `URL fichier` field

## Repo structure

```
/tokens/                        ← Design tokens (SSOT)
  brand-tokens.json
  brand-tokens.css
  brand-rules-per-format.json

/assets/
  /logos/                       ← Official logo SVGs
  /pictos/                      ← POF pictogram (mascot mark)
  /brand-elements/              ← Waves, corner brackets
  /backgrounds/                 ← Full-bleed SVG backgrounds

/docs/
  DESIGN.md                     ← Brand DNA + constraints (LLM-native spec)
  LAYOUTS.md                    ← 15 canonical slide layouts (grids + specs)
  ICONS.md                      ← Curated Tabler icon list with POF usage notes
  ASSETS.md                     ← Asset index with usage rules

/examples/
  /layouts/                     ← Annotated layout references (HTML previews)
  /slides/                      ← Validated slide examples
```

## Entity default

Default entity: **Factories**. Override with `entity=academy` or `entity=sunu` when needed.

## Media assets

Notion database: `collection://8ca51a75-2413-4f72-8f2a-c44d445fa1d0`
Query via MCP Notion. Filter: `Entité (BU)`, `Type`, `Usage recommandé`, `Orientation`.
Always use `URL fichier` field — never use Notion file attachments directly.
