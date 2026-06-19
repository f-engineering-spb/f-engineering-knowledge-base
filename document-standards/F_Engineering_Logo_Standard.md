# Unified F-Engineering Logo Standard

Status: Review
Owner: F-Engineering knowledge base
Applies to: HTML documents, commercial proposals, roadmaps, management presentations, client-facing analytical documents

## Purpose

The F-Engineering logo block is a shared brand element. It must be used consistently across new document templates unless a separate approved brand guideline explicitly overrides it.

The logo is not decorative. It marks authorship, document family, and visual continuity between proposals, roadmaps, audits, and management documents.

## Required Text

Use this exact text:

- Main line: `F - Engineering`
- Subtitle: `Facade engineering group`

The subtitle remains in English even when the document itself is prepared in Russian, Georgian, or another language.

## HTML Markup

```html
<a class="logo" href="https://github.com/f-engineering-spb" aria-label="F-Engineering">
  <span class="logo-mark">F - Engineering</span>
  <span class="logo-sub">Facade engineering group</span>
</a>
```

If the document is not published with a GitHub reference, the `href` may be removed and the wrapper may be changed from `a` to `div`, but the internal text and classes should remain the same.

## CSS Standard

```css
.logo {
  display: inline-grid;
  gap: 4px;
  color: #111;
  text-decoration: none;
  line-height: 1;
  width: max-content;
}

.logo-mark {
  font-size: 34px;
  font-weight: 650;
  letter-spacing: .125em;
}

.logo-sub {
  position: relative;
  padding-top: 5px;
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: .54em;
  word-spacing: -.12em;
  white-space: nowrap;
}

.logo-sub::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: calc(100% - 7px);
  border-top: 2px solid #111;
}
```

## Placement Rules

Place the logo in the document header area, normally after the top technical line and before the main title.

Recommended structure:

1. Top line with document metadata.
2. Brand row with the F-Engineering logo.
3. Main title and lead paragraph.
4. Key facts, summary blocks, tables, and detailed content.

## Usage Rules

- Do not replace `F - Engineering` with another spelling without explicit approval.
- Do not translate `Facade engineering group`.
- Do not use colored logo variants in the black-and-white minimalist style.
- Do not stretch, rasterize, or insert screenshot versions of the logo when HTML/CSS text rendering is possible.
- Keep the logo monochrome by default: `#111` on white.
- If a project requires a different visual identity, document the reason in the project notes.

## Mobile Behavior

The logo may keep its original proportions, but the surrounding layout must prevent horizontal scrolling. Use the shared mobile-safe CSS rule from the HTML standards:

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
```
