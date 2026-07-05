# AI Palette Style Guide

Status: Candidate
Scope: internal HTML instructions, AI workflow guides, project playbooks, checklists, index pages.

## Purpose

This guide defines reusable light palettes for internal AI-related instructions and working HTML documents.

The goal is not to make presentations. The goal is to make calm working documents that are easy to read, easy to scroll, and easy to reuse.

## General rules

1. No gradients.
2. No shadows.
3. No 3D buttons.
4. Use continuous 1px borders.
5. Use rounded rectangles consistently.
6. Use one main UI font.
7. Use bold only for headings and key terms.
8. Avoid strong color. Use only a slight color hint.
9. Text should not sit on the darkest layer unless contrast is excellent.
10. A working instruction should look like a calm workspace, not like a sales presentation.

Recommended UI font:

```css
font-family: "Segoe UI", -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif;
```

Recommended monospace font:

```css
font-family: "Segoe UI Mono", Consolas, "Courier New", monospace;
```

## Three-layer model

| Layer | Meaning | Typical use |
|---|---|---|
| Layer 1 | Main page or block background | outer section, main reading field |
| Layer 2 | Module background | grouped content, examples, tables |
| Layer 3 | Accent surface | buttons, small cards, table headers, swatches |

Layers should be close enough to feel calm, but different enough to show document structure.

## Palette registry

### P01 GitHub Light

Use for technical documentation, GitHub rules, registries, file indexes, repo-related instructions.

| Token | HEX |
|---|---|
| Layer 1 | `#ffffff` |
| Layer 2 | `#f6f8fa` |
| Layer 3 | `#eef1f4` |
| Border | `#d1d9e0` |
| Strong border | `#b8c0c8` |
| Text | `#1f2328` |
| Muted text | `#59636e` |

### P02 Apple Gray

Use as the default universal working style. Almost no color. Best for internal instructions and process documents.

| Token | HEX |
|---|---|
| Layer 1 | `#fbfbfa` |
| Layer 2 | `#f3f4f4` |
| Layer 3 | `#e9ebeb` |
| Border | `#d5d8d8` |
| Strong border | `#c4c8c8` |
| Text | `#232625` |
| Muted text | `#5e6664` |

### P03 Warm Paper

Use for long reading, methodology, soft internal guidance, onboarding notes, explanatory memos.

| Token | HEX |
|---|---|
| Layer 1 | `#fcfbf7` |
| Layer 2 | `#f4f1ea` |
| Layer 3 | `#eae5da` |
| Border | `#d9d2c4` |
| Strong border | `#c9bfad` |
| Text | `#2a2722` |
| Muted text | `#696153` |

### P04 Sage

Use for workflow, process, order, checklists, operational rules.

| Token | HEX |
|---|---|
| Layer 1 | `#fbfcf9` |
| Layer 2 | `#f1f4ee` |
| Layer 3 | `#e5ebe2` |
| Border | `#d2dacd` |
| Strong border | `#c0cab9` |
| Text | `#232822` |
| Muted text | `#5f685b` |

### P05 Sand

Use for system notes, technical recovery instructions, emergency workflows, installation guides.

| Token | HEX |
|---|---|
| Layer 1 | `#fcfbf8` |
| Layer 2 | `#f4f2ed` |
| Layer 3 | `#e9e4da` |
| Border | `#d8d0c2` |
| Strong border | `#c6baa6` |
| Text | `#2a2824` |
| Muted text | `#6a6255` |

### P06 Mist Lavender

Use for comparisons, alternative opinions, strategy thinking, model comparisons, decision reviews.

| Token | HEX |
|---|---|
| Layer 1 | `#fcfbfd` |
| Layer 2 | `#f4f2f7` |
| Layer 3 | `#e9e6ef` |
| Border | `#d7d2df` |
| Strong border | `#c7bfd1` |
| Text | `#26242b` |
| Muted text | `#625d6b` |

### P07 Ice Blue

Use for AI tooling, matrices, technology maps, desktop workflow guides, tool selection instructions.

| Token | HEX |
|---|---|
| Layer 1 | `#fbfcfd` |
| Layer 2 | `#f1f5f7` |
| Layer 3 | `#e5edf1` |
| Border | `#d0dbe1` |
| Strong border | `#bdccd4` |
| Text | `#22282c` |
| Muted text | `#5b6770` |

## How to request a palette

Use these phrases:

```text
Use palette P02 Apple Gray.
Use palette P03 Warm Paper.
Use palette P05 Sand for a technical recovery instruction.
Use palette P07 Ice Blue for an AI tools matrix.
Use palette P04 Sage for a process checklist.
```

## Inverted layer rule

Inverted means:

```text
Layer 1 and Layer 3 are swapped.
Layer 2 remains unchanged.
```

Use this phrase:

```text
Use inverted P03 Warm Paper: swap Layer 1 and Layer 3, keep Layer 2 unchanged.
```

Use inversion only for experiments or when the normal layout feels too flat.

## Recommended defaults

| Situation | Palette |
|---|---|
| Universal internal instruction | P02 Apple Gray |
| AI tools / technology matrix | P07 Ice Blue |
| Long methodology / onboarding | P03 Warm Paper |
| Process / checklist / order | P04 Sage |
| Emergency technical instruction | P05 Sand |
| Comparisons / second opinions | P06 Mist Lavender |
| GitHub / repository documentation | P01 GitHub Light |

## Example CSS variables

```css
:root {
  --layer-1: #fbfbfa;
  --layer-2: #f3f4f4;
  --layer-3: #e9ebeb;
  --border: #d5d8d8;
  --border-strong: #c4c8c8;
  --text: #232625;
  --text-muted: #5e6664;
}
```

## Status note

This guide is a Candidate standard. Promote to Approved after practical use in several internal documents.
