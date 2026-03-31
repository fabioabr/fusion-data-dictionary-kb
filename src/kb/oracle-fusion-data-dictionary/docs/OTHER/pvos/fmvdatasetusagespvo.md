---
id: DOC-OTHER-PVO-FmvDataSetUsagesPVO
doc_type: system-doc
title: "FmvDataSetUsagesPVO — PVO Cross-Module"
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
  - FmvDataSetUsagesPVO
  - fmvdatasetusagespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FmvDataSetUsagesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fmv Data Set Usages. Acessa as tabelas: PER_PERSON_NAMES_F_V, VRM_FMV_DATA_SET_USAGES, VRM_FMV_LINES (+3).

**Caminho:** `FscmTopModelAM.FinVrmRCSharedPublicModelAM.FmvDataSetUsagesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 117 | 6 | 1 | 71 | 61% |

---

## 🔗 Tabelas Relacionadas

- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 16 atributos (4 BICC)
- [[vrm_fmv_data_set_usages|VRM_FMV_DATA_SET_USAGES]] — 30 atributos (1 PKs, 22 BICC)
- [[vrm_fmv_lines|VRM_FMV_LINES]] — 65 atributos (45 BICC)
- [[vrm_fmv_templates_b|VRM_FMV_TEMPLATES_B]] — 2 atributos
- [[vrm_perf_obligations|VRM_PERF_OBLIGATIONS]] — 2 atributos
- [[vrm_perf_obligation_lines|VRM_PERF_OBLIGATION_LINES]] — 2 atributos

---

## ⚙️ Atributos

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DataSetUsagesCreatedBy | DISPLAY_NAME | — | ✅ |
| 2 | DataSetUsagesEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | DataSetUsagesEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | DataSetUsagesLastUpdatedBy | DISPLAY_NAME | — | ✅ |
| 5 | DataSetUsagesPersonNameId | PERSON_NAME_ID | — | — |
| 6 | DataSetUsagesPersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | DataSetUsagesPersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 8 | DataSetUsagesPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |
| 9 | PriceLineCreatedBy | DISPLAY_NAME | — | ✅ |
| 10 | PriceLineLastUpdatedBy | DISPLAY_NAME | — | ✅ |
| 11 | PriceLinePersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 12 | PriceLinePersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 13 | PriceLinePersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 14 | PriceLinePersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 15 | PriceLinePersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 16 | PriceLinePersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[vrm_fmv_data_set_usages|VRM_FMV_DATA_SET_USAGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DataSetUsagesBasePrice | BASE_PRICE | — | ✅ |
| 2 | DataSetUsagesComments | COMMENTS | — | ✅ |
| 3 | DataSetUsagesCreatedBy1 | CREATED_BY | — | ✅ |
| 4 | DataSetUsagesCreationDate | CREATION_DATE | — | ✅ |
| 5 | DataSetUsagesCustomerContractNumber | CUSTOMER_CONTRACT_NUMBER | — | ✅ |
| 6 | DataSetUsagesDataSetType | DATA_SET_TYPE | — | — |
| 7 | DataSetUsagesDocumentLineId | DOCUMENT_LINE_ID | — | — |
| 8 | DataSetUsagesExcludedBy | EXCLUDED_BY | — | ✅ |
| 9 | DataSetUsagesExclusionReasonCode | EXCLUSION_REASON_CODE | — | ✅ |
| 10 | DataSetUsagesExclusionStatus | EXCLUSION_STATUS | — | ✅ |
| 11 | DataSetUsagesFmvLineId | FMV_LINE_ID | — | — |
| 12 | DataSetUsagesFmvLineSetId | FMV_LINE_SET_ID | — | — |
| 13 | DataSetUsagesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | DataSetUsagesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | DataSetUsagesLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 16 | DataSetUsagesNetDiscountAmount | NET_DISCOUNT_AMOUNT | — | ✅ |
| 17 | DataSetUsagesNetDiscountPercent | NET_DISCOUNT_PERCENT | — | ✅ |
| 18 | DataSetUsagesNetLineAmount | NET_LINE_AMOUNT | — | ✅ |
| 19 | DataSetUsagesNetQuantity | NET_QUANTITY | — | ✅ |
| 20 | DataSetUsagesNetUnitSalesPctBasePrice | NET_UNIT_SALES_PCT_BASE_PRICE | — | ✅ |
| 21 | DataSetUsagesNetUnitSalesPrice | NET_UNIT_SALES_PRICE | — | ✅ |
| 22 | DataSetUsagesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | DataSetUsagesPerfObligationId | PERF_OBLIGATION_ID | — | ✅ |
| 24 | DataSetUsagesPerfObligationLineId | PERF_OBLIGATION_LINE_ID | — | ✅ |
| 25 | DataSetUsagesPriceBasisDataSetId | PRICE_BASIS_DATA_SET_ID | — | — |
| 26 | DataSetUsagesRequestId | REQUEST_ID | — | — |
| 27 | DataSetUsagesRevisedCost | REVISED_COST | — | ✅ |
| 28 | DataSetUsagesRevisedGrossMarginPercent | REVISED_GROSS_MARGIN_PERCENT | — | ✅ |
| 29 | DataSetUsagesRevisedUom | REVISED_UOM | — | ✅ |
| 30 | FmvDataSetUsageId | FMV_DATA_SET_USAGE_ID | 🔑 | ✅ |

### [[vrm_fmv_lines|VRM_FMV_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AboveRangeSspRuleCode | ABOVE_RANGE_SSP_RULE_CODE | — | ✅ |
| 2 | BelowRangeSspRuleCode | BELOW_RANGE_SSP_RULE_CODE | — | ✅ |
| 3 | InRangeSspRuleCode | IN_RANGE_SSP_RULE_CODE | — | ✅ |
| 4 | PriceLineAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 5 | PriceLineAveragePrice | AVERAGE_PRICE | — | ✅ |
| 6 | PriceLineComments | COMMENTS | — | — |
| 7 | PriceLineCorpCurrencyFmValue | CORP_CURRENCY_FM_VALUE | — | — |
| 8 | PriceLineCoverageEndDate | COVERAGE_END_DATE | — | ✅ |
| 9 | PriceLineCoverageStartDate | COVERAGE_START_DATE | — | ✅ |
| 10 | PriceLineCreatedByUserId | CREATED_BY | — | ✅ |
| 11 | PriceLineCreationDate | CREATION_DATE | — | ✅ |
| 12 | PriceLineCurrencyCode | CURRENCY_CODE | — | ✅ |
| 13 | PriceLineElementType | ELEMENT_TYPE | — | — |
| 14 | PriceLineEstablishedBy | ESTABLISHED_BY | — | ✅ |
| 15 | PriceLineEstablishedDate | ESTABLISHED_DATE | — | ✅ |
| 16 | PriceLineExceptionAction | EXCEPTION_ACTION | — | — |
| 17 | PriceLineExceptionComment | EXCEPTION_COMMENT | — | ✅ |
| 18 | PriceLineExceptionReason | EXCEPTION_REASON | — | ✅ |
| 19 | PriceLineExceptionType | EXCEPTION_TYPE | — | — |
| 20 | PriceLineExchangeDate | EXCHANGE_DATE | — | ✅ |
| 21 | PriceLineExchangeRate | EXCHANGE_RATE | — | ✅ |
| 22 | PriceLineExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 23 | PriceLineFairMarketValue | FAIR_MARKET_VALUE | — | ✅ |
| 24 | PriceLineFmvLineId | FMV_LINE_ID | — | ✅ |
| 25 | PriceLineFmvLineSetId | FMV_LINE_SET_ID | — | — |
| 26 | PriceLineFmvToleranceHighPct | FMV_TOLERANCE_HIGH_PCT | — | ✅ |
| 27 | PriceLineFmvToleranceLowPct | FMV_TOLERANCE_LOW_PCT | — | ✅ |
| 28 | PriceLineFmvType | FMV_TYPE | — | ✅ |
| 29 | PriceLineHighestPrice | HIGHEST_PRICE | — | ✅ |
| 30 | PriceLineInventoryOrgId | INVENTORY_ORG_ID | — | — |
| 31 | PriceLineItemType | ITEM_TYPE | — | — |
| 32 | PriceLineItemTypeId | ITEM_TYPE_ID | — | — |
| 33 | PriceLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | PriceLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 35 | PriceLineLastUpdatedByUserId | LAST_UPDATED_BY | — | ✅ |
| 36 | PriceLineLineCount | LINE_COUNT | — | ✅ |
| 37 | PriceLineLineSource | LINE_SOURCE | — | ✅ |
| 38 | PriceLineLowestPrice | LOWEST_PRICE | — | ✅ |
| 39 | PriceLineManuallyEnteredFlag | MANUALLY_ENTERED_FLAG | — | ✅ |
| 40 | PriceLineMinimumLineCount | MINIMUM_LINE_COUNT | — | — |
| 41 | PriceLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 42 | PriceLinePriceEffPeriodId | PRICE_EFF_PERIOD_ID | — | — |
| 43 | PriceLinePricingCombinationId | PRICING_COMBINATION_ID | — | — |
| 44 | PriceLineRequestId | REQUEST_ID | — | — |
| 45 | PriceLineReviewReason | REVIEW_REASON | — | ✅ |
| 46 | PriceLineReviewStatus | REVIEW_STATUS | — | ✅ |
| 47 | PriceLineStandardDeviation | STANDARD_DEVIATION | — | ✅ |
| 48 | PriceLineStatus | STATUS | — | — |
| 49 | PriceLineTemplateId | TEMPLATE_ID | — | — |
| 50 | PriceLineToleranceCoverage | TOLERANCE_COVERAGE | — | ✅ |
| 51 | PriceLineToleranceCoverageCount | TOLERANCE_COVERAGE_COUNT | — | ✅ |
| 52 | PriceLineTolerancePctRangeHigh | TOLERANCE_PCT_RANGE_HIGH | — | — |
| 53 | PriceLineTolerancePctRangeLow | TOLERANCE_PCT_RANGE_LOW | — | — |
| 54 | PriceLineToleranceRangeCoverage | TOLERANCE_RANGE_COVERAGE | — | ✅ |
| 55 | PriceLineTotalAmount | TOTAL_AMOUNT | — | ✅ |
| 56 | PriceLineTotalQuantity | TOTAL_QUANTITY | — | ✅ |
| 57 | PriceLineUomCode | UOM_CODE | — | ✅ |
| 58 | PriceLineUsedInCompliance | USED_IN_COMPLIANCE | — | ✅ |
| 59 | PriceLineValueReason | VALUE_REASON | — | ✅ |
| 60 | PriceLineVsoeValueStatus | VSOE_VALUE_STATUS | — | ✅ |
| 61 | PublishedSalesPoint | PUBLISHED_SALES_POINT | — | ✅ |
| 62 | SspHigh | SSP_HIGH | — | ✅ |
| 63 | SspLow | SSP_LOW | — | ✅ |
| 64 | SspMid | SSP_MID | — | ✅ |
| 65 | SspRangeTolerancePercent | SSP_RANGE_TOLERANCE_PERCENT | — | ✅ |

### [[vrm_fmv_templates_b|VRM_FMV_TEMPLATES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FMVTemplateBaseStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 2 | FMVTemplateBaseTemplateId | TEMPLATE_ID | — | — |

### [[vrm_perf_obligations|VRM_PERF_OBLIGATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerfObligationsPEOPerfObligationId | PERF_OBLIGATION_ID | — | — |
| 2 | PerfObligationsPEOPerfObligationNumber | PERF_OBLIGATION_NUMBER | — | — |

### [[vrm_perf_obligation_lines|VRM_PERF_OBLIGATION_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerfObligationLinesEOPerfObligationLineId | PERF_OBLIGATION_LINE_ID | — | — |
| 2 | PerfObligationLinesEOPerfObligationLineNumber | PERF_OBLIGATION_LINE_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
