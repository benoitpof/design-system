# /templates/ — Master files binaires

Master templates utilisés par les skills POF (ds-file-assembler, DS-Dataviz-generator).
**Source unique de vérité pour la génération.** Ne pas modifier sans validation Benoît + bump version DS.

## Fichiers attendus (à pousser)

| Fichier | Status | Usage | Pushé par |
|---|---|---|---|
| `master-deck.pptx` | TODO (T05) | Slide deck base, 15 layouts L01-L15, navy palette | Benoît |
| `master-report.docx` | TODO | Report A4 base, layouts R01-R10 | À produire |
| `master-web.html` | TODO | One-pager base avec sections W01-W08 | À produire |

## Convention de versioning

Chaque master file indique sa version DS dans le nom et dans les métadonnées :
- `master-deck-v3.4.0.pptx` (pour traçabilité multi-version)
- Symlink ou alias `master-deck.pptx` → version courante

## Utilisation par les skills

```python
# DS-Dataviz-generator
template = repo.fetch_master('templates/master-deck.pptx', version='v3.4.0')

# ds-file-assembler
template = repo.fetch_master('templates/master-report.docx')
```
