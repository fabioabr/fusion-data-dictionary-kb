---
id: DOC-GL-PVO-PersonAbsPlanEntryPVO
doc_type: system-doc
title: "PersonAbsPlanEntryPVO — PVO General Ledger"
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
  - PersonAbsPlanEntryPVO
  - personabsplanentrypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonAbsPlanEntryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Person Abs Plan Entry. Acessa as tabelas: ANC_PER_ABS_PLAN_ENTRIES, PER_ALL_ASSIGNMENTS_M, PER_ALL_PEOPLE_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GlobalAbsencesAM.PersonAbsPlanEntryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 37 | 3 | 1 | 14 | 38% |

---

## 🔗 Tabelas Relacionadas

- [[anc_per_abs_plan_entries|ANC_PER_ABS_PLAN_ENTRIES]] — 29 atributos (1 PKs, 13 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 5 atributos
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[anc_per_abs_plan_entries|ANC_PER_ABS_PLAN_ENTRIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsUnits | ABS_UNITS | — | ✅ |
| 2 | AbsencePayFactor | ABSENCE_PAY_FACTOR | — | ✅ |
| 3 | AbsencePlanId | ABSENCE_PLAN_ID | — | — |
| 4 | AssignmentId | ASSIGNMENT_ID | — | — |
| 5 | CreatedBy | CREATED_BY | — | — |
| 6 | CreationDate | CREATION_DATE | — | — |
| 7 | EndDate | END_DATE | — | ✅ |
| 8 | EndDatetime | END_DATETIME | — | ✅ |
| 9 | EndTime | END_TIME | — | ✅ |
| 10 | EnterpriseId | ENTERPRISE_ID | — | — |
| 11 | EntitlementDate | ENTITLEMENT_DATE | — | — |
| 12 | HeaderId | HEADER_ID | — | ✅ |
| 13 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | PerAbsPlanEntryId | PER_ABS_PLAN_ENTRY_ID | 🔑 | ✅ |
| 18 | PerAbsPlnSummEntryId | PER_ABS_PLN_SUMM_ENTRY_ID | — | — |
| 19 | PerAbsTypeEntryId | PER_ABS_TYPE_ENTRY_ID | — | — |
| 20 | PerAbsenceEntryId | PER_ABSENCE_ENTRY_ID | — | — |
| 21 | PersonId | PERSON_ID | — | — |
| 22 | QualificationDate | QUALIFICATION_DATE | — | — |
| 23 | RateDefinitionId | RATE_DEFINITION_ID | — | ✅ |
| 24 | ScheduledUnits | SCHEDULED_UNITS | — | ✅ |
| 25 | StartDate | START_DATE | — | ✅ |
| 26 | StartDatetime | START_DATETIME | — | ✅ |
| 27 | StartTime | START_TIME | — | ✅ |
| 28 | TmRecId | TM_REC_ID | — | — |
| 29 | Uom | UOM | — | — |

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
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonId1 | PERSON_ID | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
