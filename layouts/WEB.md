# WEB.md — POF Web Layouts

**Version:** 3.4.0 | **Updated:** 2026-04-27
**Status:** Scaffolding initial. À enrichir via ds-iterate après 3 premières pages produites.
**Format :** Responsive desktop-first. Breakpoints : 1280px (desktop), 768px (tablet), 480px (mobile).
**Médium :** HTML/CSS one-pager ou multi-page statique. Pas de framework JS lourd (React, Vue) sauf demande explicite.

---

## Cadre général

- Police titres : **Poppins** (ExtraBold cover, SemiBold sections)
- Police corps : **Raleway** Regular 16 px desktop, 14 px mobile
- Container max-width : 1280 px, padding 32 px
- Hero full-bleed avec photo + overlay system (voir `rules/PHOTOS.md`)
- Top nav : sticky, height 64 px, fond white avec border-bottom neutral-mid

## Layouts canoniques (W01–W08)

| ID | Nom | Usage |
|---|---|---|
| W01 | Hero cover | Photo full-bleed + headline + CTA |
| W02 | Section feature | Texte + visuel split 50/50 |
| W03 | Grid cards | 3-4 cards alignées (services, factories) |
| W04 | KPI band | Bandeau navy avec 3-5 KPIs grand format |
| W05 | Map section | Carte interactive + légende latérale |
| W06 | Quote block | Citation centrée, fond teal soft, photo ronde |
| W07 | Logo wall | Grille de logos partenaires (max 12) |
| W08 | Footer | Logo + sitemap + contact + mentions |

> **À détailler :** ratios exacts, breakpoints, exemples golden HTML.

---

## Règles spécifiques web

- Lazy-load images en dessous du fold
- Alt text obligatoire pour SEO + accessibilité
- Contraste WCAG AA minimum (4.5:1 pour texte)
- Pas d'animation auto-play sans user opt-in
- Charge useful content first paint < 1.5s

## Memory — capitalisation Rex

<!-- ds-iterate écrit ici -->

## Exemples golden

Voir `/golden/web/` (max 5 par layout).
