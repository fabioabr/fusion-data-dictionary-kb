---
id: DOC-OTHER-PVO-LaborCostDistributionExtractPVO
doc_type: system-doc
title: "LaborCostDistributionExtractPVO — PVO Cross-Module"
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
  - LaborCostDistributionExtractPVO
  - laborcostdistributionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LaborCostDistributionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Labor Cost Distribution Extract. Acessa as tabelas: PJC_LABOR_DIST_TXN_DETAILS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjcBiccExtractAM.LaborCostDistributionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 74 | 1 | 1 | 45 | 61% |

---

## 🔗 Tabelas Relacionadas

- [[pjc_labor_dist_txn_details|PJC_LABOR_DIST_TXN_DETAILS]] — 74 atributos (1 PKs, 45 BICC)

---

## ⚙️ Atributos

### [[pjc_labor_dist_txn_details|PJC_LABOR_DIST_TXN_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LaborDistTxnDetailsPEOAcctEventId | ACCT_EVENT_ID | — | ✅ |
| 2 | LaborDistTxnDetailsPEOAdjustedAllocTxnId | ADJUSTED_ALLOC_TXN_ID | — | ✅ |
| 3 | LaborDistTxnDetailsPEOAllocTxnId | ALLOC_TXN_ID | — | ✅ |
| 4 | LaborDistTxnDetailsPEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 5 | LaborDistTxnDetailsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 6 | LaborDistTxnDetailsPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 7 | LaborDistTxnDetailsPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 8 | LaborDistTxnDetailsPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 9 | LaborDistTxnDetailsPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 10 | LaborDistTxnDetailsPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 11 | LaborDistTxnDetailsPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 12 | LaborDistTxnDetailsPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 13 | LaborDistTxnDetailsPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 14 | LaborDistTxnDetailsPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 15 | LaborDistTxnDetailsPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 16 | LaborDistTxnDetailsPEOBillableFlag | BILLABLE_FLAG | — | ✅ |
| 17 | LaborDistTxnDetailsPEOCapitalizableFlag | CAPITALIZABLE_FLAG | — | ✅ |
| 18 | LaborDistTxnDetailsPEOContextCategory | CONTEXT_CATEGORY | — | ✅ |
| 19 | LaborDistTxnDetailsPEOContractId | CONTRACT_ID | — | ✅ |
| 20 | LaborDistTxnDetailsPEOContractLineId | CONTRACT_LINE_ID | — | ✅ |
| 21 | LaborDistTxnDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 22 | LaborDistTxnDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 23 | LaborDistTxnDetailsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 24 | LaborDistTxnDetailsPEOElementType | ELEMENT_TYPE | — | ✅ |
| 25 | LaborDistTxnDetailsPEOExpenditureItemDate | EXPENDITURE_ITEM_DATE | — | ✅ |
| 26 | LaborDistTxnDetailsPEOExpenditureItemId | EXPENDITURE_ITEM_ID | — | ✅ |
| 27 | LaborDistTxnDetailsPEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | ✅ |
| 28 | LaborDistTxnDetailsPEOFundingAllocationId | FUNDING_ALLOCATION_ID | — | ✅ |
| 29 | LaborDistTxnDetailsPEOInterfaceId | INTERFACE_ID | — | ✅ |
| 30 | LaborDistTxnDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 31 | LaborDistTxnDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 32 | LaborDistTxnDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 33 | LaborDistTxnDetailsPEOLdElementTypeId | LD_ELEMENT_TYPE_ID | — | ✅ |
| 34 | LaborDistTxnDetailsPEOLdTxnId | LD_TXN_ID | 🔑 | ✅ |
| 35 | LaborDistTxnDetailsPEOLineNum | LINE_NUM | — | ✅ |
| 36 | LaborDistTxnDetailsPEOLinePercent | LINE_PERCENT | — | ✅ |
| 37 | LaborDistTxnDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 38 | LaborDistTxnDetailsPEOOrgId | ORG_ID | — | ✅ |
| 39 | LaborDistTxnDetailsPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 40 | LaborDistTxnDetailsPEOPeriodEndDate | PERIOD_END_DATE | — | ✅ |
| 41 | LaborDistTxnDetailsPEOPeriodStartDate | PERIOD_START_DATE | — | ✅ |
| 42 | LaborDistTxnDetailsPEOPersonId | PERSON_ID | — | ✅ |
| 43 | LaborDistTxnDetailsPEOProcessingEndDate | PROCESSING_END_DATE | — | ✅ |
| 44 | LaborDistTxnDetailsPEOProcessingStartDate | PROCESSING_START_DATE | — | ✅ |
| 45 | LaborDistTxnDetailsPEOProjectId | PROJECT_ID | — | ✅ |
| 46 | LaborDistTxnDetailsPEOReservedAttribute1 | RESERVED_ATTRIBUTE1 | — | ✅ |
| 47 | LaborDistTxnDetailsPEOReservedAttribute10 | RESERVED_ATTRIBUTE10 | — | ✅ |
| 48 | LaborDistTxnDetailsPEOReservedAttribute2 | RESERVED_ATTRIBUTE2 | — | — |
| 49 | LaborDistTxnDetailsPEOReservedAttribute3 | RESERVED_ATTRIBUTE3 | — | — |
| 50 | LaborDistTxnDetailsPEOReservedAttribute4 | RESERVED_ATTRIBUTE4 | — | — |
| 51 | LaborDistTxnDetailsPEOReservedAttribute5 | RESERVED_ATTRIBUTE5 | — | — |
| 52 | LaborDistTxnDetailsPEOReservedAttribute6 | RESERVED_ATTRIBUTE6 | — | — |
| 53 | LaborDistTxnDetailsPEOReservedAttribute7 | RESERVED_ATTRIBUTE7 | — | — |
| 54 | LaborDistTxnDetailsPEOReservedAttribute8 | RESERVED_ATTRIBUTE8 | — | — |
| 55 | LaborDistTxnDetailsPEOReservedAttribute9 | RESERVED_ATTRIBUTE9 | — | — |
| 56 | LaborDistTxnDetailsPEORuleId | RULE_ID | — | ✅ |
| 57 | LaborDistTxnDetailsPEORunId | RUN_ID | — | ✅ |
| 58 | LaborDistTxnDetailsPEORunSourceDetId | RUN_SOURCE_DET_ID | — | ✅ |
| 59 | LaborDistTxnDetailsPEORunTargetId | RUN_TARGET_ID | — | ✅ |
| 60 | LaborDistTxnDetailsPEOTargetCcid | TARGET_CCID | — | ✅ |
| 61 | LaborDistTxnDetailsPEOTaskId | TASK_ID | — | ✅ |
| 62 | LaborDistTxnDetailsPEOTotalAllocation | TOTAL_ALLOCATION | — | ✅ |
| 63 | LaborDistTxnDetailsPEOTotalPoolAmount | TOTAL_POOL_AMOUNT | — | ✅ |
| 64 | LaborDistTxnDetailsPEOUserDefAttribute1 | USER_DEF_ATTRIBUTE1 | — | — |
| 65 | LaborDistTxnDetailsPEOUserDefAttribute10 | USER_DEF_ATTRIBUTE10 | — | — |
| 66 | LaborDistTxnDetailsPEOUserDefAttribute2 | USER_DEF_ATTRIBUTE2 | — | — |
| 67 | LaborDistTxnDetailsPEOUserDefAttribute3 | USER_DEF_ATTRIBUTE3 | — | — |
| 68 | LaborDistTxnDetailsPEOUserDefAttribute4 | USER_DEF_ATTRIBUTE4 | — | — |
| 69 | LaborDistTxnDetailsPEOUserDefAttribute5 | USER_DEF_ATTRIBUTE5 | — | — |
| 70 | LaborDistTxnDetailsPEOUserDefAttribute6 | USER_DEF_ATTRIBUTE6 | — | — |
| 71 | LaborDistTxnDetailsPEOUserDefAttribute7 | USER_DEF_ATTRIBUTE7 | — | — |
| 72 | LaborDistTxnDetailsPEOUserDefAttribute8 | USER_DEF_ATTRIBUTE8 | — | — |
| 73 | LaborDistTxnDetailsPEOUserDefAttribute9 | USER_DEF_ATTRIBUTE9 | — | — |
| 74 | LaborDistTxnDetailsPEOWorkTypeId | WORK_TYPE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
