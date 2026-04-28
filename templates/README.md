# /templates/ — Master files (SSOT for skills)

**These files are the unique source of truth for deliverable generation. Every skill (ds-file-assembler, DS-Dataviz-generator) MUST duplicate a layout from these files, never draw from scratch.**

## Files

| File | Format | Layouts | Usage | Status |
|---|---|---|---|---|
| `master-deck-current.pptx` | LAYOUT_WIDE 20×11.25" (508×285.75 mm) | 12 layouts | Deck SSOT — duplicate this, never modify in place | ✅ Active |
| `master-deck-base-layout.pptx` | 16:9 (254×142.9 mm) | 11 layouts | Compact slides (web embed, doc inserts) | 📐 Reference |
| `MASTER_SHA.txt` | text | — | SHA-256 of `master-deck-current.pptx` for preflight checks | 🔒 Lock |

## Layouts available (master-deck-current.pptx)

12 layouts, indices 0-11. Names below are exact PPTX layout names — these are the SSOT identifiers used by skills.

| Index | PPTX layout name | Description | Placeholders |
|---|---|---|---|
| 0 | `TITLE` | Cover slide, photo full-bleed + title + subtitle | 3 |
| 1 | `SECTION_HEADER` | Section divider, photo + roman numeral + title | 2 |
| 2 | `TITLE_AND_BODY` | Standard text slide | 3 |
| 3 | `TITLE_AND_TWO_COLUMNS` | 2 columns text or text+visual | 4 |
| 4 | `TITLE_ONLY` | Title + free zone | 2 |
| 5 | `ONE_COLUMN_TEXT` | Centered single column text | 3 |
| 6 | `MAIN_POINT` | Quote / key point | 2 |
| 7 | `SECTION_TITLE_AND_DESCRIPTION` | Section title + long description | 4 |
| 8 | `CAPTION_ONLY` | Image + caption only | 2 |
| 9 | `BIG_NUMBER` | Large KPI | 3 |
| 10 | `BLANK` | Empty slide for custom layouts | 1 |
| 11 | `Generated (g3d916d2d710_33_0)` | Custom personalized layout | 0 |

## How to use in a skill

```python
from pptx import Presentation
import hashlib

# 1. Load master
master = Presentation('templates/master-deck-current.pptx')

# 2. SHA preflight
with open('templates/master-deck-current.pptx', 'rb') as f:
    sha = hashlib.sha256(f.read()).hexdigest()
expected = open('templates/MASTER_SHA.txt').read().strip()
assert sha == expected, f"Master SHA mismatch — abort"

# 3. Whitelist
allowed = [l.name for l in master.slide_layouts]

# 4. Add slide via canonical layout (NEVER draw from scratch)
slide_layout = master.slide_layouts[2]  # TITLE_AND_BODY
new_slide = master.slides.add_slide(slide_layout)
assert new_slide.slide_layout.name in allowed

# 5. Fill named placeholders only
for ph in new_slide.placeholders:
    ph.text = "..."

master.save('outputs/POF-<title>.pptx')
```

## Versioning

- `master-deck-current.pptx` = always the production version. Bump SHA on every change.
- Past versions kept in `.archive/templates/master-deck-vYYYYMMDD.pptx` for rollback.
- Any structural change to the master = PR with explicit changelog entry + SHA bump in `MASTER_SHA.txt`.

## Forbidden

1. Drawing layouts via `add_shape` outside placeholder grid.
2. Loading a master that doesn't match `MASTER_SHA.txt`.
3. Keeping multiple "current" master files (only one).
4. Direct commit on `main` — PR only (`ITERATE.md`).
