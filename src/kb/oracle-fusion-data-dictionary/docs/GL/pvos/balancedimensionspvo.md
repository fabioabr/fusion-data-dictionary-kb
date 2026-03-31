---
id: DOC-GL-PVO-BalanceDimensionsPVO
doc_type: system-doc
title: "BalanceDimensionsPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - BalanceDimensionsPVO
  - balancedimensionspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BalanceDimensionsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Balance Dimensions. Acessa as tabelas: PAY_BALANCE_DIMENSIONS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBalancesSetupAM.BalanceDimensionsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 1 | 1 | 29 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pay_balance_dimensions|PAY_BALANCE_DIMENSIONS]] — 29 atributos (1 PKs, 29 BICC)

---

## ⚙️ Atributos

### [[pay_balance_dimensions|PAY_BALANCE_DIMENSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BalanceDimensionsPEOApplicationId | APPLICATION_ID | — | ✅ |
| 2 | BalanceDimensionsPEOAsgActionBalanceDimId | ASG_ACTION_BALANCE_DIM_ID | — | ✅ |
| 3 | BalanceDimensionsPEOBalanceDimensionId | BALANCE_DIMENSION_ID | 🔑 | ✅ |
| 4 | BalanceDimensionsPEOBaseDbItemSuffix | BASE_DB_ITEM_SUFFIX | — | ✅ |
| 5 | BalanceDimensionsPEOBaseDimensionName | BASE_DIMENSION_NAME | — | ✅ |
| 6 | BalanceDimensionsPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | BalanceDimensionsPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | BalanceDimensionsPEODescription | DESCRIPTION | — | ✅ |
| 9 | BalanceDimensionsPEODimensionLevel | DIMENSION_LEVEL | — | ✅ |
| 10 | BalanceDimensionsPEODimensionType | DIMENSION_TYPE | — | ✅ |
| 11 | BalanceDimensionsPEOEndTimeDefId | END_TIME_DEF_ID | — | ✅ |
| 12 | BalanceDimensionsPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 13 | BalanceDimensionsPEOExpiryCheckingLevel | EXPIRY_CHECKING_LEVEL | — | ✅ |
| 14 | BalanceDimensionsPEOExpiryTimeDefId | EXPIRY_TIME_DEF_ID | — | ✅ |
| 15 | BalanceDimensionsPEOFeedCheckingType | FEED_CHECKING_TYPE | — | ✅ |
| 16 | BalanceDimensionsPEOInitialDate | INITIAL_DATE | — | ✅ |
| 17 | BalanceDimensionsPEOInitialTimeDefId | INITIAL_TIME_DEF_ID | — | ✅ |
| 18 | BalanceDimensionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | BalanceDimensionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 20 | BalanceDimensionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 21 | BalanceDimensionsPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 22 | BalanceDimensionsPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 23 | BalanceDimensionsPEOModuleId | MODULE_ID | — | ✅ |
| 24 | BalanceDimensionsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 25 | BalanceDimensionsPEOPaymentsFlag | PAYMENTS_FLAG | — | ✅ |
| 26 | BalanceDimensionsPEOPeriodType | PERIOD_TYPE | — | ✅ |
| 27 | BalanceDimensionsPEORouteId | ROUTE_ID | — | ✅ |
| 28 | BalanceDimensionsPEOSaveRunBalanceEnabled | SAVE_RUN_BALANCE_ENABLED | — | ✅ |
| 29 | BalanceDimensionsPEOStartTimeDefId | START_TIME_DEF_ID | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
