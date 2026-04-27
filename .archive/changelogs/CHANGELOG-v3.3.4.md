# CHANGELOG v3.3.4 — Design System POF

**Date :** 2026-04-27
**Statut :** Patch — body sizes per medium explicit in typography.scale

## Source feedback

User feedback Claude Design preview 2026-04-27 : la "Body Type Scale" affichait UNE seule taille body (16px / 12pt = web), masquant la distinction critique entre slides (22pt) et print (11pt). Conséquence : Claude Design risque d'utiliser 16px partout, ignorant la cible medium.

## Patches

### `typography.scale` — 2 entrées body explicites

Ajout de :
- `body_slide` : 30px / 22pt — body slides (V2 template, lecture à 3m)
- `body_print` : 15px / 11pt — body print / DOCX A4 (lecture à 25cm)

Existing :
- `md` : 16px / 12pt — body web (default browser)

Les 3 sizes sont désormais visibles dans le preview Claude Design comme entrées séparées de la scale.

### `typography.body_variants` — 3 entrées au lieu de 2

Avant : `body_screen` (12pt) + `body_print` (11pt)
Après : `body_slide` (22pt) + `body_print` (11pt) + `body_web` (12pt)

Plus précis sur la cible medium.

### CSS variables

- `--pof-fs-body-slide: 30px` — pour les slides
- `--pof-fs-body-print: 15px` — pour le print

### Documentation

`docs/DESIGN.md` "Per-medium typography" table mise à jour : la ligne body référence explicitement les 3 noms de tokens (`body_slide`, `body_print`, `body_web`).

### Versions
- `tokens/brand-tokens.json` v3.3.4
- `tokens/brand-rules-per-format.json` v3.3.4
- `tokens/brand-tokens.css` (2 vars ajoutées)
- `docs/DESIGN.md` v3.3.4
- README + ASSETS/MAPS/CHARTS/ICONS bumped to v3.3.4

## Effet attendu

- Preview Claude Design "Body Type Scale" affichera désormais 3 lignes body (slide / print / web) au lieu d'une seule
- Claude Design choisira automatiquement le bon body selon le medium demandé (PPTX → body_slide 22pt, DOCX → body_print 11pt, HTML → body_web 16px)
- Cohérence avec slides.font_size_mapping (déjà 22pt) et print_lock (déjà 11pt) — pas de changement de comportement, juste plus visible
