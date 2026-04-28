# REPORT.md — POF Report Layouts (Word, PDF print)

**Version:** 3.4.0 | **Updated:** 2026-04-27
**Status:** Scaffolding initial. À enrichir via ds-iterate après 3 premiers reports produits.
**Format:** A4 portrait (210 × 297 mm), marges 25 mm L/R, 20 mm top/bottom. Bleed 3 mm si impression.
**Médium :** Word .docx (édition) → PDF print (livrable). Pas de slides ici.

---

## Cadre général

- Police titres : **Poppins** (ExtraBold pour cover, SemiBold pour H1/H2/H3)
- Police corps : **Raleway** Regular 11 pt, interligne 1.4
- Couleur navy `#1C1F3B` pour titres, body `#3C3C3C` pour texte courant
- Logo POF : top-right de chaque page sauf cover (top-left, large)
- Numérotation : bottom-center, format `Page X / Y`, Raleway 9 pt steel

## Layouts canoniques (R01–R10)

| ID | Nom | Usage | Pages |
|---|---|---|---|
| R01 | Cover full-bleed | Page 1, photo + titre + subtitle + entité | 1 |
| R02 | Section divider | Ouverture chapitre, photo + roman numeral + titre | 1 |
| R03 | TOC | Table des matières, 2 colonnes max | 1 |
| R04 | Body text | Paragraphes, max 1 visuel par page | 1+ |
| R05 | KPI page | 3 à 6 KPIs grand format, 1 page | 1 |
| R06 | Photo + caption | Photo full-width, caption en bas | 1 |
| R07 | Quote / pullquote | Citation centrée, fond teal soft | 1 |
| R08 | Map page | Carte full-width avec légende | 1 |
| R09 | Chart page | Chart + analyse texte (split 60/40) | 1 |
| R10 | Back cover | Logo + URL + contacts + mention légale | 1 |

> **À détailler :** dimensions exactes, anchor points, exemples golden. Ce scaffold sera enrichi après production de 3 reports.

---

## Règles spécifiques print

- Pas de gradient teal→clear (banni v3.3.x)
- Photos : DPI minimum 300 (sinon flou impression)
- Texte sur photo : overlay obligatoire (voir `rules/PHOTOS.md`)
- Pas de cadre gris autour des photos (banni v3.3.x)
- Bleed 3 mm si impression : visuel doit déborder, texte critique en dehors

## Memory — capitalisation Rex

<!-- ds-iterate écrit ici. Format : ### YYYY-MM-DD — <titre> -->

## Exemples golden

Voir `/golden/report/` (max 5 par layout).
