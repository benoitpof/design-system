# SOCIAL.md — POF Social Media Layouts

**Version:** 3.4.0 | **Updated:** 2026-04-27
**Status:** Scaffolding initial. À enrichir après 5 publications produites.
**Médium :** Image statique (PNG/JPG export 72 DPI), parfois vidéo courte.

---

## Formats canoniques

| ID | Plateforme | Usage | Dimensions |
|---|---|---|---|
| S01 | LinkedIn post | Image carrée single-post | 1200 × 1200 px (1:1) |
| S02 | LinkedIn banner | Image rectangulaire post | 1200 × 628 px (1.91:1) |
| S03 | LinkedIn carousel | PDF multi-pages | 1080 × 1080 px (1:1), 5-10 pages |
| S04 | Instagram feed | Square post | 1080 × 1080 px (1:1) |
| S05 | Instagram story | Vertical | 1080 × 1920 px (9:16) |
| S06 | Twitter / X post | Image inline | 1200 × 675 px (16:9) |

## Cadre général

- Logo POF : top-right ou bottom-right (jamais centré)
- Police titre : **Poppins** ExtraBold 64 pt minimum (lisible mobile)
- Police corps : **Raleway** SemiBold 32 pt minimum
- Fond : navy `#1C1F3B` ou photo + overlay heavy (90%) pour lisibilité texte
- Coral `#E8546C` réservé à 1 mot d'emphase max par visuel
- Hashtags : pas dans le visuel, dans la caption uniquement

## Règles spécifiques social

- Mobile-first : tout doit rester lisible à 375 px de large
- Texte critique au centre, jamais bord cadre
- Pas de filtre Instagram natif (incohérent charte)
- Pas d'emoji dans les visuels (caption only)
- Watermark POF jamais flou, jamais translucide < 50%

## Memory — capitalisation Rex

<!-- ds-iterate écrit ici -->

## Exemples golden

Voir `/golden/social/` (max 5 par format).

---

## Chart usage on social

Social posts use simplified chart variants from `examples/charts/` adapted to small viewport reading distance (mobile, 50cm).

| Format | Recommended charts | Notes |
|---|---|---|
| S01 LinkedIn 1:1 | `01-kpi.html` (single big number) | Coral highlight on lead KPI |
| S02 LinkedIn 1.91:1 | `02-bar` 3 categories max, `06-donut` 4 slices max | Title 64pt min |
| S03 LinkedIn carousel | Mix : KPI cover + chart + insight | 5-10 slides |
| S04 IG feed | Quote + 1 KPI + photo | Photo overlay heavy |
| S05 IG story | Single stat, vertical layout | No chart, just KPI + icon |
| S06 X post | `01-kpi.html` simplified | Max 2 datapoints |

**Hard rule:** any chart on social must pass mobile-readability check — minimum text size 32pt at 1080px width. Coral max 1 element. Logo POF + corner bracket teal mandatory.

## Cross-references

- Hard locks: `rules/HARD-LOCKS.md`
- Chart catalog: `rules/CHARTS.md`
- Photo overlays: `rules/PHOTOS.md`
- Icons (env/impact): `assets/icons/ecology/` + `rules/ICONS.md`
- Brand DNA + voice: `DESIGN.md` (root) + `rules/CONTENT-RULES.md`
