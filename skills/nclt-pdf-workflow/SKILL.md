---
name: nclt-pdf-workflow
description: Prepare, inspect, extract, merge, split, OCR, and validate PDFs for Indian legal and NCLT/NCLAT filing workflows using local tools.
---

# NCLT PDF Workflow

## Purpose

Use this skill when a lawyer needs local PDF handling for Indian court, tribunal, NCLT, NCLAT, IBC, company-law, or annexure workflows.

## Local-First Rules

- Work on local copies of filings and annexures.
- Preserve original filenames in an audit list before changing anything.
- Do not upload confidential documents to external converters.
- Keep extracted text separate from the source PDF.
- When OCR is used, mark the text as OCR-derived and check names, dates, amounts, and section references manually.

## Common Tasks

### Inspect a PDF

Capture:

- file path
- page count
- whether text is selectable
- visible signatures/seals, if known from user input
- encryption/password status
- page size and rotation issues

### Extract Text

Prefer local command-line tools:

```bash
pdftotext -layout input.pdf output.txt
```

If table fidelity matters, use `pdfplumber` or another table-aware local parser and review the output manually.

### OCR Scanned PDFs

Use OCR only when text extraction is blank or unreliable. After OCR, verify:

- party names
- CIN/DIN/GSTIN/PAN placeholders
- dates and limitation triggers
- rupee amounts
- section numbers
- annexure labels

### Merge Annexures

Before merging, create an annexure index with:

- annexure number
- document title
- date
- source file
- page range
- relevance

After merging, verify page order and bookmarks if the filing portal or local practice expects them.

### Split or Rotate

Record the operation in a processing note:

```text
Source: original.pdf
Operation: split pages 12-18 as Annexure P-3
Output: annexure-p-3.pdf
Checked by: [name/date]
```

## NCLT/NCLAT Filing Checks

Check local and current registry requirements for:

- petition/application format
- affidavits and verification
- authorisation/board resolution
- index and synopsis
- pagination
- annexure marking
- vakalatnama/appearance
- proof of service
- demand notice/proof of default where relevant
- prescribed forms and fees

## Output

Return a concise processing report with:

- files processed
- tools used
- warnings
- extracted text paths
- final PDF paths
- manual verification checklist
