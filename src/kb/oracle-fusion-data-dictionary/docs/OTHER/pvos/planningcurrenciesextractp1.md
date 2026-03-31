---
id: DOC-OTHER-PVO-PlanningCurrenciesExtractP1
doc_type: system-doc
title: "PlanningCurrenciesExtractP1 — PVO Cross-Module"
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
  - PlanningCurrenciesExtractP1
  - planningcurrenciesextractp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanningCurrenciesExtractP1

## 📌 Visão Geral

View Object para extração BICC de dados de Planning Currencies Extract P1. Acessa as tabelas: PJO_PLANNING_CURRENCIES.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjoBiccExtractAM.PlanningCurrenciesExtractP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 1 | 17 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjo_planning_currencies|PJO_PLANNING_CURRENCIES]] — 17 atributos (1 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[pjo_planning_currencies|PJO_PLANNING_CURRENCIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjoPlanningCurrenciesCreatedBy | CREATED_BY | — | ✅ |
| 2 | PjoPlanningCurrenciesCreationDate | CREATION_DATE | — | ✅ |
| 3 | PjoPlanningCurrenciesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | PjoPlanningCurrenciesLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | PjoPlanningCurrenciesLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | PjoPlanningCurrenciesObjectId1 | OBJECT_ID1 | — | ✅ |
| 7 | PjoPlanningCurrenciesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | PjoPlanningCurrenciesPcCostExchangeRate | PC_COST_EXCHANGE_RATE | — | ✅ |
| 9 | PjoPlanningCurrenciesPcRevExchangeRate | PC_REV_EXCHANGE_RATE | — | ✅ |
| 10 | PjoPlanningCurrenciesPfcCostExchangeRate | PFC_COST_EXCHANGE_RATE | — | ✅ |
| 11 | PjoPlanningCurrenciesPfcRevExchangeRate | PFC_REV_EXCHANGE_RATE | — | ✅ |
| 12 | PjoPlanningCurrenciesPlanTypeId | PLAN_TYPE_ID | — | ✅ |
| 13 | PjoPlanningCurrenciesPlanVersionId | PLAN_VERSION_ID | — | ✅ |
| 14 | PjoPlanningCurrenciesPlanningCurrencyId | PLANNING_CURRENCY_ID | 🔑 | ✅ |
| 15 | PjoPlanningCurrenciesPlanningOptionId | PLANNING_OPTION_ID | — | ✅ |
| 16 | PjoPlanningCurrenciesProjectId | PROJECT_ID | — | ✅ |
| 17 | PjoPlanningCurrenciesTxnCurrencyCode | TXN_CURRENCY_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
