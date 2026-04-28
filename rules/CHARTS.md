# CHARTS.md — POF Chart System

**Version:** 1.0 | **Updated:** 2026-04-26 | **Design system:** v3.3.0
**Catalog:** `examples/charts/` — 16 templates HTML + CSS, browse `index.html` for navigator
**Source styling:** `examples/charts/styles.css`

---

## Catalog (16 templates)

| ID | File | Type | Use |
|----|------|------|-----|
| 01 | `01-kpi.html` | KPI / big number | Headline metric, 1 to 3 callouts |
| 02 | `02-bar.html` | Bar chart vertical | Magnitude comparison, time series 5–8 points |
| 03 | `03-stacked.html` | Stacked bar | Component breakdown across categories |
| 04 | `04-grouped.html` | Grouped bar | Multi-series comparison, max 3 series |
| 05 | `05-line.html` | Line chart | Time series, trend, max 3 lines |
| 06 | `06-donut.html` | Donut | Composition, max 5 slices |
| 07 | `07-progress.html` | Progress bars | Completion rates, multi-objective tracking |
| 08 | `08-funnel.html` | Funnel | Pipeline conversion, 4–6 stages |
| 09 | `09-timeline.html` | Timeline | Milestones, dated events |
| 10 | `10-gantt.html` | Gantt | Project schedule, dependencies |
| 11 | `11-sankey.html` | Sankey | Flow / mass balance, max 8 nodes |
| 12 | `12-process.html` | Process flow | Sequential steps, max 6 |
| 13 | `13-org.html` | Org chart | Hierarchy, max 3 levels |
| 14 | `14-table.html` | Financial tables | P&L, balance sheet, cash flow, CAPEX |
| 14b | `14-table-v1.html` | Comparison table | Specs comparison, options, scenarios |
| 14c | `Tableaux-financiers.html` | Financial tables variant | P&L FR variant, multi-currency, scenarios |
| 15 | `15-radar.html` | Radar | Multi-criteria assessment, max 6 axes |

For maps, see separate `rules/MAPS.md`.

---

## Mandatory elements (every chart)

| Element | Spec |
|---------|------|
| Title | Poppins SemiBold 22 pt navy, left-aligned, max 1 line |
| Subtitle (optional) | Raleway Regular 14 pt steel, max 1 line |
| Y-axis labels | Raleway Regular 11 pt `#6C757D` |
| X-axis labels | Raleway Regular 11 pt `#6C757D` |
| Data labels (when shown) | Raleway SemiBold 11 pt navy |
| Legend (only if ≥ 2 series) | Raleway Regular 11 pt navy, dot indicators 8 px |
| Source caption | Raleway Light 9 pt `#435D74` italic, bottom-left |

---

## Legend rules

- **Maximum one legend per chart.** If both color and size encode meaning, merge into one combined legend.
- Legend position : right of chart (off-chart) preferred. On-chart only if space-constrained.
- Items max : 5. Beyond, collapse into "Other" or split chart.
- Format identical across all chart types and maps for visual consistency.

---

## Color palette per chart type

POF chart palette (in token : `tokens/brand-tokens.json` `chart_palette`) :

| Series | Color | When |
|---|---|---|
| series_1 | `#1C1F3B` navy | Primary |
| series_2 | `#435D74` steel | Secondary |
| series_3 | `#CFD9E0` light steel | Tertiary |
| series_4 (extended) | `#80C7C2` teal | Only if 4+ series |
| series_5 (extended) | `#E8546C` coral | Only if 5+ series, used sparingly |
| series_6 (last resort) | `#6C757D` gray | If 6+ series unavoidable |

If chart needs > 6 series, redesign : group tail into "Other" or split into multiple charts.

---

## Forbidden

- Gridlines (use whitespace for separation)
- Chart borders / outlines around the plot area
- 3D effects, perspective, depth shading
- Drop shadows beyond `0px 4px 12px rgba(0,0,0,0.15)` (and even this rare on charts)
- Auto color schemes from chart libraries (Plotly default, Chart.js default, Excel default)
- Pie chart with > 5 slices
- Coral as text body fill
- Two distinct legends on one chart
- Animated transitions when exporting to print / PPTX

---

## Cross-medium compatibility (web / PowerPoint / print)

POF brand requires identical rendering across all output media. Constraints :

- Use solid fills only on data series (no CSS gradients on bars / lines / dots)
- Use Raleway and Poppins web fonts with `sans-serif` fallback for print safety
- Stroke widths in `pt` (matches PowerPoint pt scale)
- Avoid CSS-only effects (`backdrop-filter`, `mix-blend-mode`, `mask-image`) — these break in PPTX export
- When exporting a chart to PPTX, prefer rasterizing the chart canvas to PNG at 2× resolution rather than pasting an inline SVG (PowerPoint SVG support is unreliable on Office 2016 and Mac variants)
- For print : ensure stroke widths ≥ 0.25 pt to avoid disappearing on 300 dpi PDF export

---

## Catalog usage workflow

1. Browse `examples/charts/index.html` to find the closest template
2. Copy the HTML+CSS of the chosen template
3. Replace data + labels (no styling change)
4. Validate output against the QA checklist in `rules/HARD-LOCKS.md`
5. If a chart variant is needed that is not in the catalog : propose addition to v3.2.x as a new file `examples/charts/NN-name.html`, never inline a one-off

The catalog is the source. Single chats producing one-off charts must NOT be the norm.

---

## Hard locks reminder (v3.2.5)

- Sizes (pt) : `[9, 11, 14, 18, 22, 26, 36]`. No 10 / 12 / 13.
- Weights : `[300, 400, 600, 700]`. No 500.
- Colors : canonical palette + chart_palette extensions only.
- No shadow on chart elements (except subtle drop shadow on stat callout if needed, max 12px blur).

---

## Memory — capitalisation Rex (v3.4.0)

<!-- ds-iterate écrit ici. Format : ### YYYY-MM-DD — <titre> -->

(vide pour l'instant)


## Patch v3.4.0 — règles ajoutées suite feedbacks

### Multi-series palette (CRITICAL)

**Règle :** séries multiples utilisent un spectre navy → gris. Teal et coral réservés au highlight (1-2 séries max), jamais dans la séquence par défaut.

**Sequence par défaut (jusqu'à 6 séries) :**
```
series_1 : #1C1F3B  navy
series_2 : #253560  navy_medium
series_3 : #435D74  steel
series_4 : #5F7D95  steel_light
series_5 : #8AAFC4  steel_pale
series_6 : #CFD9E0  steel_palest
```

**Highlight only (jamais dans la séquence par défaut) :**
- Teal `#80C7C2` ou `#2BA595` : pour 1 série à mettre en avant
- Coral `#E8546C` : pour 1 KPI critique unique

**Logique d'ordre :** assignation par logique sémantique (géographique, temporelle, taille). Pas d'ordre arbitraire.

### Éléments interdits à l'intérieur d'un chart (CRITICAL)

Les éléments suivants appartiennent au layout slide, pas au chart. **Jamais à l'intérieur d'un SVG chart :**
- `corner_mark` (L-bracket teal)
- `eyebrow_accent_line` (trait teal horizontal sous l'eyebrow)
- `pipe_accent` (barre verticale teal à gauche du titre)
- Logo overlay

Le chart doit rester autonome et réutilisable cross-medium (deck, web, print).

### Validation données source (CRITICAL)

Pour les charts avec données source identifiées (OECD, World Bank, IFC, etc.) :

1. **Respecter strictement les valeurs.** Tolérance max : 1% sur sommes et multiplicateurs.
2. **Phase de validation obligatoire avant génération** : refuser si écart > 1% vs source.
3. **Interpolation temporelle** : préférer points réels disponibles. Si interpolation nécessaire, utiliser monotone (Akima/PCHIP) pas exponentielle pure.
4. **`meta.json` du livrable** doit indiquer : source URL, date publication, méthode interpolation, points utilisés.

### Charts denses (>8 séries)

1. Palette navy → gris stricte (pas de couleur ajoutée)
2. Réduire épaisseur des connecteurs
3. Espacement dynamique anti-overlap pour les labels
4. Si > 12 séries : grouper en "Other" ou splitter en plusieurs charts
