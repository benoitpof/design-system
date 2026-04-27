# ASSETS.md — POF Brand Asset Index

**Version:** 3.3.10 | **Updated:** 2026-04-26
All paths relative to `/assets/` unless stated otherwise.

This document covers two complementary asset stores:
1. **Static brand assets** (versioned in this repo)
2. **Dynamic media assets** (Notion database `Media Assets` — referenced by ID, not stored in Git)

---

## 1. Static brand assets (in this repo)

### Logos — `/assets/logos/`

| File | Usage | Background | Notes |
|------|-------|------------|-------|
| `pof-logo-color.svg` | Default — light backgrounds | White, light gray, F9FCFF | Primary use |
| `pof-logo-white.svg` | On dark backgrounds | Navy, dark photo | Header bars, cover slides |
| `pof-logo-navy-bg.svg` | White logo with built-in navy rectangle | Any | Padding pre-applied |
| `pof-logo-variant-1.svg` | Alternate reserved version | Dark | Secondary use |
| `pof-logo-variant-2.svg` | Alternate reserved version | Dark | Secondary use |

**Logo placement on slides (verified Template POF XML, LAYOUT_WIDE 16:9):**
- Position: top-right, `x=421.3 y=20.6 w=64.5 h=16.4 mm` (inches: `x=16.587 y=0.810 w=2.541 h=0.645`)
- Never stretch, rotate, recolor
- Minimum size: 40 mm wide
- Clear space: 10 mm on all sides minimum
- Cover slide L01 exception: top-left, `x=26.7 y=12.7 w=88.9 h=22.6 mm`

### Brand pictos (mascot mark) — `/assets/pictos/`

| File | Usage | Color |
|------|-------|-------|
| `pof-picto-color.svg` | Color version on light bg | Teal #80C7C2 |
| `pof-picto-white.svg` | Reversed on dark/navy bg | White |

These are the brand symbol (waves stacked). Use as: standalone mark, loading states, favicon, decorative corner, internal asset only. **NOT a UI icon.** For UI icons see `/assets/icons/` below.

### UI icons — `/assets/icons/` — see `docs/ICONS.md`

170 SVG icons in 2 folders (v3.2.6):
- `ecology/` — 8 themes × 4 variants (currentColor, _navy, _teal, _white) = 32 SVG
- `environment/` — 46 themes × 3 variants (_navy, _teal, _white) = 138 SVG

For full inventory and selection workflow, see `docs/ICONS.md`. For Tabler CDN fallback, see same doc section 2.

55 SVG icons (47 root + 8 in `/ecology/` subfolder) covering POF use cases:
factory & production (barrel, tools, cash, flag), ecology (leaf-2, plant-2, seedling, tree, recycle), logistics (ship, plane, plane-arrival, plane-departure, truck), people & impact (heart, hand-stop, lifebuoy, trophy, sparkles), data & process (chart, refresh, settings, arrows-shuffle), comms (mail, microphone, video, camera).

All icons use `stroke="currentColor"` → recolorable via CSS `color: ...`. Default render: 24 × 24 viewBox, stroke-width 2, no fill. Set CSS `color: var(--pof-navy)` on light bg, `color: white` on dark bg.

For full list, browse `/assets/icons/`. To add new icons, source from Tabler Icons (MIT license), apply same `currentColor` pattern, commit.

### Brand elements (signature waves + corner brackets) — `/assets/brand-elements/`

| File | Description | Usage |
|------|-------------|-------|
| `wave-teal.svg` | Double wave teal #80C7C2 | Light bg slides, decorative |
| `wave-white.svg` | Double wave white | Dark bg slides |
| `corner-bracket-tl.svg` | L-bracket top-left, teal stroke | Slide corners (default pair with BR) |
| `corner-bracket-tr.svg` | L-bracket top-right | Optional symmetric framing |
| `corner-bracket-bl.svg` | L-bracket bottom-left | Optional symmetric framing |
| `corner-bracket-br.svg` | L-bracket bottom-right | Slide corners (default pair with TL) |
| `corner-bracket.svg` | Alias = corner-bracket-tl.svg | Backward compatibility |

**Wave placement:** bottom-left or top-right of content zones. Never centered. Never over text. Scale 30–60 mm wide.

**Corner brackets:** placed at slide corners per `tokens/brand-rules-per-format.json` `slides.corner_marks`. Default pair = TL + BR.

### Backgrounds — `/assets/backgrounds/`

| File | Dimensions | Description | Usage |
|------|-----------|-------------|-------|
| `bg-wave-01.svg` | 1920×540 px | Navy gradient + waves (band) | Hero strip, half-slide |
| `bg-wave-02.svg` | 1920×1080 px | Full navy gradient + waves | Full-bleed dark slides |

Always full-bleed when used. Text on top: white only (never navy or teal). For text legibility over photo + bg: layer the canonical photo overlay gradient (`tokens.gradient_overlay_lock.canonical_value`).

---


### Maps — `/assets/maps/`

POF cartographic system — see `docs/MAPS.md` for full charter.

| File | Type | Description |
|------|------|-------------|
| `pof-world-map-blank.svg` | Master vector | World map, 175 country paths with ISO-2/3 IDs and group metadata (UEMOA, CEDEAO, AU). Source for all map work. |
| `pof-world-map-annotated.svg` | Master with labels | Same as blank + country labels for priority POF countries |
| `pof-world-map.svg` | Legacy alias | Same as blank, kept for backward references |
| `pof-world-map-doc.md`, `POF-WORLD-MAP-GUIDE.md` | Docs | Country IDs, group definitions, JS query examples |
| `pof-world-map-v1.1.0.zip` | Release | Versioned package |
| `svg/01-monde.svg` to `svg/07-ocean-indien-est.svg` | 7 regional crops | Pre-cropped views (Monde, SE Asia, Africa, Indonesia, Philippines, West Africa, East Africa & Indian Ocean) |
| `png-source/01..07.png` | PNG raster source | High-res rasters for the 7 regional views |
| `map-charter.html` | Interactive charter | 5 patterns visualized (heatmap, categorical, neutral dots, data dots, anchored faded) + 3 navy heatmap N1/N2/N3 variants |
| `USAGE.md` | Asset guide | Use case + layer structure for each regional SVG |
| `_map-data.js` | Data utility | JS helpers for country selection and coloring |

For map patterns spec (heatmap, categorical, dots, anchored), see `docs/MAPS.md`.


---

## 2. Notion Media Assets database

**Source of truth for all photos, videos, illustrations, raster pictograms.**
Database ID: `8ca51a75-2413-4f72-8f2a-c44d445fa1d0`
URL: `collection://8ca51a75-2413-4f72-8f2a-c44d445fa1d0`
Notion URL: https://www.notion.so/25bd7cc0e7454f0f9cb8607870f59738?v=342c2ce245e880fabb97000cc87a1cbb
Drive folder (raw files, source for URL fichier): https://drive.google.com/drive/folders/1oqm8Wkh_lfH4Vw4j7vBJNtoO8aji9GIn

This repo is **agnostic of the photo content** — Git stores only static brand assets (above). Dynamic media (photos, videos, country-specific imagery) lives in Notion and is queried by Claude Design at generation time.

### Database schema (complete — v3.2.4)

| Field | Type | Required | Options / Format |
|-------|------|----------|------------------|
| `Nom` | title | yes | Free text title |
| `Aperçu` | file | recommended | Preview thumbnail (auto-generated or uploaded) |
| `Description` | text | optional | Free text caption / context |
| `Dimensions` | text | optional | e.g. `4032×3024 px` or `1920×1080 px` |
| `Type` | select | **required for filtering** | `Photo terrain`, `Photo produit`, `Photo équipe`, `Icône`, `Logo`, `Vidéo`, `Illustration`, `Pictogramme` |
| `Entité (BU)` | select | **required for filtering** | `Factories`, `Academy`, `Sunu PO`, `Transversal` |
| `Pays` | select | recommended | `Sénégal`, `Philippines`, `Kenya`, `France`, `Égypte`, `Liban`, `Cameroun`, `Autre` |
| `Produit / Sujet` | multi-select | recommended | `CDF`, `PTF`, `Programme`, `RSE`, `Collecte`, `Recyclage`, `Formation`, `Général`, `Equipe` |
| `Usage recommandé` | multi-select | **required for filtering** | `Hero slide`, `Fiche produit`, `Catalogue`, `LinkedIn`, `Site web`, `Deck`, `Rapport`, `Carte de visite` |
| `Orientation` | select | recommended | `Paysage`, `Portrait`, `Carré` |
| `URL fichier` | url | **MANDATORY** | Public direct URL to the asset (Notion CDN, Google Drive public, Cloudinary, S3) |

### Minimum viable record

For Claude Design to use an asset, the record MUST have:
1. `URL fichier` (non-empty, publicly accessible)
2. `Type`
3. `Entité (BU)`
4. `Usage recommandé`

Records missing any of these 4 are invisible to the auto-selection pipeline.

### Query protocol

When Claude Design needs an image for a layout, it queries the Notion DB with a filter combination, then picks the best-ranked result.

**Filter combinations by use case:**

| Use case | Query filter |
|---|---|
| Cover slide L01 (deck Factories Senegal) | `Type=Photo terrain AND Entité=Factories AND Pays=Sénégal AND Usage~Deck AND Orientation=Paysage` |
| Section divider L02 | `Type=Photo terrain AND Entité=<current> AND Usage~Deck AND Orientation=Paysage` |
| Content + image L03 (CDF detail) | `Type=Photo produit AND Produit/Sujet~CDF AND Orientation=Paysage` |
| Big number L04 (background) | `Type=Photo terrain AND Entité=<current> AND Usage~Deck AND Orientation=Paysage` |
| Team L12 portrait | `Type=Photo équipe AND Orientation~Portrait,Carré` |
| LinkedIn share post | `Type=Photo terrain OR Photo produit AND Usage~LinkedIn AND Orientation=Paysage` |
| Catalogue produit (cover product sheet) | `Type=Photo produit AND Usage~Catalogue AND Orientation=Paysage` |
| Carte de visite back side | `Type=Photo équipe OR Photo terrain AND Usage~Carte de visite AND Orientation=Paysage` |

**Ranking heuristic when multiple results:**
1. Exact `Pays` match (if specified) > generic
2. Recent `createdTime` > older
3. Higher `Dimensions` resolution (parse from text field) > lower
4. Has `Description` filled > empty

### Default values when not specified

If the user brief does not specify:
- `Entité` → default `Factories`
- `Pays` → no filter (all countries)
- `Orientation` → `Paysage` for slides, `Carré` for LinkedIn square, `Portrait` for posters
- `Usage` → match the layout type (Deck for slides, LinkedIn for social, etc.)

### What NOT to do

- Never use Notion file attachments directly (`<file>` blocks) — only the `URL fichier` text field
- Never embed images by Notion page ID — always resolve to public URL first
- Never query without at least one filter (would return everything)
- Never write back to Notion automatically — proposals go to a CSV for human review
- Never assume an asset exists without a query

### Adding new assets to Notion

Manual workflow today (no auto-import):
1. Upload the file to its hosting (Drive public folder, Notion CDN, Cloudinary)
2. Get the public direct URL
3. Create a Notion page in `Media Assets` with:
   - `Nom` = descriptive title
   - `URL fichier` = public URL
   - `Type` = one of the 8 options
   - `Entité (BU)` = one of the 4
   - `Usage recommandé` = one or more of the 8
   - `Pays` (when relevant)
   - `Produit / Sujet` (when relevant)
   - `Orientation`
   - `Description` (recommended for searchability)
4. Verify by querying the DB with the expected filter — the asset must come back

### Bulk audit & enrichment

For periodic audits (missing fields, broken URLs, duplicates):
- Use the Backlog task pattern documented in tasks chain `DESIGN-SYSTEM-V3 / Piste 2`
- Output: 4 CSVs (audit, tagging proposals, hosting recommendation, top 30 priority)
- Cadence: every 60 days while < 50 fully-tagged assets, every 6 months once stable

---

## Source-of-truth precedence

When in doubt about a brand value:
1. `tokens/brand-tokens.json` — colors, typography, spacing, components
2. `tokens/brand-rules-per-format.json` — format-specific rules (slides, docs, web, excel, linkedin)
3. `docs/DESIGN.md` — narrative spec, hard locks
4. `docs/LAYOUTS.md` — slide layouts L01–L15
5. `docs/CONTENT-RULES.md` — narrative content rules per layout
6. **This file (`docs/ASSETS.md`)** — asset index, photo DB schema and query protocol

For dynamic media (photos), Notion DB is the source. This repo is the index and protocol.

---

## Memory — capitalisation Rex (v3.4.0)

<!-- ds-iterate écrit ici. Format : ### YYYY-MM-DD — <titre> -->

(vide pour l'instant)
