# Scripts

Node.js generation scripts. Run from the repo root.

## Requirements
```bash
npm install -g pptxgenjs docx
```

## Generate PPTX layouts showcase
```bash
node scripts/generate-pptx-layouts.js
# → pof-layouts.pptx (10 layout specimens)
```

## Generate DOCX templates
```bash
node scripts/generate-docx-templates.js
# → pof-doc-cover.docx, pof-doc-backcover.docx, pof-doc-body.docx
```

## Notes
- Images are embedded from local paths — update `IMG` paths at the top of generate-pptx-layouts.js for your environment.
- PPTX uses LAYOUT_WIDE (20"×11.25"). Colors: navy=#1C1F3B, teal=#80C7C2.
- DOCX is A4 (11906×16838 DXA).
