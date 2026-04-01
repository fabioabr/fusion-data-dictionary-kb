---
id: DOC-OTHER-PVO-PerfObligationLinesPVO
doc_type: system-doc
title: "PerfObligationLinesPVO — PVO Cross-Module"
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
  - PerfObligationLinesPVO
  - perfobligationlinespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PerfObligationLinesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Perf Obligation Lines. Acessa as tabelas: GL_LEDGERS, PER_PERSON_NAMES_F_V, PER_USERS (+7).

**Caminho:** `FscmTopModelAM.FinVrmRRSharedPublicModelAM.PerfObligationLinesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 414 | 10 | 1 | 106 | 26% |

---

## 🔗 Tabelas Relacionadas

- [[gl_ledgers|GL_LEDGERS]] — 6 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos
- [[per_users|PER_USERS]] — 8 atributos
- [[vrm_customer_contract_headers|VRM_CUSTOMER_CONTRACT_HEADERS]] — 67 atributos (2 BICC)
- [[vrm_fmv_lines|VRM_FMV_LINES]] — 95 atributos (14 BICC)
- [[vrm_fmv_templates_b|VRM_FMV_TEMPLATES_B]] — 3 atributos
- [[vrm_perf_obligations|VRM_PERF_OBLIGATIONS]] — 100 atributos (30 BICC)
- [[vrm_perf_obligation_lines|VRM_PERF_OBLIGATION_LINES]] — 109 atributos (1 PKs, 52 BICC)
- [[vrm_pricing_lines|VRM_PRICING_LINES]] — 11 atributos (8 BICC)
- [[vrm_source_doc_lines|VRM_SOURCE_DOC_LINES]] — 5 atributos

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
| 1 | PerfObligPersonCreatedByDisplayName | DISPLAY_NAME | — | — |
| 2 | PerfObligPersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PerfObligPersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PerfObligPersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PerfObligPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PerfObligPersonUpdatedByDisplayName | DISPLAY_NAME | — | — |
| 7 | PerfObligPersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PerfObligPersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | PerfObligPersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | PerfObligPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerfObligUserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | PerfObligUserCreatedByPersonId | PERSON_ID | — | — |
| 3 | PerfObligUserCreatedByUserId | USER_ID | — | — |
| 4 | PerfObligUserCreatedByUsername | USERNAME | — | — |
| 5 | PerfObligUserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | PerfObligUserUpdatedByPersonId | PERSON_ID | — | — |
| 7 | PerfObligUserUpdatedByUserId | USER_ID | — | — |
| 8 | PerfObligUserUpdatedByUsername | USERNAME | — | — |

### [[vrm_customer_contract_headers|VRM_CUSTOMER_CONTRACT_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustomerContractHeadersAllocationRequestId | ALLOCATION_REQUEST_ID | — | — |
| 2 | CustomerContractHeadersAllocationStatus | ALLOCATION_STATUS | — | — |
| 3 | CustomerContractHeadersAllocationType | ALLOCATION_TYPE | — | — |
| 4 | CustomerContractHeadersAttribute102 | ATTRIBUTE10 | — | — |
| 5 | CustomerContractHeadersAttribute112 | ATTRIBUTE1 | — | — |
| 6 | CustomerContractHeadersAttribute113 | ATTRIBUTE11 | — | — |
| 7 | CustomerContractHeadersAttribute122 | ATTRIBUTE12 | — | — |
| 8 | CustomerContractHeadersAttribute132 | ATTRIBUTE13 | — | — |
| 9 | CustomerContractHeadersAttribute142 | ATTRIBUTE14 | — | — |
| 10 | CustomerContractHeadersAttribute152 | ATTRIBUTE15 | — | — |
| 11 | CustomerContractHeadersAttribute162 | ATTRIBUTE16 | — | — |
| 12 | CustomerContractHeadersAttribute172 | ATTRIBUTE17 | — | — |
| 13 | CustomerContractHeadersAttribute182 | ATTRIBUTE18 | — | — |
| 14 | CustomerContractHeadersAttribute192 | ATTRIBUTE19 | — | — |
| 15 | CustomerContractHeadersAttribute202 | ATTRIBUTE20 | — | — |
| 16 | CustomerContractHeadersAttribute22 | ATTRIBUTE2 | — | — |
| 17 | CustomerContractHeadersAttribute32 | ATTRIBUTE3 | — | — |
| 18 | CustomerContractHeadersAttribute42 | ATTRIBUTE4 | — | — |
| 19 | CustomerContractHeadersAttribute52 | ATTRIBUTE5 | — | — |
| 20 | CustomerContractHeadersAttribute62 | ATTRIBUTE6 | — | — |
| 21 | CustomerContractHeadersAttribute72 | ATTRIBUTE7 | — | — |
| 22 | CustomerContractHeadersAttribute82 | ATTRIBUTE8 | — | — |
| 23 | CustomerContractHeadersAttribute92 | ATTRIBUTE9 | — | — |
| 24 | CustomerContractHeadersAttributeCategory2 | ATTRIBUTE_CATEGORY | — | — |
| 25 | CustomerContractHeadersAttributeDate12 | ATTRIBUTE_DATE1 | — | — |
| 26 | CustomerContractHeadersAttributeDate22 | ATTRIBUTE_DATE2 | — | — |
| 27 | CustomerContractHeadersAttributeDate32 | ATTRIBUTE_DATE3 | — | — |
| 28 | CustomerContractHeadersAttributeDate42 | ATTRIBUTE_DATE4 | — | — |
| 29 | CustomerContractHeadersAttributeDate52 | ATTRIBUTE_DATE5 | — | — |
| 30 | CustomerContractHeadersAttributeNumber12 | ATTRIBUTE_NUMBER1 | — | — |
| 31 | CustomerContractHeadersAttributeNumber22 | ATTRIBUTE_NUMBER2 | — | — |
| 32 | CustomerContractHeadersAttributeNumber32 | ATTRIBUTE_NUMBER3 | — | — |
| 33 | CustomerContractHeadersAttributeNumber42 | ATTRIBUTE_NUMBER4 | — | — |
| 34 | CustomerContractHeadersAttributeNumber52 | ATTRIBUTE_NUMBER5 | — | — |
| 35 | CustomerContractHeadersComments2 | COMMENTS | — | — |
| 36 | CustomerContractHeadersContrCurTotalBilledAmt1 | CONTR_CUR_TOTAL_BILLED_AMT | — | — |
| 37 | CustomerContractHeadersContrCurTotalRecogRevAmt1 | CONTR_CUR_TOTAL_RECOG_REV_AMT | — | — |
| 38 | CustomerContractHeadersContrCurTransactionPrice | CONTR_CUR_TRANSACTION_PRICE | — | — |
| 39 | CustomerContractHeadersContractClassificationCode | CONTRACT_CLASSIFICATION_CODE | — | — |
| 40 | CustomerContractHeadersContractCurrencyCode | CONTRACT_CURRENCY_CODE | — | ✅ |
| 41 | CustomerContractHeadersContractHashCode | CONTRACT_HASH_CODE | — | — |
| 42 | CustomerContractHeadersContractPaymentAmount | CONTRACT_PAYMENT_AMOUNT | — | — |
| 43 | CustomerContractHeadersContractRuleId | CONTRACT_RULE_ID | — | — |
| 44 | CustomerContractHeadersCreatedBy2 | CREATED_BY | — | — |
| 45 | CustomerContractHeadersCreatedFrom2 | CREATED_FROM | — | — |
| 46 | CustomerContractHeadersCreationDate2 | CREATION_DATE | — | — |
| 47 | CustomerContractHeadersCustomerContractDate | CUSTOMER_CONTRACT_DATE | — | — |
| 48 | CustomerContractHeadersCustomerContractFreezeDate | CUSTOMER_CONTRACT_FREEZE_DATE | — | — |
| 49 | CustomerContractHeadersCustomerContractHeaderId2 | CUSTOMER_CONTRACT_HEADER_ID | — | — |
| 50 | CustomerContractHeadersCustomerContractNumber | CUSTOMER_CONTRACT_NUMBER | — | — |
| 51 | CustomerContractHeadersEffectivityPeriodId | EFFECTIVITY_PERIOD_ID | — | — |
| 52 | CustomerContractHeadersExchangeRate2 | EXCHANGE_RATE | — | — |
| 53 | CustomerContractHeadersExchangeRateDate2 | EXCHANGE_RATE_DATE | — | — |
| 54 | CustomerContractHeadersExchangeRateType2 | EXCHANGE_RATE_TYPE | — | — |
| 55 | CustomerContractHeadersLastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 56 | CustomerContractHeadersLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 57 | CustomerContractHeadersLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 58 | CustomerContractHeadersLedgerId1 | LEDGER_ID | — | — |
| 59 | CustomerContractHeadersLegalEntityId1 | LEGAL_ENTITY_ID | — | — |
| 60 | CustomerContractHeadersObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 61 | CustomerContractHeadersPaymentConfirmFlag | PAYMENT_CONFIRM_FLAG | — | — |
| 62 | CustomerContractHeadersProcessedRequestId | PROCESSED_REQUEST_ID | — | — |
| 63 | CustomerContractHeadersReference | REFERENCE | — | — |
| 64 | CustomerContractHeadersRequestId2 | REQUEST_ID | — | — |
| 65 | CustomerContractHeadersReviewStatus | REVIEW_STATUS | — | — |
| 66 | CustomerContractHeadersSingleObligationFlag | SINGLE_OBLIGATION_FLAG | — | — |
| 67 | CustomerContractHeadersStandaloneSalesFlag1 | STANDALONE_SALES_FLAG | — | — |

### [[vrm_fmv_lines|VRM_FMV_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AboveRangeSspRuleCode | ABOVE_RANGE_SSP_RULE_CODE | — | — |
| 2 | BelowRangeSspRuleCode | BELOW_RANGE_SSP_RULE_CODE | — | — |
| 3 | InRangeSspRuleCode | IN_RANGE_SSP_RULE_CODE | — | — |
| 4 | PriceLinePEOAttribute1018 | ATTRIBUTE10 | — | — |
| 5 | PriceLinePEOAttribute1102 | ATTRIBUTE1 | — | — |
| 6 | PriceLinePEOAttribute1122 | ATTRIBUTE11 | — | — |
| 7 | PriceLinePEOAttribute1220 | ATTRIBUTE12 | — | — |
| 8 | PriceLinePEOAttribute1318 | ATTRIBUTE13 | — | — |
| 9 | PriceLinePEOAttribute1418 | ATTRIBUTE14 | — | — |
| 10 | PriceLinePEOAttribute1518 | ATTRIBUTE15 | — | — |
| 11 | PriceLinePEOAttribute1616 | ATTRIBUTE16 | — | — |
| 12 | PriceLinePEOAttribute1716 | ATTRIBUTE17 | — | — |
| 13 | PriceLinePEOAttribute1816 | ATTRIBUTE18 | — | — |
| 14 | PriceLinePEOAttribute1916 | ATTRIBUTE19 | — | — |
| 15 | PriceLinePEOAttribute2016 | ATTRIBUTE20 | — | — |
| 16 | PriceLinePEOAttribute229 | ATTRIBUTE2 | — | — |
| 17 | PriceLinePEOAttribute318 | ATTRIBUTE3 | — | — |
| 18 | PriceLinePEOAttribute418 | ATTRIBUTE4 | — | — |
| 19 | PriceLinePEOAttribute518 | ATTRIBUTE5 | — | — |
| 20 | PriceLinePEOAttribute618 | ATTRIBUTE6 | — | — |
| 21 | PriceLinePEOAttribute718 | ATTRIBUTE7 | — | — |
| 22 | PriceLinePEOAttribute818 | ATTRIBUTE8 | — | — |
| 23 | PriceLinePEOAttribute918 | ATTRIBUTE9 | — | — |
| 24 | PriceLinePEOAttributeCategory18 | ATTRIBUTE_CATEGORY | — | — |
| 25 | PriceLinePEOAttributeDate127 | ATTRIBUTE_DATE1 | — | — |
| 26 | PriceLinePEOAttributeDate216 | ATTRIBUTE_DATE2 | — | — |
| 27 | PriceLinePEOAttributeDate316 | ATTRIBUTE_DATE3 | — | — |
| 28 | PriceLinePEOAttributeDate416 | ATTRIBUTE_DATE4 | — | — |
| 29 | PriceLinePEOAttributeDate516 | ATTRIBUTE_DATE5 | — | — |
| 30 | PriceLinePEOAttributeNumber127 | ATTRIBUTE_NUMBER1 | — | — |
| 31 | PriceLinePEOAttributeNumber216 | ATTRIBUTE_NUMBER2 | — | — |
| 32 | PriceLinePEOAttributeNumber316 | ATTRIBUTE_NUMBER3 | — | — |
| 33 | PriceLinePEOAttributeNumber416 | ATTRIBUTE_NUMBER4 | — | — |
| 34 | PriceLinePEOAttributeNumber516 | ATTRIBUTE_NUMBER5 | — | — |
| 35 | PriceLinePEOAveragePrice | AVERAGE_PRICE | — | ✅ |
| 36 | PriceLinePEOComments6 | COMMENTS | — | — |
| 37 | PriceLinePEOCorpCurrencyFmValue | CORP_CURRENCY_FM_VALUE | — | — |
| 38 | PriceLinePEOCoverageEndDate | COVERAGE_END_DATE | — | — |
| 39 | PriceLinePEOCoverageStartDate | COVERAGE_START_DATE | — | — |
| 40 | PriceLinePEOCreatedBy18 | CREATED_BY | — | — |
| 41 | PriceLinePEOCreationDate | CREATION_DATE | — | — |
| 42 | PriceLinePEOCurrencyCode3 | CURRENCY_CODE | — | ✅ |
| 43 | PriceLinePEOElementType1 | ELEMENT_TYPE | — | — |
| 44 | PriceLinePEOEstablishedBy | ESTABLISHED_BY | — | — |
| 45 | PriceLinePEOEstablishedDate | ESTABLISHED_DATE | — | — |
| 46 | PriceLinePEOExceptionAction | EXCEPTION_ACTION | — | — |
| 47 | PriceLinePEOExceptionComment | EXCEPTION_COMMENT | — | — |
| 48 | PriceLinePEOExceptionReason | EXCEPTION_REASON | — | — |
| 49 | PriceLinePEOExceptionType | EXCEPTION_TYPE | — | — |
| 50 | PriceLinePEOExchangeDate2 | EXCHANGE_DATE | — | — |
| 51 | PriceLinePEOExchangeRate5 | EXCHANGE_RATE | — | — |
| 52 | PriceLinePEOExchangeRateType5 | EXCHANGE_RATE_TYPE | — | — |
| 53 | PriceLinePEOFairMarketValue | FAIR_MARKET_VALUE | — | ✅ |
| 54 | PriceLinePEOFmvLineId2 | FMV_LINE_ID | — | — |
| 55 | PriceLinePEOFmvLineSetId1 | FMV_LINE_SET_ID | — | — |
| 56 | PriceLinePEOFmvToleranceHighPct | FMV_TOLERANCE_HIGH_PCT | — | ✅ |
| 57 | PriceLinePEOFmvToleranceLowPct | FMV_TOLERANCE_LOW_PCT | — | ✅ |
| 58 | PriceLinePEOFmvType | FMV_TYPE | — | — |
| 59 | PriceLinePEOHighestPrice | HIGHEST_PRICE | — | ✅ |
| 60 | PriceLinePEOInventoryOrgId1 | INVENTORY_ORG_ID | — | — |
| 61 | PriceLinePEOItemType | ITEM_TYPE | — | — |
| 62 | PriceLinePEOItemTypeId | ITEM_TYPE_ID | — | — |
| 63 | PriceLinePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 64 | PriceLinePEOLastUpdateLogin18 | LAST_UPDATE_LOGIN | — | — |
| 65 | PriceLinePEOLastUpdatedBy18 | LAST_UPDATED_BY | — | — |
| 66 | PriceLinePEOLineCount | LINE_COUNT | — | ✅ |
| 67 | PriceLinePEOLineSource2 | LINE_SOURCE | — | — |
| 68 | PriceLinePEOLowestPrice | LOWEST_PRICE | — | ✅ |
| 69 | PriceLinePEOManuallyEnteredFlag | MANUALLY_ENTERED_FLAG | — | — |
| 70 | PriceLinePEOMinimumLineCount | MINIMUM_LINE_COUNT | — | — |
| 71 | PriceLinePEOObjectVersionNumber12 | OBJECT_VERSION_NUMBER | — | — |
| 72 | PriceLinePEOPriceEffPeriodId2 | PRICE_EFF_PERIOD_ID | — | — |
| 73 | PriceLinePEOPricingCombinationId2 | PRICING_COMBINATION_ID | — | — |
| 74 | PriceLinePEORequestId7 | REQUEST_ID | — | — |
| 75 | PriceLinePEOReviewReason | REVIEW_REASON | — | — |
| 76 | PriceLinePEOReviewStatus1 | REVIEW_STATUS | — | — |
| 77 | PriceLinePEOStandardDeviation | STANDARD_DEVIATION | — | ✅ |
| 78 | PriceLinePEOStatus8 | STATUS | — | — |
| 79 | PriceLinePEOTemplateId1 | TEMPLATE_ID | — | — |
| 80 | PriceLinePEOToleranceCoverage | TOLERANCE_COVERAGE | — | ✅ |
| 81 | PriceLinePEOToleranceCoverageCount | TOLERANCE_COVERAGE_COUNT | — | ✅ |
| 82 | PriceLinePEOTolerancePctRangeHigh | TOLERANCE_PCT_RANGE_HIGH | — | — |
| 83 | PriceLinePEOTolerancePctRangeLow | TOLERANCE_PCT_RANGE_LOW | — | — |
| 84 | PriceLinePEOToleranceRangeCoverage | TOLERANCE_RANGE_COVERAGE | — | ✅ |
| 85 | PriceLinePEOTotalAmount | TOTAL_AMOUNT | — | ✅ |
| 86 | PriceLinePEOTotalQuantity | TOTAL_QUANTITY | — | ✅ |
| 87 | PriceLinePEOUomCode2 | UOM_CODE | — | — |
| 88 | PriceLinePEOUsedInCompliance | USED_IN_COMPLIANCE | — | — |
| 89 | PriceLinePEOValueReason | VALUE_REASON | — | — |
| 90 | PriceLinePEOVsoeValueStatus | VSOE_VALUE_STATUS | — | — |
| 91 | PublishedSalesPoint | PUBLISHED_SALES_POINT | — | — |
| 92 | SspHigh | SSP_HIGH | — | — |
| 93 | SspLow | SSP_LOW | — | — |
| 94 | SspMid | SSP_MID | — | — |
| 95 | SspRangeTolerancePercent | SSP_RANGE_TOLERANCE_PERCENT | — | — |

### [[vrm_fmv_templates_b|VRM_FMV_TEMPLATES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FMVTemplateBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | FMVTemplateBasePEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 3 | FMVTemplateBasePEOTemplateId | TEMPLATE_ID | — | — |

### [[vrm_perf_obligations|VRM_PERF_OBLIGATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerfObligationsAttribute101 | ATTRIBUTE10 | — | — |
| 2 | PerfObligationsAttribute110 | ATTRIBUTE1 | — | — |
| 3 | PerfObligationsAttribute111 | ATTRIBUTE11 | — | — |
| 4 | PerfObligationsAttribute121 | ATTRIBUTE12 | — | — |
| 5 | PerfObligationsAttribute131 | ATTRIBUTE13 | — | — |
| 6 | PerfObligationsAttribute141 | ATTRIBUTE14 | — | — |
| 7 | PerfObligationsAttribute151 | ATTRIBUTE15 | — | — |
| 8 | PerfObligationsAttribute161 | ATTRIBUTE16 | — | — |
| 9 | PerfObligationsAttribute171 | ATTRIBUTE17 | — | — |
| 10 | PerfObligationsAttribute181 | ATTRIBUTE18 | — | — |
| 11 | PerfObligationsAttribute191 | ATTRIBUTE19 | — | — |
| 12 | PerfObligationsAttribute201 | ATTRIBUTE20 | — | — |
| 13 | PerfObligationsAttribute21 | ATTRIBUTE2 | — | — |
| 14 | PerfObligationsAttribute31 | ATTRIBUTE3 | — | — |
| 15 | PerfObligationsAttribute41 | ATTRIBUTE4 | — | — |
| 16 | PerfObligationsAttribute51 | ATTRIBUTE5 | — | — |
| 17 | PerfObligationsAttribute61 | ATTRIBUTE6 | — | — |
| 18 | PerfObligationsAttribute71 | ATTRIBUTE7 | — | — |
| 19 | PerfObligationsAttribute81 | ATTRIBUTE8 | — | — |
| 20 | PerfObligationsAttribute91 | ATTRIBUTE9 | — | — |
| 21 | PerfObligationsAttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 22 | PerfObligationsAttributeDate11 | ATTRIBUTE_DATE1 | — | — |
| 23 | PerfObligationsAttributeDate21 | ATTRIBUTE_DATE2 | — | — |
| 24 | PerfObligationsAttributeDate31 | ATTRIBUTE_DATE3 | — | — |
| 25 | PerfObligationsAttributeDate41 | ATTRIBUTE_DATE4 | — | — |
| 26 | PerfObligationsAttributeDate51 | ATTRIBUTE_DATE5 | — | — |
| 27 | PerfObligationsAttributeNumber11 | ATTRIBUTE_NUMBER1 | — | — |
| 28 | PerfObligationsAttributeNumber21 | ATTRIBUTE_NUMBER2 | — | — |
| 29 | PerfObligationsAttributeNumber31 | ATTRIBUTE_NUMBER3 | — | — |
| 30 | PerfObligationsAttributeNumber41 | ATTRIBUTE_NUMBER4 | — | — |
| 31 | PerfObligationsAttributeNumber51 | ATTRIBUTE_NUMBER5 | — | — |
| 32 | PerfObligationsBasePrice | BASE_PRICE | — | ✅ |
| 33 | PerfObligationsBasePricePercentage | BASE_PRICE_PERCENTAGE | — | ✅ |
| 34 | PerfObligationsComments1 | COMMENTS | — | ✅ |
| 35 | PerfObligationsContrCurCrLiabilityAmt | CONTR_CUR_CR_LIABILITY_AMT | — | — |
| 36 | PerfObligationsContrCurDrAssetAmt | CONTR_CUR_DR_ASSET_AMT | — | — |
| 37 | PerfObligationsContrCurDrDiscountAmt | CONTR_CUR_DR_DISCOUNT_AMT | — | — |
| 38 | PerfObligationsContrCurFmvAmt1 | CONTR_CUR_FMV_AMT | — | — |
| 39 | PerfObligationsContrCurNetLineAmt1 | CONTR_CUR_NET_LINE_AMT | — | — |
| 40 | PerfObligationsContrCurTotAllocAmt | CONTR_CUR_TOT_ALLOC_AMT | — | — |
| 41 | PerfObligationsContrCurTotCarveOutAmt | CONTR_CUR_TOT_CARVE_OUT_AMT | — | — |
| 42 | PerfObligationsContrCurTotNetConsiderAmt | CONTR_CUR_TOT_NET_CONSIDER_AMT | — | — |
| 43 | PerfObligationsContrCurTotVarConsiderAmt | CONTR_CUR_TOT_VAR_CONSIDER_AMT | — | — |
| 44 | PerfObligationsContrCurTotalBilledAmt | CONTR_CUR_TOTAL_BILLED_AMT | — | — |
| 45 | PerfObligationsContrCurTotalRecogRevAmt | CONTR_CUR_TOTAL_RECOG_REV_AMT | — | — |
| 46 | PerfObligationsCostAmount | COST_AMOUNT | — | — |
| 47 | PerfObligationsCreatedBy | CREATED_BY | — | ✅ |
| 48 | PerfObligationsCreatedFrom1 | CREATED_FROM | — | — |
| 49 | PerfObligationsCreationDate1 | CREATION_DATE | — | ✅ |
| 50 | PerfObligationsCustomerContractHeaderId1 | CUSTOMER_CONTRACT_HEADER_ID | — | — |
| 51 | PerfObligationsDiscardFlag1 | DISCARD_FLAG | — | ✅ |
| 52 | PerfObligationsDiscountAmount | DISCOUNT_AMOUNT | — | — |
| 53 | PerfObligationsDiscountPercentage | DISCOUNT_PERCENTAGE | — | ✅ |
| 54 | PerfObligationsExchangeRate1 | EXCHANGE_RATE | — | — |
| 55 | PerfObligationsExchangeRateDate1 | EXCHANGE_RATE_DATE | — | — |
| 56 | PerfObligationsExchangeRateType1 | EXCHANGE_RATE_TYPE | — | — |
| 57 | PerfObligationsExemptFromAllocationFlag | EXEMPT_FROM_ALLOCATION_FLAG | — | ✅ |
| 58 | PerfObligationsFmvLineId1 | FMV_LINE_ID | — | ✅ |
| 59 | PerfObligationsFmvTemplateId | FMV_TEMPLATE_ID | — | — |
| 60 | PerfObligationsGrossMarginPercentage | GROSS_MARGIN_PERCENTAGE | — | ✅ |
| 61 | PerfObligationsImplPerfObligTemplateId | IMPL_PERF_OBLIG_TEMPLATE_ID | — | — |
| 62 | PerfObligationsInitialPerfEvtCreatedFlag | INITIAL_PERF_EVT_CREATED_FLAG | — | ✅ |
| 63 | PerfObligationsInitialPerfEvtExpectedDate | INITIAL_PERF_EVT_EXPECTED_DATE | — | ✅ |
| 64 | PerfObligationsInitialPerfEvtRecordedFlag | INITIAL_PERF_EVT_RECORDED_FLAG | — | ✅ |
| 65 | PerfObligationsLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 66 | PerfObligationsLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 67 | PerfObligationsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 68 | PerfObligationsLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 69 | PerfObligationsListPriceAmount | LIST_PRICE_AMOUNT | — | — |
| 70 | PerfObligationsObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 71 | PerfObligationsObligCurFmvAmt | OBLIG_CUR_FMV_AMT | — | — |
| 72 | PerfObligationsObligCurNetLineAmt | OBLIG_CUR_NET_LINE_AMT | — | — |
| 73 | PerfObligationsObligCurNetSalesPrice | OBLIG_CUR_NET_SALES_PRICE | — | ✅ |
| 74 | PerfObligationsObligCurTotAllocAmt | OBLIG_CUR_TOT_ALLOC_AMT | — | — |
| 75 | PerfObligationsObligCurTotCarveOutAmt | OBLIG_CUR_TOT_CARVE_OUT_AMT | — | — |
| 76 | PerfObligationsObligCurTotNetConsiderAmt | OBLIG_CUR_TOT_NET_CONSIDER_AMT | — | — |
| 77 | PerfObligationsObligCurTotVarConsiderAmt | OBLIG_CUR_TOT_VAR_CONSIDER_AMT | — | — |
| 78 | PerfObligationsObligCurTotalBilledAmt | OBLIG_CUR_TOTAL_BILLED_AMT | — | — |
| 79 | PerfObligationsObligCurTotalRecogRevAmt | OBLIG_CUR_TOTAL_RECOG_REV_AMT | — | — |
| 80 | PerfObligationsObligCurrencyCode | OBLIG_CURRENCY_CODE | — | ✅ |
| 81 | PerfObligationsObligHashCode | OBLIG_HASH_CODE | — | — |
| 82 | PerfObligationsObligPaymentAmount | OBLIG_PAYMENT_AMOUNT | — | — |
| 83 | PerfObligationsObligationReference | OBLIGATION_REFERENCE | — | ✅ |
| 84 | PerfObligationsPerfObligClassificationCode | PERF_OBLIG_CLASSIFICATION_CODE | — | ✅ |
| 85 | PerfObligationsPerfObligFreezeFlag | PERF_OBLIG_FREEZE_FLAG | — | ✅ |
| 86 | PerfObligationsPerfObligationGroupRuleId | PERF_OBLIGATION_GROUP_RULE_ID | — | — |
| 87 | PerfObligationsPerfObligationId1 | PERF_OBLIGATION_ID | — | ✅ |
| 88 | PerfObligationsPerfObligationNumber | PERF_OBLIGATION_NUMBER | — | ✅ |
| 89 | PerfObligationsPerfObligationTemplateId | PERF_OBLIGATION_TEMPLATE_ID | — | — |
| 90 | PerfObligationsPerfObligationType | PERF_OBLIGATION_TYPE | — | ✅ |
| 91 | PerfObligationsPricingCombinationId1 | PRICING_COMBINATION_ID | — | — |
| 92 | PerfObligationsRemovedFlag1 | REMOVED_FLAG | — | ✅ |
| 93 | PerfObligationsRequestId1 | REQUEST_ID | — | — |
| 94 | PerfObligationsSatisfactionDate | SATISFACTION_DATE | — | ✅ |
| 95 | PerfObligationsSatisfactionMethod | SATISFACTION_METHOD | — | ✅ |
| 96 | PerfObligationsSatisfactionStatus | SATISFACTION_STATUS | — | ✅ |
| 97 | PerfObligationsSubstantialDistCreatedFlag | SUBSTANTIAL_DIST_CREATED_FLAG | — | — |
| 98 | PerfObligationsUnitSellingPrice | UNIT_SELLING_PRICE | — | ✅ |
| 99 | PoSspRangeRuleCode | PO_SSP_RANGE_RULE_CODE | — | ✅ |
| 100 | PoSspRuleResultCode | PO_SSP_RULE_RESULT_CODE | — | ✅ |

### [[vrm_perf_obligation_lines|VRM_PERF_OBLIGATION_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsSspPol | ABS_SSP_POL | — | ✅ |
| 2 | PerfObligationLineId | PERF_OBLIGATION_LINE_ID | 🔑 | ✅ |
| 3 | PerfObligationLinesAllocationRequiredFlag | ALLOCATION_REQUIRED_FLAG | — | ✅ |
| 4 | PerfObligationLinesAttribute1 | ATTRIBUTE1 | — | — |
| 5 | PerfObligationLinesAttribute10 | ATTRIBUTE10 | — | — |
| 6 | PerfObligationLinesAttribute11 | ATTRIBUTE11 | — | — |
| 7 | PerfObligationLinesAttribute12 | ATTRIBUTE12 | — | — |
| 8 | PerfObligationLinesAttribute13 | ATTRIBUTE13 | — | — |
| 9 | PerfObligationLinesAttribute14 | ATTRIBUTE14 | — | — |
| 10 | PerfObligationLinesAttribute15 | ATTRIBUTE15 | — | — |
| 11 | PerfObligationLinesAttribute16 | ATTRIBUTE16 | — | — |
| 12 | PerfObligationLinesAttribute17 | ATTRIBUTE17 | — | — |
| 13 | PerfObligationLinesAttribute18 | ATTRIBUTE18 | — | — |
| 14 | PerfObligationLinesAttribute19 | ATTRIBUTE19 | — | — |
| 15 | PerfObligationLinesAttribute2 | ATTRIBUTE2 | — | — |
| 16 | PerfObligationLinesAttribute20 | ATTRIBUTE20 | — | — |
| 17 | PerfObligationLinesAttribute3 | ATTRIBUTE3 | — | — |
| 18 | PerfObligationLinesAttribute4 | ATTRIBUTE4 | — | — |
| 19 | PerfObligationLinesAttribute5 | ATTRIBUTE5 | — | — |
| 20 | PerfObligationLinesAttribute6 | ATTRIBUTE6 | — | — |
| 21 | PerfObligationLinesAttribute7 | ATTRIBUTE7 | — | — |
| 22 | PerfObligationLinesAttribute8 | ATTRIBUTE8 | — | — |
| 23 | PerfObligationLinesAttribute9 | ATTRIBUTE9 | — | — |
| 24 | PerfObligationLinesAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 25 | PerfObligationLinesAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 26 | PerfObligationLinesAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 27 | PerfObligationLinesAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 28 | PerfObligationLinesAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 29 | PerfObligationLinesAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 30 | PerfObligationLinesAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 31 | PerfObligationLinesAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 32 | PerfObligationLinesAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 33 | PerfObligationLinesAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 34 | PerfObligationLinesAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 35 | PerfObligationLinesAutomaticConfirmationPeriod | AUTOMATIC_CONFIRMATION_PERIOD | — | — |
| 36 | PerfObligationLinesBuId | BU_ID | — | — |
| 37 | PerfObligationLinesComments | COMMENTS | — | ✅ |
| 38 | PerfObligationLinesContrCurAllocatedAmt | CONTR_CUR_ALLOCATED_AMT | — | ✅ |
| 39 | PerfObligationLinesContrCurBilledAmt | CONTR_CUR_BILLED_AMT | — | ✅ |
| 40 | PerfObligationLinesContrCurCarveOutAmt | CONTR_CUR_CARVE_OUT_AMT | — | ✅ |
| 41 | PerfObligationLinesContrCurFmvAmt | CONTR_CUR_FMV_AMT | — | ✅ |
| 42 | PerfObligationLinesContrCurNetConsiderAmt | CONTR_CUR_NET_CONSIDER_AMT | — | ✅ |
| 43 | PerfObligationLinesContrCurNetLineAmt | CONTR_CUR_NET_LINE_AMT | — | ✅ |
| 44 | PerfObligationLinesContrCurRecogRevAmt | CONTR_CUR_RECOG_REV_AMT | — | ✅ |
| 45 | PerfObligationLinesContrCurVarConsiderAmt | CONTR_CUR_VAR_CONSIDER_AMT | — | — |
| 46 | PerfObligationLinesCreatedBy | CREATED_BY | — | — |
| 47 | PerfObligationLinesCreatedFrom | CREATED_FROM | — | — |
| 48 | PerfObligationLinesCreationDate | CREATION_DATE | — | — |
| 49 | PerfObligationLinesCustomerContractHeaderId | CUSTOMER_CONTRACT_HEADER_ID | — | — |
| 50 | PerfObligationLinesDiscardFlag | DISCARD_FLAG | — | ✅ |
| 51 | PerfObligationLinesDocumentLineId | DOCUMENT_LINE_ID | — | ✅ |
| 52 | PerfObligationLinesEnteredCurAllocatedAmt | ENTERED_CUR_ALLOCATED_AMT | — | ✅ |
| 53 | PerfObligationLinesEnteredCurBilledAmt | ENTERED_CUR_BILLED_AMT | — | ✅ |
| 54 | PerfObligationLinesEnteredCurCarveOutAmt | ENTERED_CUR_CARVE_OUT_AMT | — | ✅ |
| 55 | PerfObligationLinesEnteredCurFmvAmt | ENTERED_CUR_FMV_AMT | — | ✅ |
| 56 | PerfObligationLinesEnteredCurNetConsiderAmt | ENTERED_CUR_NET_CONSIDER_AMT | — | ✅ |
| 57 | PerfObligationLinesEnteredCurRecogRevAmt | ENTERED_CUR_RECOG_REV_AMT | — | ✅ |
| 58 | PerfObligationLinesEnteredCurVarConsiderAmt | ENTERED_CUR_VAR_CONSIDER_AMT | — | — |
| 59 | PerfObligationLinesExchangeRate | EXCHANGE_RATE | — | ✅ |
| 60 | PerfObligationLinesExchangeRateDate | EXCHANGE_RATE_DATE | — | ✅ |
| 61 | PerfObligationLinesExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 62 | PerfObligationLinesFmvLineId | FMV_LINE_ID | — | ✅ |
| 63 | PerfObligationLinesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 64 | PerfObligationLinesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 65 | PerfObligationLinesLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 66 | PerfObligationLinesLatestRevisionIntentCode | LATEST_REVISION_INTENT_CODE | — | ✅ |
| 67 | PerfObligationLinesLatestVersionDate | LATEST_VERSION_DATE | — | ✅ |
| 68 | PerfObligationLinesLedgerId | LEDGER_ID | — | — |
| 69 | PerfObligationLinesLineCurrencyCode | LINE_CURRENCY_CODE | — | ✅ |
| 70 | PerfObligationLinesLineSatisfactionDate | LINE_SATISFACTION_DATE | — | ✅ |
| 71 | PerfObligationLinesLineSatisfactionStatus | LINE_SATISFACTION_STATUS | — | ✅ |
| 72 | PerfObligationLinesLineSource | LINE_SOURCE | — | ✅ |
| 73 | PerfObligationLinesMissingRevInformationFlag | MISSING_REV_INFORMATION_FLAG | — | ✅ |
| 74 | PerfObligationLinesMoveToContrNumber | MOVE_TO_CONTR_NUMBER | — | — |
| 75 | PerfObligationLinesMoveToObligNumber | MOVE_TO_OBLIG_NUMBER | — | — |
| 76 | PerfObligationLinesNetLineAmt | NET_LINE_AMT | — | ✅ |
| 77 | PerfObligationLinesNetQuantity | NET_QUANTITY | — | — |
| 78 | PerfObligationLinesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 79 | PerfObligationLinesParentPerfObligLineId | PARENT_PERF_OBLIG_LINE_ID | — | ✅ |
| 80 | PerfObligationLinesPaymentAmount | PAYMENT_AMOUNT | — | ✅ |
| 81 | PerfObligationLinesPerfObligationId | PERF_OBLIGATION_ID | — | — |
| 82 | PerfObligationLinesPerfObligationLineNumber | PERF_OBLIGATION_LINE_NUMBER | — | ✅ |
| 83 | PerfObligationLinesPricingCombinationId | PRICING_COMBINATION_ID | — | — |
| 84 | PerfObligationLinesRemovedBy | REMOVED_BY | — | ✅ |
| 85 | PerfObligationLinesRemovedDate | REMOVED_DATE | — | ✅ |
| 86 | PerfObligationLinesRemovedFlag | REMOVED_FLAG | — | ✅ |
| 87 | PerfObligationLinesRemovedRequestId | REMOVED_REQUEST_ID | — | — |
| 88 | PerfObligationLinesReprocessLineEventsFlag | REPROCESS_LINE_EVENTS_FLAG | — | — |
| 89 | PerfObligationLinesRequestId | REQUEST_ID | — | — |
| 90 | PerfObligationLinesRevRecProcesdDocLineId | REV_REC_PROCESD_DOC_LINE_ID | — | — |
| 91 | PerfObligationLinesRevRecProcesdRevEndDate | REV_REC_PROCESD_REV_END_DATE | — | ✅ |
| 92 | PerfObligationLinesRevRecProcesdRevRuleDur | REV_REC_PROCESD_REV_RULE_DUR | — | ✅ |
| 93 | PerfObligationLinesRevRecProcesdRevRuleId | REV_REC_PROCESD_REV_RULE_ID | — | ✅ |
| 94 | PerfObligationLinesRevRecProcesdRevStartDate | REV_REC_PROCESD_REV_START_DATE | — | ✅ |
| 95 | PerfObligationLinesRevRecProcessedFlag | REV_REC_PROCESSED_FLAG | — | ✅ |
| 96 | PerfObligationLinesRevRecReprocessStatusCode | REV_REC_REPROCESS_STATUS_CODE | — | ✅ |
| 97 | PerfObligationLinesRevenueEndDate | REVENUE_END_DATE | — | ✅ |
| 98 | PerfObligationLinesRevenueRuleDuration | REVENUE_RULE_DURATION | — | ✅ |
| 99 | PerfObligationLinesRevenueRuleId | REVENUE_RULE_ID | — | — |
| 100 | PerfObligationLinesRevenueStartDate | REVENUE_START_DATE | — | ✅ |
| 101 | PerfObligationLinesSatisfactionBaseProportion | SATISFACTION_BASE_PROPORTION | — | ✅ |
| 102 | PerfObligationLinesSatisfactionConfirmFlag | SATISFACTION_CONFIRM_FLAG | — | — |
| 103 | PerfObligationLinesSatisfactionMeasurementModel | SATISFACTION_MEASUREMENT_MODEL | — | ✅ |
| 104 | PerfObligationLinesSeCreatedFromSublineFlag | SE_CREATED_FROM_SUBLINE_FLAG | — | — |
| 105 | PerfObligationLinesStandaloneSalesFlag | STANDALONE_SALES_FLAG | — | ✅ |
| 106 | PolSspRangeRuleCode | POL_SSP_RANGE_RULE_CODE | — | ✅ |
| 107 | PolSspRuleResultCode | POL_SSP_RULE_RESULT_CODE | — | ✅ |
| 108 | ServiceDuration | SERVICE_DURATION | — | — |
| 109 | ServiceUom | SERVICE_UOM | — | — |

### [[vrm_pricing_lines|VRM_PRICING_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PricingLinesDocumentLineId | DOCUMENT_LINE_ID | — | — |
| 2 | PricingLinesItemType | ITEM_TYPE | — | — |
| 3 | PricingLinesItemTypeId | ITEM_TYPE_ID | — | — |
| 4 | PricingLinesLatestPeriodActionCode | LATEST_PERIOD_ACTION_CODE | — | ✅ |
| 5 | PricingLinesLatestReversalDays | LATEST_REVERSAL_DAYS | — | ✅ |
| 6 | PricingLinesRevisedRecurPatternCode | REVISED_RECUR_PATTERN_CODE | — | ✅ |
| 7 | PricingLinesRevisedRecurringAmount | REVISED_RECURRING_AMOUNT | — | ✅ |
| 8 | PricingLinesRevisedRecurringFlag | REVISED_RECURRING_FLAG | — | ✅ |
| 9 | PricingLinesRevisedRecurringFrequency | REVISED_RECURRING_FREQUENCY | — | ✅ |
| 10 | PricingLinesRevisedTerminationDate | REVISED_TERMINATION_DATE | — | ✅ |
| 11 | PricingLinesTotalReversalDays | TOTAL_REVERSAL_DAYS | — | ✅ |

### [[vrm_source_doc_lines|VRM_SOURCE_DOC_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SourceDocLinesDocumentLineId | DOCUMENT_LINE_ID | — | — |
| 2 | SourceDocLinesInventoryOrgId | INVENTORY_ORG_ID | — | — |
| 3 | SourceDocLinesItemId | ITEM_ID | — | — |
| 4 | SourceDocLinesMemoLineSeqId | MEMO_LINE_SEQ_ID | — | — |
| 5 | SourceDocLinesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
