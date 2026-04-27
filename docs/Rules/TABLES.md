# TABLES.md — POF Table Rules per Medium

**Version:** 3.4.0 | **Updated:** 2026-04-27
**Status:** Scaffolding initial. À enrichir via ds-iterate.

---

## Catalog (cf. examples/charts/)

- `14-table.html` — Tableau financier (P&L, BS, CF, CAPEX)
- `14-table-v1.html` — Tableau comparaison (specs, scénarios)
- Excel dashboards : `examples/excel/` (2 templates v2)

## Règles communes

- Header row : navy `#1C1F3B` background, white text, Poppins SemiBold 11 pt
- Data rows : alternance white / `#F9FCFF` (gris-pof) pour zebra
- Numbers : align right, 2 décimales max sauf %, k€/k$ par défaut
- Negatives : coral `#E8546C`, pas de parenthèses
- Sources : Raleway Light 9 pt italic, bottom-left
- Pas de 3D, pas de drop shadow

## Slide deck

- Max 8 colonnes, max 12 lignes par slide
- Si plus : split en 2 slides ou réduire granularité
- Border-bottom uniquement (1 px steel-pale), pas de border globale

## Report A4

- Max 6 colonnes (lisibilité print)
- Header répété si tableau > 1 page
- Page break éviter milieu de ligne

## Web

- Responsive : pivot ou collapse sur mobile (< 768 px)
- Sticky header au scroll si > 10 lignes
- Sortable columns : aria-sort, indicateur visuel triangle

## Excel

- Formatage POF brand par xlsx skill (cf. `gsheet-format` skill)
- Headers gelés (freeze pane)
- Conditional formatting : navy → coral pour P&L (rouge si < 0)

## Forbidden

- Multicolor headers (banni v3.3.x)
- Bordures internes systématiques (encombrement visuel)
- Cellules fusionnées dans data area (uniquement headers)
- Alternance verte/rouge (incohérent palette POF)

## Memory — Rex

<!-- ds-iterate écrit ici -->

## Exemples golden

Voir `examples/charts/14-table*.html` et `examples/excel/*.xlsx`.
