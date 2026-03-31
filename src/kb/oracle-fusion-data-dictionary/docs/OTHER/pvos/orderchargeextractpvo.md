---
id: DOC-OTHER-PVO-OrderChargeExtractPVO
doc_type: system-doc
title: "OrderChargeExtractPVO — PVO Cross-Module"
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
  - OrderChargeExtractPVO
  - orderchargeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OrderChargeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Order Charge Extract. Acessa as tabelas: DOO_ORDER_CHARGES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.OrderChargeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 40 | 1 | 1 | 39 | 98% |

---

## 🔗 Tabelas Relacionadas

- [[doo_order_charges|DOO_ORDER_CHARGES]] — 40 atributos (1 PKs, 39 BICC)

---

## ⚙️ Atributos

### [[doo_order_charges|DOO_ORDER_CHARGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrderChargeAvgUnitSellingPrice | AVG_UNIT_SELLING_PRICE | — | ✅ |
| 2 | OrderChargeBlockAllowance | BLOCK_ALLOWANCE | — | ✅ |
| 3 | OrderChargeBlockSize | BLOCK_SIZE | — | ✅ |
| 4 | OrderChargeCanAdjustFlag | CAN_ADJUST_FLAG | — | ✅ |
| 5 | OrderChargeChargeAppliesTo | CHARGE_APPLIES_TO | — | ✅ |
| 6 | OrderChargeChargeCurrencyCode | CHARGE_CURRENCY_CODE | — | ✅ |
| 7 | OrderChargeChargeDefinitionCode | CHARGE_DEFINITION_CODE | — | ✅ |
| 8 | OrderChargeChargePeriodCode | CHARGE_PERIOD_CODE | — | ✅ |
| 9 | OrderChargeChargeSubtypeCode | CHARGE_SUBTYPE_CODE | — | ✅ |
| 10 | OrderChargeChargeTypeCode | CHARGE_TYPE_CODE | — | ✅ |
| 11 | OrderChargeCreatedBy | CREATED_BY | — | ✅ |
| 12 | OrderChargeCreationDate | CREATION_DATE | — | ✅ |
| 13 | OrderChargeDeltaType | DELTA_TYPE | — | ✅ |
| 14 | OrderChargeGsaUnitPrice | GSA_UNIT_PRICE | — | ✅ |
| 15 | OrderChargeId | ORDER_CHARGE_ID | 🔑 | ✅ |
| 16 | OrderChargeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | OrderChargeLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 18 | OrderChargeLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | OrderChargeModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 20 | OrderChargeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 21 | OrderChargeParentEntityCode | PARENT_ENTITY_CODE | — | ✅ |
| 22 | OrderChargeParentEntityId | PARENT_ENTITY_ID | — | ✅ |
| 23 | OrderChargePeriodicBillingFlag | PERIODIC_BILLING_FLAG | — | ✅ |
| 24 | OrderChargePeriodicRevRecognitionFlag | PERIODIC_REV_RECOGNITION_FLAG | — | ✅ |
| 25 | OrderChargePricePeriodicityCode | PRICE_PERIODICITY_CODE | — | ✅ |
| 26 | OrderChargePriceTypeCode | PRICE_TYPE_CODE | — | ✅ |
| 27 | OrderChargePricedQuantity | PRICED_QUANTITY | — | ✅ |
| 28 | OrderChargePricedQuantityUomCode | PRICED_QUANTITY_UOM_CODE | — | ✅ |
| 29 | OrderChargePrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 30 | OrderChargePromotionItemTermId | PROMOTION_ITEM_TERM_ID | — | — |
| 31 | OrderChargeReferenceOrderChargeId | REFERENCE_ORDER_CHARGE_ID | — | ✅ |
| 32 | OrderChargeRollupFlag | ROLLUP_FLAG | — | ✅ |
| 33 | OrderChargeSequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 34 | OrderChargeSourceChargeId | SOURCE_CHARGE_ID | — | ✅ |
| 35 | OrderChargeTierAggregationMethod | TIER_AGGREGATION_METHOD | — | ✅ |
| 36 | OrderChargeTierAppliesTo | TIER_APPLIES_TO | — | ✅ |
| 37 | OrderChargeTierBasisTypeCode | TIER_BASIS_TYPE_CODE | — | ✅ |
| 38 | OrderChargeTieredFlag | TIERED_FLAG | — | ✅ |
| 39 | OrderChargeUsagePriceLockFlag | USAGE_PRICE_LOCK_FLAG | — | ✅ |
| 40 | OrderChargeUsageUomCode | USAGE_UOM_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
