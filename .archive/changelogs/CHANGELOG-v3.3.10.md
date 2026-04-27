# CHANGELOG v3.3.10 — Design System POF

**Date :** 2026-04-27
**Statut :** Excel template v2 — 6 sheets

## Patch

### `examples/excel/pof-dashboard-template-v2.xlsx` — 6 onglets

Avant (v1) : 3 onglets (Dashboard KPI / Data / Chart) — basique.
Après (v2) : 6 onglets représentatifs du catalogue charts/tables :

| Sheet | Inspiration catalogue |
|-------|----------------------|
| 01 Dashboard KPI | charts/01-kpi.html — 6 cards, accent bar teal |
| 02 Data master | charts/14-table.html — 12 cols × 8 rows alternating |
| 03 Bar chart | charts/02-bar.html — tonnage par pays 2025→2026 |
| 04 Stacked | charts/03-stacked.html — revenue par stream |
| 05 P&L 3y | charts/14-table.html — compte de résultat avec formulas |
| 06 Funnel | charts/08-funnel.html — pipeline conversion |

P&L sheet inclut formulas auto-recalcul (Total revenue / Total COGS / Gross margin / Gross margin % / EBITDA / EBIT).

### Versions
- tokens v3.3.10
- README docs/* bumped
- v1 (pof-dashboard-template.xlsx) gardé pour rétro-compatibilité, à terme retiré
