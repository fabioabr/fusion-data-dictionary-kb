---
id: DOC-OTHER-PVO-ScheduleExceptionPVO
doc_type: system-doc
title: "ScheduleExceptionPVO — PVO Cross-Module"
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
  - ScheduleExceptionPVO
  - scheduleexceptionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ScheduleExceptionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Schedule Exception. Acessa as tabelas: PER_ALL_ASSIGNMENTS_M, PER_CALENDAR_EVENTS, PER_CALENDAR_EVENTS_TL (+3).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.WorkScheduleAM.ScheduleExceptionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 75 | 6 | 1 | 16 | 21% |

---

## 🔗 Tabelas Relacionadas

- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 6 atributos (1 BICC)
- [[per_calendar_events|PER_CALENDAR_EVENTS]] — 16 atributos (3 BICC)
- [[per_calendar_events_tl|PER_CALENDAR_EVENTS_TL]] — 12 atributos (2 BICC)
- [[per_resource_exceptions|PER_RESOURCE_EXCEPTIONS]] — 12 atributos (4 BICC)
- [[per_schedule_assignments|PER_SCHEDULE_ASSIGNMENTS]] — 15 atributos (1 BICC)
- [[per_schedule_exceptions|PER_SCHEDULE_EXCEPTIONS]] — 14 atributos (1 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 2 | AssignmentPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | AssignmentPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 4 | AssignmentPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 5 | AssignmentPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 6 | AssignmentPEOPersonId | PERSON_ID | — | — |

### [[per_calendar_events|PER_CALENDAR_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CalendarEventsPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CalendarEventsPEOCalendarEventId | CALENDAR_EVENT_ID | — | — |
| 3 | CalendarEventsPEOCategory | CATEGORY | — | — |
| 4 | CalendarEventsPEOCoverageType | COVERAGE_TYPE | — | — |
| 5 | CalendarEventsPEOCreatedBy | CREATED_BY | — | — |
| 6 | CalendarEventsPEOCreationDate | CREATION_DATE | — | — |
| 7 | CalendarEventsPEOEndDateTime | END_DATE_TIME | — | ✅ |
| 8 | CalendarEventsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | CalendarEventsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | CalendarEventsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | CalendarEventsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | CalendarEventsPEOShortCode | SHORT_CODE | — | — |
| 13 | CalendarEventsPEOStartDateTime | START_DATE_TIME | — | ✅ |
| 14 | CalendarEventsPEOTreeCode | TREE_CODE | — | — |
| 15 | CalendarEventsPEOTreeStructureCode | TREE_STRUCTURE_CODE | — | — |
| 16 | CalendarEventsPEOTreeVersionId | TREE_VERSION_ID | — | — |

### [[per_calendar_events_tl|PER_CALENDAR_EVENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CalendarEventsTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CalendarEventsTranslationPEOCalendarEventId | CALENDAR_EVENT_ID | — | — |
| 3 | CalendarEventsTranslationPEOCreatedBy | CREATED_BY | — | — |
| 4 | CalendarEventsTranslationPEOCreationDate | CREATION_DATE | — | — |
| 5 | CalendarEventsTranslationPEODescription | DESCRIPTION | — | — |
| 6 | CalendarEventsTranslationPEOLanguage | LANGUAGE | — | — |
| 7 | CalendarEventsTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CalendarEventsTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | CalendarEventsTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | CalendarEventsTranslationPEOName | NAME | — | ✅ |
| 11 | CalendarEventsTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | CalendarEventsTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[per_resource_exceptions|PER_RESOURCE_EXCEPTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourceExceptionPEOAvailabilityCode | AVAILABILITY_CODE | — | — |
| 2 | ResourceExceptionPEOCreatedBy | CREATED_BY | — | — |
| 3 | ResourceExceptionPEOCreationDate | CREATION_DATE | — | — |
| 4 | ResourceExceptionPEOEndDateTime | END_DATE_TIME | — | ✅ |
| 5 | ResourceExceptionPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 6 | ResourceExceptionPEOExceptionId | EXCEPTION_ID | — | — |
| 7 | ResourceExceptionPEOExceptionName | EXCEPTION_NAME | — | ✅ |
| 8 | ResourceExceptionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ResourceExceptionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | ResourceExceptionPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | ResourceExceptionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ResourceExceptionPEOStartDateTime | START_DATE_TIME | — | ✅ |

### [[per_schedule_assignments|PER_SCHEDULE_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ScheduleAssignmentPEOCreatedBy | CREATED_BY | — | — |
| 2 | ScheduleAssignmentPEOCreationDate | CREATION_DATE | — | — |
| 3 | ScheduleAssignmentPEOEndDate | END_DATE | — | — |
| 4 | ScheduleAssignmentPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 5 | ScheduleAssignmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ScheduleAssignmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ScheduleAssignmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ScheduleAssignmentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ScheduleAssignmentPEOPrimaryFlag | PRIMARY_FLAG | — | — |
| 10 | ScheduleAssignmentPEOResourceId | RESOURCE_ID | — | — |
| 11 | ScheduleAssignmentPEOResourceType | RESOURCE_TYPE | — | — |
| 12 | ScheduleAssignmentPEOScheduleAssignmentId | SCHEDULE_ASSIGNMENT_ID | — | — |
| 13 | ScheduleAssignmentPEOScheduleId | SCHEDULE_ID | — | — |
| 14 | ScheduleAssignmentPEOStartDate | START_DATE | — | — |
| 15 | ScheduleAssignmentPEOStartPatternDtlId | START_PATTERN_DTL_ID | — | — |

### [[per_schedule_exceptions|PER_SCHEDULE_EXCEPTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ScheduleExceptionPEOAvailabilityCode | AVAILABILITY_CODE | — | ✅ |
| 2 | ScheduleExceptionPEOCreatedBy | CREATED_BY | — | — |
| 3 | ScheduleExceptionPEOCreationDate | CREATION_DATE | — | — |
| 4 | ScheduleExceptionPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 5 | ScheduleExceptionPEOExceptionCode | EXCEPTION_CODE | — | ✅ |
| 6 | ScheduleExceptionPEOExceptionId | EXCEPTION_ID | — | — |
| 7 | ScheduleExceptionPEOExceptionType | EXCEPTION_TYPE | — | ✅ |
| 8 | ScheduleExceptionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ScheduleExceptionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | ScheduleExceptionPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | ScheduleExceptionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ScheduleExceptionPEOScheduleAssignmentId | SCHEDULE_ASSIGNMENT_ID | — | — |
| 13 | ScheduleExceptionPEOScheduleExceptionId | SCHEDULE_EXCEPTION_ID | 🔑 | ✅ |
| 14 | ScheduleExceptionPEOScheduleId | SCHEDULE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
