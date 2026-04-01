---
id: DOC-GL-PVO-PersonAbsTypeEntryPVO
doc_type: system-doc
title: "PersonAbsTypeEntryPVO — PVO General Ledger"
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
  - PersonAbsTypeEntryPVO
  - personabstypeentrypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonAbsTypeEntryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Person Abs Type Entry. Acessa as tabelas: ANC_PER_ABS_TYPE_ENTRIES, PER_ALL_ASSIGNMENTS_M, PER_ALL_PEOPLE_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GlobalAbsencesAM.PersonAbsTypeEntryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 42 | 3 | 1 | 23 | 55% |

---

## 🔗 Tabelas Relacionadas

- [[anc_per_abs_type_entries|ANC_PER_ABS_TYPE_ENTRIES]] — 34 atributos (1 PKs, 23 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 5 atributos
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 3 atributos

---

## ⚙️ Atributos

### [[anc_per_abs_type_entries|ANC_PER_ABS_TYPE_ENTRIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsenceStatus | ABSENCE_STATUS | — | ✅ |
| 2 | AbsenceTypeId | ABSENCE_TYPE_ID | — | ✅ |
| 3 | AbsenceTypeReasonId | ABSENCE_TYPE_REASON_ID | — | ✅ |
| 4 | ActualChildBirthDt | ACTUAL_CHILD_BIRTH_DT | — | — |
| 5 | ActualReturnDt | ACTUAL_RETURN_DT | — | — |
| 6 | ActualStDt | ACTUAL_ST_DT | — | — |
| 7 | AssignmentId | ASSIGNMENT_ID | — | ✅ |
| 8 | Comments | COMMENTS | — | — |
| 9 | CreatedBy | CREATED_BY | — | ✅ |
| 10 | CreationDate | CREATION_DATE | — | ✅ |
| 11 | EndDate | END_DATE | — | ✅ |
| 12 | EndDateDuration | END_DATE_DURATION | — | ✅ |
| 13 | EndDatetime | END_DATETIME | — | ✅ |
| 14 | EndTime | END_TIME | — | ✅ |
| 15 | EnterpriseId | ENTERPRISE_ID | — | — |
| 16 | ExpectedDtChildBirth | EXPECTED_DT_CHILD_BIRTH | — | — |
| 17 | IntendToWork | INTEND_TO_WORK | — | — |
| 18 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 21 | LeaveDuration | LEAVE_DURATION | — | ✅ |
| 22 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | PerAbsTypeEntryId | PER_ABS_TYPE_ENTRY_ID | 🔑 | ✅ |
| 24 | PerAbsenceEntryId | PER_ABSENCE_ENTRY_ID | — | ✅ |
| 25 | PersonId | PERSON_ID | — | ✅ |
| 26 | PlannedReturnDt | PLANNED_RETURN_DT | — | ✅ |
| 27 | PlannedStDt | PLANNED_ST_DT | — | — |
| 28 | Qty | QTY | — | ✅ |
| 29 | StartDate | START_DATE | — | ✅ |
| 30 | StartDateDuration | START_DATE_DURATION | — | ✅ |
| 31 | StartDatetime | START_DATETIME | — | ✅ |
| 32 | StartTime | START_TIME | — | ✅ |
| 33 | TmRecGrpId | TM_REC_GRP_ID | — | — |
| 34 | Uom | UOM | — | ✅ |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 2 | AssignmentPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | AssignmentPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 4 | AssignmentPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 5 | AssignmentPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | PersonId1 | PERSON_ID | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
