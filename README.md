# POF Design System — `benoitpof/design-system`

**Version:** 3.4.0 | **Updated:** 2026-04-27
**Slide format:** LAYOUT_WIDE 20 × 11.25" (508 × 285.75 mm), 16:9
**Coordinates:** mm primary (SSOT). Inches in comments for pptxgenjs.

Source de vérité unique pour tous les assets, layouts, et règles de génération de contenus Plastic Odyssey Factories. Cross-medium consistent : web, slide deck, report A4, social media.

**Galerie visuelle :** https://benoitpof.github.io/design-system/ (à activer dans Settings → Pages → main / `/site` folder)

---

## Comment utiliser ce repo

Avant de générer un asset (slide, page, report, chart, map, icon, photo), lire ces fichiers dans cet ordre :

1. `docs/rules/DESIGN.md` — brand DNA, hard locks (type-scale, weight, gradient, corner marks)
2. `tokens/brand-tokens.json` — colors, typography, spacing, components, entity overrides
3. `tokens/brand-rules-per-format.json` — slides, docs, web, excel, linkedin, charts, maps, icons rules
4. `docs/layouts/<MEDIUM>.md` — DECK / REPORT / WEB / SOCIAL selon le livrable
5. `docs/rules/CONTENT-RULES.md` — narrative content rules + RAW vs FINAL confirmation step

Références spécialisées sur demande :

- `docs/rules/ASSETS.md` — index assets + Notion Media Assets DB schema et query protocol
- `docs/rules/ICONS.md` — Tabler CDN + brand pictos POF
- `docs/rules/MAPS.md` — 5 patterns (heatmap, categorical, neutral dots, data dots, anchored faded)
- `docs/rules/CHARTS.md` — 16 chart templates catalog
- `docs/rules/PHOTOS.md` — sources autorisées, recadrage, overlay system 5 presets
- `docs/rules/TABLES.md` — règles tableaux par medium (slide, report, web, excel)
- `assets/maps/map-charter.html` — interactive visual charter for map patterns
- `examples/charts/index.html` — 16 ready-to-use chart templates HTML+CSS

---

## Repo structure (v3.4.0)

```
/tokens/                   ← SSOT colors, typography, components
  brand-tokens.json
  brand-tokens.css
  brand-rules-per-format.json

/docs/
  /rules/                  ← règles par sujet (transverses)
    DESIGN.md  CONTENT-RULES.md  ASSETS.md
    CHARTS.md  MAPS.md  ICONS.md  PHOTOS.md  TABLES.md
  /layouts/                ← layouts par medium
    DECK.md  REPORT.md  WEB.md  SOCIAL.md

/memory/                   ← Rex capitalisés par ds-iterate
  deck.md  report.md  web.md  social.md
  chart.md  map.md  photo.md  icon.md

/assets/                   ← static brand assets
  /logos/  /pictos/  /icons/  /brand-elements/  /backgrounds/  /maps/

/examples/                 ← exemples par type (avec subdirs)
  /charts/  /maps/  /deck/  /report/  /web/  /social/
  /email-signatures/  /excel/

/golden/                   ← golden references (hard limit 5 par type)
  /deck/  /chart/  /map/  /report/  /web/  /social/  /photo/

/templates/                ← master files binaires (pptx, docx, html)

/site/                     ← GitHub Pages V1
  index.html  architecture.html  styles.css  _nav.js

/scripts/                  ← générateurs et outils
  generate-docx-templates.js
  generate-pptx-layouts.js
  (à venir : pof-asset-render.py, composition-qa.py, build-gallery.py)

/.archive/                 ← archives (ne pas modifier)
  /changelogs/             ← 16 CHANGELOG-v3.X.X.md historiques

CHANGELOG.md               ← historique consolidé
ITERATE.md                 ← guide ds-iterate
VISUALIZE.md               ← URL gallery + local preview
README.md                  ← ce fichier
```

---

## Architecture v3.4.0 — 3 skills

1. **DS-Dataviz-generator** — génère charts, maps, tables. Cherche d'abord dans Notion, sinon génère.
2. **ds-file-assembler** — assemble decks, reports, web pages, social posts. Orchestre DS-Dataviz-generator.
3. **ds-iterate** — capitalise les apprentissages dans `memory/` et propose des modifs sur les `rules/`.

Loops :
- **ds-feedback** (skill atomique) — log ingest des Rex en mode quick / iterate.
- **Notion = working memory** uniquement (Media Assets DB, DS Feedback DB).
- **GitHub = SSOT** : règles, golden, code, templates.

Voir `site/architecture.html` pour les diagrammes mermaid.

---

## Versioning et release

- Modif règles (rules/) ou layouts (layouts/) = bump patch (v3.4.1 → v3.4.2)
- Modif tokens/ = bump minor (v3.4.x → v3.5.0)
- Modif structure repo / Skills = bump major (v3.x.x → v4.0.0)
- Toute modif passe par PR (jamais commit direct sur main). Voir `ITERATE.md`.

