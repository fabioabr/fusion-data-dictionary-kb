---
id: DOC-HCM-PVO-AssignmentSupervisorExtractPVO
doc_type: system-doc
title: "AssignmentSupervisorExtractPVO — PVO Human Capital Management"
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
  - AssignmentSupervisorExtractPVO
  - assignmentsupervisorextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssignmentSupervisorExtractPVO

## 📌 Visão Geral

Extrai supervisores de assignment via BICC com vigencia, acao e business group. Utilizado para cargas analiticas de hierarquia de reporte.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.AssignmentBiccExtractAM.AssignmentSupervisorExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 51 | 1 | 3 | 20 | 39% |

---

## 🔗 Tabelas Relacionadas

- [[per_assignment_supervisors_f|PER_ASSIGNMENT_SUPERVISORS_F]] — 51 atributos (3 PKs, 20 BICC)

---

## ⚙️ Atributos

### [[per_assignment_supervisors_f|PER_ASSIGNMENT_SUPERVISORS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 2 | AssignmentId | ASSIGNMENT_ID | — | ✅ |
| 3 | AssignmentSupervisorId | ASSIGNMENT_SUPERVISOR_ID | 🔑 | ✅ |
| 4 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 8 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 9 | FreezeStartDate | FREEZE_START_DATE | — | ✅ |
| 10 | FreezeUntilDate | FREEZE_UNTIL_DATE | — | ✅ |
| 11 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | ManagerAssignmentId | MANAGER_ASSIGNMENT_ID | — | ✅ |
| 15 | ManagerId | MANAGER_ID | — | ✅ |
| 16 | ManagerType | MANAGER_TYPE | — | ✅ |
| 17 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | PersonId | PERSON_ID | — | ✅ |
| 19 | PrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 20 | SupAttribute1 | SUP_ATTRIBUTE1 | — | — |
| 21 | SupAttribute10 | SUP_ATTRIBUTE10 | — | — |
| 22 | SupAttribute11 | SUP_ATTRIBUTE11 | — | — |
| 23 | SupAttribute12 | SUP_ATTRIBUTE12 | — | — |
| 24 | SupAttribute13 | SUP_ATTRIBUTE13 | — | — |
| 25 | SupAttribute14 | SUP_ATTRIBUTE14 | — | — |
| 26 | SupAttribute15 | SUP_ATTRIBUTE15 | — | — |
| 27 | SupAttribute16 | SUP_ATTRIBUTE16 | — | — |
| 28 | SupAttribute17 | SUP_ATTRIBUTE17 | — | — |
| 29 | SupAttribute18 | SUP_ATTRIBUTE18 | — | — |
| 30 | SupAttribute19 | SUP_ATTRIBUTE19 | — | — |
| 31 | SupAttribute2 | SUP_ATTRIBUTE2 | — | — |
| 32 | SupAttribute20 | SUP_ATTRIBUTE20 | — | — |
| 33 | SupAttribute21 | SUP_ATTRIBUTE21 | — | — |
| 34 | SupAttribute22 | SUP_ATTRIBUTE22 | — | — |
| 35 | SupAttribute23 | SUP_ATTRIBUTE23 | — | — |
| 36 | SupAttribute24 | SUP_ATTRIBUTE24 | — | — |
| 37 | SupAttribute25 | SUP_ATTRIBUTE25 | — | — |
| 38 | SupAttribute26 | SUP_ATTRIBUTE26 | — | — |
| 39 | SupAttribute27 | SUP_ATTRIBUTE27 | — | — |
| 40 | SupAttribute28 | SUP_ATTRIBUTE28 | — | — |
| 41 | SupAttribute29 | SUP_ATTRIBUTE29 | — | — |
| 42 | SupAttribute3 | SUP_ATTRIBUTE3 | — | — |
| 43 | SupAttribute30 | SUP_ATTRIBUTE30 | — | — |
| 44 | SupAttribute4 | SUP_ATTRIBUTE4 | — | — |
| 45 | SupAttribute5 | SUP_ATTRIBUTE5 | — | — |
| 46 | SupAttribute6 | SUP_ATTRIBUTE6 | — | — |
| 47 | SupAttribute7 | SUP_ATTRIBUTE7 | — | — |
| 48 | SupAttribute8 | SUP_ATTRIBUTE8 | — | — |
| 49 | SupAttribute9 | SUP_ATTRIBUTE9 | — | — |
| 50 | SupAttributeCategory | SUP_ATTRIBUTE_CATEGORY | — | — |
| 51 | WorkingPercentage | WORKING_PERCENTAGE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
