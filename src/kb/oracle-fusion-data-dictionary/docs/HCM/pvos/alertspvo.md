---
id: DOC-HCM-PVO-AlertsPVO
doc_type: system-doc
title: "AlertsPVO — PVO Human Capital Management"
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
  - AlertsPVO
  - alertspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AlertsPVO

## 📌 Visão Geral

Extrai alertas de compensacao gerados durante processos de Compensation Workbench (CWB). Utilizado para monitorar excecoes em ciclos de remuneracao.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.CompensationAM.AlertsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 36 | 2 | 2 | 16 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[cmp_calc_alerts_vl|CMP_CALC_ALERTS_VL]] — 20 atributos (5 BICC)
- [[cmp_cwb_alerts|CMP_CWB_ALERTS]] — 16 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[cmp_calc_alerts_vl|CMP_CALC_ALERTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CalcAlertsPEOAlertDescription | ALERT_DESCRIPTION | — | ✅ |
| 2 | CalcAlertsPEOAlertId | ALERT_ID | — | — |
| 3 | CalcAlertsPEOAlertKey | ALERT_KEY | — | — |
| 4 | CalcAlertsPEOAlertName | ALERT_NAME | — | ✅ |
| 5 | CalcAlertsPEOAlertType | ALERT_TYPE | — | ✅ |
| 6 | CalcAlertsPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 7 | CalcAlertsPEOCreatedBy | CREATED_BY | — | — |
| 8 | CalcAlertsPEOCreationDate | CREATION_DATE | — | — |
| 9 | CalcAlertsPEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 10 | CalcAlertsPEOKeyType | KEY_TYPE | — | — |
| 11 | CalcAlertsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | CalcAlertsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | CalcAlertsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | CalcAlertsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | CalcAlertsPEOPartiProcessEna | PARTI_PROCESS_ENA | — | — |
| 16 | CalcAlertsPEOQuickAlertCode | QUICK_ALERT_CODE | — | — |
| 17 | CalcAlertsPEOQuickAlertFlag | QUICK_ALERT_FLAG | — | — |
| 18 | CalcAlertsPEORefreshProcessEna | REFRESH_PROCESS_ENA | — | — |
| 19 | CalcAlertsPEOWrkshtSaveEna | WRKSHT_SAVE_ENA | — | — |
| 20 | CalcAlertsPEOWrkshtTabOutEna | WRKSHT_TAB_OUT_ENA | — | — |

### [[cmp_cwb_alerts|CMP_CWB_ALERTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AlertsPEOAlertId | ALERT_ID | 🔑 | ✅ |
| 2 | AlertsPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | AlertsPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | AlertsPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | AlertsPEODisplayFlag | DISPLAY_FLAG | — | ✅ |
| 6 | AlertsPEOHideFromManagerFlag | HIDE_FROM_MANAGER_FLAG | — | ✅ |
| 7 | AlertsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | AlertsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | AlertsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | AlertsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | AlertsPEOPeriodId | PERIOD_ID | — | — |
| 12 | AlertsPEOPersonEventId | PERSON_EVENT_ID | 🔑 | ✅ |
| 13 | AlertsPEOPlanId | PLAN_ID | — | — |
| 14 | AlertsPEOTriggerSource | TRIGGER_SOURCE | — | ✅ |
| 15 | AlertsPEOTriggeredBy | TRIGGERED_BY | — | ✅ |
| 16 | AlertsPEOTriggeredDate | TRIGGERED_DATE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
