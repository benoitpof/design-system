# POF Design System — `benoitpof/design-system`

**Version:** 3.5.0 | **Updated:** 2026-04-28
**Slide format:** LAYOUT_WIDE 20 × 11.25" (508 × 285.75 mm), 16:9
**Coordinates:** mm primary (SSOT). Inches in comments only when needed for legacy pptxgenjs code.

Source de vérité unique pour tous les assets, layouts, et règles de génération de contenus Plastic Odyssey Factories. Cross-medium consistent : web, slide deck, report A4, social media.

**Galerie visuelle :** https://benoitpof.github.io/design-system/

---

## Comment utiliser ce repo

Avant de générer un asset (slide, page, report, chart, map, icon, photo), lire ces fichiers dans cet ordre :

1. `docs/Rules/DESIGN.md` — brand DNA, hard locks (type-scale, weight, gradient, corner marks)
2. `tokens/brand-tokens.json` — colors, typography, spacing, components, entity overrides
3. `tokens/brand-rules-per-format.json` — slides, docs, web, excel, linkedin, charts, maps, icons rules
4. `docs/Layout/<MEDIUM>.md` — DECK / REPORT / WEB / SOCIAL selon le livrable
5. `docs/Rules/CONTENT-RULES.md` — narrative content rules + RAW vs FINAL confirmation step

Références spécialisées sur demande :

- `docs/Rules/ASSETS.md` — index assets + Notion Media Assets DB schema et query protocol
- `docs/Rules/ICONS.md` — Tabler CDN + brand pictos POF
- `docs/Rules/MAPS.md` — 5 patterns (heatmap, categorical, neutral dots, data dots, anchored faded)
- `docs/Rules/CHARTS.md` — 16 chart templates catalog
- `docs/Rules/PHOTOS.md` — sources autorisées, recadrage, overlay system 3 presets
- `docs/Rules/TABLES.md` — règles tableaux par medium (slide, report, web, excel)
- `assets/maps/map-charter.html` — interactive visual charter for map patterns
- `docs/Exemple/charts/index.html` — 19 ready-to-use chart/table/icon templates HTML+CSS

---

## Master template (SSOT)

**Single source of truth pour la génération deck :** `templates/master-deck-current.pptx`. Toute skill DOIT dupliquer un layout depuis ce fichier (`master.slide_layouts[i]`), jamais dessiner from-scratch.

**SHA preflight** : avant tout render, valider que le SHA-256 du master local correspond à `templates/MASTER_SHA.txt`. Mismatch = abort.

Voir `templates/README.md` pour la liste exacte des layouts (12 layouts canoniques nommés `TITLE`, `SECTION_HEADER`, `TITLE_AND_BODY`, etc.).

---

## Repo structure (v3.5.0)

```
/tokens/                            ← SSOT colors, typography, components
  brand-tokens.json
  brand-tokens.css
  brand-rules-per-format.json

/docs/
  /Rules/                           ← règles par sujet (transverses)
    DESIGN.md  CONTENT-RULES.md  ASSETS.md
    CHARTS.md  MAPS.md  ICONS.md  PHOTOS.md  TABLES.md

  /Layout/                          ← layouts par medium
    DECK.md  REPORT.md  WEB.md  SOCIAL.md

  /Memory/                          ← Rex capitalisés par ds-iterate
    deck.md  report.md  web.md  social.md
    chart.md  map.md  photo.md  icon.md

  /Exemple/                         ← exemples par type (working examples)
    /charts/   (19 HTML templates : KPI, bar, stacked, …, table, radar, map, icons, images)
    /maps/     /deck/     /report/    /web/   /social/   /tables/   /icons/   /photo/
    /Sheets/   /Other/

  /Golden/                          ← golden references (hard limit 5 par type)
    /deck/     /chart/    /map/      /report/   /web/   /social/   /photo/
    /tables/   /icons/    /Sheets/   /Other/

/assets/                            ← static brand assets
  /logos/        (4 SVG logos)
  /monogramme/   (2 SVG pictos)
  /icons/        (332 SVG, Tabler-derived, 4 variantes)
  /brand-elements/ (waves, corner brackets)
  /backgrounds/  (2 SVG bg waves)
  /maps/
    pof-world-map-blank.svg
    pof-world-map-annotated.svg
    /svg/        (7 cropped regional maps + 00-monde-cropped)
    /png-source/ (PNG sources)
    map-charter.html

/templates/                         ← master files (binary SSOT)
  master-deck-current.pptx          ← THE master, SHA-locked
  master-deck-base-layout.pptx      ← compact 16:9 alternate
  MASTER_SHA.txt                    ← preflight check
  README.md                         ← layout inventory

/site/                              ← GitHub Pages V1
  index.html  architecture.html
  charts.html  maps.html
  styles.css   _nav.js

/scripts/                           ← générateurs et outils
  build-gallery.py
  generate-pptx-layouts.js
  generate-docx-templates.js
  (à venir : composition_qa.py, path_router.py)

/.archive/                          ← archives (ne pas modifier)
  /changelogs/                      ← CHANGELOG-v3.X.X.md historiques

CHANGELOG.md                        ← historique consolidé
ITERATE.md                          ← guide ds-iterate
VISUALIZE.md                        ← URL gallery + local preview
README.md                           ← ce fichier
```

---

## Architecture v3.5.0 — 3 skills

1. **DS-Dataviz-generator** — génère charts, maps, tables atomiques. Cherche d'abord dans Notion, sinon génère depuis `docs/Exemple/charts/<id>.html` ou `assets/maps/svg/<id>.svg`.
2. **ds-file-assembler** — assemble decks, reports, web pages, social posts. Master template obligatoire (PJ ou fallback Git). SHA preflight. Layout whitelist. Visual diff vs `docs/Golden/<medium>/`.
3. **ds-iterate** — capitalise les apprentissages dans `docs/Memory/` et propose des modifs sur les `docs/Rules/` via PR.

Loops :
- **ds-feedback** (skill atomique) — log ingest des Rex en mode quick / iterate.
- **Notion = working memory** uniquement (Media Assets DB, DS Feedback DB).
- **GitHub = SSOT** : règles, golden, code, templates.

Voir `site/architecture.html` pour les diagrammes mermaid.

---

## Versioning et release

- Modif `docs/Rules/` ou `docs/Layout/` = bump patch (v3.5.1, v3.5.2, …)
- Modif `tokens/` = bump minor (v3.5.x → v3.6.0)
- Modif `templates/master-deck-current.pptx` = bump minor + nouveau `MASTER_SHA.txt`
- Modif structure repo / Skills = bump major (v3.x → v4.0)
- Toute modif passe par PR (jamais commit direct sur `main`). Voir `ITERATE.md`.

---

## Paths à ne JAMAIS utiliser (ghost paths)

Les paths suivants ne sont PAS dans ce repo. Toute skill ou doc qui les référence est buggée :

| Ghost path | Vrai path |
|---|---|
| `docs/rules/` | `docs/Rules/` |
| `docs/layouts/` | `docs/Layout/` (sans S) |
| `examples/` | `docs/Exemple/` (FR + capital E) |
| `golden/` | `docs/Golden/` |
| `memory/` | `docs/Memory/` |
| `playbooks/` | n/a (n'existe pas) |
| `evals/` | n/a (à créer si besoin) |
| `assets/maps/cooked/` | `assets/maps/svg/` |
| `tokens/colors.json` | `tokens/brand-tokens.json` (palette interne) |
| `templates/master-deck-v3.4.0.pptx` | `templates/master-deck-current.pptx` |
| `git checkout v3.4.0` | aucun tag historique avant v3.5.0, utiliser HEAD |
