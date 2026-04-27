# CONTENT-RULES.md — POF Narrative Content Rules per Layout

**Version:** 1.0 | **Updated:** 2026-04
**Purpose:** Tells Claude WHAT goes WHERE in each layout — not just the visual format.
Without this file, Claude improvises content. With it, every generated slide is production-ready.

---

## Global content rules (all layouts)

- **Language:** Match the deck's declared language (FR or EN). Never mix within a slide.
- **Titles:** Max 6 words. Always action-oriented or descriptive — never vague ("Overview", "Introduction").
- **Numbers:** Always sourced. If estimated, append "est." or "(proj.)". Never invent KPIs.
- **Coral emphasis:** Max 1–2 uses per deck. Reserve for the single most important claim.
- **No filler:** Every text block must earn its place. If you can't find content for a slot, remove the slot.
- **Tone:** Direct, evidence-based, institutional. No greenwashing language. No exclamation marks.
- **Sources:** Financial or impact data always gets a caption: "Source: POF Business Plan / Odoo / IFC report — [year]"

---

## L01 — COVER

| Slot | Content rule | Example | Forbidden |
|------|-------------|---------|-----------|
| Eyebrow tag | Document type + year. Max 4 words, all caps. | `PITCH DECK · 2025` | Generic ("Document", "Report") |
| Main title | The core value proposition or report subject. Max 4 words, 3 lines max. Impact claim preferred. | `Transforming Waste into Local Wealth.` | Questions. Taglines with no subject. |
| Subtitle | One sentence: who + what + scope. | `Plastic Odyssey Factories — 200-factory franchise network` | Marketing speak. More than one sentence. |
| Date/context | City + month + year | `Dakar, Senegal · April 2025` | Quarters ("Q2 2025") |
| Photo | Must be a real field photo: CDF exterior, team at work, aerial site. **Never** a stock photo, never a render. Query: `Usage=Cover` in Notion Media Assets. | — | Hands holding earth. Generic "industrial" photography. |

---

## L02 — SECTION DIVIDER

| Slot | Content rule | Example | Forbidden |
|------|-------------|---------|-----------|
| Section number | Sequential integer, large ghost format | `01` | Letters. Roman numerals. |
| Section label | `SECTION XX` in caps above title | `SECTION 01` | Omitting the number |
| Section title | Name of the section. Max 4 words. | `The Problem` | Generic ("Next", "More") |
| Subtitle | One crisp sentence that frames the section's argument | `80% of ocean plastic starts on land` | Summaries of what's to come. Lists. |
| Photo | Contextually matched to section topic. Impact or problem photos for Problem section. Solution/field for Solution section. | — | Same photo as cover. |

---

## L03 — CONTENT + IMAGE (50/50)

| Slot | Content rule | Example | Forbidden |
|------|-------------|---------|-----------|
| H2 title | Specific descriptive title for the content. Not the slide title repeated. | `What's inside a CDF?` | Same as header title |
| Bullet list | 4–6 bullets. Each bullet = one concrete fact, spec, or capability. Start with the strongest. Raleway body. | `Industrial extruder — 300T/year capacity` | Vague claims. More than 6 bullets. Questions. |
| Photo | Right half, full-bleed. Must show the subject of the text. If text = CDF specs → CDF photo. If text = entrepreneur → portrait. Query: `Type=Photo terrain` + topic tag. | — | Decorative/unrelated photos. AI-generated. |
| No callout box | This layout does not use stat callouts. Move KPIs to L04. | — | Adding floating stat boxes |

---

## L04 — BIG NUMBER / KPI STATS

**Layout logic:** Lead with the most impressive number. Order: Environmental impact → Social impact → Scale/ambition.

| Slot | Content rule | Example | Forbidden |
|------|-------------|---------|-----------|
| Stat 1 (top) | Environmental/impact metric | `1,000T · PLASTIC / YEAR · diverted from landfill and ocean` | Financial metrics in slot 1 |
| Stat 2 (middle) | Social/economic metric | `30 · FORMAL JOBS · created per factory at full capacity` | Percentage without absolute value |
| Stat 3 (bottom) | Scale/network metric | `1 · FACTORY · serves a city of 30,000 people` | Future projections without "proj." label |
| Number format | Integer or 1 decimal max. K/M/T/B suffixes. No full numbers (not "1,000,000", use "1M") | `1,000T`, `€2.4M`, `30` | Decimals on social metrics (not "28.4 jobs") |
| Label format | Caps, max 4 words, Poppins SemiBold, teal | `PLASTIC / YEAR` | Lowercase labels |
| Descriptor | One lowercase sentence, teal, max 8 words | `diverted from landfill and ocean` | Repeating the number in the descriptor |
| Photo | Left half, full-bleed, CDF or operations visual. Query: `Usage=Content+Image` or `Usage=KPI slide`. | — | Abstract/decorative. Charts. |

---

## L05 — VALUE PROPOSITION (3 cards)

**Card order:** Always: (1) Product/Technology → (2) Services/Support → (3) Market/Impact. Never reorder.

| Slot | Content rule | Example | Forbidden |
|------|-------------|---------|-----------|
| Card title | 2–4 words, the pillar name | `Machines & Technology` | Generic ("We provide", "Our offer") |
| Card body | 2–3 sentences max. One concrete differentiator per sentence. | `Field-tested extruder optimized for HDPE, PP and mixed plastics. Locally repairable with standard tools.` | Bullet lists inside cards. More than 3 sentences. |
| Icon | From ICONS.md Tabler list. Color: navy circle bg. Must match the card topic. | `building-factory-2` for Card 1 | Emojis as permanent icons. Off-list icons. |
| No stats | This layout is qualitative. Numbers belong in L04. | — | KPIs, percentages inside cards |

---

## L06 — PROCESS FLOW (3–5 steps)

**Rule:** Always describe the franchisee's journey, not POF's internal process.

| Slot | Content rule | Example | Forbidden |
|------|-------------|---------|-----------|
| Step number | `01`–`05`. Sequential. Teal on navy circle. | `03` | Letters. Skipping numbers. |
| Step title | Verb + noun. Max 3 words. | `Financing Setup` | Passive voice. Noun-only titles. |
| Step body | Max 2 lines. Who does what, concretely. | `Leasing structure, DFI grants, local bank coordination` | Timeline ("takes 3 weeks"). Internal POF jargon. |
| Step count | 4 steps = preferred. 5 = max. 3 = only for summary slides. | — | 6+ steps (split into two slides) |
| Subtitle | The total duration or outcome | `From signed contract to operational factory in under 6 months` | Vague ("A simple process") |

---

## L07 — BAR CHART

| Slot | Content rule | Example | Forbidden |
|------|-------------|---------|-----------|
| Chart title | Metric + time range | `Revenue Projections 2025–2030` | "Our growth" without metric |
| Subtitle | Geographic scope or qualifier | `Consolidated network — 3 regional clusters` | Repeating the title |
| Y-axis unit | Always labeled in unit header, not on axis ticks | `€M` in chart title | Raw numbers without unit |
| Series order | Series 1 = primary metric (navy), Series 2 = secondary (steel), Series 3 = emerging (teal) | Equipment Sales / Services / Impact Credits | More than 4 series |
| Max series | 3 recommended. 4 if absolutely necessary. Merge tail into "Other" beyond 4. | — | 5+ series |
| Stat callout box | Optional. 1 big takeaway number, top-right. Navy bg, teal number. | `€58M · target revenue by 2030` | Multiple callout boxes. Callout repeating Y-axis info. |
| Source caption | Bottom-left, italic, 12pt, gray | `* Based on 200 factories target — illustrative` | Omitting sources on financial projections |

---

## L08 — TABLE

| Slot | Content rule | Example | Forbidden |
|------|-------------|---------|-----------|
| Column headers | Short, max 2 words. Navy bg, white Poppins Bold. | `Capacity`, `CAPEX`, `Payback` | Verbose headers ("Average payback period") |
| Row labels | First column = row identifier. Poppins SemiBold navy. | `CDF Standard`, `CDF Pro` | Numbers as row labels |
| Cell content | Concise values. Prefer ranges over single numbers for estimates. | `€120–160K`, `18–24 months` | Explanatory sentences in cells |
| Max rows | 8 rows max per slide. Split if more. | — | 12+ rows on one slide |
| Max columns | 5 columns max. First col = label (wider). | — | 6+ columns |
| Source | Bottom of slide, caption style, always for financial data. | `Source: POF Business Plan v2026` | Tables without source on financial data |

---

## L09 — SWOT

**Quadrant order:** S top-left (navy), W top-right (light), O bottom-left (teal), T bottom-right (mid).

| Slot | Content rule | Example | Forbidden |
|------|-------------|---------|-----------|
| Items per quadrant | 3–4 max. One concrete claim per bullet. | `Proven in 10+ countries` | Vague claims ("Good team"). More than 4 bullets. |
| S — Strengths | Internal assets: proprietary tech, partnerships, track record | `In-house manufacturing hub in Dakar` | Aspirational claims (what you want to be) |
| W — Weaknesses | Honest internal limitations. Not "challenges" dressed as positives. | `High upfront CAPEX vs NGO models` | Downplaying or hedging weaknesses |
| O — Opportunities | External positive factors: regulation, market shifts, demand. Specific and current. | `EPR legislation accelerating in target markets` | Generic industry trends |
| T — Threats | External risks. Specific and honest. | `Hormuz crisis → freight cost volatility` | Internal execution risks (those go in W) |

---

## L10 — CALLOUT / KEY MESSAGE (dark)

**Rule:** One message per slide. If you have two messages, use two slides.

| Slot | Content rule | Example | Forbidden |
|------|-------------|---------|-----------|
| Label | Section context or document type. Teal, caps, charSpacing. | `OUR VISION` | Date. Generic ("Summary") |
| Main message | 1–2 lines max. The single most important thing. Bold, white, 38pt. | `Plastic Odyssey Factories bridges impact and profitability — transforming local waste into local wealth.` | 3+ sentences. Lists. Numbers without context. |
| Sub text | 1 line of supporting facts or CTA. Teal, 20pt. | `200 factories · 10,000 jobs · 200,000T diverted by 2030` | Repeating the main message. Weak qualifiers. |
| CTA button | Optional. Teal bg, navy text. Used only on closing slides or investor decks. | `Join the network →` | Multiple CTAs. CTAs on internal slides. |

---

## L11 — QUOTE / TESTIMONIAL

| Slot | Content rule | Example | Forbidden |
|------|-------------|---------|-----------|
| Quote text | Real quote from a real person. If no real quote available, do not use this layout. | `"In 6 months we had our first profitable batch. The support team never let us down."` | Paraphrased quotes. Invented quotes. Internal claims reframed as testimonials. |
| Attribution | First name, last name, title | `Mamadou Diallo, Franchise Operator — Dakar` | Job title without name. Anonymous quotes. |
| Portrait | Optional. Real photo of the quoted person. Never a stock portrait. | — | AI-generated faces. Stock portraits. |

---

## L12 — TEAM

| Slot | Content rule | Example | Forbidden |
|------|-------------|---------|-----------|
| Name | Full name, Poppins SemiBold | `Benoît Blancher` | Abbreviated names |
| Role | Job title, max 4 words | `CEO & Co-founder` | Department names without role |
| Portrait | Real photo, circular crop. Consistent framing (face centered, same background style across team). | — | LinkedIn profile photos at low resolution. AI portraits. |
| Max per slide | 8 (2 rows of 4). Use second slide for larger teams. | — | 9+ on one slide |
| Advisory board | Separate slide. Mark "(Advisor)" after role. | `Advisor, Impact Finance` | Mixing team and advisors on same slide |

---

## L13 — TIMELINE

| Slot | Content rule | Example | Forbidden |
|------|-------------|---------|-----------|
| Milestone label | Event + short description. Max 3 lines. | `2022 · First CDF deployed in Dakar` | Lengthy explanations |
| Past vs future | Past dots: teal solid. Future dots: steel, dashed axis. | — | Same visual treatment for past and future |
| Max milestones | 6. Split into two slides if more. | — | 7+ on one slide |
| Year format | 4-digit year above dot | `2030` | Quarters. "Q1 2028" |

---

## L14 — COMPARISON (2 columns)

**Rule:** Always name both columns explicitly. Never "us vs them" without naming them.

| Slot | Content rule | Example | Forbidden |
|------|-------------|---------|-----------|
| Column titles | Named, specific | `NGO/Informal Model` vs `POF Franchise` | "Before" / "After". "Option A" / "Option B". |
| Items | Use ✓ / ✗ icons or check/x Tabler icons, not bullet points. 4–6 items per column. | `✓ Locally repairable` | More than 6 items. Vague comparisons. |
| Balance | Both columns should have similar item count. Avoid 6 vs 2. | — | Stacking all negatives on one side (looks biased) |
| Optional badge | coral badge for "NOT THIS" column, teal for "THIS" column. | `⚠ Status quo` vs `✓ POF Model` | Multiple badges per column |

---

## L15 — SECTION DIVIDER (dark variant — same rules as L02)

Same rules as L02 but with dark background. Use for closing sections, "The Ask", "Investment Thesis".

---

## Anti-patterns to refuse

These patterns must be rejected regardless of what the user requests:

1. **Fake quotes** — never generate a quote and attribute it to a real person.
2. **Invented KPIs** — never fabricate numbers. If source is unknown, do not include.
3. **Greenwashing slides** — hands holding earth, ocean plastic cleanup heroes, butterfly metaphors.
4. **"We are the only..."** — claims of uniqueness require a source.
5. **Confidential data in examples** — never use real financial data from internal documents as placeholder content.
6. **White text on teal** — prohibited by WCAG. Always refuse this combination.
7. **More than 2 font families** — Poppins + Raleway only.
8. **Coral as background** — coral is emphasis only, never a fill color for text blocks.

---

## VERBATIM CONTENT MODE (v3.2.3)

When the user brief contains content marked as final, Claude must NOT paraphrase, summarize, expand, or substitute with examples from this document.

### Activation triggers (any of):
- Brief includes `<final_content>...</final_content>` XML tags
- Brief contains the phrases: "verbatim", "this is final content", "do not edit", "preserve wording", "ne pas modifier", "contenu final"
- Brief is uploaded as a file (.docx, .pdf, .md) and user says "use this content"

### Behavior in verbatim mode:
1. Place the provided text into layout slots WITHOUT changing words
2. Only allowed transformations: line breaks for fitting, slot redistribution across slides
3. NEVER pull examples from this CONTENT-RULES.md as substitute content (they are format references, not scripts)
4. If the provided content does not fit the chosen layout, propose a different layout — never trim or paraphrase

### Behavior outside verbatim mode (default):
- Free interpretation of the brief into layout slots
- Examples from this document may be used as inspiration
- Words can be reformulated for slot fit and tone

### Failure mode to flag in QA:
If a deck contains the literal example text "Transforming Waste into Local Wealth" or "200-factory franchise network" (the CONTENT-RULES.md L01 example) when the user provided different content, this is a verbatim mode failure.

### MANDATORY confirmation step before generation

Before generating any slide, deck, page, or report, Claude MUST explicitly confirm with the user the nature of the provided content using one of these two states:

- **RAW MATERIAL** — content is reference / source / draft. Claude is allowed to summarize, restructure, paraphrase, expand, or condense to fit the layout. Examples are pulled from CONTENT-RULES.md as needed.
- **FINAL CONTENT** — content is locked verbatim. Claude must preserve wording exactly, only redistribute across slots. No paraphrase, no example substitution.

Default ambiguous behaviour : ask one explicit clarification question — "Is the content I just received RAW MATERIAL (I can rephrase) or FINAL CONTENT (verbatim only)?" — and wait for the answer before generating.

If the user does not specify and the brief is short or note-form (< 200 words), default to RAW MATERIAL.
If the user provides a structured document (.docx, .pdf, full sentences with proper punctuation, > 500 words), default to FINAL CONTENT and confirm with the user.

This confirmation is non-skippable for any first-time generation in a chat session. Subsequent regenerations in the same chat inherit the previously-confirmed mode unless the user states otherwise.

---

## Memory — capitalisation Rex (v3.4.0)

<!-- ds-iterate écrit ici. Format : ### YYYY-MM-DD — <titre> -->

(vide pour l'instant)
