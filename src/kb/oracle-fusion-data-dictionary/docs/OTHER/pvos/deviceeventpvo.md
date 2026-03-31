---
id: DOC-OTHER-PVO-DeviceEventPVO
doc_type: system-doc
title: "DeviceEventPVO — PVO Cross-Module"
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
  - DeviceEventPVO
  - deviceeventpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DeviceEventPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Device Event. Acessa as tabelas: HWM_TM_EVENTS_V, PER_ALL_ASSIGNMENTS_M, PER_ALL_PEOPLE_F (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeEventsAM.DeviceEventPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 50 | 4 | 1 | 36 | 72% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tm_events_v|HWM_TM_EVENTS_V]] — 28 atributos (1 PKs, 26 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 6 atributos (2 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 8 atributos (4 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 8 atributos (4 BICC)

---

## ⚙️ Atributos

### [[hwm_tm_events_v|HWM_TM_EVENTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeviceEventPEOCorrAssignmentId | CORR_ASSIGNMENT_ID | — | ✅ |
| 2 | DeviceEventPEOCorrBadgeId | CORR_BADGE_ID | — | ✅ |
| 3 | DeviceEventPEOCorrCreatedBy | CORR_CREATED_BY | — | ✅ |
| 4 | DeviceEventPEOCorrCreationDate | CORR_CREATION_DATE | — | ✅ |
| 5 | DeviceEventPEOCorrLastUpdateDate | CORR_LAST_UPDATE_DATE | — | ✅ |
| 6 | DeviceEventPEOCorrLastUpdateLogin | CORR_LAST_UPDATE_LOGIN | — | ✅ |
| 7 | DeviceEventPEOCorrLastUpdatedBy | CORR_LAST_UPDATED_BY | — | ✅ |
| 8 | DeviceEventPEOCorrPersonId | CORR_PERSON_ID | — | ✅ |
| 9 | DeviceEventPEOCreatedBy | CREATED_BY | — | ✅ |
| 10 | DeviceEventPEOCreationDate | CREATION_DATE | — | ✅ |
| 11 | DeviceEventPEODeviceId | DEVICE_ID | — | ✅ |
| 12 | DeviceEventPEOEventStatus | EVENT_STATUS | — | ✅ |
| 13 | DeviceEventPEOEventTimeReal | EVENT_TIME_REAL | — | ✅ |
| 14 | DeviceEventPEOEventTimeString | EVENT_TIME_STRING | — | ✅ |
| 15 | DeviceEventPEOEventType | EVENT_TYPE | — | ✅ |
| 16 | DeviceEventPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | DeviceEventPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 18 | DeviceEventPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | DeviceEventPEOPersonId | PERSON_ID | — | ✅ |
| 20 | DeviceEventPEORefTimezoneId | REF_TIMEZONE_ID | — | ✅ |
| 21 | DeviceEventPEOReporterId | REPORTER_ID | — | ✅ |
| 22 | DeviceEventPEOReporterIdType | REPORTER_ID_TYPE | — | ✅ |
| 23 | DeviceEventPEOResourceId | RESOURCE_ID | — | ✅ |
| 24 | DeviceEventPEOStatus | STATUS | — | — |
| 25 | DeviceEventPEOTimezoneOffset | TIMEZONE_OFFSET | — | — |
| 26 | DeviceEventPEOTmEventCorrectionId | TM_EVENT_CORRECTION_ID | — | ✅ |
| 27 | DeviceEventPEOTmEventId | TM_EVENT_ID | 🔑 | ✅ |
| 28 | DeviceEventPEOTmEventReqId | TM_EVENT_REQ_ID | — | ✅ |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentId | ASSIGNMENT_ID | — | — |
| 2 | AssignmentPEOAssignmentNumber | ASSIGNMENT_NUMBER | — | ✅ |
| 3 | AssignmentPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | AssignmentPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 5 | AssignmentPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 6 | AssignmentPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CorrPersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | CorrPersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | CorrPersonDetailsPEOPersonId | PERSON_ID | — | — |
| 4 | CorrPersonDetailsPEOPersonNumber | PERSON_NUMBER | — | ✅ |
| 5 | EventPersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | EventPersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | EventPersonDetailsPEOPersonId | PERSON_ID | — | — |
| 8 | EventPersonDetailsPEOPersonNumber | PERSON_NUMBER | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CorrPersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | CorrPersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | CorrPersonNamePEOPersonName | FULL_NAME | — | ✅ |
| 4 | CorrPersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |
| 5 | EventPersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | EventPersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | EventPersonNamePEOPersonName | FULL_NAME | — | ✅ |
| 8 | EventPersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
