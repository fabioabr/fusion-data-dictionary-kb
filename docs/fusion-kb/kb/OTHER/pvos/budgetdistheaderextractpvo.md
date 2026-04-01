---
id: DOC-OTHER-PVO-BudgetDistHeaderExtractPVO
doc_type: system-doc
title: "BudgetDistHeaderExtractPVO — PVO Cross-Module"
system: Oracle Fusion Cloud ERP
module: Cross-Module
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - other
  - data-dictionary
  - pvo
  - bicc
aliases:
  - BudgetDistHeaderExtractPVO
  - budgetdistheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BudgetDistHeaderExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Budget Dist Header Extract. Acessa as tabelas: XCC_BUDGET_DIST_HEADERS.

**Caminho:** `FscmTopModelAM.FinExtractAM.XccBiccExtractAM.BudgetDistHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 36 | 1 | 1 | 25 | 69% |

---

## 🔗 Tabelas Relacionadas

- [[xcc_budget_dist_headers|XCC_BUDGET_DIST_HEADERS]] — 36 atributos (1 PKs, 25 BICC)

---

## ⚙️ Atributos

### [[xcc_budget_dist_headers|XCC_BUDGET_DIST_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApprovalComments | APPROVAL_COMMENTS | — | ✅ |
| 2 | ApprovedBy | APPROVED_BY | — | ✅ |
| 3 | ApprovedDate | APPROVED_DATE | — | ✅ |
| 4 | AttachmentUrl | ATTACHMENT_URL | — | ✅ |
| 5 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 6 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 7 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 8 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 9 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 10 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 11 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 12 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 13 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 14 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 15 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 16 | BudgetEntryTypeCode | BUDGET_ENTRY_TYPE_CODE | — | ✅ |
| 17 | BudgetTypeCode | BUDGET_TYPE_CODE | — | ✅ |
| 18 | CreatedBy | CREATED_BY | — | ✅ |
| 19 | CreatedByJobCode | CREATED_BY_JOB_CODE | — | ✅ |
| 20 | CreationDate | CREATION_DATE | — | ✅ |
| 21 | DataPurgedFlag | DATA_PURGED_FLAG | — | ✅ |
| 22 | DataSet | DATA_SET | — | ✅ |
| 23 | HeaderId | HEADER_ID | 🔑 | ✅ |
| 24 | ImportSourceCode | IMPORT_SOURCE_CODE | — | ✅ |
| 25 | JustificationTxt | JUSTIFICATION_TXT | — | ✅ |
| 26 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 27 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 28 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 29 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 30 | OverwriteModeCode | OVERWRITE_MODE_CODE | — | ✅ |
| 31 | PeriodNameReleased | PERIOD_NAME_RELEASED | — | ✅ |
| 32 | RequestId | REQUEST_ID | — | ✅ |
| 33 | RevisionDescription | REVISION_DESCRIPTION | — | ✅ |
| 34 | SourceApplication | SOURCE_APPLICATION | — | ✅ |
| 35 | SourceBudget | SOURCE_BUDGET | — | ✅ |
| 36 | StatusCode | STATUS_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
