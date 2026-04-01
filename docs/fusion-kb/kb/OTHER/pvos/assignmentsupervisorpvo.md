---
id: DOC-OTHER-PVO-AssignmentSupervisorPVO
doc_type: system-doc
title: "AssignmentSupervisorPVO — PVO Cross-Module"
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
  - AssignmentSupervisorPVO
  - assignmentsupervisorpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssignmentSupervisorPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Assignment Supervisor. Acessa as tabelas: PER_ASSIGNMENT_SUPERVISORS_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.AssignmentAM.AssignmentSupervisorPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 1 | 2 | 18 | 90% |

---

## 🔗 Tabelas Relacionadas

- [[per_assignment_supervisors_f|PER_ASSIGNMENT_SUPERVISORS_F]] — 20 atributos (2 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[per_assignment_supervisors_f|PER_ASSIGNMENT_SUPERVISORS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentSupervisorId | ASSIGNMENT_SUPERVISOR_ID | 🔑 | ✅ |
| 2 | AssignmentSupervisorPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 3 | AssignmentSupervisorPEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 4 | AssignmentSupervisorPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 5 | AssignmentSupervisorPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | AssignmentSupervisorPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | AssignmentSupervisorPEOFreezeStartDate | FREEZE_START_DATE | — | ✅ |
| 8 | AssignmentSupervisorPEOFreezeUntilDate | FREEZE_UNTIL_DATE | — | ✅ |
| 9 | AssignmentSupervisorPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | AssignmentSupervisorPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | AssignmentSupervisorPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | AssignmentSupervisorPEOManagerAssignmentId | MANAGER_ASSIGNMENT_ID | — | ✅ |
| 13 | AssignmentSupervisorPEOManagerId | MANAGER_ID | — | ✅ |
| 14 | AssignmentSupervisorPEOManagerType | MANAGER_TYPE | — | ✅ |
| 15 | AssignmentSupervisorPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | AssignmentSupervisorPEOPersonId | PERSON_ID | — | ✅ |
| 17 | AssignmentSupervisorPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 18 | AssignmentSupervisorPEOWorkingPercentage | WORKING_PERCENTAGE | — | ✅ |
| 19 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 20 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
