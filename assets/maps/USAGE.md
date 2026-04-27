# POF Maps — Usage Guide

> Version: 2.0.0 — 2026-04-26  
> Source: `POF-Maps-Regional-v2-neutre.pptx` + `pof-world-map.svg`

---

## Asset inventory

| File | Region | Base layer | Country coloring | Edge fades |
|------|--------|------------|-----------------|-----------|
| `svg/01-monde.svg` | World (Robinson) | **Vector** (177 paths from `pof-world-map.svg`) | ✅ Full | Left, Top, Bottom |
| `svg/02-asie-du-sud-est.svg` | Southeast Asia | PNG (vector pending) | ⚠️ Overlay group | Left, Top, Bottom |
| `svg/03-afrique.svg` | Africa | PNG (vector pending) | ⚠️ Overlay group | Top (right), Right |
| `svg/04-indonesie.svg` | Indonesia | PNG (vector pending) | ⚠️ Overlay group | Top, Bottom |
| `svg/05-philippines.svg` | Philippines | PNG (vector pending) | ⚠️ Overlay group | Top (right), Bottom (right) |
| `svg/06-afrique-de-louest.svg` | West Africa | PNG (vector pending) | ⚠️ Overlay group | Top (right), Right, Bottom (right) |
| `svg/07-ocean-indien-est.svg` | Indian Ocean & East Africa | PNG (vector pending) | ⚠️ Overlay group | Left, Top (left), Bottom (left) |

---

## SVG layer structure

Every file follows the same 4-layer pattern:

```xml
<svg viewBox="0 0 1920 1080">
  <defs>
    <!-- V2 gradient definitions + optional clipPath -->
  </defs>

  <!-- ❶ White slide background -->
  <rect width="1920" height="1080" fill="white"/>

  <!-- ❷ Base map
       01-monde: inline vector paths (Robinson projection, viewBox = PPTX crop)
       02-07:    PNG <image> element (RGBA, preserveAspectRatio="none") -->

  <!-- ❸ Country color overlay — ADD HIGHLIGHTS HERE
       Insert colored paths/shapes between base map and gradient.
       They are automatically faded by ❹. -->
  <g id="pof-country-overlay" opacity="0.75">
    <!-- country highlight shapes go here -->
  </g>

  <!-- ❹ V2 gradient fades — always last, always on top -->
</svg>
```

---

## Coloring countries

### On 01-monde (vector)

Target paths by ISO 3166-1 alpha-2 code using CSS or JS:

```css
/* CSS — in a <style> block or external sheet */
path[data-iso2="SN"] { fill: #E8546C; }
path[data-iso2="CI"] { fill: #80C7C2; }
```

```js
// JavaScript
document.querySelectorAll('[data-iso2="SN"]')
  .forEach(el => el.setAttribute('fill', '#E8546C'));
```

Or add highlight paths into `#pof-country-overlay` to layer on top of the base:

```xml
<g id="pof-country-overlay" opacity="0.75">
  <path data-iso2="SN" fill="#E8546C"
    d="M 312.4 584.1 L 318.2 ..." />
</g>
```
Path coordinates are in the Robinson projection space of `pof-world-map.svg` (viewBox 0 0 2418 1248).
The world map SVG is cropped via `<svg viewBox="421 47 1936 1010">` — highlight coordinates must be in the **same** projection space (no transform needed).

### On 02-07 (PNG-based, `data-vector="pending"`)

Add simplified shapes into `#pof-country-overlay`. These can be:
- Rectangles or circles approximating a country's bounding area
- Exact paths from `pof-world-map.svg` with a coordinate transform applied
- Dots for point markers

The overlay group sits between the base PNG and the gradient fades, so highlights are automatically estompés at the edges.

```xml
<g id="pof-country-overlay" opacity="0.75">
  <!-- Approximate shape for a West African country -->
  <ellipse cx="720" cy="540" rx="40" ry="55" fill="#E8546C" opacity="0.6"/>
</g>
```

---

## White fade overlay system (type_1_white_fade, v4.0.0)

Map edge fades use fully opaque white → transparent. Four cardinal directions available, cumulation allowed.

| SVG gradient ID | Direction |
|----------------|-----------|
| `g_LR` | Left edge → transparent |
| `g_RL` | Right edge → transparent |
| `g_TB` | Top edge → transparent |
| `g_BT` | Bottom edge → transparent |

Gradient spec: `rgba(255,255,255,1.0)` → `rgba(255,255,255,0)`. `stop-opacity="1"` at the edge stop — **never 0.95**.

**World map defaults (always active):**
- `g_TB` (top): stops at North Africa latitude (~37°N) — prevents Europe from appearing cut
- `g_LR` (left): stops at West Africa coast — prevents Americas edge artifact

To adjust coverage: change `width` or `height` of the `<rect>`.  
Full spec: `tokens/brand-rules-per-format.json` → `overlay_system.type_1_white_fade`.

---

## PNG source files (`png-source/`)

Raw RGBA exports from the original PPTX — no overlay, no crop applied.  
Use as reference or for tools that don't support SVG.

```bash
# Render any SVG at 2× retina
cairosvg svg/01-monde.svg -o 01-monde@2x.png -W 3840 -H 2160
```

---

## PPTX crop parameters (srcRect)

Three regional maps have non-zero crops inherited from the PPTX layout.  
In the SVG these are encoded as `<clipPath>` + offset `<image>` position.

| Map | Left | Top | Right | Bottom | Applied as |
|-----|------|-----|-------|--------|-----------|
| 01-monde | 17.43% | 3.75% | 2.53% | 15.31% | `viewBox` on nested `<svg>` |
| 03-afrique | 0% | 0% | 0% | 5.33% | `<clipPath>` |
| 05-philippines | 4.87% | 0% | 0% | 0% | `<clipPath>` |

---

## Upgrading a regional map from PNG to vector

1. Generate a regional SVG from Natural Earth data at the correct projection
2. Replace the `<image>` element in ❷ with inline `<path>` elements
3. Update `data-vector` attribute from `"pending"` to `"1.0.0"`
4. Paths must share the same coordinate space as `pof-world-map.svg` or use a local projection with documented transform

---

## File naming

```
NN-slug.svg / NN-slug.png
```
- `NN` = 2-digit index (01–07), preserves slide order from `POF-Maps-Regional-v2-neutre.pptx`
- `slug` = kebab-case region name

---

## Sources

- Vector paths: `pof-world-map.svg` v1.0.0 (Natural Earth 110m, Robinson projection)
- PNG exports: `POF-Maps-Regional-v2-neutre.pptx` (design system v3.2.3)
- Projections: Robinson (world), Lambert Equal Area (Africa), national (country-level)
