---
id: DOC-OTHER-PVO-ExpenseTypeExtractPVO
doc_type: system-doc
title: "ExpenseTypeExtractPVO — PVO Cross-Module"
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
  - ExpenseTypeExtractPVO
  - expensetypeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenseTypeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Expense Type Extract. Acessa as tabelas: EXM_EXPENSE_TYPES.

**Caminho:** `FscmTopModelAM.FinExtractAM.ExmBiccExtractAM.ExpenseTypeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 57 | 1 | 1 | 19 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[exm_expense_types|EXM_EXPENSE_TYPES]] — 57 atributos (1 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[exm_expense_types|EXM_EXPENSE_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenseTypeCategoryCode | CATEGORY_CODE | — | ✅ |
| 2 | ExpenseTypeCcReceiptRequiredFlag | CC_RECEIPT_REQUIRED_FLAG | — | ✅ |
| 3 | ExpenseTypeCcReceiptThreshold | CC_RECEIPT_THRESHOLD | — | ✅ |
| 4 | ExpenseTypeCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 5 | ExpenseTypeCreatedBy | CREATED_BY | — | — |
| 6 | ExpenseTypeCreationDate | CREATION_DATE | — | ✅ |
| 7 | ExpenseTypeDefaultProjExpendType | DEFAULT_PROJ_EXPEND_TYPE | — | — |
| 8 | ExpenseTypeDescription | DESCRIPTION | — | ✅ |
| 9 | ExpenseTypeDispRcptViolationFlag | DISP_RCPT_VIOLATION_FLAG | — | ✅ |
| 10 | ExpenseTypeEnableProjectsFlag | ENABLE_PROJECTS_FLAG | — | — |
| 11 | ExpenseTypeEndDate | END_DATE | — | ✅ |
| 12 | ExpenseTypeId | EXPENSE_TYPE_ID | 🔑 | ✅ |
| 13 | ExpenseTypeItemizationBehaviourCode | ITEMIZATION_BEHAVIOUR_CODE | — | ✅ |
| 14 | ExpenseTypeItemizationOnlyFlag | ITEMIZATION_ONLY_FLAG | — | ✅ |
| 15 | ExpenseTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | ExpenseTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | ExpenseTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | ExpenseTypeName | NAME | — | ✅ |
| 19 | ExpenseTypeNegativeRcptReqCode | NEGATIVE_RCPT_REQ_CODE | — | ✅ |
| 20 | ExpenseTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | ExpenseTypeOrgId | ORG_ID | — | ✅ |
| 22 | ExpenseTypeRcptRequiredProjFlag | RCPT_REQUIRED_PROJ_FLAG | — | ✅ |
| 23 | ExpenseTypeReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | ✅ |
| 24 | ExpenseTypeReceiptThreshold | RECEIPT_THRESHOLD | — | ✅ |
| 25 | ExpenseTypeSegment1 | SEGMENT1 | — | — |
| 26 | ExpenseTypeSegment10 | SEGMENT10 | — | — |
| 27 | ExpenseTypeSegment11 | SEGMENT11 | — | — |
| 28 | ExpenseTypeSegment12 | SEGMENT12 | — | — |
| 29 | ExpenseTypeSegment13 | SEGMENT13 | — | — |
| 30 | ExpenseTypeSegment14 | SEGMENT14 | — | — |
| 31 | ExpenseTypeSegment15 | SEGMENT15 | — | — |
| 32 | ExpenseTypeSegment16 | SEGMENT16 | — | — |
| 33 | ExpenseTypeSegment17 | SEGMENT17 | — | — |
| 34 | ExpenseTypeSegment18 | SEGMENT18 | — | — |
| 35 | ExpenseTypeSegment19 | SEGMENT19 | — | — |
| 36 | ExpenseTypeSegment2 | SEGMENT2 | — | — |
| 37 | ExpenseTypeSegment20 | SEGMENT20 | — | — |
| 38 | ExpenseTypeSegment21 | SEGMENT21 | — | — |
| 39 | ExpenseTypeSegment22 | SEGMENT22 | — | — |
| 40 | ExpenseTypeSegment23 | SEGMENT23 | — | — |
| 41 | ExpenseTypeSegment24 | SEGMENT24 | — | — |
| 42 | ExpenseTypeSegment25 | SEGMENT25 | — | — |
| 43 | ExpenseTypeSegment26 | SEGMENT26 | — | — |
| 44 | ExpenseTypeSegment27 | SEGMENT27 | — | — |
| 45 | ExpenseTypeSegment28 | SEGMENT28 | — | — |
| 46 | ExpenseTypeSegment29 | SEGMENT29 | — | — |
| 47 | ExpenseTypeSegment3 | SEGMENT3 | — | — |
| 48 | ExpenseTypeSegment30 | SEGMENT30 | — | — |
| 49 | ExpenseTypeSegment4 | SEGMENT4 | — | — |
| 50 | ExpenseTypeSegment5 | SEGMENT5 | — | — |
| 51 | ExpenseTypeSegment6 | SEGMENT6 | — | — |
| 52 | ExpenseTypeSegment7 | SEGMENT7 | — | — |
| 53 | ExpenseTypeSegment8 | SEGMENT8 | — | — |
| 54 | ExpenseTypeSegment9 | SEGMENT9 | — | — |
| 55 | ExpenseTypeStartDate | START_DATE | — | — |
| 56 | ExpenseTypeTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | ✅ |
| 57 | ExpenseTypeTemplateId | EXPENSE_TEMPLATE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
