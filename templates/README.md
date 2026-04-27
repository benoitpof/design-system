# /templates/ — Master files binaires (SSOT pour skills)

**Ces fichiers sont la source unique de vérité pour la génération de livrables. Toute skill (ds-file-assembler, DS-Dataviz-generator) DOIT dupliquer un layout depuis ces fichiers, jamais dessiner from-scratch.**

## Fichiers

| Fichier | Format | Layouts | Usage | Status |
|---|---|---|---|---|
| `master-deck-v3.4.0.pptx` | LAYOUT_WIDE 20×11.25" (508×285.75 mm) | 12 layouts | Slide deck POF (cover, sections, KPI, charts, etc.) | ✅ Actif |
| `trame-verge-deck-v2.pptx` | LAYOUT_WIDE 20×11.25" | 12 layouts | Trame de référence avec exemples remplis | 📐 Référence |

## Layouts disponibles (master-deck-v3.4.0.pptx)

| ID | Nom (PPTX) | Description | Placeholders |
|---|---|---|---|
| L00 | TITLE | Cover slide, photo full-bleed + titre + subtitle | 3 |
| L01 | SECTION_HEADER | Section divider, photo + roman numeral + titre | 2 |
| L02 | TITLE_AND_BODY | Slide standard texte | 3 |
| L03 | TITLE_AND_TWO_COLUMNS | 2 colonnes texte ou texte+visuel | 4 |
| L04 | TITLE_ONLY | Titre + zone libre | 2 |
| L05 | ONE_COLUMN_TEXT | 1 colonne texte central | 3 |
| L06 | MAIN_POINT | Citation / point clé | 2 |
| L07 | SECTION_TITLE_AND_DESCRIPTION | Titre section + description longue | 4 |
| L08 | CAPTION_ONLY | Image + caption uniquement | 2 |
| L09 | BIG_NUMBER | KPI grand format | 3 |
| L10 | BLANK | Slide vide pour layouts custom | 1 |
| L11 | Generated | Layout custom personnalisé | 0 |

**Note importante :** Les noms de layouts dans le PPTX (TITLE, SECTION_HEADER, etc.) NE correspondent PAS aux IDs L01-L15 référencés dans `docs/Layout/DECK.md`. La doc DECK.md doit être mise à jour pour s'aligner sur les 12 layouts réels du master.

## Comment l'utiliser dans une skill

```python
from pptx import Presentation
master = Presentation('templates/master-deck-v3.4.0.pptx')
# Pour chaque slide à générer :
slide_layout = master.slide_layouts[2]  # L02 TITLE_AND_BODY
new_slide = master.slides.add_slide(slide_layout)
# Remplir les placeholders nommés
for ph in new_slide.placeholders:
    if ph.placeholder_format.type == ...:
        ph.text = "..."
master.save('outputs/POF-<title>.pptx')
```

## Versioning

- `master-deck-v3.4.0.pptx` = version courante
- À chaque modif structurelle du template : bump version (v3.4.1, v3.5.0, etc.) + push nouveau fichier
- Garder les 3 dernières versions pour rollback
