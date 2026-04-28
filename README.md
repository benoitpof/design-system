# POF Design System

**Repo:** `benoitpof/design-system` · **Version:** 4.0.0 · **Updated:** 2026-04-28
**Owner:** Benoît Blancher · benoit@plasticodyssey.org

Plastic Odyssey Factories visual identity SSOT. Compatible with Claude Design ingestion.

---

## Architecture

```
.
├── DESIGN.md                    # SSOT canonical (Claude Design 9 sections)
├── README.md                    # This file
├── CHANGELOG.md                 # Version history
├── ITERATE.md                   # PR risk levels A/B/C/D
├── VISUALIZE.md                 # Site renderer instructions
│
├── tokens/                      # Atoms (machine-readable)
│   ├── brand-tokens.json        # Colors, typography, spacing
│   ├── brand-tokens.css         # CSS variables (generated)
│   └── brand-rules-per-format.json
│
├── rules/                       # Hard rules (human + Claude readable)
│   ├── HARD-LOCKS.md            # Strict enforcement (palette, typo, overlays)
│   ├── CONTENT-RULES.md         # Editorial rules
│   ├── ASSETS.md                # Logos, corner, wave usage
│   ├── CHARTS.md                # 16 chart templates spec
│   ├── MAPS.md                  # 5 map presets + white_fade
│   ├── TABLES.md                # Tables per medium
│   ├── ICONS.md                 # Tabler + custom POF icons
│   └── PHOTOS.md                # Photos, crops, overlay system
│
├── examples/                    # Canonical references (HTML, golden specs)
│   ├── charts/                  # 18 SVG chart templates HTML
│   ├── maps/                    # Map examples
│   ├── tables/                  # Table examples
│   ├── deck/                    # Deck examples
│   ├── report/                  # Report examples
│   ├── web/                     # Web examples
│   ├── social/                  # LinkedIn / IG examples
│   ├── photo/                   # Photo overlay examples
│   ├── icons/                   # Icon usage examples
│   ├── Other/                   # Email signatures by entity
│   ├── Sheets/                  # Excel dashboard templates
│   └── GOLDEN-SPEC.md           # Goldens overview
│
├── layouts/                     # Layout specs per medium
│   ├── REPORT.md                # A4 docx/pdf
│   ├── WEB.md                   # Landing page
│   └── SOCIAL.md                # LinkedIn / Instagram
│
├── assets/                      # Binary library
│   ├── logos/                   # Per entity
│   ├── monogramme/              # Compact mark
│   ├── brand-elements/          # Corner brackets, wave
│   ├── backgrounds/             # Wave SVGs
│   ├── icons/                   # Custom POF icons
│   └── maps/                    # SVG map sources
│       ├── svg/
│       └── png-source/
│
├── templates/                   # Master binaries (locked)
│   ├── master-deck-current.pptx
│   ├── master-deck-base-layout.pptx
│   ├── MASTER_SHA.txt           # SHA preflight
│   └── README.md
│
├── memory/                      # Learnings (Rex) per medium
│   ├── chart.md, deck.md, icon.md, map.md
│   ├── photo.md, report.md, social.md, web.md
│   ├── Other/, Sheets/, tables/
│   └── README.md
│
├── scripts/                     # QA + build tools
│   ├── build-gallery.py         # Builds site/ from examples + rules
│   ├── generate-pptx-layouts.js
│   └── generate-docx-templates.js
│
└── site/                        # Static gallery (rendered docs)
```

---

## Reading order (for AI agents)

1. **`DESIGN.md`** (root) — SSOT canonical, 9 sections compiled from tokens + rules.
2. **`tokens/brand-tokens.json`** — machine-readable atoms.
3. **`tokens/brand-rules-per-format.json`** — per-medium constraints.
4. **`rules/HARD-LOCKS.md`** — strict enforcement spec.
5. **`rules/<MEDIUM>.md`** — medium-specific rules (CHARTS, MAPS, TABLES, etc.).
6. **`layouts/<MEDIUM>.md`** — layout spec (REPORT, WEB, SOCIAL).
7. **`examples/<MEDIUM>/`** — canonical reference HTML/SVG.
8. **`templates/master-*.pptx`** — binary master, validate SHA before use.
9. **`memory/<MEDIUM>.md`** — capitalised Rex / learnings.

---

## Skills consuming this DS

- **`ds-file-assembler`** — assembles decks, reports, web pages, social posts. Validates master SHA, inherits canonical layouts only, runs visual diff.
- **`ds-dataviz-generator`** — generates atomic charts, maps, tables. Reads tokens + rules + examples. Pushes to Notion Media Assets DB.
- **`ds-iterate`** — capitalises Rex into `memory/`, proposes PRs on `rules/` and `tokens/`.
- **`ds-feedback`** — atomic Rex logger to Notion DS Feedback DB.

---

## Versioning

Semantic versioning per `ITERATE.md`:
- Modif `rules/`, `layouts/`, `examples/` = bump patch (v4.0.1, v4.0.2…)
- Modif `tokens/`, `templates/` = bump minor (v4.1.0)
- Modif `DESIGN.md` racine ou breaking arbo = bump major (v5.0.0)

PR risk levels:
- **A** (auto-merge eligible): docs, examples, READMEs
- **B** (PR review): `rules/`, `layouts/`, `memory/`
- **C** (Benoît validation): `tokens/`
- **D** (Benoît formal validation): `templates/`, `DESIGN.md`, schema changes

---

## Migration v3.5 → v4.0

Done in PR #2 (this commit):
- `docs/Rules/` → `rules/`
- `docs/Rules/DESIGN.md` → `rules/HARD-LOCKS.md` (rename to free DESIGN.md slot)
- `docs/Layout/` → `layouts/`
- `docs/Memory/` → `memory/`
- `docs/Exemple/` → `examples/`
- `docs/Golden/<type>/README.md` → `examples/<type>/golden-spec.md` (merged)
- `docs/Golden/README.md` → `examples/GOLDEN-SPEC.md`
- New `DESIGN.md` at root (canonical Claude Design v1.0)
- `scripts/build-gallery.py` and `tokens/brand-rules-per-format.json` paths updated

---

## Compatibility

- **Claude Design** (Anthropic Labs, April 2026) — `DESIGN.md` racine compatible. Ingestible directement.
- **PPTX skills** — `templates/master-deck-current.pptx` SHA-locked.
- **Web** — `site/` static gallery published via GitHub Pages.

---

## Contact

Benoît Blancher · CEO Plastic Odyssey Factories · benoit@plasticodyssey.org
