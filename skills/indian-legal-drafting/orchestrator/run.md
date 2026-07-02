---
skill: indian_legal_drafting
component: orchestrator
description: Controls execution flow of the legal drafting pipeline.
---

# Execution Flow

## Step 1: Validate Input
Ensure:
- document_type is valid
- facts are not empty
- parties are defined

## Step 2: Select Template
Map:
- legal_notice → templates/legal_notice.md
- civil_suit → templates/civil_suit.md
- criminal_complaint → templates/criminal_complaint.md
- affidavit → templates/affidavit.md

## Step 3: Run Citation Engine
- Extract relevant legal provisions
- Use references:
  - ipc.md
  - crpc.md
  - cpc.md
  - constitution.md

## Step 4: Draft Document
- Inject:
  - facts
  - parties
  - relief
  - legal sections
- Follow template structure

## Step 5: Review & Refine
- Improve clarity
- Fix structure
- Validate legal alignment

## Step 6: Output Final Document
Return:
- Clean formatted legal draft
- Proper headings
- No placeholders