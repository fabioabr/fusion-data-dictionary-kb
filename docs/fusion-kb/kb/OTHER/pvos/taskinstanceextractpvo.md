---
id: DOC-OTHER-PVO-TaskInstanceExtractPVO
doc_type: system-doc
title: "TaskInstanceExtractPVO — PVO Cross-Module"
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
  - TaskInstanceExtractPVO
  - taskinstanceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaskInstanceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Task Instance Extract. Acessa as tabelas: DOO_TASK_INSTANCES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.TaskInstanceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 1 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_task_instances|DOO_TASK_INSTANCES]] — 22 atributos (1 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[doo_task_instances|DOO_TASK_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskInstanceActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 2 | TaskInstanceActualStartDate | ACTUAL_START_DATE | — | ✅ |
| 3 | TaskInstanceCreatedBy | CREATED_BY | — | ✅ |
| 4 | TaskInstanceCreationDate | CREATION_DATE | — | ✅ |
| 5 | TaskInstanceDooProcessInstanceId | DOO_PROCESS_INSTANCE_ID | — | ✅ |
| 6 | TaskInstanceJeopardyReason | JEOPARDY_REASON | — | ✅ |
| 7 | TaskInstanceJeopardyScore | JEOPARDY_SCORE | — | ✅ |
| 8 | TaskInstanceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | TaskInstanceLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | TaskInstanceLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | TaskInstanceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | TaskInstancePlannedCompletionDate | PLANNED_COMPLETION_DATE | — | ✅ |
| 13 | TaskInstancePlannedStartDate | PLANNED_START_DATE | — | ✅ |
| 14 | TaskInstanceRequiredCompletionDate | REQUIRED_COMPLETION_DATE | — | ✅ |
| 15 | TaskInstanceRequiredStartDate | REQUIRED_START_DATE | — | ✅ |
| 16 | TaskInstanceRootParentGroupId | ROOT_PARENT_GROUP_ID | — | ✅ |
| 17 | TaskInstanceScheduledCompletionDate | SCHEDULED_COMPLETION_DATE | — | ✅ |
| 18 | TaskInstanceScheduledStartDate | SCHEDULED_START_DATE | — | ✅ |
| 19 | TaskInstanceStatusCode | STATUS_CODE | — | ✅ |
| 20 | TaskInstanceStepActive | STEP_ACTIVE | — | ✅ |
| 21 | TaskInstanceTaskId | TASK_ID | — | ✅ |
| 22 | TaskInstanceTaskInstanceId | TASK_INSTANCE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
