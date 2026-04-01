---
id: DOC-HCM-PVO-AbsenceEventsPVO
doc_type: system-doc
title: "AbsenceEventsPVO — PVO Human Capital Management"
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
  - AbsenceEventsPVO
  - absenceeventspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AbsenceEventsPVO

## 📌 Visão Geral

Consolida eventos de ausencia com tipo, motivo, periodo e status. Suporta gestao de licencas, afastamentos e controle de absenteismo.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AbsenceAM.AbsenceEventsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 70 | 4 | 1 | 6 | 9% |

---

## 🔗 Tabelas Relacionadas

- [[per_absence_attendances|PER_ABSENCE_ATTENDANCES]] — 24 atributos (1 BICC)
- [[per_absence_attendance_types_b|PER_ABSENCE_ATTENDANCE_TYPES_B]] — 21 atributos (1 BICC)
- [[per_abs_attendance_reasons|PER_ABS_ATTENDANCE_REASONS]] — 11 atributos (1 BICC)
- [[per_asg_absence_recording|PER_ASG_ABSENCE_RECORDING]] — 14 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[per_absence_attendances|PER_ABSENCE_ATTENDANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsencePEOAbsAttendanceReasonId | ABS_ATTENDANCE_REASON_ID | — | — |
| 2 | AbsencePEOAbsInformationCategory | ABS_INFORMATION_CATEGORY | — | — |
| 3 | AbsencePEOAbsenceAttendanceId | ABSENCE_ATTENDANCE_ID | — | — |
| 4 | AbsencePEOAbsenceAttendanceTypeId | ABSENCE_ATTENDANCE_TYPE_ID | — | — |
| 5 | AbsencePEOAbsenceCaseId | ABSENCE_CASE_ID | — | — |
| 6 | AbsencePEOBatchId | BATCH_ID | — | — |
| 7 | AbsencePEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 8 | AbsencePEOCreatedBy | CREATED_BY | — | — |
| 9 | AbsencePEOCreationDate | CREATION_DATE | — | — |
| 10 | AbsencePEODateEnd | DATE_END | — | — |
| 11 | AbsencePEODateNotification | DATE_NOTIFICATION | — | — |
| 12 | AbsencePEODateProjectedEnd | DATE_PROJECTED_END | — | — |
| 13 | AbsencePEODateProjectedStart | DATE_PROJECTED_START | — | — |
| 14 | AbsencePEODateStart | DATE_START | — | — |
| 15 | AbsencePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | AbsencePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | AbsencePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | AbsencePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | AbsencePEOPeriodOfIncapacityId | PERIOD_OF_INCAPACITY_ID | — | — |
| 20 | AbsencePEOPersonId | PERSON_ID | — | — |
| 21 | AbsencePEOTimeEnd | TIME_END | — | — |
| 22 | AbsencePEOTimeProjectedEnd | TIME_PROJECTED_END | — | — |
| 23 | AbsencePEOTimeProjectedStart | TIME_PROJECTED_START | — | — |
| 24 | AbsencePEOTimeStart | TIME_START | — | — |

### [[per_absence_attendance_types_b|PER_ABSENCE_ATTENDANCE_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsenceTypePEOAbsenceAttendanceTypeId | ABSENCE_ATTENDANCE_TYPE_ID | — | — |
| 2 | AbsenceTypePEOAbsenceCategory | ABSENCE_CATEGORY | — | — |
| 3 | AbsenceTypePEOAbsenceOverlapFlag | ABSENCE_OVERLAP_FLAG | — | — |
| 4 | AbsenceTypePEOAssignmentStatusTypeId | ASSIGNMENT_STATUS_TYPE_ID | — | — |
| 5 | AbsenceTypePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 6 | AbsenceTypePEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 7 | AbsenceTypePEOCreatedBy | CREATED_BY | — | — |
| 8 | AbsenceTypePEOCreationDate | CREATION_DATE | — | — |
| 9 | AbsenceTypePEODateEffective | DATE_EFFECTIVE | — | — |
| 10 | AbsenceTypePEODateEnd | DATE_END | — | — |
| 11 | AbsenceTypePEOHoursOrDays | HOURS_OR_DAYS | — | — |
| 12 | AbsenceTypePEOIncreasingOrDecreasingFlag | INCREASING_OR_DECREASING_FLAG | — | — |
| 13 | AbsenceTypePEOInputValueId | INPUT_VALUE_ID | — | — |
| 14 | AbsenceTypePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | AbsenceTypePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | AbsenceTypePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | AbsenceTypePEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 18 | AbsenceTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | AbsenceTypePEOOverrideFlag | OVERRIDE_FLAG | — | — |
| 20 | AbsenceTypePEOPerOrWorkrelFlag | PER_OR_WORKREL_FLAG | — | — |
| 21 | AbsenceTypePEOSchBasedDur | SCH_BASED_DUR | — | — |

### [[per_abs_attendance_reasons|PER_ABS_ATTENDANCE_REASONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsenceReasonPEOAbsAttendanceReasonId | ABS_ATTENDANCE_REASON_ID | — | — |
| 2 | AbsenceReasonPEOAbsenceAttendanceTypeId | ABSENCE_ATTENDANCE_TYPE_ID | — | — |
| 3 | AbsenceReasonPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | AbsenceReasonPEOCreatedBy | CREATED_BY | — | — |
| 5 | AbsenceReasonPEOCreationDate | CREATION_DATE | — | — |
| 6 | AbsenceReasonPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AbsenceReasonPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | AbsenceReasonPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | AbsenceReasonPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 10 | AbsenceReasonPEOName | NAME | — | — |
| 11 | AbsenceReasonPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[per_asg_absence_recording|PER_ASG_ABSENCE_RECORDING]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsenceAssignmentPEOAbsenceAttendanceId | ABSENCE_ATTENDANCE_ID | — | ✅ |
| 2 | AbsenceAssignmentPEOAbsenceDays | ABSENCE_DAYS | — | — |
| 3 | AbsenceAssignmentPEOAbsenceHours | ABSENCE_HOURS | — | — |
| 4 | AbsenceAssignmentPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 5 | AbsenceAssignmentPEOAuthorisingPersonId | AUTHORISING_PERSON_ID | — | — |
| 6 | AbsenceAssignmentPEOCreatedBy | CREATED_BY | — | — |
| 7 | AbsenceAssignmentPEOCreationDate | CREATION_DATE | — | — |
| 8 | AbsenceAssignmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | AbsenceAssignmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | AbsenceAssignmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | AbsenceAssignmentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | AbsenceAssignmentPEOPersonId | PERSON_ID | — | — |
| 13 | AbsenceAssignmentPEOReplacementPersonId | REPLACEMENT_PERSON_ID | — | — |
| 14 | AsgAbsenceRecordingId | ASG_ABSENCE_RECORDING_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
