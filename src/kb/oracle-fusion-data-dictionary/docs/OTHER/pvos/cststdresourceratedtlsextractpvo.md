---
id: DOC-OTHER-PVO-CstStdResourceRateDtlsExtractPVO
doc_type: system-doc
title: "CstStdResourceRateDtlsExtractPVO — PVO Cross-Module"
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
  - CstStdResourceRateDtlsExtractPVO
  - cststdresourceratedtlsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstStdResourceRateDtlsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Std Resource Rate Dtls Extract. Acessa as tabelas: CST_STD_RESOURCE_RATES, CST_STD_RESOURCE_RATE_DETAILS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstStdResourceRateDtlsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 33 | 2 | 1 | 33 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_std_resource_rates|CST_STD_RESOURCE_RATES]] — 23 atributos (23 BICC)
- [[cst_std_resource_rate_details|CST_STD_RESOURCE_RATE_DETAILS]] — 10 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[cst_std_resource_rates|CST_STD_RESOURCE_RATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourceRatesPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 2 | ResourceRatesPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 3 | ResourceRatesPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 4 | ResourceRatesPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 5 | ResourceRatesPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 6 | ResourceRatesPEOFromPeriodName | FROM_PERIOD_NAME | — | ✅ |
| 7 | ResourceRatesPEOInvOrgId | INV_ORG_ID | — | ✅ |
| 8 | ResourceRatesPEOLastUsedDate | LAST_USED_DATE | — | ✅ |
| 9 | ResourceRatesPEOLastUsedTransactionId | LAST_USED_TRANSACTION_ID | — | ✅ |
| 10 | ResourceRatesPEOPlanningResourceRateId | PLANNING_RESOURCE_RATE_ID | — | ✅ |
| 11 | ResourceRatesPEOPreviousEffectiveEndDate | PREVIOUS_EFFECTIVE_END_DATE | — | ✅ |
| 12 | ResourceRatesPEOPreviousEffectiveStartDate | PREVIOUS_EFFECTIVE_START_DATE | — | ✅ |
| 13 | ResourceRatesPEOPreviousStdResourceRateId | PREVIOUS_STD_RESOURCE_RATE_ID | — | ✅ |
| 14 | ResourceRatesPEOResourceId | RESOURCE_ID | — | ✅ |
| 15 | ResourceRatesPEOScenarioEventId | SCENARIO_EVENT_ID | — | ✅ |
| 16 | ResourceRatesPEOScenarioId | SCENARIO_ID | — | ✅ |
| 17 | ResourceRatesPEOSourceDi | SOURCE_DI | — | ✅ |
| 18 | ResourceRatesPEOStagedForStdCostAdjFlag | STAGED_FOR_STD_COST_ADJ_FLAG | — | ✅ |
| 19 | ResourceRatesPEOStatusCode | STATUS_CODE | — | ✅ |
| 20 | ResourceRatesPEOStdResourceRateId | STD_RESOURCE_RATE_ID | — | ✅ |
| 21 | ResourceRatesPEOToPeriodName | TO_PERIOD_NAME | — | ✅ |
| 22 | ResourceRatesPEOTotalRate | TOTAL_RATE | — | ✅ |
| 23 | ResourceRatesPEOUomCode | UOM_CODE | — | ✅ |

### [[cst_std_resource_rate_details|CST_STD_RESOURCE_RATE_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourceRateDetailsPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 2 | ResourceRateDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | ResourceRateDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | ResourceRateDetailsPEOExpensePoolId | EXPENSE_POOL_ID | — | ✅ |
| 5 | ResourceRateDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ResourceRateDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ResourceRateDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ResourceRateDetailsPEOStdResourceRateDetailId | STD_RESOURCE_RATE_DETAIL_ID | 🔑 | ✅ |
| 9 | ResourceRateDetailsPEOStdResourceRateId | STD_RESOURCE_RATE_ID | — | ✅ |
| 10 | ResourceRateDetailsPEOUnitRate | UNIT_RATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
