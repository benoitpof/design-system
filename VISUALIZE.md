# VISUALIZE.md — GitHub Pages gallery

**URL :** https://benoitpof.github.io/design-system/ (à activer dans Settings → Pages → Source : main / `/site` folder)

## Structure

`/site/index.html` est le point d'entrée. Il liste tous les contenus du DS par catégorie :
- Master content layouts (Deck, Report, Web, Social)
- Asset rules & catalogs (DESIGN, CONTENT-RULES, CHARTS, MAPS, ICONS, PHOTOS, TABLES, ASSETS)
- Tokens & assets bruts (logos, icons, maps, brand-elements)
- Examples & goldens (Chart Bank, Map Charter, Email signatures, Excel)
- Skills & iteration (memory, ITERATE, CHANGELOG)

`/site/architecture.html` montre l'architecture v3.4.0 avec 3 diagrammes mermaid : couches, flux génération, cycle itération.

## Local preview

```bash
cd site/ && python3 -m http.server 8080
# Ouvrir http://localhost:8080
```

## Deploy automatique (V2 sprint suivant)

GitHub Action `.github/workflows/pages.yml` (à créer) :
- Trigger : push sur main
- Steps : checkout → run `scripts/build-gallery.py` → deploy `/site/` vers GitHub Pages
- Le script Python régénère index.html à partir de l'arborescence du repo (assets, examples, golden, memory)

## Privacy

Pour scope POF only : Cloudflare Access devant le custom domain. Voir spec Notion.
