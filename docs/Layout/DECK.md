# DECK.md — POF Canonical Slide Layouts (15)

**Version:** 3.4.1 | **Updated:** 2026-04-27
**Format:** LAYOUT_WIDE — 20" × 11.25" (508 × 285.75 mm), 16:9
**SSOT binaire :** `templates/master-deck-v3.4.0.pptx`
**Status:** ✅ VALIDATED layouts L01-L09 · 🔄 DRAFT L10-L15 (à remplir au fil des productions)

**Convention coords :** mm partout (SSOT). Inches conservés en commentaires pour pptxgenjs (× 25.4 → mm).

---

## Ancrages globaux (tous layouts)

```
Canvas:          20.0"  × 11.25"   (508.0 × 285.75 mm)
Logo:            x=421.3 y=20.6 w=64.5 h=16.4 mm   (top-right, sauf L01)
Logo L01 cover:  x=26.7  y=12.7 w=88.9 h=22.6 mm   (top-left, format élargi)
Corner TL:       x=19.0  y=16.3 w=7.7  h=7.7 mm    teal grpSp décoratif
Corner BR:       x=483.2 y=265.5 w=7.7 h=7.7 mm    teal grpSp décoratif
Slide number:    x=470.7 y=259.1 w=30.5 h=21.9 mm  Raleway 11pt steel
Title:           x=26.7  y=20.6 w=231.3 h=10.3 mm  Poppins ExtraBold 26pt teal ou white
Subtitle:        x=26.7  y=31.4 w=243.1 h=12.0 mm  Raleway SemiBold 26pt navy
Pipe accent:     x=19.0  y=19.05 w=1.4 h=12.2 mm   teal vertical bar à gauche du titre
Content zone:    x=26.7  y=50.8 max-w=454.6 max-h=223.5 mm
Footer source:   x=26.7  y=270.0 w=350.0 h=8.0 mm  Raleway Light 9pt steel italique
```

**Zone utile (safe zone) :** marges 26.7 mm L/R, 50.8 mm top, 11.4 mm bottom. Aucun contenu critique en dehors. Corner marks teal débordent volontairement.

---

## Backgrounds canoniques (4 types)

| ID | Type | Usage | Asset |
|---|---|---|---|
| BG_LIGHT | Fond clair `#F9FCFF` | Layouts texte standard (L02-L08, L13-L14) | none |
| BG_DARK | Fond navy `#1C1F3B` plein | L01 cover, L15 callout | none |
| BG_PHOTO_OVERLAY | Photo full-bleed + overlay 3-type system | L01 cover, L02 section, L09 map | `assets/backgrounds/bg-wave-02.svg` ou photo Notion |
| BG_WAVE_BAND | Bandeau navy gradient + waves | L04 KPI, L11 quote | `assets/backgrounds/bg-wave-01.svg` 1920×540 |

**Overlay system (3 types — voir `docs/Rules/PHOTOS.md`) :**
- `type_1_white_fade` : carte ou photo avec fade blanc sur les bords (default L09 maps, L13 timeline si photo)
- `type_2_navy_gradient` : photo + gradient navy from-bottom (default L01 cover)
- `type_3_solid_dark` : photo + voile navy uniforme medium (default L02 section)

---

## L01 — COVER (full-bleed photo + overlay navy)

**Background :** BG_PHOTO_OVERLAY type_2_navy_gradient
**Logo :** top-LEFT format élargi (x=26.7, y=12.7, w=88.9, h=22.6 mm) — couleur `pof-logo-teal-white.svg`
**Title :** centré horizontalement, y=140-180mm. Poppins ExtraBold 36pt white. Max 4 mots, 3 lignes.
**Subtitle :** sous title, Poppins SemiBold 22pt white. 1 phrase max.
**Eyebrow :** top, y=70mm, Poppins SemiBold 11pt teal letter-spacing 2px UPPERCASE. Format `<TYPE> · <YEAR>`.
**Date/lieu :** bottom-left, y=260mm, Raleway Regular 14pt white. Format `Dakar, Senegal · April 2026`.
**Corner marks :** **NONE** (incompatible avec logo top-left).
**Pipe :** **NONE** (cover sans pipe).

**Forbidden :** 
- Logo en top-right (réservé aux autres layouts)
- Photos stock / IA / hands holding earth
- Plus de 4 mots dans le title

---

## L02 — SECTION DIVIDER (photo + overlay navy heavy)

**Background :** BG_PHOTO_OVERLAY type_3_solid_dark (overlay navy 80%)
**Logo :** top-right standard
**Roman numeral :** centré horizontalement, y=120mm. Poppins ExtraBold 120pt teal `#80C7C2` opacity 0.4. Format `I`, `II`, `III`...
**Section title :** sous le numeral, y=180mm, Poppins ExtraBold 36pt white. UPPERCASE ou Title Case.
**Section descriptor :** sous title, Raleway Regular 18pt white opacity 0.85. 1 phrase 12 mots max.
**Corner marks :** TL + BR teal.
**Pipe :** none.

**Forbidden :**
- Section title en multi-ligne (1 ligne stricte)
- Photo de transition générique (doit être contextuelle au sujet de la section)

---

## L03 — CONTENT + IMAGE (split 50/50)

**Background :** BG_LIGHT
**Logo :** top-right standard
**Title :** standard (x=26.7, y=20.6) Poppins ExtraBold 26pt teal
**Subtitle :** standard Raleway SemiBold 22pt navy
**Pipe :** TL teal, à gauche du titre
**Content gauche :** 50% width (w=216 mm), texte en bullet points ou paragraphes courts. Max 3 niveaux d'indentation.
**Image droite :** 50% width (x=270, y=80, w=212, h=148 mm), overlay type_1_white_fade si photo paysage.
**Source caption :** bottom-left, Raleway Light 9pt steel italique
**Corner marks :** TL + BR teal

---

## L04 — BIG NUMBER / KPI (1 à 3 callouts)

**Background :** BG_LIGHT ou BG_WAVE_BAND
**Logo :** top-right standard
**Title :** standard
**Subtitle :** standard, court
**Pipe :** TL teal
**KPI block(s) :** centrés verticalement, y=130-200mm.
- **1 KPI :** centré horizontalement. Number 120pt Poppins ExtraBold navy. Label sous-jacent 18pt Raleway Regular steel.
- **2 KPIs :** alignés horizontalement, gap 60mm. Number 72pt.
- **3 KPIs :** alignés horizontalement, gap 30mm. Number 64pt.
**Source caption :** bottom-left
**Corner marks :** TL + BR teal

**Couleurs :** Number en navy `#1C1F3B`. Si highlight critique : 1 number en coral `#E8546C` max sur 3.
**Forbidden :** 4 KPIs ou plus sur la même slide (split en 2 slides).

---

## L05 — VALUE PROPOSITION (3 cards horizontal)

**Background :** BG_LIGHT
**Logo :** top-right standard
**Title :** standard Poppins ExtraBold 26pt teal
**Subtitle :** standard
**Pipe :** TL teal
**3 cards :** alignés horizontalement, y=80mm, w=140mm chacune, gap 20mm.
- Card header : Poppins SemiBold 18pt navy, max 3 mots
- Card icon (optional) : 32px Tabler ou POF picto, navy. **Considérer mais pas imposer**
- Card body : Raleway Regular 14pt body, max 4 lignes
- Card border : 1px steel-pale, border-radius 4mm

**Forbidden :** 4 cards ou plus (si besoin, splitter ou utiliser L08 table).

---

## L06 — PROCESS FLOW (3 à 5 steps horizontal)

**Background :** BG_LIGHT
**Logo :** top-right standard
**Title :** standard
**Subtitle :** standard
**Pipe :** TL teal
**Steps :** alignés horizontalement, y=120mm.
- Numéroter 01, 02, 03 (Poppins ExtraBold 22pt teal)
- Header step : Poppins SemiBold 18pt navy
- Body step : Raleway Regular 12pt body, 1 ligne
- Connector arrow : SVG path UNIQUE (M x1 y1 L x2 y2 + markerEnd integré). **Jamais 2 éléments séparés.**
- Color sequence : navy → navy_medium → steel → steel_light → teal (highlight final si critical)

**Forbidden :** 6 steps ou plus.

---

## L07 — BAR CHART

**Background :** BG_LIGHT
**Logo :** top-right standard
**Title :** standard (titre du chart)
**Subtitle :** standard (sous-titre du chart, contexte)
**Pipe :** TL teal
**Chart :** centré, y=80mm, w=400, h=180 mm. SVG embedded, généré via `DS-Dataviz-generator type=chart template=02-bar`.
**Source caption :** bottom-left, OBLIGATOIRE pour chart.
**Corner marks :** TL + BR

**Voir `docs/Rules/CHARTS.md`** pour palette, forbidden, data accuracy.

---

## L08 — TABLE (financial / comparison)

**Background :** BG_LIGHT
**Logo :** top-right standard
**Title :** standard
**Subtitle :** standard (contexte du tableau)
**Pipe :** TL teal
**Table :** centrée, y=80mm.
- Header row : navy `#1C1F3B`, white text, Poppins SemiBold 11pt
- Data rows : alternance white / `#F9FCFF` (zebra)
- Numbers right-align, max 2 décimales sauf %
- Negatives en coral `#E8546C` (pas de parenthèses)
- Max 8 cols, max 12 rows par slide
**Source caption :** bottom-left

**Voir `docs/Rules/TABLES.md`.**

---

## L09 — MAP / GEOGRAPHIC

**Background :** BG_LIGHT ou BG_PHOTO_OVERLAY (si carte sur photo)
**Logo :** top-right standard
**Title :** standard
**Subtitle :** standard
**Pipe :** TL teal
**Map :** anchored faded-edge Pattern 5 (jamais centrée flottante). x=170mm right-anchored ou left-anchored.
- Edge fade overlays type_1_white_fade obligatoires sur les bords
- Pays POF actifs en navy `#1C1F3B`
- Pays pipeline en steel `#435D74`
- Pays featured en teal `#80C7C2`
- Cluster overlays : circles (single r), JAMAIS ellipses

**Voir `docs/Rules/MAPS.md` pour 5 patterns.**

---

## L10 — SWOT (2x2 grid)

**Background :** BG_LIGHT
**Logo :** top-right standard
**Title :** standard
**Pipe :** TL teal
**4 quadrants :** y=80mm, alignés en grille 2x2, gap 10mm chacun.
- Top-left : Strengths (header navy, body steel)
- Top-right : Weaknesses (header coral, body steel)
- Bottom-left : Opportunities (header teal, body steel)
- Bottom-right : Threats (header navy_medium, body steel)
- Header quadrant : Poppins SemiBold 14pt UPPERCASE
- Body : Raleway Regular 11pt, bullets max 4 par quadrant

🔄 DRAFT — à valider avec exemple golden.

---

## L11 — QUOTE / TESTIMONIAL

**Background :** BG_WAVE_BAND ou BG_LIGHT
**Logo :** top-right standard
**Title :** none (le quote est le focus)
**Subtitle :** none
**Quote :** centrée, y=120mm, w=350mm. Poppins SemiBold 28pt navy italique. Max 3 lignes, 25 mots.
**Author photo :** circulaire, w=60mm h=60mm, à gauche du quote OU sous le quote centré
**Author name :** Poppins SemiBold 16pt navy
**Author role :** Raleway Regular 12pt steel
**Pipe :** none

🔄 DRAFT — à valider.

---

## L12 — TEAM (grid de portraits)

**Background :** BG_LIGHT
**Logo :** top-right standard
**Title :** standard
**Subtitle :** standard
**Pipe :** TL teal
**Grid :** 4-6 portraits par row, max 2 rows.
- Photo circulaire ou rectangulaire ratio 3:4
- Nom : Poppins SemiBold 14pt navy sous photo
- Rôle : Raleway Regular 11pt steel
- Si photo manquante : initiales fond steel-pale

🔄 DRAFT — à valider.

---

## L13 — TIMELINE (horizontal milestones)

**Background :** BG_LIGHT
**Logo :** top-right standard
**Title :** standard
**Subtitle :** standard
**Pipe :** TL teal
**Timeline axis :** ligne horizontale navy 2px, y=150mm
**Milestones :** dots teal/navy/coral selon importance, label année + descripteur
**Color sequence :** navy → steel → teal (highlight) → coral (key milestone)

🔄 DRAFT — à valider.

---

## L14 — COMPARISON (2 colonnes side-by-side)

**Background :** BG_LIGHT
**Logo :** top-right standard
**Title :** standard
**Subtitle :** standard
**Pipe :** TL teal
**2 colonnes :** y=80mm, w=215mm chacune, gap 30mm.
- Header colonne : Poppins SemiBold 18pt UPPERCASE
- Items list : checkboxes ou bullets, Raleway Regular 14pt body
- Color cue : colonne gauche neutral (steel), colonne droite highlight (teal ou navy bold)

🔄 DRAFT — à valider.

---

## L15 — CALLOUT / KEY MESSAGE (dark, full-bleed)

**Background :** BG_DARK navy plein OU BG_WAVE_BAND
**Logo :** top-right teal-white version
**Title :** none (le message EST le titre)
**Eyebrow :** top, Poppins SemiBold 11pt teal letter-spacing 2px UPPERCASE
**Message :** centré, y=130mm, Poppins ExtraBold 44pt white. Max 12 mots, 3 lignes.
**Highlight :** 1-2 mots max en coral `#E8546C` ou teal `#80C7C2`
**Pipe :** TL teal vertical

**Forbidden :** plus de 12 mots dans le message.

---

## Memory — capitalisation Rex (v3.4.0)

<!-- ds-iterate écrit ici. Format : ### YYYY-MM-DD — <titre> -->

(vide pour l'instant)
