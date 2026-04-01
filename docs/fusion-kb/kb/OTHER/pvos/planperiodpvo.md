---
id: DOC-OTHER-PVO-PlanPeriodPVO
doc_type: system-doc
title: "PlanPeriodPVO — PVO Cross-Module"
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
  - PlanPeriodPVO
  - planperiodpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanPeriodPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Plan Period. Acessa as tabelas: CMP_PLAN_PERIODS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.CompensationAM.PlanPeriodPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 1 | 1 | 34 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmp_plan_periods|CMP_PLAN_PERIODS]] — 34 atributos (1 PKs, 34 BICC)

---

## ⚙️ Atributos

### [[cmp_plan_periods|CMP_PLAN_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CompType | COMP_TYPE | — | ✅ |
| 2 | PeriodId | PERIOD_ID | 🔑 | ✅ |
| 3 | PlanPeriodPEOAssignmentChangeDate | ASSIGNMENT_CHANGE_DATE | — | ✅ |
| 4 | PlanPeriodPEOAvailEndDate | AVAIL_END_DATE | — | ✅ |
| 5 | PlanPeriodPEOAvailStartDate | AVAIL_START_DATE | — | ✅ |
| 6 | PlanPeriodPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | PlanPeriodPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | PlanPeriodPEODefaultDueDate | DEFAULT_DUE_DATE | — | ✅ |
| 9 | PlanPeriodPEODisplayName | DISPLAY_NAME | — | ✅ |
| 10 | PlanPeriodPEOEligibilityDate | ELIGIBILITY_DATE | — | ✅ |
| 11 | PlanPeriodPEOEndDate | END_DATE | — | ✅ |
| 12 | PlanPeriodPEOExchangeRateDate | EXCHANGE_RATE_DATE | — | ✅ |
| 13 | PlanPeriodPEOFreezeDate | FREEZE_DATE | — | ✅ |
| 14 | PlanPeriodPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | PlanPeriodPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | PlanPeriodPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | PlanPeriodPEOLvl1DefaultDueDate | LVL_1_DEFAULT_DUE_DATE | — | ✅ |
| 18 | PlanPeriodPEOLvl2DefaultDueDate | LVL_2_DEFAULT_DUE_DATE | — | ✅ |
| 19 | PlanPeriodPEOLvl3DefaultDueDate | LVL_3_DEFAULT_DUE_DATE | — | ✅ |
| 20 | PlanPeriodPEOLvl4DefaultDueDate | LVL_4_DEFAULT_DUE_DATE | — | ✅ |
| 21 | PlanPeriodPEOLvl5DefaultDueDate | LVL_5_DEFAULT_DUE_DATE | — | ✅ |
| 22 | PlanPeriodPEOLvl6DefaultDueDate | LVL_6_DEFAULT_DUE_DATE | — | ✅ |
| 23 | PlanPeriodPEOLvl7DefaultDueDate | LVL_7_DEFAULT_DUE_DATE | — | ✅ |
| 24 | PlanPeriodPEOMgrUpdDueDateFlag | MGR_UPD_DUE_DATE_FLAG | — | ✅ |
| 25 | PlanPeriodPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 26 | PlanPeriodPEOPerformanceDate | PERFORMANCE_DATE | — | ✅ |
| 27 | PlanPeriodPEOPeriodName | PERIOD_NAME | — | ✅ |
| 28 | PlanPeriodPEOPeriodType | PERIOD_TYPE | — | ✅ |
| 29 | PlanPeriodPEOPlanAccessId | PLAN_ACCESS_ID | — | ✅ |
| 30 | PlanPeriodPEOPlanId | PLAN_ID | — | ✅ |
| 31 | PlanPeriodPEOStartDate | START_DATE | — | ✅ |
| 32 | PlanPeriodPEOTopMgrDefaultDueDate | TOP_MGR_DEFAULT_DUE_DATE | — | ✅ |
| 33 | PlanPeriodPEOUpdateEndDate | UPDATE_END_DATE | — | ✅ |
| 34 | PlanPeriodPEOUpdateStartDate | UPDATE_START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
