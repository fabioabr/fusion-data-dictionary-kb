---
id: DOC-OTHER-PVO-MaintenanceSchedulePattern
doc_type: system-doc
title: "MaintenanceSchedulePattern — PVO Cross-Module"
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
  - MaintenanceSchedulePattern
  - maintenanceschedulepattern
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MaintenanceSchedulePattern

## 📌 Visão Geral

View Object para extração BICC de dados de Maintenance Schedule Pattern. Acessa as tabelas: MNT_SCHEDULE_PATTERNS_B, MNT_SCHEDULE_PATTERNS_TL.

**Caminho:** `FscmTopModelAM.MaintProgramAM.MaintenanceSchedulePattern`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 75 | 2 | 1 | 8 | 11% |

---

## 🔗 Tabelas Relacionadas

- [[mnt_schedule_patterns_b|MNT_SCHEDULE_PATTERNS_B]] — 71 atributos (1 PKs, 6 BICC)
- [[mnt_schedule_patterns_tl|MNT_SCHEDULE_PATTERNS_TL]] — 4 atributos (2 BICC)

---

## ⚙️ Atributos

### [[mnt_schedule_patterns_b|MNT_SCHEDULE_PATTERNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SchedulePatternBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | SchedulePatternBasePEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 3 | SchedulePatternBasePEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 4 | SchedulePatternBasePEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 5 | SchedulePatternBasePEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 6 | SchedulePatternBasePEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 7 | SchedulePatternBasePEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 8 | SchedulePatternBasePEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 9 | SchedulePatternBasePEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 10 | SchedulePatternBasePEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 11 | SchedulePatternBasePEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 12 | SchedulePatternBasePEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 13 | SchedulePatternBasePEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 14 | SchedulePatternBasePEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 15 | SchedulePatternBasePEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 16 | SchedulePatternBasePEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 17 | SchedulePatternBasePEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 18 | SchedulePatternBasePEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 19 | SchedulePatternBasePEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 20 | SchedulePatternBasePEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 21 | SchedulePatternBasePEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 22 | SchedulePatternBasePEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | SchedulePatternBasePEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 24 | SchedulePatternBasePEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 25 | SchedulePatternBasePEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 26 | SchedulePatternBasePEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 27 | SchedulePatternBasePEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 28 | SchedulePatternBasePEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 29 | SchedulePatternBasePEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 30 | SchedulePatternBasePEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 31 | SchedulePatternBasePEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 32 | SchedulePatternBasePEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 33 | SchedulePatternBasePEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 34 | SchedulePatternBasePEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 35 | SchedulePatternBasePEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 36 | SchedulePatternBasePEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 37 | SchedulePatternBasePEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 38 | SchedulePatternBasePEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 39 | SchedulePatternBasePEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 40 | SchedulePatternBasePEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 41 | SchedulePatternBasePEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 42 | SchedulePatternBasePEOCreatedBy | CREATED_BY | — | — |
| 43 | SchedulePatternBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 44 | SchedulePatternBasePEOCycleInterval | CYCLE_INTERVAL | — | ✅ |
| 45 | SchedulePatternBasePEODailyEveryWeekdayFlag | DAILY_EVERY_WEEKDAY_FLAG | — | — |
| 46 | SchedulePatternBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 47 | SchedulePatternBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 48 | SchedulePatternBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 49 | SchedulePatternBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 50 | SchedulePatternBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 51 | SchedulePatternBasePEOMonthlySpecificDay | MONTHLY_SPECIFIC_DAY | — | — |
| 52 | SchedulePatternBasePEOMonthlyWeekday | MONTHLY_WEEKDAY | — | — |
| 53 | SchedulePatternBasePEOMonthlyWeekdayOrdinal | MONTHLY_WEEKDAY_ORDINAL | — | — |
| 54 | SchedulePatternBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 55 | SchedulePatternBasePEOProgramId | PROGRAM_ID | — | — |
| 56 | SchedulePatternBasePEORequestId | REQUEST_ID | — | — |
| 57 | SchedulePatternBasePEOSchedulePatternId | SCHEDULE_PATTERN_ID | 🔑 | ✅ |
| 58 | SchedulePatternBasePEOSchedulePatternName | SCHEDULE_PATTERN_NAME | — | ✅ |
| 59 | SchedulePatternBasePEOSchedulePatternType | SCHEDULE_PATTERN_TYPE | — | ✅ |
| 60 | SchedulePatternBasePEOWeeklyDayFridayFlag | WEEKLY_DAY_FRIDAY_FLAG | — | — |
| 61 | SchedulePatternBasePEOWeeklyDayMondayFlag | WEEKLY_DAY_MONDAY_FLAG | — | — |
| 62 | SchedulePatternBasePEOWeeklyDaySaturdayFlag | WEEKLY_DAY_SATURDAY_FLAG | — | — |
| 63 | SchedulePatternBasePEOWeeklyDaySundayFlag | WEEKLY_DAY_SUNDAY_FLAG | — | — |
| 64 | SchedulePatternBasePEOWeeklyDayThursdayFlag | WEEKLY_DAY_THURSDAY_FLAG | — | — |
| 65 | SchedulePatternBasePEOWeeklyDayTuesdayFlag | WEEKLY_DAY_TUESDAY_FLAG | — | — |
| 66 | SchedulePatternBasePEOWeeklyDayWednesdayFlag | WEEKLY_DAY_WEDNESDAY_FLAG | — | — |
| 67 | SchedulePatternBasePEOYearlyMonth | YEARLY_MONTH | — | — |
| 68 | SchedulePatternBasePEOYearlySpecificDay | YEARLY_SPECIFIC_DAY | — | — |
| 69 | SchedulePatternBasePEOYearlySpecificMonth | YEARLY_SPECIFIC_MONTH | — | — |
| 70 | SchedulePatternBasePEOYearlyWeekday | YEARLY_WEEKDAY | — | — |
| 71 | SchedulePatternBasePEOYearlyWeekdayOrdinal | YEARLY_WEEKDAY_ORDINAL | — | — |

### [[mnt_schedule_patterns_tl|MNT_SCHEDULE_PATTERNS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SchedulePatternTLPEOLanguage | LANGUAGE | — | ✅ |
| 2 | SchedulePatternTLPEOSchedulePatternDesc | SCHEDULE_PATTERN_DESC | — | ✅ |
| 3 | SchedulePatternTLPEOSchedulePatternId | SCHEDULE_PATTERN_ID | — | — |
| 4 | SchedulePatternTLPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
