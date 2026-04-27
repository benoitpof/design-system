# CHANGELOG v3.3.6 — Design System POF

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
