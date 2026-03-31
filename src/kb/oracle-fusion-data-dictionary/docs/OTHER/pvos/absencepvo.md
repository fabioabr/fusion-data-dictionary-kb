---
id: DOC-OTHER-PVO-AbsencePVO
doc_type: system-doc
title: "AbsencePVO — PVO Cross-Module"
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
  - AbsencePVO
  - absencepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AbsencePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Absence. Acessa as tabelas: PER_ABSENCE_ATTENDANCES.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AbsenceAM.AbsencePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 1 | 1 | 2 | 8% |

---

## 🔗 Tabelas Relacionadas

- [[per_absence_attendances|PER_ABSENCE_ATTENDANCES]] — 24 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[per_absence_attendances|PER_ABSENCE_ATTENDANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsenceAttendanceId | ABSENCE_ATTENDANCE_ID | 🔑 | ✅ |
| 2 | AbsencePEOAbsAttendanceReasonId | ABS_ATTENDANCE_REASON_ID | — | — |
| 3 | AbsencePEOAbsInformationCategory | ABS_INFORMATION_CATEGORY | — | — |
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

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
