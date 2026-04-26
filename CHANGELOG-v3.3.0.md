# CHANGELOG v3.3.0 — Design System POF

**Date :** 2026-04-26
**Statut :** Minor release — fixes + new features (templates + vectorized maps + feedback DB) — fix régression icons + docs maps/charts/icons

Source : audit Github 2026-04-26 par Benoit. Identifie une régression et trois manques de doc.

## Patches appliqués

### Fix critique — Régression icons hex

162 SVG dans `assets/icons/ecology/` et `assets/icons/environment/` utilisaient `#1A2B4A` (hex non-canonique introduit par un autre chat Claude Design entre v3.2.4 et v3.2.5). Fix sed global sur tous les fichiers.

Avant : 54 fichiers contenant `#1A2B4A` + 10+ fichiers contenant `#80c8c3`
Après : 0 fichier non-canonique. Tous les icons utilisent uniquement `#1C1F3B`, `#80C7C2`, `#FFFFFF`, ou `currentColor`.

### `docs/MAPS.md` — nouveau

Charte cartographique complète extraite et structurée depuis `assets/maps/map-charter.html` (qui reste la référence visuelle interactive). Couvre :
- 5 patterns canoniques (heatmap, categorical, neutral dots, data dots, anchored faded)
- Region overlays avec 3 régions canoniques POF (West Africa, East Africa & Indian Ocean, South-East Asia)
- Règle d'anchoring obligatoire (cartes adossées à un bord)
- Légendes on-map + off-map (max 1 légende par map)
- Compatibilité cross-medium (web / PowerPoint / print)

### `docs/CHARTS.md` — nouveau

Catalogue des 16 chart templates dans `examples/charts/` avec usage par type, éléments mandatory, palette par série, contraintes cross-medium, règles de légende (max 1 par chart).

### `docs/ICONS.md` v2 — réécrit

Ancien doc obsolète (mentions des icônes Tabler retirées du repo, pas de référence à `ecology/` et `environment/`). Nouveau doc :
- 3 sources : POF curated `assets/icons/ecology/` et `environment/`, Tabler CDN fallback, POF brand pictos
- Stratégie de variantes : `currentColor` pour CSS, `_navy / _teal / _white` pour PPTX/DOCX/PDF
- Workflow de sélection
- Enforcement des couleurs canoniques

### `docs/ASSETS.md` v3.2.6

Sync version. Ajout d'une section "Maps" qui référence `assets/maps/` complet. Mise à jour de la section icons pour pointer vers `docs/ICONS.md` v2.

### `tokens/brand-rules-per-format.json` — blocs `charts_lock` + `maps_lock`

Formalisation des règles charts et maps en blocs JSON exploitables par Claude Design :
- `charts_lock` : max legends, max series, palette, forbidden list, cross-medium constraints
- `maps_lock` : 5 patterns canoniques avec leurs valeurs hex et formules, region overlays canoniques (3 régions avec listes ISO), règles d'anchoring, contraintes cross-medium

### `README.md` — réécrit

Structure du repo à jour (icons sub-dirs, maps, examples/charts), mandatory reads par priorité, philosophie cross-medium explicitée, hard locks récap.

### Versions
- `tokens/brand-tokens.json` v3.2.6
- `tokens/brand-rules-per-format.json` v3.2.6
- `docs/ASSETS.md` v3.2.6
- `docs/DESIGN.md` v3.2.6
- `docs/MAPS.md` v1.0 (nouveau)
- `docs/CHARTS.md` v1.0 (nouveau)
- `docs/ICONS.md` v2.0 (réécrit)
- `README.md` v3.2.6



### Vectorize regional maps (v3.3.0)

`assets/maps/svg/02-07.svg` étaient des PNG embarqués dans des wrappers SVG (USAGE.md flaggait `PNG (vector pending)`). Régénérés depuis `pof-world-map-blank.svg` en proper vector :

| File | viewBox | Countries in bbox | POF priority |
|------|---------|-------------------|--------------|
| 02-asie-du-sud-est.svg | 626 × 608 | 33 | ID, PH, VN, KH |
| 03-afrique.svg | 584 × 675 | 90 | SN, CI, CM, NG, KE, TZ, MG, EG |
| 04-indonesie.svg | 431 × 342 | 16 | ID |
| 05-philippines.svg | 435 × 346 | 16 | PH |
| 06-afrique-de-louest.svg | 399 × 317 | 38 | SN, CI, CM, NG, GN |
| 07-ocean-indien-est.svg | 383 × 495 | 48 | KE, TZ, MG |

Chaque SVG suit la structure 4 couches (bg / base / overlay / fade) documentée dans `assets/maps/USAGE.md`. Pré-rempli avec POF priority countries en navy `#1C1F3B`.

### Templates secondaires (v3.3.0)

**`examples/email-signatures/` — 3 HTML**
- factories.html, academy.html, sunu-po.html
- Outlook + Gmail compatible (table-based, inline CSS, base64 logo)
- Variables Mustache : first_name, last_name, role, phone_e164, email
- Disclaimer GDPR inclus

**`examples/excel/pof-dashboard-template.xlsx`**
- Sheet 1 : Dashboard KPI (6 cards, 3 × 2 grid)
- Sheet 2 : Data table (12 col × 50 rows, alternating fills, frozen header)
- Sheet 3 : Chart (bar chart POF palette, no gridlines)

### Notion DB Feedback (v3.3.0)

Database "Design System Feedback" créée :
- URL : https://www.notion.so/d100a1de858f4d7d9391dbcd5c8cd7e0
- Collection ID : `collection://a3f73a10-caf3-4726-b37f-421244a9cc6f`
- 11 champs : Comment, Date, Chat, Livrable, Slide ou section, Sévérité, Catégorie (multi), Patch proposé, Appliqué, Patch version, Notes
- Workflow : Benoit consigne les commentaires Claude Design à chaque session, je consolide en patches hebdomadaires.

### Versions
- `tokens/brand-tokens.json` v3.3.0
- `tokens/brand-rules-per-format.json` v3.3.0
- `README.md` v3.3.0
- `docs/DESIGN.md` v3.3.0
- `docs/ASSETS.md` v3.3.0
- `docs/MAPS.md` v1.0 (design system v3.3.0)
- `docs/CHARTS.md` v1.0 (design system v3.3.0)
- `docs/ICONS.md` v2.0 (design system v3.3.0)

## Vérification

```bash
# Aucun hex non-canonique dans les icons
grep -rE "#1A2B4A|#80c8c3|#1D1E3A" assets/icons/    # doit être vide

# Documents nouveaux présents
ls docs/MAPS.md docs/CHARTS.md

# Locks présents
jq '.charts_lock' tokens/brand-rules-per-format.json
jq '.maps_lock' tokens/brand-rules-per-format.json

# Versions alignées
grep -h '"version"' tokens/*.json
```

## Hors scope (différé)

- **Validation PowerPoint des 15 layouts** (humain — non automatisable)
- **Audit photos Notion** (Piste 2 backlog — à lancer dans un chat dédié)
- **Templates LinkedIn cards** (encore en exploration)
- **Rapport PDF complet** (dépend des DOCX validés)
- **P&L 3 ans + balance sheet templates Excel** (v1.1 du template Excel)
- **Pattern dégradé navy pour profondeur** (feedback Benoit, à formaliser pour v3.4)

## Ce qui change pour les nouveaux chats Claude Design

Plus besoin de coller un long bloc "Any other notes" — le repo est désormais auto-suffisant. Le bloc à coller est minimal (cf section starter pack délivré par Benoit le 2026-04-26).
