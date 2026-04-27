# CHANGELOG v3.3.9 — Design System POF

**Date :** 2026-04-27
**Statut :** Patch — overlay intensity medium + integrate Graphs & maps catalogue

## Patches

### Overlay intensity 'medium' added

Trois niveaux désormais : `full` (1.0) / **`medium` (0.75)** / `soft` (0.5). Tous finissent transparent à 100%.

Pattern CSS medium :
`linear-gradient(<angle>, rgba(28,31,59,0.75) 0%, rgba(28,31,59,0.75) <hold_pct>%, transparent 100%)`

Use case : photo équilibrée entre dimming fort et léger, contexte préservé tout en gardant un texte lisible.

Combinaisons gradient totales : 4×4×2×3 = **96** (was 64).

### Catalogue Graphs & maps intégré

Output du projet Claude Design Graphs & maps poussé dans le repo :
- `examples/charts/16-map.html` (936 lignes) — page maps complète avec patterns + crops régionaux
- `examples/charts/17-icons.html` — POF Tabler shortlist 106 icônes × 3 variants navy/teal/white via CDN
- `examples/charts/18-images.html` — page images avec live photos Notion DB + sections types/overlays/text rules/forbidden
- `examples/charts/Tableaux-financiers.html` — variante tables financières
- `examples/charts/index.html` mis à jour avec sections (Data viz / Stat / Structure / Data display / Geo / Library)

Photos dans 18-images.html servies via Google Drive (`lh3.googleusercontent.com`) résolues depuis la Notion DB. Pipeline confirmé fonctionnel.

### Versions
- tokens v3.3.9
- README + DESIGN + MAPS + CHARTS + ICONS + ASSETS bumped to v3.3.9
