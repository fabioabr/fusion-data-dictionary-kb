---
id: DOC-OTHER-PVO-ExpenseTemplateExtractPVO
doc_type: system-doc
title: "ExpenseTemplateExtractPVO — PVO Cross-Module"
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
  - ExpenseTemplateExtractPVO
  - expensetemplateextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenseTemplateExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Expense Template Extract. Acessa as tabelas: EXM_EXPENSE_TEMPLATES.

**Caminho:** `FscmTopModelAM.FinExtractAM.ExmBiccExtractAM.ExpenseTemplateExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 1 | 1 | 15 | 71% |

---

## 🔗 Tabelas Relacionadas

- [[exm_expense_templates|EXM_EXPENSE_TEMPLATES]] — 21 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[exm_expense_templates|EXM_EXPENSE_TEMPLATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenseTemplateAllowRcptMissingFlag | ALLOW_RCPT_MISSING_FLAG | — | ✅ |
| 2 | ExpenseTemplateCashReceiptReqFlag | CASH_RECEIPT_REQ_FLAG | — | ✅ |
| 3 | ExpenseTemplateCashReceiptReqLimit | CASH_RECEIPT_REQ_LIMIT | — | ✅ |
| 4 | ExpenseTemplateCcReceiptReqFlag | CC_RECEIPT_REQ_FLAG | — | ✅ |
| 5 | ExpenseTemplateCcReceiptReqLimit | CC_RECEIPT_REQ_LIMIT | — | ✅ |
| 6 | ExpenseTemplateCreatedBy | CREATED_BY | — | — |
| 7 | ExpenseTemplateCreationDate | CREATION_DATE | — | ✅ |
| 8 | ExpenseTemplateDescription | DESCRIPTION | — | ✅ |
| 9 | ExpenseTemplateDfltCcExpTypeId | DFLT_CC_EXP_TYPE_ID | — | — |
| 10 | ExpenseTemplateDispRcptViolationFlag | DISP_RCPT_VIOLATION_FLAG | — | ✅ |
| 11 | ExpenseTemplateEnableCcMappingFlag | ENABLE_CC_MAPPING_FLAG | — | — |
| 12 | ExpenseTemplateId | EXPENSE_TEMPLATE_ID | 🔑 | ✅ |
| 13 | ExpenseTemplateInactiveDate | INACTIVE_DATE | — | ✅ |
| 14 | ExpenseTemplateLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | ExpenseTemplateLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | ExpenseTemplateLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | ExpenseTemplateName | NAME | — | ✅ |
| 18 | ExpenseTemplateNegativeRcptReqFlag | NEGATIVE_RCPT_REQ_FLAG | — | ✅ |
| 19 | ExpenseTemplateObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | ExpenseTemplateOrgId | ORG_ID | — | ✅ |
| 21 | ExpenseTemplateStartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
