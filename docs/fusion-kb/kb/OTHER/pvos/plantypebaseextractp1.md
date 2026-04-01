---
id: DOC-OTHER-PVO-PlanTypeBaseExtractP1
doc_type: system-doc
title: "PlanTypeBaseExtractP1 — PVO Cross-Module"
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
  - PlanTypeBaseExtractP1
  - plantypebaseextractp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanTypeBaseExtractP1

## 📌 Visão Geral

View Object para extração BICC de dados de Plan Type Base Extract P1. Acessa as tabelas: PJO_PLAN_TYPES_B, PJO_PLAN_TYPES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjoBiccExtractAM.PlanTypeBaseExtractP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 64 | 2 | 1 | 33 | 52% |

---

## 🔗 Tabelas Relacionadas

- [[pjo_plan_types_b|PJO_PLAN_TYPES_B]] — 53 atributos (1 PKs, 22 BICC)
- [[pjo_plan_types_tl|PJO_PLAN_TYPES_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[pjo_plan_types_b|PJO_PLAN_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanTypeBasePEOApprovedCostPlanTypeFlag | APPROVED_COST_PLAN_TYPE_FLAG | — | ✅ |
| 2 | PlanTypeBasePEOApprovedRevPlanTypeFlag | APPROVED_REV_PLAN_TYPE_FLAG | — | ✅ |
| 3 | PlanTypeBasePEOAttribute1 | ATTRIBUTE1 | — | — |
| 4 | PlanTypeBasePEOAttribute10 | ATTRIBUTE10 | — | — |
| 5 | PlanTypeBasePEOAttribute11 | ATTRIBUTE11 | — | — |
| 6 | PlanTypeBasePEOAttribute12 | ATTRIBUTE12 | — | — |
| 7 | PlanTypeBasePEOAttribute13 | ATTRIBUTE13 | — | — |
| 8 | PlanTypeBasePEOAttribute14 | ATTRIBUTE14 | — | — |
| 9 | PlanTypeBasePEOAttribute15 | ATTRIBUTE15 | — | — |
| 10 | PlanTypeBasePEOAttribute16 | ATTRIBUTE16 | — | — |
| 11 | PlanTypeBasePEOAttribute17 | ATTRIBUTE17 | — | — |
| 12 | PlanTypeBasePEOAttribute18 | ATTRIBUTE18 | — | — |
| 13 | PlanTypeBasePEOAttribute19 | ATTRIBUTE19 | — | — |
| 14 | PlanTypeBasePEOAttribute2 | ATTRIBUTE2 | — | — |
| 15 | PlanTypeBasePEOAttribute20 | ATTRIBUTE20 | — | — |
| 16 | PlanTypeBasePEOAttribute21 | ATTRIBUTE21 | — | — |
| 17 | PlanTypeBasePEOAttribute22 | ATTRIBUTE22 | — | — |
| 18 | PlanTypeBasePEOAttribute23 | ATTRIBUTE23 | — | — |
| 19 | PlanTypeBasePEOAttribute24 | ATTRIBUTE24 | — | — |
| 20 | PlanTypeBasePEOAttribute25 | ATTRIBUTE25 | — | — |
| 21 | PlanTypeBasePEOAttribute26 | ATTRIBUTE26 | — | — |
| 22 | PlanTypeBasePEOAttribute27 | ATTRIBUTE27 | — | — |
| 23 | PlanTypeBasePEOAttribute28 | ATTRIBUTE28 | — | — |
| 24 | PlanTypeBasePEOAttribute29 | ATTRIBUTE29 | — | — |
| 25 | PlanTypeBasePEOAttribute3 | ATTRIBUTE3 | — | — |
| 26 | PlanTypeBasePEOAttribute30 | ATTRIBUTE30 | — | — |
| 27 | PlanTypeBasePEOAttribute4 | ATTRIBUTE4 | — | — |
| 28 | PlanTypeBasePEOAttribute5 | ATTRIBUTE5 | — | — |
| 29 | PlanTypeBasePEOAttribute6 | ATTRIBUTE6 | — | — |
| 30 | PlanTypeBasePEOAttribute7 | ATTRIBUTE7 | — | — |
| 31 | PlanTypeBasePEOAttribute8 | ATTRIBUTE8 | — | — |
| 32 | PlanTypeBasePEOAttribute9 | ATTRIBUTE9 | — | — |
| 33 | PlanTypeBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 34 | PlanTypeBasePEOAutoApproveFlag | AUTO_APPROVE_FLAG | — | ✅ |
| 35 | PlanTypeBasePEOAutoSubmitForAppr | AUTO_SUBMIT_FOR_APPR | — | ✅ |
| 36 | PlanTypeBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 37 | PlanTypeBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 38 | PlanTypeBasePEODefaultFinPlanTypeFlag | DEFAULT_FIN_PLAN_TYPE_FLAG | — | ✅ |
| 39 | PlanTypeBasePEOEnableWfFlag | ENABLE_WF_FLAG | — | ✅ |
| 40 | PlanTypeBasePEOEndDate | END_DATE | — | ✅ |
| 41 | PlanTypeBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 42 | PlanTypeBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 43 | PlanTypeBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 44 | PlanTypeBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 45 | PlanTypeBasePEOPlanClassCode | PLAN_CLASS_CODE | — | ✅ |
| 46 | PlanTypeBasePEOPlanInMultiCurrFlag | PLAN_IN_MULTI_CURR_FLAG | — | ✅ |
| 47 | PlanTypeBasePEOPlanOptionCode | PLAN_OPTION_CODE | — | ✅ |
| 48 | PlanTypeBasePEOPlanTypeCode | PLAN_TYPE_CODE | — | ✅ |
| 49 | PlanTypeBasePEOPlanTypeId | PLAN_TYPE_ID | 🔑 | ✅ |
| 50 | PlanTypeBasePEOPrimaryCostForecastFlag | PRIMARY_COST_FORECAST_FLAG | — | ✅ |
| 51 | PlanTypeBasePEOPrimaryRevForecastFlag | PRIMARY_REV_FORECAST_FLAG | — | ✅ |
| 52 | PlanTypeBasePEOReportQuantityFromCode | REPORT_QUANTITY_FROM_CODE | — | ✅ |
| 53 | PlanTypeBasePEOStartDate | START_DATE | — | ✅ |

### [[pjo_plan_types_tl|PJO_PLAN_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PlanTypeTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PlanTypeTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PlanTypeTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | PlanTypeTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 5 | PlanTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PlanTypeTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | PlanTypeTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | PlanTypeTranslationPEOName | NAME | — | ✅ |
| 9 | PlanTypeTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | PlanTypeTranslationPEOPlanTypeId | PLAN_TYPE_ID | — | ✅ |
| 11 | PlanTypeTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
