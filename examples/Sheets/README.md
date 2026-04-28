# Excel template — POF v2.0

6 sheets ready-to-use, brand-aligned with v3.3.9 hard locks.

| Sheet | Purpose |
|-------|---------|
| **01 Dashboard KPI** | 6-card grid (3×2) showing top metrics + teal accent bar per card |
| **02 Data master** | 12-column 50-row table, alternating fills, frozen header, monetary/percent formats |
| **03 Bar chart** | Tonnage by country 2025→2026 — POF palette (navy + steel) |
| **04 Stacked** | Revenue composition by stream (Equipment / Training / Off-take / Plastic credits) |
| **05 P&L 3y** | Compte de résultat consolidé FY2025-2027 with formulas (revenue/COGS/gross margin/OPEX/EBITDA/EBIT) |
| **06 Funnel** | Pipeline conversion — Inquiries → Operational |

## Style applied (v3.3.9 canonical)

- Header rows: navy `#1C1F3B` fill, white text Poppins SemiBold 11pt
- Data rows: alternating `#FFFFFF` / `#F9FCFF`, no borders
- Subtotal rows: neutral `#EAEBED` fill, Raleway SemiBold 11pt navy
- KPI cards: navy header bar + light value zone + teal 6px accent bar bottom
- Money: `#,##0 €;(#,##0 €)` (negatives in parens, no minus)
- Percentages: `0.0%`
- Captions: Raleway Italic 9pt `#6C757D`
- Chart series: `#1C1F3B` (primary), `#435D74` (secondary), `#CFD9E0` (tertiary)
- No chart gridlines, no chart borders

## How to use

1. Open `pof-dashboard-template-v2.xlsx`
2. Replace data with your own (P&L formulas auto-recalculate)
3. Add/remove KPI cards on Sheet 1 (each card = 4 merged rows × 5 columns)
4. Add rows on Sheet 2 (alternating fill apply via the existing pattern)
5. Update chart data ranges on Sheets 3, 4, 6 if needed

## Notes

- Compatible Excel 365 / 2019+, Numbers (Mac), Google Sheets (visual diff possible on charts)
- Fonts fallback to Arial if Poppins/Raleway not installed locally
- v2 deprecates v1 (single-sheet pof-dashboard-template.xlsx) which had only 3 sheets
