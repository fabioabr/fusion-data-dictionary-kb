---
id: DOC-OTHER-PVO-BudgetDistLineExtractPVO
doc_type: system-doc
title: "BudgetDistLineExtractPVO — PVO Cross-Module"
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
  - BudgetDistLineExtractPVO
  - budgetdistlineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BudgetDistLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Budget Dist Line Extract. Acessa as tabelas: XCC_BUDGET_DIST_LINES.

**Caminho:** `FscmTopModelAM.FinExtractAM.XccBiccExtractAM.BudgetDistLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 79 | 1 | 2 | 53 | 67% |

---

## 🔗 Tabelas Relacionadas

- [[xcc_budget_dist_lines|XCC_BUDGET_DIST_LINES]] — 79 atributos (2 PKs, 53 BICC)

---

## ⚙️ Atributos

### [[xcc_budget_dist_lines|XCC_BUDGET_DIST_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccountCcid | ACCOUNT_CCID | — | ✅ |
| 2 | AnnotationTxt | ANNOTATION_TXT | — | ✅ |
| 3 | AttachmentUrl | ATTACHMENT_URL | — | ✅ |
| 4 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 5 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 6 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 7 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 8 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 9 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 10 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 11 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 12 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 13 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 14 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 15 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 16 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 17 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 18 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 19 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 20 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 21 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 22 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 23 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 24 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 25 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 26 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 27 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 28 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 29 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 30 | CreatedBy | CREATED_BY | — | ✅ |
| 31 | CreationDate | CREATION_DATE | — | ✅ |
| 32 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 33 | DataPurgedFlag | DATA_PURGED_FLAG | — | ✅ |
| 34 | HeaderId | HEADER_ID | 🔑 | ✅ |
| 35 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 36 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 37 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 38 | LineNumber | LINE_NUMBER | 🔑 | ✅ |
| 39 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 40 | OverwrittenFlag | OVERWRITTEN_FLAG | — | ✅ |
| 41 | PjcContractId | PJC_CONTRACT_ID | — | ✅ |
| 42 | PjcFundingSourceId | PJC_FUNDING_SOURCE_ID | — | ✅ |
| 43 | PjcProjectId | PJC_PROJECT_ID | — | ✅ |
| 44 | PjcResourceId | PJC_RESOURCE_ID | — | ✅ |
| 45 | PjcTaskId | PJC_TASK_ID | — | ✅ |
| 46 | PjcTopResourceId | PJC_TOP_RESOURCE_ID | — | ✅ |
| 47 | PjcTopTaskId | PJC_TOP_TASK_ID | — | ✅ |
| 48 | Segment1 | SEGMENT1 | — | ✅ |
| 49 | Segment10 | SEGMENT10 | — | ✅ |
| 50 | Segment11 | SEGMENT11 | — | ✅ |
| 51 | Segment12 | SEGMENT12 | — | ✅ |
| 52 | Segment13 | SEGMENT13 | — | ✅ |
| 53 | Segment14 | SEGMENT14 | — | ✅ |
| 54 | Segment15 | SEGMENT15 | — | ✅ |
| 55 | Segment16 | SEGMENT16 | — | ✅ |
| 56 | Segment17 | SEGMENT17 | — | ✅ |
| 57 | Segment18 | SEGMENT18 | — | ✅ |
| 58 | Segment19 | SEGMENT19 | — | ✅ |
| 59 | Segment2 | SEGMENT2 | — | ✅ |
| 60 | Segment20 | SEGMENT20 | — | ✅ |
| 61 | Segment21 | SEGMENT21 | — | ✅ |
| 62 | Segment22 | SEGMENT22 | — | ✅ |
| 63 | Segment23 | SEGMENT23 | — | ✅ |
| 64 | Segment24 | SEGMENT24 | — | ✅ |
| 65 | Segment25 | SEGMENT25 | — | ✅ |
| 66 | Segment26 | SEGMENT26 | — | ✅ |
| 67 | Segment27 | SEGMENT27 | — | ✅ |
| 68 | Segment28 | SEGMENT28 | — | ✅ |
| 69 | Segment29 | SEGMENT29 | — | ✅ |
| 70 | Segment3 | SEGMENT3 | — | ✅ |
| 71 | Segment30 | SEGMENT30 | — | ✅ |
| 72 | Segment4 | SEGMENT4 | — | ✅ |
| 73 | Segment5 | SEGMENT5 | — | ✅ |
| 74 | Segment6 | SEGMENT6 | — | ✅ |
| 75 | Segment7 | SEGMENT7 | — | ✅ |
| 76 | Segment8 | SEGMENT8 | — | ✅ |
| 77 | Segment9 | SEGMENT9 | — | ✅ |
| 78 | TransactionSubtypeCode | TRANSACTION_SUBTYPE_CODE | — | ✅ |
| 79 | UomCode | UOM_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
