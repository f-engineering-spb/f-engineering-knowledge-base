# Estimate Scope Tools

Status: `Candidate`

Reusable tools for extracting a compact scope register from estimate and bill of
quantities spreadsheets (`.xlsx`). The tools are intended for project folders
where customer estimate exports, Grand-Smeta exports, local estimates, object
estimates, and VOR/BQ files must be converted into a readable work map before
commercial planning, cash-flow planning, or drawing verification.

Do not store customer spreadsheets in this repository. Run the tools against the
project folder and save generated outputs in that project folder.

## When To Use

Use this tool when a task includes one or more of these signals:

- Excel estimate files, local estimates, object estimates, VOR/BQ tables;
- Grand-Smeta exports converted to `.xlsx`;
- need to understand "what works and quantities we are signing for";
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

## Main Command

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

## Typical Workflow

1. Inventory all estimate files in the project folder.
2. Run the extractor on the estimate/VOR folder.
3. Review `Summary` and remove categories outside the commercial scope.
4. Compare key quantities with drawings using the applicable drawing audit
   methodology.
5. Preserve source links: file name, sheet name, row number, position text,
   unit, quantity, formula/comment.

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

## Verification

Run the smoke test:

```powershell
python tools\estimate_scope\tests\test_extract_estimate_scope.py
```

The test creates a temporary workbook, runs the extractor, and checks that
facade categories and quantities are detected.
