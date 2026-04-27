# CHANGELOG v3.2.2 — Design System POF

**Date :** 2026-04-25 (patch même jour que v3.2.1)
**Type :** Hotfix brand consistency

## Correction critique

### Couleurs SVG alignées sur tokens canoniques

Les fichiers SVG du repo (`assets/logos/`, `assets/pictos/`, `assets/brand-elements/`, `assets/backgrounds/`) utilisaient des hex non-canoniques en violation directe de `docs/DESIGN.md` ("NEVER use #1D1E3A or #75DBCD").

| Avant (export Illustrator) | Après (canonique tokens.json) |
|---|---|
| `#80c8c3` | `#80C7C2` (teal) |
| `#1d1e3a` | `#1C1F3B` (navy) |
| `#75dbcd` | `#80C7C2` (teal) |

Patch appliqué via `sed -i` sur tous les SVG. Aucune modification géométrique. Delta E perceptuel < 1 (invisible à l'œil), mais alignement strict requis pour la cohérence brand sur tous les canaux (slides PPTX qui échantillonnent les SVG, web Odoo qui les consomme en CSS, etc.).

## Dette à résorber côté design team

**Source de vérité long-terme :** les fichiers Illustrator `.ai` originaux contiennent toujours les anciens hex. Tout nouvel export SVG depuis Illustrator ré-introduira `#80c8c3` et `#1d1e3a`.

**Action design team :**
1. Ouvrir les `.ai` sources
2. Mettre à jour la palette globale Illustrator vers `#1C1F3B` et `#80C7C2`
3. Re-exporter les SVG (les remplacer dans `/assets/`)
4. Confirmer dans le prochain push qu'aucun grep ne ressort plus les anciens hex

Tant que cette action n'est pas faite, tout PR qui ré-importe un SVG depuis Illustrator devra repasser le sed patch. À automatiser via un `pre-commit hook` si nécessaire (cf Sprint 6).

## Vérification

```bash
grep -rE "#80c8c3|#1d1e3a|#75dbcd" assets/   # doit ne rien retourner
```
