# CHANGELOG v3.3.5 — Design System POF

**Date :** 2026-04-27
**Statut :** Major patch — multi-feedback consolidation

## Source feedback

User feedback du 2026-04-27 — synthèse des reviews Claude Design + maps + buttons + gradient.

## Patches

### Buttons Ghost — hiérarchie corrigée

Avant : Ghost border navy + text navy (équivalent visuel à Primary)
Après : Ghost = lowest emphasis variant.
- Light : border #435D74 (steel) + text steel, hover bg #CFD9E0
- Dark : border #5F7D95 (light-steel) + text light-steel, hover bg white 8%
- Hierarchy : Primary > Secondary > Danger > Ghost

Bloc `components.button_ghost` ajouté dans `tokens/brand-tokens.json`.

### Navy depth gradient — itération finale (5e passe)

Avant : `linear-gradient(180deg, #1C1F3B 0%, #80C7C2 100%)` (navy → solid teal vertical)
Après : `linear-gradient(45deg, rgba(128,199,194,0.38) 0%, rgba(128,199,194,0) 60%), #1C1F3B` (teal glow from bottom-left, transition to fully transparent at 60%, on solid navy base, teal final opacity 38%)

Effet : "coin lumineux" subtil en bas-gauche, navy solide ailleurs. Plus institutionnel que le dégradé vertical.

### World basemap nouveau master — `00-monde-cropped.svg`

Crop sur les 2 axes :
- x ≥ 950 : Americas dropped
- y ≤ 1000 : Antarctica dropped

148 pays, no labels (text stripped). 3 fades baked-in (g_BT, g_LR, g_TB) pour anchors top, left, bottom.

ViewBox : `950 0 1468 1000`. Stocké dans `assets/maps/svg/00-monde-cropped.svg`.

### Heatmap palettes — formalisation

Bloc `maps_lock.heatmap_palettes` avec 4 variantes :
- N1 (default white→navy)
- N2 (neutral gray→navy)
- N3 (steel→navy, skewed-high data)
- **T1 (teal-only)** — NEW v3.3.5. 4 stops `#F1FBFA → #80C7C2 → #2BA595 → #09414A`. Pour Pattern 1 + R3 regional Indian Ocean.

### Maps fade rules

Bloc `maps_lock.fade_rules` formalisé :
- `no_overlap_with_colored`: true — fade ne couvre jamais countries colorés ou dots
- `legend_z_order`: top — légende toujours rendue last, jamais sous le fade
- `fade_start_at_viewbox_edge`: gradient START coordinate = viewBox edge

### Environment icons archivés

`assets/icons/environment/` → `assets/icons/_archived/environment/`. Retiré du scope actif. Réversible.

### Versions
- `tokens/brand-tokens.json` v3.3.5
- `tokens/brand-rules-per-format.json` v3.3.5
- `tokens/brand-tokens.css` (Ghost vars + navy-depth refined)
- `assets/maps/svg/00-monde-cropped.svg` (NEW)
- `assets/icons/environment/` → `_archived/`
- README + ASSETS/MAPS/CHARTS/ICONS bumped to v3.3.5
