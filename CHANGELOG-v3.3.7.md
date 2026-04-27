# CHANGELOG v3.3.7 — Design System POF

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
