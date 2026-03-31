---
id: DOC-GL-PVO-PersonAbsEntryPVO
doc_type: system-doc
title: "PersonAbsEntryPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PersonAbsEntryPVO
  - personabsentrypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonAbsEntryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Person Abs Entry. Acessa as tabelas: ANC_PER_ABS_ENTRIES, PER_ALL_PEOPLE_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GlobalAbsencesAM.PersonAbsEntryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 63 | 2 | 2 | 43 | 68% |

---

## 🔗 Tabelas Relacionadas

- [[anc_per_abs_entries|ANC_PER_ABS_ENTRIES]] — 60 atributos (2 PKs, 43 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 3 atributos

---

## ⚙️ Atributos

### [[anc_per_abs_entries|ANC_PER_ABS_ENTRIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsenceCaseId | ABSENCE_CASE_ID | — | — |
| 2 | AbsenceEntryBasicFlag | ABSENCE_ENTRY_BASIC_FLAG | — | ✅ |
| 3 | AbsencePatternCd | ABSENCE_PATTERN_CD | — | ✅ |
| 4 | AbsenceStatusCd | ABSENCE_STATUS_CD | — | ✅ |
| 5 | AbsenceTypeId | ABSENCE_TYPE_ID | — | — |
| 6 | AbsenceTypeReasonId | ABSENCE_TYPE_REASON_ID | — | ✅ |
| 7 | ApprovalStatusCd | APPROVAL_STATUS_CD | — | ✅ |
| 8 | AuthStatusUpdateDate | AUTH_STATUS_UPDATE_DATE | — | ✅ |
| 9 | BlockedLeaveCandidate | BLOCKED_LEAVE_CANDIDATE | — | ✅ |
| 10 | CertificationAuthFlag | CERTIFICATION_AUTH_FLAG | — | ✅ |
| 11 | ChildEventTypeCd | CHILD_EVENT_TYPE_CD | — | ✅ |
| 12 | Comments | COMMENTS | — | ✅ |
| 13 | ConditionStartDate | CONDITION_START_DATE | — | ✅ |
| 14 | ConfirmedDate | CONFIRMED_DATE | — | ✅ |
| 15 | CreatedBy | CREATED_BY | — | ✅ |
| 16 | CreationDate | CREATION_DATE | — | ✅ |
| 17 | DiseaseCode | DISEASE_CODE | — | ✅ |
| 18 | Duration | DURATION | — | ✅ |
| 19 | EndDate | END_DATE | — | — |
| 20 | EndDateDuration | END_DATE_DURATION | — | ✅ |
| 21 | EndDatetime | END_DATETIME | — | ✅ |
| 22 | EndTime | END_TIME | — | ✅ |
| 23 | EnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 24 | EstablishmentDate | ESTABLISHMENT_DATE | — | ✅ |
| 25 | Frequency | FREQUENCY | — | ✅ |
| 26 | InitialReportById | INITIAL_REPORT_BY_ID | — | ✅ |
| 27 | InitialTimelyNotifyFlag | INITIAL_TIMELY_NOTIFY_FLAG | — | ✅ |
| 28 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 29 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 30 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 31 | LateNotifyFlag | LATE_NOTIFY_FLAG | — | ✅ |
| 32 | LegalEntityId | LEGAL_ENTITY_ID | — | — |
| 33 | LegislationCode | LEGISLATION_CODE | — | — |
| 34 | LegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 35 | NotificationDate | NOTIFICATION_DATE | — | ✅ |
| 36 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 37 | OpenEndedFlag | OPEN_ENDED_FLAG | — | ✅ |
| 38 | Overridden | OVERRIDDEN | — | — |
| 39 | PerAbsenceEntryId | PER_ABSENCE_ENTRY_ID | 🔑 | ✅ |
| 40 | PeriodOfIncapToWorkFlag | PERIOD_OF_INCAP_TO_WORK_FLAG | — | ✅ |
| 41 | PeriodOfServiceId | PERIOD_OF_SERVICE_ID | — | — |
| 42 | PersonAbsEntryPEOApprovalDatetime | APPROVAL_DATETIME | — | — |
| 43 | PersonAbsEntryPEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 44 | PersonAbsEntryPEOEndDtDurPrefCd | END_DT_DUR_PREF_CD | — | — |
| 45 | PersonAbsEntryPEOStartDtDurPrefCd | START_DT_DUR_PREF_CD | — | — |
| 46 | PersonId | PERSON_ID | — | — |
| 47 | PlannedEndDate | PLANNED_END_DATE | — | — |
| 48 | ProcessingStatus | PROCESSING_STATUS | — | — |
| 49 | ProjectId | PROJECT_ID | — | ✅ |
| 50 | SingleDayFlag | SINGLE_DAY_FLAG | — | ✅ |
| 51 | Source | SOURCE | — | ✅ |
| 52 | SplCondition | SPL_CONDITION | — | ✅ |
| 53 | StartDate | START_DATE | — | ✅ |
| 54 | StartDateDuration | START_DATE_DURATION | — | ✅ |
| 55 | StartDatetime | START_DATETIME | — | ✅ |
| 56 | StartTime | START_TIME | — | ✅ |
| 57 | SubmittedDate | SUBMITTED_DATE | — | ✅ |
| 58 | TimelinessOverrideDate | TIMELINESS_OVERRIDE_DATE | — | ✅ |
| 59 | Uom | UOM | — | — |
| 60 | UserMode | USER_MODE | — | ✅ |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | PersonId1 | PERSON_ID | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
