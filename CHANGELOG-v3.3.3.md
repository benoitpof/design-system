# CHANGELOG v3.3.3 — Design System POF

**Date :** 2026-04-27
**Statut :** Patch — scope reduction + clean-up palette + 26pt slide_title

## Patches

### Scope : POF Factories only

Académy et Sunu PO retirés du design system (décision Benoit 2026-04-27).

Removed :
- `tokens/brand-tokens.json` `entity_overrides.academy`
- `tokens/brand-tokens.json` `entity_overrides.sunu_po`
- `tokens/brand-tokens.css` `--pof-academy-*` variables
- `tokens/brand-tokens.css` `--pof-sunu-*` variables (si présentes)
- `README.md` section "Entity defaults" remplacée par "Entity scope" simple
- `docs/DESIGN.md` mentions Academy / Sunu retirées du brand DNA

### Palette clean-up

Removed :
- `colors.semantic.info` `#0D6EFD` — unused, simplifie la palette sémantique (success, warning, error suffisent)
- `colors.neutral.near_black` `#090911` — redondant avec navy `#1C1F3B`
- CSS vars `--pof-info` et `--pof-near-black`

### Typography scale

Ajout de `slide_title` (26pt / 35px) dans `typography.scale` entre `xl` (18pt) et `2xl` (21pt).

Justification : 26pt est la taille la plus utilisée sur les slides POF (titre + sous-titre par V2 template), mais absente de la scale harmonique. Visualisée correctement dans les preview cards Claude Design désormais.

Ajout CSS var `--pof-text-slide-title: 35px` dans `brand-tokens.css`.

### Versions
- `tokens/brand-tokens.json` v3.3.3
- `tokens/brand-rules-per-format.json` v3.3.3
- `tokens/brand-tokens.css` (vars retirées + ajoutée)
- `README.md` v3.3.3
- `docs/DESIGN.md` v3.3.3
- ASSETS / MAPS / CHARTS / ICONS headers v3.3.3
