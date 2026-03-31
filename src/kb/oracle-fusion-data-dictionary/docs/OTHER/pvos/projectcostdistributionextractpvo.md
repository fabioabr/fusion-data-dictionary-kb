---
id: DOC-OTHER-PVO-ProjectCostDistributionExtractPVO
doc_type: system-doc
title: "ProjectCostDistributionExtractPVO — PVO Cross-Module"
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
  - ProjectCostDistributionExtractPVO
  - projectcostdistributionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectCostDistributionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Cost Distribution Extract. Acessa as tabelas: PJC_COST_DIST_LINES_ALL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjcBiccExtractAM.ProjectCostDistributionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 85 | 1 | 2 | 85 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjc_cost_dist_lines_all|PJC_COST_DIST_LINES_ALL]] — 85 atributos (2 PKs, 85 BICC)

---

## ⚙️ Atributos

### [[pjc_cost_dist_lines_all|PJC_COST_DIST_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjcCostDistLinesAllAccountingStatusCode | ACCOUNTING_STATUS_CODE | — | ✅ |
| 2 | PjcCostDistLinesAllAcctBurdenedCost | ACCT_BURDENED_COST | — | ✅ |
| 3 | PjcCostDistLinesAllAcctCurrencyCode | ACCT_CURRENCY_CODE | — | ✅ |
| 4 | PjcCostDistLinesAllAcctEventId | ACCT_EVENT_ID | — | ✅ |
| 5 | PjcCostDistLinesAllAcctExchangeRate | ACCT_EXCHANGE_RATE | — | ✅ |
| 6 | PjcCostDistLinesAllAcctRateDate | ACCT_RATE_DATE | — | ✅ |
| 7 | PjcCostDistLinesAllAcctRateType | ACCT_RATE_TYPE | — | ✅ |
| 8 | PjcCostDistLinesAllAcctRawCost | ACCT_RAW_COST | — | ✅ |
| 9 | PjcCostDistLinesAllAcctSourceCode | ACCT_SOURCE_CODE | — | ✅ |
| 10 | PjcCostDistLinesAllBillableFlag | BILLABLE_FLAG | — | ✅ |
| 11 | PjcCostDistLinesAllBudgetCcid | BUDGET_CCID | — | ✅ |
| 12 | PjcCostDistLinesAllBudgetPeriodId | BUDGET_PERIOD_ID | — | ✅ |
| 13 | PjcCostDistLinesAllBudgetaryControlValStatus | BUDGETARY_CONTROL_VAL_STATUS | — | ✅ |
| 14 | PjcCostDistLinesAllBurdenCostCrCcid | BURDEN_COST_CR_CCID | — | ✅ |
| 15 | PjcCostDistLinesAllBurdenCostDrCcid | BURDEN_COST_DR_CCID | — | ✅ |
| 16 | PjcCostDistLinesAllBurdenSumRejectionCode | BURDEN_SUM_REJECTION_CODE | — | ✅ |
| 17 | PjcCostDistLinesAllBurdenSumSourceRunId | BURDEN_SUM_SOURCE_RUN_ID | — | ✅ |
| 18 | PjcCostDistLinesAllBurdenedCostCrCcid | BURDENED_COST_CR_CCID | — | ✅ |
| 19 | PjcCostDistLinesAllBurdenedCostDrCcid | BURDENED_COST_DR_CCID | — | ✅ |
| 20 | PjcCostDistLinesAllCapitalizableFlag | CAPITALIZABLE_FLAG | — | ✅ |
| 21 | PjcCostDistLinesAllCompDetailsId | COMP_DETAILS_ID | — | ✅ |
| 22 | PjcCostDistLinesAllCostScheduleId | COST_SCHEDULE_ID | — | ✅ |
| 23 | PjcCostDistLinesAllCostScheduleLineId | COST_SCHEDULE_LINE_ID | — | ✅ |
| 24 | PjcCostDistLinesAllCreatedBy | CREATED_BY | — | ✅ |
| 25 | PjcCostDistLinesAllCreationDate | CREATION_DATE | — | ✅ |
| 26 | PjcCostDistLinesAllDataSetId | DATA_SET_ID | — | ✅ |
| 27 | PjcCostDistLinesAllDenomBurdenedCost | DENOM_BURDENED_COST | — | ✅ |
| 28 | PjcCostDistLinesAllDenomCurrencyCode | DENOM_CURRENCY_CODE | — | ✅ |
| 29 | PjcCostDistLinesAllDenomRawCost | DENOM_RAW_COST | — | ✅ |
| 30 | PjcCostDistLinesAllExpenditureItemId | EXPENDITURE_ITEM_ID | 🔑 | ✅ |
| 31 | PjcCostDistLinesAllIndCompiledSetId | IND_COMPILED_SET_ID | — | ✅ |
| 32 | PjcCostDistLinesAllInterfaceId | INTERFACE_ID | — | ✅ |
| 33 | PjcCostDistLinesAllJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 34 | PjcCostDistLinesAllJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 35 | PjcCostDistLinesAllLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 36 | PjcCostDistLinesAllLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 37 | PjcCostDistLinesAllLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 38 | PjcCostDistLinesAllLineNum | LINE_NUM | 🔑 | ✅ |
| 39 | PjcCostDistLinesAllLineNumReversed | LINE_NUM_REVERSED | — | ✅ |
| 40 | PjcCostDistLinesAllLineType | LINE_TYPE | — | ✅ |
| 41 | PjcCostDistLinesAllNonLaborResourceId | NON_LABOR_RESOURCE_ID | — | ✅ |
| 42 | PjcCostDistLinesAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 43 | PjcCostDistLinesAllOrgId | ORG_ID | — | ✅ |
| 44 | PjcCostDistLinesAllOrgLaborSchRuleId | ORG_LABOR_SCH_RULE_ID | — | ✅ |
| 45 | PjcCostDistLinesAllOrigHistoricalFlag | ORIG_HISTORICAL_FLAG | — | ✅ |
| 46 | PjcCostDistLinesAllParentLineNum | PARENT_LINE_NUM | — | ✅ |
| 47 | PjcCostDistLinesAllPjsSummaryId | PJS_SUMMARY_ID | — | ✅ |
| 48 | PjcCostDistLinesAllPrbsElementId | PRBS_ELEMENT_ID | — | ✅ |
| 49 | PjcCostDistLinesAllPrbsTxnAccumHeaderId | PRBS_TXN_ACCUM_HEADER_ID | — | ✅ |
| 50 | PjcCostDistLinesAllPrevIndCompiledSetId | PREV_IND_COMPILED_SET_ID | — | ✅ |
| 51 | PjcCostDistLinesAllProjectBurdenedCost | PROJECT_BURDENED_COST | — | ✅ |
| 52 | PjcCostDistLinesAllProjectCurrencyCode | PROJECT_CURRENCY_CODE | — | ✅ |
| 53 | PjcCostDistLinesAllProjectExchangeRate | PROJECT_EXCHANGE_RATE | — | ✅ |
| 54 | PjcCostDistLinesAllProjectId | PROJECT_ID | — | ✅ |
| 55 | PjcCostDistLinesAllProjectRateDate | PROJECT_RATE_DATE | — | ✅ |
| 56 | PjcCostDistLinesAllProjectRateType | PROJECT_RATE_TYPE | — | ✅ |
| 57 | PjcCostDistLinesAllProjectRawCost | PROJECT_RAW_COST | — | ✅ |
| 58 | PjcCostDistLinesAllProjectUnitId | PROJECT_UNIT_ID | — | ✅ |
| 59 | PjcCostDistLinesAllProjfuncBurdenedCost | PROJFUNC_BURDENED_COST | — | ✅ |
| 60 | PjcCostDistLinesAllProjfuncCostExchangeRate | PROJFUNC_COST_EXCHANGE_RATE | — | ✅ |
| 61 | PjcCostDistLinesAllProjfuncCostRateDate | PROJFUNC_COST_RATE_DATE | — | ✅ |
| 62 | PjcCostDistLinesAllProjfuncCostRateType | PROJFUNC_COST_RATE_TYPE | — | ✅ |
| 63 | PjcCostDistLinesAllProjfuncCurrencyCode | PROJFUNC_CURRENCY_CODE | — | ✅ |
| 64 | PjcCostDistLinesAllProjfuncRawCost | PROJFUNC_RAW_COST | — | ✅ |
| 65 | PjcCostDistLinesAllPrvdrGlDate | PRVDR_GL_DATE | — | ✅ |
| 66 | PjcCostDistLinesAllPrvdrGlPeriodName | PRVDR_GL_PERIOD_NAME | — | ✅ |
| 67 | PjcCostDistLinesAllPrvdrPaDate | PRVDR_PA_DATE | — | ✅ |
| 68 | PjcCostDistLinesAllPrvdrPaPeriodName | PRVDR_PA_PERIOD_NAME | — | ✅ |
| 69 | PjcCostDistLinesAllQuantity | QUANTITY | — | ✅ |
| 70 | PjcCostDistLinesAllRateOverrideId | RATE_OVERRIDE_ID | — | ✅ |
| 71 | PjcCostDistLinesAllRawCostCrCcid | RAW_COST_CR_CCID | — | ✅ |
| 72 | PjcCostDistLinesAllRawCostDrCcid | RAW_COST_DR_CCID | — | ✅ |
| 73 | PjcCostDistLinesAllRawLineNumReversed | RAW_LINE_NUM_REVERSED | — | ✅ |
| 74 | PjcCostDistLinesAllRecvrGlDate | RECVR_GL_DATE | — | ✅ |
| 75 | PjcCostDistLinesAllRecvrGlPeriodName | RECVR_GL_PERIOD_NAME | — | ✅ |
| 76 | PjcCostDistLinesAllRecvrPaDate | RECVR_PA_DATE | — | ✅ |
| 77 | PjcCostDistLinesAllRecvrPaPeriodName | RECVR_PA_PERIOD_NAME | — | ✅ |
| 78 | PjcCostDistLinesAllRequestId | REQUEST_ID | — | ✅ |
| 79 | PjcCostDistLinesAllReversedFlag | REVERSED_FLAG | — | ✅ |
| 80 | PjcCostDistLinesAllSiAssetsAdditionFlag | SI_ASSETS_ADDITION_FLAG | — | ✅ |
| 81 | PjcCostDistLinesAllTaskId | TASK_ID | — | ✅ |
| 82 | PjcCostDistLinesAllTransferRejectionReason | TRANSFER_REJECTION_REASON | — | ✅ |
| 83 | PjcCostDistLinesAllTransferStatusCode | TRANSFER_STATUS_CODE | — | ✅ |
| 84 | PjcCostDistLinesAllTxnAccumHeaderId | TXN_ACCUM_HEADER_ID | — | ✅ |
| 85 | PjcCostDistLinesAllWorkTypeId | WORK_TYPE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
