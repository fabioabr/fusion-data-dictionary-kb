---
id: DOC-OTHER-PVO-ProjectAssetLineDetailPVO
doc_type: system-doc
title: "ProjectAssetLineDetailPVO — PVO Cross-Module"
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
  - ProjectAssetLineDetailPVO
  - projectassetlinedetailpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectAssetLineDetailPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Asset Line Detail. Acessa as tabelas: CST_ALL_TXN_TYPES_V, FUN_ALL_BUSINESS_UNITS_V, HR_ORGANIZATION_INFORMATION_F (+14).

**Caminho:** `FscmTopModelAM.PjcCapitalAM.ProjectAssetLineDetailPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 406 | 17 | 1 | 143 | 35% |

---

## 🔗 Tabelas Relacionadas

- [[cst_all_txn_types_v|CST_ALL_TXN_TYPES_V]] — 3 atributos (1 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 1 atributos
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 20 atributos (2 BICC)
- [[pjc_cost_dist_lines_all|PJC_COST_DIST_LINES_ALL]] — 82 atributos (25 BICC)
- [[pjc_exp_comments|PJC_EXP_COMMENTS]] — 4 atributos (1 BICC)
- [[pjc_exp_items_all|PJC_EXP_ITEMS_ALL]] — 209 atributos (86 BICC)
- [[pjc_prj_asset_lns_all|PJC_PRJ_ASSET_LNS_ALL]] — 46 atributos (14 BICC)
- [[pjc_prj_asset_ln_dets|PJC_PRJ_ASSET_LN_DETS]] — 15 atributos (1 PKs, 7 BICC)
- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 8 atributos
- [[pjf_project_types_b|PJF_PROJECT_TYPES_B]] — 4 atributos (2 BICC)
- [[pjf_txn_document_vl|PJF_TXN_DOCUMENT_VL]] — 2 atributos (1 BICC)
- [[pjf_txn_doc_entry_vl|PJF_TXN_DOC_ENTRY_VL]] — 2 atributos (1 BICC)
- [[pjf_txn_sources_vl|PJF_TXN_SOURCES_VL]] — 4 atributos (2 BICC)
- [[wis_equipment_instances|WIS_EQUIPMENT_INSTANCES]] — 1 atributos
- [[wis_labor_instances|WIS_LABOR_INSTANCES]] — 1 atributos
- [[wis_resources_vl|WIS_RESOURCES_VL]] — 1 atributos
- [[xle_entity_profiles|XLE_ENTITY_PROFILES]] — 3 atributos (1 BICC)

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
| 1 | ExpProjectBusinessUnitPEOBusinessUnitId | BU_ID | — | — |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CDLBusinessUnitPEOBusinessUnitId | ORGANIZATION_ID | — | — |
| 2 | CDLBusinessUnitPEOCreatedBy | CREATED_BY | — | — |
| 3 | CDLBusinessUnitPEOCreationDate | CREATION_DATE | — | — |
| 4 | CDLBusinessUnitPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 5 | CDLBusinessUnitPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 6 | CDLBusinessUnitPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CDLBusinessUnitPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | CDLBusinessUnitPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | CDLBusinessUnitPEOOrgInformationId | ORG_INFORMATION_ID | — | — |
| 10 | CDLBusinessUnitPEOPrimaryLedgerId | ORG_INFORMATION3 | — | — |
| 11 | ExpBUPEOBusinessUnitId | ORGANIZATION_ID | — | — |
| 12 | ExpBUPEOCreatedBy | CREATED_BY | — | — |
| 13 | ExpBUPEOCreationDate | CREATION_DATE | — | — |
| 14 | ExpBUPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 15 | ExpBUPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 16 | ExpBUPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | ExpBUPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | ExpBUPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | ExpBUPEOOrgInformationId | ORG_INFORMATION_ID | — | — |
| 20 | ExpBUPEOPrimaryLedgerId | ORG_INFORMATION3 | — | — |

### [[pjc_cost_dist_lines_all|PJC_COST_DIST_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectCostDistributionPEOAccountingStatusCode | ACCOUNTING_STATUS_CODE | — | — |
| 2 | ProjectCostDistributionPEOAcctBurdenedCost | ACCT_BURDENED_COST | — | — |
| 3 | ProjectCostDistributionPEOAcctCurrencyCode | ACCT_CURRENCY_CODE | — | — |
| 4 | ProjectCostDistributionPEOAcctEventId | ACCT_EVENT_ID | — | — |
| 5 | ProjectCostDistributionPEOAcctExchangeRate | ACCT_EXCHANGE_RATE | — | ✅ |
| 6 | ProjectCostDistributionPEOAcctRateDate | ACCT_RATE_DATE | — | ✅ |
| 7 | ProjectCostDistributionPEOAcctRateType | ACCT_RATE_TYPE | — | ✅ |
| 8 | ProjectCostDistributionPEOAcctRawCost | ACCT_RAW_COST | — | — |
| 9 | ProjectCostDistributionPEOAcctSourceCode | ACCT_SOURCE_CODE | — | — |
| 10 | ProjectCostDistributionPEOAccumulatedFlag | ACCUMULATED_FLAG | — | — |
| 11 | ProjectCostDistributionPEOBillableFlag | BILLABLE_FLAG | — | — |
| 12 | ProjectCostDistributionPEOBudgetPeriodId | BUDGET_PERIOD_ID | — | — |
| 13 | ProjectCostDistributionPEOBudgetaryControlValStatus | BUDGETARY_CONTROL_VAL_STATUS | — | — |
| 14 | ProjectCostDistributionPEOBurdenCostCrCcid | BURDEN_COST_CR_CCID | — | — |
| 15 | ProjectCostDistributionPEOBurdenCostDrCcid | BURDEN_COST_DR_CCID | — | — |
| 16 | ProjectCostDistributionPEOBurdenSumRejectionCode | BURDEN_SUM_REJECTION_CODE | — | — |
| 17 | ProjectCostDistributionPEOBurdenSumSourceRunId | BURDEN_SUM_SOURCE_RUN_ID | — | — |
| 18 | ProjectCostDistributionPEOBurdenedCostCrCcid | BURDENED_COST_CR_CCID | — | — |
| 19 | ProjectCostDistributionPEOBurdenedCostDrCcid | BURDENED_COST_DR_CCID | — | — |
| 20 | ProjectCostDistributionPEOCapitalizableFlag | CAPITALIZABLE_FLAG | — | ✅ |
| 21 | ProjectCostDistributionPEOCompDetailsId | COMP_DETAILS_ID | — | — |
| 22 | ProjectCostDistributionPEOCostScheduleId | COST_SCHEDULE_ID | — | — |
| 23 | ProjectCostDistributionPEOCostScheduleLineId | COST_SCHEDULE_LINE_ID | — | — |
| 24 | ProjectCostDistributionPEOCreatedBy | CREATED_BY | — | ✅ |
| 25 | ProjectCostDistributionPEOCreationDate | CREATION_DATE | — | ✅ |
| 26 | ProjectCostDistributionPEODenomBurdenedCost | DENOM_BURDENED_COST | — | — |
| 27 | ProjectCostDistributionPEODenomCurrencyCode | DENOM_CURRENCY_CODE | — | — |
| 28 | ProjectCostDistributionPEODenomRawCost | DENOM_RAW_COST | — | — |
| 29 | ProjectCostDistributionPEOExpenditureItemId | EXPENDITURE_ITEM_ID | — | — |
| 30 | ProjectCostDistributionPEOIndCompiledSetId | IND_COMPILED_SET_ID | — | — |
| 31 | ProjectCostDistributionPEOInterfaceId | INTERFACE_ID | — | — |
| 32 | ProjectCostDistributionPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 33 | ProjectCostDistributionPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 34 | ProjectCostDistributionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 35 | ProjectCostDistributionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 36 | ProjectCostDistributionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 37 | ProjectCostDistributionPEOLineNum | LINE_NUM | — | — |
| 38 | ProjectCostDistributionPEOLineNumReversed | LINE_NUM_REVERSED | — | ✅ |
| 39 | ProjectCostDistributionPEOLineType | LINE_TYPE | — | ✅ |
| 40 | ProjectCostDistributionPEONonLaborResourceId | NON_LABOR_RESOURCE_ID | — | — |
| 41 | ProjectCostDistributionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 42 | ProjectCostDistributionPEOOrgId | ORG_ID | — | — |
| 43 | ProjectCostDistributionPEOOrgLaborSchRuleId | ORG_LABOR_SCH_RULE_ID | — | — |
| 44 | ProjectCostDistributionPEOOrigHistoricalFlag | ORIG_HISTORICAL_FLAG | — | — |
| 45 | ProjectCostDistributionPEOParentLineNum | PARENT_LINE_NUM | — | ✅ |
| 46 | ProjectCostDistributionPEOPjsSummaryId | PJS_SUMMARY_ID | — | — |
| 47 | ProjectCostDistributionPEOPrcGeneratedFlag | PRC_GENERATED_FLAG | — | — |
| 48 | ProjectCostDistributionPEOPrevIndCompiledSetId | PREV_IND_COMPILED_SET_ID | — | — |
| 49 | ProjectCostDistributionPEOProjectBurdenedCost | PROJECT_BURDENED_COST | — | — |
| 50 | ProjectCostDistributionPEOProjectCurrencyCode | PROJECT_CURRENCY_CODE | — | — |
| 51 | ProjectCostDistributionPEOProjectExchangeRate | PROJECT_EXCHANGE_RATE | — | ✅ |
| 52 | ProjectCostDistributionPEOProjectId | PROJECT_ID | — | — |
| 53 | ProjectCostDistributionPEOProjectRateDate | PROJECT_RATE_DATE | — | ✅ |
| 54 | ProjectCostDistributionPEOProjectRateType | PROJECT_RATE_TYPE | — | ✅ |
| 55 | ProjectCostDistributionPEOProjectRawCost | PROJECT_RAW_COST | — | — |
| 56 | ProjectCostDistributionPEOProjectUnitId | PROJECT_UNIT_ID | — | — |
| 57 | ProjectCostDistributionPEOProjfuncBurdenedCost | PROJFUNC_BURDENED_COST | — | — |
| 58 | ProjectCostDistributionPEOProjfuncCostExchangeRate | PROJFUNC_COST_EXCHANGE_RATE | — | ✅ |
| 59 | ProjectCostDistributionPEOProjfuncCostRateDate | PROJFUNC_COST_RATE_DATE | — | ✅ |
| 60 | ProjectCostDistributionPEOProjfuncCostRateType | PROJFUNC_COST_RATE_TYPE | — | ✅ |
| 61 | ProjectCostDistributionPEOProjfuncCurrencyCode | PROJFUNC_CURRENCY_CODE | — | — |
| 62 | ProjectCostDistributionPEOProjfuncRawCost | PROJFUNC_RAW_COST | — | — |
| 63 | ProjectCostDistributionPEOPrvdrGlDate | PRVDR_GL_DATE | — | ✅ |
| 64 | ProjectCostDistributionPEOPrvdrGlPeriodName | PRVDR_GL_PERIOD_NAME | — | — |
| 65 | ProjectCostDistributionPEOPrvdrPaDate | PRVDR_PA_DATE | — | ✅ |
| 66 | ProjectCostDistributionPEOPrvdrPaPeriodName | PRVDR_PA_PERIOD_NAME | — | — |
| 67 | ProjectCostDistributionPEOQuantity | QUANTITY | — | — |
| 68 | ProjectCostDistributionPEORawCostCrCcid | RAW_COST_CR_CCID | — | — |
| 69 | ProjectCostDistributionPEORawCostDrCcid | RAW_COST_DR_CCID | — | — |
| 70 | ProjectCostDistributionPEORawLineNumReversed | RAW_LINE_NUM_REVERSED | — | ✅ |
| 71 | ProjectCostDistributionPEORecvrGlDate | RECVR_GL_DATE | — | — |
| 72 | ProjectCostDistributionPEORecvrGlPeriodName | RECVR_GL_PERIOD_NAME | — | — |
| 73 | ProjectCostDistributionPEORecvrPaDate | RECVR_PA_DATE | — | — |
| 74 | ProjectCostDistributionPEORecvrPaPeriodName | RECVR_PA_PERIOD_NAME | — | — |
| 75 | ProjectCostDistributionPEORequestId | REQUEST_ID | — | — |
| 76 | ProjectCostDistributionPEOReversedFlag | REVERSED_FLAG | — | ✅ |
| 77 | ProjectCostDistributionPEOSiAssetsAdditionFlag | SI_ASSETS_ADDITION_FLAG | — | ✅ |
| 78 | ProjectCostDistributionPEOTaskId | TASK_ID | — | — |
| 79 | ProjectCostDistributionPEOTransferRejectionReason | TRANSFER_REJECTION_REASON | — | ✅ |
| 80 | ProjectCostDistributionPEOTransferStatusCode | TRANSFER_STATUS_CODE | — | ✅ |
| 81 | ProjectCostDistributionPEOTxnAccumHeaderId | TXN_ACCUM_HEADER_ID | — | — |
| 82 | ProjectCostDistributionPEOWorkTypeId | WORK_TYPE_ID | — | — |

### [[pjc_exp_comments|PJC_EXP_COMMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectExpenditureCommentsPEOExpenditureComment | EXPENDITURE_COMMENT | — | ✅ |
| 2 | ProjectExpenditureCommentsPEOExpenditureItemId | EXPENDITURE_ITEM_ID | — | — |
| 3 | ProjectExpenditureCommentsPEOLineNumber | LINE_NUMBER | — | — |
| 4 | ProjectExpenditureCommentsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[pjc_exp_items_all|PJC_EXP_ITEMS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistributionId | DISTRIBUTION_ID | — | ✅ |
| 2 | ProjectExpenditureItemPEOAcctBurdenedCost | ACCT_BURDENED_COST | — | — |
| 3 | ProjectExpenditureItemPEOAcctCurrencyCode | ACCT_CURRENCY_CODE | — | ✅ |
| 4 | ProjectExpenditureItemPEOAcctExchangeRate | ACCT_EXCHANGE_RATE | — | ✅ |
| 5 | ProjectExpenditureItemPEOAcctExchangeRoundingLimit | ACCT_EXCHANGE_ROUNDING_LIMIT | — | ✅ |
| 6 | ProjectExpenditureItemPEOAcctRateDate | ACCT_RATE_DATE | — | ✅ |
| 7 | ProjectExpenditureItemPEOAcctRateDateType | ACCT_RATE_DATE_TYPE | — | ✅ |
| 8 | ProjectExpenditureItemPEOAcctRateType | ACCT_RATE_TYPE | — | ✅ |
| 9 | ProjectExpenditureItemPEOAcctRawCost | ACCT_RAW_COST | — | — |
| 10 | ProjectExpenditureItemPEOAcctTpExchangeRate | ACCT_TP_EXCHANGE_RATE | — | ✅ |
| 11 | ProjectExpenditureItemPEOAcctTpRateDate | ACCT_TP_RATE_DATE | — | ✅ |
| 12 | ProjectExpenditureItemPEOAcctTpRateType | ACCT_TP_RATE_TYPE | — | — |
| 13 | ProjectExpenditureItemPEOAcctTransferPrice | ACCT_TRANSFER_PRICE | — | — |
| 14 | ProjectExpenditureItemPEOAdjustedExpenditureItemId | ADJUSTED_EXPENDITURE_ITEM_ID | — | ✅ |
| 15 | ProjectExpenditureItemPEOAdjustmentStatus | ADJUSTMENT_STATUS | — | ✅ |
| 16 | ProjectExpenditureItemPEOAdjustmentType | ADJUSTMENT_TYPE | — | ✅ |
| 17 | ProjectExpenditureItemPEOAttribute1 | ATTRIBUTE1 | — | — |
| 18 | ProjectExpenditureItemPEOAttribute10 | ATTRIBUTE10 | — | — |
| 19 | ProjectExpenditureItemPEOAttribute2 | ATTRIBUTE2 | — | — |
| 20 | ProjectExpenditureItemPEOAttribute3 | ATTRIBUTE3 | — | — |
| 21 | ProjectExpenditureItemPEOAttribute4 | ATTRIBUTE4 | — | — |
| 22 | ProjectExpenditureItemPEOAttribute5 | ATTRIBUTE5 | — | — |
| 23 | ProjectExpenditureItemPEOAttribute6 | ATTRIBUTE6 | — | — |
| 24 | ProjectExpenditureItemPEOAttribute7 | ATTRIBUTE7 | — | — |
| 25 | ProjectExpenditureItemPEOAttribute8 | ATTRIBUTE8 | — | — |
| 26 | ProjectExpenditureItemPEOAttribute9 | ATTRIBUTE9 | — | — |
| 27 | ProjectExpenditureItemPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 28 | ProjectExpenditureItemPEOBillByCostCode | BILL_BY_COST_CODE | — | — |
| 29 | ProjectExpenditureItemPEOBillHoldFlag | BILL_HOLD_FLAG | — | ✅ |
| 30 | ProjectExpenditureItemPEOBillTransCurrencyCode | BILL_TRANS_CURRENCY_CODE | — | — |
| 31 | ProjectExpenditureItemPEOBillableFlag | BILLABLE_FLAG | — | ✅ |
| 32 | ProjectExpenditureItemPEOBurdenCostRate | BURDEN_COST_RATE | — | ✅ |
| 33 | ProjectExpenditureItemPEOBurdenSumDestRunId | BURDEN_SUM_DEST_RUN_ID | — | — |
| 34 | ProjectExpenditureItemPEOCapitalEventId | CAPITAL_EVENT_ID | — | — |
| 35 | ProjectExpenditureItemPEOCapitalizableFlag | CAPITALIZABLE_FLAG | — | ✅ |
| 36 | ProjectExpenditureItemPEOCapitalizationDistFlag | CAPITALIZATION_DIST_FLAG | — | ✅ |
| 37 | ProjectExpenditureItemPEOCcBlDistributedCode | CC_BL_DISTRIBUTED_CODE | — | ✅ |
| 38 | ProjectExpenditureItemPEOCcCrossChargeCode | CC_CROSS_CHARGE_CODE | — | ✅ |
| 39 | ProjectExpenditureItemPEOCcCrossChargeType | CC_CROSS_CHARGE_TYPE | — | ✅ |
| 40 | ProjectExpenditureItemPEOCcMarkupBaseCode | CC_MARKUP_BASE_CODE | — | ✅ |
| 41 | ProjectExpenditureItemPEOCcProcessedFlag | CC_PROCESSED_FLAG | — | — |
| 42 | ProjectExpenditureItemPEOCcPrvdrCostReclassCode | CC_PRVDR_COST_RECLASS_CODE | — | — |
| 43 | ProjectExpenditureItemPEOCcPrvdrOrganizationId | CC_PRVDR_ORGANIZATION_ID | — | — |
| 44 | ProjectExpenditureItemPEOCcRecvrOrganizationId | CC_RECVR_ORGANIZATION_ID | — | — |
| 45 | ProjectExpenditureItemPEOCcRejectionCode | CC_REJECTION_CODE | — | — |
| 46 | ProjectExpenditureItemPEOContextCategory | CONTEXT_CATEGORY | — | — |
| 47 | ProjectExpenditureItemPEOContractId | CONTRACT_ID | — | — |
| 48 | ProjectExpenditureItemPEOContractLineId | CONTRACT_LINE_ID | — | — |
| 49 | ProjectExpenditureItemPEOConvertedFlag | CONVERTED_FLAG | — | ✅ |
| 50 | ProjectExpenditureItemPEOCostAllocationKeyflexId | COST_ALLOCATION_KEYFLEX_ID | — | — |
| 51 | ProjectExpenditureItemPEOCostDistWarningCode | COST_DIST_WARNING_CODE | — | — |
| 52 | ProjectExpenditureItemPEOCostId | COST_ID | — | — |
| 53 | ProjectExpenditureItemPEOCostIndCompiledSetId | COST_IND_COMPILED_SET_ID | — | — |
| 54 | ProjectExpenditureItemPEOCostJobId | COST_JOB_ID | — | — |
| 55 | ProjectExpenditureItemPEOCostScheduleId | COST_SCHEDULE_ID | — | — |
| 56 | ProjectExpenditureItemPEOCostScheduleLineId | COST_SCHEDULE_LINE_ID | — | — |
| 57 | ProjectExpenditureItemPEOCreatedBy | CREATED_BY | — | ✅ |
| 58 | ProjectExpenditureItemPEOCreationDate | CREATION_DATE | — | ✅ |
| 59 | ProjectExpenditureItemPEODenomBurdenedCost | DENOM_BURDENED_COST | — | — |
| 60 | ProjectExpenditureItemPEODenomCurrencyCode | DENOM_CURRENCY_CODE | — | ✅ |
| 61 | ProjectExpenditureItemPEODenomRawCost | DENOM_RAW_COST | — | — |
| 62 | ProjectExpenditureItemPEODenomTpCurrencyCode | DENOM_TP_CURRENCY_CODE | — | — |
| 63 | ProjectExpenditureItemPEODenomTransferPrice | DENOM_TRANSFER_PRICE | — | — |
| 64 | ProjectExpenditureItemPEODocEntryId | DOC_ENTRY_ID | — | — |
| 65 | ProjectExpenditureItemPEODocRefId1 | DOC_REF_ID1 | — | ✅ |
| 66 | ProjectExpenditureItemPEODocRefId10 | DOC_REF_ID10 | — | — |
| 67 | ProjectExpenditureItemPEODocRefId2 | DOC_REF_ID2 | — | ✅ |
| 68 | ProjectExpenditureItemPEODocumentDistributionType | DOCUMENT_DISTRIBUTION_TYPE | — | — |
| 69 | ProjectExpenditureItemPEODocumentId | DOCUMENT_ID | — | — |
| 70 | ProjectExpenditureItemPEODocumentType | DOCUMENT_TYPE | — | — |
| 71 | ProjectExpenditureItemPEOExpGroupId | EXP_GROUP_ID | — | — |
| 72 | ProjectExpenditureItemPEOExpenditureEndingDate | EXPENDITURE_ENDING_DATE | — | ✅ |
| 73 | ProjectExpenditureItemPEOExpenditureItemDate | EXPENDITURE_ITEM_DATE | — | ✅ |
| 74 | ProjectExpenditureItemPEOExpenditureItemId | EXPENDITURE_ITEM_ID | — | — |
| 75 | ProjectExpenditureItemPEOExpenditureOrganizationId | EXPENDITURE_ORGANIZATION_ID | — | — |
| 76 | ProjectExpenditureItemPEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 77 | ProjectExpenditureItemPEOHcmAssignmentId | HCM_ASSIGNMENT_ID | — | — |
| 78 | ProjectExpenditureItemPEOHistoricalFlag | HISTORICAL_FLAG | — | — |
| 79 | ProjectExpenditureItemPEOIcBillByCostCode | IC_BILL_BY_COST_CODE | — | ✅ |
| 80 | ProjectExpenditureItemPEOIcBillHoldFlag | IC_BILL_HOLD_FLAG | — | ✅ |
| 81 | ProjectExpenditureItemPEOIcBillableFlag | IC_BILLABLE_FLAG | — | ✅ |
| 82 | ProjectExpenditureItemPEOIcInvoicedFlag | IC_INVOICED_FLAG | — | ✅ |
| 83 | ProjectExpenditureItemPEOIcInvoicedPercentage | IC_INVOICED_PERCENTAGE | — | ✅ |
| 84 | ProjectExpenditureItemPEOIcLedgerCurrInvAmt | IC_LEDGER_CURR_INV_AMT | — | — |
| 85 | ProjectExpenditureItemPEOIcLedgerCurrRevAmt | IC_LEDGER_CURR_REV_AMT | — | — |
| 86 | ProjectExpenditureItemPEOIcProjectCurrInvAmt | IC_PROJECT_CURR_INV_AMT | — | — |
| 87 | ProjectExpenditureItemPEOIcProjectCurrRevAmt | IC_PROJECT_CURR_REV_AMT | — | — |
| 88 | ProjectExpenditureItemPEOIcRbsElementId | IC_RBS_ELEMENT_ID | — | — |
| 89 | ProjectExpenditureItemPEOIcRevRecogPercentage | IC_REV_RECOG_PERCENTAGE | — | ✅ |
| 90 | ProjectExpenditureItemPEOIcRevenueHoldFlag | IC_REVENUE_HOLD_FLAG | — | ✅ |
| 91 | ProjectExpenditureItemPEOIcRevenueRecognizedFlag | IC_REVENUE_RECOGNIZED_FLAG | — | ✅ |
| 92 | ProjectExpenditureItemPEOIcTpAmtTypeCode | IC_TP_AMT_TYPE_CODE | — | ✅ |
| 93 | ProjectExpenditureItemPEOIcTpBaseCode | IC_TP_BASE_CODE | — | ✅ |
| 94 | ProjectExpenditureItemPEOIncurredByOrganizationId | INCURRED_BY_ORGANIZATION_ID | — | — |
| 95 | ProjectExpenditureItemPEOIncurredByPersonId | INCURRED_BY_PERSON_ID | — | — |
| 96 | ProjectExpenditureItemPEOInvExcludeFlag | INV_EXCLUDE_FLAG | — | ✅ |
| 97 | ProjectExpenditureItemPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 98 | ProjectExpenditureItemPEOInvoiceExceptionFlag | INVOICE_EXCEPTION_FLAG | — | ✅ |
| 99 | ProjectExpenditureItemPEOInvoicedFlag | INVOICED_FLAG | — | ✅ |
| 100 | ProjectExpenditureItemPEOInvoicedPercentage | INVOICED_PERCENTAGE | — | ✅ |
| 101 | ProjectExpenditureItemPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 102 | ProjectExpenditureItemPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 103 | ProjectExpenditureItemPEOLaborCostMultiplierName | LABOR_COST_MULTIPLIER_NAME | — | ✅ |
| 104 | ProjectExpenditureItemPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 105 | ProjectExpenditureItemPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 106 | ProjectExpenditureItemPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 107 | ProjectExpenditureItemPEOLdOrigTransactionReference | LD_ORIG_TRANSACTION_REFERENCE | — | — |
| 108 | ProjectExpenditureItemPEOLedgerCurrInvAmt | LEDGER_CURR_INV_AMT | — | — |
| 109 | ProjectExpenditureItemPEOLedgerCurrRevAmt | LEDGER_CURR_REV_AMT | — | — |
| 110 | ProjectExpenditureItemPEOManualFlag | MANUAL_FLAG | — | — |
| 111 | ProjectExpenditureItemPEONetZeroAdjustmentFlag | NET_ZERO_ADJUSTMENT_FLAG | — | ✅ |
| 112 | ProjectExpenditureItemPEONonLaborResourceId | NON_LABOR_RESOURCE_ID | — | — |
| 113 | ProjectExpenditureItemPEONonLaborResourceOrgId | NON_LABOR_RESOURCE_ORG_ID | — | — |
| 114 | ProjectExpenditureItemPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 115 | ProjectExpenditureItemPEOOrgId | ORG_ID | — | — |
| 116 | ProjectExpenditureItemPEOOrigTransactionReference | ORIG_TRANSACTION_REFERENCE | — | ✅ |
| 117 | ProjectExpenditureItemPEOOriginalDistId | ORIGINAL_DIST_ID | — | ✅ |
| 118 | ProjectExpenditureItemPEOOriginalHeaderId | ORIGINAL_HEADER_ID | — | ✅ |
| 119 | ProjectExpenditureItemPEOOriginalLineNumber | ORIGINAL_LINE_NUMBER | — | ✅ |
| 120 | ProjectExpenditureItemPEOOverrideToOrganizationId | OVERRIDE_TO_ORGANIZATION_ID | — | — |
| 121 | ProjectExpenditureItemPEOParentDistId | PARENT_DIST_ID | — | ✅ |
| 122 | ProjectExpenditureItemPEOParentHeaderId | PARENT_HEADER_ID | — | ✅ |
| 123 | ProjectExpenditureItemPEOParentLineNumber | PARENT_LINE_NUMBER | — | ✅ |
| 124 | ProjectExpenditureItemPEOPeriodAccrualFlag | PERIOD_ACCRUAL_FLAG | — | ✅ |
| 125 | ProjectExpenditureItemPEOPersonJobId | PERSON_JOB_ID | — | — |
| 126 | ProjectExpenditureItemPEOPersonType | PERSON_TYPE | — | ✅ |
| 127 | ProjectExpenditureItemPEOProjacctTransferPrice | PROJACCT_TRANSFER_PRICE | — | — |
| 128 | ProjectExpenditureItemPEOProjectBurdenedCost | PROJECT_BURDENED_COST | — | — |
| 129 | ProjectExpenditureItemPEOProjectCurrInvAmt | PROJECT_CURR_INV_AMT | — | — |
| 130 | ProjectExpenditureItemPEOProjectCurrRevAmt | PROJECT_CURR_REV_AMT | — | — |
| 131 | ProjectExpenditureItemPEOProjectCurrencyCode | PROJECT_CURRENCY_CODE | — | — |
| 132 | ProjectExpenditureItemPEOProjectExchangeRate | PROJECT_EXCHANGE_RATE | — | ✅ |
| 133 | ProjectExpenditureItemPEOProjectId | PROJECT_ID | — | — |
| 134 | ProjectExpenditureItemPEOProjectRateDate | PROJECT_RATE_DATE | — | ✅ |
| 135 | ProjectExpenditureItemPEOProjectRateDateType | PROJECT_RATE_DATE_TYPE | — | ✅ |
| 136 | ProjectExpenditureItemPEOProjectRateType | PROJECT_RATE_TYPE | — | ✅ |
| 137 | ProjectExpenditureItemPEOProjectRawCost | PROJECT_RAW_COST | — | — |
| 138 | ProjectExpenditureItemPEOProjectTpExchangeRate | PROJECT_TP_EXCHANGE_RATE | — | ✅ |
| 139 | ProjectExpenditureItemPEOProjectTpRateDate | PROJECT_TP_RATE_DATE | — | ✅ |
| 140 | ProjectExpenditureItemPEOProjectTpRateType | PROJECT_TP_RATE_TYPE | — | ✅ |
| 141 | ProjectExpenditureItemPEOProjectTransferPrice | PROJECT_TRANSFER_PRICE | — | — |
| 142 | ProjectExpenditureItemPEOProjectUnitId | PROJECT_UNIT_ID | — | — |
| 143 | ProjectExpenditureItemPEOProjfuncBurdenedCost | PROJFUNC_BURDENED_COST | — | — |
| 144 | ProjectExpenditureItemPEOProjfuncCostExchangeRate | PROJFUNC_COST_EXCHANGE_RATE | — | ✅ |
| 145 | ProjectExpenditureItemPEOProjfuncCostRateDate | PROJFUNC_COST_RATE_DATE | — | ✅ |
| 146 | ProjectExpenditureItemPEOProjfuncCostRateType | PROJFUNC_COST_RATE_TYPE | — | ✅ |
| 147 | ProjectExpenditureItemPEOProjfuncCurrencyCode | PROJFUNC_CURRENCY_CODE | — | — |
| 148 | ProjectExpenditureItemPEOProjfuncRateDateType | PROJFUNC_RATE_DATE_TYPE | — | ✅ |
| 149 | ProjectExpenditureItemPEOProjfuncRawCost | PROJFUNC_RAW_COST | — | — |
| 150 | ProjectExpenditureItemPEOProjfuncTpExchangeRate | PROJFUNC_TP_EXCHANGE_RATE | — | — |
| 151 | ProjectExpenditureItemPEOProjfuncTpRateDate | PROJFUNC_TP_RATE_DATE | — | — |
| 152 | ProjectExpenditureItemPEOProjfuncTpRateType | PROJFUNC_TP_RATE_TYPE | — | — |
| 153 | ProjectExpenditureItemPEOProjfuncTransferPrice | PROJFUNC_TRANSFER_PRICE | — | — |
| 154 | ProjectExpenditureItemPEOPrvdrAccrualDate | PRVDR_ACCRUAL_DATE | — | ✅ |
| 155 | ProjectExpenditureItemPEOPrvdrLegalEntityId | PRVDR_LEGAL_ENTITY_ID | — | — |
| 156 | ProjectExpenditureItemPEOQuantity | QUANTITY | — | — |
| 157 | ProjectExpenditureItemPEORawCostRate | RAW_COST_RATE | — | ✅ |
| 158 | ProjectExpenditureItemPEORbsElementId | RBS_ELEMENT_ID | — | — |
| 159 | ProjectExpenditureItemPEOReceiptCurrencyAmount | RECEIPT_CURRENCY_AMOUNT | — | — |
| 160 | ProjectExpenditureItemPEOReceiptCurrencyCode | RECEIPT_CURRENCY_CODE | — | — |
| 161 | ProjectExpenditureItemPEOReceiptExchangeRate | RECEIPT_EXCHANGE_RATE | — | — |
| 162 | ProjectExpenditureItemPEORecvrAccrualDate | RECVR_ACCRUAL_DATE | — | ✅ |
| 163 | ProjectExpenditureItemPEORecvrOrgId | RECVR_ORG_ID | — | — |
| 164 | ProjectExpenditureItemPEOReferenceId1 | REFERENCE_ID1 | — | ✅ |
| 165 | ProjectExpenditureItemPEORequestId | REQUEST_ID | — | — |
| 166 | ProjectExpenditureItemPEOReservedAttribute1 | RESERVED_ATTRIBUTE1 | — | — |
| 167 | ProjectExpenditureItemPEOReservedAttribute10 | RESERVED_ATTRIBUTE10 | — | — |
| 168 | ProjectExpenditureItemPEOReservedAttribute2 | RESERVED_ATTRIBUTE2 | — | — |
| 169 | ProjectExpenditureItemPEOReservedAttribute3 | RESERVED_ATTRIBUTE3 | — | — |
| 170 | ProjectExpenditureItemPEOReservedAttribute4 | RESERVED_ATTRIBUTE4 | — | — |
| 171 | ProjectExpenditureItemPEOReservedAttribute5 | RESERVED_ATTRIBUTE5 | — | — |
| 172 | ProjectExpenditureItemPEOReservedAttribute6 | RESERVED_ATTRIBUTE6 | — | — |
| 173 | ProjectExpenditureItemPEOReservedAttribute7 | RESERVED_ATTRIBUTE7 | — | — |
| 174 | ProjectExpenditureItemPEOReservedAttribute8 | RESERVED_ATTRIBUTE8 | — | — |
| 175 | ProjectExpenditureItemPEOReservedAttribute9 | RESERVED_ATTRIBUTE9 | — | — |
| 176 | ProjectExpenditureItemPEORevExcludeFlag | REV_EXCLUDE_FLAG | — | ✅ |
| 177 | ProjectExpenditureItemPEORevenueExceptionFlag | REVENUE_EXCEPTION_FLAG | — | ✅ |
| 178 | ProjectExpenditureItemPEORevenueHoldFlag | REVENUE_HOLD_FLAG | — | ✅ |
| 179 | ProjectExpenditureItemPEORevenueRecogPercentage | REVENUE_RECOG_PERCENTAGE | — | ✅ |
| 180 | ProjectExpenditureItemPEORevenueRecognizedFlag | REVENUE_RECOGNIZED_FLAG | — | ✅ |
| 181 | ProjectExpenditureItemPEOSourceExpenditureItemId | SOURCE_EXPENDITURE_ITEM_ID | — | ✅ |
| 182 | ProjectExpenditureItemPEOSrcSystemLinkageFunction | SRC_SYSTEM_LINKAGE_FUNCTION | — | — |
| 183 | ProjectExpenditureItemPEOSystemLinkageFunction | SYSTEM_LINKAGE_FUNCTION | — | ✅ |
| 184 | ProjectExpenditureItemPEOTaskId | TASK_ID | — | — |
| 185 | ProjectExpenditureItemPEOTpAmtTypeCode | TP_AMT_TYPE_CODE | — | ✅ |
| 186 | ProjectExpenditureItemPEOTpBaseAmount | TP_BASE_AMOUNT | — | — |
| 187 | ProjectExpenditureItemPEOTpBillMarkupPercentage | TP_BILL_MARKUP_PERCENTAGE | — | ✅ |
| 188 | ProjectExpenditureItemPEOTpBillRate | TP_BILL_RATE | — | ✅ |
| 189 | ProjectExpenditureItemPEOTpIndCompiledSetId | TP_IND_COMPILED_SET_ID | — | — |
| 190 | ProjectExpenditureItemPEOTpJobId | TP_JOB_ID | — | — |
| 191 | ProjectExpenditureItemPEOTpRulePercentage | TP_RULE_PERCENTAGE | — | ✅ |
| 192 | ProjectExpenditureItemPEOTpScheduleLinePercentage | TP_SCHEDULE_LINE_PERCENTAGE | — | ✅ |
| 193 | ProjectExpenditureItemPEOTransactionSourceId | TRANSACTION_SOURCE_ID | — | — |
| 194 | ProjectExpenditureItemPEOTransferredFromExpItemId | TRANSFERRED_FROM_EXP_ITEM_ID | — | ✅ |
| 195 | ProjectExpenditureItemPEOTxnAccumHeaderId | TXN_ACCUM_HEADER_ID | — | — |
| 196 | ProjectExpenditureItemPEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 197 | ProjectExpenditureItemPEOUserDefAttribute1 | USER_DEF_ATTRIBUTE1 | — | — |
| 198 | ProjectExpenditureItemPEOUserDefAttribute10 | USER_DEF_ATTRIBUTE10 | — | — |
| 199 | ProjectExpenditureItemPEOUserDefAttribute2 | USER_DEF_ATTRIBUTE2 | — | — |
| 200 | ProjectExpenditureItemPEOUserDefAttribute3 | USER_DEF_ATTRIBUTE3 | — | — |
| 201 | ProjectExpenditureItemPEOUserDefAttribute4 | USER_DEF_ATTRIBUTE4 | — | — |
| 202 | ProjectExpenditureItemPEOUserDefAttribute5 | USER_DEF_ATTRIBUTE5 | — | — |
| 203 | ProjectExpenditureItemPEOUserDefAttribute6 | USER_DEF_ATTRIBUTE6 | — | — |
| 204 | ProjectExpenditureItemPEOUserDefAttribute7 | USER_DEF_ATTRIBUTE7 | — | — |
| 205 | ProjectExpenditureItemPEOUserDefAttribute8 | USER_DEF_ATTRIBUTE8 | — | — |
| 206 | ProjectExpenditureItemPEOUserDefAttribute9 | USER_DEF_ATTRIBUTE9 | — | — |
| 207 | ProjectExpenditureItemPEOVendorId | VENDOR_ID | — | — |
| 208 | ProjectExpenditureItemPEOWorkTypeId | WORK_TYPE_ID | — | — |
| 209 | SourceTxnQuantity | SOURCE_TXN_QUANTITY | — | — |

### [[pjc_prj_asset_lns_all|PJC_PRJ_ASSET_LNS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectAssetLinePEOAmortizeFlag | AMORTIZE_FLAG | — | — |
| 2 | ProjectAssetLinePEOApDistributionLineNumber | AP_DISTRIBUTION_LINE_NUMBER | — | — |
| 3 | ProjectAssetLinePEOAssetCategoryId | ASSET_CATEGORY_ID | — | — |
| 4 | ProjectAssetLinePEOAssetCostCcid | ASSET_COST_CCID | — | — |
| 5 | ProjectAssetLinePEOCapitalEventId | CAPITAL_EVENT_ID | — | — |
| 6 | ProjectAssetLinePEOCipCcid | CIP_CCID | — | — |
| 7 | ProjectAssetLinePEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | ProjectAssetLinePEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | ProjectAssetLinePEOCurrentAssetCost | CURRENT_ASSET_COST | — | — |
| 10 | ProjectAssetLinePEODescription | DESCRIPTION | — | ✅ |
| 11 | ProjectAssetLinePEOFaPeriodName | FA_PERIOD_NAME | — | ✅ |
| 12 | ProjectAssetLinePEOGlDate | GL_DATE | — | — |
| 13 | ProjectAssetLinePEOInvoiceCreatedBy | INVOICE_CREATED_BY | — | — |
| 14 | ProjectAssetLinePEOInvoiceDate | INVOICE_DATE | — | — |
| 15 | ProjectAssetLinePEOInvoiceDistributionId | INVOICE_DISTRIBUTION_ID | — | — |
| 16 | ProjectAssetLinePEOInvoiceId | INVOICE_ID | — | — |
| 17 | ProjectAssetLinePEOInvoiceLineNumber | INVOICE_LINE_NUMBER | — | — |
| 18 | ProjectAssetLinePEOInvoiceNumber | INVOICE_NUMBER | — | — |
| 19 | ProjectAssetLinePEOInvoiceUpdatedBy | INVOICE_UPDATED_BY | — | — |
| 20 | ProjectAssetLinePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 21 | ProjectAssetLinePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 22 | ProjectAssetLinePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | ProjectAssetLinePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | ProjectAssetLinePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | ProjectAssetLinePEOLineType | LINE_TYPE | — | ✅ |
| 26 | ProjectAssetLinePEONewMasterFlag | NEW_MASTER_FLAG | — | — |
| 27 | ProjectAssetLinePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 28 | ProjectAssetLinePEOOrgId | ORG_ID | — | — |
| 29 | ProjectAssetLinePEOOriginalAssetCost | ORIGINAL_ASSET_COST | — | — |
| 30 | ProjectAssetLinePEOOriginalAssetId | ORIGINAL_ASSET_ID | — | — |
| 31 | ProjectAssetLinePEOPayablesBatchName | PAYABLES_BATCH_NAME | — | — |
| 32 | ProjectAssetLinePEOPoNumber | PO_NUMBER | — | — |
| 33 | ProjectAssetLinePEOPoVendorId | PO_VENDOR_ID | — | — |
| 34 | ProjectAssetLinePEOProjectAssetId | PROJECT_ASSET_ID | — | ✅ |
| 35 | ProjectAssetLinePEOProjectAssetLineDetailId | PROJECT_ASSET_LINE_DETAIL_ID | — | — |
| 36 | ProjectAssetLinePEOProjectAssetLineId | PROJECT_ASSET_LINE_ID | — | ✅ |
| 37 | ProjectAssetLinePEOProjectId | PROJECT_ID | — | — |
| 38 | ProjectAssetLinePEORequestId | REQUEST_ID | — | — |
| 39 | ProjectAssetLinePEORetAdjustmentTxnId | RET_ADJUSTMENT_TXN_ID | — | ✅ |
| 40 | ProjectAssetLinePEORetirementCostType | RETIREMENT_COST_TYPE | — | ✅ |
| 41 | ProjectAssetLinePEORevFromProjAssetLineId | REV_FROM_PROJ_ASSET_LINE_ID | — | — |
| 42 | ProjectAssetLinePEORevProjAssetLineId | REV_PROJ_ASSET_LINE_ID | — | ✅ |
| 43 | ProjectAssetLinePEOTaskId | TASK_ID | — | — |
| 44 | ProjectAssetLinePEOTransferRejectionReason | TRANSFER_REJECTION_REASON | — | ✅ |
| 45 | ProjectAssetLinePEOTransferStatusCode | TRANSFER_STATUS_CODE | — | ✅ |
| 46 | ProjectAssetLinePEOVendorNumber | VENDOR_NUMBER | — | — |

### [[pjc_prj_asset_ln_dets|PJC_PRJ_ASSET_LN_DETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjAssetLineDtlUniqId | PROJ_ASSET_LINE_DTL_UNIQ_ID | 🔑 | ✅ |
| 2 | ProjectAssetLineDetailPEOCipCost | CIP_COST | — | — |
| 3 | ProjectAssetLineDetailPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | ProjectAssetLineDetailPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | ProjectAssetLineDetailPEOExpenditureItemId | EXPENDITURE_ITEM_ID | — | ✅ |
| 6 | ProjectAssetLineDetailPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 7 | ProjectAssetLineDetailPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 8 | ProjectAssetLineDetailPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ProjectAssetLineDetailPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | ProjectAssetLineDetailPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ProjectAssetLineDetailPEOLineNum | LINE_NUM | — | ✅ |
| 12 | ProjectAssetLineDetailPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | ProjectAssetLineDetailPEOProjectAssetLineDetailId | PROJECT_ASSET_LINE_DETAIL_ID | — | — |
| 14 | ProjectAssetLineDetailPEORequestId | REQUEST_ID | — | — |
| 15 | ProjectAssetLineDetailPEOReversedFlag | REVERSED_FLAG | — | — |

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CDLProjectBasePEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 2 | CDLProjectBasePEOOrgId | ORG_ID | — | — |
| 3 | CDLProjectBasePEOProjectId | PROJECT_ID | — | — |
| 4 | CDLProjectBasePEOProjectUnitId | PROJECT_UNIT_ID | — | — |
| 5 | ExpProjectBasePEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 6 | ExpProjectBasePEOOrgId | ORG_ID | — | — |
| 7 | ExpProjectBasePEOProjectId | PROJECT_ID | — | — |
| 8 | ExpProjectBasePEOProjectUnitId | PROJECT_UNIT_ID | — | — |

### [[pjf_project_types_b|PJF_PROJECT_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectTypeBasePEOCapitalCostTypeCode | CAPITAL_COST_TYPE_CODE | — | — |
| 2 | ProjectTypeBasePEOEnableBillingFlag | ENABLE_BILLING_FLAG | — | ✅ |
| 3 | ProjectTypeBasePEOEnableCapitalizationFlag | ENABLE_CAPITALIZATION_FLAG | — | ✅ |
| 4 | ProjectTypeBasePEOProjectTypeId | PROJECT_TYPE_ID | — | — |

### [[pjf_txn_document_vl|PJF_TXN_DOCUMENT_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionDocumentPEODocumentCode | DOCUMENT_CODE | — | ✅ |
| 2 | TransactionDocumentPEODocumentId | DOCUMENT_ID | — | — |

### [[pjf_txn_doc_entry_vl|PJF_TXN_DOC_ENTRY_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionDocEntryPEODocEntryCode | DOC_ENTRY_CODE | — | ✅ |
| 2 | TransactionDocEntryPEODocEntryId | DOC_ENTRY_ID | — | — |

### [[pjf_txn_sources_vl|PJF_TXN_SOURCES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionSourcePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | TransactionSourcePEOTransactionSource | TRANSACTION_SOURCE | — | ✅ |
| 3 | TransactionSourcePEOTransactionSourceId | TRANSACTION_SOURCE_ID | — | — |
| 4 | TransactionSourcePEOUserTransactionSource | USER_TRANSACTION_SOURCE | — | ✅ |

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
| 1 | LegalEntityPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 2 | LegalEntityPEOName | NAME | — | ✅ |
| 3 | LegalEntityPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
