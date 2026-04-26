# ICONS.md — POF Icon System

**Version:** 2.0 | **Updated:** 2026-04-26 | **Design system:** v3.3.0

POF icon system uses three sources, in priority order :

1. **POF curated icons in repo** (`/assets/icons/ecology/` and `/assets/icons/environment/`)
2. **Tabler Icons via CDN** (fallback for generic UI icons)
3. **POF brand pictos** (`/assets/pictos/`) — brand mark only, NOT a UI icon

---

## 1. POF curated icons — `/assets/icons/`

### `ecology/` — 8 themes × 4 variants = 32 SVG

Themes : `bolt`, `droplet`, `fish`, `flame`, `leaf`, `planet`, `recycle`, `solar-panel`

Variant pattern :

| Suffix | Color strategy | Use |
|---|---|---|
| `<name>.svg` | `stroke="currentColor"` | Recolor via CSS (`color: ...`). Preferred when context allows CSS theming. |
| `<name>_navy.svg` | hardcoded `#1C1F3B` | Embed in PPTX, DOCX, PDF — anywhere CSS does not apply. Default for light backgrounds. |
| `<name>_teal.svg` | hardcoded `#80C7C2` | Accent / highlight on white or navy backgrounds. |
| `<name>_white.svg` | hardcoded `#FFFFFF` | On dark / navy backgrounds. |

### `environment/` — 46 themes × 3 variants = 138 SVG

Themes covering POF operations : agriculture, arbre, borne-collecte, borne-depot, circularite, cle-outil, contenant-eco, contenant-reutilisable, eau-propre, mobilite-electrique, plastique-1 à plastique-7 (resin codes), produit-eco-concu, produit-marin, verre-recyclable, etc.

Variant pattern : `_navy`, `_teal`, `_white` (no unsuffixed `currentColor` variant in this folder yet — to be added in v3.2.7).

### Selection workflow

1. Identify icon need → look in `ecology/` first, then `environment/`
2. Pick the right variant for the medium :
   - Slide on light bg → `_navy` (or unsuffixed if CSS-controlled HTML)
   - Slide on dark bg → `_white`
   - Accent / call-out → `_teal`
   - Web (HTML/CSS) → unsuffixed + CSS `color: var(--pof-navy)`

### Canonical colors enforcement

All POF icons in repo use only canonical hex :
- navy `#1C1F3B`
- teal `#80C7C2`
- white `#FFFFFF`
- `currentColor` (CSS-controlled)

Forbidden in icons : `#1A2B4A`, `#1D1E3A`, `#75DBCD`, `#80C8C3`, `#1C2D2B`, any other variant. Audited and enforced as of v3.2.6.

---

## 2. Tabler Icons — fallback CDN

When POF curated icons do not cover a need, use Tabler Icons via CDN :

```
https://unpkg.com/@tabler/icons/icons/outline/[name].svg
```

Examples : `building-factory-2`, `container`, `package`, `truck`, `arrows-exchange`, `chart-bar`, `users`, `settings`, `mail`.

When integrating a Tabler icon :
1. Fetch SVG from CDN
2. Replace `stroke="currentColor"` is already there — keep it
3. For PPTX / DOCX / PDF : recolor by adding `style="color: #1C1F3B"` on parent or rasterize at target color
4. Document the icon used in the deliverable's source caption when relevant

Do NOT commit Tabler icons back into this repo. The CDN is the source.

---

## 3. POF pictos — brand mark — `/assets/pictos/`

Two files only :

| File | Color | Use |
|---|---|---|
| `pof-picto-color.svg` | Teal `#80C7C2` | Mark on light backgrounds |
| `pof-picto-white.svg` | White | Mark on dark backgrounds |

This is the POF brand symbol (waves stacked). Use cases : favicon, loading state, decorative corner mark, internal asset.

**NOT a UI icon.** Do not place it inline in body text or as a generic icon for content.

---

## Size guide (LAYOUT_WIDE slides)

| Use case | Render size |
|---|---|
| Feature card icon | 0.6 × 0.6" (rasterize at 256px for PPTX) |
| Inline header icon | 0.4 × 0.4" |
| Full-width hero icon | 1.0 × 1.0" |
| Process step icon | 0.5 × 0.5" |
| Web (HTML/CSS) | 24 × 24 px to 64 × 64 px depending on context |

---

## Forbidden

- Any color outside the canonical palette
- Coral `#E8546C` for icons (emphasis only, not iconography)
- Adding shadow, drop-shadow, blur, filter to icons
- Using brand picto as a UI icon
- Stretching, rotating, or distorting icons
- Mixing Tabler icons and POF curated icons in the same row / context (visual inconsistency)
