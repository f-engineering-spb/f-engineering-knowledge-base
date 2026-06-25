# Estimate Scope Tools

Status: `Candidate`

Reusable tools for extracting estimate scope registers from estimate and bill of
quantities spreadsheets (`.xlsx`). The tools are intended for project folders
where customer estimate exports, Grand-Smeta exports, local estimates, object
estimates, and VOR/BQ files must be converted into a readable work map before
commercial planning, cash-flow planning, or drawing verification.

Do not store customer spreadsheets in this repository. Run the tools against the
project folder and save generated outputs in that project folder.

## When To Use

Use this toolset when a task includes one or more of these signals:

- Excel estimate files, local estimates, object estimates, VOR/BQ tables;
- Grand-Smeta exports converted to `.xlsx`;
- need to understand "what works and quantities we are signing for";
- need to prove why two source documents do not match;
- facade scope separation: ventilated facade, plinth/stone/granite, slopes,
  window flashings, galvanized sheet metal, parapets, minor metal coverings;
- preparation for cash-flow planning or facade quantity verification.

## Dependencies

Recommended:

```powershell
python -m pip install -r tools\estimate_scope\requirements.txt
```

In Codex Desktop, if the system `python` does not contain `openpyxl`, use the
bundled workspace Python exposed by `load_workspace_dependencies`.

On Windows with Cyrillic paths, prefer explicit UTF-8 and `-LiteralPath`:

```powershell
$env:PYTHONIOENCODING = 'utf-8'
[Console]::OutputEncoding = [Text.UTF8Encoding]::UTF8
```

## Two Different Extraction Modes

There are two separate workflows. Do not mix their meaning.

### 1. Compact Scope Register

Use `extract_estimate_scope.py` when the task is to find likely relevant work
rows and build a compact commercial overview.

```powershell
python tools\estimate_scope\extract_estimate_scope.py `
  --input "H:\Project\СД\xlsx" `
  --output "H:\Project\02_Drafts\Estimate_Scope\scope_register.xlsx" `
  --keywords "вентилируем,фасад,керамогранит,гранит,цокол,откос,отлив,оцинк,парапет"
```

The command produces:

- `Summary` sheet: compact grouped totals by file, sheet, body/corpus, category,
  unit, and quantity;
- `Rows` sheet: extracted source rows with traceability;
- `Files` sheet: source file inventory.

CSV output is also supported when `--output` ends with `.csv`; in that case only
the extracted rows are written.

### 2. Full Grand-Smeta Row Composition

Use `extract_grand_smeta_full_rows.py` when the task is to show the full estimate
composition: parent estimate positions, resource rows, subtotals, overhead/profit
rows, and totals.

```powershell
python tools\estimate_scope\extract_grand_smeta_full_rows.py `
  --input "H:\Project\СД\xlsx" `
  --output "H:\Project\02_Drafts\Estimate_Scope\grand_smeta_full_rows.xlsx"
```

The command produces:

- `FullRows` sheet: all non-empty rows with source file, sheet, row number,
  parent position, detected row type, quantity/price fields, and source row text;
- `Summary` sheet: row counts, parent position counts, and detected estimate
  totals by file/sheet;
- `Method` sheet: short rules for interpreting parent and resource rows.

This mode is required when a customer estimate contains many rows that are not
independent works: electrodes, mortar, machinery, transport, labor, overhead,
profit, and other resources. Those rows explain the price composition of the
parent estimate position. They must not be compared to VOR or drawings as
separate contractual works unless the source document explicitly defines them as
separate work items.

## Interpretation Rule: Parent Positions vs Resources

For comparisons between VOR, local estimates, Grand-Smeta XLSX exports and
working documentation:

- compare scope and quantities at the parent estimate position level first;
- keep resource rows visible as evidence of price composition;
- do not treat resource rows as separate facade works only because they contain a
  material or machine name;
- when a compact extract is used for overview, verify disputed items with the
  full row composition before making commercial conclusions;
- in comparison tables, mark whether each item is present in VOR, Grand-Smeta,
  customer Excel estimate, and RD/PDF, instead of mechanically subtracting
  unrelated columns.

## Typical Workflow

1. Inventory all estimate files in the project folder.
2. Run the compact extractor on the estimate/VOR folder to see likely facade
   scope.
3. Run the full Grand-Smeta extractor on disputed estimate exports.
4. Review parent positions and remove categories outside the commercial scope.
5. Compare key quantities with drawings using the applicable drawing audit
   methodology.
6. Preserve source links: file name, sheet name, row number, position text,
   unit, quantity, formula/comment.
7. For client-facing tables, add presence/comment markers such as `есть в ВОР`,
   `есть в смете`, `нет в РД`, `есть только в Excel-смете`.

## Scope Classification

The default classifier is intentionally conservative. It marks likely categories
but does not decide commercial inclusion by itself.

Default categories:

- `NVF / porcelain stoneware`
- `Plinth / granite / stone`
- `Opening slopes / framing`
- `Window flashings`
- `Galvanized sheet metal / minor coverings`
- `Parapets / copings`
- `Demolition`
- `Other facade-related`

If a row contains both a generic work name and a specific material resource,
prefer the specific material for commercial interpretation. Example: a row named
"ventilated facade with porcelain stoneware" can still represent a granite
plinth if the material resource is "granite slab".

## UTF-8 And Cyrillic Notes

- Keep scripts in UTF-8.
- For CSV opened manually in Excel, write `utf-8-sig`.
- Use `Path` and PowerShell `-LiteralPath` for Cyrillic paths.
- If a local Google Drive mirror or PowerShell output shows mojibake, do not
  conclude that the repository file is broken. Re-read through the GitHub
  connector, Google Drive connector, or explicit UTF-8 file read.
- Do not copy mojibake into Markdown, CSV, HTML, or Python sources.

## Verification

Run the smoke test:

```powershell
python tools\estimate_scope\tests\test_extract_estimate_scope.py
```

The test creates a temporary workbook, runs the compact extractor, and checks
that facade categories and quantities are detected.

For `extract_grand_smeta_full_rows.py`, run it on a small exported estimate and
confirm that:

- `FullRows` includes parent positions and resource rows;
- `parent_position` is filled for resource/subtotal rows below a parent item;
- `Summary` contains the expected number of non-empty rows;
- Russian text is readable in Excel and does not contain mojibake.
