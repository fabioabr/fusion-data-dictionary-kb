---
id: DOC-OTHER-PVO-AssignmentTasksPVO
doc_type: system-doc
title: "AssignmentTasksPVO — PVO Cross-Module"
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
  - AssignmentTasksPVO
  - assignmenttaskspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssignmentTasksPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Assignment Tasks. Acessa as tabelas: WLF_ASSIGNMENT_TASKS_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.AssignmentTasksPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 1 | 3 | 14 | 52% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_assignment_tasks_f|WLF_ASSIGNMENT_TASKS_F]] — 27 atributos (3 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[wlf_assignment_tasks_f|WLF_ASSIGNMENT_TASKS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentTasksDEOAssignmentRecordId | ASSIGNMENT_RECORD_ID | — | — |
| 2 | AssignmentTasksDEOAssignmentTaskId | ASSIGNMENT_TASK_ID | 🔑 | ✅ |
| 3 | AssignmentTasksDEOCompletionDate | COMPLETION_DATE | — | ✅ |
| 4 | AssignmentTasksDEOCreatedBy | CREATED_BY | — | — |
| 5 | AssignmentTasksDEOCreationDate | CREATION_DATE | — | — |
| 6 | AssignmentTasksDEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 7 | AssignmentTasksDEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 8 | AssignmentTasksDEOEffort | EFFORT | — | ✅ |
| 9 | AssignmentTasksDEOEffortUom | EFFORT_UOM | — | ✅ |
| 10 | AssignmentTasksDEOEnterpriseId | ENTERPRISE_ID | — | — |
| 11 | AssignmentTasksDEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | AssignmentTasksDEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | AssignmentTasksDEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | AssignmentTasksDEOLearningItemId | LEARNING_ITEM_ID | — | ✅ |
| 15 | AssignmentTasksDEONotes | NOTES | — | ✅ |
| 16 | AssignmentTasksDEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | AssignmentTasksDEOParentTaskId | PARENT_TASK_ID | — | — |
| 18 | AssignmentTasksDEOReasonCode | REASON_CODE | — | ✅ |
| 19 | AssignmentTasksDEOScore | SCORE | — | ✅ |
| 20 | AssignmentTasksDEOSourceObjectCode | SOURCE_OBJECT_CODE | — | — |
| 21 | AssignmentTasksDEOSourceObjectId | SOURCE_OBJECT_ID | — | — |
| 22 | AssignmentTasksDEOSourceObjectType | SOURCE_OBJECT_TYPE | — | — |
| 23 | AssignmentTasksDEOTaskOwnerId | TASK_OWNER_ID | — | — |
| 24 | AssignmentTasksDEOTaskOwnerType | TASK_OWNER_TYPE | — | — |
| 25 | AssignmentTasksDEOTaskStatus | TASK_STATUS | — | ✅ |
| 26 | AssignmentTasksDEOTaskSubStatus | TASK_SUB_STATUS | — | ✅ |
| 27 | AssignmentTasksDEOTrainingEffort | TRAINING_EFFORT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
