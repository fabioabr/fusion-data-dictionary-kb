---
id: DOC-OTHER-PVO-ExpenditureItemExtractPVO
doc_type: system-doc
title: "ExpenditureItemExtractPVO — PVO Cross-Module"
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
  - ExpenditureItemExtractPVO
  - expenditureitemextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenditureItemExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Expenditure Item Extract. Acessa as tabelas: PJC_EXP_ITEMS_ALL, PJC_TXN_XFACE_ALL, PJF_UNITS_OF_MEASURE_V.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjcBiccExtractAM.ExpenditureItemExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 235 | 3 | 1 | 202 | 86% |

---

## 🔗 Tabelas Relacionadas

- [[pjc_exp_items_all|PJC_EXP_ITEMS_ALL]] — 232 atributos (1 PKs, 199 BICC)
- [[pjc_txn_xface_all|PJC_TXN_XFACE_ALL]] — 1 atributos (1 BICC)
- [[pjf_units_of_measure_v|PJF_UNITS_OF_MEASURE_V]] — 2 atributos (2 BICC)

---

## ⚙️ Atributos

### [[pjc_exp_items_all|PJC_EXP_ITEMS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjcExpItemsAllAcctBurdenedCost | ACCT_BURDENED_COST | — | ✅ |
| 2 | PjcExpItemsAllAcctCurrencyCode | ACCT_CURRENCY_CODE | — | ✅ |
| 3 | PjcExpItemsAllAcctExchangeRate | ACCT_EXCHANGE_RATE | — | ✅ |
| 4 | PjcExpItemsAllAcctExchangeRoundingLimit | ACCT_EXCHANGE_ROUNDING_LIMIT | — | ✅ |
| 5 | PjcExpItemsAllAcctRateDate | ACCT_RATE_DATE | — | ✅ |
| 6 | PjcExpItemsAllAcctRateDateType | ACCT_RATE_DATE_TYPE | — | ✅ |
| 7 | PjcExpItemsAllAcctRateType | ACCT_RATE_TYPE | — | ✅ |
| 8 | PjcExpItemsAllAcctRawCost | ACCT_RAW_COST | — | ✅ |
| 9 | PjcExpItemsAllAcctTpExchangeRate | ACCT_TP_EXCHANGE_RATE | — | ✅ |
| 10 | PjcExpItemsAllAcctTpRateDate | ACCT_TP_RATE_DATE | — | ✅ |
| 11 | PjcExpItemsAllAcctTpRateType | ACCT_TP_RATE_TYPE | — | ✅ |
| 12 | PjcExpItemsAllAcctTransferPrice | ACCT_TRANSFER_PRICE | — | ✅ |
| 13 | PjcExpItemsAllAdjustedExpenditureItemId | ADJUSTED_EXPENDITURE_ITEM_ID | — | ✅ |
| 14 | PjcExpItemsAllAdjustmentStatus | ADJUSTMENT_STATUS | — | ✅ |
| 15 | PjcExpItemsAllAdjustmentType | ADJUSTMENT_TYPE | — | ✅ |
| 16 | PjcExpItemsAllAttribute1 | ATTRIBUTE1 | — | — |
| 17 | PjcExpItemsAllAttribute10 | ATTRIBUTE10 | — | — |
| 18 | PjcExpItemsAllAttribute2 | ATTRIBUTE2 | — | — |
| 19 | PjcExpItemsAllAttribute3 | ATTRIBUTE3 | — | — |
| 20 | PjcExpItemsAllAttribute4 | ATTRIBUTE4 | — | — |
| 21 | PjcExpItemsAllAttribute5 | ATTRIBUTE5 | — | — |
| 22 | PjcExpItemsAllAttribute6 | ATTRIBUTE6 | — | — |
| 23 | PjcExpItemsAllAttribute7 | ATTRIBUTE7 | — | — |
| 24 | PjcExpItemsAllAttribute8 | ATTRIBUTE8 | — | — |
| 25 | PjcExpItemsAllAttribute9 | ATTRIBUTE9 | — | — |
| 26 | PjcExpItemsAllAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 27 | PjcExpItemsAllBillByCostCode | BILL_BY_COST_CODE | — | ✅ |
| 28 | PjcExpItemsAllBillHoldFlag | BILL_HOLD_FLAG | — | ✅ |
| 29 | PjcExpItemsAllBillTransCurrencyCode | BILL_TRANS_CURRENCY_CODE | — | ✅ |
| 30 | PjcExpItemsAllBillableFlag | BILLABLE_FLAG | — | ✅ |
| 31 | PjcExpItemsAllBudgetaryControlValStatus | BUDGETARY_CONTROL_VAL_STATUS | — | ✅ |
| 32 | PjcExpItemsAllBurdenCostRate | BURDEN_COST_RATE | — | ✅ |
| 33 | PjcExpItemsAllBurdenSumDestRunId | BURDEN_SUM_DEST_RUN_ID | — | ✅ |
| 34 | PjcExpItemsAllCONTEXT_CATEGORY | CONTEXT_CATEGORY | — | ✅ |
| 35 | PjcExpItemsAllCapitalEventId | CAPITAL_EVENT_ID | — | ✅ |
| 36 | PjcExpItemsAllCapitalizableFlag | CAPITALIZABLE_FLAG | — | ✅ |
| 37 | PjcExpItemsAllCapitalizationDistFlag | CAPITALIZATION_DIST_FLAG | — | ✅ |
| 38 | PjcExpItemsAllCcBlDistributedCode | CC_BL_DISTRIBUTED_CODE | — | ✅ |
| 39 | PjcExpItemsAllCcCrossChargeCode | CC_CROSS_CHARGE_CODE | — | ✅ |
| 40 | PjcExpItemsAllCcCrossChargeType | CC_CROSS_CHARGE_TYPE | — | ✅ |
| 41 | PjcExpItemsAllCcMarkupBaseCode | CC_MARKUP_BASE_CODE | — | ✅ |
| 42 | PjcExpItemsAllCcProcessedFlag | CC_PROCESSED_FLAG | — | ✅ |
| 43 | PjcExpItemsAllCcPrvdrCostReclassCode | CC_PRVDR_COST_RECLASS_CODE | — | ✅ |
| 44 | PjcExpItemsAllCcPrvdrOrganizationId | CC_PRVDR_ORGANIZATION_ID | — | ✅ |
| 45 | PjcExpItemsAllCcRecvrOrganizationId | CC_RECVR_ORGANIZATION_ID | — | ✅ |
| 46 | PjcExpItemsAllCcRejectionCode | CC_REJECTION_CODE | — | ✅ |
| 47 | PjcExpItemsAllCmrAccountingEventId | CMR_ACCOUNTING_EVENT_ID | — | ✅ |
| 48 | PjcExpItemsAllCmrEventCostId | CMR_EVENT_COST_ID | — | ✅ |
| 49 | PjcExpItemsAllCmrExpAdjustmentFlag | CMR_EXP_ADJUSTMENT_FLAG | — | ✅ |
| 50 | PjcExpItemsAllCmrTransactionTypeCode | CMR_TRANSACTION_TYPE_CODE | — | ✅ |
| 51 | PjcExpItemsAllContextCategory | CONTEXT_CATEGORY | — | ✅ |
| 52 | PjcExpItemsAllContractId | CONTRACT_ID | — | ✅ |
| 53 | PjcExpItemsAllContractLineId | CONTRACT_LINE_ID | — | ✅ |
| 54 | PjcExpItemsAllConvertedFlag | CONVERTED_FLAG | — | ✅ |
| 55 | PjcExpItemsAllCostDistWarningCode | COST_DIST_WARNING_CODE | — | ✅ |
| 56 | PjcExpItemsAllCostIndCompiledSetId | COST_IND_COMPILED_SET_ID | — | ✅ |
| 57 | PjcExpItemsAllCostJobId | COST_JOB_ID | — | ✅ |
| 58 | PjcExpItemsAllCostScheduleId | COST_SCHEDULE_ID | — | ✅ |
| 59 | PjcExpItemsAllCostScheduleLineId | COST_SCHEDULE_LINE_ID | — | ✅ |
| 60 | PjcExpItemsAllCreatedBy | CREATED_BY | — | ✅ |
| 61 | PjcExpItemsAllCreationDate | CREATION_DATE | — | ✅ |
| 62 | PjcExpItemsAllCreationSource | CREATION_SOURCE | — | ✅ |
| 63 | PjcExpItemsAllDenomBurdenedCost | DENOM_BURDENED_COST | — | ✅ |
| 64 | PjcExpItemsAllDenomCurrencyCode | DENOM_CURRENCY_CODE | — | ✅ |
| 65 | PjcExpItemsAllDenomRawCost | DENOM_RAW_COST | — | ✅ |
| 66 | PjcExpItemsAllDenomTpCurrencyCode | DENOM_TP_CURRENCY_CODE | — | ✅ |
| 67 | PjcExpItemsAllDenomTransferPrice | DENOM_TRANSFER_PRICE | — | ✅ |
| 68 | PjcExpItemsAllDocEntryId | DOC_ENTRY_ID | — | ✅ |
| 69 | PjcExpItemsAllDocRefId1 | DOC_REF_ID1 | — | ✅ |
| 70 | PjcExpItemsAllDocRefId2 | DOC_REF_ID2 | — | ✅ |
| 71 | PjcExpItemsAllDocRefId3 | DOC_REF_ID3 | — | ✅ |
| 72 | PjcExpItemsAllDocRefId4 | DOC_REF_ID4 | — | ✅ |
| 73 | PjcExpItemsAllDocRefId5 | DOC_REF_ID5 | — | ✅ |
| 74 | PjcExpItemsAllDocumentDistributionType | DOCUMENT_DISTRIBUTION_TYPE | — | ✅ |
| 75 | PjcExpItemsAllDocumentId | DOCUMENT_ID | — | ✅ |
| 76 | PjcExpItemsAllDocumentType | DOCUMENT_TYPE | — | ✅ |
| 77 | PjcExpItemsAllExpGroupId | EXP_GROUP_ID | — | ✅ |
| 78 | PjcExpItemsAllExpenditureComment | EXPENDITURE_COMMENT | — | ✅ |
| 79 | PjcExpItemsAllExpenditureEndingDate | EXPENDITURE_ENDING_DATE | — | ✅ |
| 80 | PjcExpItemsAllExpenditureItemDate | EXPENDITURE_ITEM_DATE | — | ✅ |
| 81 | PjcExpItemsAllExpenditureItemId | EXPENDITURE_ITEM_ID | 🔑 | ✅ |
| 82 | PjcExpItemsAllExpenditureOrganizationId | EXPENDITURE_ORGANIZATION_ID | — | ✅ |
| 83 | PjcExpItemsAllExpenditureTypeId | EXPENDITURE_TYPE_ID | — | ✅ |
| 84 | PjcExpItemsAllExtOvrdBillRate | EXT_OVRD_BILL_RATE | — | ✅ |
| 85 | PjcExpItemsAllExtOvrdBillRateCurrCode | EXT_OVRD_BILL_RATE_CURR_CODE | — | ✅ |
| 86 | PjcExpItemsAllExtOvrdBillRateSourceName | EXT_OVRD_BILL_RATE_SOURCE_NAME | — | ✅ |
| 87 | PjcExpItemsAllExtOvrdBillRateSourceRef | EXT_OVRD_BILL_RATE_SOURCE_REF | — | ✅ |
| 88 | PjcExpItemsAllHcmAssignmentId | HCM_ASSIGNMENT_ID | — | ✅ |
| 89 | PjcExpItemsAllHistoricalFlag | HISTORICAL_FLAG | — | ✅ |
| 90 | PjcExpItemsAllIcBillByCostCode | IC_BILL_BY_COST_CODE | — | ✅ |
| 91 | PjcExpItemsAllIcBillHoldFlag | IC_BILL_HOLD_FLAG | — | ✅ |
| 92 | PjcExpItemsAllIcBillableFlag | IC_BILLABLE_FLAG | — | ✅ |
| 93 | PjcExpItemsAllIcInvoicedFlag | IC_INVOICED_FLAG | — | ✅ |
| 94 | PjcExpItemsAllIcInvoicedPercentage | IC_INVOICED_PERCENTAGE | — | ✅ |
| 95 | PjcExpItemsAllIcLedgerCurrInvAmt | IC_LEDGER_CURR_INV_AMT | — | ✅ |
| 96 | PjcExpItemsAllIcLedgerCurrRevAmt | IC_LEDGER_CURR_REV_AMT | — | ✅ |
| 97 | PjcExpItemsAllIcOvrdBillRate | IC_OVRD_BILL_RATE | — | ✅ |
| 98 | PjcExpItemsAllIcOvrdBillRateCurrCode | IC_OVRD_BILL_RATE_CURR_CODE | — | ✅ |
| 99 | PjcExpItemsAllIcOvrdBillRateSourceName | IC_OVRD_BILL_RATE_SOURCE_NAME | — | ✅ |
| 100 | PjcExpItemsAllIcOvrdBillRateSourceRef | IC_OVRD_BILL_RATE_SOURCE_REF | — | ✅ |
| 101 | PjcExpItemsAllIcProjectCurrInvAmt | IC_PROJECT_CURR_INV_AMT | — | ✅ |
| 102 | PjcExpItemsAllIcProjectCurrRevAmt | IC_PROJECT_CURR_REV_AMT | — | ✅ |
| 103 | PjcExpItemsAllIcRbsElementId | IC_RBS_ELEMENT_ID | — | ✅ |
| 104 | PjcExpItemsAllIcRevRecogPercentage | IC_REV_RECOG_PERCENTAGE | — | ✅ |
| 105 | PjcExpItemsAllIcRevenueHoldFlag | IC_REVENUE_HOLD_FLAG | — | ✅ |
| 106 | PjcExpItemsAllIcRevenueRecognizedFlag | IC_REVENUE_RECOGNIZED_FLAG | — | ✅ |
| 107 | PjcExpItemsAllIcTpAmtTypeCode | IC_TP_AMT_TYPE_CODE | — | ✅ |
| 108 | PjcExpItemsAllIcTpBaseCode | IC_TP_BASE_CODE | — | ✅ |
| 109 | PjcExpItemsAllIncurredByOrganizationId | INCURRED_BY_ORGANIZATION_ID | — | ✅ |
| 110 | PjcExpItemsAllIncurredByPersonId | INCURRED_BY_PERSON_ID | — | ✅ |
| 111 | PjcExpItemsAllInvAssetCategoryId | INV_ASSET_CATEGORY_ID | — | ✅ |
| 112 | PjcExpItemsAllInvExcludeFlag | INV_EXCLUDE_FLAG | — | ✅ |
| 113 | PjcExpItemsAllInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 114 | PjcExpItemsAllInvoiceExceptionFlag | INVOICE_EXCEPTION_FLAG | — | ✅ |
| 115 | PjcExpItemsAllInvoicedFlag | INVOICED_FLAG | — | ✅ |
| 116 | PjcExpItemsAllInvoicedPercentage | INVOICED_PERCENTAGE | — | ✅ |
| 117 | PjcExpItemsAllJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 118 | PjcExpItemsAllJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 119 | PjcExpItemsAllLaborCostMultiplierName | LABOR_COST_MULTIPLIER_NAME | — | ✅ |
| 120 | PjcExpItemsAllLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 121 | PjcExpItemsAllLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 122 | PjcExpItemsAllLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 123 | PjcExpItemsAllLdOrigTransactionReference | LD_ORIG_TRANSACTION_REFERENCE | — | ✅ |
| 124 | PjcExpItemsAllLedgerCurrInvAmt | LEDGER_CURR_INV_AMT | — | ✅ |
| 125 | PjcExpItemsAllLedgerCurrRevAmt | LEDGER_CURR_REV_AMT | — | ✅ |
| 126 | PjcExpItemsAllManualFlag | MANUAL_FLAG | — | ✅ |
| 127 | PjcExpItemsAllNetZeroAdjustmentFlag | NET_ZERO_ADJUSTMENT_FLAG | — | ✅ |
| 128 | PjcExpItemsAllNonLaborResourceId | NON_LABOR_RESOURCE_ID | — | ✅ |
| 129 | PjcExpItemsAllNonLaborResourceOrgId | NON_LABOR_RESOURCE_ORG_ID | — | ✅ |
| 130 | PjcExpItemsAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 131 | PjcExpItemsAllOrgId | ORG_ID | — | ✅ |
| 132 | PjcExpItemsAllOrigTransactionReference | ORIG_TRANSACTION_REFERENCE | — | ✅ |
| 133 | PjcExpItemsAllOriginalDistId | ORIGINAL_DIST_ID | — | ✅ |
| 134 | PjcExpItemsAllOriginalDistId2 | ORIGINAL_DIST_ID2 | — | — |
| 135 | PjcExpItemsAllOriginalHeaderId | ORIGINAL_HEADER_ID | — | ✅ |
| 136 | PjcExpItemsAllOriginalLineNumber | ORIGINAL_LINE_NUMBER | — | ✅ |
| 137 | PjcExpItemsAllOverrideToOrganizationId | OVERRIDE_TO_ORGANIZATION_ID | — | ✅ |
| 138 | PjcExpItemsAllParentDistId | PARENT_DIST_ID | — | ✅ |
| 139 | PjcExpItemsAllParentHeaderId | PARENT_HEADER_ID | — | ✅ |
| 140 | PjcExpItemsAllParentLineNumber | PARENT_LINE_NUMBER | — | ✅ |
| 141 | PjcExpItemsAllPeriodAccrualFlag | PERIOD_ACCRUAL_FLAG | — | ✅ |
| 142 | PjcExpItemsAllPersonJobId | PERSON_JOB_ID | — | ✅ |
| 143 | PjcExpItemsAllPersonType | PERSON_TYPE | — | ✅ |
| 144 | PjcExpItemsAllPoCategoryId | PO_CATEGORY_ID | — | ✅ |
| 145 | PjcExpItemsAllProjacctTransferPrice | PROJACCT_TRANSFER_PRICE | — | ✅ |
| 146 | PjcExpItemsAllProjectBurdenedCost | PROJECT_BURDENED_COST | — | ✅ |
| 147 | PjcExpItemsAllProjectCurrInvAmt | PROJECT_CURR_INV_AMT | — | ✅ |
| 148 | PjcExpItemsAllProjectCurrRevAmt | PROJECT_CURR_REV_AMT | — | ✅ |
| 149 | PjcExpItemsAllProjectCurrencyCode | PROJECT_CURRENCY_CODE | — | ✅ |
| 150 | PjcExpItemsAllProjectExchangeRate | PROJECT_EXCHANGE_RATE | — | ✅ |
| 151 | PjcExpItemsAllProjectId | PROJECT_ID | — | ✅ |
| 152 | PjcExpItemsAllProjectRateDate | PROJECT_RATE_DATE | — | ✅ |
| 153 | PjcExpItemsAllProjectRateDateType | PROJECT_RATE_DATE_TYPE | — | ✅ |
| 154 | PjcExpItemsAllProjectRateType | PROJECT_RATE_TYPE | — | ✅ |
| 155 | PjcExpItemsAllProjectRawCost | PROJECT_RAW_COST | — | ✅ |
| 156 | PjcExpItemsAllProjectRoleId | PROJECT_ROLE_ID | — | ✅ |
| 157 | PjcExpItemsAllProjectTpExchangeRate | PROJECT_TP_EXCHANGE_RATE | — | ✅ |
| 158 | PjcExpItemsAllProjectTpRateDate | PROJECT_TP_RATE_DATE | — | ✅ |
| 159 | PjcExpItemsAllProjectTpRateType | PROJECT_TP_RATE_TYPE | — | ✅ |
| 160 | PjcExpItemsAllProjectTransferPrice | PROJECT_TRANSFER_PRICE | — | ✅ |
| 161 | PjcExpItemsAllProjectUnitId | PROJECT_UNIT_ID | — | ✅ |
| 162 | PjcExpItemsAllProjfuncBurdenedCost | PROJFUNC_BURDENED_COST | — | ✅ |
| 163 | PjcExpItemsAllProjfuncCostExchangeRate | PROJFUNC_COST_EXCHANGE_RATE | — | ✅ |
| 164 | PjcExpItemsAllProjfuncCostRateDate | PROJFUNC_COST_RATE_DATE | — | ✅ |
| 165 | PjcExpItemsAllProjfuncCostRateType | PROJFUNC_COST_RATE_TYPE | — | ✅ |
| 166 | PjcExpItemsAllProjfuncCurrencyCode | PROJFUNC_CURRENCY_CODE | — | ✅ |
| 167 | PjcExpItemsAllProjfuncRateDateType | PROJFUNC_RATE_DATE_TYPE | — | ✅ |
| 168 | PjcExpItemsAllProjfuncRawCost | PROJFUNC_RAW_COST | — | ✅ |
| 169 | PjcExpItemsAllProjfuncTpExchangeRate | PROJFUNC_TP_EXCHANGE_RATE | — | ✅ |
| 170 | PjcExpItemsAllProjfuncTpRateDate | PROJFUNC_TP_RATE_DATE | — | ✅ |
| 171 | PjcExpItemsAllProjfuncTpRateType | PROJFUNC_TP_RATE_TYPE | — | ✅ |
| 172 | PjcExpItemsAllProjfuncTransferPrice | PROJFUNC_TRANSFER_PRICE | — | ✅ |
| 173 | PjcExpItemsAllPrvdrAccrualDate | PRVDR_ACCRUAL_DATE | — | ✅ |
| 174 | PjcExpItemsAllPrvdrLegalEntityId | PRVDR_LEGAL_ENTITY_ID | — | ✅ |
| 175 | PjcExpItemsAllQuantity | QUANTITY | — | ✅ |
| 176 | PjcExpItemsAllRawCostRate | RAW_COST_RATE | — | ✅ |
| 177 | PjcExpItemsAllRbsElementId | RBS_ELEMENT_ID | — | ✅ |
| 178 | PjcExpItemsAllReceiptCurrencyAmount | RECEIPT_CURRENCY_AMOUNT | — | ✅ |
| 179 | PjcExpItemsAllReceiptCurrencyCode | RECEIPT_CURRENCY_CODE | — | ✅ |
| 180 | PjcExpItemsAllReceiptExchangeRate | RECEIPT_EXCHANGE_RATE | — | ✅ |
| 181 | PjcExpItemsAllRecvrAccrualDate | RECVR_ACCRUAL_DATE | — | ✅ |
| 182 | PjcExpItemsAllRecvrOrgId | RECVR_ORG_ID | — | ✅ |
| 183 | PjcExpItemsAllReferenceId1 | REFERENCE_ID1 | — | ✅ |
| 184 | PjcExpItemsAllReferenceId2 | REFERENCE_ID2 | — | ✅ |
| 185 | PjcExpItemsAllReferenceId3 | REFERENCE_ID3 | — | ✅ |
| 186 | PjcExpItemsAllReferenceId4 | REFERENCE_ID4 | — | ✅ |
| 187 | PjcExpItemsAllReferenceId5 | REFERENCE_ID5 | — | ✅ |
| 188 | PjcExpItemsAllRequestId | REQUEST_ID | — | ✅ |
| 189 | PjcExpItemsAllReservedAttribute1 | RESERVED_ATTRIBUTE1 | — | — |
| 190 | PjcExpItemsAllReservedAttribute10 | RESERVED_ATTRIBUTE10 | — | — |
| 191 | PjcExpItemsAllReservedAttribute2 | RESERVED_ATTRIBUTE2 | — | — |
| 192 | PjcExpItemsAllReservedAttribute3 | RESERVED_ATTRIBUTE3 | — | — |
| 193 | PjcExpItemsAllReservedAttribute4 | RESERVED_ATTRIBUTE4 | — | — |
| 194 | PjcExpItemsAllReservedAttribute5 | RESERVED_ATTRIBUTE5 | — | — |
| 195 | PjcExpItemsAllReservedAttribute6 | RESERVED_ATTRIBUTE6 | — | — |
| 196 | PjcExpItemsAllReservedAttribute7 | RESERVED_ATTRIBUTE7 | — | — |
| 197 | PjcExpItemsAllReservedAttribute8 | RESERVED_ATTRIBUTE8 | — | — |
| 198 | PjcExpItemsAllReservedAttribute9 | RESERVED_ATTRIBUTE9 | — | — |
| 199 | PjcExpItemsAllRevExcludeFlag | REV_EXCLUDE_FLAG | — | ✅ |
| 200 | PjcExpItemsAllRevenueExceptionFlag | REVENUE_EXCEPTION_FLAG | — | ✅ |
| 201 | PjcExpItemsAllRevenueHoldFlag | REVENUE_HOLD_FLAG | — | ✅ |
| 202 | PjcExpItemsAllRevenueRecogPercentage | REVENUE_RECOG_PERCENTAGE | — | ✅ |
| 203 | PjcExpItemsAllRevenueRecognizedFlag | REVENUE_RECOGNIZED_FLAG | — | ✅ |
| 204 | PjcExpItemsAllSourceExpenditureItemId | SOURCE_EXPENDITURE_ITEM_ID | — | ✅ |
| 205 | PjcExpItemsAllSrcSystemLinkageFunction | SRC_SYSTEM_LINKAGE_FUNCTION | — | ✅ |
| 206 | PjcExpItemsAllSystemLinkageFunction | SYSTEM_LINKAGE_FUNCTION | — | ✅ |
| 207 | PjcExpItemsAllTaskId | TASK_ID | — | ✅ |
| 208 | PjcExpItemsAllTpAmtTypeCode | TP_AMT_TYPE_CODE | — | ✅ |
| 209 | PjcExpItemsAllTpBaseAmount | TP_BASE_AMOUNT | — | ✅ |
| 210 | PjcExpItemsAllTpBillMarkupPercentage | TP_BILL_MARKUP_PERCENTAGE | — | ✅ |
| 211 | PjcExpItemsAllTpBillRate | TP_BILL_RATE | — | ✅ |
| 212 | PjcExpItemsAllTpIndCompiledSetId | TP_IND_COMPILED_SET_ID | — | ✅ |
| 213 | PjcExpItemsAllTpJobId | TP_JOB_ID | — | ✅ |
| 214 | PjcExpItemsAllTpRulePercentage | TP_RULE_PERCENTAGE | — | ✅ |
| 215 | PjcExpItemsAllTpScheduleLinePercentage | TP_SCHEDULE_LINE_PERCENTAGE | — | ✅ |
| 216 | PjcExpItemsAllTransactionSourceId | TRANSACTION_SOURCE_ID | — | ✅ |
| 217 | PjcExpItemsAllTransferredFromExpItemId | TRANSFERRED_FROM_EXP_ITEM_ID | — | ✅ |
| 218 | PjcExpItemsAllTxnAccumHeaderId | TXN_ACCUM_HEADER_ID | — | ✅ |
| 219 | PjcExpItemsAllUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 220 | PjcExpItemsAllUserDefAttribute1 | USER_DEF_ATTRIBUTE1 | — | — |
| 221 | PjcExpItemsAllUserDefAttribute10 | USER_DEF_ATTRIBUTE10 | — | — |
| 222 | PjcExpItemsAllUserDefAttribute2 | USER_DEF_ATTRIBUTE2 | — | — |
| 223 | PjcExpItemsAllUserDefAttribute3 | USER_DEF_ATTRIBUTE3 | — | — |
| 224 | PjcExpItemsAllUserDefAttribute4 | USER_DEF_ATTRIBUTE4 | — | — |
| 225 | PjcExpItemsAllUserDefAttribute5 | USER_DEF_ATTRIBUTE5 | — | — |
| 226 | PjcExpItemsAllUserDefAttribute6 | USER_DEF_ATTRIBUTE6 | — | — |
| 227 | PjcExpItemsAllUserDefAttribute7 | USER_DEF_ATTRIBUTE7 | — | — |
| 228 | PjcExpItemsAllUserDefAttribute8 | USER_DEF_ATTRIBUTE8 | — | — |
| 229 | PjcExpItemsAllUserDefAttribute9 | USER_DEF_ATTRIBUTE9 | — | — |
| 230 | PjcExpItemsAllVendorId | VENDOR_ID | — | ✅ |
| 231 | PjcExpItemsAllWorkTypeId | WORK_TYPE_ID | — | ✅ |
| 232 | PjcExpItemsAllXccBtcStatus | XCC_BTC_STATUS | — | — |

### [[pjc_txn_xface_all|PJC_TXN_XFACE_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjcExpItemsAllCONTEXT_CATEGORY | CONTEXT_CATEGORY | — | ✅ |

### [[pjf_units_of_measure_v|PJF_UNITS_OF_MEASURE_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UnitOfMeasurePEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 2 | UnitOfMeasurePEOUomCode | UOM_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
