---
id: DOC-GL-PVO-PersonAccrualEntryPVO
doc_type: system-doc
title: "PersonAccrualEntryPVO — PVO General Ledger"
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
  - PersonAccrualEntryPVO
  - personaccrualentrypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonAccrualEntryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Person Accrual Entry. Acessa as tabelas: ANC_PER_ACCRUAL_ENTRIES, PER_ALL_ASSIGNMENTS_M, PER_ALL_PEOPLE_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GlobalAbsencesAM.PersonAccrualEntryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 3 | 1 | 16 | 57% |

---

## 🔗 Tabelas Relacionadas

- [[anc_per_accrual_entries|ANC_PER_ACCRUAL_ENTRIES]] — 19 atributos (1 PKs, 16 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 6 atributos
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 3 atributos

---

## ⚙️ Atributos

### [[anc_per_accrual_entries|ANC_PER_ACCRUAL_ENTRIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccrualPeriod | ACCRUAL_PERIOD | — | ✅ |
| 2 | Accrued | ACCRUED | — | ✅ |
| 3 | BeginBal | BEGIN_BAL | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | EndBal | END_BAL | — | ✅ |
| 7 | EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | PerAccrualEntryId | PER_ACCRUAL_ENTRY_ID | 🔑 | ✅ |
| 13 | PerPlanEnrtId | PER_PLAN_ENRT_ID | — | ✅ |
| 14 | PersonEventId | PERSON_EVENT_ID | — | — |
| 15 | PersonId | PERSON_ID | — | ✅ |
| 16 | PlanId | PLAN_ID | — | ✅ |
| 17 | PrdOfSvcId | PRD_OF_SVC_ID | — | ✅ |
| 18 | Used | USED | — | ✅ |
| 19 | WorkTermAsgId | WORK_TERM_ASG_ID | — | ✅ |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 2 | AssignmentPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | AssignmentPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 4 | AssignmentPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 5 | AssignmentPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 6 | AssignmentPEOWorkTermsAssignmentId | WORK_TERMS_ASSIGNMENT_ID | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | PersonId1 | PERSON_ID | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
