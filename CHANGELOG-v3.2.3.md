# CHANGELOG v3.2.3 — Design System POF

**Date :** 2026-04-26
**Statut :** Hard locks + corner brackets migration

Source feedback : analyse des 3 livrables Claude Design (Deck POF Investor, Rapport, Site web v1/v2/v3) du 2026-04-26.

## Patches appliqués

### P1+P2 — Typography lock (STRICT)

Ajout d'un bloc `typography_lock` dans `tokens/brand-rules-per-format.json` :
- Tailles autorisées (pt) : `[9, 11, 14, 18, 22, 26, 36]`
- Tailles stat-only (pt) : `[72, 120]`
- Poids autorisés : `[300, 400, 600, 700]`
- ExtraBold (800) restreint à : titre cover (L01), titre section (L02), stat number (L04)
- Black (900) **interdit**

Justification : le deck livré utilisait 16 tailles distinctes et 5 poids — fragmentation visuelle perçue. Cap dur applique la cohérence à la racine.

`slides.font_size_mapping` re-écrit pour ne référencer que des valeurs du lock.

### P3 — Gradient overlay lock

Bloc `gradient_overlay_lock` ajouté à `brand-rules-per-format.json`.

Valeur canonique unique : `linear-gradient(135deg, rgba(28,31,59,0.85) 0%, rgba(28,31,59,0.45) 100%)`.

CSS var : `--pof-photo-overlay`.

Justification : le deck mélangeait 2 gradients (`105deg 0.92→0.05` et `135deg 0.85→0.15`). Lock élimine l'inconstance.

### P5 — Corner marks → L-brackets

Migration des marks (anciennement carrés solides 7.7 mm) vers des L-brackets vectoriels.

Nouveaux assets :
- `assets/brand-elements/corner-bracket-tl.svg` — angle haut-gauche
- `assets/brand-elements/corner-bracket-tr.svg` — angle haut-droit
- `assets/brand-elements/corner-bracket-bl.svg` — angle bas-gauche
- `assets/brand-elements/corner-bracket-br.svg` — angle bas-droit

Spec : 12 mm × 12 mm, stroke 5 px, color `#80C7C2`, stroke-linecap square. ViewBox 48×48.

Default pair = TL + BR (TR/BL optionnels pour cadrage symétrique).

Bloc `slides.corner_marks` remis à plat dans `brand-rules-per-format.json` avec coords mm pour chaque orientation.

`assets/brand-elements/corner-bracket.svg` mis à jour comme alias canonique du TL.

Justification : la spec disait carrés solides, le SVG existant était une L-shape, le template XML utilisait `grpSp` carrés. 3 sources contradictoires. Décision Benoit du 2026-04-26 : L-brackets (signature plus distinctive).

### P6 — Mode `final_content` documenté

Section ajoutée à `docs/CONTENT-RULES.md` : « VERBATIM CONTENT MODE ».

Triggers d'activation : tag `<final_content>...</final_content>`, mots-clés "verbatim / this is final / do not edit / contenu final / ne pas modifier".

Comportement : placer le texte fourni dans les slots de layout sans paraphrase. Interdit de substituer par les exemples de CONTENT-RULES.md.

Justification : Claude Design a tendance à recopier les exemples du doc CONTENT-RULES.md ("Transforming Waste into Local Wealth", "200-factory franchise network") même quand l'utilisateur fournit son propre contenu.

### Updates collatérales

- `tokens/brand-tokens.json` `_meta.version` → 3.2.3
- `components.gradient_overlay.value` aligné sur le canonical lock
- `README.md` version mise à jour
- `docs/DESIGN.md` ajoute en tête une section « Hard locks (v3.2.3) — STRICT ENFORCEMENT »

## Patches NON appliqués (hors scope)

- **P4 — Shortlist 20 pictos pré-colorés** : géré dans un autre chat Claude Design d'après Benoit. À ré-intégrer plus tard via PR séparée.

## Vérification

```bash
# Type-scale lock présent
jq '.typography_lock' tokens/brand-rules-per-format.json
# Gradient lock présent
jq '.gradient_overlay_lock.canonical_value' tokens/brand-rules-per-format.json
# 4 corner brackets
ls assets/brand-elements/corner-bracket-{tl,tr,bl,br}.svg
# Verbatim mode dans content-rules
grep -A 2 "VERBATIM CONTENT MODE" docs/CONTENT-RULES.md
```

## Action requise côté Claude Design

Ajouter au bloc « Any other notes » :

```
HARD LOCKS v3.2.3:
- Font sizes ONLY in [9, 11, 14, 18, 22, 26, 36] pt + stats [72, 120].
- Font weights ONLY in [300, 400, 600, 700]. ExtraBold (800) only on cover title, section title, stat numbers. NEVER 900.
- Photo overlay: ONLY linear-gradient(135deg, rgba(28,31,59,0.85) 0%, rgba(28,31,59,0.45) 100%).
- Corner marks: L-brackets from assets/brand-elements/corner-bracket-{tl,tr,bl,br}.svg. NEVER solid squares.
- VERBATIM mode: when brief has <final_content>...</final_content> or says "verbatim / final content / do not edit", preserve user wording exactly. Do not pull examples from CONTENT-RULES.md.
```
