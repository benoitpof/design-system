# CHANGELOG v3.3.8 — Design System POF

**Date :** 2026-04-27
**Statut :** Patch — Overlay gradient intensity added

## Source feedback

User 2026-04-27 : « Je ne vois pas l'overlay qui part de 50% transparence et va à 100% de transparence ».

## Patch

### `overlay_system.gradient.intensity` — 2 niveaux

Avant : tous les gradients commençaient à 100% opaque dans la zone hold.
Après : 2 intensités possibles, toutes deux finissent à 100% transparent :

- **`full`** (default) : start_opacity 1.0 — `linear-gradient(<angle>, #1C1F3B 0%, #1C1F3B <hold_pct>%, transparent 100%)`
- **`soft`** : start_opacity 0.5 — `linear-gradient(<angle>, rgba(28,31,59,0.50) 0%, rgba(28,31,59,0.50) <hold_pct>%, transparent 100%)`

Use case `soft` : photos chaudes où on veut garder le contexte visible à travers le tint (visages, produits).

### Combinations valides

Avant : 4 × 4 × 2 = 32
Après : 4 × 4 × 2 × 2 = **64** combinaisons valides

### Selection rules

Ajout : `warm_photo_with_caption` → `gradient.from_bottom.half.navy_pure.soft`.

### Versions
- tokens/brand-tokens.json v3.3.8
- tokens/brand-rules-per-format.json v3.3.8
- docs/DESIGN.md v3.3.8
- README + ASSETS/MAPS/CHARTS/ICONS bumped to v3.3.8
