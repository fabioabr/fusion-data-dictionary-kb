---
id: DOC-OTHER-PVO-ExpenditureItemRefPVO
doc_type: system-doc
title: "ExpenditureItemRefPVO — PVO Cross-Module"
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
  - ExpenditureItemRefPVO
  - expenditureitemrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpenditureItemRefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Expenditure Item Ref. Acessa as tabelas: CST_ALL_TXN_TYPES_V, FUN_ALL_BUSINESS_UNITS_V, HR_ORGANIZATION_INFORMATION_F (+23).

**Caminho:** `FscmTopModelAM.PjcTransactionsAM.ExpenditureItemRefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 333 | 26 | 1 | 131 | 39% |

---

## 🔗 Tabelas Relacionadas

- [[cst_all_txn_types_v|CST_ALL_TXN_TYPES_V]] — 3 atributos (1 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 2 atributos
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 4 atributos (1 BICC)
- [[hr_organization_v|HR_ORGANIZATION_V]] — 17 atributos (6 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 6 atributos (2 BICC)
- [[per_jobs_f_vl|PER_JOBS_F_VL]] — 10 atributos (4 BICC)
- [[pjc_capital_events|PJC_CAPITAL_EVENTS]] — 2 atributos (1 BICC)
- [[pjc_exp_comments|PJC_EXP_COMMENTS]] — 4 atributos (1 BICC)
- [[pjc_exp_groups_all|PJC_EXP_GROUPS_ALL]] — 3 atributos (1 BICC)
- [[pjc_exp_items_all|PJC_EXP_ITEMS_ALL]] — 227 atributos (1 PKs, 96 BICC)
- [[pjf_exp_types_b|PJF_EXP_TYPES_B]] — 3 atributos
- [[pjf_non_labor_res_vl|PJF_NON_LABOR_RES_VL]] — 3 atributos
- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 10 atributos (1 BICC)
- [[pjf_project_types_b|PJF_PROJECT_TYPES_B]] — 9 atributos (3 BICC)
- [[pjf_rate_schedules_vl|PJF_RATE_SCHEDULES_VL]] — 2 atributos (1 BICC)
- [[pjf_rbs_elements_vl|PJF_RBS_ELEMENTS_VL]] — 2 atributos
- [[pjf_rbs_element_names_vl|PJF_RBS_ELEMENT_NAMES_VL]] — 4 atributos (2 BICC)
- [[pjf_system_linkages_vl|PJF_SYSTEM_LINKAGES_VL]] — 4 atributos (1 BICC)
- [[pjf_txn_document_vl|PJF_TXN_DOCUMENT_VL]] — 3 atributos (2 BICC)
- [[pjf_txn_doc_entry_vl|PJF_TXN_DOC_ENTRY_VL]] — 3 atributos (2 BICC)
- [[pjf_txn_sources_vl|PJF_TXN_SOURCES_VL]] — 4 atributos (2 BICC)
- [[pjf_units_of_measure_v|PJF_UNITS_OF_MEASURE_V]] — 3 atributos (3 BICC)
- [[wis_equipment_instances|WIS_EQUIPMENT_INSTANCES]] — 1 atributos
- [[wis_labor_instances|WIS_LABOR_INSTANCES]] — 1 atributos
- [[wis_resources_vl|WIS_RESOURCES_VL]] — 1 atributos
- [[xle_entity_profiles|XLE_ENTITY_PROFILES]] — 2 atributos (1 BICC)

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

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgInfomationPEOPrvdrPrimaryLedgerID | ORG_INFORMATION3 | — | — |
| 2 | OrganizationInformationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | OrganizationInformationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | OrganizationInformationPEOOrgInformationId | ORG_INFORMATION_ID | — | — |

### [[hr_organization_v|HR_ORGANIZATION_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CCPrvdrOrganizationDPEOClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | CCPrvdrOrganizationDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | CCPrvdrOrganizationDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | CCPrvdrOrganizationDPEOName | NAME | — | ✅ |
| 5 | CCPrvdrOrganizationDPEOOrganizationId | ORGANIZATION_ID | — | — |
| 6 | CCRecvrOrganizationDPEOClassificationCode | CLASSIFICATION_CODE | — | — |
| 7 | CCRecvrOrganizationDPEOCreatedBy | CREATED_BY | — | — |
| 8 | CCRecvrOrganizationDPEOCreationDate | CREATION_DATE | — | — |
| 9 | CCRecvrOrganizationDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 10 | CCRecvrOrganizationDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 11 | CCRecvrOrganizationDPEOName | NAME | — | ✅ |
| 12 | CCRecvrOrganizationDPEOOrganizationId | ORGANIZATION_ID | — | — |
| 13 | OverrideToOrganizationDPEOClassificationCode | CLASSIFICATION_CODE | — | — |
| 14 | OverrideToOrganizationDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 15 | OverrideToOrganizationDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 16 | OverrideToOrganizationDPEOName | NAME | — | ✅ |
| 17 | OverrideToOrganizationDPEOOrganizationId | ORGANIZATION_ID | — | — |

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
| 2 | ExpenditureItemId | EXPENDITURE_ITEM_ID | 🔑 | ✅ |
| 3 | ExpenditureItemPEOAcctBurdenedCost | ACCT_BURDENED_COST | — | — |
| 4 | ExpenditureItemPEOAcctCurrencyCode | ACCT_CURRENCY_CODE | — | ✅ |
| 5 | ExpenditureItemPEOAcctExchangeRate | ACCT_EXCHANGE_RATE | — | ✅ |
| 6 | ExpenditureItemPEOAcctExchangeRoundingLimit | ACCT_EXCHANGE_ROUNDING_LIMIT | — | ✅ |
| 7 | ExpenditureItemPEOAcctRateDate | ACCT_RATE_DATE | — | ✅ |
| 8 | ExpenditureItemPEOAcctRateDateType | ACCT_RATE_DATE_TYPE | — | ✅ |
| 9 | ExpenditureItemPEOAcctRateType | ACCT_RATE_TYPE | — | ✅ |
| 10 | ExpenditureItemPEOAcctRawCost | ACCT_RAW_COST | — | — |
| 11 | ExpenditureItemPEOAcctTpExchangeRate | ACCT_TP_EXCHANGE_RATE | — | ✅ |
| 12 | ExpenditureItemPEOAcctTpRateDate | ACCT_TP_RATE_DATE | — | ✅ |
| 13 | ExpenditureItemPEOAcctTpRateType | ACCT_TP_RATE_TYPE | — | ✅ |
| 14 | ExpenditureItemPEOAcctTransferPrice | ACCT_TRANSFER_PRICE | — | — |
| 15 | ExpenditureItemPEOAdjustedExpenditureItemId | ADJUSTED_EXPENDITURE_ITEM_ID | — | ✅ |
| 16 | ExpenditureItemPEOAdjustmentStatus | ADJUSTMENT_STATUS | — | ✅ |
| 17 | ExpenditureItemPEOAdjustmentType | ADJUSTMENT_TYPE | — | ✅ |
| 18 | ExpenditureItemPEOBillByCostCode | BILL_BY_COST_CODE | — | — |
| 19 | ExpenditureItemPEOBillHoldFlag | BILL_HOLD_FLAG | — | ✅ |
| 20 | ExpenditureItemPEOBillTransCurrencyCode | BILL_TRANS_CURRENCY_CODE | — | — |
| 21 | ExpenditureItemPEOBillableFlag | BILLABLE_FLAG | — | ✅ |
| 22 | ExpenditureItemPEOBurdenCostRate | BURDEN_COST_RATE | — | ✅ |
| 23 | ExpenditureItemPEOBurdenSumDestRunId | BURDEN_SUM_DEST_RUN_ID | — | — |
| 24 | ExpenditureItemPEOCapitalEventId | CAPITAL_EVENT_ID | — | — |
| 25 | ExpenditureItemPEOCapitalizableFlag | CAPITALIZABLE_FLAG | — | ✅ |
| 26 | ExpenditureItemPEOCapitalizationDistFlag | CAPITALIZATION_DIST_FLAG | — | ✅ |
| 27 | ExpenditureItemPEOCcBlDistributedCode | CC_BL_DISTRIBUTED_CODE | — | ✅ |
| 28 | ExpenditureItemPEOCcCrossChargeCode | CC_CROSS_CHARGE_CODE | — | ✅ |
| 29 | ExpenditureItemPEOCcCrossChargeType | CC_CROSS_CHARGE_TYPE | — | ✅ |
| 30 | ExpenditureItemPEOCcMarkupBaseCode | CC_MARKUP_BASE_CODE | — | ✅ |
| 31 | ExpenditureItemPEOCcProcessedFlag | CC_PROCESSED_FLAG | — | — |
| 32 | ExpenditureItemPEOCcPrvdrCostReclassCode | CC_PRVDR_COST_RECLASS_CODE | — | — |
| 33 | ExpenditureItemPEOCcPrvdrOrganizationId | CC_PRVDR_ORGANIZATION_ID | — | — |
| 34 | ExpenditureItemPEOCcRecvrOrganizationId | CC_RECVR_ORGANIZATION_ID | — | — |
| 35 | ExpenditureItemPEOCcRejectionCode | CC_REJECTION_CODE | — | — |
| 36 | ExpenditureItemPEOCmrAccountingEventId | CMR_ACCOUNTING_EVENT_ID | — | — |
| 37 | ExpenditureItemPEOCmrAdjutmentFlag | CMR_EXP_ADJUSTMENT_FLAG | — | — |
| 38 | ExpenditureItemPEOCmrEventCostId | CMR_EVENT_COST_ID | — | — |
| 39 | ExpenditureItemPEOCmrTransactionTypeCode | CMR_TRANSACTION_TYPE_CODE | — | — |
| 40 | ExpenditureItemPEOContextCategory | CONTEXT_CATEGORY | — | — |
| 41 | ExpenditureItemPEOContractId | CONTRACT_ID | — | — |
| 42 | ExpenditureItemPEOConvertedFlag | CONVERTED_FLAG | — | ✅ |
| 43 | ExpenditureItemPEOCostAllocationKeyflexId | COST_ALLOCATION_KEYFLEX_ID | — | — |
| 44 | ExpenditureItemPEOCostDistWarningCode | COST_DIST_WARNING_CODE | — | — |
| 45 | ExpenditureItemPEOCostId | COST_ID | — | — |
| 46 | ExpenditureItemPEOCostIndCompiledSetId | COST_IND_COMPILED_SET_ID | — | — |
| 47 | ExpenditureItemPEOCostJobId | COST_JOB_ID | — | — |
| 48 | ExpenditureItemPEOCostScheduleId | COST_SCHEDULE_ID | — | — |
| 49 | ExpenditureItemPEOCostScheduleLineId | COST_SCHEDULE_LINE_ID | — | — |
| 50 | ExpenditureItemPEOCreatedBy | CREATED_BY | — | ✅ |
| 51 | ExpenditureItemPEOCreationDate | CREATION_DATE | — | ✅ |
| 52 | ExpenditureItemPEODenomBurdenedCost | DENOM_BURDENED_COST | — | — |
| 53 | ExpenditureItemPEODenomCurrencyCode | DENOM_CURRENCY_CODE | — | ✅ |
| 54 | ExpenditureItemPEODenomRawCost | DENOM_RAW_COST | — | — |
| 55 | ExpenditureItemPEODenomTpCurrencyCode | DENOM_TP_CURRENCY_CODE | — | — |
| 56 | ExpenditureItemPEODenomTransferPrice | DENOM_TRANSFER_PRICE | — | — |
| 57 | ExpenditureItemPEODocEntryId | DOC_ENTRY_ID | — | — |
| 58 | ExpenditureItemPEODocRefId1 | DOC_REF_ID1 | — | ✅ |
| 59 | ExpenditureItemPEODocRefId10 | DOC_REF_ID10 | — | — |
| 60 | ExpenditureItemPEODocRefId2 | DOC_REF_ID2 | — | ✅ |
| 61 | ExpenditureItemPEODocRefId3 | DOC_REF_ID3 | — | — |
| 62 | ExpenditureItemPEODocRefId4 | DOC_REF_ID4 | — | — |
| 63 | ExpenditureItemPEODocRefId5 | DOC_REF_ID5 | — | — |
| 64 | ExpenditureItemPEODocRefId6 | DOC_REF_ID6 | — | — |
| 65 | ExpenditureItemPEODocRefId7 | DOC_REF_ID7 | — | — |
| 66 | ExpenditureItemPEODocRefId8 | DOC_REF_ID8 | — | — |
| 67 | ExpenditureItemPEODocRefId9 | DOC_REF_ID9 | — | — |
| 68 | ExpenditureItemPEODocumentDistributionType | DOCUMENT_DISTRIBUTION_TYPE | — | — |
| 69 | ExpenditureItemPEODocumentId | DOCUMENT_ID | — | — |
| 70 | ExpenditureItemPEODocumentType | DOCUMENT_TYPE | — | — |
| 71 | ExpenditureItemPEOExpGroupId | EXP_GROUP_ID | — | — |
| 72 | ExpenditureItemPEOExpenditureEndingDate | EXPENDITURE_ENDING_DATE | — | ✅ |
| 73 | ExpenditureItemPEOExpenditureItemDate | EXPENDITURE_ITEM_DATE | — | ✅ |
| 74 | ExpenditureItemPEOExpenditureOrganizationId | EXPENDITURE_ORGANIZATION_ID | — | — |
| 75 | ExpenditureItemPEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
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
| 101 | ExpenditureItemPEOIncurredByOrganizationId | INCURRED_BY_ORGANIZATION_ID | — | — |
| 102 | ExpenditureItemPEOIncurredByPersonId | INCURRED_BY_PERSON_ID | — | — |
| 103 | ExpenditureItemPEOInvExcludeFlag | INV_EXCLUDE_FLAG | — | ✅ |
| 104 | ExpenditureItemPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 105 | ExpenditureItemPEOInvoiceExceptionFlag | INVOICE_EXCEPTION_FLAG | — | ✅ |
| 106 | ExpenditureItemPEOInvoicedFlag | INVOICED_FLAG | — | ✅ |
| 107 | ExpenditureItemPEOInvoicedPercentage | INVOICED_PERCENTAGE | — | ✅ |
| 108 | ExpenditureItemPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 109 | ExpenditureItemPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 110 | ExpenditureItemPEOLaborCostMultiplierName | LABOR_COST_MULTIPLIER_NAME | — | ✅ |
| 111 | ExpenditureItemPEOLaborDistributionTransactionReference | LD_ORIG_TRANSACTION_REFERENCE | — | — |
| 112 | ExpenditureItemPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 113 | ExpenditureItemPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 114 | ExpenditureItemPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 115 | ExpenditureItemPEOLedgerCurrInvAmt | LEDGER_CURR_INV_AMT | — | — |
| 116 | ExpenditureItemPEOLedgerCurrRevAmt | LEDGER_CURR_REV_AMT | — | — |
| 117 | ExpenditureItemPEOManualFlag | MANUAL_FLAG | — | — |
| 118 | ExpenditureItemPEONetZeroAdjustmentFlag | NET_ZERO_ADJUSTMENT_FLAG | — | ✅ |
| 119 | ExpenditureItemPEONonLaborResourceId | NON_LABOR_RESOURCE_ID | — | — |
| 120 | ExpenditureItemPEONonLaborResourceOrgId | NON_LABOR_RESOURCE_ORG_ID | — | — |
| 121 | ExpenditureItemPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 122 | ExpenditureItemPEOOrgId | ORG_ID | — | — |
| 123 | ExpenditureItemPEOOrigTransactionReference | ORIG_TRANSACTION_REFERENCE | — | ✅ |
| 124 | ExpenditureItemPEOOriginalDistId | ORIGINAL_DIST_ID | — | ✅ |
| 125 | ExpenditureItemPEOOriginalDistributionId2 | ORIGINAL_DIST_ID2 | — | — |
| 126 | ExpenditureItemPEOOriginalHeaderId | ORIGINAL_HEADER_ID | — | ✅ |
| 127 | ExpenditureItemPEOOriginalLineNumber | ORIGINAL_LINE_NUMBER | — | ✅ |
| 128 | ExpenditureItemPEOOverrideToOrganizationId | OVERRIDE_TO_ORGANIZATION_ID | — | — |
| 129 | ExpenditureItemPEOParentDistId | PARENT_DIST_ID | — | ✅ |
| 130 | ExpenditureItemPEOParentHeaderId | PARENT_HEADER_ID | — | ✅ |
| 131 | ExpenditureItemPEOParentLineNumber | PARENT_LINE_NUMBER | — | ✅ |
| 132 | ExpenditureItemPEOPeriodAccrualFlag | PERIOD_ACCRUAL_FLAG | — | ✅ |
| 133 | ExpenditureItemPEOPersonJobId | PERSON_JOB_ID | — | — |
| 134 | ExpenditureItemPEOPersonType | PERSON_TYPE | — | ✅ |
| 135 | ExpenditureItemPEOProjacctTransferPrice | PROJACCT_TRANSFER_PRICE | — | — |
| 136 | ExpenditureItemPEOProjectBurdenedCost | PROJECT_BURDENED_COST | — | — |
| 137 | ExpenditureItemPEOProjectCurrInvAmt | PROJECT_CURR_INV_AMT | — | — |
| 138 | ExpenditureItemPEOProjectCurrRevAmt | PROJECT_CURR_REV_AMT | — | — |
| 139 | ExpenditureItemPEOProjectCurrencyCode | PROJECT_CURRENCY_CODE | — | — |
| 140 | ExpenditureItemPEOProjectExchangeRate | PROJECT_EXCHANGE_RATE | — | ✅ |
| 141 | ExpenditureItemPEOProjectId | PROJECT_ID | — | — |
| 142 | ExpenditureItemPEOProjectRateDate | PROJECT_RATE_DATE | — | ✅ |
| 143 | ExpenditureItemPEOProjectRateDateType | PROJECT_RATE_DATE_TYPE | — | ✅ |
| 144 | ExpenditureItemPEOProjectRateType | PROJECT_RATE_TYPE | — | ✅ |
| 145 | ExpenditureItemPEOProjectRawCost | PROJECT_RAW_COST | — | — |
| 146 | ExpenditureItemPEOProjectRoleId | PROJECT_ROLE_ID | — | — |
| 147 | ExpenditureItemPEOProjectTpExchangeRate | PROJECT_TP_EXCHANGE_RATE | — | ✅ |
| 148 | ExpenditureItemPEOProjectTpRateDate | PROJECT_TP_RATE_DATE | — | ✅ |
| 149 | ExpenditureItemPEOProjectTpRateType | PROJECT_TP_RATE_TYPE | — | ✅ |
| 150 | ExpenditureItemPEOProjectTransferPrice | PROJECT_TRANSFER_PRICE | — | — |
| 151 | ExpenditureItemPEOProjectUnitId | PROJECT_UNIT_ID | — | — |
| 152 | ExpenditureItemPEOProjfuncBurdenedCost | PROJFUNC_BURDENED_COST | — | — |
| 153 | ExpenditureItemPEOProjfuncCostExchangeRate | PROJFUNC_COST_EXCHANGE_RATE | — | ✅ |
| 154 | ExpenditureItemPEOProjfuncCostRateDate | PROJFUNC_COST_RATE_DATE | — | ✅ |
| 155 | ExpenditureItemPEOProjfuncCostRateType | PROJFUNC_COST_RATE_TYPE | — | ✅ |
| 156 | ExpenditureItemPEOProjfuncCurrencyCode | PROJFUNC_CURRENCY_CODE | — | — |
| 157 | ExpenditureItemPEOProjfuncRateDateType | PROJFUNC_RATE_DATE_TYPE | — | ✅ |
| 158 | ExpenditureItemPEOProjfuncRawCost | PROJFUNC_RAW_COST | — | — |
| 159 | ExpenditureItemPEOProjfuncTpExchangeRate | PROJFUNC_TP_EXCHANGE_RATE | — | — |
| 160 | ExpenditureItemPEOProjfuncTpRateDate | PROJFUNC_TP_RATE_DATE | — | — |
| 161 | ExpenditureItemPEOProjfuncTpRateType | PROJFUNC_TP_RATE_TYPE | — | — |
| 162 | ExpenditureItemPEOProjfuncTransferPrice | PROJFUNC_TRANSFER_PRICE | — | — |
| 163 | ExpenditureItemPEOPrvdrAccrualDate | PRVDR_ACCRUAL_DATE | — | ✅ |
| 164 | ExpenditureItemPEOPrvdrLegalEntityId | PRVDR_LEGAL_ENTITY_ID | — | — |
| 165 | ExpenditureItemPEOQuantity | QUANTITY | — | — |
| 166 | ExpenditureItemPEORawCostRate | RAW_COST_RATE | — | ✅ |
| 167 | ExpenditureItemPEORbsElementId | RBS_ELEMENT_ID | — | — |
| 168 | ExpenditureItemPEOReceiptCurrencyAmount | RECEIPT_CURRENCY_AMOUNT | — | — |
| 169 | ExpenditureItemPEOReceiptCurrencyCode | RECEIPT_CURRENCY_CODE | — | — |
| 170 | ExpenditureItemPEOReceiptExchangeRate | RECEIPT_EXCHANGE_RATE | — | — |
| 171 | ExpenditureItemPEORecvrAccrualDate | RECVR_ACCRUAL_DATE | — | ✅ |
| 172 | ExpenditureItemPEORecvrOrgId | RECVR_ORG_ID | — | — |
| 173 | ExpenditureItemPEOReferenceId1 | REFERENCE_ID1 | — | ✅ |
| 174 | ExpenditureItemPEOReferenceId10 | REFERENCE_ID10 | — | — |
| 175 | ExpenditureItemPEOReferenceId2 | REFERENCE_ID2 | — | — |
| 176 | ExpenditureItemPEOReferenceId3 | REFERENCE_ID3 | — | — |
| 177 | ExpenditureItemPEOReferenceId4 | REFERENCE_ID4 | — | — |
| 178 | ExpenditureItemPEOReferenceId5 | REFERENCE_ID5 | — | — |
| 179 | ExpenditureItemPEOReferenceId6 | REFERENCE_ID6 | — | — |
| 180 | ExpenditureItemPEOReferenceId7 | REFERENCE_ID7 | — | — |
| 181 | ExpenditureItemPEOReferenceId8 | REFERENCE_ID8 | — | — |
| 182 | ExpenditureItemPEOReferenceId9 | REFERENCE_ID9 | — | — |
| 183 | ExpenditureItemPEORequestId | REQUEST_ID | — | — |
| 184 | ExpenditureItemPEOReservedAttribute1 | RESERVED_ATTRIBUTE1 | — | — |
| 185 | ExpenditureItemPEOReservedAttribute10 | RESERVED_ATTRIBUTE10 | — | — |
| 186 | ExpenditureItemPEOReservedAttribute2 | RESERVED_ATTRIBUTE2 | — | — |
| 187 | ExpenditureItemPEOReservedAttribute3 | RESERVED_ATTRIBUTE3 | — | — |
| 188 | ExpenditureItemPEOReservedAttribute4 | RESERVED_ATTRIBUTE4 | — | — |
| 189 | ExpenditureItemPEOReservedAttribute5 | RESERVED_ATTRIBUTE5 | — | — |
| 190 | ExpenditureItemPEOReservedAttribute6 | RESERVED_ATTRIBUTE6 | — | — |
| 191 | ExpenditureItemPEOReservedAttribute7 | RESERVED_ATTRIBUTE7 | — | — |
| 192 | ExpenditureItemPEOReservedAttribute8 | RESERVED_ATTRIBUTE8 | — | — |
| 193 | ExpenditureItemPEOReservedAttribute9 | RESERVED_ATTRIBUTE9 | — | — |
| 194 | ExpenditureItemPEORevExcludeFlag | REV_EXCLUDE_FLAG | — | ✅ |
| 195 | ExpenditureItemPEORevenueExceptionFlag | REVENUE_EXCEPTION_FLAG | — | ✅ |
| 196 | ExpenditureItemPEORevenueHoldFlag | REVENUE_HOLD_FLAG | — | ✅ |
| 197 | ExpenditureItemPEORevenueRecogPercentage | REVENUE_RECOG_PERCENTAGE | — | ✅ |
| 198 | ExpenditureItemPEORevenueRecognizedFlag | REVENUE_RECOGNIZED_FLAG | — | ✅ |
| 199 | ExpenditureItemPEOSourceExpenditureItemId | SOURCE_EXPENDITURE_ITEM_ID | — | ✅ |
| 200 | ExpenditureItemPEOSrcSystemLinkageFunction | SRC_SYSTEM_LINKAGE_FUNCTION | — | — |
| 201 | ExpenditureItemPEOSystemLinkageFunction | SYSTEM_LINKAGE_FUNCTION | — | ✅ |
| 202 | ExpenditureItemPEOTaskId | TASK_ID | — | — |
| 203 | ExpenditureItemPEOTpAmtTypeCode | TP_AMT_TYPE_CODE | — | ✅ |
| 204 | ExpenditureItemPEOTpBaseAmount | TP_BASE_AMOUNT | — | — |
| 205 | ExpenditureItemPEOTpBillMarkupPercentage | TP_BILL_MARKUP_PERCENTAGE | — | ✅ |
| 206 | ExpenditureItemPEOTpBillRate | TP_BILL_RATE | — | ✅ |
| 207 | ExpenditureItemPEOTpIndCompiledSetId | TP_IND_COMPILED_SET_ID | — | — |
| 208 | ExpenditureItemPEOTpJobId | TP_JOB_ID | — | — |
| 209 | ExpenditureItemPEOTpRulePercentage | TP_RULE_PERCENTAGE | — | ✅ |
| 210 | ExpenditureItemPEOTpScheduleLinePercentage | TP_SCHEDULE_LINE_PERCENTAGE | — | ✅ |
| 211 | ExpenditureItemPEOTransactionSourceId | TRANSACTION_SOURCE_ID | — | — |
| 212 | ExpenditureItemPEOTransferredFromExpItemId | TRANSFERRED_FROM_EXP_ITEM_ID | — | ✅ |
| 213 | ExpenditureItemPEOTxnAccumHeaderId | TXN_ACCUM_HEADER_ID | — | — |
| 214 | ExpenditureItemPEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 215 | ExpenditureItemPEOUserDefAttribute1 | USER_DEF_ATTRIBUTE1 | — | — |
| 216 | ExpenditureItemPEOUserDefAttribute10 | USER_DEF_ATTRIBUTE10 | — | — |
| 217 | ExpenditureItemPEOUserDefAttribute2 | USER_DEF_ATTRIBUTE2 | — | — |
| 218 | ExpenditureItemPEOUserDefAttribute3 | USER_DEF_ATTRIBUTE3 | — | — |
| 219 | ExpenditureItemPEOUserDefAttribute4 | USER_DEF_ATTRIBUTE4 | — | — |
| 220 | ExpenditureItemPEOUserDefAttribute5 | USER_DEF_ATTRIBUTE5 | — | — |
| 221 | ExpenditureItemPEOUserDefAttribute6 | USER_DEF_ATTRIBUTE6 | — | — |
| 222 | ExpenditureItemPEOUserDefAttribute7 | USER_DEF_ATTRIBUTE7 | — | — |
| 223 | ExpenditureItemPEOUserDefAttribute8 | USER_DEF_ATTRIBUTE8 | — | — |
| 224 | ExpenditureItemPEOUserDefAttribute9 | USER_DEF_ATTRIBUTE9 | — | — |
| 225 | ExpenditureItemPEOVendorId | VENDOR_ID | — | — |
| 226 | ExpenditureItemPEOWorkTypeId | WORK_TYPE_ID | — | — |
| 227 | SourceTxnQuantity | SOURCE_TXN_QUANTITY | — | — |

### [[pjf_exp_types_b|PJF_EXP_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenditureTypeBasePEOExpenditureCategoryId | EXPENDITURE_CATEGORY_ID | — | — |
| 2 | ExpenditureTypeBasePEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | — |
| 3 | ExpenditureTypeBasePEORevenueCategoryCode | REVENUE_CATEGORY_CODE | — | — |

### [[pjf_non_labor_res_vl|PJF_NON_LABOR_RES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NonLaborResourcePEOEquipmentResourceFlag | EQUIPMENT_RESOURCE_FLAG | — | — |
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
| 10 | ProjectBasePEOProjectUnitId | PROJECT_UNIT_ID | — | — |

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
| 1 | CostSchedulePEORateScheduleId | RATE_SCHEDULE_ID | — | — |
| 2 | CostSchedulePEORateScheduleName | RATE_SCHEDULE_NAME | — | ✅ |

### [[pjf_rbs_elements_vl|PJF_RBS_ELEMENTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectIcRBSElementIdPEORbsElementId | RBS_ELEMENT_ID | — | — |
| 2 | ProjectRBSElementPEORbsElementId | RBS_ELEMENT_ID | — | — |

### [[pjf_rbs_element_names_vl|PJF_RBS_ELEMENT_NAMES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectIcRBSElementNamePEORbsElementName | NAME | — | ✅ |
| 2 | ProjectIcRBSElementNamePEORbsElementNameId | RBS_ELEMENT_NAME_ID | — | — |
| 3 | ProjectRBSElementNamePEORbsElementName | NAME | — | ✅ |
| 4 | ProjectRBSElementNamePEORbsElementNameId | RBS_ELEMENT_NAME_ID | — | — |

### [[pjf_system_linkages_vl|PJF_SYSTEM_LINKAGES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SrcSystemLinkagePEOFunction | FUNCTION | — | — |
| 2 | SrcSystemLinkagePEOMeaning | MEANING | — | ✅ |
| 3 | SystemLinkagePEOFunction | FUNCTION | — | — |
| 4 | SystemLinkagePEOMeaning | MEANING | — | — |

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
| 1 | LegalEntityPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 2 | LegalEntityPEOName | NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
