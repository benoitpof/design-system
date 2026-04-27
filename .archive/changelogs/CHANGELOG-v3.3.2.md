# CHANGELOG v3.3.2 — Design System POF

**Date :** 2026-04-26
**Statut :** Patch — feedback Benoit sur Position Paper render

## Source feedback

User feedback du 2026-04-26 sur `Position Paper — Plastic Odyssey Factories.pdf` (rendu Claude Design v3.3.1). 6 corrections concrètes :

1. Bleu navy trop clair en haut de la couverture
2. Trop de titres en Teal — Teal est secondaire
3. Sous-titre couverture trop grand
4. Corner mark : juste en haut à gauche, jamais en bas
5. Filigrane vague coupé
6. 4ème de couverture : éviter tout le texte en Teal, white par défaut sur navy

## Patches

### `corner_marks.default_pair` : `top_left` only

Avant : `["top_left", "bottom_right"]` (TL + BR)
Après : `["top_left"]` seul

BR, TR, BL : marqués `FORBIDDEN_BY_DEFAULT — only on explicit request`. La signature POF est désormais le coin supérieur gauche uniquement.

### `color_hierarchy_lock` (nouveau)

Capture la règle « Teal est secondaire » :
- Title default : navy sur fond clair, white sur fond sombre
- Teal max 2 usages par page/slide
- Allowed : accent words slogan, callout border, pipe accent, wave, stat number sur dark, chart series 4+
- Forbidden : title slide, title section, heading body, all text back cover

### `covers_lock` (nouveau)

- Cover title : 36pt MAX, ExtraBold, white sur navy / navy sur clair
- Cover subtitle : **26pt MAX, 22pt recommended**, JAMAIS 28pt+ pour subtitle
- Cover bg : flat navy `#1C1F3B`. Navy depth gradient INTERDIT au top de cover
- Cover wave : MUST be fully visible

### `back_cover_lock` (nouveau)

- Default text color : white
- Teal allowed sur 1 seul élément (typiquement tagline)
- Forbidden : all text en teal

### `wave_decorative_lock` (nouveau)

- Wave watermark MUST be fully visible
- 5 mm margin minimum from any edge

## Documents mis à jour

- `tokens/brand-rules-per-format.json` v3.3.2
- `tokens/brand-tokens.json` v3.3.2
- `docs/DESIGN.md` v3.3.2 (ajout 5 sections locks)
- `README.md` + ASSETS/MAPS/CHARTS/ICONS headers v3.3.2

## Action recommandée

Régénérer le Position Paper avec un nouveau prompt qui inclut explicitement ces 6 règles. Le repo seul ne suffit pas si Claude Design n'a pas accès / ne lit pas — il faut aussi rappeler dans le prompt de session.

## Patches added 2026-04-26 (suite feedback Benoit)

### Gradient direction corrigée
`navy_depth_subtle` : avant `#1C1F3B → #25284A` (navy → lighter navy), après `#1C1F3B → #80C7C2` (navy → teal). Feedback : « Teal vers Navy et pas Navy vers clair ».

### `print_lock` ajouté — distinction format slides vs print
- Slides body : 22pt (lecture à 3m)
- **Print body : 11pt (lecture à 25cm — compact)**
- Print H1 22pt, H2 14pt, H3 12pt, caption 9pt italic
- Validé contre Rapport v1 (Couverture rapport.html + Rapport-print.html)

### Cross-medium philosophy clarifiée
- Identique : couleurs canoniques, fonts Poppins/Raleway, logos, corner marks
- DISTINCT : tailles, grilles, line-heights — adaptés au medium

`docs/DESIGN.md` ajoute section « Per-medium typography ».
