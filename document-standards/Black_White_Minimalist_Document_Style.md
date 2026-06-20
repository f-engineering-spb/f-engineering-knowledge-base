# Black-White Minimalist Document Style

Status: Review
Owner: F-Engineering knowledge base
Applies to: Commercial proposals, roadmaps, management presentations, project offers, client-facing analytical HTML documents

## Purpose

This is the default visual style for most new F-Engineering business documents. It is strict, monochrome, readable, and built around the logic of the proposal rather than decoration.

The style should help a client quickly understand:

- what is being proposed;
- how the process is organized;
- what decisions are required;
- where money, materials, work stages, and responsibility are connected;
- what outcome the client receives.

## Default Priority

Use this black-white minimalist style by default for new commercial and management documents unless the user explicitly asks for another style.

Earlier color or gradient styles remain allowed only when:

- the user explicitly requests them;
- an existing approved project template requires them;
- the document is a special marketing presentation where color is part of the agreed visual task.

For ordinary proposals, roadmaps, audits, specifications, and process-control documents, this monochrome style has priority.

## Visual Principles

- White document page on light gray desktop background.
- Black typography, black borders, restrained gray accents.
- No gradients, decorative color cards, large colored hero blocks, or unnecessary visual effects.
- Structure is created by spacing, borders, tables, and clear hierarchy.
- Every visual block must carry meaning: status, process, responsibility, cost, schedule, risk, or decision.

## Base Layout CSS

```css
html, body {
  max-width: 100%;
  overflow-x: hidden;
}

*, *::before, *::after {
  box-sizing: border-box;
  min-width: 0;
}

img, svg, canvas {
  max-width: 100%;
  height: auto;
}

body {
  margin: 0;
  background: #f3f3f3;
  color: #111;
  font-family: Arial, Helvetica, sans-serif;
  line-height: 1.42;
}

.page {
  max-width: 1000px;
  min-height: 1580px;
  margin: 24px auto;
  padding: 40px 42px;
  background: #fff;
  border: 1px solid #cfcfcf;
  overflow: hidden;
}
```

## Header Pattern

```css
.topline {
  display: flex;
  justify-content: space-between;
  gap: 32px;
  padding-bottom: 18px;
  border-bottom: 2px solid #111;
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: .08em;
}

.brand {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 22px;
  margin: 28px 0 8px;
}
```

The header must include the shared F-Engineering logo standard from:

`document-standards/F_Engineering_Logo_Standard.md`

## Typography

```css
h1 {
  margin: 34px 0 18px;
  font-size: 42px;
  line-height: 1.08;
  font-weight: 700;
}

h2 {
  margin: 34px 0 14px;
  padding-top: 18px;
  border-top: 1px solid #111;
  font-size: 22px;
  line-height: 1.2;
}

h3 {
  margin: 22px 0 10px;
  font-size: 16px;
}

p {
  margin: 0 0 12px;
  font-size: 15px;
  overflow-wrap: break-word;
}

.lead {
  max-width: 930px;
  font-size: 18px;
  line-height: 1.45;
}
```

## Key Components

### Key Facts

Use compact bordered cards for the main parameters: scope, term, responsibility, cost logic, decision required, or control model.

```css
.meta {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  margin: 26px 0 30px;
}

.meta-item {
  min-height: 96px;
  border: 1px solid #111;
  padding: 14px;
}

.label {
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: .08em;
  color: #555;
}

.value {
  font-size: 20px;
  font-weight: 700;
  line-height: 1.2;
}
```

### Two-Column Logic Blocks

```css
.grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 22px;
}
```

Use this for comparisons such as:

- old model / proposed model;
- work process / money process;
- client responsibility / F-Engineering responsibility;
- design / procurement;
- production / installation.

### Tables

```css
table {
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
  margin: 12px 0 18px;
  font-size: 11px;
}

th, td {
  border: 1px solid #111;
  padding: 6px 7px;
  vertical-align: top;
}

th {
  background: #eee;
  text-align: center;
  font-weight: 700;
}

.text { text-align: left; }
.num { text-align: right; }
```

### Notes

```css
.note {
  border-left: 4px solid #111;
  padding: 8px 0 8px 14px;
  color: #333;
  font-size: 14px;
}
```

Use notes for important assumptions, boundaries of responsibility, or client decisions.

### Outcome Cards

```css
.outcomes {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  counter-reset: outcome;
}

.outcome {
  min-height: 112px;
  border: 1px solid #111;
  padding: 12px;
}

.outcome::before {
  counter-increment: outcome;
  content: "0" counter(outcome);
  display: block;
  margin-bottom: 16px;
  font-size: 12px;
  font-weight: 700;
  color: #555;
}

.outcome strong {
  display: block;
  margin-bottom: 8px;
  font-size: 14px;
}

.outcome span {
  display: block;
  font-size: 12px;
  color: #333;
}
```

## Recommended Document Logic

For proposals and roadmaps, organize content in this order:

1. Header and F-Engineering logo.
2. Main offer in one clear sentence.
3. Short lead paragraph explaining why this model is different.
4. Key facts: object, scope, control model, expected result.
5. Current market model: client gives money, receives result, then manages problems.
6. Proposed model: client participates in controlled process and sees work, money, procurement, and responsibility.
7. Production or project process schedule: design, procurement, production, installation, handover, warranty response.
8. Software control layer: daily plan/fact, schedule deviation, money movement, corrective actions.
9. Responsibility matrix: what F-Engineering controls, what contractors do, what the client decides.
10. Cost, staffing, schedule, risks, and next decision.

## Process-Control Emphasis

For management proposals, the main idea should usually be the controlled production process, not a list of services.

The document must show that F-Engineering offers:

- project logic;
- procurement logic;
- production and installation planning;
- daily plan/fact control;
- financial movement control;
- visible corrective actions when the project deviates from the plan.

The client should see a route from start to finish, not only promises and separate service blocks.

## Mobile Rules

```css
@media (max-width: 720px) {
  body { background: #fff; }

  .page {
    width: 100%;
    margin: 0;
    padding: 22px 12px;
    border: 0;
  }

  .topline,
  .brand,
  .grid-2 {
    display: block;
  }

  h1 { font-size: 28px; }
  h2 { font-size: 19px; }
  .lead { font-size: 16px; }

  .meta,
  .outcomes {
    grid-template-columns: 1fr;
  }

  table {
    font-size: 10px;
  }

  th, td {
    padding: 5px;
    overflow-wrap: anywhere;
  }
}
```

## Print Rules

```css
@media print {
  body { background: #fff; }

  .page {
    margin: 0;
    border: 0;
  }

  h2,
  table,
  .meta-item,
  .outcome {
    break-inside: avoid;
  }
}
```

## Do Not Use

- Gradient background as default.
- Colored hero blocks as default.
- Decorative icons that do not explain process, responsibility, cost, or schedule.
- Mixed font families unless inherited from an approved template.
- Long unstructured text without tables, process blocks, or responsibility blocks.

## Quality Check

Before delivering a document in this style, verify:

- the logo follows the unified standard;
- the document opens on desktop without horizontal scroll;
- mobile width does not create horizontal scroll;
- tables are readable;
- the first screen explains the offer;
- the process and money logic are visible as separate but connected blocks;
- every block answers a client question or supports a decision.
