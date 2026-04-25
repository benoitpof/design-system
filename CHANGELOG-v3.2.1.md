# CHANGELOG v3.2.1 — Design System POF

**Date :** 2026-04-25
**Statut :** Push initial GitHub `benoitpof/design-system`.

---

## Corrections critiques

### `tokens/brand-rules-per-format.json` — bloc `slides` réécrit
- **Avant :** dimensions 254×190.5 mm (4:3, ratio incorrect, vestige du Google Slides standard).
- **Après :** dimensions 508×285.75 mm (16:9, LAYOUT_WIDE), vérifié depuis `Template POF - Claude.pptx` XML (`cx=18288000 cy=10287000` EMU).
- **Impact :** content_zone, header, logo, footer, corner marks ré-ancrés sur le bon canvas. Coordonnées contradictoires éliminées entre LAYOUTS.md et brand-rules.
- Suppression de `header_bar` (DESIGN.md interdit déjà les bandeaux pleine largeur sous les titres).
- Ajout des clés `title_zone`, `subtitle_zone`, `pipe_accent`, `corner_marks`.
- Convention de coordonnées : **mm partout (SSOT)**. Inches conservés dans `_inches` pour pptxgenjs.

### `docs/DESIGN.md` §4 — anchors content zone
- **Avant :** `Content zone: x=1.051 y=2.0 to edge 18.949 x 9.0` (typo : `9.0` au lieu de `max-h=8.8`).
- **Après :** tableau dual-unit (mm + inches) explicite, avec marges symétriques L/R = 26.7 mm.

### `docs/LAYOUTS.md` — global anchors dual-unit
- Ajout des coordonnées mm en miroir des inches existantes pour chaque ancrage global.
- Bloc « zone utile (safe zone) » explicité : marges, top header, bottom footer.

### `tokens/brand-tokens.json` — `logo_lockup.slide_position`
- **Avant :** x=224 y=4 w=26 h=12 mm (basé sur 4:3 obsolète).
- **Après :** x=421.3 y=20.6 w=64.5 h=16.4 mm (LAYOUT_WIDE 16:9, vérifié XML).

### Versions alignées
- README.md, brand-tokens.json, brand-rules-per-format.json, DESIGN.md → tous v3.2.1.

---

## Décisions reportées (non bloquantes)

- **15 layouts annoncés vs 12 dans le master XML Google :** écart à valider lors de la prochaine itération PowerPoint réelle (Étape 2 roadmap).
- **L11–L15 :** marqués 🔄 DRAFT. Pas encore générés en pptxgenjs.
- **Conversion exhaustive des coordonnées des layouts L01–L15 en mm :** non réalisée dans ce commit. Les inches restent la convention dans LAYOUTS.md (pour pptxgenjs natif), avec mm en commentaire pour les global anchors. À harmoniser si SSOT mm devient strict.

---

## Vérifié contre

- `Template POF - Claude (1).pptx` ppt/presentation.xml (canvas 16:9)
- `Template POF - Claude (1).pptx` ppt/slideMasters/slideMaster1.xml (placeholders title/body/footer)
- `docs/LAYOUTS.md` global anchors (cohérence inches inchangée)
