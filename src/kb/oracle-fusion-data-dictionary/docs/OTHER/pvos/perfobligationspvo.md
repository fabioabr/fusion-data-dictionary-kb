---
id: DOC-OTHER-PVO-PerfObligationsPVO
doc_type: system-doc
title: "PerfObligationsPVO — PVO Cross-Module"
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
  - PerfObligationsPVO
  - perfobligationspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PerfObligationsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Perf Obligations. Acessa as tabelas: GL_LEDGERS, PER_PERSON_NAMES_F_V, PER_USERS (+4).

**Caminho:** `FscmTopModelAM.FinVrmRRSharedPublicModelAM.PerfObligationsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 244 | 7 | 1 | 68 | 28% |

---

## 🔗 Tabelas Relacionadas

- [[gl_ledgers|GL_LEDGERS]] — 6 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 20 atributos
- [[per_users|PER_USERS]] — 16 atributos
- [[vrm_customer_contract_headers|VRM_CUSTOMER_CONTRACT_HEADERS]] — 34 atributos (2 BICC)
- [[vrm_fmv_lines|VRM_FMV_LINES]] — 93 atributos (14 BICC)
- [[vrm_fmv_templates_b|VRM_FMV_TEMPLATES_B]] — 3 atributos
- [[vrm_perf_obligations|VRM_PERF_OBLIGATIONS]] — 72 atributos (1 PKs, 52 BICC)

---

## ⚙️ Atributos

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlLedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 2 | GlLedgersCreatedBy | CREATED_BY | — | — |
| 3 | GlLedgersCreationDate | CREATION_DATE | — | — |
| 4 | GlLedgersLedgerId | LEDGER_ID | — | — |
| 5 | GlLedgersName | NAME | — | — |
| 6 | GlLedgersObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustContHdrPEOCreatedBy | DISPLAY_NAME | — | — |
| 2 | CustContHdrPEOLastUpdatedBy | DISPLAY_NAME | — | — |
| 3 | CustContHeadPersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | CustContHeadPersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 5 | CustContHeadPersonCreatedByPersonId | PERSON_ID | — | — |
| 6 | CustContHeadPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 7 | CustContHeadPersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | CustContHeadPersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | CustContHeadPersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | CustContHeadPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |
| 11 | PersonCreatedByDisplayName | DISPLAY_NAME | — | — |
| 12 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 13 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 14 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 15 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 16 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | — |
| 17 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 18 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 19 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 20 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustContHeadUserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | CustContHeadUserCreatedByPersonId | PERSON_ID | — | — |
| 3 | CustContHeadUserCreatedByUserId | USER_ID | — | — |
| 4 | CustContHeadUserCreatedByUsername | USERNAME | — | — |
| 5 | CustContHeadUserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | CustContHeadUserUpdatedByPersonId | PERSON_ID | — | — |
| 7 | CustContHeadUserUpdatedByUserId | USER_ID | — | — |
| 8 | CustContHeadUserUpdatedByUsername | USERNAME | — | — |
| 9 | UserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | UserCreatedByPersonId | PERSON_ID | — | — |
| 11 | UserCreatedByUserId | USER_ID | — | — |
| 12 | UserCreatedByUsername | USERNAME | — | — |
| 13 | UserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 15 | UserUpdatedByUserId | USER_ID | — | — |
| 16 | UserUpdatedByUsername | USERNAME | — | — |

### [[vrm_customer_contract_headers|VRM_CUSTOMER_CONTRACT_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustContHdrPEOAllocationRequestId | ALLOCATION_REQUEST_ID | — | — |
| 2 | CustContHdrPEOAllocationStatus | ALLOCATION_STATUS | — | — |
| 3 | CustContHdrPEOAllocationType | ALLOCATION_TYPE | — | — |
| 4 | CustContHdrPEOComments | COMMENTS | — | — |
| 5 | CustContHdrPEOContrCurTotalBilledAmt | CONTR_CUR_TOTAL_BILLED_AMT | — | — |
| 6 | CustContHdrPEOContrCurTotalRecogRevAmt | CONTR_CUR_TOTAL_RECOG_REV_AMT | — | — |
| 7 | CustContHdrPEOContrCurTransactionPrice | CONTR_CUR_TRANSACTION_PRICE | — | — |
| 8 | CustContHdrPEOContractClassificationCode | CONTRACT_CLASSIFICATION_CODE | — | — |
| 9 | CustContHdrPEOContractCurrencyCode | CONTRACT_CURRENCY_CODE | — | ✅ |
| 10 | CustContHdrPEOContractHashCode | CONTRACT_HASH_CODE | — | — |
| 11 | CustContHdrPEOContractPaymentAmount | CONTRACT_PAYMENT_AMOUNT | — | — |
| 12 | CustContHdrPEOContractRuleId | CONTRACT_RULE_ID | — | — |
| 13 | CustContHdrPEOCreatedFrom | CREATED_FROM | — | — |
| 14 | CustContHdrPEOCreationDate | CREATION_DATE | — | — |
| 15 | CustContHdrPEOCustomerContractDate | CUSTOMER_CONTRACT_DATE | — | — |
| 16 | CustContHdrPEOCustomerContractFreezeDate | CUSTOMER_CONTRACT_FREEZE_DATE | — | — |
| 17 | CustContHdrPEOCustomerContractHeaderId | CUSTOMER_CONTRACT_HEADER_ID | — | — |
| 18 | CustContHdrPEOCustomerContractNumber | CUSTOMER_CONTRACT_NUMBER | — | — |
| 19 | CustContHdrPEOEffectivityPeriodId | EFFECTIVITY_PERIOD_ID | — | — |
| 20 | CustContHdrPEOExchangeRate | EXCHANGE_RATE | — | — |
| 21 | CustContHdrPEOExchangeRateDate | EXCHANGE_RATE_DATE | — | — |
| 22 | CustContHdrPEOExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 23 | CustContHdrPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | CustContHdrPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 25 | CustContHdrPEOLedgerId | LEDGER_ID | — | — |
| 26 | CustContHdrPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 27 | CustContHdrPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 28 | CustContHdrPEOPaymentConfirmFlag | PAYMENT_CONFIRM_FLAG | — | — |
| 29 | CustContHdrPEOProcessedRequestId | PROCESSED_REQUEST_ID | — | — |
| 30 | CustContHdrPEOReference | REFERENCE | — | — |
| 31 | CustContHdrPEORequestId | REQUEST_ID | — | — |
| 32 | CustContHdrPEOReviewStatus | REVIEW_STATUS | — | — |
| 33 | CustContHdrPEOSingleObligationFlag | SINGLE_OBLIGATION_FLAG | — | — |
| 34 | CustContHdrPEOStandaloneSalesFlag | STANDALONE_SALES_FLAG | — | — |

### [[vrm_fmv_lines|VRM_FMV_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AboveRangeSspRuleCode | ABOVE_RANGE_SSP_RULE_CODE | — | — |
| 2 | BelowRangeSspRuleCode | BELOW_RANGE_SSP_RULE_CODE | — | — |
| 3 | DerivedPriceLinePEOEstablishedDate | ESTABLISHED_DATE | — | — |
| 4 | InRangeSspRuleCode | IN_RANGE_SSP_RULE_CODE | — | — |
| 5 | PriceLinePEOAttribute1 | ATTRIBUTE1 | — | — |
| 6 | PriceLinePEOAttribute10 | ATTRIBUTE10 | — | — |
| 7 | PriceLinePEOAttribute11 | ATTRIBUTE11 | — | — |
| 8 | PriceLinePEOAttribute12 | ATTRIBUTE12 | — | — |
| 9 | PriceLinePEOAttribute13 | ATTRIBUTE13 | — | — |
| 10 | PriceLinePEOAttribute14 | ATTRIBUTE14 | — | — |
| 11 | PriceLinePEOAttribute15 | ATTRIBUTE15 | — | — |
| 12 | PriceLinePEOAttribute16 | ATTRIBUTE16 | — | — |
| 13 | PriceLinePEOAttribute17 | ATTRIBUTE17 | — | — |
| 14 | PriceLinePEOAttribute18 | ATTRIBUTE18 | — | — |
| 15 | PriceLinePEOAttribute19 | ATTRIBUTE19 | — | — |
| 16 | PriceLinePEOAttribute2 | ATTRIBUTE2 | — | — |
| 17 | PriceLinePEOAttribute20 | ATTRIBUTE20 | — | — |
| 18 | PriceLinePEOAttribute3 | ATTRIBUTE3 | — | — |
| 19 | PriceLinePEOAttribute4 | ATTRIBUTE4 | — | — |
| 20 | PriceLinePEOAttribute5 | ATTRIBUTE5 | — | — |
| 21 | PriceLinePEOAttribute6 | ATTRIBUTE6 | — | — |
| 22 | PriceLinePEOAttribute7 | ATTRIBUTE7 | — | — |
| 23 | PriceLinePEOAttribute8 | ATTRIBUTE8 | — | — |
| 24 | PriceLinePEOAttribute9 | ATTRIBUTE9 | — | — |
| 25 | PriceLinePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 26 | PriceLinePEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 27 | PriceLinePEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 28 | PriceLinePEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 29 | PriceLinePEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 30 | PriceLinePEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 31 | PriceLinePEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 32 | PriceLinePEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 33 | PriceLinePEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 34 | PriceLinePEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 35 | PriceLinePEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 36 | PriceLinePEOAveragePrice | AVERAGE_PRICE | — | ✅ |
| 37 | PriceLinePEOComments | COMMENTS | — | — |
| 38 | PriceLinePEOCorpCurrencyFmValue | CORP_CURRENCY_FM_VALUE | — | — |
| 39 | PriceLinePEOCoverageEndDate | COVERAGE_END_DATE | — | — |
| 40 | PriceLinePEOCoverageStartDate | COVERAGE_START_DATE | — | — |
| 41 | PriceLinePEOCreationDate | CREATION_DATE | — | — |
| 42 | PriceLinePEOCurrencyCode | CURRENCY_CODE | — | — |
| 43 | PriceLinePEOElementType | ELEMENT_TYPE | — | — |
| 44 | PriceLinePEOEstablishedBy | ESTABLISHED_BY | — | — |
| 45 | PriceLinePEOExceptionAction | EXCEPTION_ACTION | — | — |
| 46 | PriceLinePEOExceptionComment | EXCEPTION_COMMENT | — | — |
| 47 | PriceLinePEOExceptionReason | EXCEPTION_REASON | — | — |
| 48 | PriceLinePEOExceptionType | EXCEPTION_TYPE | — | — |
| 49 | PriceLinePEOExchangeDate | EXCHANGE_DATE | — | — |
| 50 | PriceLinePEOExchangeRate | EXCHANGE_RATE | — | — |
| 51 | PriceLinePEOExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 52 | PriceLinePEOFairMarketValue | FAIR_MARKET_VALUE | — | ✅ |
| 53 | PriceLinePEOFmvLineId | FMV_LINE_ID | — | — |
| 54 | PriceLinePEOFmvLineSetId | FMV_LINE_SET_ID | — | — |
| 55 | PriceLinePEOFmvToleranceHighPct | FMV_TOLERANCE_HIGH_PCT | — | ✅ |
| 56 | PriceLinePEOFmvToleranceLowPct | FMV_TOLERANCE_LOW_PCT | — | ✅ |
| 57 | PriceLinePEOFmvType | FMV_TYPE | — | — |
| 58 | PriceLinePEOHighestPrice | HIGHEST_PRICE | — | ✅ |
| 59 | PriceLinePEOInventoryOrgId | INVENTORY_ORG_ID | — | — |
| 60 | PriceLinePEOItemType | ITEM_TYPE | — | — |
| 61 | PriceLinePEOItemTypeId | ITEM_TYPE_ID | — | — |
| 62 | PriceLinePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 63 | PriceLinePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 64 | PriceLinePEOLineCount | LINE_COUNT | — | ✅ |
| 65 | PriceLinePEOLineSource | LINE_SOURCE | — | — |
| 66 | PriceLinePEOLowestPrice | LOWEST_PRICE | — | ✅ |
| 67 | PriceLinePEOManuallyEnteredFlag | MANUALLY_ENTERED_FLAG | — | — |
| 68 | PriceLinePEOMinimumLineCount | MINIMUM_LINE_COUNT | — | — |
| 69 | PriceLinePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 70 | PriceLinePEOPriceEffPeriodId | PRICE_EFF_PERIOD_ID | — | — |
| 71 | PriceLinePEOPricingCombinationId | PRICING_COMBINATION_ID | — | — |
| 72 | PriceLinePEORequestId | REQUEST_ID | — | — |
| 73 | PriceLinePEOReviewReason | REVIEW_REASON | — | — |
| 74 | PriceLinePEOReviewStatus | REVIEW_STATUS | — | — |
| 75 | PriceLinePEOStandardDeviation | STANDARD_DEVIATION | — | ✅ |
| 76 | PriceLinePEOStatus | STATUS | — | — |
| 77 | PriceLinePEOTemplateId | TEMPLATE_ID | — | — |
| 78 | PriceLinePEOToleranceCoverage | TOLERANCE_COVERAGE | — | ✅ |
| 79 | PriceLinePEOToleranceCoverageCount | TOLERANCE_COVERAGE_COUNT | — | ✅ |
| 80 | PriceLinePEOTolerancePctRangeHigh | TOLERANCE_PCT_RANGE_HIGH | — | — |
| 81 | PriceLinePEOTolerancePctRangeLow | TOLERANCE_PCT_RANGE_LOW | — | — |
| 82 | PriceLinePEOToleranceRangeCoverage | TOLERANCE_RANGE_COVERAGE | — | ✅ |
| 83 | PriceLinePEOTotalAmount | TOTAL_AMOUNT | — | ✅ |
| 84 | PriceLinePEOTotalQuantity | TOTAL_QUANTITY | — | ✅ |
| 85 | PriceLinePEOUomCode | UOM_CODE | — | — |
| 86 | PriceLinePEOUsedInCompliance | USED_IN_COMPLIANCE | — | — |
| 87 | PriceLinePEOValueReason | VALUE_REASON | — | — |
| 88 | PriceLinePEOVsoeValueStatus | VSOE_VALUE_STATUS | — | — |
| 89 | PublishedSalesPoint | PUBLISHED_SALES_POINT | — | — |
| 90 | SspHigh | SSP_HIGH | — | — |
| 91 | SspLow | SSP_LOW | — | — |
| 92 | SspMid | SSP_MID | — | — |
| 93 | SspRangeTolerancePercent | SSP_RANGE_TOLERANCE_PERCENT | — | — |

### [[vrm_fmv_templates_b|VRM_FMV_TEMPLATES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FMVTemplateBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | FMVTemplateBasePEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 3 | FMVTemplateBasePEOTemplateId | TEMPLATE_ID | — | — |

### [[vrm_perf_obligations|VRM_PERF_OBLIGATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsSspPo | ABS_SSP_PO | — | ✅ |
| 2 | PerfObligationId | PERF_OBLIGATION_ID | 🔑 | ✅ |
| 3 | PerfObligationsBasePrice | BASE_PRICE | — | ✅ |
| 4 | PerfObligationsBasePricePercentage | BASE_PRICE_PERCENTAGE | — | ✅ |
| 5 | PerfObligationsComments | COMMENTS | — | ✅ |
| 6 | PerfObligationsContrCurCrLiabilityAmt | CONTR_CUR_CR_LIABILITY_AMT | — | ✅ |
| 7 | PerfObligationsContrCurDrAssetAmt | CONTR_CUR_DR_ASSET_AMT | — | ✅ |
| 8 | PerfObligationsContrCurDrDiscountAmt | CONTR_CUR_DR_DISCOUNT_AMT | — | ✅ |
| 9 | PerfObligationsContrCurFmvAmt | CONTR_CUR_FMV_AMT | — | ✅ |
| 10 | PerfObligationsContrCurNetLineAmt | CONTR_CUR_NET_LINE_AMT | — | ✅ |
| 11 | PerfObligationsContrCurTotAllocAmt | CONTR_CUR_TOT_ALLOC_AMT | — | ✅ |
| 12 | PerfObligationsContrCurTotCarveOutAmt | CONTR_CUR_TOT_CARVE_OUT_AMT | — | ✅ |
| 13 | PerfObligationsContrCurTotNetConsiderAmt | CONTR_CUR_TOT_NET_CONSIDER_AMT | — | ✅ |
| 14 | PerfObligationsContrCurTotVarConsiderAmt | CONTR_CUR_TOT_VAR_CONSIDER_AMT | — | — |
| 15 | PerfObligationsContrCurTotalBilledAmt | CONTR_CUR_TOTAL_BILLED_AMT | — | ✅ |
| 16 | PerfObligationsContrCurTotalRecogRevAmt | CONTR_CUR_TOTAL_RECOG_REV_AMT | — | ✅ |
| 17 | PerfObligationsCostAmount | COST_AMOUNT | — | ✅ |
| 18 | PerfObligationsCreatedBy1 | CREATED_BY | — | ✅ |
| 19 | PerfObligationsCreatedFrom | CREATED_FROM | — | — |
| 20 | PerfObligationsCreationDate | CREATION_DATE | — | ✅ |
| 21 | PerfObligationsCustomerContractHeaderId | CUSTOMER_CONTRACT_HEADER_ID | — | — |
| 22 | PerfObligationsDiscardFlag | DISCARD_FLAG | — | ✅ |
| 23 | PerfObligationsDiscountAmount | DISCOUNT_AMOUNT | — | ✅ |
| 24 | PerfObligationsDiscountPercentage | DISCOUNT_PERCENTAGE | — | ✅ |
| 25 | PerfObligationsExchangeRate | EXCHANGE_RATE | — | — |
| 26 | PerfObligationsExchangeRateDate | EXCHANGE_RATE_DATE | — | — |
| 27 | PerfObligationsExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 28 | PerfObligationsExemptFromAllocationFlag | EXEMPT_FROM_ALLOCATION_FLAG | — | ✅ |
| 29 | PerfObligationsFirstSatisfactionEventDate | FIRST_SATISFACTION_EVENT_DATE | — | — |
| 30 | PerfObligationsFmvLineId | FMV_LINE_ID | — | ✅ |
| 31 | PerfObligationsFmvTemplateId | FMV_TEMPLATE_ID | — | — |
| 32 | PerfObligationsGrossMarginPercentage | GROSS_MARGIN_PERCENTAGE | — | ✅ |
| 33 | PerfObligationsImplPerfObligTemplateId | IMPL_PERF_OBLIG_TEMPLATE_ID | — | — |
| 34 | PerfObligationsInitialPerfEvtCreatedFlag | INITIAL_PERF_EVT_CREATED_FLAG | — | ✅ |
| 35 | PerfObligationsInitialPerfEvtExpectedDate | INITIAL_PERF_EVT_EXPECTED_DATE | — | ✅ |
| 36 | PerfObligationsInitialPerfEvtRecordedFlag | INITIAL_PERF_EVT_RECORDED_FLAG | — | ✅ |
| 37 | PerfObligationsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 38 | PerfObligationsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 39 | PerfObligationsLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 40 | PerfObligationsLatestRevisionIntentCode | LATEST_REVISION_INTENT_CODE | — | ✅ |
| 41 | PerfObligationsLatestVersionDate | LATEST_VERSION_DATE | — | ✅ |
| 42 | PerfObligationsLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 43 | PerfObligationsListPriceAmount | LIST_PRICE_AMOUNT | — | ✅ |
| 44 | PerfObligationsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 45 | PerfObligationsObligCurFmvAmt | OBLIG_CUR_FMV_AMT | — | ✅ |
| 46 | PerfObligationsObligCurNetLineAmt | OBLIG_CUR_NET_LINE_AMT | — | ✅ |
| 47 | PerfObligationsObligCurNetSalesPrice | OBLIG_CUR_NET_SALES_PRICE | — | ✅ |
| 48 | PerfObligationsObligCurTotAllocAmt | OBLIG_CUR_TOT_ALLOC_AMT | — | ✅ |
| 49 | PerfObligationsObligCurTotCarveOutAmt | OBLIG_CUR_TOT_CARVE_OUT_AMT | — | ✅ |
| 50 | PerfObligationsObligCurTotNetConsiderAmt | OBLIG_CUR_TOT_NET_CONSIDER_AMT | — | ✅ |
| 51 | PerfObligationsObligCurTotVarConsiderAmt | OBLIG_CUR_TOT_VAR_CONSIDER_AMT | — | — |
| 52 | PerfObligationsObligCurTotalBilledAmt | OBLIG_CUR_TOTAL_BILLED_AMT | — | ✅ |
| 53 | PerfObligationsObligCurTotalRecogRevAmt | OBLIG_CUR_TOTAL_RECOG_REV_AMT | — | ✅ |
| 54 | PerfObligationsObligCurrencyCode | OBLIG_CURRENCY_CODE | — | ✅ |
| 55 | PerfObligationsObligHashCode | OBLIG_HASH_CODE | — | — |
| 56 | PerfObligationsObligPaymentAmount | OBLIG_PAYMENT_AMOUNT | — | — |
| 57 | PerfObligationsObligationReference | OBLIGATION_REFERENCE | — | ✅ |
| 58 | PerfObligationsPerfObligClassificationCode | PERF_OBLIG_CLASSIFICATION_CODE | — | ✅ |
| 59 | PerfObligationsPerfObligFreezeFlag | PERF_OBLIG_FREEZE_FLAG | — | ✅ |
| 60 | PerfObligationsPerfObligationGroupRuleId | PERF_OBLIGATION_GROUP_RULE_ID | — | — |
| 61 | PerfObligationsPerfObligationNumber | PERF_OBLIGATION_NUMBER | — | ✅ |
| 62 | PerfObligationsPerfObligationTemplateId | PERF_OBLIGATION_TEMPLATE_ID | — | — |
| 63 | PerfObligationsPerfObligationType | PERF_OBLIGATION_TYPE | — | ✅ |
| 64 | PerfObligationsPricingCombinationId | PRICING_COMBINATION_ID | — | — |
| 65 | PerfObligationsRemovedFlag | REMOVED_FLAG | — | ✅ |
| 66 | PerfObligationsRequestId | REQUEST_ID | — | — |
| 67 | PerfObligationsSatisfactionDate | SATISFACTION_DATE | — | ✅ |
| 68 | PerfObligationsSatisfactionMethod | SATISFACTION_METHOD | — | ✅ |
| 69 | PerfObligationsSubstantialDistCreatedFlag | SUBSTANTIAL_DIST_CREATED_FLAG | — | — |
| 70 | PerfObligationsUnitSellingPrice | UNIT_SELLING_PRICE | — | ✅ |
| 71 | PoSspRangeRuleCode | PO_SSP_RANGE_RULE_CODE | — | ✅ |
| 72 | PoSspRuleResultCode | PO_SSP_RULE_RESULT_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
