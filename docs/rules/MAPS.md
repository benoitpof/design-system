# MAPS.md — POF Map System

**Version:** 1.0 | **Updated:** 2026-04-26 | **Design system:** v3.3.0
**Source of truth:** `assets/maps/pof-world-map-blank.svg` (175 country paths, ISO-2/3 IDs, group metadata)
**Interactive reference:** `assets/maps/map-charter.html` (visual examples of all 5 patterns)

POF cartographic system — 5 canonical patterns and rules for geographic visualization across slide / web / print.

---

## 5 canonical patterns

| Pattern | Use | Data type |
|---|---|---|
| 1. Heatmap | Concentration / density per country (gradient) | Continuous value per country |
| 2. Colored countries (categorical) | Status by country (active / pipeline / etc.) | Discrete category |
| 3. Neutral dots | Locations without data | Presence (yes / no) |
| 4. Data dots (proportional) | Magnitude per location | Quantitative value |
| 5. Faded-edge anchored | Decorative map anchored to slide edge | None (illustration) |

Patterns can combine : categorical + data dots + region overlays.

---

## Pattern 1 — Heatmap (continuous gradient)

**3 navy variants are documented** in `map-charter.html` (N1, N2, N3) — pick the one closest to data distribution :

| Variant | 5 stops | Use |
|---|---|---|
| N1 navy | `#F9FCFF → #CFD9E0 → #80C7C2 → #435D74 → #1C1F3B` | Standard heatmap (linear distribution) |
| N2 (TBD) | spec in `map-charter.html` | Skewed-low data |
| N3 (TBD) | spec in `map-charter.html` | Skewed-high data |

Stroke between countries : `#FFFFFF` 0.8 pt. No-data fill : `#EAEBED`.

Legend horizontal bar : 5 stops, 120 × 8 mm, value labels at extremes.

---

## Pattern 2 — Colored countries (categorical)

| Status | Fill | Description |
|---|---|---|
| Active deployment | `#1C1F3B` | Operational POF deployment |
| Pipeline | `#435D74` | Engaged project, not yet operational |
| Featured / interest | `#80C7C2` | Strategic priority |
| Context | `#EAEBED` | Regional context |
| No data | `#F9FCFF` | Out of scope |

Stroke : `#FFFFFF` 0.8 pt. Default rendering : flat solid fills, no gradient (data clarity > decoration).

---

## Pattern 3 — Neutral dots (presence)

```
<circle cx cy r="6" fill="#1C1F3B" stroke="#FFFFFF" stroke-width="1.5"/>
```

Fixed diameter 12 px at viewBox 2418×1248. Optional label to the right : Raleway Regular 11 pt navy.

---

## Pattern 4 — Data dots (proportional sizing)

```
r = sqrt(value / max_value) × R_max
R_max ∈ [12, 36] px at viewBox 2418×1248
```

Circle : fill `#1C1F3B`, stroke `#FFFFFF` 1.5 pt. Inside label : Raleway Bold white, font-size = `clamp(9pt, r/3, 18pt)`. Outside label (country name) : Raleway Regular 11 pt navy, right or below.

POF reference scales :
- Tonnes / year : 0–100 → 8–20 px
- Jobs created : 0–200 → 8–24 px
- Factories deployed : 0–10 → 12–32 px

---

## Pattern 5 — Faded-edge anchored

Maps must NEVER float centered. Always anchor to a slide edge with gradient fade toward the opposite side.

| Anchor | Map placement | Gradient direction (white → transparent) |
|---|---|---|
| right | x covers right half | `90deg, white 0% → transparent 60%` |
| left | x covers left half | `270deg, white 0% → transparent 60%` |
| top | y covers top half | `0deg, white 0% → transparent 60%` |
| bottom | y covers bottom half | `180deg, white 0% → transparent 60%` |
| full-bleed | full content zone | overlay only — no fade |

Map opacity in faded mode : 50 % (`alpha=0.5` or `<a:alphaModFix amt="50000"/>` in PPTX).

Forbidden : map floating centered with empty whitespace on all sides. The fade-anchor pattern is what gives the POF map signature feel.

---

## Region overlays (optional, on any pattern)

Dashed ellipses around country clusters to highlight a region.

```svg
<ellipse cx cy rx ry fill="none"
         stroke="#1C1F3B" stroke-width="1.5"
         stroke-dasharray="6 4" stroke-linecap="round"/>
```

Region label : Raleway SemiBold 14 pt coral `#E8546C`, UPPERCASE, letter-spacing 1 px, positioned above the ellipse.

**Canonical regions for POF v3.2.6 :**

| Code | Label | Members (ISO-2) |
|------|-------|-----------------|
| `WEST_AFRICA_REGION` | West Africa | SN, ML, BF, NE, NG, CI, GH, TG, BJ, GN, SL, LR, MR, GW, GM, CV |
| `EAST_AFRICA_INDIAN_OCEAN` | East Africa & Indian Ocean | KE, TZ, UG, RW, BI, ET, SO, ER, DJ, SS, SD, MG, KM, MU, SC, MZ, MW, ZM, ZW |
| `SOUTH_EAST_ASIA` | South-East Asia | MM, TH, LA, VN, KH, MY, SG, BN, ID, PH, TL |

Group definitions are also embedded as JSON `<metadata id="pof-map-groupings">` in `pof-world-map-blank.svg`. Use `data-groups` attribute on country `<path>` to filter programmatically.

---

## Legends — on-map AND off-map

To stay consistent with charts in `examples/charts/`, maps reuse the same legend pattern.

### On-map legend (compact)
- Position : bottom-left by default (or wherever the fade anchor leaves space)
- Background : `rgba(255,255,255,0.85)` (semi-transparent white)
- Padding : 6 mm
- Border-radius : 4 px
- Max items : 4 (more = move legend off-map)

### Off-map legend (vertical, beside the map)
- Position : right of the map, vertically centered
- Width : 60 mm
- Items : dot indicator 8 px + Raleway Regular 11 pt navy label + optional Raleway Light 9 pt italic sub-label
- Gap between items : 8 mm

Legend strict limit (per POF brand guideline) : **maximum one legend type per slide**. If both color category and dot size are encoded, use ONE legend that explains both, never two separate legends.

---

## Anchoring rules — slide layouts

A map MUST anchor to at least one edge of the content zone. Five canonical configurations :

| Config | Map zone | Side panel | Use case |
|---|---|---|---|
| Right anchor | x = 10..18.95 in | x = 1.05..9 in (left) | L09 with KPIs left |
| Left anchor | x = 1.05..10 in | x = 10..18.95 in | L09 with text right |
| Top anchor | y = 2..6.5 in | y = 6.5..10.8 in | KPIs below |
| Bottom anchor | y = 6.5..10.8 in | y = 2..6.5 in | Title + context above |
| Full-bleed | full content zone | overlay only | L02 section divider |

A map never floats centered with empty space on all sides.

---

## Cross-medium compatibility (web / PowerPoint / print)

POF brand requires identical visual rendering across web, slide, and print outputs. To ensure this :

| Constraint | Rationale |
|---|---|
| All map fills are flat solid (no CSS gradients on country paths) | PowerPoint and PDF export do not always preserve CSS gradients |
| Heatmap stops are pre-computed solid fills (5 discrete steps), not continuous interpolation | Stable across renderers |
| Photo overlay gradient (Pattern 5 fade) is the ONLY gradient in maps | Pre-rasterize when exporting to PPTX if rendering issue |
| Stroke widths in `pt` and `px` (no `mm`) | Consistent stroke perception |
| Fonts referenced as Poppins / Raleway with web fallback `sans-serif` | Print-safe font cascade |
| No drop-shadow, no filter, no blur on any map element | Cross-renderer guaranteed |
| Region ellipses use `stroke-dasharray` (renderer-agnostic) | Avoid CSS-only dash patterns |

When exporting a map to PPTX : rasterize the SVG to PNG at 2× resolution if any gradient or alpha is used. Embed PNG at slide size.

---

## Hard locks reminder (v3.2.5)

- Colors : canonical palette only. No `#FF5A60` for region labels (use `#E8546C`).
- Sizes (pt) : `[9, 11, 14, 18, 22, 26, 36]` + stat-only `[72, 120]`. No 10 pt, 12 pt, 13 pt.
- Weights : `[300, 400, 600, 700]`. No 500.
- No filter, no drop-shadow, no opacity reduction on corner brackets.
- Map opacity 50 % allowed ONLY in Pattern 5 anchored mode.

---

## File reference

| File | Use |
|---|---|
| `assets/maps/pof-world-map-blank.svg` | Source of truth — vector base |
| `assets/maps/pof-world-map-annotated.svg` | Same base + priority labels |
| `assets/maps/svg/01-monde.svg` | 7 pre-cropped regional views (01 = vector, 02-07 = PNG-embedded pending vectorization) |
| `assets/maps/png-source/*.png` | High-res raster source for regional views |
| `assets/maps/map-charter.html` | Interactive visual charter |
| `assets/maps/USAGE.md` | Use case guide for the 7 regional crops |
| `assets/maps/POF-WORLD-MAP-GUIDE.md` | Country IDs and groups |
| `assets/maps/_map-data.js` | JS helpers |

---

## Memory — capitalisation Rex (v3.4.0)

<!-- ds-iterate écrit ici. Format : ### YYYY-MM-DD — <titre> -->

(vide pour l'instant)
