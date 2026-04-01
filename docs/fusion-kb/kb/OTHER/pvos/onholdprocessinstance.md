---
id: DOC-OTHER-PVO-OnHoldProcessInstance
doc_type: system-doc
title: "OnHoldProcessInstance — PVO Cross-Module"
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
  - OnHoldProcessInstance
  - onholdprocessinstance
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OnHoldProcessInstance

## 📌 Visão Geral

View Object para extração BICC de dados de On Hold Process Instance. Acessa as tabelas: DOO_JEOPARDY_PRIORITIES, DOO_ORCHESTRATION_GROUPS, DOO_PROCESS_INSTANCES (+1).

**Caminho:** `FscmTopModelAM.DooTopAM.OnHoldProcessInstance`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 4 | 1 | 7 | 24% |

---

## 🔗 Tabelas Relacionadas

- [[doo_jeopardy_priorities|DOO_JEOPARDY_PRIORITIES]] — 2 atributos
- [[doo_orchestration_groups|DOO_ORCHESTRATION_GROUPS]] — 2 atributos
- [[doo_process_instances|DOO_PROCESS_INSTANCES]] — 23 atributos (1 PKs, 7 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 2 atributos

---

## ⚙️ Atributos

### [[doo_jeopardy_priorities|DOO_JEOPARDY_PRIORITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JeopardyPriorityCode | JEOPARDY_PRIORITY_CODE | — | — |
| 2 | JeopardyPriorityId | JEOPARDY_PRIORITY_ID | — | — |

### [[doo_orchestration_groups|DOO_ORCHESTRATION_GROUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrchestrationGroupGroupSeqId | GROUP_SEQ_ID | — | — |
| 2 | OrchestrationGroupOrgId | ORG_ID | — | — |

### [[doo_process_instances|DOO_PROCESS_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DooProcessInstanceId | DOO_PROCESS_INSTANCE_ID | 🔑 | ✅ |
| 2 | ProcessInstanceActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
| 3 | ProcessInstanceActualFulfillDate | ACTUAL_FULFILL_DATE | — | — |
| 4 | ProcessInstanceActualStartDate | ACTUAL_START_DATE | — | — |
| 5 | ProcessInstanceBpelInstanceId | BPEL_INSTANCE_ID | — | — |
| 6 | ProcessInstanceCreatedBy | CREATED_BY | — | — |
| 7 | ProcessInstanceCreationDate | CREATION_DATE | — | — |
| 8 | ProcessInstanceDooProcessId | DOO_PROCESS_ID | — | ✅ |
| 9 | ProcessInstanceDooProcessVersion | DOO_PROCESS_VERSION | — | — |
| 10 | ProcessInstanceJeopardyReason | JEOPARDY_REASON | — | ✅ |
| 11 | ProcessInstanceJeopardyReasonTaskInstId | JEOPARDY_REASON_TASK_INST_ID | — | — |
| 12 | ProcessInstanceJeopardyScore | JEOPARDY_SCORE | — | ✅ |
| 13 | ProcessInstanceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | ProcessInstanceLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | ProcessInstanceLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | ProcessInstanceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | ProcessInstancePlannedCompletionDate | PLANNED_COMPLETION_DATE | — | — |
| 18 | ProcessInstancePlannedFulfillDate | PLANNED_FULFILL_DATE | — | — |
| 19 | ProcessInstanceProcessActive | PROCESS_ACTIVE | — | ✅ |
| 20 | ProcessInstanceProcessNumber | PROCESS_NUMBER | — | ✅ |
| 21 | ProcessInstanceReferenceProcessInstanceId | REFERENCE_PROCESS_INSTANCE_ID | — | — |
| 22 | ProcessInstanceRequiredFulfillDate | REQUIRED_FULFILL_DATE | — | — |
| 23 | ProcessInstanceStatusCode | STATUS_CODE | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUBusinessUnitId | BU_ID | — | — |
| 2 | BUName | BU_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
