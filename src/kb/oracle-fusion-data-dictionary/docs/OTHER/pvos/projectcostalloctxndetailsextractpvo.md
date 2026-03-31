---
id: DOC-OTHER-PVO-ProjectCostAllocTxnDetailsExtractPVO
doc_type: system-doc
title: "ProjectCostAllocTxnDetailsExtractPVO — PVO Cross-Module"
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
  - ProjectCostAllocTxnDetailsExtractPVO
  - projectcostalloctxndetailsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectCostAllocTxnDetailsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Cost Alloc Txn Details Extract. Acessa as tabelas: PJC_ALLOC_TXN_DETAILS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjcBiccExtractAM.ProjectCostAllocTxnDetailsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 66 | 1 | 1 | 37 | 56% |

---

## 🔗 Tabelas Relacionadas

- [[pjc_alloc_txn_details|PJC_ALLOC_TXN_DETAILS]] — 66 atributos (1 PKs, 37 BICC)

---

## ⚙️ Atributos

### [[pjc_alloc_txn_details|PJC_ALLOC_TXN_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LaborAllocTxnDetailsPEOAllocTxnId | ALLOC_TXN_ID | 🔑 | ✅ |
| 2 | LaborAllocTxnDetailsPEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | LaborAllocTxnDetailsPEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | LaborAllocTxnDetailsPEOAttribute2 | ATTRIBUTE2 | — | — |
| 5 | LaborAllocTxnDetailsPEOAttribute3 | ATTRIBUTE3 | — | — |
| 6 | LaborAllocTxnDetailsPEOAttribute4 | ATTRIBUTE4 | — | — |
| 7 | LaborAllocTxnDetailsPEOAttribute5 | ATTRIBUTE5 | — | — |
| 8 | LaborAllocTxnDetailsPEOAttribute6 | ATTRIBUTE6 | — | — |
| 9 | LaborAllocTxnDetailsPEOAttribute7 | ATTRIBUTE7 | — | — |
| 10 | LaborAllocTxnDetailsPEOAttribute8 | ATTRIBUTE8 | — | — |
| 11 | LaborAllocTxnDetailsPEOAttribute9 | ATTRIBUTE9 | — | — |
| 12 | LaborAllocTxnDetailsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 13 | LaborAllocTxnDetailsPEOBillableFlag | BILLABLE_FLAG | — | ✅ |
| 14 | LaborAllocTxnDetailsPEOCapitalizableFlag | CAPITALIZABLE_FLAG | — | ✅ |
| 15 | LaborAllocTxnDetailsPEOContextCategory | CONTEXT_CATEGORY | — | ✅ |
| 16 | LaborAllocTxnDetailsPEOContractId | CONTRACT_ID | — | ✅ |
| 17 | LaborAllocTxnDetailsPEOContractLineId | CONTRACT_LINE_ID | — | ✅ |
| 18 | LaborAllocTxnDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 19 | LaborAllocTxnDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 20 | LaborAllocTxnDetailsPEOCurrentAllocation | CURRENT_ALLOCATION | — | ✅ |
| 21 | LaborAllocTxnDetailsPEOExpenditureItemDate | EXPENDITURE_ITEM_DATE | — | ✅ |
| 22 | LaborAllocTxnDetailsPEOExpenditureItemId | EXPENDITURE_ITEM_ID | — | ✅ |
| 23 | LaborAllocTxnDetailsPEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | ✅ |
| 24 | LaborAllocTxnDetailsPEOFiscalYear | FISCAL_YEAR | — | ✅ |
| 25 | LaborAllocTxnDetailsPEOFundingAllocationId | FUNDING_ALLOCATION_ID | — | ✅ |
| 26 | LaborAllocTxnDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 27 | LaborAllocTxnDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 28 | LaborAllocTxnDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 29 | LaborAllocTxnDetailsPEOLdAdjustedAllocTxnId | LD_ADJUSTED_ALLOC_TXN_ID | — | ✅ |
| 30 | LaborAllocTxnDetailsPEOLdTargetCcid | LD_TARGET_CCID | — | ✅ |
| 31 | LaborAllocTxnDetailsPEOLineNum | LINE_NUM | — | ✅ |
| 32 | LaborAllocTxnDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 33 | LaborAllocTxnDetailsPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 34 | LaborAllocTxnDetailsPEOPeriodNum | PERIOD_NUM | — | ✅ |
| 35 | LaborAllocTxnDetailsPEOPreviousAllocation | PREVIOUS_ALLOCATION | — | ✅ |
| 36 | LaborAllocTxnDetailsPEOProjectId | PROJECT_ID | — | ✅ |
| 37 | LaborAllocTxnDetailsPEOQuarterNum | QUARTER_NUM | — | ✅ |
| 38 | LaborAllocTxnDetailsPEOReservedAttribute1 | RESERVED_ATTRIBUTE1 | — | ✅ |
| 39 | LaborAllocTxnDetailsPEOReservedAttribute10 | RESERVED_ATTRIBUTE10 | — | ✅ |
| 40 | LaborAllocTxnDetailsPEOReservedAttribute2 | RESERVED_ATTRIBUTE2 | — | — |
| 41 | LaborAllocTxnDetailsPEOReservedAttribute3 | RESERVED_ATTRIBUTE3 | — | — |
| 42 | LaborAllocTxnDetailsPEOReservedAttribute4 | RESERVED_ATTRIBUTE4 | — | — |
| 43 | LaborAllocTxnDetailsPEOReservedAttribute5 | RESERVED_ATTRIBUTE5 | — | — |
| 44 | LaborAllocTxnDetailsPEOReservedAttribute6 | RESERVED_ATTRIBUTE6 | — | — |
| 45 | LaborAllocTxnDetailsPEOReservedAttribute7 | RESERVED_ATTRIBUTE7 | — | — |
| 46 | LaborAllocTxnDetailsPEOReservedAttribute8 | RESERVED_ATTRIBUTE8 | — | — |
| 47 | LaborAllocTxnDetailsPEOReservedAttribute9 | RESERVED_ATTRIBUTE9 | — | — |
| 48 | LaborAllocTxnDetailsPEORuleId | RULE_ID | — | ✅ |
| 49 | LaborAllocTxnDetailsPEORunId | RUN_ID | — | ✅ |
| 50 | LaborAllocTxnDetailsPEORunPeriod | RUN_PERIOD | — | ✅ |
| 51 | LaborAllocTxnDetailsPEORunTargetId | RUN_TARGET_ID | — | ✅ |
| 52 | LaborAllocTxnDetailsPEOStatusCode | STATUS_CODE | — | ✅ |
| 53 | LaborAllocTxnDetailsPEOTaskId | TASK_ID | — | ✅ |
| 54 | LaborAllocTxnDetailsPEOTotalAllocation | TOTAL_ALLOCATION | — | ✅ |
| 55 | LaborAllocTxnDetailsPEOTransactionType | TRANSACTION_TYPE | — | ✅ |
| 56 | LaborAllocTxnDetailsPEOUserDefAttribute1 | USER_DEF_ATTRIBUTE1 | — | — |
| 57 | LaborAllocTxnDetailsPEOUserDefAttribute10 | USER_DEF_ATTRIBUTE10 | — | — |
| 58 | LaborAllocTxnDetailsPEOUserDefAttribute2 | USER_DEF_ATTRIBUTE2 | — | — |
| 59 | LaborAllocTxnDetailsPEOUserDefAttribute3 | USER_DEF_ATTRIBUTE3 | — | — |
| 60 | LaborAllocTxnDetailsPEOUserDefAttribute4 | USER_DEF_ATTRIBUTE4 | — | — |
| 61 | LaborAllocTxnDetailsPEOUserDefAttribute5 | USER_DEF_ATTRIBUTE5 | — | — |
| 62 | LaborAllocTxnDetailsPEOUserDefAttribute6 | USER_DEF_ATTRIBUTE6 | — | — |
| 63 | LaborAllocTxnDetailsPEOUserDefAttribute7 | USER_DEF_ATTRIBUTE7 | — | — |
| 64 | LaborAllocTxnDetailsPEOUserDefAttribute8 | USER_DEF_ATTRIBUTE8 | — | — |
| 65 | LaborAllocTxnDetailsPEOUserDefAttribute9 | USER_DEF_ATTRIBUTE9 | — | — |
| 66 | LaborAllocTxnDetailsPEOWorkTypeId | WORK_TYPE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
