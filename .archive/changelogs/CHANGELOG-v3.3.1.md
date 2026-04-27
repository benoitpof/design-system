# CHANGELOG v3.3.1 — Design System POF

**Date :** 2026-04-26
**Statut :** Patch — gradient sync + navy depth + alignment V2 template

## Patches

### Sync `tokens/brand-tokens.css` gradient overlay

`--pof-gradient-navy-overlay` était out-of-sync avec le hard lock v3.2.3 :
- Avant : `135deg, #1C1F3B 0%, rgba(29,30,58,0.58) 100%` (100% / 58%)
- Après : `135deg, rgba(28,31,59,0.85) 0%, rgba(28,31,59,0.45) 100%` (lock canonique)

### Nouvelle option `navy_depth_subtle`

Feedback Benoit (« éviter à-plat navy sans nuance »). Alternative optionnelle :
`linear-gradient(180deg, #1C1F3B 0%, #25284A 100%)`. Vertical, ≥30 mm surface.
Tokens JSON + CSS + DESIGN.md section dédiée.

### Alignment template V2 (Charte/Trame/Zone-utile deck V2 du 2026-04-26)

Audit révèle drift entre design system Git et les templates V2 utilisés en pratique :

**1. Type-scale lock élargi à 8 tailles (était 7)**
Ajout 28pt. Allowed : `[9, 11, 14, 18, 22, 26, 28, 36]` + stat-only `[72, 120]`.
Rationale : V2 utilise 28pt pour les slogans (cover, section divider, closing).

**2. ExtraBold (800) restriction loosened**
Avant : restreint à L01 cover, L02 section, L04 stat number.
Après : autorisé sur slide_title_default (any layout). V2 utilise « TRÈS GRAS 26pt » comme titre standard de slide. La restriction précédente était trop stricte.

**3. `slides.max_envelope` ajouté (zone utile V2)**
- `x_mm: 26.3, y_mm: 20.6, max_width_mm: 455.3, max_height_mm: 244.6`
- Inclut le header zone (au-dessus du content_zone).
- `content_zone` reste la zone de body content, sous le header.
- Distinction documentée dans DESIGN.md section dédiée.

**4. `font_size_mapping` réécrit selon hiérarchie V2**
- cover_title 36pt ExtraBold
- slide_title 26pt ExtraBold (V2 « TRÈS GRAS »)
- slide_subtitle 26pt SemiBold (V2 « moyen »)
- slogan 28pt SemiBold
- body 22pt Regular (V2 « normal »)
- caption 18pt / 11pt / 9pt selon contexte
- stat_number 120pt ExtraBold

### Versions
- tokens/brand-tokens.json v3.3.1
- tokens/brand-rules-per-format.json v3.3.1
- tokens/brand-tokens.css (sync + navy-depth)
- docs/DESIGN.md v3.3.1
- README.md + ASSETS/MAPS/CHARTS/ICONS headers v3.3.1

## Audit photos Notion (parallèle)

Audit lancé via subagent :
- ~85 assets dans la DB
- 100 % fully-tagged sur l'échantillon (16 inspectés)
- 30 photos prêtes pour deck investisseurs (Sénégal, Philippines surtout, Paysage, Usage~Deck)
- Recommandation : aucun re-tagging requis, hosting Google Drive OK
- Gap : 0 photo Indonésie / Kenya, 0 photo Academy / Sunu PO

## Hors scope (Claude Design corrections en cours)

- Environment icons : variantes currentColor (à venir v3.3.2)
- N1/N2/N3 heatmap variants doc (à venir v3.3.2)
- Fade reconciliation maps (à venir v3.3.2)
- L11-L15 examples HTML/PPTX (à venir v3.3.2)
