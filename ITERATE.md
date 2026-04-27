# ITERATE.md — Guide ds-iterate

**Version:** 3.4.0 | **Updated:** 2026-04-27
**Audience :** Benoît + skill `ds-iterate` (manuel et scheduled).

---

## Niveaux de risque

| Niveau | Type modif | Validation | Mode autorisé |
|---|---|---|---|
| **A. Faible** | Ajout entrée `memory/<type>.md` | Auto-merge | scheduled + manuel |
| **B. Moyen** | Modif règle dans `docs/rules/<file>.md` ou `docs/layouts/<file>.md` | Review en quelques minutes | scheduled + manuel (PR) |
| **C. Élevé** | Modif `tokens/*.json` ou tokens CSS | Validation formelle Benoît | manuel uniquement |
| **D. Critique** | Modif Skill, structure DB, master template | Validation formelle Benoît + tests | manuel uniquement |

## Format de PR systématique

Toute modif passe par PR (jamais de commit direct sur main).

Branche : `iterate/YYYY-MM-DD/<type>/<short-slug>`. Exemple : `iterate/2026-04-27/rules/deck-overlay-fix`.

Titre PR : `[<NIVEAU>] <Type> · <slug>`. Exemple : `[B] rules · deck overlay 5 presets`.

Body PR :
```markdown
## Source

- Lien vers entrée `memory/*.md` ou `ds-feedback` log Notion
- Livrable concerné

## Diagnostic

(2-3 lignes : ce qui a posé problème)

## Modification

(diff résumé)

## Risque

Niveau A / B / C / D + justification

## Tests

- [ ] Lecture cohérente avec règles existantes
- [ ] Pas de breaking change pour skills POF
- [ ] (si C/D) Tests Skills passent en local
```

## Règles d'or

1. **Jamais de commit direct sur main** — toujours PR.
2. **Snapshot pré-modif** — branche systématique avant édition.
3. **Niveau C/D = manuel uniquement** — scheduled task ne touche jamais ces fichiers.
4. **Pas de modif simultanée rules + skills** — un PR par type.
5. **Tag `[BENOIT-VALIDATION-REQUIRED]`** dans le titre PR pour bloquer auto-merge si niveau C/D.

## Mode scheduled task (Monday 9h Paris)

Le scheduled task de ds-iterate :
1. Lit la DB Notion `DS Feedback` (entrées non traitées de la semaine)
2. Cluster + diagnostic
3. Produit un fichier `proposals/<YYYY-MM-DD>.md` listant les modifs proposées
4. Ouvre 1 PR par groupe de modifs cohérent (toutes niveau A ou B)
5. Notifie Benoît via Slack `#ai-design-system`

**Le scheduled task ne touche jamais : `tokens/`, `templates/`, Skills, structure DB Notion.**

## Mode manuel ad-hoc

```
/ds-iterate
  --type rules|memory|tokens|skill
  --source <ds-feedback-id|memory-entry|free-text>
  --target <file-path>
  --risk A|B|C|D
```

Le manuel autorise les niveaux A à D. Pour C/D, demande validation explicite avant push.
