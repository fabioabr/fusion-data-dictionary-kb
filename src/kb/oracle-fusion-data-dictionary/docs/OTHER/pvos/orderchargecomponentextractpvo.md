---
id: DOC-OTHER-PVO-OrderChargeComponentExtractPVO
doc_type: system-doc
title: "OrderChargeComponentExtractPVO — PVO Cross-Module"
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
  - OrderChargeComponentExtractPVO
  - orderchargecomponentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OrderChargeComponentExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Order Charge Component Extract. Acessa as tabelas: DOO_ORDER_CHARGE_COMPONENTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.OrderChargeComponentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 36 | 1 | 1 | 34 | 94% |

---

## 🔗 Tabelas Relacionadas

- [[doo_order_charge_components|DOO_ORDER_CHARGE_COMPONENTS]] — 36 atributos (1 PKs, 34 BICC)

---

## ⚙️ Atributos

### [[doo_order_charge_components|DOO_ORDER_CHARGE_COMPONENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrderChargeComponentChargeCurrDurationExtAmt | CHARGE_CURR_DURATION_EXT_AMT | — | ✅ |
| 2 | OrderChargeComponentChargeCurrencyCode | CHARGE_CURRENCY_CODE | — | ✅ |
| 3 | OrderChargeComponentChargeCurrencyExtAmount | CHARGE_CURRENCY_EXT_AMOUNT | — | ✅ |
| 4 | OrderChargeComponentChargeCurrencyUnitPrice | CHARGE_CURRENCY_UNIT_PRICE | — | ✅ |
| 5 | OrderChargeComponentCreatedBy | CREATED_BY | — | ✅ |
| 6 | OrderChargeComponentCreationDate | CREATION_DATE | — | ✅ |
| 7 | OrderChargeComponentDeltaType | DELTA_TYPE | — | ✅ |
| 8 | OrderChargeComponentExplanation | EXPLANATION | — | ✅ |
| 9 | OrderChargeComponentExplanationMessageName | EXPLANATION_MESSAGE_NAME | — | ✅ |
| 10 | OrderChargeComponentHeaderCurrDurationExtAmt | HEADER_CURR_DURATION_EXT_AMT | — | ✅ |
| 11 | OrderChargeComponentHeaderCurrencyCode | HEADER_CURRENCY_CODE | — | ✅ |
| 12 | OrderChargeComponentHeaderCurrencyExtAmount | HEADER_CURRENCY_EXT_AMOUNT | — | ✅ |
| 13 | OrderChargeComponentHeaderCurrencyUnitPrice | HEADER_CURRENCY_UNIT_PRICE | — | ✅ |
| 14 | OrderChargeComponentId | ORDER_CHARGE_COMPONENT_ID | 🔑 | ✅ |
| 15 | OrderChargeComponentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | OrderChargeComponentLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | OrderChargeComponentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | OrderChargeComponentModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 19 | OrderChargeComponentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 20 | OrderChargeComponentOrderChargeId | ORDER_CHARGE_ID | — | ✅ |
| 21 | OrderChargeComponentParentChargeComponentId | PARENT_CHARGE_COMPONENT_ID | — | ✅ |
| 22 | OrderChargeComponentPercentOfComparisonElement | PERCENT_OF_COMPARISON_ELEMENT | — | ✅ |
| 23 | OrderChargeComponentPriceElementCode | PRICE_ELEMENT_CODE | — | ✅ |
| 24 | OrderChargeComponentPriceElementUsageCode | PRICE_ELEMENT_USAGE_CODE | — | ✅ |
| 25 | OrderChargeComponentPricingSourceId | PRICING_SOURCE_ID | — | ✅ |
| 26 | OrderChargeComponentPricingSourceTypeCode | PRICING_SOURCE_TYPE_CODE | — | ✅ |
| 27 | OrderChargeComponentPromotionId | PROMOTION_ID | — | — |
| 28 | OrderChargeComponentPromotionLineId | PROMOTION_LINE_ID | — | — |
| 29 | OrderChargeComponentReferenceOrderChargeCompId | REFERENCE_ORDER_CHARGE_COMP_ID | — | ✅ |
| 30 | OrderChargeComponentRollupFlag | ROLLUP_FLAG | — | ✅ |
| 31 | OrderChargeComponentSequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 32 | OrderChargeComponentSourceChargeComponentId | SOURCE_CHARGE_COMPONENT_ID | — | ✅ |
| 33 | OrderChargeComponentSourceChargeId | SOURCE_CHARGE_ID | — | ✅ |
| 34 | OrderChargeComponentSourceMpaId | SOURCE_MPA_ID | — | ✅ |
| 35 | OrderChargeComponentSourceParentChargeCompId | SOURCE_PARENT_CHARGE_COMP_ID | — | ✅ |
| 36 | OrderChargeComponentTaxIncludedFlag | TAX_INCLUDED_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
