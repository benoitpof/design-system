# /golden/ — Golden references du Design System

**Hard limit : 5 par type, par layout.** Quand un nouveau golden entre, le moins bon sort.

Structure :
```
golden/
├── deck/         (5 PNG max — Cover L01, Section L02, KPI L04, Map L09, Callout L15)
├── chart/        (5 PNG max — un par template chart le plus utilisé)
├── map/          (5 PNG max — un par pattern)
├── report/       (5 PNG max — un par layout R01-R10 le plus utilisé)
├── web/          (5 PNG max)
├── social/       (5 PNG max)
└── photo/        (5 PNG max — meilleurs crops + overlay presets)
```

## Format

Chaque golden = 1 PNG haute résolution + 1 fichier `meta.json` :

```json
{
  "id": "deck-cover-L01-2026-04",
  "type": "deck",
  "layout": "L01",
  "ds_version": "v3.4.0",
  "validated_by": "Benoit",
  "validated_on": "2026-04-27",
  "source": "examples/deck/<asset-id>/source.pptx",
  "tags": ["cover", "factories", "fr"]
}
```

## Règles

- Aucune golden sans validation formelle Benoît
- Rotation gérée par ds-iterate (mode rules-only ne touche pas, mode manuel oui)
- À chaque release du DS, vérifier que les goldens restent valides vs nouvelles règles
