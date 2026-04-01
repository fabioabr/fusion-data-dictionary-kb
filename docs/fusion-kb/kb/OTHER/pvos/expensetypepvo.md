---
id: DOC-OTHER-PVO-ExpenseTypePVO
doc_type: system-doc
title: "ExpenseTypePVO — PVO Cross-Module"
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
  - ExpenseTypePVO
  - expensetypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenseTypePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Expense Type. Acessa as tabelas: EXM_EXPENSE_TEMPLATES, EXM_EXPENSE_TYPES.

**Caminho:** `FscmTopModelAM.FinExmSetupSharedAM.ExpenseTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 68 | 2 | 1 | 8 | 12% |

---

## 🔗 Tabelas Relacionadas

- [[exm_expense_templates|EXM_EXPENSE_TEMPLATES]] — 14 atributos (1 BICC)
- [[exm_expense_types|EXM_EXPENSE_TYPES]] — 54 atributos (1 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[exm_expense_templates|EXM_EXPENSE_TEMPLATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy1 | CREATED_BY | — | — |
| 2 | CreationDate1 | CREATION_DATE | — | — |
| 3 | Description1 | DESCRIPTION | — | — |
| 4 | DfltCcExpTypeId | DFLT_CC_EXP_TYPE_ID | — | — |
| 5 | EnableCcMappingFlag | ENABLE_CC_MAPPING_FLAG | — | — |
| 6 | ExpenseTemplateId1 | EXPENSE_TEMPLATE_ID | — | — |
| 7 | InactiveDate | INACTIVE_DATE | — | — |
| 8 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 10 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 11 | Name1 | NAME | — | — |
| 12 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 13 | OrgId1 | ORG_ID | — | — |
| 14 | StartDate1 | START_DATE | — | — |

### [[exm_expense_types|EXM_EXPENSE_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryCode | CATEGORY_CODE | — | ✅ |
| 2 | CodeCombinationId | CODE_COMBINATION_ID | — | — |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | DefaultProjExpendType | DEFAULT_PROJ_EXPEND_TYPE | — | — |
| 6 | Description | DESCRIPTION | — | — |
| 7 | DispRcptViolationFlag | DISP_RCPT_VIOLATION_FLAG | — | — |
| 8 | EnableProjectsFlag | ENABLE_PROJECTS_FLAG | — | — |
| 9 | EndDate | END_DATE | — | — |
| 10 | ExpenseTemplateId | EXPENSE_TEMPLATE_ID | — | — |
| 11 | ExpenseTypeId | EXPENSE_TYPE_ID | 🔑 | ✅ |
| 12 | ItemizationBehaviourCode | ITEMIZATION_BEHAVIOUR_CODE | — | — |
| 13 | ItemizationOnlyFlag | ITEMIZATION_ONLY_FLAG | — | — |
| 14 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | Name | NAME | — | ✅ |
| 18 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | OrgId | ORG_ID | — | — |
| 20 | RcptRequiredProjFlag | RCPT_REQUIRED_PROJ_FLAG | — | — |
| 21 | ReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 22 | ReceiptThreshold | RECEIPT_THRESHOLD | — | — |
| 23 | Segment1 | SEGMENT1 | — | — |
| 24 | Segment10 | SEGMENT10 | — | — |
| 25 | Segment11 | SEGMENT11 | — | — |
| 26 | Segment12 | SEGMENT12 | — | — |
| 27 | Segment13 | SEGMENT13 | — | — |
| 28 | Segment14 | SEGMENT14 | — | — |
| 29 | Segment15 | SEGMENT15 | — | — |
| 30 | Segment16 | SEGMENT16 | — | — |
| 31 | Segment17 | SEGMENT17 | — | — |
| 32 | Segment18 | SEGMENT18 | — | — |
| 33 | Segment19 | SEGMENT19 | — | — |
| 34 | Segment2 | SEGMENT2 | — | — |
| 35 | Segment20 | SEGMENT20 | — | — |
| 36 | Segment21 | SEGMENT21 | — | — |
| 37 | Segment22 | SEGMENT22 | — | — |
| 38 | Segment23 | SEGMENT23 | — | — |
| 39 | Segment24 | SEGMENT24 | — | — |
| 40 | Segment25 | SEGMENT25 | — | — |
| 41 | Segment26 | SEGMENT26 | — | — |
| 42 | Segment27 | SEGMENT27 | — | — |
| 43 | Segment28 | SEGMENT28 | — | — |
| 44 | Segment29 | SEGMENT29 | — | — |
| 45 | Segment3 | SEGMENT3 | — | — |
| 46 | Segment30 | SEGMENT30 | — | — |
| 47 | Segment4 | SEGMENT4 | — | — |
| 48 | Segment5 | SEGMENT5 | — | — |
| 49 | Segment6 | SEGMENT6 | — | — |
| 50 | Segment7 | SEGMENT7 | — | — |
| 51 | Segment8 | SEGMENT8 | — | — |
| 52 | Segment9 | SEGMENT9 | — | — |
| 53 | StartDate | START_DATE | — | — |
| 54 | TaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
