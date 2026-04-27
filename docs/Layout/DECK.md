# LAYOUTS.md — POF Canonical Slide Layouts

**Format:** LAYOUT_WIDE — 20" × 11.25" (508 × 285.75 mm), 16:9 (pptxgenjs `pres.layout = 'LAYOUT_WIDE'`)
**Colors:** navy=#1C1F3B · teal=#80C7C2 · coral=#E8546C · light=#F9FCFF · steel=#435D74
**Status:** ✅ VALIDATED | 🔄 DRAFT — validate before generating at scale

**Convention:** SSOT en mm (`tokens/brand-rules-per-format.json`). Inches conservés ci-dessous pour pptxgenjs (× 25.4 → mm).

---

## Global anchors (all layouts — verified from Template POF XML)

```
Canvas:          20" × 11.25"   (508 × 285.75 mm)
Logo:            x=16.587 y=0.810 w=2.541 h=0.645   (mm: x=421.3 y=20.6 w=64.5 h=16.4)
Corner TL:       x=0.748  y=0.642 w=0.303 h=0.303   (mm: x=19.0  y=16.3 w=7.7  h=7.7)   teal grpSp mark
Corner BR:       x=19.025 y=10.454 w=0.303 h=0.303  (mm: x=483.2 y=265.5 w=7.7 h=7.7)   teal grpSp mark
Slide number:    x=18.531 y=10.200 w=1.200 h=0.861  (mm: x=470.7 y=259.1 w=30.5 h=21.9)
Title:           x=1.051  y=0.810 w=9.106 h=0.404   (mm: x=26.7 y=20.6 w=231.3 h=10.3)  Poppins ExtraBold 26pt teal or white
Subtitle:        x=1.051  y=1.237 w=9.570 h=0.471   (mm: x=26.7 y=31.4 w=243.1 h=12.0)  Raleway SemiBold 26pt navy
Pipe accent:     x=0.748  y=0.75  w=0.055 h=0.48    (mm: x=19.0 y=19.05 w=1.4 h=12.2)   teal vertical bar left of title
Content zone:    x=1.051  y=2.0   max-w=17.898 max-h=8.8  (mm: x=26.7 y=50.8 max-w=454.6 max-h=223.5)
```

**Zone utile (safe zone) :** marges symétriques 26.7 mm L/R, 50.8 mm top (header logo+title+subtitle), 11.4 mm bottom (footer slide number). Aucun contenu critique en dehors. Les corner marks teal sont décoratifs et débordent volontairement de la zone utile.

---

## L01 — COVER (dark, full-bleed)

**Status:** 🔄 DRAFT
**Use:** Opening slide — photo right half, text left, dark bg

```
bg:              navy #1C1F3B (or bg-wave-02.svg full-bleed)
No logo on master — add pof-logo-white x=1.051 y=0.5 w=3.5 (larger on cover)
Photo zone:      x=9.54 y=1.53 w=10.46 h=6.08  full-bleed right — sizing=cover
Navy overlay:    x=9.54 y=0 w=10.46 h=11.25    bg=1C1F3B transparency=45
Wave:            assets/brand-elements/wave-white.svg x=0 y=8.5 w=7 opacity=0.3
Title:           x=1.051 y=3.2 w=8.0 Poppins ExtraBold 36pt white uppercase
Subtitle:        x=1.051 y=4.8 w=8.0 Raleway SemiBold 26pt teal
Date/context:    x=1.051 y=5.8 w=6.0 Raleway Regular 22pt F9FCFF
Slogan:          x=1.051 y=7.0 w=7.0 Raleway ExtraBold 26pt — words alternating white/teal
```

---

## L02 — SECTION DIVIDER

**Status:** 🔄 DRAFT
**Use:** Between major sections in long decks

```
bg:              navy #1C1F3B (or bg-wave-01.svg full-bleed)
Section number:  Poppins Bold 120pt teal opacity=0.2 x=14.0 y=0.5
Section title:   Poppins ExtraBold 40pt white uppercase x=1.051 y=4.0
Subtitle:        Raleway SemiBold 26pt teal x=1.051 y=5.8
Logo:            pof-logo-white x=16.587 y=0.810 w=2.541
Corners:         standard teal grpSp marks
```

---

## L03 — CONTENT + IMAGE (50/50 split)

**Status:** 🔄 DRAFT
**Use:** Product presentation, site description, case study

```
bg:              white #FFFFFF
Title:           standard (teal)
Subtitle:        standard (navy)
Text zone:       x=1.051 y=2.0 w=8.4 h=8.8
  H2:            Poppins SemiBold 22pt navy
  Body:          Raleway Regular 22pt #1C1F3B
  Bullets:       bullet=true Raleway 22pt, indentLevel=0
Image zone:      x=9.54 y=0 w=10.46 h=11.25 — full-bleed right — sizing=cover
  (Matches slide 12/13 pattern: x=9.54 y=1.53 w=10.46 h=6.08 for smaller image)
```

---

## L04 — BIG NUMBER / STATS (1–3 callouts)

**Status:** 🔄 DRAFT
**Use:** Impact KPIs — matches slide 5 and 15 patterns

```
bg:              navy #1C1F3B or white
Photo zone:      x=1.051 y=2.45 w=8.71 h=7.99  left image (slide 5 pattern)
Stats zone:      x=10.25 y=3.69 to right edge — stacked teal boxes

Per stat box:
  Outer box:     x=10.25 y=3.69 w=8.71 h=2.27 bg=05387B
  Inner text:    x=11.44 y=3.69 w=7.29 h=2.02
    Number:      Raleway ExtraBold 120pt teal
    Label:       Raleway Bold 24pt white
  Second box:    x=10.25 y=6.33 w=8.71 h=2.43 (same pattern)

Variant (3 cols on white):
  3 cols:        w=5.6" each, gutter=0.4" y=3.0
    Number:      Raleway ExtraBold 72pt navy centered
    Unit:        Poppins SemiBold 30pt teal
    Label:       Raleway Regular 22pt steel
    Wave:        wave-teal.svg w=2.5" centered below
```

---

## L05 — VALUE PROPOSITION (3 cards)

**Status:** 🔄 DRAFT
**Use:** What we provide — machines, training, market, finance

```
bg:              white
Title:           standard
3 cards:         y=2.0 h=8.0 gutter=0.4" x_start=1.051
  card-w:        5.8"
  bg:            F9FCFF
  Teal top bar:  w=full h=0.25" bg=80C7C2
  Icon:          Tabler 48×48px navy x=0.3" y=0.5" from card
  Title:         Poppins SemiBold 22pt navy x=0.3" y=1.1"
  Body:          Raleway Regular 20pt #1C1F3B x=0.3" y=1.7" max 5 lines
```

---

## L06 — PROCESS FLOW (3–5 steps)

**Status:** 🔄 DRAFT
**Use:** How the franchise works, deployment steps

```
bg:              white
Title:           standard
Connector line:  y=5.2" x=1.5" w=17.0" h=0 line=0.5pt navy
Steps (max 5):   y=4.0" centered row
  Circle:        d=1.4" bg=1C1F3B number Poppins Bold 28pt white centered
  Title:         Poppins SemiBold 22pt navy below circle centered w=3.0"
  Body:          Raleway 20pt #1C1F3B below title w=3.0" 3 lines max
  Arrows:        → 0.5pt navy between circles
```

---

## L07 — BAR CHART

**Status:** 🔄 DRAFT
**Use:** Revenue by year, factories deployed, tonnage — inspired by Corn Farm slide 11/12

```
bg:              white
Title:           standard
Chart:           pptxgenjs addChart BAR x=1.051 y=2.0 w=14.0 h=8.0
  barDir:        'col'
  chartColors:   ['1C1F3B', '435D74', 'CFD9E0', '80C7C2']
  chartArea:     fill white, no border
  valGridLine:   color=EAEBED size=0.5
  catGridLine:   style='none'
  catAxisLabelColor: '6C757D'
  valAxisLabelColor: '6C757D'
  showValue:     true  dataLabelPosition='outEnd'  dataLabelColor='1C1F3B'
  showLegend:    true if >1 series, legendPos='r'

Stat callout:    optional — x=15.5 y=2.0 w=3.5 h=3.0
  bg:            1C1F3B
  Number:        Raleway ExtraBold 48pt teal centered
  Label:         Raleway Regular 22pt white centered

Source note:     x=1.051 y=10.5 Raleway Light 18pt steel italic
```

---

## L08 — TABLE

**Status:** 🔄 DRAFT
**Use:** Comparative specs, financial summary, franchise terms — inspired by Corn Farm slide 12

```
bg:              white
Title:           standard
Table:           x=1.051 y=2.0 w=17.898 (addTable)
  Header row:    fill={color:'1C1F3B'} Poppins SemiBold 18pt white bold=true h=0.55"
  Data rows:     h=0.45" alternating bg FFFFFF / F9FCFF
  Cell font:     Raleway Regular 18pt #1C1F3B
  No borders
  First col:     Poppins SemiBold 18pt navy w=3.5" (row label)
  Max rows:      12 — split beyond that
  colW:          distribute based on content — first col wider

Caption:         x=1.051 y=10.5 Raleway Light 18pt steel italic — source/note
```

---

## L09 — MAP / GEOGRAPHIC

**Status:** 🔄 DRAFT
**Use:** Deployment countries, 3 regional clusters

```
bg:              white
Title:           standard
Map zone:        x=1.051 y=2.0 w=12.5 h=8.5
  SVG flat map   generated or inserted as image
  Inactive:      EAEBED · Active: 1C1F3B · Pipeline: 435D74
  Deployed dot:  80C7C2 circle
Legend:          x=14.0 y=2.5 w=4.9
  Items:         Raleway 20pt navy, dot icon, gap=0.4"
Stat callout:    x=14.0 y=6.0 w=4.9 h=2.5 bg=1C1F3B
  Number:        Raleway ExtraBold 48pt teal
  Label:         Raleway Regular 22pt white
```

---

## L10 — SWOT

**Status:** 🔄 DRAFT
**Use:** Strategic analysis — inspired by Biomass slide 12 (lettered quadrants)

```
bg:              white
Title:           standard
4 quadrants:     2×2 grid gutter=0.24" x=1.051 y=2.0
  Each cell:     w=8.8" h=4.2"
  S top-left:    bg=1C1F3B — giant letter "S" Poppins Bold 96pt teal opacity=0.15
                 title Poppins SemiBold 22pt white — items Raleway 20pt white
  W top-right:   bg=F9FCFF — letter "W" navy opacity=0.1 — title+items navy
  O bot-left:    bg=80C7C2 — letter "O" navy opacity=0.15 — title+items NAVY (never white on teal)
  T bot-right:   bg=EAEBED — letter "T" navy opacity=0.1 — title+items navy
  Max items:     4 per cell — Raleway Regular 20pt
```

---

## L11 — QUOTE / TESTIMONIAL

**Status:** 🔄 DRAFT
**Use:** Franchisee quote, partner statement — inspired by Biomass slide 7

```
bg:              white
Title:           standard
Left border:     x=1.051 y=2.2 w=0.22" h=5.5" bg=80C7C2
Quote text:      x=1.5 y=2.4 w=14.0 Poppins SemiBold 28pt navy italic line-height=1.3
Attribution:     x=1.5 y=7.0 Raleway Regular 22pt steel
Role/org:        x=1.5 y=7.6 Raleway Light 20pt steel
Portrait:        optional — circle d=3.0" x=16.5 y=3.5 rounding=true
```

---

## L12 — TEAM

**Status:** 🔄 DRAFT
**Use:** Team, advisory board — inspired by Biomass slide 16

```
bg:              white
Title:           standard
Grid 4 per row:  y=2.2 gutter=0.3"
  Portrait:      circle d=3.0" rounding=true
  Name:          Poppins SemiBold 22pt navy below centered
  Role:          Raleway Regular 20pt steel centered
  col-x spacing: (20 - 2×1.051 - 4×3.0) / 3 = 1.299" gap
Max:             8 persons (2 rows of 4)
```

---

## L13 — TIMELINE

**Status:** 🔄 DRAFT
**Use:** Company history, deployment roadmap 2022–2030

```
bg:              white
Title:           standard
Axis line:       y=5.5 x=1.5 to x=18.5 h=0 line=0.5pt navy
Milestones (max 6):
  Dot past:      d=0.55" bg=80C7C2 on axis
  Dot future:    d=0.45" bg=435D74 dashed axis
  Year:          Poppins SemiBold 20pt navy above dot y=4.8
  Label:         Raleway Regular 20pt #1C1F3B below dot y=6.2 w=2.5" 3 lines
```

---

## L14 — COMPARISON (2 columns)

**Status:** 🔄 DRAFT
**Use:** Before/after, POF vs NGO model, option A vs B

```
bg:              white
Title:           standard
Divider:         x=10.0 y=2.0 h=8.5 w=0 line=0.5pt navy
Left col:        x=1.051 y=2.0 w=8.5
Right col:       x=10.5  y=2.0 w=8.5
Per column:
  Optional badge: highlight color block — teal or coral — above title
  Title:         Poppins SemiBold 26pt navy uppercase
  Teal accent:   rect x=0 y=title_bottom w=2.5" h=0.18" bg=80C7C2
  Items:         Raleway 22pt #1C1F3B bullet=true gap=0.2"
```

---

## L15 — CALLOUT / KEY MESSAGE (dark)

**Status:** 🔄 DRAFT
**Use:** Closing ask, target statement, investment thesis

```
bg:              navy #1C1F3B
Wave:            wave-white.svg x=0 y=7.0 w=7.0 opacity=0.25
Logo:            pof-logo-white standard position
Corners:         standard teal grpSp
Label:           x=1.051 y=2.5 Poppins SemiBold 22pt teal uppercase
Main message:    x=1.051 y=3.2 w=15.0 Poppins ExtraBold 40pt white line-height=1.2 max 2 lines
Sub text:        x=1.051 y=6.5 Raleway SemiBold 26pt teal
```

---

## Layout → Use case quick reference

| ID | Layout | Typical slide in a POF deck |
|----|--------|---------------------------|
| L01 | Cover | Slide 1 |
| L02 | Section divider | Between Problem / Solution / Model / Impact |
| L03 | Content + Image | CDF description, deployment site, case study |
| L04 | Big Number | 1 000T, 30 jobs, 200 factories KPIs |
| L05 | Value Prop 3 cards | What we provide (machines+training+market+finance) |
| L06 | Process Flow | Franchise deployment in 4 steps |
| L07 | Bar Chart | Revenue projections, factories per year |
| L08 | Table | CAPEX comparison, franchise terms, country specs |
| L09 | Map | Where we operate — 3 regional clusters |
| L10 | SWOT | Strategic positioning |
| L11 | Quote | Franchisee testimonial, partner quote |
| L12 | Team | Core team, advisors |
| L13 | Timeline | 2022–2030 roadmap |
| L14 | Comparison | NGO model vs POF / centralized vs decentralized |
| L15 | Callout dark | The ask, closing statement |
