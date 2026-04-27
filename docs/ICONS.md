# ICONS.md — POF Icon System

**Version:** 3.0 | **Updated:** 2026-04-27 | **Design system:** v3.3.6

POF icon system uses **Tabler Icons CDN** as the primary source. Custom curated POF SVG icons (ecology, environment) have been archived because their custom stroke-width (28) was incompatible with the visual lightness of Tabler outline style.

---

## 1. Tabler Icons via CDN — primary source

```
https://unpkg.com/@tabler/icons/icons/outline/[name].svg
```

Examples : `building-factory-2`, `container`, `package`, `truck`, `arrows-exchange`, `chart-bar`, `users`, `settings`, `mail`, `recycle`, `leaf`, `droplet`, `flame`, `bolt`, `fish`, `planet`, `solar-panel`.

### Selection workflow

1. Browse https://tabler.io/icons or https://tabler-icons.io to find the icon
2. Use the outline variant: `unpkg.com/@tabler/icons/icons/outline/<name>.svg`
3. The SVG already has `stroke="currentColor"` and `stroke-width="2"` (light, modern)
4. Recolor via CSS : `<svg style="color: var(--pof-navy)">` or `color: var(--pof-teal)` etc.

### Embed strategies

| Context | Approach |
|---|---|
| HTML / Web | `<img src="https://unpkg.com/@tabler/icons/icons/outline/[name].svg">` + CSS `color` (currentColor cascade) |
| Inline HTML | Fetch SVG, paste inline, add `style="color: ..."` |
| PPTX | Fetch SVG, rasterize to PNG at target color (e.g. via `sharp` Node.js or any vector tool), embed PNG |
| DOCX / PDF | Fetch SVG, convert to PNG, embed image |

### Default colors per medium

- **Light bg** : `#1C1F3B` (navy)
- **Dark bg** : `#FFFFFF` (white)
- **Accent / highlight** : `#80C7C2` (teal)
- **Forbidden** : coral `#E8546C` for icons (emphasis only, not iconography)

### Recommended icon shortlist for POF

Industrial / production : `building-factory-2`, `container`, `package`, `tools`, `hammer`, `filter`, `truck`, `arrows-exchange`
Ecology / environment : `recycle`, `leaf`, `droplet`, `flame`, `bolt`, `fish`, `planet`, `solar-panel`, `tree`, `seedling`
Process / data : `chart-bar`, `chart-line`, `arrows-shuffle`, `refresh`, `settings`
Impact / people : `users`, `heart`, `trophy`, `award`, `school`
Logistics : `ship`, `plane`, `route`

---

## 2. POF brand pictos — `/assets/pictos/`

Two files only :

| File | Color | Use |
|---|---|---|
| `pof-picto-color.svg` | Teal `#80C7C2` | Mark on light backgrounds |
| `pof-picto-white.svg` | White | Mark on dark backgrounds |

POF brand symbol (waves stacked). Use cases : favicon, loading state, decorative corner mark, internal asset.

**NOT a UI icon.** Do not place inline in body text.

---

## 3. Archived (out of scope)

- `assets/icons/_archived/ecology/` — 32 SVG with stroke-width 28 (too thick vs Tabler style). Kept for reference, not used.
- `assets/icons/_archived/environment/` — 138 SVG, archived in v3.3.5.

These can be un-archived if a future need justifies it.

---

## Size guide

| Use case | Render size |
|---|---|
| Feature card icon | 0.6 × 0.6" (rasterize at 256px for PPTX) |
| Inline header icon | 0.4 × 0.4" |
| Full-width hero icon | 1.0 × 1.0" |
| Process step icon | 0.5 × 0.5" |
| Web (HTML/CSS) | 24 × 24 px to 64 × 64 px |

---

## Forbidden

- Drawing custom SVG icons inline (use Tabler CDN)
- Coral `#E8546C` for icons (emphasis only)
- Adding shadow / drop-shadow / blur / filter on icons
- Using brand picto as a UI icon
- Stretching, rotating, distorting icons
- Mixing different icon families in the same row / context (visual inconsistency)
