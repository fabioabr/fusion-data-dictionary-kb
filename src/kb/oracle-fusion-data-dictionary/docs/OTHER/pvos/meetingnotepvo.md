---
id: DOC-OTHER-PVO-MeetingNotePVO
doc_type: system-doc
title: "MeetingNotePVO — PVO Cross-Module"
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
  - MeetingNotePVO
  - meetingnotepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MeetingNotePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Meeting Note. Acessa as tabelas: HRR_DASHBOARDS, HRT_NOTES.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmTalentCalibDashAM.MeetingNotePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 42 | 2 | 5 | 17 | 40% |

---

## 🔗 Tabelas Relacionadas

- [[hrr_dashboards|HRR_DASHBOARDS]] — 25 atributos (4 PKs, 5 BICC)
- [[hrt_notes|HRT_NOTES]] — 17 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[hrr_dashboards|HRR_DASHBOARDS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgeGroupValue | AGE_GROUP_VALUE | — | — |
| 2 | AssignmentId | ASSIGNMENT_ID | — | — |
| 3 | BuLeaderDirectId | BU_LEADER_DIRECT_ID | — | — |
| 4 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 5 | CreatedBy | CREATED_BY | — | — |
| 6 | CreationDate | CREATION_DATE | — | — |
| 7 | DashboardId | DASHBOARD_ID | 🔑 | ✅ |
| 8 | ImpactLossCalbRtLvlId | IMPACT_LOSS_CALB_RT_LVL_ID | — | — |
| 9 | ImpactLossRtLvlId | IMPACT_LOSS_RT_LVL_ID | — | — |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | MeetingId | MEETING_ID | 🔑 | ✅ |
| 14 | MobilityCalibValue | MOBILITY_CALIB_VALUE | — | — |
| 15 | MobilityValue | MOBILITY_VALUE | — | — |
| 16 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | PerfCalibRtLvlId | PERF_CALIB_RT_LVL_ID | — | — |
| 18 | PerfRtLvlId | PERF_RT_LVL_ID | — | — |
| 19 | PersonId | PERSON_ID | 🔑 | ✅ |
| 20 | PotCalibRtLvlId | POT_CALIB_RT_LVL_ID | — | — |
| 21 | PotRtLvlId | POT_RT_LVL_ID | — | — |
| 22 | RiskLossCalibRtLvlId | RISK_LOSS_CALIB_RT_LVL_ID | — | — |
| 23 | RiskLossRtLvlId | RISK_LOSS_RT_LVL_ID | — | — |
| 24 | TalentScorCalbRtLvlId | TALENT_SCOR_CALB_RT_LVL_ID | — | — |
| 25 | TalentScoreRtLvlId | TALENT_SCORE_RT_LVL_ID | — | — |

### [[hrt_notes|HRT_NOTES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NotePEOAuthorId | AUTHOR_ID | — | ✅ |
| 2 | NotePEOContextId | CONTEXT_ID | — | — |
| 3 | NotePEOContextNameVo | CONTEXT_NAME_VO | — | — |
| 4 | NotePEOContextType | CONTEXT_TYPE | — | — |
| 5 | NotePEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | NotePEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | NotePEOEnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 8 | NotePEOHiddenFlag | HIDDEN_FLAG | — | — |
| 9 | NotePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | NotePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | NotePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | NotePEONoteId | NOTE_ID | — | ✅ |
| 13 | NotePEONoteTextClob | NOTE_TEXT | — | ✅ |
| 14 | NotePEONoteVisibilityCode | NOTE_VISIBILITY_CODE | — | ✅ |
| 15 | NotePEOObjectId | OBJECT_ID | — | — |
| 16 | NotePEOObjectType | OBJECT_TYPE | — | ✅ |
| 17 | NotePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
