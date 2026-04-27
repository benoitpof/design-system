# PHOTOS.md — POF Photography Rules

**Version:** 3.4.0 | **Updated:** 2026-04-27
**Status:** Scaffolding initial. À enrichir via ds-iterate.

---

## Sources autorisées

- Photos terrain POF (CDF, équipes, sites) : Notion `Media Assets` DB collection `8ca51a75-2413-4f72-8f2a-c44d445fa1d0`, Usage = Photo
- Photos partenaires validées : Notion DB Usage = Partner Photo
- **Forbidden** : stock photo générique, render 3D, IA générative, hands holding earth

## Recadrage

- Format slide deck : 16:9 ou 4:3 selon zone
- Format report A4 : 3:2 ou 4:3 (jamais étiré)
- Format social square : 1:1 centré sur le sujet humain
- Crop : human first, subject filling 60% of frame minimum

## Overlay system (rappel — voir DESIGN.md pour spec complète)

5 presets nommés (réduction des 96 combinaisons brutes) :

| Preset | Usage | Valeur |
|---|---|---|
| `cover_hero` | L01 cover slide | gradient navy 0% → 90% from_bottom |
| `section_dark` | L02 section divider | solid heavy 90% |
| `kpi_photo_side` | L04 KPI sur photo | gradient navy 0% → 60% from_left |
| `quote_dim` | L15 callout | solid medium 60% |
| `decorative_no_text` | Pure décoratif | solid light 30% |

## Forbidden

- Distortion (stretch non-uniforme)
- Multi-photo collage sans grille définie
- Filtre IG natif (saturation excessive, vignette)
- Cadre gris autour des photos (banni v3.3.x)
- Bords arrondis sauf composants UI (cards web)

## Memory — Rex

<!-- ds-iterate écrit ici -->

## Exemples golden

Voir `/golden/photo/` (max 5 par usage).
