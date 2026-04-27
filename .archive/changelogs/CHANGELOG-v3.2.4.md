# CHANGELOG v3.2.4 — Design System POF

**Date :** 2026-04-26
**Statut :** Integration patch — charts, icons recoloring, ASSETS.md doc complete

Source : feedback Benoit du 2026-04-26 sur le zip Graphiques & maps de Claude Design + audit pictos repo + audit DB Notion Media Assets.

## Patches appliqués

### Charts integrés (`/examples/charts/`)

16 chart templates HTML+CSS livrés par Claude Design ajoutés au repo comme catalogue de référence :

- 01 KPI / Big number
- 02 Bar
- 03 Stacked
- 04 Grouped
- 05 Line
- 06 Donut
- 07 Progress
- 08 Funnel
- 09 Timeline
- 10 Gantt
- 11 Sankey
- 12 Process
- 13 Org chart
- 14 Tables (financial + comparison)
- 15 Radar

`16-map.html` **explicitement exclu** : Benoit itère encore sur les déclinaisons map (Monde, SE Asie, Afrique, Indonésie, Philippines, Afrique Ouest, Océan Indien). Sera intégré en v3.2.5 ou v3.3.

Chaque chart est une page HTML standalone avec styles CSS partagés (`styles.css`). Réutilisable comme référence pour Claude Design ou comme template à copier dans un livrable.

### CSS canonical-palette compliance

Patches sur `examples/charts/styles.css` et tous les charts HTML :
- `font-weight:500` → `font-weight:600` (le 500 Medium n'est pas dans le hard lock v3.2.3)
- `#2a3147` → `#1C1F3B` (canonical navy)
- `#3a4a66` → `#435D74` (canonical steel)
- `#9db1c2` → `#CFD9E0` (chart_palette extended series 3)
- `#eff2f6` → `#F9FCFF` (canonical light)

**Dette résiduelle (v3.2.5) :** styles.css utilise 11 tailles font-size en `px` (9, 9.5, 10, 11, 12, 13, 14, 16, 18, 24, 36). Le hard lock v3.2.3 définit 7 tailles en `pt`. Conversion px → pt à effectuer (×0.75) et consolidation à 7 valeurs.

### Pictos icons recolorables — `/assets/icons/*.svg`

55 SVG (47 + 8 ecology) corrigés :
- `stroke="#1A2B4A"` → `stroke="currentColor"` (recoloration via CSS `color: ...`)
- `#1A2B4A` (hex non-canonique, légèrement différent du navy POF) → `#1C1F3B` (canonical)

Avant : impossible de mettre une icône en blanc sur fond navy car la couleur était hardcoded.
Après : `<svg style="color: white">` ou parent CSS suffit.

### `docs/ASSETS.md` v3.2.4 — réécriture complète

L'ancien doc (v3.1.0) ne documentait pas la base Notion Media Assets. Réécriture totale avec :

**Section 1 — Static brand assets** (versionnés dans le repo)
- Logos (5 fichiers + placement vérifié 16:9)
- Brand pictos (2 fichiers brand mark — pas UI icon)
- UI icons (55 fichiers Tabler curated, currentColor, recolorables)
- Brand elements (waves, corner brackets 4 orientations)
- Backgrounds (2 fichiers full-bleed)

**Section 2 — Notion Media Assets database** (dynamic, hors Git)
- Schema complet 11 champs : `Nom`, `Aperçu`, `Description`, `Dimensions`, `Type` (8 options), `Entité (BU)` (4), `Pays` (8), `Produit/Sujet` (9 multi), `Usage recommandé` (8 multi), `Orientation` (3), `URL fichier`
- Minimum viable record (4 champs requis pour qu'un asset soit utilisable)
- Protocole de query avec filter combinations par use case (Cover, Section divider, Content+Image, Big number, Team, LinkedIn, Catalogue, Carte de visite)
- Ranking heuristic quand plusieurs résultats
- Default values quand non spécifié
- Workflow d'ajout manuel + cadence audit

**Justification Git agnostique :** ce repo ne stocke aucune photo. Notion = source de vérité des médias dynamiques. Git = index, schema, protocole.

### Versions alignées
- `tokens/brand-tokens.json` v3.2.4
- `tokens/brand-rules-per-format.json` v3.2.4
- `README.md` v3.2.4
- `docs/DESIGN.md` v3.2.4

## Hors scope (différé en v3.2.5)

- **Maps** : 4 SVG (`pof-world-map-blank.svg`, `pof-world-map-annotated.svg` + variantes régionales) NON intégrés. Benoit itère sur les déclinaisons par région.
- **Type-scale conversion px → pt** dans styles.css charts.
- **Maps regional sub-files** : SE Asie, Afrique, Indonésie, Philippines, Afrique Ouest, Océan Indien.

## Vérification

```bash
# Icons recolorables
grep -L "currentColor" assets/icons/*.svg     # doit retourner 0 fichier
# Hex canon
grep -E "#1A2B4A|#1a2b4a" assets/             # doit retourner 0 ligne
# ASSETS.md couvre la DB Notion
grep -c "8ca51a75-2413-4f72-8f2a-c44d445fa1d0" docs/ASSETS.md  # doit retourner ≥ 1
# Charts catalogue
ls examples/charts/[0-9]*.html | wc -l        # doit retourner 16
```

## Action requise côté Claude Design

Mettre à jour le bloc « Any other notes » avec :

```
Read docs/ASSETS.md before any image query. Notion DB Media Assets schema, query protocol, and minimum record requirements are documented there.

When generating a slide that needs a photo:
1. Identify use case (Cover, Section, Content+Image, Big number, Team, etc.)
2. Build filter combination per docs/ASSETS.md "Query protocol" table
3. Query collection://8ca51a75-2413-4f72-8f2a-c44d445fa1d0
4. Apply ranking heuristic if multiple results
5. Use ONLY URL fichier field — never Notion attachment IDs

Reference catalog of charts/tables in /examples/charts/. Reuse before generating from scratch.
```
