# CHANGELOG v3.2.5 — Design System POF

**Date :** 2026-04-26
**Statut :** Hotfix doc — règle explicite « no shadow on corner marks »

## Patch

### Règle explicite : aucune ombre sur les corner brackets

Audit du repo : aucune ombre détectée dans les 5 SVG `corner-bracket-*.svg`, ni dans la spec `slides.corner_marks` de `brand-rules-per-format.json`. Les assets sont propres.

**Mais** la règle n'était pas documentée explicitement → risque que Claude Design (HTML artifact, CSS local, PowerPoint shape effect) en ajoute une à la rendition.

Patches appliqués :

**`tokens/brand-rules-per-format.json` `slides.corner_marks`** :
- Nouveau flag `shadow_forbidden: true`
- Nouveau bloc `effects_forbidden` listant : drop-shadow, inner-shadow, filter:blur, filter:drop-shadow, PowerPoint shape shadow, CSS opacity < 1
- Nouveau champ `rendering_rule` : « Render as flat L-bracket strokes only. No depth effect of any kind. Brand mark is geometric, not skeuomorphic. »
- `_violation_examples` étendu

**`docs/DESIGN.md` § Hard locks** :
Section « Corner marks lock » étoffée avec un paragraphe « No shadow, ever » couvrant CSS drop-shadow, PowerPoint shape effects, opacity reductions, blur — quel que soit le medium de rendu.

### Versions
- `tokens/brand-tokens.json` v3.2.5
- `tokens/brand-rules-per-format.json` v3.2.5
- `README.md` v3.2.5
- `docs/DESIGN.md` v3.2.5

## Vérification

```bash
# Aucune ombre dans les SVG
grep -ciE "filter|shadow|blur|opacity" assets/brand-elements/corner-bracket-*.svg
# La règle est bien documentée
grep -c "shadow_forbidden" tokens/brand-rules-per-format.json
grep -c "No shadow, ever" docs/DESIGN.md
```

## À ajouter dans le bloc « Any other notes » de Claude Design

```
Corner marks (L-brackets) NEVER have shadow, drop-shadow, blur, opacity < 1, or any depth effect. Render exactly as the SVG: flat teal strokes, transparent background. Whether the medium is slide, web, artifact, or report — no exception.
```
