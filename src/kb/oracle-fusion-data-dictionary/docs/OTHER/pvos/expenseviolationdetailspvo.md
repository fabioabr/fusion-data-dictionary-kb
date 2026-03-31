---
id: DOC-OTHER-PVO-ExpenseViolationDetailsPVO
doc_type: system-doc
title: "ExpenseViolationDetailsPVO — PVO Cross-Module"
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
  - ExpenseViolationDetailsPVO
  - expenseviolationdetailspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenseViolationDetailsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Expense Violation Details. Acessa as tabelas: EXM_EXPENSE_VIOLATIONS.

**Caminho:** `FscmTopModelAM.FinExmEntrySharedAM.ExpenseViolationDetailsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 1 | 1 | 5 | 25% |

---

## 🔗 Tabelas Relacionadas

- [[exm_expense_violations|EXM_EXPENSE_VIOLATIONS]] — 20 atributos (1 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[exm_expense_violations|EXM_EXPENSE_VIOLATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenseViolationDetailsAllowableAmount | ALLOWABLE_AMOUNT | — | — |
| 2 | ExpenseViolationDetailsCreatedBy | CREATED_BY | — | — |
| 3 | ExpenseViolationDetailsCreationDate | CREATION_DATE | — | — |
| 4 | ExpenseViolationDetailsDisplayToUserFlag | DISPLAY_TO_USER_FLAG | — | — |
| 5 | ExpenseViolationDetailsExceededAmount | EXCEEDED_AMOUNT | — | — |
| 6 | ExpenseViolationDetailsExpenseId | EXPENSE_ID | — | — |
| 7 | ExpenseViolationDetailsExpenseReportId | EXPENSE_REPORT_ID | — | — |
| 8 | ExpenseViolationDetailsExpenseTypeCategoryCode | EXPENSE_TYPE_CATEGORY_CODE | — | — |
| 9 | ExpenseViolationDetailsExpenseViolationId | EXPENSE_VIOLATION_ID | 🔑 | ✅ |
| 10 | ExpenseViolationDetailsFuncCurrencyAllowableAmt | FUNC_CURRENCY_ALLOWABLE_AMT | — | — |
| 11 | ExpenseViolationDetailsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | ExpenseViolationDetailsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | ExpenseViolationDetailsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | ExpenseViolationDetailsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | ExpenseViolationDetailsOrgId | ORG_ID | — | — |
| 16 | ExpenseViolationDetailsPersonId | PERSON_ID | — | — |
| 17 | ExpenseViolationDetailsSupervisorId | SUPERVISOR_ID | — | — |
| 18 | ExpenseViolationDetailsViolationDate | VIOLATION_DATE | — | ✅ |
| 19 | ExpenseViolationDetailsViolationSource | VIOLATION_SOURCE | — | ✅ |
| 20 | ExpenseViolationDetailsViolationType | VIOLATION_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
