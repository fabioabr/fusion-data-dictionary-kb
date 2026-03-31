---
id: DOC-OTHER-PVO-VrmSystemOptionsPVO
doc_type: system-doc
title: "VrmSystemOptionsPVO — PVO Cross-Module"
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
  - VrmSystemOptionsPVO
  - vrmsystemoptionspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# VrmSystemOptionsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Vrm System Options. Acessa as tabelas: VRM_SYSTEM_OPTIONS.

**Caminho:** `FscmTopModelAM.FinVrmShrdSetupPublicModelAM.VrmSystemOptionsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 31 | 1 | 1 | 2 | 6% |

---

## 🔗 Tabelas Relacionadas

- [[vrm_system_options|VRM_SYSTEM_OPTIONS]] — 31 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[vrm_system_options|VRM_SYSTEM_OPTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActDateInClosedPeriod | ACT_DATE_IN_CLOSED_PERIOD | — | — |
| 2 | AdjReviewRequiredFlag | ADJ_REVIEW_REQUIRED_FLAG | — | — |
| 3 | AutoGroupDocLines | AUTO_GROUP_DOC_LINES | — | — |
| 4 | CarveoutUndeliveredItems | CARVEOUT_UNDELIVERED_ITEMS | — | — |
| 5 | CorporateCurrency | CORPORATE_CURRENCY | — | — |
| 6 | CreateClearingOption | CREATE_CLEARING_OPTION | — | — |
| 7 | CreatedBy | CREATED_BY | — | — |
| 8 | CreationDate | CREATION_DATE | — | — |
| 9 | DefaultMeaPeriod | DEFAULT_MEA_PERIOD | — | — |
| 10 | DefaultMeaPeriodUnit | DEFAULT_MEA_PERIOD_UNIT | — | — |
| 11 | ExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 12 | ExtractionPeriodType | EXTRACTION_PERIOD_TYPE | — | — |
| 13 | FmvToleranceFlag | FMV_TOLERANCE_FLAG | — | — |
| 14 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | MeaAdjControlLevel | MEA_ADJ_CONTROL_LEVEL | — | — |
| 18 | MeaItemClfCatSetId | MEA_ITEM_CLF_CAT_SET_ID | — | — |
| 19 | MeaItemClfCategoryId | MEA_ITEM_CLF_CATEGORY_ID | — | — |
| 20 | MeaTimeFrame | MEA_TIME_FRAME | — | — |
| 21 | MeaTimeFrameUnit | MEA_TIME_FRAME_UNIT | — | — |
| 22 | NumberOfProcessors | NUMBER_OF_PROCESSORS | — | — |
| 23 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | PctValuePrecision | PCT_VALUE_PRECISION | — | — |
| 25 | ProcessingUnitSize | PROCESSING_UNIT_SIZE | — | — |
| 26 | RoundingRule | ROUNDING_RULE | — | — |
| 27 | StandaloneDataPeriod | STANDALONE_DATA_PERIOD | — | — |
| 28 | StandaloneDataPeriodUnit | STANDALONE_DATA_PERIOD_UNIT | — | — |
| 29 | SystemOptionId | SYSTEM_OPTION_ID | 🔑 | ✅ |
| 30 | UpdateEffectivityPeriod | UPDATE_EFFECTIVITY_PERIOD | — | — |
| 31 | VrmSystemOptions1 | VRM_SYSTEM_OPTIONS | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
