---
id: DOC-OTHER-PVO-ManualPriceAdjustmentExtractPVO
doc_type: system-doc
title: "ManualPriceAdjustmentExtractPVO — PVO Cross-Module"
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
  - ManualPriceAdjustmentExtractPVO
  - manualpriceadjustmentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ManualPriceAdjustmentExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Manual Price Adjustment Extract. Acessa as tabelas: DOO_MANUAL_PRICE_ADJUSTMENTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.ManualPriceAdjustmentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 1 | 1 | 27 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_manual_price_adjustments|DOO_MANUAL_PRICE_ADJUSTMENTS]] — 27 atributos (1 PKs, 27 BICC)

---

## ⚙️ Atributos

### [[doo_manual_price_adjustments|DOO_MANUAL_PRICE_ADJUSTMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ManualPriceAdjustmentAdjustmentAmount | ADJUSTMENT_AMOUNT | — | ✅ |
| 2 | ManualPriceAdjustmentAdjustmentElementBasis | ADJUSTMENT_ELEMENT_BASIS | — | ✅ |
| 3 | ManualPriceAdjustmentAdjustmentTypeCode | ADJUSTMENT_TYPE_CODE | — | ✅ |
| 4 | ManualPriceAdjustmentChargeDefinitionCode | CHARGE_DEFINITION_CODE | — | ✅ |
| 5 | ManualPriceAdjustmentChargeRollupFlag | CHARGE_ROLLUP_FLAG | — | ✅ |
| 6 | ManualPriceAdjustmentComments | COMMENTS | — | ✅ |
| 7 | ManualPriceAdjustmentCreatedBy | CREATED_BY | — | ✅ |
| 8 | ManualPriceAdjustmentCreationDate | CREATION_DATE | — | ✅ |
| 9 | ManualPriceAdjustmentDeltaType | DELTA_TYPE | — | ✅ |
| 10 | ManualPriceAdjustmentEffectivityTypeCode | EFFECTIVITY_TYPE_CODE | — | ✅ |
| 11 | ManualPriceAdjustmentId | MANUAL_PRICE_ADJUSTMENT_ID | 🔑 | ✅ |
| 12 | ManualPriceAdjustmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | ManualPriceAdjustmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | ManualPriceAdjustmentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | ManualPriceAdjustmentModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 16 | ManualPriceAdjustmentNumberOfPeriods | NUMBER_OF_PERIODS | — | ✅ |
| 17 | ManualPriceAdjustmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | ManualPriceAdjustmentParentEntityCode | PARENT_ENTITY_CODE | — | ✅ |
| 19 | ManualPriceAdjustmentParentEntityId | PARENT_ENTITY_ID | — | ✅ |
| 20 | ManualPriceAdjustmentPeriodFrom | PERIOD_FROM | — | ✅ |
| 21 | ManualPriceAdjustmentPeriodUntil | PERIOD_UNTIL | — | ✅ |
| 22 | ManualPriceAdjustmentPricePeriodicityCode | PRICE_PERIODICITY_CODE | — | ✅ |
| 23 | ManualPriceAdjustmentReasonCode | REASON_CODE | — | ✅ |
| 24 | ManualPriceAdjustmentReferenceMpaId | REFERENCE_MPA_ID | — | ✅ |
| 25 | ManualPriceAdjustmentSequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 26 | ManualPriceAdjustmentSourceManualPriceAdjId | SOURCE_MANUAL_PRICE_ADJ_ID | — | ✅ |
| 27 | ManualPriceAdjustmentValidationStatusCode | VALIDATION_STATUS_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
