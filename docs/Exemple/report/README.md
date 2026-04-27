# examples/report/

Exemples produits de type **report**. Chaque exemple suit le format :

```
examples/report/<asset-id>/
  ├── source.<ext>      (HTML, DOCX, PPTX, PNG selon medium)
  ├── preview.png       (rendu PNG pour gallery)
  └── meta.json         (id, date, ds_version, layout, status, source_data_url)
```

Statut possible : `draft`, `validated`, `golden`, `deprecated`.

Les exemples `golden` (max 5 par type, rotation hard) sont en plus dans `/golden/report/`.
