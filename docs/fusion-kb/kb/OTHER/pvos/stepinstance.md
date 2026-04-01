---
id: DOC-OTHER-PVO-StepInstance
doc_type: system-doc
title: "StepInstance — PVO Cross-Module"
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
  - StepInstance
  - stepinstance
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# StepInstance

## 📌 Visão Geral

View Object para extração BICC de dados de Step Instance. Acessa as tabelas: DOO_JEOPARDY_PRIORITIES, DOO_ORCHESTRATION_GROUPS, DOO_PROCESS_INSTANCES (+3).

**Caminho:** `FscmTopModelAM.DooTopAM.StepInstance`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 69 | 6 | 1 | 18 | 26% |

---

## 🔗 Tabelas Relacionadas

- [[doo_jeopardy_priorities|DOO_JEOPARDY_PRIORITIES]] — 2 atributos
- [[doo_orchestration_groups|DOO_ORCHESTRATION_GROUPS]] — 1 atributos
- [[doo_process_instances|DOO_PROCESS_INSTANCES]] — 21 atributos (2 BICC)
- [[doo_process_step_instances|DOO_PROCESS_STEP_INSTANCES]] — 22 atributos (1 PKs, 12 BICC)
- [[doo_task_instances|DOO_TASK_INSTANCES]] — 22 atributos (4 BICC)
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
| 1 | OrchestrationGroupGroupSeqId | GROUP_SEQ_ID | — | — |

### [[doo_process_instances|DOO_PROCESS_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessInstanceActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
| 2 | ProcessInstanceActualFulfillDate | ACTUAL_FULFILL_DATE | — | — |
| 3 | ProcessInstanceActualStartDate | ACTUAL_START_DATE | — | — |
| 4 | ProcessInstanceCreatedBy | CREATED_BY | — | — |
| 5 | ProcessInstanceCreationDate | CREATION_DATE | — | — |
| 6 | ProcessInstanceDooProcessId | DOO_PROCESS_ID | — | — |
| 7 | ProcessInstanceDooProcessInstanceId | DOO_PROCESS_INSTANCE_ID | — | ✅ |
| 8 | ProcessInstanceDooProcessVersion | DOO_PROCESS_VERSION | — | — |
| 9 | ProcessInstanceJeopardyReason | JEOPARDY_REASON | — | — |
| 10 | ProcessInstanceJeopardyReasonTaskInstId | JEOPARDY_REASON_TASK_INST_ID | — | — |
| 11 | ProcessInstanceJeopardyScore | JEOPARDY_SCORE | — | — |
| 12 | ProcessInstanceLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 13 | ProcessInstanceLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | ProcessInstanceLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | ProcessInstanceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | ProcessInstancePlannedCompletionDate | PLANNED_COMPLETION_DATE | — | — |
| 17 | ProcessInstancePlannedFulfillDate | PLANNED_FULFILL_DATE | — | — |
| 18 | ProcessInstanceProcessActive | PROCESS_ACTIVE | — | — |
| 19 | ProcessInstanceProcessNumber | PROCESS_NUMBER | — | ✅ |
| 20 | ProcessInstanceRequiredFulfillDate | REQUIRED_FULFILL_DATE | — | — |
| 21 | ProcessInstanceStatusCode | STATUS_CODE | — | — |

### [[doo_process_step_instances|DOO_PROCESS_STEP_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessStepInstanceActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 2 | ProcessStepInstanceActualStartDate | ACTUAL_START_DATE | — | ✅ |
| 3 | ProcessStepInstanceCreatedBy | CREATED_BY | — | — |
| 4 | ProcessStepInstanceCreationDate | CREATION_DATE | — | ✅ |
| 5 | ProcessStepInstanceDooProcessInstanceId | DOO_PROCESS_INSTANCE_ID | — | — |
| 6 | ProcessStepInstanceGroupId | GROUP_ID | — | — |
| 7 | ProcessStepInstanceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ProcessStepInstanceLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ProcessStepInstanceLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ProcessStepInstanceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ProcessStepInstancePlannedCompletionDate | PLANNED_COMPLETION_DATE | — | ✅ |
| 12 | ProcessStepInstancePlannedStartDate | PLANNED_START_DATE | — | ✅ |
| 13 | ProcessStepInstanceReferenceStepInstanceId | REFERENCE_STEP_INSTANCE_ID | — | — |
| 14 | ProcessStepInstanceRequiredCompletionDate | REQUIRED_COMPLETION_DATE | — | — |
| 15 | ProcessStepInstanceRequiredStartDate | REQUIRED_START_DATE | — | — |
| 16 | ProcessStepInstanceScheduledCompletionDate | SCHEDULED_COMPLETION_DATE | — | ✅ |
| 17 | ProcessStepInstanceScheduledStartDate | SCHEDULED_START_DATE | — | ✅ |
| 18 | ProcessStepInstanceStepActive | STEP_ACTIVE | — | ✅ |
| 19 | ProcessStepInstanceStepId | STEP_ID | — | ✅ |
| 20 | ProcessStepInstanceStepStatus | STEP_STATUS | — | ✅ |
| 21 | ProcessStepInstanceTaskInstanceId | TASK_INSTANCE_ID | — | — |
| 22 | StepInstanceId | STEP_INSTANCE_ID | 🔑 | ✅ |

### [[doo_task_instances|DOO_TASK_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskInstanceActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
| 2 | TaskInstanceActualStartDate | ACTUAL_START_DATE | — | — |
| 3 | TaskInstanceCreatedBy | CREATED_BY | — | — |
| 4 | TaskInstanceCreationDate | CREATION_DATE | — | — |
| 5 | TaskInstanceDooProcessInstanceId | DOO_PROCESS_INSTANCE_ID | — | — |
| 6 | TaskInstanceJeopardyReason | JEOPARDY_REASON | — | ✅ |
| 7 | TaskInstanceJeopardyScore | JEOPARDY_SCORE | — | ✅ |
| 8 | TaskInstanceLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 9 | TaskInstanceLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | TaskInstanceLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | TaskInstanceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | TaskInstancePlannedCompletionDate | PLANNED_COMPLETION_DATE | — | — |
| 13 | TaskInstancePlannedStartDate | PLANNED_START_DATE | — | — |
| 14 | TaskInstanceRequiredCompletionDate | REQUIRED_COMPLETION_DATE | — | — |
| 15 | TaskInstanceRequiredStartDate | REQUIRED_START_DATE | — | — |
| 16 | TaskInstanceRootParentGroupId | ROOT_PARENT_GROUP_ID | — | — |
| 17 | TaskInstanceScheduledCompletionDate | SCHEDULED_COMPLETION_DATE | — | — |
| 18 | TaskInstanceScheduledStartDate | SCHEDULED_START_DATE | — | — |
| 19 | TaskInstanceStatusCode | STATUS_CODE | — | ✅ |
| 20 | TaskInstanceStepActive | STEP_ACTIVE | — | — |
| 21 | TaskInstanceTaskId | TASK_ID | — | — |
| 22 | TaskInstanceTaskInstanceId | TASK_INSTANCE_ID | — | ✅ |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUBusinessUnitId | BU_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
