---
id: DOC-OTHER-PVO-MntSchedulePatternExtractPVO
doc_type: system-doc
title: "MntSchedulePatternExtractPVO — PVO Cross-Module"
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
  - MntSchedulePatternExtractPVO
  - mntschedulepatternextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MntSchedulePatternExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Mnt Schedule Pattern Extract. Acessa as tabelas: MNT_SCHEDULE_PATTERNS_B, MNT_SCHEDULE_PATTERNS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.MntBiccExtractAM.MntSchedulePatternExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 81 | 2 | 3 | 81 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[mnt_schedule_patterns_b|MNT_SCHEDULE_PATTERNS_B]] — 71 atributos (1 PKs, 71 BICC)
- [[mnt_schedule_patterns_tl|MNT_SCHEDULE_PATTERNS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[mnt_schedule_patterns_b|MNT_SCHEDULE_PATTERNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 2 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 3 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 4 | AttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 5 | AttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 6 | AttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 7 | AttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 8 | AttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 9 | AttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 10 | AttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 11 | AttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 12 | AttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 13 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 14 | AttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 15 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 16 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 17 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 18 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 19 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 20 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 21 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 22 | AttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 23 | AttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 24 | AttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 25 | AttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 26 | AttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 27 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 28 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 29 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 30 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 31 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 32 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 33 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 34 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 35 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 36 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 37 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 38 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 39 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 40 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 41 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 42 | CreatedBy | CREATED_BY | — | ✅ |
| 43 | CreationDate | CREATION_DATE | — | ✅ |
| 44 | CycleInterval | CYCLE_INTERVAL | — | ✅ |
| 45 | DailyEveryWeekdayFlag | DAILY_EVERY_WEEKDAY_FLAG | — | ✅ |
| 46 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 47 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 48 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 49 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 50 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 51 | MonthlySpecificDay | MONTHLY_SPECIFIC_DAY | — | ✅ |
| 52 | MonthlyWeekday | MONTHLY_WEEKDAY | — | ✅ |
| 53 | MonthlyWeekdayOrdinal | MONTHLY_WEEKDAY_ORDINAL | — | ✅ |
| 54 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 55 | ProgramId | PROGRAM_ID | — | ✅ |
| 56 | RequestId | REQUEST_ID | — | ✅ |
| 57 | SchedulePatternId | SCHEDULE_PATTERN_ID | 🔑 | ✅ |
| 58 | SchedulePatternName | SCHEDULE_PATTERN_NAME | — | ✅ |
| 59 | SchedulePatternType | SCHEDULE_PATTERN_TYPE | — | ✅ |
| 60 | WeeklyDayFridayFlag | WEEKLY_DAY_FRIDAY_FLAG | — | ✅ |
| 61 | WeeklyDayMondayFlag | WEEKLY_DAY_MONDAY_FLAG | — | ✅ |
| 62 | WeeklyDaySaturdayFlag | WEEKLY_DAY_SATURDAY_FLAG | — | ✅ |
| 63 | WeeklyDaySundayFlag | WEEKLY_DAY_SUNDAY_FLAG | — | ✅ |
| 64 | WeeklyDayThursdayFlag | WEEKLY_DAY_THURSDAY_FLAG | — | ✅ |
| 65 | WeeklyDayTuesdayFlag | WEEKLY_DAY_TUESDAY_FLAG | — | ✅ |
| 66 | WeeklyDayWednesdayFlag | WEEKLY_DAY_WEDNESDAY_FLAG | — | ✅ |
| 67 | YearlyMonth | YEARLY_MONTH | — | ✅ |
| 68 | YearlySpecificDay | YEARLY_SPECIFIC_DAY | — | ✅ |
| 69 | YearlySpecificMonth | YEARLY_SPECIFIC_MONTH | — | ✅ |
| 70 | YearlyWeekday | YEARLY_WEEKDAY | — | ✅ |
| 71 | YearlyWeekdayOrdinal | YEARLY_WEEKDAY_ORDINAL | — | ✅ |

### [[mnt_schedule_patterns_tl|MNT_SCHEDULE_PATTERNS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MntSchedulePatternTranslatio1CreatedBy | CREATED_BY | — | ✅ |
| 2 | MntSchedulePatternTranslatio1CreationDate | CREATION_DATE | — | ✅ |
| 3 | MntSchedulePatternTranslatio1Language | LANGUAGE | 🔑 | ✅ |
| 4 | MntSchedulePatternTranslatio1LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | MntSchedulePatternTranslatio1LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | MntSchedulePatternTranslatio1LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | MntSchedulePatternTranslatio1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | MntSchedulePatternTranslatio1SchedulePatternDesc | SCHEDULE_PATTERN_DESC | — | ✅ |
| 9 | MntSchedulePatternTranslatio1SchedulePatternId | SCHEDULE_PATTERN_ID | 🔑 | ✅ |
| 10 | MntSchedulePatternTranslatio1SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
