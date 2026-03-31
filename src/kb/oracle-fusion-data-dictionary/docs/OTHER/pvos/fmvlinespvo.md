---
id: DOC-OTHER-PVO-FmvLinesPVO
doc_type: system-doc
title: "FmvLinesPVO — PVO Cross-Module"
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
  - FmvLinesPVO
  - fmvlinespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FmvLinesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fmv Lines. Acessa as tabelas: PER_PERSON_NAMES_F_V, PER_USERS, VRM_FMV_LINES (+1).

**Caminho:** `FscmTopModelAM.FinVrmRCSharedPublicModelAM.FmvLinesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 78 | 4 | 1 | 53 | 68% |

---

## 🔗 Tabelas Relacionadas

- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 8 atributos (2 BICC)
- [[per_users|PER_USERS]] — 4 atributos
- [[vrm_fmv_lines|VRM_FMV_LINES]] — 64 atributos (1 PKs, 51 BICC)
- [[vrm_fmv_templates_b|VRM_FMV_TEMPLATES_B]] — 2 atributos

---

## ⚙️ Atributos

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | — |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 5 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | — |
| 6 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 8 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UserCreatedByUserId | USER_ID | — | — |
| 3 | UserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | UserUpdatedByUserId | USER_ID | — | — |

### [[vrm_fmv_lines|VRM_FMV_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AboveRangeSspRuleCode | ABOVE_RANGE_SSP_RULE_CODE | — | ✅ |
| 2 | BelowRangeSspRuleCode | BELOW_RANGE_SSP_RULE_CODE | — | ✅ |
| 3 | FmvLineId | FMV_LINE_ID | 🔑 | ✅ |
| 4 | InRangeSspRuleCode | IN_RANGE_SSP_RULE_CODE | — | ✅ |
| 5 | PriceLineAveragePrice | AVERAGE_PRICE | — | ✅ |
| 6 | PriceLineComments | COMMENTS | — | ✅ |
| 7 | PriceLineCorpCurrencyFmValue | CORP_CURRENCY_FM_VALUE | — | ✅ |
| 8 | PriceLineCoverageEndDate | COVERAGE_END_DATE | — | ✅ |
| 9 | PriceLineCoverageStartDate | COVERAGE_START_DATE | — | ✅ |
| 10 | PriceLineCreatedByUserId | CREATED_BY | — | ✅ |
| 11 | PriceLineCreationDate | CREATION_DATE | — | ✅ |
| 12 | PriceLineCurrencyCode | CURRENCY_CODE | — | ✅ |
| 13 | PriceLineElementType | ELEMENT_TYPE | — | ✅ |
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
| 24 | PriceLineFmvLineSetId | FMV_LINE_SET_ID | — | — |
| 25 | PriceLineFmvToleranceHighPct | FMV_TOLERANCE_HIGH_PCT | — | ✅ |
| 26 | PriceLineFmvToleranceLowPct | FMV_TOLERANCE_LOW_PCT | — | ✅ |
| 27 | PriceLineFmvType | FMV_TYPE | — | ✅ |
| 28 | PriceLineHighestPrice | HIGHEST_PRICE | — | ✅ |
| 29 | PriceLineInventoryOrgId | INVENTORY_ORG_ID | — | — |
| 30 | PriceLineItemType | ITEM_TYPE | — | ✅ |
| 31 | PriceLineItemTypeId | ITEM_TYPE_ID | — | — |
| 32 | PriceLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 33 | PriceLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 34 | PriceLineLastUpdatedByUserId | LAST_UPDATED_BY | — | ✅ |
| 35 | PriceLineLineCount | LINE_COUNT | — | ✅ |
| 36 | PriceLineLineSource | LINE_SOURCE | — | ✅ |
| 37 | PriceLineLowestPrice | LOWEST_PRICE | — | ✅ |
| 38 | PriceLineManuallyEnteredFlag | MANUALLY_ENTERED_FLAG | — | ✅ |
| 39 | PriceLineMinimumLineCount | MINIMUM_LINE_COUNT | — | — |
| 40 | PriceLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 41 | PriceLinePriceEffPeriodId | PRICE_EFF_PERIOD_ID | — | — |
| 42 | PriceLinePricingCombinationId | PRICING_COMBINATION_ID | — | — |
| 43 | PriceLineRequestId | REQUEST_ID | — | — |
| 44 | PriceLineReviewReason | REVIEW_REASON | — | ✅ |
| 45 | PriceLineReviewStatus | REVIEW_STATUS | — | ✅ |
| 46 | PriceLineStandardDeviation | STANDARD_DEVIATION | — | ✅ |
| 47 | PriceLineStatus | STATUS | — | — |
| 48 | PriceLineTemplateId | TEMPLATE_ID | — | — |
| 49 | PriceLineToleranceCoverage | TOLERANCE_COVERAGE | — | ✅ |
| 50 | PriceLineToleranceCoverageCount | TOLERANCE_COVERAGE_COUNT | — | ✅ |
| 51 | PriceLineTolerancePctRangeHigh | TOLERANCE_PCT_RANGE_HIGH | — | ✅ |
| 52 | PriceLineTolerancePctRangeLow | TOLERANCE_PCT_RANGE_LOW | — | ✅ |
| 53 | PriceLineToleranceRangeCoverage | TOLERANCE_RANGE_COVERAGE | — | ✅ |
| 54 | PriceLineTotalAmount | TOTAL_AMOUNT | — | ✅ |
| 55 | PriceLineTotalQuantity | TOTAL_QUANTITY | — | ✅ |
| 56 | PriceLineUomCode | UOM_CODE | — | ✅ |
| 57 | PriceLineUsedInCompliance | USED_IN_COMPLIANCE | — | ✅ |
| 58 | PriceLineValueReason | VALUE_REASON | — | ✅ |
| 59 | PriceLineVsoeValueStatus | VSOE_VALUE_STATUS | — | ✅ |
| 60 | PublishedSalesPoint | PUBLISHED_SALES_POINT | — | ✅ |
| 61 | SspHigh | SSP_HIGH | — | ✅ |
| 62 | SspLow | SSP_LOW | — | ✅ |
| 63 | SspMid | SSP_MID | — | ✅ |
| 64 | SspRangeTolerancePercent | SSP_RANGE_TOLERANCE_PERCENT | — | ✅ |

### [[vrm_fmv_templates_b|VRM_FMV_TEMPLATES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FMVTemplateBaseStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 2 | FMVTemplateBaseTemplateId | TEMPLATE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
