---
id: DOC-OTHER-PVO-DashboardPVO
doc_type: system-doc
title: "DashboardPVO — PVO Cross-Module"
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
  - DashboardPVO
  - dashboardpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DashboardPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Dashboard. Acessa as tabelas: HRR_DASHBOARDS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmTalentCalibDashAM.DashboardPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 1 | 1 | 25 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hrr_dashboards|HRR_DASHBOARDS]] — 25 atributos (1 PKs, 25 BICC)

---

## ⚙️ Atributos

### [[hrr_dashboards|HRR_DASHBOARDS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgeGroupValue | AGE_GROUP_VALUE | — | ✅ |
| 2 | AssignmentId | ASSIGNMENT_ID | — | ✅ |
| 3 | BuLeaderDirectId | BU_LEADER_DIRECT_ID | — | ✅ |
| 4 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | DashboardId | DASHBOARD_ID | 🔑 | ✅ |
| 8 | ImpactLossCalbRtLvlId | IMPACT_LOSS_CALB_RT_LVL_ID | — | ✅ |
| 9 | ImpactLossRtLvlId | IMPACT_LOSS_RT_LVL_ID | — | ✅ |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | MeetingId | MEETING_ID | — | ✅ |
| 14 | MobilityCalibValue | MOBILITY_CALIB_VALUE | — | ✅ |
| 15 | MobilityValue | MOBILITY_VALUE | — | ✅ |
| 16 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | PerfCalibRtLvlId | PERF_CALIB_RT_LVL_ID | — | ✅ |
| 18 | PerfRtLvlId | PERF_RT_LVL_ID | — | ✅ |
| 19 | PersonId | PERSON_ID | — | ✅ |
| 20 | PotCalibRtLvlId | POT_CALIB_RT_LVL_ID | — | ✅ |
| 21 | PotRtLvlId | POT_RT_LVL_ID | — | ✅ |
| 22 | RiskLossCalibRtLvlId | RISK_LOSS_CALIB_RT_LVL_ID | — | ✅ |
| 23 | RiskLossRtLvlId | RISK_LOSS_RT_LVL_ID | — | ✅ |
| 24 | TalentScorCalbRtLvlId | TALENT_SCOR_CALB_RT_LVL_ID | — | ✅ |
| 25 | TalentScoreRtLvlId | TALENT_SCORE_RT_LVL_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
