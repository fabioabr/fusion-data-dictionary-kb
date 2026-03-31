---
id: DOC-OTHER-PVO-ProjectUnprocessedCostTransactionPVO
doc_type: system-doc
title: "ProjectUnprocessedCostTransactionPVO — PVO Cross-Module"
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
  - ProjectUnprocessedCostTransactionPVO
  - projectunprocessedcosttransactionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectUnprocessedCostTransactionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Unprocessed Cost Transaction. Acessa as tabelas: CST_ALL_TXN_TYPES_V, FUN_ALL_BUSINESS_UNITS_V, HR_ORGANIZATION_V (+11).

**Caminho:** `FscmTopModelAM.PjcTransactionsAM.ProjectUnprocessedCostTransactionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 231 | 14 | 1 | 97 | 42% |

---

## 🔗 Tabelas Relacionadas

- [[cst_all_txn_types_v|CST_ALL_TXN_TYPES_V]] — 3 atributos (1 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 2 atributos
- [[hr_organization_v|HR_ORGANIZATION_V]] — 10 atributos (3 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 6 atributos (2 BICC)
- [[per_jobs_f_vl|PER_JOBS_F_VL]] — 4 atributos (2 BICC)
- [[pjc_exp_groups_all|PJC_EXP_GROUPS_ALL]] — 2 atributos (1 BICC)
- [[pjc_txn_xface_all|PJC_TXN_XFACE_ALL]] — 181 atributos (1 PKs, 82 BICC)
- [[pjf_exp_types_b|PJF_EXP_TYPES_B]] — 3 atributos
- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 9 atributos (1 BICC)
- [[pjf_rate_schedules_vl|PJF_RATE_SCHEDULES_VL]] — 2 atributos (1 BICC)
- [[pjf_txn_document_vl|PJF_TXN_DOCUMENT_VL]] — 2 atributos (1 BICC)
- [[pjf_txn_doc_entry_vl|PJF_TXN_DOC_ENTRY_VL]] — 2 atributos (1 BICC)
- [[pjf_txn_sources_vl|PJF_TXN_SOURCES_VL]] — 2 atributos (1 BICC)
- [[pjf_units_of_measure_v|PJF_UNITS_OF_MEASURE_V]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[cst_all_txn_types_v|CST_ALL_TXN_TYPES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BaseTxnSourceTypeId | BASE_TXN_SOURCE_TYPE_ID | — | — |
| 2 | BaseTxnTypeId | BASE_TXN_TYPE_ID | — | — |
| 3 | BaseTxnTypeName | BASE_TXN_TYPE_NAME | — | ✅ |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RecvrBusinessUnitPEOBusinessUnitId | BU_ID | — | — |
| 2 | RecvrBusinessUnitPEOName | BU_NAME | — | — |

### [[hr_organization_v|HR_ORGANIZATION_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationDPEOClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | OrganizationDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | OrganizationDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | OrganizationDPEOName | NAME | — | — |
| 5 | OrganizationDPEOOrganizationId | ORGANIZATION_ID | — | — |
| 6 | OverrideToOrganizationDPEOClassificationCode | CLASSIFICATION_CODE | — | — |
| 7 | OverrideToOrganizationDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | OverrideToOrganizationDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 9 | OverrideToOrganizationDPEOName | NAME | — | ✅ |
| 10 | OverrideToOrganizationDPEOOrganizationId | ORGANIZATION_ID | — | — |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentDPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 2 | AssignmentDPEOAssignmentName | ASSIGNMENT_NAME | — | ✅ |
| 3 | AssignmentDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | AssignmentDPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 5 | AssignmentDPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 6 | AssignmentDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |

### [[per_jobs_f_vl|PER_JOBS_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostJobDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | CostJobDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | CostJobDPEOJobId | JOB_ID | — | — |
| 4 | CostJobDPEOName | NAME | — | ✅ |

### [[pjc_exp_groups_all|PJC_EXP_GROUPS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectExpenditureGroupPEOExpGroupId | EXP_GROUP_ID | — | — |
| 2 | ProjectExpenditureGroupPEOUserBatchName | USER_BATCH_NAME | — | ✅ |

### [[pjc_txn_xface_all|PJC_TXN_XFACE_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistributionId | DISTRIBUTION_ID | — | ✅ |
| 2 | ProjectUnprocessedCostTxnPEOAccountingStatusCode | ACCOUNTING_STATUS_CODE | — | — |
| 3 | ProjectUnprocessedCostTxnPEOAccrualFlag | ACCRUAL_FLAG | — | ✅ |
| 4 | ProjectUnprocessedCostTxnPEOAccrueOnReceiptFlag | ACCRUE_ON_RECEIPT_FLAG | — | ✅ |
| 5 | ProjectUnprocessedCostTxnPEOAcctBurdenedCost | ACCT_BURDENED_COST | — | ✅ |
| 6 | ProjectUnprocessedCostTxnPEOAcctCurrencyCode | ACCT_CURRENCY_CODE | — | — |
| 7 | ProjectUnprocessedCostTxnPEOAcctEventId | ACCT_EVENT_ID | — | — |
| 8 | ProjectUnprocessedCostTxnPEOAcctExchangeRate | ACCT_EXCHANGE_RATE | — | ✅ |
| 9 | ProjectUnprocessedCostTxnPEOAcctExchangeRoundingLimit | ACCT_EXCHANGE_ROUNDING_LIMIT | — | ✅ |
| 10 | ProjectUnprocessedCostTxnPEOAcctRateDate | ACCT_RATE_DATE | — | ✅ |
| 11 | ProjectUnprocessedCostTxnPEOAcctRateDateType | ACCT_RATE_DATE_TYPE | — | ✅ |
| 12 | ProjectUnprocessedCostTxnPEOAcctRateType | ACCT_RATE_TYPE | — | ✅ |
| 13 | ProjectUnprocessedCostTxnPEOAcctRawCost | ACCT_RAW_COST | — | ✅ |
| 14 | ProjectUnprocessedCostTxnPEOAcctSourceCode | ACCT_SOURCE_CODE | — | — |
| 15 | ProjectUnprocessedCostTxnPEOAdjustedExpenditureItemId | ADJUSTED_EXPENDITURE_ITEM_ID | — | ✅ |
| 16 | ProjectUnprocessedCostTxnPEOAdjustedTxnInterfaceId | ADJUSTED_TXN_INTERFACE_ID | — | ✅ |
| 17 | ProjectUnprocessedCostTxnPEOAllowCcFlag | ALLOW_CC_FLAG | — | ✅ |
| 18 | ProjectUnprocessedCostTxnPEOBatchDescription | BATCH_DESCRIPTION | — | ✅ |
| 19 | ProjectUnprocessedCostTxnPEOBatchEndingDate | BATCH_ENDING_DATE | — | ✅ |
| 20 | ProjectUnprocessedCostTxnPEOBatchName | BATCH_NAME | — | ✅ |
| 21 | ProjectUnprocessedCostTxnPEOBillableFlag | BILLABLE_FLAG | — | ✅ |
| 22 | ProjectUnprocessedCostTxnPEOBudgetPeriodId | BUDGET_PERIOD_ID | — | — |
| 23 | ProjectUnprocessedCostTxnPEOBurdenCostCrCcid | BURDEN_COST_CR_CCID | — | — |
| 24 | ProjectUnprocessedCostTxnPEOBurdenCostDrCcid | BURDEN_COST_DR_CCID | — | — |
| 25 | ProjectUnprocessedCostTxnPEOBurdenSumDestRunId | BURDEN_SUM_DEST_RUN_ID | — | — |
| 26 | ProjectUnprocessedCostTxnPEOBurdenedCostCrCcid | BURDENED_COST_CR_CCID | — | — |
| 27 | ProjectUnprocessedCostTxnPEOBurdenedCostDrCcid | BURDENED_COST_DR_CCID | — | — |
| 28 | ProjectUnprocessedCostTxnPEOBurdenedCostRate | BURDENED_COST_RATE | — | ✅ |
| 29 | ProjectUnprocessedCostTxnPEOCalcIndirectCostFlag | CALC_INDIRECT_COST_FLAG | — | — |
| 30 | ProjectUnprocessedCostTxnPEOCalcRawCostFlag | CALC_RAW_COST_FLAG | — | — |
| 31 | ProjectUnprocessedCostTxnPEOCapitalizableFlag | CAPITALIZABLE_FLAG | — | ✅ |
| 32 | ProjectUnprocessedCostTxnPEOCdlLineNum | CDL_LINE_NUM | — | ✅ |
| 33 | ProjectUnprocessedCostTxnPEOCdlLineNumReversed | CDL_LINE_NUM_REVERSED | — | ✅ |
| 34 | ProjectUnprocessedCostTxnPEOCdlLineType | CDL_LINE_TYPE | — | ✅ |
| 35 | ProjectUnprocessedCostTxnPEOCdlParentLineNum | CDL_PARENT_LINE_NUM | — | ✅ |
| 36 | ProjectUnprocessedCostTxnPEOCommitmentControlFlag | COMMITMENT_CONTROL_FLAG | — | — |
| 37 | ProjectUnprocessedCostTxnPEOCommsNlTrackableFlag | COMMS_NL_TRACKABLE_FLAG | — | — |
| 38 | ProjectUnprocessedCostTxnPEOCompDetailsId | COMP_DETAILS_ID | — | — |
| 39 | ProjectUnprocessedCostTxnPEOContextCategory | CONTEXT_CATEGORY | — | — |
| 40 | ProjectUnprocessedCostTxnPEOContractId | CONTRACT_ID | — | — |
| 41 | ProjectUnprocessedCostTxnPEOConvertedFlag | CONVERTED_FLAG | — | ✅ |
| 42 | ProjectUnprocessedCostTxnPEOCostIndCompiledSetId | COST_IND_COMPILED_SET_ID | — | — |
| 43 | ProjectUnprocessedCostTxnPEOCostJobId | COST_JOB_ID | — | — |
| 44 | ProjectUnprocessedCostTxnPEOCostScheduleId | COST_SCHEDULE_ID | — | — |
| 45 | ProjectUnprocessedCostTxnPEOCostScheduleLineId | COST_SCHEDULE_LINE_ID | — | — |
| 46 | ProjectUnprocessedCostTxnPEOCreatedBy | CREATED_BY | — | ✅ |
| 47 | ProjectUnprocessedCostTxnPEOCreationDate | CREATION_DATE | — | ✅ |
| 48 | ProjectUnprocessedCostTxnPEODenomBurdenedCost | DENOM_BURDENED_COST | — | ✅ |
| 49 | ProjectUnprocessedCostTxnPEODenomCurrencyCode | DENOM_CURRENCY_CODE | — | — |
| 50 | ProjectUnprocessedCostTxnPEODenomRawCost | DENOM_RAW_COST | — | ✅ |
| 51 | ProjectUnprocessedCostTxnPEODerivationsFlag | DERIVATIONS_FLAG | — | — |
| 52 | ProjectUnprocessedCostTxnPEODocEntryId | DOC_ENTRY_ID | — | — |
| 53 | ProjectUnprocessedCostTxnPEODocEntryName | DOC_ENTRY_NAME | — | — |
| 54 | ProjectUnprocessedCostTxnPEODocumentDistributionType | DOCUMENT_DISTRIBUTION_TYPE | — | ✅ |
| 55 | ProjectUnprocessedCostTxnPEODocumentId | DOCUMENT_ID | — | — |
| 56 | ProjectUnprocessedCostTxnPEODocumentName | DOCUMENT_NAME | — | — |
| 57 | ProjectUnprocessedCostTxnPEODocumentType | DOCUMENT_TYPE | — | — |
| 58 | ProjectUnprocessedCostTxnPEOEiCreationFlag | EI_CREATION_FLAG | — | ✅ |
| 59 | ProjectUnprocessedCostTxnPEOErrorGroup | ERROR_GROUP | — | ✅ |
| 60 | ProjectUnprocessedCostTxnPEOExpGroupId | EXP_GROUP_ID | — | — |
| 61 | ProjectUnprocessedCostTxnPEOExpenditureComment | EXPENDITURE_COMMENT | — | ✅ |
| 62 | ProjectUnprocessedCostTxnPEOExpenditureEndingDate | EXPENDITURE_ENDING_DATE | — | ✅ |
| 63 | ProjectUnprocessedCostTxnPEOExpenditureItemDate | EXPENDITURE_ITEM_DATE | — | — |
| 64 | ProjectUnprocessedCostTxnPEOExpenditureItemId | EXPENDITURE_ITEM_ID | — | ✅ |
| 65 | ProjectUnprocessedCostTxnPEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 66 | ProjectUnprocessedCostTxnPEOGlDate | GL_DATE | — | — |
| 67 | ProjectUnprocessedCostTxnPEOHcmAssignmentId | HCM_ASSIGNMENT_ID | — | — |
| 68 | ProjectUnprocessedCostTxnPEOInterfaceId | INTERFACE_ID | — | — |
| 69 | ProjectUnprocessedCostTxnPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 70 | ProjectUnprocessedCostTxnPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 71 | ProjectUnprocessedCostTxnPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 72 | ProjectUnprocessedCostTxnPEOLaborCostMultiplierName | LABOR_COST_MULTIPLIER_NAME | — | ✅ |
| 73 | ProjectUnprocessedCostTxnPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 74 | ProjectUnprocessedCostTxnPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 75 | ProjectUnprocessedCostTxnPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 76 | ProjectUnprocessedCostTxnPEONetZeroAdjustmentFlag | NET_ZERO_ADJUSTMENT_FLAG | — | ✅ |
| 77 | ProjectUnprocessedCostTxnPEONonLaborResourceId | NON_LABOR_RESOURCE_ID | — | — |
| 78 | ProjectUnprocessedCostTxnPEONonLaborResourceOrgId | NON_LABOR_RESOURCE_ORG_ID | — | — |
| 79 | ProjectUnprocessedCostTxnPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 80 | ProjectUnprocessedCostTxnPEOOrderTypeLookupCode | ORDER_TYPE_LOOKUP_CODE | — | — |
| 81 | ProjectUnprocessedCostTxnPEOOrgId | ORG_ID | — | — |
| 82 | ProjectUnprocessedCostTxnPEOOrgLaborSchRuleId | ORG_LABOR_SCH_RULE_ID | — | — |
| 83 | ProjectUnprocessedCostTxnPEOOrganizationId | ORGANIZATION_ID | — | — |
| 84 | ProjectUnprocessedCostTxnPEOOrigExpTxnReference1 | ORIG_EXP_TXN_REFERENCE1 | — | ✅ |
| 85 | ProjectUnprocessedCostTxnPEOOrigExpTxnReference2 | ORIG_EXP_TXN_REFERENCE2 | — | ✅ |
| 86 | ProjectUnprocessedCostTxnPEOOrigExpTxnReference3 | ORIG_EXP_TXN_REFERENCE3 | — | ✅ |
| 87 | ProjectUnprocessedCostTxnPEOOrigHistoricalFlag | ORIG_HISTORICAL_FLAG | — | — |
| 88 | ProjectUnprocessedCostTxnPEOOrigTransactionReference | ORIG_TRANSACTION_REFERENCE | — | ✅ |
| 89 | ProjectUnprocessedCostTxnPEOOrigUserExpTxnReference | ORIG_USER_EXP_TXN_REFERENCE | — | ✅ |
| 90 | ProjectUnprocessedCostTxnPEOOriginalDistId | ORIGINAL_DIST_ID | — | ✅ |
| 91 | ProjectUnprocessedCostTxnPEOOriginalHeaderId | ORIGINAL_HEADER_ID | — | ✅ |
| 92 | ProjectUnprocessedCostTxnPEOOriginalLineNumber | ORIGINAL_LINE_NUMBER | — | ✅ |
| 93 | ProjectUnprocessedCostTxnPEOOverrideToOrganizationId | OVERRIDE_TO_ORGANIZATION_ID | — | — |
| 94 | ProjectUnprocessedCostTxnPEOParentDistId | PARENT_DIST_ID | — | ✅ |
| 95 | ProjectUnprocessedCostTxnPEOParentHeaderId | PARENT_HEADER_ID | — | ✅ |
| 96 | ProjectUnprocessedCostTxnPEOParentLineNumber | PARENT_LINE_NUMBER | — | ✅ |
| 97 | ProjectUnprocessedCostTxnPEOParentReversalId | PARENT_REVERSAL_ID | — | ✅ |
| 98 | ProjectUnprocessedCostTxnPEOPersonId | PERSON_ID | — | — |
| 99 | ProjectUnprocessedCostTxnPEOPersonJobId | PERSON_JOB_ID | — | — |
| 100 | ProjectUnprocessedCostTxnPEOPersonType | PERSON_TYPE | — | ✅ |
| 101 | ProjectUnprocessedCostTxnPEOProcessGroupId | PROCESS_GROUP_ID | — | — |
| 102 | ProjectUnprocessedCostTxnPEOProjectBurdenedCost | PROJECT_BURDENED_COST | — | ✅ |
| 103 | ProjectUnprocessedCostTxnPEOProjectCurrencyCode | PROJECT_CURRENCY_CODE | — | — |
| 104 | ProjectUnprocessedCostTxnPEOProjectExchangeRate | PROJECT_EXCHANGE_RATE | — | ✅ |
| 105 | ProjectUnprocessedCostTxnPEOProjectId | PROJECT_ID | — | — |
| 106 | ProjectUnprocessedCostTxnPEOProjectRateDate | PROJECT_RATE_DATE | — | ✅ |
| 107 | ProjectUnprocessedCostTxnPEOProjectRateDateType | PROJECT_RATE_DATE_TYPE | — | ✅ |
| 108 | ProjectUnprocessedCostTxnPEOProjectRateType | PROJECT_RATE_TYPE | — | ✅ |
| 109 | ProjectUnprocessedCostTxnPEOProjectRawCost | PROJECT_RAW_COST | — | ✅ |
| 110 | ProjectUnprocessedCostTxnPEOProjectRoleId | PROJECT_ROLE_ID | — | — |
| 111 | ProjectUnprocessedCostTxnPEOProjectUnitId | PROJECT_UNIT_ID | — | — |
| 112 | ProjectUnprocessedCostTxnPEOProjfuncBurdenedCost | PROJFUNC_BURDENED_COST | — | ✅ |
| 113 | ProjectUnprocessedCostTxnPEOProjfuncCostExchangeRate | PROJFUNC_COST_EXCHANGE_RATE | — | ✅ |
| 114 | ProjectUnprocessedCostTxnPEOProjfuncCostRateDate | PROJFUNC_COST_RATE_DATE | — | ✅ |
| 115 | ProjectUnprocessedCostTxnPEOProjfuncCostRateType | PROJFUNC_COST_RATE_TYPE | — | ✅ |
| 116 | ProjectUnprocessedCostTxnPEOProjfuncCurrencyCode | PROJFUNC_CURRENCY_CODE | — | — |
| 117 | ProjectUnprocessedCostTxnPEOProjfuncRateDateType | PROJFUNC_RATE_DATE_TYPE | — | ✅ |
| 118 | ProjectUnprocessedCostTxnPEOProjfuncRawCost | PROJFUNC_RAW_COST | — | ✅ |
| 119 | ProjectUnprocessedCostTxnPEOPrvdrAccrualDate | PRVDR_ACCRUAL_DATE | — | — |
| 120 | ProjectUnprocessedCostTxnPEOPrvdrGlPeriodName | PRVDR_GL_PERIOD_NAME | — | ✅ |
| 121 | ProjectUnprocessedCostTxnPEOPrvdrPaDate | PRVDR_PA_DATE | — | — |
| 122 | ProjectUnprocessedCostTxnPEOPrvdrPaPeriodName | PRVDR_PA_PERIOD_NAME | — | ✅ |
| 123 | ProjectUnprocessedCostTxnPEOQuantity | QUANTITY | — | ✅ |
| 124 | ProjectUnprocessedCostTxnPEORaiseAcctEventFlag | RAISE_ACCT_EVENT_FLAG | — | — |
| 125 | ProjectUnprocessedCostTxnPEORawCostCrCcid | RAW_COST_CR_CCID | — | — |
| 126 | ProjectUnprocessedCostTxnPEORawCostDrCcid | RAW_COST_DR_CCID | — | — |
| 127 | ProjectUnprocessedCostTxnPEORawCostRate | RAW_COST_RATE | — | ✅ |
| 128 | ProjectUnprocessedCostTxnPEORawLineNumReversed | RAW_LINE_NUM_REVERSED | — | ✅ |
| 129 | ProjectUnprocessedCostTxnPEOReceiptCurrencyAmount | RECEIPT_CURRENCY_AMOUNT | — | ✅ |
| 130 | ProjectUnprocessedCostTxnPEOReceiptCurrencyCode | RECEIPT_CURRENCY_CODE | — | ✅ |
| 131 | ProjectUnprocessedCostTxnPEOReceiptExchangeRate | RECEIPT_EXCHANGE_RATE | — | ✅ |
| 132 | ProjectUnprocessedCostTxnPEORecvrAccrualDate | RECVR_ACCRUAL_DATE | — | — |
| 133 | ProjectUnprocessedCostTxnPEORecvrGlDate | RECVR_GL_DATE | — | — |
| 134 | ProjectUnprocessedCostTxnPEORecvrGlPeriodName | RECVR_GL_PERIOD_NAME | — | — |
| 135 | ProjectUnprocessedCostTxnPEORecvrOrgId | RECVR_ORG_ID | — | — |
| 136 | ProjectUnprocessedCostTxnPEORecvrPaDate | RECVR_PA_DATE | — | — |
| 137 | ProjectUnprocessedCostTxnPEORecvrPaPeriodName | RECVR_PA_PERIOD_NAME | — | — |
| 138 | ProjectUnprocessedCostTxnPEORequestId | REQUEST_ID | — | ✅ |
| 139 | ProjectUnprocessedCostTxnPEOReservedAttribute1 | RESERVED_ATTRIBUTE1 | — | — |
| 140 | ProjectUnprocessedCostTxnPEOReservedAttribute10 | RESERVED_ATTRIBUTE10 | — | — |
| 141 | ProjectUnprocessedCostTxnPEOReservedAttribute2 | RESERVED_ATTRIBUTE2 | — | — |
| 142 | ProjectUnprocessedCostTxnPEOReservedAttribute3 | RESERVED_ATTRIBUTE3 | — | — |
| 143 | ProjectUnprocessedCostTxnPEOReservedAttribute4 | RESERVED_ATTRIBUTE4 | — | — |
| 144 | ProjectUnprocessedCostTxnPEOReservedAttribute5 | RESERVED_ATTRIBUTE5 | — | — |
| 145 | ProjectUnprocessedCostTxnPEOReservedAttribute6 | RESERVED_ATTRIBUTE6 | — | — |
| 146 | ProjectUnprocessedCostTxnPEOReservedAttribute7 | RESERVED_ATTRIBUTE7 | — | — |
| 147 | ProjectUnprocessedCostTxnPEOReservedAttribute8 | RESERVED_ATTRIBUTE8 | — | — |
| 148 | ProjectUnprocessedCostTxnPEOReservedAttribute9 | RESERVED_ATTRIBUTE9 | — | — |
| 149 | ProjectUnprocessedCostTxnPEOReversalFlag | REVERSAL_FLAG | — | ✅ |
| 150 | ProjectUnprocessedCostTxnPEOReversedOrigTxnReference | REVERSED_ORIG_TXN_REFERENCE | — | ✅ |
| 151 | ProjectUnprocessedCostTxnPEOScXferCode | SC_XFER_CODE | — | — |
| 152 | ProjectUnprocessedCostTxnPEOSiAssetsAdditionFlag | SI_ASSETS_ADDITION_FLAG | — | — |
| 153 | ProjectUnprocessedCostTxnPEOSourceExpItemId | SOURCE_EXP_ITEM_ID | — | ✅ |
| 154 | ProjectUnprocessedCostTxnPEOSrcSystemLinkageFunction | SRC_SYSTEM_LINKAGE_FUNCTION | — | ✅ |
| 155 | ProjectUnprocessedCostTxnPEOSystemLinkage | SYSTEM_LINKAGE | — | — |
| 156 | ProjectUnprocessedCostTxnPEOTaskId | TASK_ID | — | — |
| 157 | ProjectUnprocessedCostTxnPEOTiebackStatusCode | TIEBACK_STATUS_CODE | — | — |
| 158 | ProjectUnprocessedCostTxnPEOTransactionSourceCode | TRANSACTION_SOURCE_CODE | — | — |
| 159 | ProjectUnprocessedCostTxnPEOTransactionSourceId | TRANSACTION_SOURCE_ID | — | — |
| 160 | ProjectUnprocessedCostTxnPEOTransactionStatusCode | TRANSACTION_STATUS_CODE | — | ✅ |
| 161 | ProjectUnprocessedCostTxnPEOTransferredFromExpItemId | TRANSFERRED_FROM_EXP_ITEM_ID | — | — |
| 162 | ProjectUnprocessedCostTxnPEOTxnAccumHeaderId | TXN_ACCUM_HEADER_ID | — | — |
| 163 | ProjectUnprocessedCostTxnPEOTxnReviewComment | TXN_REVIEW_COMMENT | — | ✅ |
| 164 | ProjectUnprocessedCostTxnPEOUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 165 | ProjectUnprocessedCostTxnPEOUnmatchedNegativeTxnFlag | UNMATCHED_NEGATIVE_TXN_FLAG | — | ✅ |
| 166 | ProjectUnprocessedCostTxnPEOUserDefAttribute1 | USER_DEF_ATTRIBUTE1 | — | — |
| 167 | ProjectUnprocessedCostTxnPEOUserDefAttribute10 | USER_DEF_ATTRIBUTE10 | — | — |
| 168 | ProjectUnprocessedCostTxnPEOUserDefAttribute2 | USER_DEF_ATTRIBUTE2 | — | — |
| 169 | ProjectUnprocessedCostTxnPEOUserDefAttribute3 | USER_DEF_ATTRIBUTE3 | — | — |
| 170 | ProjectUnprocessedCostTxnPEOUserDefAttribute4 | USER_DEF_ATTRIBUTE4 | — | — |
| 171 | ProjectUnprocessedCostTxnPEOUserDefAttribute5 | USER_DEF_ATTRIBUTE5 | — | — |
| 172 | ProjectUnprocessedCostTxnPEOUserDefAttribute6 | USER_DEF_ATTRIBUTE6 | — | — |
| 173 | ProjectUnprocessedCostTxnPEOUserDefAttribute7 | USER_DEF_ATTRIBUTE7 | — | — |
| 174 | ProjectUnprocessedCostTxnPEOUserDefAttribute8 | USER_DEF_ATTRIBUTE8 | — | — |
| 175 | ProjectUnprocessedCostTxnPEOUserDefAttribute9 | USER_DEF_ATTRIBUTE9 | — | — |
| 176 | ProjectUnprocessedCostTxnPEOUserTransactionSource | USER_TRANSACTION_SOURCE | — | — |
| 177 | ProjectUnprocessedCostTxnPEOValidationsFlag | VALIDATIONS_FLAG | — | — |
| 178 | ProjectUnprocessedCostTxnPEOVendorId | VENDOR_ID | — | — |
| 179 | ProjectUnprocessedCostTxnPEOWorkTypeId | WORK_TYPE_ID | — | — |
| 180 | SourceTxnQuantity | SOURCE_TXN_QUANTITY | — | ✅ |
| 181 | TxnInterfaceId | TXN_INTERFACE_ID | 🔑 | ✅ |

### [[pjf_exp_types_b|PJF_EXP_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureTypeBasePEOExpenditureCategoryId | EXPENDITURE_CATEGORY_ID | — | — |
| 2 | ExpenditureTypeBasePEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 3 | ExpenditureTypeBasePEORevenueCategoryCode | REVENUE_CATEGORY_CODE | — | — |

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectBasePEOCarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 2 | ProjectBasePEOCreatedBy | CREATED_BY | — | — |
| 3 | ProjectBasePEOCreationDate | CREATION_DATE | — | — |
| 4 | ProjectBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ProjectBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ProjectBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ProjectBasePEOOrgId | ORG_ID | — | — |
| 8 | ProjectBasePEOProjectId | PROJECT_ID | — | — |
| 9 | ProjectBasePEOProjectUnitId | PROJECT_UNIT_ID | — | — |

### [[pjf_rate_schedules_vl|PJF_RATE_SCHEDULES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostSchedulePEORateScheduleId | RATE_SCHEDULE_ID | — | — |
| 2 | CostSchedulePEORateScheduleName | RATE_SCHEDULE_NAME | — | ✅ |

### [[pjf_txn_document_vl|PJF_TXN_DOCUMENT_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionDocumentPEODocumentId | DOCUMENT_ID | — | — |
| 2 | TransactionDocumentPEODocumentName | DOCUMENT_NAME | — | ✅ |

### [[pjf_txn_doc_entry_vl|PJF_TXN_DOC_ENTRY_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionDocEntryPEODocEntryId | DOC_ENTRY_ID | — | — |
| 2 | TransactionDocEntryPEODocEntryName | DOC_ENTRY_NAME | — | ✅ |

### [[pjf_txn_sources_vl|PJF_TXN_SOURCES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionSourcePEOTransactionSourceId | TRANSACTION_SOURCE_ID | — | — |
| 2 | TransactionSourcePEOUserTransactionSource | USER_TRANSACTION_SOURCE | — | ✅ |

### [[pjf_units_of_measure_v|PJF_UNITS_OF_MEASURE_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UnitOfMeasurePEODescription | DESCRIPTION | — | — |
| 2 | UnitOfMeasurePEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 3 | UnitOfMeasurePEOUomCode | UOM_CODE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
