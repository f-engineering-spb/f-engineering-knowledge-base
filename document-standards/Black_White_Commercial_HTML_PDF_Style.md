# Black-and-White Commercial HTML/PDF Style

Use this standard for client-facing commercial proposals, preliminary facade scope reports, tender support notes, and pre-KM facade solution packages when the deliverable must be strict, readable, and suitable for sending as both HTML and PDF.

Reference decision: the black-and-white commercial proposal for `L1 Kupchino / OD-150 / facades` was accepted as the approved visual direction on 2026-06-19.

## Deliverables

- Prepare one self-contained HTML file and one PDF exported from the same HTML source.
- The HTML must open correctly on desktop and phone screens without horizontal scrolling.
- The PDF must preserve the same visual identity, spacing, logo, table structure, and black-and-white hierarchy.
- Do not duplicate price, deadline, or other commercial terms at the bottom when they are already shown in the top summary block.

## Visual Rules

- Use a strict black-and-white palette: black text, white page, light gray page background, gray borders, and no color accents.
- Do not use gradients, decorative blobs, colored highlights, colored table fills, or marketing-style illustration.
- Keep the page calm and technical: dense enough for engineering content, but with generous section spacing.
- Use `Arial`, `Helvetica`, or another neutral sans-serif as the primary font.
- Use a centered page container with `width: 100%` and `max-width: 1000px`.
- Use black borders for the main page frame and gray borders for tables and internal blocks.

## Logo

Use a text logo at the top unless an approved vector logo is explicitly provided.

The approved text construction is:

- Main line: `F-Engineering`
- Secondary line: `FACADE ENGINEERING GROUP`
- Main line should be wide, light enough, and not visually heavy.
- Secondary line should read as one continuous inscription: increase letter spacing, reduce word spacing, and avoid large gaps between words.

Recommended CSS:

```css
.brand {
  display: inline-block;
  color: #111;
  text-decoration: none;
}

.logo-mark {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 34px;
  font-weight: 650;
  line-height: .9;
  letter-spacing: .025em;
}

.logo-sub {
  margin-top: 6px;
  border-top: 2px solid #111;
  padding-top: 5px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .31em;
  word-spacing: -.08em;
  white-space: nowrap;
}
```

## Top Summary

Place the most important commercial information near the top:

- project name;
- object or building group;
- document type;
- scope summary;
- price;
- planned completion date;
- F-Engineering / FNG link when appropriate.

The top area should make it clear that the team studied the project documentation and is proposing a concrete technical package, not a generic service.

## Scope Wording

Use a concise scope limiter instead of long exclusion lists:

> Commercial proposal applies only to the facade cladding and construction types listed below. Other facade elements are considered separately if required.

Russian wording approved for client documents:

> Коммерческое предложение распространяется только на указанные ниже виды фасадных облицовок и конструкций. Иные элементы фасада рассматриваются отдельно при необходимости.

## Construction Specification

The specification of considered constructions must include:

- construction type;
- project description or marking;
- preliminary volume;
- volume unit;
- drawing or source reference.

Keep the description specific enough to show that project documentation was reviewed: include system type, material, color, elevation zone, stone type, marking, or drawing reference when these are available.

Do not show piece counts for warm or cold stained-glass structures unless the meaning of `quantity` in the source specification is confirmed and explained. By default, use square meters for these constructions.

## Volumes

- Mark all quantities as preliminary when they are used for a commercial proposal before full takeoff.
- State whether each volume comes from an existing specification, a drawing measurement, or an approximate facade envelope check.
- When measured manually, cite the drawing sheets or views used for the measurement.
- Include gross facade area and a control sum by facade construction types when useful. The purpose is to show that the proposal is dimensionally grounded, not to replace final quantity surveying.

## Tables

Use fixed-layout tables and force wrapping so wide engineering content stays inside the page.

Recommended CSS:

```css
table {
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
}

th,
td {
  border: 1px solid #cfcfcf;
  padding: 7px 8px;
  vertical-align: top;
  overflow-wrap: anywhere;
  word-break: normal;
}

th {
  text-align: center;
  font-size: 10px;
  text-transform: uppercase;
}

td.num,
td.unit,
td.source {
  text-align: center;
  vertical-align: middle;
}
```

For wide technical tables, use smaller text but keep it readable in PDF. Numeric values and units should be centered in their cells.

## Client-Facing Language

Do not mention internal tool names, AI, Codex, parsing attempts, temporary file names, or repository operations in the client document.

Do use direct engineering language:

- what structures are included;
- what sources were reviewed;
- what technical decisions will be prepared;
- how the result can be used by the client, tender participants, designers, and future KM contractors.

The proposed result may be described as a technical basis for future KM development: typical nodes, calculation schemes, system choices, and drawings for representative facade areas that can be scaled by the selected contractor to similar facade areas.

## Responsive HTML

Required baseline:

```css
html,
body {
  max-width: 100%;
  overflow-x: hidden;
}

.page {
  width: 100%;
  max-width: 1000px;
  margin: 0 auto;
}

@media (max-width: 720px) {
  body {
    padding: 0;
  }

  .page {
    border-left: 0;
    border-right: 0;
  }

  table {
    font-size: 10px;
  }
}
```

When browser automation is available, verify that:

```js
document.documentElement.scrollWidth <= document.documentElement.clientWidth
```

If browser verification is not available, apply the mobile rules from `HTML_Mobile_Standard.md` and manually inspect the exported PDF.

## PDF Export

- Export the PDF from the final HTML, not from a separately recreated layout.
- Disable browser-generated PDF headers and footers when possible.
- Verify that all tables fit within the printable page width.
- Verify that the logo and top commercial summary remain on the first page.
- Verify that no section title is left alone at the bottom of a page when the following table starts on the next page.
