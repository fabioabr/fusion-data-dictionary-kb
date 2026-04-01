---
id: DOC-OTHER-PVO-TaskInstance
doc_type: system-doc
title: "TaskInstance — PVO Cross-Module"
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
  - TaskInstance
  - taskinstance
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaskInstance

## 📌 Visão Geral

View Object para extração BICC de dados de Task Instance. Acessa as tabelas: DOO_JEOPARDY_PRIORITIES, DOO_ORCHESTRATION_GROUPS, DOO_PROCESS_INSTANCES (+2).

**Caminho:** `FscmTopModelAM.DooTopAM.TaskInstance`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 49 | 5 | 1 | 17 | 35% |

---

## 🔗 Tabelas Relacionadas

- [[doo_jeopardy_priorities|DOO_JEOPARDY_PRIORITIES]] — 2 atributos
- [[doo_orchestration_groups|DOO_ORCHESTRATION_GROUPS]] — 1 atributos (1 BICC)
- [[doo_process_instances|DOO_PROCESS_INSTANCES]] — 23 atributos (2 BICC)
- [[doo_task_instances|DOO_TASK_INSTANCES]] — 22 atributos (1 PKs, 14 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 1 atributos

---

## ⚙️ Atributos

### [[doo_jeopardy_priorities|DOO_JEOPARDY_PRIORITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JeopardyPriorityJeopardyPriorityCode | JEOPARDY_PRIORITY_CODE | — | — |
| 2 | JeopardyPriorityJeopardyPriorityId | JEOPARDY_PRIORITY_ID | — | — |

### [[doo_orchestration_groups|DOO_ORCHESTRATION_GROUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrchestrationGroupGroupSeqId | GROUP_SEQ_ID | — | ✅ |

### [[doo_process_instances|DOO_PROCESS_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessInstanceActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
| 2 | ProcessInstanceActualFulfillDate | ACTUAL_FULFILL_DATE | — | — |
| 3 | ProcessInstanceActualStartDate | ACTUAL_START_DATE | — | — |
| 4 | ProcessInstanceBpelInstanceId | BPEL_INSTANCE_ID | — | — |
| 5 | ProcessInstanceCreatedBy | CREATED_BY | — | — |
| 6 | ProcessInstanceCreationDate | CREATION_DATE | — | — |
| 7 | ProcessInstanceDooProcessId | DOO_PROCESS_ID | — | — |
| 8 | ProcessInstanceDooProcessInstanceId | DOO_PROCESS_INSTANCE_ID | — | ✅ |
| 9 | ProcessInstanceDooProcessVersion | DOO_PROCESS_VERSION | — | — |
| 10 | ProcessInstanceJeopardyReason | JEOPARDY_REASON | — | — |
| 11 | ProcessInstanceJeopardyReasonTaskInstId | JEOPARDY_REASON_TASK_INST_ID | — | — |
| 12 | ProcessInstanceJeopardyScore | JEOPARDY_SCORE | — | — |
| 13 | ProcessInstanceLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 14 | ProcessInstanceLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | ProcessInstanceLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | ProcessInstanceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | ProcessInstancePlannedCompletionDate | PLANNED_COMPLETION_DATE | — | — |
| 18 | ProcessInstancePlannedFulfillDate | PLANNED_FULFILL_DATE | — | — |
| 19 | ProcessInstanceProcessActive | PROCESS_ACTIVE | — | — |
| 20 | ProcessInstanceProcessNumber | PROCESS_NUMBER | — | ✅ |
| 21 | ProcessInstanceReferenceProcessInstanceId | REFERENCE_PROCESS_INSTANCE_ID | — | — |
| 22 | ProcessInstanceRequiredFulfillDate | REQUIRED_FULFILL_DATE | — | — |
| 23 | ProcessInstanceStatusCode | STATUS_CODE | — | — |

### [[doo_task_instances|DOO_TASK_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskInstanceActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 2 | TaskInstanceActualStartDate | ACTUAL_START_DATE | — | ✅ |
| 3 | TaskInstanceCreatedBy | CREATED_BY | — | — |
| 4 | TaskInstanceCreationDate | CREATION_DATE | — | ✅ |
| 5 | TaskInstanceDooProcessInstanceId | DOO_PROCESS_INSTANCE_ID | — | — |
| 6 | TaskInstanceId | TASK_INSTANCE_ID | 🔑 | ✅ |
| 7 | TaskInstanceJeopardyReason | JEOPARDY_REASON | — | ✅ |
| 8 | TaskInstanceJeopardyScore | JEOPARDY_SCORE | — | ✅ |
| 9 | TaskInstanceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | TaskInstanceLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | TaskInstanceLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | TaskInstanceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | TaskInstancePlannedCompletionDate | PLANNED_COMPLETION_DATE | — | ✅ |
| 14 | TaskInstancePlannedStartDate | PLANNED_START_DATE | — | ✅ |
| 15 | TaskInstanceRequiredCompletionDate | REQUIRED_COMPLETION_DATE | — | — |
| 16 | TaskInstanceRequiredStartDate | REQUIRED_START_DATE | — | — |
| 17 | TaskInstanceRootParentGroupId | ROOT_PARENT_GROUP_ID | — | — |
| 18 | TaskInstanceScheduledCompletionDate | SCHEDULED_COMPLETION_DATE | — | ✅ |
| 19 | TaskInstanceScheduledStartDate | SCHEDULED_START_DATE | — | ✅ |
| 20 | TaskInstanceStatusCode | STATUS_CODE | — | ✅ |
| 21 | TaskInstanceStepActive | STEP_ACTIVE | — | ✅ |
| 22 | TaskInstanceTaskId | TASK_ID | — | ✅ |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUBusinessUnitId | BU_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
