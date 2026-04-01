---
id: DOC-OTHER-PVO-ProcessInstance
doc_type: system-doc
title: "ProcessInstance — PVO Cross-Module"
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
  - ProcessInstance
  - processinstance
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProcessInstance

## 📌 Visão Geral

View Object para extração BICC de dados de Process Instance. Acessa as tabelas: DOO_JEOPARDY_PRIORITIES, DOO_ORCHESTRATION_GROUPS, DOO_PROCESS_INSTANCES (+1).

**Caminho:** `FscmTopModelAM.DooTopAM.ProcessInstance`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 4 | 1 | 19 | 76% |

---

## 🔗 Tabelas Relacionadas

- [[doo_jeopardy_priorities|DOO_JEOPARDY_PRIORITIES]] — 2 atributos (1 BICC)
- [[doo_orchestration_groups|DOO_ORCHESTRATION_GROUPS]] — 1 atributos (1 BICC)
- [[doo_process_instances|DOO_PROCESS_INSTANCES]] — 21 atributos (1 PKs, 16 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 1 atributos (1 BICC)

---

## ⚙️ Atributos

### [[doo_jeopardy_priorities|DOO_JEOPARDY_PRIORITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JeopardyPriorityCode | JEOPARDY_PRIORITY_CODE | — | ✅ |
| 2 | JeopardyPriorityId | JEOPARDY_PRIORITY_ID | — | — |

### [[doo_orchestration_groups|DOO_ORCHESTRATION_GROUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrchestrationGroupGroupSeqId | GROUP_SEQ_ID | — | ✅ |

### [[doo_process_instances|DOO_PROCESS_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 2 | ActualFulfillDate | ACTUAL_FULFILL_DATE | — | — |
| 3 | ActualStartDate | ACTUAL_START_DATE | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | DooProcessId | DOO_PROCESS_ID | — | ✅ |
| 7 | DooProcessInstanceId | DOO_PROCESS_INSTANCE_ID | 🔑 | ✅ |
| 8 | DooProcessVersion | DOO_PROCESS_VERSION | — | ✅ |
| 9 | JeopardyReason | JEOPARDY_REASON | — | ✅ |
| 10 | JeopardyReasonTaskInstId | JEOPARDY_REASON_TASK_INST_ID | — | — |
| 11 | JeopardyScore | JEOPARDY_SCORE | — | ✅ |
| 12 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | PlannedCompletionDate | PLANNED_COMPLETION_DATE | — | ✅ |
| 17 | PlannedFulfillDate | PLANNED_FULFILL_DATE | — | — |
| 18 | ProcessActive | PROCESS_ACTIVE | — | ✅ |
| 19 | ProcessNumber | PROCESS_NUMBER | — | ✅ |
| 20 | RequiredFulfillDate | REQUIRED_FULFILL_DATE | — | ✅ |
| 21 | StatusCode | STATUS_CODE | — | ✅ |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUBusinessUnitId | BU_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
