---
id: DOC-OTHER-PVO-CrossChargeDistributionP1
doc_type: system-doc
title: "CrossChargeDistributionP1 — PVO Cross-Module"
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
  - CrossChargeDistributionP1
  - crosschargedistributionp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CrossChargeDistributionP1

## 📌 Visão Geral

View Object para extração BICC de dados de Cross Charge Distribution P1. Acessa as tabelas: FUN_ALL_BUSINESS_UNITS_V, PJC_CC_DIST_LINES_ALL, PJC_EXP_ITEMS_ALL (+1).

**Caminho:** `FscmTopModelAM.PjcTransactionsAM.CrossChargeDistributionP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 236 | 4 | 1 | 44 | 19% |

---

## 🔗 Tabelas Relacionadas

- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 2 atributos (1 BICC)
- [[pjc_cc_dist_lines_all|PJC_CC_DIST_LINES_ALL]] — 58 atributos (1 PKs, 28 BICC)
- [[pjc_exp_items_all|PJC_EXP_ITEMS_ALL]] — 165 atributos (13 BICC)
- [[pjf_non_labor_res_b|PJF_NON_LABOR_RES_B]] — 11 atributos (2 BICC)

---

## ⚙️ Atributos

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOBusinessUnitId | BU_ID | — | — |
| 2 | BusinessUnitPEOPrimaryLedgerId | PRIMARY_LEDGER_ID | — | ✅ |

### [[pjc_cc_dist_lines_all|PJC_CC_DIST_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CcDistLineId | CC_DIST_LINE_ID | 🔑 | ✅ |
| 2 | CrossChargeDistributionPEOAccountingStatusCode | ACCOUNTING_STATUS_CODE | — | ✅ |
| 3 | CrossChargeDistributionPEOAcctCurrencyCode | ACCT_CURRENCY_CODE | — | ✅ |
| 4 | CrossChargeDistributionPEOAcctEventId | ACCT_EVENT_ID | — | ✅ |
| 5 | CrossChargeDistributionPEOAcctSourceCode | ACCT_SOURCE_CODE | — | — |
| 6 | CrossChargeDistributionPEOAcctTpExchangeRate | ACCT_TP_EXCHANGE_RATE | — | ✅ |
| 7 | CrossChargeDistributionPEOAcctTpRateDate | ACCT_TP_RATE_DATE | — | — |
| 8 | CrossChargeDistributionPEOAcctTpRateType | ACCT_TP_RATE_TYPE | — | — |
| 9 | CrossChargeDistributionPEOAmount | AMOUNT | — | ✅ |
| 10 | CrossChargeDistributionPEOBillMarkupPercentage | BILL_MARKUP_PERCENTAGE | — | — |
| 11 | CrossChargeDistributionPEOBillRate | BILL_RATE | — | — |
| 12 | CrossChargeDistributionPEOCreatedBy | CREATED_BY | — | ✅ |
| 13 | CrossChargeDistributionPEOCreationDate | CREATION_DATE | — | ✅ |
| 14 | CrossChargeDistributionPEOCrossChargeCode | CROSS_CHARGE_CODE | — | — |
| 15 | CrossChargeDistributionPEODenomTpCurrencyCode | DENOM_TP_CURRENCY_CODE | — | ✅ |
| 16 | CrossChargeDistributionPEODenomTransferPrice | DENOM_TRANSFER_PRICE | — | ✅ |
| 17 | CrossChargeDistributionPEODistLineIdReversed | DIST_LINE_ID_REVERSED | — | — |
| 18 | CrossChargeDistributionPEOExpenditureItemId | EXPENDITURE_ITEM_ID | — | ✅ |
| 19 | CrossChargeDistributionPEOGlDate | GL_DATE | — | ✅ |
| 20 | CrossChargeDistributionPEOGlPeriodName | GL_PERIOD_NAME | — | — |
| 21 | CrossChargeDistributionPEOIndCompiledSetId | IND_COMPILED_SET_ID | — | — |
| 22 | CrossChargeDistributionPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 23 | CrossChargeDistributionPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 24 | CrossChargeDistributionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | CrossChargeDistributionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 26 | CrossChargeDistributionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 27 | CrossChargeDistributionPEOLineNum | LINE_NUM | — | ✅ |
| 28 | CrossChargeDistributionPEOLineNumReversed | LINE_NUM_REVERSED | — | — |
| 29 | CrossChargeDistributionPEOLineType | LINE_TYPE | — | ✅ |
| 30 | CrossChargeDistributionPEOMarkupCalcBaseCode | MARKUP_CALC_BASE_CODE | — | ✅ |
| 31 | CrossChargeDistributionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 32 | CrossChargeDistributionPEOOrgId | ORG_ID | — | ✅ |
| 33 | CrossChargeDistributionPEOPaDate | PA_DATE | — | ✅ |
| 34 | CrossChargeDistributionPEOPaPeriodName | PA_PERIOD_NAME | — | — |
| 35 | CrossChargeDistributionPEOProjectId | PROJECT_ID | — | ✅ |
| 36 | CrossChargeDistributionPEOProjectTpCurrencyCode | PROJECT_TP_CURRENCY_CODE | — | ✅ |
| 37 | CrossChargeDistributionPEOProjectTpExchangeRate | PROJECT_TP_EXCHANGE_RATE | — | ✅ |
| 38 | CrossChargeDistributionPEOProjectTpRateDate | PROJECT_TP_RATE_DATE | — | — |
| 39 | CrossChargeDistributionPEOProjectTpRateType | PROJECT_TP_RATE_TYPE | — | — |
| 40 | CrossChargeDistributionPEOProjectTransferPrice | PROJECT_TRANSFER_PRICE | — | ✅ |
| 41 | CrossChargeDistributionPEOProjfuncTpCurrencyCode | PROJFUNC_TP_CURRENCY_CODE | — | ✅ |
| 42 | CrossChargeDistributionPEOProjfuncTpExchangeRate | PROJFUNC_TP_EXCHANGE_RATE | — | ✅ |
| 43 | CrossChargeDistributionPEOProjfuncTpRateDate | PROJFUNC_TP_RATE_DATE | — | — |
| 44 | CrossChargeDistributionPEOProjfuncTpRateType | PROJFUNC_TP_RATE_TYPE | — | ✅ |
| 45 | CrossChargeDistributionPEOProjfuncTransferPrice | PROJFUNC_TRANSFER_PRICE | — | ✅ |
| 46 | CrossChargeDistributionPEOReference1 | REFERENCE_1 | — | — |
| 47 | CrossChargeDistributionPEOReference2 | REFERENCE_2 | — | — |
| 48 | CrossChargeDistributionPEOReference3 | REFERENCE_3 | — | — |
| 49 | CrossChargeDistributionPEOReversedFlag | REVERSED_FLAG | — | — |
| 50 | CrossChargeDistributionPEORulePercentage | RULE_PERCENTAGE | — | — |
| 51 | CrossChargeDistributionPEOScheduleLinePercentage | SCHEDULE_LINE_PERCENTAGE | — | — |
| 52 | CrossChargeDistributionPEOTaskId | TASK_ID | — | ✅ |
| 53 | CrossChargeDistributionPEOTpAmtTypeCode | TP_AMT_TYPE_CODE | — | — |
| 54 | CrossChargeDistributionPEOTpBaseAmount | TP_BASE_AMOUNT | — | — |
| 55 | CrossChargeDistributionPEOTpJobId | TP_JOB_ID | — | — |
| 56 | CrossChargeDistributionPEOTpScheduleLineId | TP_SCHEDULE_LINE_ID | — | — |
| 57 | CrossChargeDistributionPEOTransferRejectionCode | TRANSFER_REJECTION_CODE | — | — |
| 58 | CrossChargeDistributionPEOTransferredDate | TRANSFERRED_DATE | — | — |

### [[pjc_exp_items_all|PJC_EXP_ITEMS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjcExpItemsAllAcctBurdenedCost | ACCT_BURDENED_COST | — | — |
| 2 | PjcExpItemsAllAcctCurrencyCode | ACCT_CURRENCY_CODE | — | — |
| 3 | PjcExpItemsAllAcctExchangeRate | ACCT_EXCHANGE_RATE | — | — |
| 4 | PjcExpItemsAllAcctExchangeRoundingLimit | ACCT_EXCHANGE_ROUNDING_LIMIT | — | — |
| 5 | PjcExpItemsAllAcctRateDate | ACCT_RATE_DATE | — | — |
| 6 | PjcExpItemsAllAcctRateDateType | ACCT_RATE_DATE_TYPE | — | — |
| 7 | PjcExpItemsAllAcctRateType | ACCT_RATE_TYPE | — | — |
| 8 | PjcExpItemsAllAcctRawCost | ACCT_RAW_COST | — | — |
| 9 | PjcExpItemsAllAcctTpExchangeRate | ACCT_TP_EXCHANGE_RATE | — | — |
| 10 | PjcExpItemsAllAcctTpRateDate | ACCT_TP_RATE_DATE | — | — |
| 11 | PjcExpItemsAllAcctTpRateType | ACCT_TP_RATE_TYPE | — | — |
| 12 | PjcExpItemsAllAcctTransferPrice | ACCT_TRANSFER_PRICE | — | — |
| 13 | PjcExpItemsAllAdjustedExpenditureItemId | ADJUSTED_EXPENDITURE_ITEM_ID | — | — |
| 14 | PjcExpItemsAllAdjustmentStatus | ADJUSTMENT_STATUS | — | — |
| 15 | PjcExpItemsAllAdjustmentType | ADJUSTMENT_TYPE | — | — |
| 16 | PjcExpItemsAllBillByCostCode | BILL_BY_COST_CODE | — | — |
| 17 | PjcExpItemsAllBillHoldFlag | BILL_HOLD_FLAG | — | — |
| 18 | PjcExpItemsAllBillTransCurrencyCode | BILL_TRANS_CURRENCY_CODE | — | — |
| 19 | PjcExpItemsAllBillableFlag | BILLABLE_FLAG | — | — |
| 20 | PjcExpItemsAllBurdenCostRate | BURDEN_COST_RATE | — | — |
| 21 | PjcExpItemsAllBurdenSumDestRunId | BURDEN_SUM_DEST_RUN_ID | — | — |
| 22 | PjcExpItemsAllCapitalEventId | CAPITAL_EVENT_ID | — | — |
| 23 | PjcExpItemsAllCapitalizableFlag | CAPITALIZABLE_FLAG | — | — |
| 24 | PjcExpItemsAllCapitalizationDistFlag | CAPITALIZATION_DIST_FLAG | — | — |
| 25 | PjcExpItemsAllCcBlDistributedCode | CC_BL_DISTRIBUTED_CODE | — | — |
| 26 | PjcExpItemsAllCcCrossChargeCode | CC_CROSS_CHARGE_CODE | — | ✅ |
| 27 | PjcExpItemsAllCcCrossChargeType | CC_CROSS_CHARGE_TYPE | — | ✅ |
| 28 | PjcExpItemsAllCcMarkupBaseCode | CC_MARKUP_BASE_CODE | — | — |
| 29 | PjcExpItemsAllCcProcessedFlag | CC_PROCESSED_FLAG | — | — |
| 30 | PjcExpItemsAllCcPrvdrCostReclassCode | CC_PRVDR_COST_RECLASS_CODE | — | — |
| 31 | PjcExpItemsAllCcPrvdrOrganizationId | CC_PRVDR_ORGANIZATION_ID | — | — |
| 32 | PjcExpItemsAllCcRecvrOrganizationId | CC_RECVR_ORGANIZATION_ID | — | — |
| 33 | PjcExpItemsAllCcRejectionCode | CC_REJECTION_CODE | — | — |
| 34 | PjcExpItemsAllContextCategory | CONTEXT_CATEGORY | — | — |
| 35 | PjcExpItemsAllConvertedFlag | CONVERTED_FLAG | — | — |
| 36 | PjcExpItemsAllCostDistWarningCode | COST_DIST_WARNING_CODE | — | — |
| 37 | PjcExpItemsAllCostIndCompiledSetId | COST_IND_COMPILED_SET_ID | — | — |
| 38 | PjcExpItemsAllCostJobId | COST_JOB_ID | — | — |
| 39 | PjcExpItemsAllCostScheduleId | COST_SCHEDULE_ID | — | — |
| 40 | PjcExpItemsAllCostScheduleLineId | COST_SCHEDULE_LINE_ID | — | — |
| 41 | PjcExpItemsAllCreatedBy | CREATED_BY | — | — |
| 42 | PjcExpItemsAllCreationDate | CREATION_DATE | — | — |
| 43 | PjcExpItemsAllDenomBurdenedCost | DENOM_BURDENED_COST | — | — |
| 44 | PjcExpItemsAllDenomCurrencyCode | DENOM_CURRENCY_CODE | — | — |
| 45 | PjcExpItemsAllDenomRawCost | DENOM_RAW_COST | — | — |
| 46 | PjcExpItemsAllDenomTpCurrencyCode | DENOM_TP_CURRENCY_CODE | — | — |
| 47 | PjcExpItemsAllDenomTransferPrice | DENOM_TRANSFER_PRICE | — | — |
| 48 | PjcExpItemsAllDocEntryId | DOC_ENTRY_ID | — | — |
| 49 | PjcExpItemsAllDocumentDistributionType | DOCUMENT_DISTRIBUTION_TYPE | — | — |
| 50 | PjcExpItemsAllDocumentId | DOCUMENT_ID | — | — |
| 51 | PjcExpItemsAllDocumentType | DOCUMENT_TYPE | — | — |
| 52 | PjcExpItemsAllExpGroupId | EXP_GROUP_ID | — | — |
| 53 | PjcExpItemsAllExpenditureEndingDate | EXPENDITURE_ENDING_DATE | — | — |
| 54 | PjcExpItemsAllExpenditureItemDate | EXPENDITURE_ITEM_DATE | — | ✅ |
| 55 | PjcExpItemsAllExpenditureItemId | EXPENDITURE_ITEM_ID | — | — |
| 56 | PjcExpItemsAllExpenditureTypeId | EXPENDITURE_TYPE_ID | — | ✅ |
| 57 | PjcExpItemsAllHcmAssignmentId | HCM_ASSIGNMENT_ID | — | — |
| 58 | PjcExpItemsAllHistoricalFlag | HISTORICAL_FLAG | — | — |
| 59 | PjcExpItemsAllIcBillByCostCode | IC_BILL_BY_COST_CODE | — | — |
| 60 | PjcExpItemsAllIcBillHoldFlag | IC_BILL_HOLD_FLAG | — | — |
| 61 | PjcExpItemsAllIcBillableFlag | IC_BILLABLE_FLAG | — | — |
| 62 | PjcExpItemsAllIcInvoicedFlag | IC_INVOICED_FLAG | — | — |
| 63 | PjcExpItemsAllIcInvoicedPercentage | IC_INVOICED_PERCENTAGE | — | — |
| 64 | PjcExpItemsAllIcLedgerCurrInvAmt | IC_LEDGER_CURR_INV_AMT | — | — |
| 65 | PjcExpItemsAllIcLedgerCurrRevAmt | IC_LEDGER_CURR_REV_AMT | — | — |
| 66 | PjcExpItemsAllIcProjectCurrInvAmt | IC_PROJECT_CURR_INV_AMT | — | — |
| 67 | PjcExpItemsAllIcProjectCurrRevAmt | IC_PROJECT_CURR_REV_AMT | — | — |
| 68 | PjcExpItemsAllIcRbsElementId | IC_RBS_ELEMENT_ID | — | — |
| 69 | PjcExpItemsAllIcRevRecogPercentage | IC_REV_RECOG_PERCENTAGE | — | — |
| 70 | PjcExpItemsAllIcRevenueHoldFlag | IC_REVENUE_HOLD_FLAG | — | — |
| 71 | PjcExpItemsAllIcRevenueRecognizedFlag | IC_REVENUE_RECOGNIZED_FLAG | — | — |
| 72 | PjcExpItemsAllIcTpAmtTypeCode | IC_TP_AMT_TYPE_CODE | — | — |
| 73 | PjcExpItemsAllIcTpBaseCode | IC_TP_BASE_CODE | — | — |
| 74 | PjcExpItemsAllIncurredByOrganizationId | INCURRED_BY_ORGANIZATION_ID | — | ✅ |
| 75 | PjcExpItemsAllIncurredByPersonId | INCURRED_BY_PERSON_ID | — | ✅ |
| 76 | PjcExpItemsAllInvExcludeFlag | INV_EXCLUDE_FLAG | — | — |
| 77 | PjcExpItemsAllInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 78 | PjcExpItemsAllInvoiceExceptionFlag | INVOICE_EXCEPTION_FLAG | — | — |
| 79 | PjcExpItemsAllInvoicedFlag | INVOICED_FLAG | — | — |
| 80 | PjcExpItemsAllInvoicedPercentage | INVOICED_PERCENTAGE | — | — |
| 81 | PjcExpItemsAllJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 82 | PjcExpItemsAllJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 83 | PjcExpItemsAllLaborCostMultiplierName | LABOR_COST_MULTIPLIER_NAME | — | — |
| 84 | PjcExpItemsAllLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 85 | PjcExpItemsAllLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 86 | PjcExpItemsAllLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 87 | PjcExpItemsAllLedgerCurrInvAmt | LEDGER_CURR_INV_AMT | — | — |
| 88 | PjcExpItemsAllLedgerCurrRevAmt | LEDGER_CURR_REV_AMT | — | — |
| 89 | PjcExpItemsAllManualFlag | MANUAL_FLAG | — | — |
| 90 | PjcExpItemsAllNetZeroAdjustmentFlag | NET_ZERO_ADJUSTMENT_FLAG | — | — |
| 91 | PjcExpItemsAllNonLaborResourceId | NON_LABOR_RESOURCE_ID | — | ✅ |
| 92 | PjcExpItemsAllNonLaborResourceOrgId | NON_LABOR_RESOURCE_ORG_ID | — | — |
| 93 | PjcExpItemsAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 94 | PjcExpItemsAllOrgId | ORG_ID | — | — |
| 95 | PjcExpItemsAllOrigTransactionReference | ORIG_TRANSACTION_REFERENCE | — | — |
| 96 | PjcExpItemsAllOriginalDistId | ORIGINAL_DIST_ID | — | — |
| 97 | PjcExpItemsAllOriginalHeaderId | ORIGINAL_HEADER_ID | — | — |
| 98 | PjcExpItemsAllOriginalLineNumber | ORIGINAL_LINE_NUMBER | — | — |
| 99 | PjcExpItemsAllOverrideToOrganizationId | OVERRIDE_TO_ORGANIZATION_ID | — | ✅ |
| 100 | PjcExpItemsAllParentDistId | PARENT_DIST_ID | — | — |
| 101 | PjcExpItemsAllParentHeaderId | PARENT_HEADER_ID | — | — |
| 102 | PjcExpItemsAllParentLineNumber | PARENT_LINE_NUMBER | — | — |
| 103 | PjcExpItemsAllPeriodAccrualFlag | PERIOD_ACCRUAL_FLAG | — | — |
| 104 | PjcExpItemsAllPersonJobId | PERSON_JOB_ID | — | ✅ |
| 105 | PjcExpItemsAllPersonType | PERSON_TYPE | — | — |
| 106 | PjcExpItemsAllProjacctTransferPrice | PROJACCT_TRANSFER_PRICE | — | — |
| 107 | PjcExpItemsAllProjectBurdenedCost | PROJECT_BURDENED_COST | — | — |
| 108 | PjcExpItemsAllProjectCurrInvAmt | PROJECT_CURR_INV_AMT | — | — |
| 109 | PjcExpItemsAllProjectCurrRevAmt | PROJECT_CURR_REV_AMT | — | — |
| 110 | PjcExpItemsAllProjectCurrencyCode | PROJECT_CURRENCY_CODE | — | — |
| 111 | PjcExpItemsAllProjectExchangeRate | PROJECT_EXCHANGE_RATE | — | — |
| 112 | PjcExpItemsAllProjectId | PROJECT_ID | — | — |
| 113 | PjcExpItemsAllProjectRateDate | PROJECT_RATE_DATE | — | — |
| 114 | PjcExpItemsAllProjectRateDateType | PROJECT_RATE_DATE_TYPE | — | — |
| 115 | PjcExpItemsAllProjectRateType | PROJECT_RATE_TYPE | — | — |
| 116 | PjcExpItemsAllProjectRawCost | PROJECT_RAW_COST | — | — |
| 117 | PjcExpItemsAllProjectTpExchangeRate | PROJECT_TP_EXCHANGE_RATE | — | — |
| 118 | PjcExpItemsAllProjectTpRateDate | PROJECT_TP_RATE_DATE | — | — |
| 119 | PjcExpItemsAllProjectTpRateType | PROJECT_TP_RATE_TYPE | — | — |
| 120 | PjcExpItemsAllProjectTransferPrice | PROJECT_TRANSFER_PRICE | — | — |
| 121 | PjcExpItemsAllProjectUnitId | PROJECT_UNIT_ID | — | — |
| 122 | PjcExpItemsAllProjfuncBurdenedCost | PROJFUNC_BURDENED_COST | — | — |
| 123 | PjcExpItemsAllProjfuncCostExchangeRate | PROJFUNC_COST_EXCHANGE_RATE | — | — |
| 124 | PjcExpItemsAllProjfuncCostRateDate | PROJFUNC_COST_RATE_DATE | — | — |
| 125 | PjcExpItemsAllProjfuncCostRateType | PROJFUNC_COST_RATE_TYPE | — | — |
| 126 | PjcExpItemsAllProjfuncCurrencyCode | PROJFUNC_CURRENCY_CODE | — | — |
| 127 | PjcExpItemsAllProjfuncRateDateType | PROJFUNC_RATE_DATE_TYPE | — | — |
| 128 | PjcExpItemsAllProjfuncRawCost | PROJFUNC_RAW_COST | — | — |
| 129 | PjcExpItemsAllProjfuncTpExchangeRate | PROJFUNC_TP_EXCHANGE_RATE | — | — |
| 130 | PjcExpItemsAllProjfuncTpRateDate | PROJFUNC_TP_RATE_DATE | — | — |
| 131 | PjcExpItemsAllProjfuncTpRateType | PROJFUNC_TP_RATE_TYPE | — | — |
| 132 | PjcExpItemsAllProjfuncTransferPrice | PROJFUNC_TRANSFER_PRICE | — | — |
| 133 | PjcExpItemsAllPrvdrAccrualDate | PRVDR_ACCRUAL_DATE | — | — |
| 134 | PjcExpItemsAllPrvdrLegalEntityId | PRVDR_LEGAL_ENTITY_ID | — | — |
| 135 | PjcExpItemsAllQuantity | QUANTITY | — | — |
| 136 | PjcExpItemsAllRawCostRate | RAW_COST_RATE | — | — |
| 137 | PjcExpItemsAllRbsElementId | RBS_ELEMENT_ID | — | — |
| 138 | PjcExpItemsAllReceiptCurrencyAmount | RECEIPT_CURRENCY_AMOUNT | — | — |
| 139 | PjcExpItemsAllReceiptCurrencyCode | RECEIPT_CURRENCY_CODE | — | — |
| 140 | PjcExpItemsAllReceiptExchangeRate | RECEIPT_EXCHANGE_RATE | — | — |
| 141 | PjcExpItemsAllRecvrAccrualDate | RECVR_ACCRUAL_DATE | — | — |
| 142 | PjcExpItemsAllRecvrOrgId | RECVR_ORG_ID | — | — |
| 143 | PjcExpItemsAllRequestId | REQUEST_ID | — | — |
| 144 | PjcExpItemsAllRevExcludeFlag | REV_EXCLUDE_FLAG | — | — |
| 145 | PjcExpItemsAllRevenueExceptionFlag | REVENUE_EXCEPTION_FLAG | — | — |
| 146 | PjcExpItemsAllRevenueHoldFlag | REVENUE_HOLD_FLAG | — | — |
| 147 | PjcExpItemsAllRevenueRecogPercentage | REVENUE_RECOG_PERCENTAGE | — | — |
| 148 | PjcExpItemsAllRevenueRecognizedFlag | REVENUE_RECOGNIZED_FLAG | — | — |
| 149 | PjcExpItemsAllSourceExpenditureItemId | SOURCE_EXPENDITURE_ITEM_ID | — | — |
| 150 | PjcExpItemsAllSrcSystemLinkageFunction | SRC_SYSTEM_LINKAGE_FUNCTION | — | — |
| 151 | PjcExpItemsAllSystemLinkageFunction | SYSTEM_LINKAGE_FUNCTION | — | ✅ |
| 152 | PjcExpItemsAllTaskId | TASK_ID | — | — |
| 153 | PjcExpItemsAllTpAmtTypeCode | TP_AMT_TYPE_CODE | — | — |
| 154 | PjcExpItemsAllTpBaseAmount | TP_BASE_AMOUNT | — | — |
| 155 | PjcExpItemsAllTpBillMarkupPercentage | TP_BILL_MARKUP_PERCENTAGE | — | — |
| 156 | PjcExpItemsAllTpBillRate | TP_BILL_RATE | — | — |
| 157 | PjcExpItemsAllTpIndCompiledSetId | TP_IND_COMPILED_SET_ID | — | — |
| 158 | PjcExpItemsAllTpRulePercentage | TP_RULE_PERCENTAGE | — | — |
| 159 | PjcExpItemsAllTpScheduleLinePercentage | TP_SCHEDULE_LINE_PERCENTAGE | — | — |
| 160 | PjcExpItemsAllTransactionSourceId | TRANSACTION_SOURCE_ID | — | — |
| 161 | PjcExpItemsAllTransferredFromExpItemId | TRANSFERRED_FROM_EXP_ITEM_ID | — | — |
| 162 | PjcExpItemsAllTxnAccumHeaderId | TXN_ACCUM_HEADER_ID | — | — |
| 163 | PjcExpItemsAllUnitOfMeasure | UNIT_OF_MEASURE | — | — |
| 164 | PjcExpItemsAllVendorId | VENDOR_ID | — | — |
| 165 | PjcExpItemsAllWorkTypeId | WORK_TYPE_ID | — | ✅ |

### [[pjf_non_labor_res_b|PJF_NON_LABOR_RES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NonLaborResourceBasePEOCreatedBy | CREATED_BY | — | — |
| 2 | NonLaborResourceBasePEOCreationDate | CREATION_DATE | — | — |
| 3 | NonLaborResourceBasePEOEndDateActive | END_DATE_ACTIVE | — | — |
| 4 | NonLaborResourceBasePEOEquipmentResourceFlag | EQUIPMENT_RESOURCE_FLAG | — | ✅ |
| 5 | NonLaborResourceBasePEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 6 | NonLaborResourceBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | NonLaborResourceBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | NonLaborResourceBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | NonLaborResourceBasePEONonLaborResourceId | NON_LABOR_RESOURCE_ID | — | — |
| 10 | NonLaborResourceBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | NonLaborResourceBasePEOStartDateActive | START_DATE_ACTIVE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
