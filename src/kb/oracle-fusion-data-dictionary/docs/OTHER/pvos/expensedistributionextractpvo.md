---
id: DOC-OTHER-PVO-ExpenseDistributionExtractPVO
doc_type: system-doc
title: "ExpenseDistributionExtractPVO — PVO Cross-Module"
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
  - ExpenseDistributionExtractPVO
  - expensedistributionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenseDistributionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Expense Distribution Extract. Acessa as tabelas: EXM_EXPENSE_DISTS.

**Caminho:** `FscmTopModelAM.FinExtractAM.ExmBiccExtractAM.ExpenseDistributionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 77 | 1 | 1 | 23 | 30% |

---

## 🔗 Tabelas Relacionadas

- [[exm_expense_dists|EXM_EXPENSE_DISTS]] — 77 atributos (1 PKs, 23 BICC)

---

## ⚙️ Atributos

### [[exm_expense_dists|EXM_EXPENSE_DISTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenseDistributionCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 2 | ExpenseDistributionCostCenter | COST_CENTER | — | ✅ |
| 3 | ExpenseDistributionCreatedBy | CREATED_BY | — | — |
| 4 | ExpenseDistributionCreationDate | CREATION_DATE | — | ✅ |
| 5 | ExpenseDistributionExpenseId | EXPENSE_ID | — | ✅ |
| 6 | ExpenseDistributionExpenseReportId | EXPENSE_REPORT_ID | — | ✅ |
| 7 | ExpenseDistributionId | EXPENSE_DIST_ID | 🔑 | ✅ |
| 8 | ExpenseDistributionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ExpenseDistributionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | ExpenseDistributionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | ExpenseDistributionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ExpenseDistributionOrgId | ORG_ID | — | ✅ |
| 13 | ExpenseDistributionPjcBillableFlag | PJC_BILLABLE_FLAG | — | ✅ |
| 14 | ExpenseDistributionPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | ✅ |
| 15 | ExpenseDistributionPjcContextCategory | PJC_CONTEXT_CATEGORY | — | ✅ |
| 16 | ExpenseDistributionPjcContractId | PJC_CONTRACT_ID | — | ✅ |
| 17 | ExpenseDistributionPjcContractLineId | PJC_CONTRACT_LINE_ID | — | ✅ |
| 18 | ExpenseDistributionPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | ✅ |
| 19 | ExpenseDistributionPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | ✅ |
| 20 | ExpenseDistributionPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | ✅ |
| 21 | ExpenseDistributionPjcOrganizationId | PJC_ORGANIZATION_ID | — | ✅ |
| 22 | ExpenseDistributionPjcProjectId | PJC_PROJECT_ID | — | ✅ |
| 23 | ExpenseDistributionPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 24 | ExpenseDistributionPjcReservedAttribute10 | PJC_RESERVED_ATTRIBUTE10 | — | — |
| 25 | ExpenseDistributionPjcReservedAttribute2 | PJC_RESERVED_ATTRIBUTE2 | — | — |
| 26 | ExpenseDistributionPjcReservedAttribute3 | PJC_RESERVED_ATTRIBUTE3 | — | — |
| 27 | ExpenseDistributionPjcReservedAttribute4 | PJC_RESERVED_ATTRIBUTE4 | — | — |
| 28 | ExpenseDistributionPjcReservedAttribute5 | PJC_RESERVED_ATTRIBUTE5 | — | — |
| 29 | ExpenseDistributionPjcReservedAttribute6 | PJC_RESERVED_ATTRIBUTE6 | — | — |
| 30 | ExpenseDistributionPjcReservedAttribute7 | PJC_RESERVED_ATTRIBUTE7 | — | — |
| 31 | ExpenseDistributionPjcReservedAttribute8 | PJC_RESERVED_ATTRIBUTE8 | — | — |
| 32 | ExpenseDistributionPjcReservedAttribute9 | PJC_RESERVED_ATTRIBUTE9 | — | — |
| 33 | ExpenseDistributionPjcTaskId | PJC_TASK_ID | — | ✅ |
| 34 | ExpenseDistributionPjcUserDefAttribute1 | PJC_USER_DEF_ATTRIBUTE1 | — | — |
| 35 | ExpenseDistributionPjcUserDefAttribute10 | PJC_USER_DEF_ATTRIBUTE10 | — | — |
| 36 | ExpenseDistributionPjcUserDefAttribute2 | PJC_USER_DEF_ATTRIBUTE2 | — | — |
| 37 | ExpenseDistributionPjcUserDefAttribute3 | PJC_USER_DEF_ATTRIBUTE3 | — | — |
| 38 | ExpenseDistributionPjcUserDefAttribute4 | PJC_USER_DEF_ATTRIBUTE4 | — | — |
| 39 | ExpenseDistributionPjcUserDefAttribute5 | PJC_USER_DEF_ATTRIBUTE5 | — | — |
| 40 | ExpenseDistributionPjcUserDefAttribute6 | PJC_USER_DEF_ATTRIBUTE6 | — | — |
| 41 | ExpenseDistributionPjcUserDefAttribute7 | PJC_USER_DEF_ATTRIBUTE7 | — | — |
| 42 | ExpenseDistributionPjcUserDefAttribute8 | PJC_USER_DEF_ATTRIBUTE8 | — | — |
| 43 | ExpenseDistributionPjcUserDefAttribute9 | PJC_USER_DEF_ATTRIBUTE9 | — | — |
| 44 | ExpenseDistributionPjcWorkTypeId | PJC_WORK_TYPE_ID | — | ✅ |
| 45 | ExpenseDistributionPreparerModifiedFlag | PREPARER_MODIFIED_FLAG | — | — |
| 46 | ExpenseDistributionReimbursableAmount | REIMBURSABLE_AMOUNT | — | ✅ |
| 47 | ExpenseDistributionSegment1 | SEGMENT1 | — | ✅ |
| 48 | ExpenseDistributionSegment10 | SEGMENT10 | — | — |
| 49 | ExpenseDistributionSegment11 | SEGMENT11 | — | — |
| 50 | ExpenseDistributionSegment12 | SEGMENT12 | — | — |
| 51 | ExpenseDistributionSegment13 | SEGMENT13 | — | — |
| 52 | ExpenseDistributionSegment14 | SEGMENT14 | — | — |
| 53 | ExpenseDistributionSegment15 | SEGMENT15 | — | — |
| 54 | ExpenseDistributionSegment16 | SEGMENT16 | — | — |
| 55 | ExpenseDistributionSegment17 | SEGMENT17 | — | — |
| 56 | ExpenseDistributionSegment18 | SEGMENT18 | — | — |
| 57 | ExpenseDistributionSegment19 | SEGMENT19 | — | — |
| 58 | ExpenseDistributionSegment2 | SEGMENT2 | — | ✅ |
| 59 | ExpenseDistributionSegment20 | SEGMENT20 | — | — |
| 60 | ExpenseDistributionSegment21 | SEGMENT21 | — | — |
| 61 | ExpenseDistributionSegment22 | SEGMENT22 | — | — |
| 62 | ExpenseDistributionSegment23 | SEGMENT23 | — | — |
| 63 | ExpenseDistributionSegment24 | SEGMENT24 | — | — |
| 64 | ExpenseDistributionSegment25 | SEGMENT25 | — | — |
| 65 | ExpenseDistributionSegment26 | SEGMENT26 | — | — |
| 66 | ExpenseDistributionSegment27 | SEGMENT27 | — | — |
| 67 | ExpenseDistributionSegment28 | SEGMENT28 | — | — |
| 68 | ExpenseDistributionSegment29 | SEGMENT29 | — | — |
| 69 | ExpenseDistributionSegment3 | SEGMENT3 | — | — |
| 70 | ExpenseDistributionSegment30 | SEGMENT30 | — | — |
| 71 | ExpenseDistributionSegment4 | SEGMENT4 | — | — |
| 72 | ExpenseDistributionSegment5 | SEGMENT5 | — | — |
| 73 | ExpenseDistributionSegment6 | SEGMENT6 | — | — |
| 74 | ExpenseDistributionSegment7 | SEGMENT7 | — | — |
| 75 | ExpenseDistributionSegment8 | SEGMENT8 | — | — |
| 76 | ExpenseDistributionSegment9 | SEGMENT9 | — | — |
| 77 | ExpenseDistributionSequenceNum | SEQUENCE_NUM | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
