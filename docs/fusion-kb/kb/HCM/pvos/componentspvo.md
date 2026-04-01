---
id: DOC-HCM-PVO-ComponentsPVO
doc_type: system-doc
title: "ComponentsPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ComponentsPVO
  - componentspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ComponentsPVO

## 📌 Visão Geral

Cataloga componentes de planos de compensacao com tipo e traducoes. Referencia para proventos, bonus e outros elementos de remuneracao.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.CompensationAM.ComponentsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 31 | 2 | 2 | 31 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmp_components_b|CMP_COMPONENTS_B]] — 20 atributos (1 PKs, 20 BICC)
- [[cmp_components_tl|CMP_COMPONENTS_TL]] — 11 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[cmp_components_b|CMP_COMPONENTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ComponentId | COMPONENT_ID | 🔑 | ✅ |
| 2 | ComponentsPEOCompType | COMP_TYPE | — | ✅ |
| 3 | ComponentsPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | ComponentsPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | ComponentsPEOCurrencyDeterminationCode | CURRENCY_DETERMINATION_CODE | — | ✅ |
| 6 | ComponentsPEOGrantType | GRANT_TYPE | — | ✅ |
| 7 | ComponentsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ComponentsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | ComponentsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ComponentsPEONonMonetaryUom | NON_MONETARY_UOM | — | ✅ |
| 11 | ComponentsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | ComponentsPEOOrderNum | ORDER_NUM | — | ✅ |
| 13 | ComponentsPEOPeriodId | PERIOD_ID | — | ✅ |
| 14 | ComponentsPEOPlanId | PLAN_ID | — | ✅ |
| 15 | ComponentsPEOPoolIdToConsume | POOL_ID_TO_CONSUME | — | ✅ |
| 16 | ComponentsPEOPostAsSalaryFlag | POST_AS_SALARY_FLAG | — | ✅ |
| 17 | ComponentsPEORuleId | RULE_ID | — | ✅ |
| 18 | ComponentsPEOSalaryComponent | SALARY_COMPONENT | — | ✅ |
| 19 | ComponentsPEOSystemOrderNum | SYSTEM_ORDER_NUM | — | ✅ |
| 20 | ComponentsPEOTradingSymbol | TRADING_SYMBOL | — | ✅ |

### [[cmp_components_tl|CMP_COMPONENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ComponentsTLPEOComponentId1 | COMPONENT_ID | — | ✅ |
| 2 | ComponentsTLPEOComponentName | COMPONENT_NAME | — | ✅ |
| 3 | ComponentsTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | ComponentsTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | ComponentsTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | ComponentsTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ComponentsTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ComponentsTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ComponentsTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | ComponentsTLPEOPlanId1 | PLAN_ID | — | ✅ |
| 11 | ComponentsTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
