---
id: DOC-OTHER-PVO-ProjectCostDistributionPVO
doc_type: system-doc
title: "ProjectCostDistributionPVO — PVO Cross-Module"
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
  - ProjectCostDistributionPVO
  - projectcostdistributionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectCostDistributionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Cost Distribution. Acessa as tabelas: CST_ALL_TXN_TYPES_V, FND_MESSAGES_VL, FUN_ALL_BUSINESS_UNITS_V (+25).

**Caminho:** `FscmTopModelAM.PjcTransactionsAM.ProjectCostDistributionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 430 | 28 | 2 | 210 | 49% |

---

## 🔗 Tabelas Relacionadas

- [[cst_all_txn_types_v|CST_ALL_TXN_TYPES_V]] — 3 atributos (1 BICC)
- [[fnd_messages_vl|FND_MESSAGES_VL]] — 3 atributos (1 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 2 atributos
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 20 atributos (5 BICC)
- [[hr_organization_v|HR_ORGANIZATION_V]] — 15 atributos (9 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 6 atributos (2 BICC)
- [[per_jobs_f_vl|PER_JOBS_F_VL]] — 10 atributos (4 BICC)
- [[pjc_capital_events|PJC_CAPITAL_EVENTS]] — 2 atributos (1 BICC)
- [[pjc_cost_dist_lines_all|PJC_COST_DIST_LINES_ALL]] — 82 atributos (2 PKs, 47 BICC)
- [[pjc_exp_comments|PJC_EXP_COMMENTS]] — 4 atributos (1 BICC)
- [[pjc_exp_groups_all|PJC_EXP_GROUPS_ALL]] — 3 atributos (1 BICC)
- [[pjc_exp_items_all|PJC_EXP_ITEMS_ALL]] — 224 atributos (114 BICC)
- [[pjf_exp_types_b|PJF_EXP_TYPES_B]] — 3 atributos
- [[pjf_non_labor_res_vl|PJF_NON_LABOR_RES_VL]] — 3 atributos (1 BICC)
- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 9 atributos (1 BICC)
- [[pjf_project_types_b|PJF_PROJECT_TYPES_B]] — 9 atributos (3 BICC)
- [[pjf_rate_schedules_vl|PJF_RATE_SCHEDULES_VL]] — 4 atributos (2 BICC)
- [[pjf_rbs_elements_vl|PJF_RBS_ELEMENTS_VL]] — 2 atributos
- [[pjf_rbs_element_names_vl|PJF_RBS_ELEMENT_NAMES_VL]] — 4 atributos (2 BICC)
- [[pjf_system_linkages_vl|PJF_SYSTEM_LINKAGES_VL]] — 4 atributos (4 BICC)
- [[pjf_txn_document_vl|PJF_TXN_DOCUMENT_VL]] — 3 atributos (2 BICC)
- [[pjf_txn_doc_entry_vl|PJF_TXN_DOC_ENTRY_VL]] — 3 atributos (2 BICC)
- [[pjf_txn_sources_vl|PJF_TXN_SOURCES_VL]] — 4 atributos (2 BICC)
- [[pjf_units_of_measure_v|PJF_UNITS_OF_MEASURE_V]] — 3 atributos (3 BICC)
- [[wis_equipment_instances|WIS_EQUIPMENT_INSTANCES]] — 1 atributos
- [[wis_labor_instances|WIS_LABOR_INSTANCES]] — 1 atributos
- [[wis_resources_vl|WIS_RESOURCES_VL]] — 1 atributos
- [[xle_entity_profiles|XLE_ENTITY_PROFILES]] — 2 atributos (2 BICC)

---

## ⚙️ Atributos

### [[cst_all_txn_types_v|CST_ALL_TXN_TYPES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BaseTxnSourceTypeId | BASE_TXN_SOURCE_TYPE_ID | — | — |
| 2 | BaseTxnTypeId | BASE_TXN_TYPE_ID | — | — |
| 3 | BaseTxnTypeName | BASE_TXN_TYPE_NAME | — | ✅ |

### [[fnd_messages_vl|FND_MESSAGES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MessagePEOApplicationId | APPLICATION_ID | — | — |
| 2 | MessagePEOMessageName | MESSAGE_NAME | — | ✅ |
| 3 | MessagePEOMessageText | MESSAGE_TEXT | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RecvrBusinessUnitPEOBusinessUnitId | BU_ID | — | — |
| 2 | RecvrBusinessUnitPEOName | BU_NAME | — | — |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureBUPEOBusinessUnitId | ORGANIZATION_ID | — | — |
| 2 | ExpenditureBUPEOCreatedBy | CREATED_BY | — | — |
| 3 | ExpenditureBUPEOCreationDate | CREATION_DATE | — | — |
| 4 | ExpenditureBUPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 5 | ExpenditureBUPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 6 | ExpenditureBUPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ExpenditureBUPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ExpenditureBUPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ExpenditureBUPEOOrgInformationId | ORG_INFORMATION_ID | — | — |
| 10 | ExpenditureBUPEOPrimaryLedgerId | ORG_INFORMATION3 | — | — |
| 11 | ProjectBUPEOBusinessUnitId | ORGANIZATION_ID | — | — |
| 12 | ProjectBUPEOCreatedBy | CREATED_BY | — | — |
| 13 | ProjectBUPEOCreationDate | CREATION_DATE | — | — |
| 14 | ProjectBUPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 15 | ProjectBUPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 16 | ProjectBUPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | ProjectBUPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | ProjectBUPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | ProjectBUPEOOrgInformationId | ORG_INFORMATION_ID | — | — |
| 20 | ProjectBUPEOPrimaryLedgerId | ORG_INFORMATION3 | — | ✅ |

### [[hr_organization_v|HR_ORGANIZATION_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CCPrvdrOrganizationDPEOClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | CCPrvdrOrganizationDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | CCPrvdrOrganizationDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | CCPrvdrOrganizationDPEOName | NAME | — | ✅ |
| 5 | CCPrvdrOrganizationDPEOOrganizationId | ORGANIZATION_ID | — | — |
| 6 | CCRecvrOrganizationDPEOClassificationCode | CLASSIFICATION_CODE | — | — |
| 7 | CCRecvrOrganizationDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | CCRecvrOrganizationDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 9 | CCRecvrOrganizationDPEOName | NAME | — | ✅ |
| 10 | CCRecvrOrganizationDPEOOrganizationId | ORGANIZATION_ID | — | — |
| 11 | OverrideToOrganizationDPEOClassificationCode | CLASSIFICATION_CODE | — | ✅ |
| 12 | OverrideToOrganizationDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 13 | OverrideToOrganizationDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 14 | OverrideToOrganizationDPEOName | NAME | — | ✅ |
| 15 | OverrideToOrganizationDPEOOrganizationId | ORGANIZATION_ID | — | ✅ |

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
| 5 | CostJobDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | TpJobDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | TpJobDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 8 | TpJobDPEOJobId | JOB_ID | — | — |
| 9 | TpJobDPEOName | NAME | — | ✅ |
| 10 | TpJobDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[pjc_capital_events|PJC_CAPITAL_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectCapitalEventPEOCapitalEventId | CAPITAL_EVENT_ID | — | — |
| 2 | ProjectCapitalEventPEOEventName | EVENT_NAME | — | ✅ |

### [[pjc_cost_dist_lines_all|PJC_COST_DIST_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureItemId | EXPENDITURE_ITEM_ID | 🔑 | ✅ |
| 2 | LineNum | LINE_NUM | 🔑 | ✅ |
| 3 | ProjectCostDistributionPEOAccountingStatusCode | ACCOUNTING_STATUS_CODE | — | — |
| 4 | ProjectCostDistributionPEOAcctBurdenedCost | ACCT_BURDENED_COST | — | ✅ |
| 5 | ProjectCostDistributionPEOAcctCurrencyCode | ACCT_CURRENCY_CODE | — | ✅ |
| 6 | ProjectCostDistributionPEOAcctEventId | ACCT_EVENT_ID | — | — |
| 7 | ProjectCostDistributionPEOAcctExchangeRate | ACCT_EXCHANGE_RATE | — | ✅ |
| 8 | ProjectCostDistributionPEOAcctRateDate | ACCT_RATE_DATE | — | ✅ |
| 9 | ProjectCostDistributionPEOAcctRateType | ACCT_RATE_TYPE | — | ✅ |
| 10 | ProjectCostDistributionPEOAcctRawCost | ACCT_RAW_COST | — | ✅ |
| 11 | ProjectCostDistributionPEOAcctSourceCode | ACCT_SOURCE_CODE | — | — |
| 12 | ProjectCostDistributionPEOAccumulatedFlag | ACCUMULATED_FLAG | — | — |
| 13 | ProjectCostDistributionPEOBillableFlag | BILLABLE_FLAG | — | ✅ |
| 14 | ProjectCostDistributionPEOBudgetPeriodId | BUDGET_PERIOD_ID | — | — |
| 15 | ProjectCostDistributionPEOBudgetaryControlValStatus | BUDGETARY_CONTROL_VAL_STATUS | — | — |
| 16 | ProjectCostDistributionPEOBurdenCostCrCcid | BURDEN_COST_CR_CCID | — | — |
| 17 | ProjectCostDistributionPEOBurdenCostDrCcid | BURDEN_COST_DR_CCID | — | — |
| 18 | ProjectCostDistributionPEOBurdenSumRejectionCode | BURDEN_SUM_REJECTION_CODE | — | — |
| 19 | ProjectCostDistributionPEOBurdenSumSourceRunId | BURDEN_SUM_SOURCE_RUN_ID | — | — |
| 20 | ProjectCostDistributionPEOBurdenedCostCrCcid | BURDENED_COST_CR_CCID | — | — |
| 21 | ProjectCostDistributionPEOBurdenedCostDrCcid | BURDENED_COST_DR_CCID | — | — |
| 22 | ProjectCostDistributionPEOCapitalizableFlag | CAPITALIZABLE_FLAG | — | ✅ |
| 23 | ProjectCostDistributionPEOCompDetailsId | COMP_DETAILS_ID | — | — |
| 24 | ProjectCostDistributionPEOCostScheduleId | COST_SCHEDULE_ID | — | — |
| 25 | ProjectCostDistributionPEOCostScheduleLineId | COST_SCHEDULE_LINE_ID | — | — |
| 26 | ProjectCostDistributionPEOCreatedBy | CREATED_BY | — | ✅ |
| 27 | ProjectCostDistributionPEOCreationDate | CREATION_DATE | — | ✅ |
| 28 | ProjectCostDistributionPEODenomBurdenedCost | DENOM_BURDENED_COST | — | ✅ |
| 29 | ProjectCostDistributionPEODenomCurrencyCode | DENOM_CURRENCY_CODE | — | ✅ |
| 30 | ProjectCostDistributionPEODenomRawCost | DENOM_RAW_COST | — | ✅ |
| 31 | ProjectCostDistributionPEOIndCompiledSetId | IND_COMPILED_SET_ID | — | — |
| 32 | ProjectCostDistributionPEOInterfaceId | INTERFACE_ID | — | — |
| 33 | ProjectCostDistributionPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 34 | ProjectCostDistributionPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 35 | ProjectCostDistributionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 36 | ProjectCostDistributionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 37 | ProjectCostDistributionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 38 | ProjectCostDistributionPEOLineNumReversed | LINE_NUM_REVERSED | — | ✅ |
| 39 | ProjectCostDistributionPEOLineType | LINE_TYPE | — | ✅ |
| 40 | ProjectCostDistributionPEONonLaborResourceId | NON_LABOR_RESOURCE_ID | — | — |
| 41 | ProjectCostDistributionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 42 | ProjectCostDistributionPEOOrgId | ORG_ID | — | ✅ |
| 43 | ProjectCostDistributionPEOOrgLaborSchRuleId | ORG_LABOR_SCH_RULE_ID | — | — |
| 44 | ProjectCostDistributionPEOOrigHistoricalFlag | ORIG_HISTORICAL_FLAG | — | — |
| 45 | ProjectCostDistributionPEOParentLineNum | PARENT_LINE_NUM | — | ✅ |
| 46 | ProjectCostDistributionPEOPjsSummaryId | PJS_SUMMARY_ID | — | — |
| 47 | ProjectCostDistributionPEOPrcGeneratedFlag | PRC_GENERATED_FLAG | — | — |
| 48 | ProjectCostDistributionPEOPrevIndCompiledSetId | PREV_IND_COMPILED_SET_ID | — | — |
| 49 | ProjectCostDistributionPEOProjectBurdenedCost | PROJECT_BURDENED_COST | — | ✅ |
| 50 | ProjectCostDistributionPEOProjectCurrencyCode | PROJECT_CURRENCY_CODE | — | ✅ |
| 51 | ProjectCostDistributionPEOProjectExchangeRate | PROJECT_EXCHANGE_RATE | — | ✅ |
| 52 | ProjectCostDistributionPEOProjectId | PROJECT_ID | — | ✅ |
| 53 | ProjectCostDistributionPEOProjectRateDate | PROJECT_RATE_DATE | — | ✅ |
| 54 | ProjectCostDistributionPEOProjectRateType | PROJECT_RATE_TYPE | — | ✅ |
| 55 | ProjectCostDistributionPEOProjectRawCost | PROJECT_RAW_COST | — | ✅ |
| 56 | ProjectCostDistributionPEOProjectUnitId | PROJECT_UNIT_ID | — | — |
| 57 | ProjectCostDistributionPEOProjfuncBurdenedCost | PROJFUNC_BURDENED_COST | — | ✅ |
| 58 | ProjectCostDistributionPEOProjfuncCostExchangeRate | PROJFUNC_COST_EXCHANGE_RATE | — | ✅ |
| 59 | ProjectCostDistributionPEOProjfuncCostRateDate | PROJFUNC_COST_RATE_DATE | — | ✅ |
| 60 | ProjectCostDistributionPEOProjfuncCostRateType | PROJFUNC_COST_RATE_TYPE | — | ✅ |
| 61 | ProjectCostDistributionPEOProjfuncCurrencyCode | PROJFUNC_CURRENCY_CODE | — | ✅ |
| 62 | ProjectCostDistributionPEOProjfuncRawCost | PROJFUNC_RAW_COST | — | ✅ |
| 63 | ProjectCostDistributionPEOPrvdrGlDate | PRVDR_GL_DATE | — | ✅ |
| 64 | ProjectCostDistributionPEOPrvdrGlPeriodName | PRVDR_GL_PERIOD_NAME | — | — |
| 65 | ProjectCostDistributionPEOPrvdrPaDate | PRVDR_PA_DATE | — | ✅ |
| 66 | ProjectCostDistributionPEOPrvdrPaPeriodName | PRVDR_PA_PERIOD_NAME | — | — |
| 67 | ProjectCostDistributionPEOQuantity | QUANTITY | — | ✅ |
| 68 | ProjectCostDistributionPEORawCostCrCcid | RAW_COST_CR_CCID | — | — |
| 69 | ProjectCostDistributionPEORawCostDrCcid | RAW_COST_DR_CCID | — | — |
| 70 | ProjectCostDistributionPEORawLineNumReversed | RAW_LINE_NUM_REVERSED | — | ✅ |
| 71 | ProjectCostDistributionPEORecvrGlDate | RECVR_GL_DATE | — | ✅ |
| 72 | ProjectCostDistributionPEORecvrGlPeriodName | RECVR_GL_PERIOD_NAME | — | — |
| 73 | ProjectCostDistributionPEORecvrPaDate | RECVR_PA_DATE | — | ✅ |
| 74 | ProjectCostDistributionPEORecvrPaPeriodName | RECVR_PA_PERIOD_NAME | — | — |
| 75 | ProjectCostDistributionPEORequestId | REQUEST_ID | — | — |
| 76 | ProjectCostDistributionPEOReversedFlag | REVERSED_FLAG | — | ✅ |
| 77 | ProjectCostDistributionPEOSiAssetsAdditionFlag | SI_ASSETS_ADDITION_FLAG | — | ✅ |
| 78 | ProjectCostDistributionPEOTaskId | TASK_ID | — | ✅ |
| 79 | ProjectCostDistributionPEOTransferRejectionReason | TRANSFER_REJECTION_REASON | — | ✅ |
| 80 | ProjectCostDistributionPEOTransferStatusCode | TRANSFER_STATUS_CODE | — | ✅ |
| 81 | ProjectCostDistributionPEOTxnAccumHeaderId | TXN_ACCUM_HEADER_ID | — | — |
| 82 | ProjectCostDistributionPEOWorkTypeId | WORK_TYPE_ID | — | ✅ |

### [[pjc_exp_comments|PJC_EXP_COMMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectExpenditureCommentsPEOExpenditureComment | EXPENDITURE_COMMENT | — | ✅ |
| 2 | ProjectExpenditureCommentsPEOExpenditureItemId | EXPENDITURE_ITEM_ID | — | — |
| 3 | ProjectExpenditureCommentsPEOLineNumber | LINE_NUMBER | — | — |
| 4 | ProjectExpenditureCommentsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[pjc_exp_groups_all|PJC_EXP_GROUPS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectExpenditureGroupPEOExpGroupId | EXP_GROUP_ID | — | — |
| 2 | ProjectExpenditureGroupPEOExpenditureGroup | EXPENDITURE_GROUP | — | ✅ |
| 3 | ProjectExpenditureGroupPEOUserBatchName | USER_BATCH_NAME | — | — |

### [[pjc_exp_items_all|PJC_EXP_ITEMS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistributionId | DISTRIBUTION_ID | — | ✅ |
| 2 | ExpenditureItemPEOAcctBurdenedCost | ACCT_BURDENED_COST | — | — |
| 3 | ExpenditureItemPEOAcctCurrencyCode | ACCT_CURRENCY_CODE | — | ✅ |
| 4 | ExpenditureItemPEOAcctExchangeRate | ACCT_EXCHANGE_RATE | — | ✅ |
| 5 | ExpenditureItemPEOAcctExchangeRoundingLimit | ACCT_EXCHANGE_ROUNDING_LIMIT | — | ✅ |
| 6 | ExpenditureItemPEOAcctRateDate | ACCT_RATE_DATE | — | ✅ |
| 7 | ExpenditureItemPEOAcctRateDateType | ACCT_RATE_DATE_TYPE | — | ✅ |
| 8 | ExpenditureItemPEOAcctRateType | ACCT_RATE_TYPE | — | ✅ |
| 9 | ExpenditureItemPEOAcctRawCost | ACCT_RAW_COST | — | — |
| 10 | ExpenditureItemPEOAcctTpExchangeRate | ACCT_TP_EXCHANGE_RATE | — | ✅ |
| 11 | ExpenditureItemPEOAcctTpRateDate | ACCT_TP_RATE_DATE | — | ✅ |
| 12 | ExpenditureItemPEOAcctTpRateType | ACCT_TP_RATE_TYPE | — | ✅ |
| 13 | ExpenditureItemPEOAcctTransferPrice | ACCT_TRANSFER_PRICE | — | ✅ |
| 14 | ExpenditureItemPEOAdjustedExpenditureItemId | ADJUSTED_EXPENDITURE_ITEM_ID | — | ✅ |
| 15 | ExpenditureItemPEOAdjustmentStatus | ADJUSTMENT_STATUS | — | ✅ |
| 16 | ExpenditureItemPEOAdjustmentType | ADJUSTMENT_TYPE | — | ✅ |
| 17 | ExpenditureItemPEOBillByCostCode | BILL_BY_COST_CODE | — | — |
| 18 | ExpenditureItemPEOBillHoldFlag | BILL_HOLD_FLAG | — | ✅ |
| 19 | ExpenditureItemPEOBillTransCurrencyCode | BILL_TRANS_CURRENCY_CODE | — | — |
| 20 | ExpenditureItemPEOBillableFlag | BILLABLE_FLAG | — | ✅ |
| 21 | ExpenditureItemPEOBurdenCostRate | BURDEN_COST_RATE | — | ✅ |
| 22 | ExpenditureItemPEOBurdenSumDestRunId | BURDEN_SUM_DEST_RUN_ID | — | — |
| 23 | ExpenditureItemPEOCapitalEventId | CAPITAL_EVENT_ID | — | — |
| 24 | ExpenditureItemPEOCapitalizableFlag | CAPITALIZABLE_FLAG | — | ✅ |
| 25 | ExpenditureItemPEOCapitalizationDistFlag | CAPITALIZATION_DIST_FLAG | — | ✅ |
| 26 | ExpenditureItemPEOCcBlDistributedCode | CC_BL_DISTRIBUTED_CODE | — | ✅ |
| 27 | ExpenditureItemPEOCcCrossChargeCode | CC_CROSS_CHARGE_CODE | — | ✅ |
| 28 | ExpenditureItemPEOCcCrossChargeType | CC_CROSS_CHARGE_TYPE | — | ✅ |
| 29 | ExpenditureItemPEOCcMarkupBaseCode | CC_MARKUP_BASE_CODE | — | ✅ |
| 30 | ExpenditureItemPEOCcProcessedFlag | CC_PROCESSED_FLAG | — | — |
| 31 | ExpenditureItemPEOCcPrvdrCostReclassCode | CC_PRVDR_COST_RECLASS_CODE | — | — |
| 32 | ExpenditureItemPEOCcPrvdrOrganizationId | CC_PRVDR_ORGANIZATION_ID | — | — |
| 33 | ExpenditureItemPEOCcRecvrOrganizationId | CC_RECVR_ORGANIZATION_ID | — | — |
| 34 | ExpenditureItemPEOCcRejectionCode | CC_REJECTION_CODE | — | — |
| 35 | ExpenditureItemPEOCmrAccountingEventId | CMR_ACCOUNTING_EVENT_ID | — | — |
| 36 | ExpenditureItemPEOCmrAdjutmentFlag | CMR_EXP_ADJUSTMENT_FLAG | — | — |
| 37 | ExpenditureItemPEOCmrEventCostId | CMR_EVENT_COST_ID | — | — |
| 38 | ExpenditureItemPEOCmrTransactionTypeCode | CMR_TRANSACTION_TYPE_CODE | — | — |
| 39 | ExpenditureItemPEOContextCategory | CONTEXT_CATEGORY | — | — |
| 40 | ExpenditureItemPEOContractId | CONTRACT_ID | — | ✅ |
| 41 | ExpenditureItemPEOConvertedFlag | CONVERTED_FLAG | — | ✅ |
| 42 | ExpenditureItemPEOCostAllocationKeyflexId | COST_ALLOCATION_KEYFLEX_ID | — | — |
| 43 | ExpenditureItemPEOCostDistWarningCode | COST_DIST_WARNING_CODE | — | — |
| 44 | ExpenditureItemPEOCostId | COST_ID | — | — |
| 45 | ExpenditureItemPEOCostIndCompiledSetId | COST_IND_COMPILED_SET_ID | — | — |
| 46 | ExpenditureItemPEOCostJobId | COST_JOB_ID | — | ✅ |
| 47 | ExpenditureItemPEOCostScheduleId | COST_SCHEDULE_ID | — | — |
| 48 | ExpenditureItemPEOCostScheduleLineId | COST_SCHEDULE_LINE_ID | — | — |
| 49 | ExpenditureItemPEOCreatedBy | CREATED_BY | — | ✅ |
| 50 | ExpenditureItemPEOCreationDate | CREATION_DATE | — | ✅ |
| 51 | ExpenditureItemPEODenomBurdenedCost | DENOM_BURDENED_COST | — | — |
| 52 | ExpenditureItemPEODenomCurrencyCode | DENOM_CURRENCY_CODE | — | ✅ |
| 53 | ExpenditureItemPEODenomRawCost | DENOM_RAW_COST | — | — |
| 54 | ExpenditureItemPEODenomTpCurrencyCode | DENOM_TP_CURRENCY_CODE | — | — |
| 55 | ExpenditureItemPEODenomTransferPrice | DENOM_TRANSFER_PRICE | — | ✅ |
| 56 | ExpenditureItemPEODocEntryId | DOC_ENTRY_ID | — | ✅ |
| 57 | ExpenditureItemPEODocRefId1 | DOC_REF_ID1 | — | ✅ |
| 58 | ExpenditureItemPEODocRefId10 | DOC_REF_ID10 | — | — |
| 59 | ExpenditureItemPEODocRefId2 | DOC_REF_ID2 | — | ✅ |
| 60 | ExpenditureItemPEODocRefId3 | DOC_REF_ID3 | — | — |
| 61 | ExpenditureItemPEODocRefId4 | DOC_REF_ID4 | — | — |
| 62 | ExpenditureItemPEODocRefId5 | DOC_REF_ID5 | — | — |
| 63 | ExpenditureItemPEODocRefId6 | DOC_REF_ID6 | — | — |
| 64 | ExpenditureItemPEODocRefId7 | DOC_REF_ID7 | — | — |
| 65 | ExpenditureItemPEODocRefId8 | DOC_REF_ID8 | — | — |
| 66 | ExpenditureItemPEODocRefId9 | DOC_REF_ID9 | — | — |
| 67 | ExpenditureItemPEODocumentDistributionType | DOCUMENT_DISTRIBUTION_TYPE | — | — |
| 68 | ExpenditureItemPEODocumentId | DOCUMENT_ID | — | ✅ |
| 69 | ExpenditureItemPEODocumentType | DOCUMENT_TYPE | — | — |
| 70 | ExpenditureItemPEOExpGroupId | EXP_GROUP_ID | — | — |
| 71 | ExpenditureItemPEOExpenditureEndingDate | EXPENDITURE_ENDING_DATE | — | ✅ |
| 72 | ExpenditureItemPEOExpenditureItemDate | EXPENDITURE_ITEM_DATE | — | ✅ |
| 73 | ExpenditureItemPEOExpenditureItemId | EXPENDITURE_ITEM_ID | — | ✅ |
| 74 | ExpenditureItemPEOExpenditureOrganizationId | EXPENDITURE_ORGANIZATION_ID | — | ✅ |
| 75 | ExpenditureItemPEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | ✅ |
| 76 | ExpenditureItemPEOExtOvrdBillRate | EXT_OVRD_BILL_RATE | — | ✅ |
| 77 | ExpenditureItemPEOExtOvrdBillRateCurrCode | EXT_OVRD_BILL_RATE_CURR_CODE | — | ✅ |
| 78 | ExpenditureItemPEOExtOvrdBillRateSourceName | EXT_OVRD_BILL_RATE_SOURCE_NAME | — | ✅ |
| 79 | ExpenditureItemPEOExtOvrdBillRateSourceRef | EXT_OVRD_BILL_RATE_SOURCE_REF | — | ✅ |
| 80 | ExpenditureItemPEOHcmAssignmentId | HCM_ASSIGNMENT_ID | — | — |
| 81 | ExpenditureItemPEOHistoricalFlag | HISTORICAL_FLAG | — | — |
| 82 | ExpenditureItemPEOIcBillByCostCode | IC_BILL_BY_COST_CODE | — | ✅ |
| 83 | ExpenditureItemPEOIcBillHoldFlag | IC_BILL_HOLD_FLAG | — | ✅ |
| 84 | ExpenditureItemPEOIcBillableFlag | IC_BILLABLE_FLAG | — | ✅ |
| 85 | ExpenditureItemPEOIcInvoicedFlag | IC_INVOICED_FLAG | — | ✅ |
| 86 | ExpenditureItemPEOIcInvoicedPercentage | IC_INVOICED_PERCENTAGE | — | ✅ |
| 87 | ExpenditureItemPEOIcLedgerCurrInvAmt | IC_LEDGER_CURR_INV_AMT | — | — |
| 88 | ExpenditureItemPEOIcLedgerCurrRevAmt | IC_LEDGER_CURR_REV_AMT | — | — |
| 89 | ExpenditureItemPEOIcOvrdBillRate | IC_OVRD_BILL_RATE | — | ✅ |
| 90 | ExpenditureItemPEOIcOvrdBillRateCurrCode | IC_OVRD_BILL_RATE_CURR_CODE | — | ✅ |
| 91 | ExpenditureItemPEOIcOvrdBillRateSourceName | IC_OVRD_BILL_RATE_SOURCE_NAME | — | ✅ |
| 92 | ExpenditureItemPEOIcOvrdBillRateSourceRef | IC_OVRD_BILL_RATE_SOURCE_REF | — | ✅ |
| 93 | ExpenditureItemPEOIcProjectCurrInvAmt | IC_PROJECT_CURR_INV_AMT | — | — |
| 94 | ExpenditureItemPEOIcProjectCurrRevAmt | IC_PROJECT_CURR_REV_AMT | — | — |
| 95 | ExpenditureItemPEOIcRbsElementId | IC_RBS_ELEMENT_ID | — | — |
| 96 | ExpenditureItemPEOIcRevRecogPercentage | IC_REV_RECOG_PERCENTAGE | — | ✅ |
| 97 | ExpenditureItemPEOIcRevenueHoldFlag | IC_REVENUE_HOLD_FLAG | — | ✅ |
| 98 | ExpenditureItemPEOIcRevenueRecognizedFlag | IC_REVENUE_RECOGNIZED_FLAG | — | ✅ |
| 99 | ExpenditureItemPEOIcTpAmtTypeCode | IC_TP_AMT_TYPE_CODE | — | ✅ |
| 100 | ExpenditureItemPEOIcTpBaseCode | IC_TP_BASE_CODE | — | ✅ |
| 101 | ExpenditureItemPEOIncurredByOrganizationId | INCURRED_BY_ORGANIZATION_ID | — | ✅ |
| 102 | ExpenditureItemPEOIncurredByPersonId | INCURRED_BY_PERSON_ID | — | ✅ |
| 103 | ExpenditureItemPEOInvExcludeFlag | INV_EXCLUDE_FLAG | — | ✅ |
| 104 | ExpenditureItemPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 105 | ExpenditureItemPEOInvoiceExceptionFlag | INVOICE_EXCEPTION_FLAG | — | ✅ |
| 106 | ExpenditureItemPEOInvoicedFlag | INVOICED_FLAG | — | ✅ |
| 107 | ExpenditureItemPEOInvoicedPercentage | INVOICED_PERCENTAGE | — | ✅ |
| 108 | ExpenditureItemPEOLaborCostMultiplierName | LABOR_COST_MULTIPLIER_NAME | — | ✅ |
| 109 | ExpenditureItemPEOLaborDistributionTransactionReference | LD_ORIG_TRANSACTION_REFERENCE | — | — |
| 110 | ExpenditureItemPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 111 | ExpenditureItemPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 112 | ExpenditureItemPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 113 | ExpenditureItemPEOLedgerCurrInvAmt | LEDGER_CURR_INV_AMT | — | — |
| 114 | ExpenditureItemPEOLedgerCurrRevAmt | LEDGER_CURR_REV_AMT | — | — |
| 115 | ExpenditureItemPEOManualFlag | MANUAL_FLAG | — | — |
| 116 | ExpenditureItemPEONetZeroAdjustmentFlag | NET_ZERO_ADJUSTMENT_FLAG | — | ✅ |
| 117 | ExpenditureItemPEONonLaborResourceId | NON_LABOR_RESOURCE_ID | — | ✅ |
| 118 | ExpenditureItemPEONonLaborResourceOrgId | NON_LABOR_RESOURCE_ORG_ID | — | — |
| 119 | ExpenditureItemPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 120 | ExpenditureItemPEOOrgId | ORG_ID | — | — |
| 121 | ExpenditureItemPEOOrigTransactionReference | ORIG_TRANSACTION_REFERENCE | — | ✅ |
| 122 | ExpenditureItemPEOOriginalDistId | ORIGINAL_DIST_ID | — | ✅ |
| 123 | ExpenditureItemPEOOriginalDistributionId2 | ORIGINAL_DIST_ID2 | — | — |
| 124 | ExpenditureItemPEOOriginalHeaderId | ORIGINAL_HEADER_ID | — | ✅ |
| 125 | ExpenditureItemPEOOriginalLineNumber | ORIGINAL_LINE_NUMBER | — | ✅ |
| 126 | ExpenditureItemPEOOverrideToOrganizationId | OVERRIDE_TO_ORGANIZATION_ID | — | ✅ |
| 127 | ExpenditureItemPEOParentDistId | PARENT_DIST_ID | — | ✅ |
| 128 | ExpenditureItemPEOParentHeaderId | PARENT_HEADER_ID | — | ✅ |
| 129 | ExpenditureItemPEOParentLineNumber | PARENT_LINE_NUMBER | — | ✅ |
| 130 | ExpenditureItemPEOPeriodAccrualFlag | PERIOD_ACCRUAL_FLAG | — | ✅ |
| 131 | ExpenditureItemPEOPersonJobId | PERSON_JOB_ID | — | ✅ |
| 132 | ExpenditureItemPEOPersonType | PERSON_TYPE | — | ✅ |
| 133 | ExpenditureItemPEOProjacctTransferPrice | PROJACCT_TRANSFER_PRICE | — | — |
| 134 | ExpenditureItemPEOProjectBurdenedCost | PROJECT_BURDENED_COST | — | — |
| 135 | ExpenditureItemPEOProjectCurrInvAmt | PROJECT_CURR_INV_AMT | — | — |
| 136 | ExpenditureItemPEOProjectCurrRevAmt | PROJECT_CURR_REV_AMT | — | — |
| 137 | ExpenditureItemPEOProjectCurrencyCode | PROJECT_CURRENCY_CODE | — | — |
| 138 | ExpenditureItemPEOProjectExchangeRate | PROJECT_EXCHANGE_RATE | — | ✅ |
| 139 | ExpenditureItemPEOProjectId | PROJECT_ID | — | — |
| 140 | ExpenditureItemPEOProjectRateDate | PROJECT_RATE_DATE | — | ✅ |
| 141 | ExpenditureItemPEOProjectRateDateType | PROJECT_RATE_DATE_TYPE | — | ✅ |
| 142 | ExpenditureItemPEOProjectRateType | PROJECT_RATE_TYPE | — | ✅ |
| 143 | ExpenditureItemPEOProjectRawCost | PROJECT_RAW_COST | — | — |
| 144 | ExpenditureItemPEOProjectRoleId | PROJECT_ROLE_ID | — | — |
| 145 | ExpenditureItemPEOProjectTpExchangeRate | PROJECT_TP_EXCHANGE_RATE | — | ✅ |
| 146 | ExpenditureItemPEOProjectTpRateDate | PROJECT_TP_RATE_DATE | — | ✅ |
| 147 | ExpenditureItemPEOProjectTpRateType | PROJECT_TP_RATE_TYPE | — | ✅ |
| 148 | ExpenditureItemPEOProjectTransferPrice | PROJECT_TRANSFER_PRICE | — | — |
| 149 | ExpenditureItemPEOProjectUnitId | PROJECT_UNIT_ID | — | — |
| 150 | ExpenditureItemPEOProjfuncBurdenedCost | PROJFUNC_BURDENED_COST | — | — |
| 151 | ExpenditureItemPEOProjfuncCostExchangeRate | PROJFUNC_COST_EXCHANGE_RATE | — | ✅ |
| 152 | ExpenditureItemPEOProjfuncCostRateDate | PROJFUNC_COST_RATE_DATE | — | ✅ |
| 153 | ExpenditureItemPEOProjfuncCostRateType | PROJFUNC_COST_RATE_TYPE | — | ✅ |
| 154 | ExpenditureItemPEOProjfuncCurrencyCode | PROJFUNC_CURRENCY_CODE | — | — |
| 155 | ExpenditureItemPEOProjfuncRateDateType | PROJFUNC_RATE_DATE_TYPE | — | ✅ |
| 156 | ExpenditureItemPEOProjfuncRawCost | PROJFUNC_RAW_COST | — | — |
| 157 | ExpenditureItemPEOProjfuncTpExchangeRate | PROJFUNC_TP_EXCHANGE_RATE | — | — |
| 158 | ExpenditureItemPEOProjfuncTpRateDate | PROJFUNC_TP_RATE_DATE | — | — |
| 159 | ExpenditureItemPEOProjfuncTpRateType | PROJFUNC_TP_RATE_TYPE | — | — |
| 160 | ExpenditureItemPEOProjfuncTransferPrice | PROJFUNC_TRANSFER_PRICE | — | ✅ |
| 161 | ExpenditureItemPEOPrvdrAccrualDate | PRVDR_ACCRUAL_DATE | — | ✅ |
| 162 | ExpenditureItemPEOPrvdrLegalEntityId | PRVDR_LEGAL_ENTITY_ID | — | — |
| 163 | ExpenditureItemPEOQuantity | QUANTITY | — | — |
| 164 | ExpenditureItemPEORawCostRate | RAW_COST_RATE | — | ✅ |
| 165 | ExpenditureItemPEORbsElementId | RBS_ELEMENT_ID | — | — |
| 166 | ExpenditureItemPEOReceiptCurrencyAmount | RECEIPT_CURRENCY_AMOUNT | — | — |
| 167 | ExpenditureItemPEOReceiptCurrencyCode | RECEIPT_CURRENCY_CODE | — | — |
| 168 | ExpenditureItemPEOReceiptExchangeRate | RECEIPT_EXCHANGE_RATE | — | — |
| 169 | ExpenditureItemPEORecvrAccrualDate | RECVR_ACCRUAL_DATE | — | ✅ |
| 170 | ExpenditureItemPEORecvrOrgId | RECVR_ORG_ID | — | — |
| 171 | ExpenditureItemPEOReferenceId1 | REFERENCE_ID1 | — | ✅ |
| 172 | ExpenditureItemPEOReferenceId10 | REFERENCE_ID10 | — | — |
| 173 | ExpenditureItemPEOReferenceId2 | REFERENCE_ID2 | — | — |
| 174 | ExpenditureItemPEOReferenceId3 | REFERENCE_ID3 | — | — |
| 175 | ExpenditureItemPEOReferenceId4 | REFERENCE_ID4 | — | — |
| 176 | ExpenditureItemPEOReferenceId5 | REFERENCE_ID5 | — | — |
| 177 | ExpenditureItemPEOReferenceId6 | REFERENCE_ID6 | — | — |
| 178 | ExpenditureItemPEOReferenceId7 | REFERENCE_ID7 | — | — |
| 179 | ExpenditureItemPEOReferenceId8 | REFERENCE_ID8 | — | — |
| 180 | ExpenditureItemPEOReferenceId9 | REFERENCE_ID9 | — | — |
| 181 | ExpenditureItemPEOReservedAttribute1 | RESERVED_ATTRIBUTE1 | — | — |
| 182 | ExpenditureItemPEOReservedAttribute10 | RESERVED_ATTRIBUTE10 | — | — |
| 183 | ExpenditureItemPEOReservedAttribute2 | RESERVED_ATTRIBUTE2 | — | — |
| 184 | ExpenditureItemPEOReservedAttribute3 | RESERVED_ATTRIBUTE3 | — | — |
| 185 | ExpenditureItemPEOReservedAttribute4 | RESERVED_ATTRIBUTE4 | — | — |
| 186 | ExpenditureItemPEOReservedAttribute5 | RESERVED_ATTRIBUTE5 | — | — |
| 187 | ExpenditureItemPEOReservedAttribute6 | RESERVED_ATTRIBUTE6 | — | — |
| 188 | ExpenditureItemPEOReservedAttribute7 | RESERVED_ATTRIBUTE7 | — | — |
| 189 | ExpenditureItemPEOReservedAttribute8 | RESERVED_ATTRIBUTE8 | — | — |
| 190 | ExpenditureItemPEOReservedAttribute9 | RESERVED_ATTRIBUTE9 | — | — |
| 191 | ExpenditureItemPEORevExcludeFlag | REV_EXCLUDE_FLAG | — | ✅ |
| 192 | ExpenditureItemPEORevenueExceptionFlag | REVENUE_EXCEPTION_FLAG | — | ✅ |
| 193 | ExpenditureItemPEORevenueHoldFlag | REVENUE_HOLD_FLAG | — | ✅ |
| 194 | ExpenditureItemPEORevenueRecogPercentage | REVENUE_RECOG_PERCENTAGE | — | ✅ |
| 195 | ExpenditureItemPEORevenueRecognizedFlag | REVENUE_RECOGNIZED_FLAG | — | ✅ |
| 196 | ExpenditureItemPEOSourceExpenditureItemId | SOURCE_EXPENDITURE_ITEM_ID | — | ✅ |
| 197 | ExpenditureItemPEOSrcSystemLinkageFunction | SRC_SYSTEM_LINKAGE_FUNCTION | — | — |
| 198 | ExpenditureItemPEOSystemLinkageFunction | SYSTEM_LINKAGE_FUNCTION | — | ✅ |
| 199 | ExpenditureItemPEOTaskId | TASK_ID | — | — |
| 200 | ExpenditureItemPEOTpAmtTypeCode | TP_AMT_TYPE_CODE | — | ✅ |
| 201 | ExpenditureItemPEOTpBaseAmount | TP_BASE_AMOUNT | — | — |
| 202 | ExpenditureItemPEOTpBillMarkupPercentage | TP_BILL_MARKUP_PERCENTAGE | — | ✅ |
| 203 | ExpenditureItemPEOTpBillRate | TP_BILL_RATE | — | ✅ |
| 204 | ExpenditureItemPEOTpIndCompiledSetId | TP_IND_COMPILED_SET_ID | — | — |
| 205 | ExpenditureItemPEOTpJobId | TP_JOB_ID | — | — |
| 206 | ExpenditureItemPEOTpRulePercentage | TP_RULE_PERCENTAGE | — | ✅ |
| 207 | ExpenditureItemPEOTpScheduleLinePercentage | TP_SCHEDULE_LINE_PERCENTAGE | — | ✅ |
| 208 | ExpenditureItemPEOTransactionSourceId | TRANSACTION_SOURCE_ID | — | ✅ |
| 209 | ExpenditureItemPEOTransferredFromExpItemId | TRANSFERRED_FROM_EXP_ITEM_ID | — | ✅ |
| 210 | ExpenditureItemPEOTxnAccumHeaderId | TXN_ACCUM_HEADER_ID | — | — |
| 211 | ExpenditureItemPEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 212 | ExpenditureItemPEOUserDefAttribute1 | USER_DEF_ATTRIBUTE1 | — | — |
| 213 | ExpenditureItemPEOUserDefAttribute10 | USER_DEF_ATTRIBUTE10 | — | — |
| 214 | ExpenditureItemPEOUserDefAttribute2 | USER_DEF_ATTRIBUTE2 | — | — |
| 215 | ExpenditureItemPEOUserDefAttribute3 | USER_DEF_ATTRIBUTE3 | — | — |
| 216 | ExpenditureItemPEOUserDefAttribute4 | USER_DEF_ATTRIBUTE4 | — | — |
| 217 | ExpenditureItemPEOUserDefAttribute5 | USER_DEF_ATTRIBUTE5 | — | — |
| 218 | ExpenditureItemPEOUserDefAttribute6 | USER_DEF_ATTRIBUTE6 | — | — |
| 219 | ExpenditureItemPEOUserDefAttribute7 | USER_DEF_ATTRIBUTE7 | — | — |
| 220 | ExpenditureItemPEOUserDefAttribute8 | USER_DEF_ATTRIBUTE8 | — | — |
| 221 | ExpenditureItemPEOUserDefAttribute9 | USER_DEF_ATTRIBUTE9 | — | — |
| 222 | ExpenditureItemPEOVendorId | VENDOR_ID | — | ✅ |
| 223 | ExpenditureItemPEOWorkTypeId | WORK_TYPE_ID | — | — |
| 224 | SourceTxnQuantity | SOURCE_TXN_QUANTITY | — | ✅ |

### [[pjf_exp_types_b|PJF_EXP_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureTypeBasePEOExpenditureCategoryId | EXPENDITURE_CATEGORY_ID | — | — |
| 2 | ExpenditureTypeBasePEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 3 | ExpenditureTypeBasePEORevenueCategoryCode | REVENUE_CATEGORY_CODE | — | — |

### [[pjf_non_labor_res_vl|PJF_NON_LABOR_RES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NonLaborResourcePEOEquipmentResourceFlag | EQUIPMENT_RESOURCE_FLAG | — | ✅ |
| 2 | NonLaborResourcePEONlrName | NLR_NAME | — | — |
| 3 | NonLaborResourcePEONonLaborResourceId | NON_LABOR_RESOURCE_ID | — | — |

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectBasePEOCarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 2 | ProjectBasePEOCreatedBy | CREATED_BY | — | — |
| 3 | ProjectBasePEOCreationDate | CREATION_DATE | — | — |
| 4 | ProjectBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ProjectBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ProjectBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ProjectBasePEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 8 | ProjectBasePEOOrgId | ORG_ID | — | — |
| 9 | ProjectBasePEOProjectId | PROJECT_ID | — | — |

### [[pjf_project_types_b|PJF_PROJECT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectTypeBasePEOCapitalCostTypeCode | CAPITAL_COST_TYPE_CODE | — | — |
| 2 | ProjectTypeBasePEOCreatedBy | CREATED_BY | — | — |
| 3 | ProjectTypeBasePEOCreationDate | CREATION_DATE | — | — |
| 4 | ProjectTypeBasePEOEnableBillingFlag | ENABLE_BILLING_FLAG | — | ✅ |
| 5 | ProjectTypeBasePEOEnableCapitalizationFlag | ENABLE_CAPITALIZATION_FLAG | — | ✅ |
| 6 | ProjectTypeBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ProjectTypeBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ProjectTypeBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ProjectTypeBasePEOProjectTypeId | PROJECT_TYPE_ID | — | — |

### [[pjf_rate_schedules_vl|PJF_RATE_SCHEDULES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostRateSchedulePEORateScheduleId | RATE_SCHEDULE_ID | — | — |
| 2 | CostRateSchedulePEORateScheduleName | RATE_SCHEDULE_NAME | — | ✅ |
| 3 | CostSchedulePEORateScheduleId | RATE_SCHEDULE_ID | — | — |
| 4 | CostSchedulePEORateScheduleName | RATE_SCHEDULE_NAME | — | ✅ |

### [[pjf_rbs_elements_vl|PJF_RBS_ELEMENTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjfRBSElementIdPEORbsElementId | RBS_ELEMENT_ID | — | — |
| 2 | ProjectIcRBSElementIdPEORbsElementId | RBS_ELEMENT_ID | — | — |

### [[pjf_rbs_element_names_vl|PJF_RBS_ELEMENT_NAMES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjfRBSElementNamePEORbsElementName | NAME | — | ✅ |
| 2 | PjfRBSElementNamePEORbsElementNameId | RBS_ELEMENT_NAME_ID | — | — |
| 3 | ProjectIcRBSElementNamePEORbsElementName | NAME | — | ✅ |
| 4 | ProjectIcRBSElementNamePEORbsElementNameId | RBS_ELEMENT_NAME_ID | — | — |

### [[pjf_system_linkages_vl|PJF_SYSTEM_LINKAGES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SrcSystemLinkagePEOFunction | FUNCTION | — | ✅ |
| 2 | SrcSystemLinkagePEOMeaning | MEANING | — | ✅ |
| 3 | SystemLinkagePEOFunction | FUNCTION | — | ✅ |
| 4 | SystemLinkagePEOMeaning | MEANING | — | ✅ |

### [[pjf_txn_document_vl|PJF_TXN_DOCUMENT_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionDocumentPEODocumentCode | DOCUMENT_CODE | — | ✅ |
| 2 | TransactionDocumentPEODocumentId | DOCUMENT_ID | — | — |
| 3 | TransactionDocumentPEODocumentName | DOCUMENT_NAME | — | ✅ |

### [[pjf_txn_doc_entry_vl|PJF_TXN_DOC_ENTRY_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionDocEntryPEODocEntryCode | DOC_ENTRY_CODE | — | ✅ |
| 2 | TransactionDocEntryPEODocEntryId | DOC_ENTRY_ID | — | — |
| 3 | TransactionDocEntryPEODocEntryName | DOC_ENTRY_NAME | — | ✅ |

### [[pjf_txn_sources_vl|PJF_TXN_SOURCES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionSourcePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | TransactionSourcePEOTransactionSource | TRANSACTION_SOURCE | — | ✅ |
| 3 | TransactionSourcePEOTransactionSourceId | TRANSACTION_SOURCE_ID | — | — |
| 4 | TransactionSourcePEOUserTransactionSource | USER_TRANSACTION_SOURCE | — | ✅ |

### [[pjf_units_of_measure_v|PJF_UNITS_OF_MEASURE_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UnitOfMeasurePEODescription | DESCRIPTION | — | ✅ |
| 2 | UnitOfMeasurePEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 3 | UnitOfMeasurePEOUomCode | UOM_CODE | — | ✅ |

### [[wis_equipment_instances|WIS_EQUIPMENT_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EquipmentInstancePEOEquipmentInstanceId | EQUIPMENT_INSTANCE_ID | — | — |

### [[wis_labor_instances|WIS_LABOR_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LaborInstancePEOLaborInstanceId | LABOR_INSTANCE_ID | — | — |

### [[wis_resources_vl|WIS_RESOURCES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WisResourcesPEOResourceId | RESOURCE_ID | — | — |

### [[xle_entity_profiles|XLE_ENTITY_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LegalEntityPEOLegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 2 | LegalEntityPEOName | NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
