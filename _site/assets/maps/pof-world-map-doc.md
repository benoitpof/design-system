# POF World Map — `pof-world-map.svg`

## Overview

Self-contained SVG world map asset for Plastic Odyssey Factories (POF) design system.
Built from **Natural Earth 110m admin_0_countries** data, projected in **Robinson**.

- **Version**: 1.0.0  
- **Date**: 2026-04-26  
- **Source**: Natural Earth 110m (public domain)  
- **Projection**: Robinson (`+proj=robin +lon_0=0`)  
- **Dimensions**: 2418 × 1248 px (slide L09 full-bleed @ 2×)  
- **Countries**: 177  
- **Labels**: 78 (12 priority, 66 secondary)

---

## File structure

```
assets/maps/
├── pof-world-map.svg          # Source SVG (this file)
└── pof-world-map-doc.md       # This documentation
```

---

## Country identification

Each country `<path>` carries:

| Attribute | Content |
|-----------|---------|
| `id` | `c-{ISO2}` — e.g. `c-SN`, `c-NG`, `c-ID` |
| `data-iso2` | ISO 3166-1 alpha-2 code |
| `data-iso3` | ISO 3166-1 alpha-3 code |
| `data-name` | English name (Natural Earth) |
| `data-continent` | Continent string |
| `data-subregion` | Subregion string |
| `data-groups` | Space-separated group keys (see below) |

### Selection example

```js
// Select Nigeria
document.getElementById('c-NG')

// Select all UEMOA members
document.querySelectorAll('[data-groups~="UEMOA"]')

// Select all West Africa region countries
document.querySelectorAll('[data-groups~="WEST_AFRICA_REGION"]')
```

---

## Groups / Ensembles

Stored in `<metadata id="pof-map-groupings">` as JSON, and applied via `data-groups` on each path.

| Key | Name (FR) | Members |
|-----|-----------|---------|
| `UEMOA` | UEMOA | BF, BJ, CI, GW, ML, NE, SN, TG |
| `CEDEAO` | CEDEAO / ECOWAS | 15 membres (Afrique de l'Ouest) |
| `UA` | Union Africaine | 55 membres |
| `EU` | Union Européenne | 27 membres |
| `ASEAN` | ASEAN | BN, KH, ID, LA, MY, MM, PH, SG, TH, VN |
| `ACP` | ACP | ~79 pays Afrique-Caraïbes-Pacifique |
| `WEST_AFRICA_REGION` | Afrique de l'Ouest | Région prioritaire POF |
| `EAST_AFRICA_IO_REGION` | Afrique de l'Est & Océan Indien | Région prioritaire POF |
| `SEA_REGION` | Asie du Sud-Est | Région prioritaire POF |

---

## Priority countries (labels in bold)

These 12 countries carry bold Poppins 11px labels — they are POF's primary deployment targets or key countries of interest:

`SN` Sénégal · `GN` Guinée · `CI` Côte d'Ivoire · `CM` Cameroun · `NG` Nigeria  
`KE` Kenya · `MA` Maroc · `ID` Indonésie · `PH` Philippines  
`MG` Madagascar · `MU` Île Maurice · `RW` Rwanda

---

## Usage in Claude Design

### Color states (via CSS class or inline fill override)

| State | Fill | Usage |
|-------|------|-------|
| Inactive (default) | `#EAEBED` | Countries not in focus |
| Pipeline | `#435D74` (steel) | Countries in deployment pipeline |
| Active / deployed | `#1C1F3B` (navy) | Countries with active factory |
| Highlight | `#80C7C2` (teal) | Hover / selected |

```html
<!-- Example: highlight Nigeria as active -->
<style>
  #c-NG { fill: #1C1F3B; }
  #c-SN { fill: #435D74; }
</style>
```

### Adding factory dots

```html
<!-- Dot on Dakar, Sénégal -->
<!-- Compute SVG coordinates from lon/lat using Robinson projection -->
<circle cx="912" cy="400" r="6" fill="#80C7C2" aria-label="Dakar — Sénégal"/>
```

---

## Projection details

**Robinson** (`+proj=robin +lon_0=0 +x_0=0 +y_0=0 +datum=WGS84 +units=m`)

- Scale: `0.0001 px/m`
- SVG origin: top-left corner = northwest of bounding box
- Y axis: inverted (SVG convention, south = higher y value)

To convert lon/lat to SVG pixel coordinates (Python):
```python
from pyproj import Transformer
t = Transformer.from_crs("EPSG:4326",
    "+proj=robin +lon_0=0 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs",
    always_xy=True)
x_proj, y_proj = t.transform(lon, lat)
svg_x = x_proj * 0.0001 + 1209.0
svg_y = -y_proj * 0.0001 + 491.7
```

---

## Design system compliance

- Colors: POF palette only (`#EAEBED`, `#435D74`, `#1C1F3B`, `#80C7C2`, `#FFFFFF`)
- Fonts: Poppins (priority labels, 11px 600) · Raleway (secondary labels, 8px 400)
- No gridlines · No chart borders · No drop shadows
- Stroke: `#FFFFFF` 0.6px between countries

