---
id: DOC-HCM-PVO-AbsenceEventFactPVO
doc_type: system-doc
title: "AbsenceEventFactPVO — PVO Human Capital Management"
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
  - AbsenceEventFactPVO
  - absenceeventfactpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AbsenceEventFactPVO

## 📌 Visão Geral

Extrai fatos diarios de ausencia por assignment, com quebra por dia e tipo. Utilizado para analise granular de absenteismo e calculo de dias perdidos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AbsenceAM.AbsenceEventFactPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 1 | 3 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[per_assignment_day_absences|PER_ASSIGNMENT_DAY_ABSENCES]] — 18 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[per_assignment_day_absences|PER_ASSIGNMENT_DAY_ABSENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsenseDailyBreakUpPEOAbsenceAttendanceId | ABSENCE_ATTENDANCE_ID | — | ✅ |
| 2 | AbsenseDailyBreakUpPEOAbsenceDate | ABSENCE_DATE | — | — |
| 3 | AbsenseDailyBreakUpPEOAbsenceDurationDays | ABSENCE_DURATION_DAYS | — | — |
| 4 | AbsenseDailyBreakUpPEOAbsenceDurationHours | ABSENCE_DURATION_HOURS | — | — |
| 5 | AbsenseDailyBreakUpPEOAsgAbsenceRecordingId | ASG_ABSENCE_RECORDING_ID | — | — |
| 6 | AbsenseDailyBreakUpPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 7 | AbsenseDailyBreakUpPEOCalendarEventDuration | CALENDAR_EVENT_DURATION | — | — |
| 8 | AbsenseDailyBreakUpPEOCreatedBy | CREATED_BY | — | — |
| 9 | AbsenseDailyBreakUpPEOCreationDate | CREATION_DATE | — | — |
| 10 | AbsenseDailyBreakUpPEODayType | DAY_TYPE | — | — |
| 11 | AbsenseDailyBreakUpPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | AbsenseDailyBreakUpPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | AbsenseDailyBreakUpPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | AbsenseDailyBreakUpPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | AbsenseDailyBreakUpPEOPersonId | PERSON_ID | — | — |
| 16 | AbsenseDailyBreakUpPEOScheduleWorkDuration | SCHEDULE_WORK_DURATION | — | — |
| 17 | AbsenseDailyBreakUpPEOWorkScheduleUnit | WORK_SCHEDULE_UNIT | — | — |
| 18 | AssignmentDayAbsenceId | ASSIGNMENT_DAY_ABSENCE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
