# CHANGELOG — POF Design System

**Format :** sections par version, plus récente en haut. Breaking changes signalés en gras.

---

## v3.4.0 — 2026-04-27

**Restructuration majeure de l'arborescence repo (sans perte de contenu).**

### Added
- `docs/layouts/{REPORT,WEB,SOCIAL}.md` — scaffolding par medium
- `docs/rules/{PHOTOS,TABLES}.md` — règles isolées photo et tableaux
- `memory/` (8 types : deck, report, web, social, chart, map, photo, icon)
- `golden/` (hard limit 5 par type, doc README.md)
- `templates/` (master files binaires, à remplir)
- `examples/{maps,deck,report,web,social}/` (subdirs avec README format)
- `site/` (GitHub Pages V1 : index.html overview + architecture.html)
- `ITERATE.md` (guide ds-iterate avec niveaux risque)
- `VISUALIZE.md` (URL gallery + local preview)
- `CHANGELOG.md` (consolidé, ce fichier)

### Changed
- `docs/LAYOUTS.md` → `docs/layouts/DECK.md`
- `docs/{DESIGN,CONTENT-RULES,ASSETS,CHARTS,MAPS,ICONS}.md` → `docs/rules/*`
- `docs/ICONS.md` + `docs/ICONS-TABLER.md` → fusion dans `docs/rules/ICONS.md` (302 lignes)
- 16 `CHANGELOG-v3.X.X.md` consolidés ici (originaux dans `.archive/changelogs/`)

### Architecture
- 3 skills cibles : DS-Dataviz-generator, ds-file-assembler, ds-iterate
- Notion = working memory uniquement, GitHub = SSOT règles + golden + code
- Tags callouts Notion : 📐 Layout, 🖼️ Illustration, 💡 Exemple, 📝 Note, 📚 Source
- ds-iterate scheduled task touche uniquement niveaux A et B (memory + rules)
- Niveau C (tokens) et D (Skills, masters, DB) : validation formelle Benoît

---

## v3.3.10 — historique


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

---

## v3.3.9 — historique


**Date :** 2026-04-27
**Statut :** Patch — overlay intensity medium + integrate Graphs & maps catalogue

## Patches

### Overlay intensity 'medium' added

Trois niveaux désormais : `full` (1.0) / **`medium` (0.75)** / `soft` (0.5). Tous finissent transparent à 100%.

Pattern CSS medium :
`linear-gradient(<angle>, rgba(28,31,59,0.75) 0%, rgba(28,31,59,0.75) <hold_pct>%, transparent 100%)`

Use case : photo équilibrée entre dimming fort et léger, contexte préservé tout en gardant un texte lisible.

Combinaisons gradient totales : 4×4×2×3 = **96** (was 64).

### Catalogue Graphs & maps intégré

Output du projet Claude Design Graphs & maps poussé dans le repo :
- `examples/charts/16-map.html` (936 lignes) — page maps complète avec patterns + crops régionaux
- `examples/charts/17-icons.html` — POF Tabler shortlist 106 icônes × 3 variants navy/teal/white via CDN
- `examples/charts/18-images.html` — page images avec live photos Notion DB + sections types/overlays/text rules/forbidden
- `examples/charts/Tableaux-financiers.html` — variante tables financières
- `examples/charts/index.html` mis à jour avec sections (Data viz / Stat / Structure / Data display / Geo / Library)

Photos dans 18-images.html servies via Google Drive (`lh3.googleusercontent.com`) résolues depuis la Notion DB. Pipeline confirmé fonctionnel.

### Versions
- tokens v3.3.9
- README + DESIGN + MAPS + CHARTS + ICONS + ASSETS bumped to v3.3.9

---

## v3.3.8 — historique


**Date :** 2026-04-27
**Statut :** Patch — Overlay gradient intensity added

## Source feedback

User 2026-04-27 : « Je ne vois pas l'overlay qui part de 50% transparence et va à 100% de transparence ».

## Patch

### `overlay_system.gradient.intensity` — 2 niveaux

Avant : tous les gradients commençaient à 100% opaque dans la zone hold.
Après : 2 intensités possibles, toutes deux finissent à 100% transparent :

- **`full`** (default) : start_opacity 1.0 — `linear-gradient(<angle>, #1C1F3B 0%, #1C1F3B <hold_pct>%, transparent 100%)`
- **`soft`** : start_opacity 0.5 — `linear-gradient(<angle>, rgba(28,31,59,0.50) 0%, rgba(28,31,59,0.50) <hold_pct>%, transparent 100%)`

Use case `soft` : photos chaudes où on veut garder le contexte visible à travers le tint (visages, produits).

### Combinations valides

Avant : 4 × 4 × 2 = 32
Après : 4 × 4 × 2 × 2 = **64** combinaisons valides

### Selection rules

Ajout : `warm_photo_with_caption` → `gradient.from_bottom.half.navy_pure.soft`.

### Versions
- tokens/brand-tokens.json v3.3.8
- tokens/brand-rules-per-format.json v3.3.8
- docs/DESIGN.md v3.3.8
- README + ASSETS/MAPS/CHARTS/ICONS bumped to v3.3.8

---

## v3.3.7 — historique


**Date :** 2026-04-27
**Statut :** Major patch — Overlay system formalized

## Source feedback

User 2026-04-27 + Overlays.pptx (V2 charte) + screenshots Section 2 charts/18-images.html : l'overlay précédent (single canonical 135deg 85%/45%) ne correspond pas aux usages réels. Le V2 demande un système plus riche.

## Patches

### Système d'overlays — `overlay_system` block

REMPLACE l'ancien `gradient_overlay_lock` (single canonical) par un système structuré à 35 combinaisons valides.

**A. Solid uniform — 3 niveaux**
- `light` 30%, `medium` 60%, `heavy` 90% (rgba navy)
- Use cases : full-photo wash, big number bg, hero, dramatic quote

**B. Gradient — 4 × 4 × 2 = 32 combinaisons**
- 4 directions exclusives : from_left / from_right / from_top / from_bottom (no diagonal, no cumulation)
- 4 coverages : quarter (25%) / third (33%) / half (50%) / full (75%)
- 2 colors : navy_pure OR navy_with_teal_reflet (radial teal bottom-left)
- Pattern : `linear-gradient(<angle>, #1C1F3B 0%, #1C1F3B <hold_pct>%, transparent 100%)`
- **Always ends 100% transparent**

Selection rules par use case formalisées :
- cover_slide_with_text : gradient.from_left.third.navy_pure
- big_number_bg : solid_uniform.medium
- section_divider : gradient.from_bottom.half.navy_pure
- caption_strip : gradient.from_bottom.quarter.navy_pure
- hero_photo_wash : solid_uniform.light
- dark_dramatic_quote : solid_uniform.heavy

### Forbidden

- Non-axial directions (45deg etc.)
- Cumulating directions (left + bottom)
- Coverage hold_pct hors [25, 33, 50, 75]
- Final stop non-transparent
- Teal reflet sans navy primary
- Teal reflet position autre que bottom-left

### Documentation

- `docs/DESIGN.md` : section "Gradient overlay lock" remplacée par "Overlay system (v3.3.7)"
- `tokens/brand-tokens.json` `colors.gradients._overlay_system_ref` pointe vers la spec complète
- README + ASSETS/MAPS/CHARTS/ICONS bumped to v3.3.7

## Migration

Anciens usages avec `linear-gradient(135deg, rgba(28,31,59,0.85) 0%, rgba(28,31,59,0.45) 100%)` :
→ Migrer vers `gradient.from_left.third.navy_pure` (équivalent visuel proche, conforme spec)

Legacy CSS var `--pof-photo-overlay` reste disponible pour compatibilité mais marqué DEPRECATED. À retirer en v3.4.

---

## v3.3.6 — historique


**Date :** 2026-04-27
**Statut :** Patch — icons strategy switch + Drive folder doc

## Source feedback

User 2026-04-27 : « Claude Design ne voit que les ecology icons, on supprime les pictos avec double épaisseur et on s'assure que tous les Tabler sont accessibles ».

## Patches

### Ecology icons archivés

`assets/icons/ecology/` → `assets/icons/_archived/ecology/`. 32 SVG retirés du scope actif. Raison : `stroke-width="28"` incompatible avec le style Tabler outline (typique `stroke-width="2"`). Réversible.

Inventaire actif : aucun POF curated icon. Tabler CDN devient la source primaire pour tous les pictos.

### `docs/ICONS.md` v3.0 — réécriture

Avant : 3 sources (POF curated en 1, Tabler en 2, brand pictos en 3).
Après : 2 sources (Tabler CDN en 1, brand pictos en 2). POF curated = archived seulement.

Sections :
- Tabler CDN URL pattern + selection workflow + embed strategies par medium
- Recommended shortlist par catégorie POF (industrial, ecology, process, impact, logistics)
- Default colors par medium
- Brand pictos (2 fichiers, brand mark only)
- Archived list

### `docs/ASSETS.md` v3.3.6

Bloc Notion Media Assets DB enrichi avec :
- URL Notion publique : https://www.notion.so/25bd7cc0e7454f0f9cb8607870f59738?v=342c2ce245e880fabb97000cc87a1cbb
- Drive folder source : https://drive.google.com/drive/folders/1oqm8Wkh_lfH4Vw4j7vBJNtoO8aji9GIn

Le Drive folder contient les fichiers raw, le champ `URL fichier` Notion pointe vers leur version partagée publique. Claude Design peut accéder aux deux via MCP.

### Versions
- tokens/brand-tokens.json v3.3.6
- tokens/brand-rules-per-format.json v3.3.6
- docs/ICONS.md v3.0 (alignée v3.3.6)
- docs/ASSETS.md v3.3.6
- README + DESIGN.md + MAPS.md + CHARTS.md headers v3.3.6

---

## v3.3.5 — historique


**Date :** 2026-04-27
**Statut :** Major patch — multi-feedback consolidation

## Source feedback

User feedback du 2026-04-27 — synthèse des reviews Claude Design + maps + buttons + gradient.

## Patches

### Buttons Ghost — hiérarchie corrigée

Avant : Ghost border navy + text navy (équivalent visuel à Primary)
Après : Ghost = lowest emphasis variant.
- Light : border #435D74 (steel) + text steel, hover bg #CFD9E0
- Dark : border #5F7D95 (light-steel) + text light-steel, hover bg white 8%
- Hierarchy : Primary > Secondary > Danger > Ghost

Bloc `components.button_ghost` ajouté dans `tokens/brand-tokens.json`.

### Navy depth gradient — itération finale (5e passe)

Avant : `linear-gradient(180deg, #1C1F3B 0%, #80C7C2 100%)` (navy → solid teal vertical)
Après : `linear-gradient(45deg, rgba(128,199,194,0.38) 0%, rgba(128,199,194,0) 60%), #1C1F3B` (teal glow from bottom-left, transition to fully transparent at 60%, on solid navy base, teal final opacity 38%)

Effet : "coin lumineux" subtil en bas-gauche, navy solide ailleurs. Plus institutionnel que le dégradé vertical.

### World basemap nouveau master — `00-monde-cropped.svg`

Crop sur les 2 axes :
- x ≥ 950 : Americas dropped
- y ≤ 1000 : Antarctica dropped

148 pays, no labels (text stripped). 3 fades baked-in (g_BT, g_LR, g_TB) pour anchors top, left, bottom.

ViewBox : `950 0 1468 1000`. Stocké dans `assets/maps/svg/00-monde-cropped.svg`.

### Heatmap palettes — formalisation

Bloc `maps_lock.heatmap_palettes` avec 4 variantes :
- N1 (default white→navy)
- N2 (neutral gray→navy)
- N3 (steel→navy, skewed-high data)
- **T1 (teal-only)** — NEW v3.3.5. 4 stops `#F1FBFA → #80C7C2 → #2BA595 → #09414A`. Pour Pattern 1 + R3 regional Indian Ocean.

### Maps fade rules

Bloc `maps_lock.fade_rules` formalisé :
- `no_overlap_with_colored`: true — fade ne couvre jamais countries colorés ou dots
- `legend_z_order`: top — légende toujours rendue last, jamais sous le fade
- `fade_start_at_viewbox_edge`: gradient START coordinate = viewBox edge

### Environment icons archivés

`assets/icons/environment/` → `assets/icons/_archived/environment/`. Retiré du scope actif. Réversible.

### Versions
- `tokens/brand-tokens.json` v3.3.5
- `tokens/brand-rules-per-format.json` v3.3.5
- `tokens/brand-tokens.css` (Ghost vars + navy-depth refined)
- `assets/maps/svg/00-monde-cropped.svg` (NEW)
- `assets/icons/environment/` → `_archived/`
- README + ASSETS/MAPS/CHARTS/ICONS bumped to v3.3.5

---

## v3.3.4 — historique


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

---

## v3.3.3 — historique


**Date :** 2026-04-27
**Statut :** Patch — scope reduction + clean-up palette + 26pt slide_title

## Patches

### Scope : POF Factories only

Académy et Sunu PO retirés du design system (décision Benoit 2026-04-27).

Removed :
- `tokens/brand-tokens.json` `entity_overrides.academy`
- `tokens/brand-tokens.json` `entity_overrides.sunu_po`
- `tokens/brand-tokens.css` `--pof-academy-*` variables
- `tokens/brand-tokens.css` `--pof-sunu-*` variables (si présentes)
- `README.md` section "Entity defaults" remplacée par "Entity scope" simple
- `docs/DESIGN.md` mentions Academy / Sunu retirées du brand DNA

### Palette clean-up

Removed :
- `colors.semantic.info` `#0D6EFD` — unused, simplifie la palette sémantique (success, warning, error suffisent)
- `colors.neutral.near_black` `#090911` — redondant avec navy `#1C1F3B`
- CSS vars `--pof-info` et `--pof-near-black`

### Typography scale

Ajout de `slide_title` (26pt / 35px) dans `typography.scale` entre `xl` (18pt) et `2xl` (21pt).

Justification : 26pt est la taille la plus utilisée sur les slides POF (titre + sous-titre par V2 template), mais absente de la scale harmonique. Visualisée correctement dans les preview cards Claude Design désormais.

Ajout CSS var `--pof-text-slide-title: 35px` dans `brand-tokens.css`.

### Versions
- `tokens/brand-tokens.json` v3.3.3
- `tokens/brand-rules-per-format.json` v3.3.3
- `tokens/brand-tokens.css` (vars retirées + ajoutée)
- `README.md` v3.3.3
- `docs/DESIGN.md` v3.3.3
- ASSETS / MAPS / CHARTS / ICONS headers v3.3.3

---

## v3.3.2 — historique


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

---

## v3.3.1 — historique


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

---

## v3.3.0 — historique


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

---

## v3.2.5 — historique


**Date :** 2026-04-26
**Statut :** Hotfix doc — règle explicite « no shadow on corner marks »

## Patch

### Règle explicite : aucune ombre sur les corner brackets

Audit du repo : aucune ombre détectée dans les 5 SVG `corner-bracket-*.svg`, ni dans la spec `slides.corner_marks` de `brand-rules-per-format.json`. Les assets sont propres.

**Mais** la règle n'était pas documentée explicitement → risque que Claude Design (HTML artifact, CSS local, PowerPoint shape effect) en ajoute une à la rendition.

Patches appliqués :

**`tokens/brand-rules-per-format.json` `slides.corner_marks`** :
- Nouveau flag `shadow_forbidden: true`
- Nouveau bloc `effects_forbidden` listant : drop-shadow, inner-shadow, filter:blur, filter:drop-shadow, PowerPoint shape shadow, CSS opacity < 1
- Nouveau champ `rendering_rule` : « Render as flat L-bracket strokes only. No depth effect of any kind. Brand mark is geometric, not skeuomorphic. »
- `_violation_examples` étendu

**`docs/DESIGN.md` § Hard locks** :
Section « Corner marks lock » étoffée avec un paragraphe « No shadow, ever » couvrant CSS drop-shadow, PowerPoint shape effects, opacity reductions, blur — quel que soit le medium de rendu.

### Versions
- `tokens/brand-tokens.json` v3.2.5
- `tokens/brand-rules-per-format.json` v3.2.5
- `README.md` v3.2.5
- `docs/DESIGN.md` v3.2.5

## Vérification

```bash
# Aucune ombre dans les SVG
grep -ciE "filter|shadow|blur|opacity" assets/brand-elements/corner-bracket-*.svg
# La règle est bien documentée
grep -c "shadow_forbidden" tokens/brand-rules-per-format.json
grep -c "No shadow, ever" docs/DESIGN.md
```

## À ajouter dans le bloc « Any other notes » de Claude Design

```
Corner marks (L-brackets) NEVER have shadow, drop-shadow, blur, opacity < 1, or any depth effect. Render exactly as the SVG: flat teal strokes, transparent background. Whether the medium is slide, web, artifact, or report — no exception.
```

---

## v3.2.4 — historique


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

---

## v3.2.3 — historique


**Date :** 2026-04-26
**Statut :** Hard locks + corner brackets migration

Source feedback : analyse des 3 livrables Claude Design (Deck POF Investor, Rapport, Site web v1/v2/v3) du 2026-04-26.

## Patches appliqués

### P1+P2 — Typography lock (STRICT)

Ajout d'un bloc `typography_lock` dans `tokens/brand-rules-per-format.json` :
- Tailles autorisées (pt) : `[9, 11, 14, 18, 22, 26, 36]`
- Tailles stat-only (pt) : `[72, 120]`
- Poids autorisés : `[300, 400, 600, 700]`
- ExtraBold (800) restreint à : titre cover (L01), titre section (L02), stat number (L04)
- Black (900) **interdit**

Justification : le deck livré utilisait 16 tailles distinctes et 5 poids — fragmentation visuelle perçue. Cap dur applique la cohérence à la racine.

`slides.font_size_mapping` re-écrit pour ne référencer que des valeurs du lock.

### P3 — Gradient overlay lock

Bloc `gradient_overlay_lock` ajouté à `brand-rules-per-format.json`.

Valeur canonique unique : `linear-gradient(135deg, rgba(28,31,59,0.85) 0%, rgba(28,31,59,0.45) 100%)`.

CSS var : `--pof-photo-overlay`.

Justification : le deck mélangeait 2 gradients (`105deg 0.92→0.05` et `135deg 0.85→0.15`). Lock élimine l'inconstance.

### P5 — Corner marks → L-brackets

Migration des marks (anciennement carrés solides 7.7 mm) vers des L-brackets vectoriels.

Nouveaux assets :
- `assets/brand-elements/corner-bracket-tl.svg` — angle haut-gauche
- `assets/brand-elements/corner-bracket-tr.svg` — angle haut-droit
- `assets/brand-elements/corner-bracket-bl.svg` — angle bas-gauche
- `assets/brand-elements/corner-bracket-br.svg` — angle bas-droit

Spec : 12 mm × 12 mm, stroke 5 px, color `#80C7C2`, stroke-linecap square. ViewBox 48×48.

Default pair = TL + BR (TR/BL optionnels pour cadrage symétrique).

Bloc `slides.corner_marks` remis à plat dans `brand-rules-per-format.json` avec coords mm pour chaque orientation.

`assets/brand-elements/corner-bracket.svg` mis à jour comme alias canonique du TL.

Justification : la spec disait carrés solides, le SVG existant était une L-shape, le template XML utilisait `grpSp` carrés. 3 sources contradictoires. Décision Benoit du 2026-04-26 : L-brackets (signature plus distinctive).

### P6 — Mode `final_content` documenté

Section ajoutée à `docs/CONTENT-RULES.md` : « VERBATIM CONTENT MODE ».

Triggers d'activation : tag `<final_content>...</final_content>`, mots-clés "verbatim / this is final / do not edit / contenu final / ne pas modifier".

Comportement : placer le texte fourni dans les slots de layout sans paraphrase. Interdit de substituer par les exemples de CONTENT-RULES.md.

Justification : Claude Design a tendance à recopier les exemples du doc CONTENT-RULES.md ("Transforming Waste into Local Wealth", "200-factory franchise network") même quand l'utilisateur fournit son propre contenu.

### Updates collatérales

- `tokens/brand-tokens.json` `_meta.version` → 3.2.3
- `components.gradient_overlay.value` aligné sur le canonical lock
- `README.md` version mise à jour
- `docs/DESIGN.md` ajoute en tête une section « Hard locks (v3.2.3) — STRICT ENFORCEMENT »

## Patches NON appliqués (hors scope)

- **P4 — Shortlist 20 pictos pré-colorés** : géré dans un autre chat Claude Design d'après Benoit. À ré-intégrer plus tard via PR séparée.

## Vérification

```bash
# Type-scale lock présent
jq '.typography_lock' tokens/brand-rules-per-format.json
# Gradient lock présent
jq '.gradient_overlay_lock.canonical_value' tokens/brand-rules-per-format.json
# 4 corner brackets
ls assets/brand-elements/corner-bracket-{tl,tr,bl,br}.svg
# Verbatim mode dans content-rules
grep -A 2 "VERBATIM CONTENT MODE" docs/CONTENT-RULES.md
```

## Action requise côté Claude Design

Ajouter au bloc « Any other notes » :

```
HARD LOCKS v3.2.3:
- Font sizes ONLY in [9, 11, 14, 18, 22, 26, 36] pt + stats [72, 120].
- Font weights ONLY in [300, 400, 600, 700]. ExtraBold (800) only on cover title, section title, stat numbers. NEVER 900.
- Photo overlay: ONLY linear-gradient(135deg, rgba(28,31,59,0.85) 0%, rgba(28,31,59,0.45) 100%).
- Corner marks: L-brackets from assets/brand-elements/corner-bracket-{tl,tr,bl,br}.svg. NEVER solid squares.
- VERBATIM mode: when brief has <final_content>...</final_content> or says "verbatim / final content / do not edit", preserve user wording exactly. Do not pull examples from CONTENT-RULES.md.
```

---

## v3.2.2 — historique


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

---

## v3.2.1 — historique


**Date :** 2026-04-25
**Statut :** Push initial GitHub `benoitpof/design-system`.

---

## Corrections critiques

### `tokens/brand-rules-per-format.json` — bloc `slides` réécrit
- **Avant :** dimensions 254×190.5 mm (4:3, ratio incorrect, vestige du Google Slides standard).
- **Après :** dimensions 508×285.75 mm (16:9, LAYOUT_WIDE), vérifié depuis `Template POF - Claude.pptx` XML (`cx=18288000 cy=10287000` EMU).
- **Impact :** content_zone, header, logo, footer, corner marks ré-ancrés sur le bon canvas. Coordonnées contradictoires éliminées entre LAYOUTS.md et brand-rules.
- Suppression de `header_bar` (DESIGN.md interdit déjà les bandeaux pleine largeur sous les titres).
- Ajout des clés `title_zone`, `subtitle_zone`, `pipe_accent`, `corner_marks`.
- Convention de coordonnées : **mm partout (SSOT)**. Inches conservés dans `_inches` pour pptxgenjs.

### `docs/DESIGN.md` §4 — anchors content zone
- **Avant :** `Content zone: x=1.051 y=2.0 to edge 18.949 x 9.0` (typo : `9.0` au lieu de `max-h=8.8`).
- **Après :** tableau dual-unit (mm + inches) explicite, avec marges symétriques L/R = 26.7 mm.

### `docs/LAYOUTS.md` — global anchors dual-unit
- Ajout des coordonnées mm en miroir des inches existantes pour chaque ancrage global.
- Bloc « zone utile (safe zone) » explicité : marges, top header, bottom footer.

### `tokens/brand-tokens.json` — `logo_lockup.slide_position`
- **Avant :** x=224 y=4 w=26 h=12 mm (basé sur 4:3 obsolète).
- **Après :** x=421.3 y=20.6 w=64.5 h=16.4 mm (LAYOUT_WIDE 16:9, vérifié XML).

### Versions alignées
- README.md, brand-tokens.json, brand-rules-per-format.json, DESIGN.md → tous v3.2.1.

---

## Décisions reportées (non bloquantes)

- **15 layouts annoncés vs 12 dans le master XML Google :** écart à valider lors de la prochaine itération PowerPoint réelle (Étape 2 roadmap).
- **L11–L15 :** marqués 🔄 DRAFT. Pas encore générés en pptxgenjs.
- **Conversion exhaustive des coordonnées des layouts L01–L15 en mm :** non réalisée dans ce commit. Les inches restent la convention dans LAYOUTS.md (pour pptxgenjs natif), avec mm en commentaire pour les global anchors. À harmoniser si SSOT mm devient strict.

---

## Vérifié contre

- `Template POF - Claude (1).pptx` ppt/presentation.xml (canvas 16:9)
- `Template POF - Claude (1).pptx` ppt/slideMasters/slideMaster1.xml (placeholders title/body/footer)
- `docs/LAYOUTS.md` global anchors (cohérence inches inchangée)

---

