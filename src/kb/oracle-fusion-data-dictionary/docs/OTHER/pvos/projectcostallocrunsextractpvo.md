---
id: DOC-OTHER-PVO-ProjectCostAllocRunsExtractPVO
doc_type: system-doc
title: "ProjectCostAllocRunsExtractPVO — PVO Cross-Module"
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
  - ProjectCostAllocRunsExtractPVO
  - projectcostallocrunsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectCostAllocRunsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Cost Alloc Runs Extract. Acessa as tabelas: PJC_ALLOC_RUNS_ALL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjcBiccExtractAM.ProjectCostAllocRunsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 103 | 1 | 1 | 103 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjc_alloc_runs_all|PJC_ALLOC_RUNS_ALL]] — 103 atributos (1 PKs, 103 BICC)

---

## ⚙️ Atributos

### [[pjc_alloc_runs_all|PJC_ALLOC_RUNS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LaborDistRunsAllPEOAllocRbsHeaderId | ALLOC_RBS_HEADER_ID | — | ✅ |
| 2 | LaborDistRunsAllPEOAllocRbsVersion | ALLOC_RBS_VERSION | — | ✅ |
| 3 | LaborDistRunsAllPEOAllocatedAmount | ALLOCATED_AMOUNT | — | ✅ |
| 4 | LaborDistRunsAllPEOAllocationMethod | ALLOCATION_METHOD | — | ✅ |
| 5 | LaborDistRunsAllPEOAutoReleaseFlag | AUTO_RELEASE_FLAG | — | ✅ |
| 6 | LaborDistRunsAllPEOBasisAmountType | BASIS_AMOUNT_TYPE | — | ✅ |
| 7 | LaborDistRunsAllPEOBasisBalanceCategory | BASIS_BALANCE_CATEGORY | — | ✅ |
| 8 | LaborDistRunsAllPEOBasisBalanceType | BASIS_BALANCE_TYPE | — | ✅ |
| 9 | LaborDistRunsAllPEOBasisFinPlanTypeId | BASIS_FIN_PLAN_TYPE_ID | — | ✅ |
| 10 | LaborDistRunsAllPEOBasisMethod | BASIS_METHOD | — | ✅ |
| 11 | LaborDistRunsAllPEOBasisRbsHeaderId | BASIS_RBS_HEADER_ID | — | ✅ |
| 12 | LaborDistRunsAllPEOBasisRbsVersion | BASIS_RBS_VERSION | — | ✅ |
| 13 | LaborDistRunsAllPEOBasisRelativeEndDate | BASIS_RELATIVE_END_DATE | — | ✅ |
| 14 | LaborDistRunsAllPEOBasisRelativeFiscalYear | BASIS_RELATIVE_FISCAL_YEAR | — | ✅ |
| 15 | LaborDistRunsAllPEOBasisRelativePeriod | BASIS_RELATIVE_PERIOD | — | ✅ |
| 16 | LaborDistRunsAllPEOBasisRelativePeriodName | BASIS_RELATIVE_PERIOD_NAME | — | ✅ |
| 17 | LaborDistRunsAllPEOBasisRelativePeriodNum | BASIS_RELATIVE_PERIOD_NUM | — | ✅ |
| 18 | LaborDistRunsAllPEOBasisRelativeQuarterNum | BASIS_RELATIVE_QUARTER_NUM | — | ✅ |
| 19 | LaborDistRunsAllPEOBasisRelativeStartDate | BASIS_RELATIVE_START_DATE | — | ✅ |
| 20 | LaborDistRunsAllPEOBcPassFlag | BC_PASS_FLAG | — | ✅ |
| 21 | LaborDistRunsAllPEOCostActionId | COST_ACTION_ID | — | ✅ |
| 22 | LaborDistRunsAllPEOCostActionType | COST_ACTION_TYPE | — | ✅ |
| 23 | LaborDistRunsAllPEOCostAllocationKeyflexId | COST_ALLOCATION_KEYFLEX_ID | — | ✅ |
| 24 | LaborDistRunsAllPEOCostId | COST_ID | — | ✅ |
| 25 | LaborDistRunsAllPEOCreatedBy | CREATED_BY | — | ✅ |
| 26 | LaborDistRunsAllPEOCreationDate | CREATION_DATE | — | ✅ |
| 27 | LaborDistRunsAllPEODeleteFlag | DELETE_FLAG | — | ✅ |
| 28 | LaborDistRunsAllPEODenomCurrencyCode | DENOM_CURRENCY_CODE | — | ✅ |
| 29 | LaborDistRunsAllPEODocumentId | DOCUMENT_ID | — | ✅ |
| 30 | LaborDistRunsAllPEODraftRequestDate | DRAFT_REQUEST_DATE | — | ✅ |
| 31 | LaborDistRunsAllPEODraftRequestId | DRAFT_REQUEST_ID | — | ✅ |
| 32 | LaborDistRunsAllPEODupTargetsFlag | DUP_TARGETS_FLAG | — | ✅ |
| 33 | LaborDistRunsAllPEOExpndItemDate | EXPND_ITEM_DATE | — | ✅ |
| 34 | LaborDistRunsAllPEOFiscalYear | FISCAL_YEAR | — | ✅ |
| 35 | LaborDistRunsAllPEOFixedAmount | FIXED_AMOUNT | — | ✅ |
| 36 | LaborDistRunsAllPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 37 | LaborDistRunsAllPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 38 | LaborDistRunsAllPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 39 | LaborDistRunsAllPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 40 | LaborDistRunsAllPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 41 | LaborDistRunsAllPEOLdAssignmentId | LD_ASSIGNMENT_ID | — | ✅ |
| 42 | LaborDistRunsAllPEOLdBatchName | LD_BATCH_NAME | — | ✅ |
| 43 | LaborDistRunsAllPEOLdDailyRate | LD_DAILY_RATE | — | ✅ |
| 44 | LaborDistRunsAllPEOLdElementType | LD_ELEMENT_TYPE | — | ✅ |
| 45 | LaborDistRunsAllPEOLdElementTypeId | LD_ELEMENT_TYPE_ID | — | ✅ |
| 46 | LaborDistRunsAllPEOLdInterfaceId | LD_INTERFACE_ID | — | ✅ |
| 47 | LaborDistRunsAllPEOLdOrigTransactionReference | LD_ORIG_TRANSACTION_REFERENCE | — | ✅ |
| 48 | LaborDistRunsAllPEOLdPeriodEndDate | LD_PERIOD_END_DATE | — | ✅ |
| 49 | LaborDistRunsAllPEOLdPeriodStartDate | LD_PERIOD_START_DATE | — | ✅ |
| 50 | LaborDistRunsAllPEOLdPersonId | LD_PERSON_ID | — | ✅ |
| 51 | LaborDistRunsAllPEOLimitTargetProjectsCode | LIMIT_TARGET_PROJECTS_CODE | — | ✅ |
| 52 | LaborDistRunsAllPEOMissingOffsetProjAmt | MISSING_OFFSET_PROJ_AMT | — | ✅ |
| 53 | LaborDistRunsAllPEOMissingSourceProjAmt | MISSING_SOURCE_PROJ_AMT | — | ✅ |
| 54 | LaborDistRunsAllPEOMissingTargetProjAmt | MISSING_TARGET_PROJ_AMT | — | ✅ |
| 55 | LaborDistRunsAllPEONetZeroAdjustmentFlag | NET_ZERO_ADJUSTMENT_FLAG | — | ✅ |
| 56 | LaborDistRunsAllPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 57 | LaborDistRunsAllPEOOccurPayPeriodEndDate | OCCUR_PAY_PERIOD_END_DATE | — | ✅ |
| 58 | LaborDistRunsAllPEOOccurPayPeriodStartDate | OCCUR_PAY_PERIOD_START_DATE | — | ✅ |
| 59 | LaborDistRunsAllPEOOffsetCostType | OFFSET_COST_TYPE | — | ✅ |
| 60 | LaborDistRunsAllPEOOffsetExpOrgId | OFFSET_EXP_ORG_ID | — | ✅ |
| 61 | LaborDistRunsAllPEOOffsetExpTypeClass | OFFSET_EXP_TYPE_CLASS | — | ✅ |
| 62 | LaborDistRunsAllPEOOffsetExpTypeId | OFFSET_EXP_TYPE_ID | — | ✅ |
| 63 | LaborDistRunsAllPEOOffsetMethod | OFFSET_METHOD | — | ✅ |
| 64 | LaborDistRunsAllPEOOffsetProjectId | OFFSET_PROJECT_ID | — | ✅ |
| 65 | LaborDistRunsAllPEOOffsetTaskId | OFFSET_TASK_ID | — | ✅ |
| 66 | LaborDistRunsAllPEOOrgId | ORG_ID | — | ✅ |
| 67 | LaborDistRunsAllPEOOverridenBasisMethod | OVERRIDEN_BASIS_METHOD | — | ✅ |
| 68 | LaborDistRunsAllPEOPayrollEffectiveDate | PAYROLL_EFFECTIVE_DATE | — | ✅ |
| 69 | LaborDistRunsAllPEOPayrollId | PAYROLL_ID | — | ✅ |
| 70 | LaborDistRunsAllPEOPayrollLoadRequestId | PAYROLL_LOAD_REQUEST_ID | — | ✅ |
| 71 | LaborDistRunsAllPEOPayrollName | PAYROLL_NAME | — | ✅ |
| 72 | LaborDistRunsAllPEOPayrollRelActionId | PAYROLL_REL_ACTION_ID | — | ✅ |
| 73 | LaborDistRunsAllPEOPeriodNum | PERIOD_NUM | — | ✅ |
| 74 | LaborDistRunsAllPEOPeriodType | PERIOD_TYPE | — | ✅ |
| 75 | LaborDistRunsAllPEOPoolPercent | POOL_PERCENT | — | ✅ |
| 76 | LaborDistRunsAllPEOPriorOffsetAmount | PRIOR_OFFSET_AMOUNT | — | ✅ |
| 77 | LaborDistRunsAllPEOPriorRequestId | PRIOR_REQUEST_ID | — | ✅ |
| 78 | LaborDistRunsAllPEOProcessingEndDate | PROCESSING_END_DATE | — | ✅ |
| 79 | LaborDistRunsAllPEOProcessingStartDate | PROCESSING_START_DATE | — | ✅ |
| 80 | LaborDistRunsAllPEOQuarter | QUARTER | — | ✅ |
| 81 | LaborDistRunsAllPEOReleaseRequestDate | RELEASE_REQUEST_DATE | — | ✅ |
| 82 | LaborDistRunsAllPEOReleaseRequestId | RELEASE_REQUEST_ID | — | ✅ |
| 83 | LaborDistRunsAllPEORemnantAmount | REMNANT_AMOUNT | — | ✅ |
| 84 | LaborDistRunsAllPEOReversalDate | REVERSAL_DATE | — | ✅ |
| 85 | LaborDistRunsAllPEOReverseRequestId | REVERSE_REQUEST_ID | — | ✅ |
| 86 | LaborDistRunsAllPEORuleId | RULE_ID | — | ✅ |
| 87 | LaborDistRunsAllPEORunActionId | RUN_ACTION_ID | — | ✅ |
| 88 | LaborDistRunsAllPEORunId | RUN_ID | 🔑 | ✅ |
| 89 | LaborDistRunsAllPEORunPeriod | RUN_PERIOD | — | ✅ |
| 90 | LaborDistRunsAllPEORunStatus | RUN_STATUS | — | ✅ |
| 91 | LaborDistRunsAllPEOSourceAmountType | SOURCE_AMOUNT_TYPE | — | ✅ |
| 92 | LaborDistRunsAllPEOSourceBalanceCategory | SOURCE_BALANCE_CATEGORY | — | ✅ |
| 93 | LaborDistRunsAllPEOSourceBalanceType | SOURCE_BALANCE_TYPE | — | ✅ |
| 94 | LaborDistRunsAllPEOSubRequestId | SUB_REQUEST_ID | — | ✅ |
| 95 | LaborDistRunsAllPEOTargetCostType | TARGET_COST_TYPE | — | ✅ |
| 96 | LaborDistRunsAllPEOTargetExpGroupId | TARGET_EXP_GROUP_ID | — | ✅ |
| 97 | LaborDistRunsAllPEOTargetExpOrgId | TARGET_EXP_ORG_ID | — | ✅ |
| 98 | LaborDistRunsAllPEOTargetExpTypeClass | TARGET_EXP_TYPE_CLASS | — | ✅ |
| 99 | LaborDistRunsAllPEOTargetExpTypeId | TARGET_EXP_TYPE_ID | — | ✅ |
| 100 | LaborDistRunsAllPEOTotalAllocatedAmount | TOTAL_ALLOCATED_AMOUNT | — | ✅ |
| 101 | LaborDistRunsAllPEOTotalOffsettedAmount | TOTAL_OFFSETTED_AMOUNT | — | ✅ |
| 102 | LaborDistRunsAllPEOTotalPoolAmount | TOTAL_POOL_AMOUNT | — | ✅ |
| 103 | LaborDistRunsAllPEOTotalPriorAllocAmount | TOTAL_PRIOR_ALLOC_AMOUNT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
