---
id: DOC-OTHER-PVO-ProcessInstanceExtractPVO
doc_type: system-doc
title: "ProcessInstanceExtractPVO — PVO Cross-Module"
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
  - ProcessInstanceExtractPVO
  - processinstanceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProcessInstanceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Process Instance Extract. Acessa as tabelas: DOO_PROCESS_INSTANCES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.ProcessInstanceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 1 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_process_instances|DOO_PROCESS_INSTANCES]] — 22 atributos (1 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[doo_process_instances|DOO_PROCESS_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessInstanceActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 2 | ProcessInstanceActualFulfillDate | ACTUAL_FULFILL_DATE | — | ✅ |
| 3 | ProcessInstanceActualStartDate | ACTUAL_START_DATE | — | ✅ |
| 4 | ProcessInstanceCreatedBy | CREATED_BY | — | ✅ |
| 5 | ProcessInstanceCreationDate | CREATION_DATE | — | ✅ |
| 6 | ProcessInstanceDooProcessId | DOO_PROCESS_ID | — | ✅ |
| 7 | ProcessInstanceDooProcessInstanceId | DOO_PROCESS_INSTANCE_ID | 🔑 | ✅ |
| 8 | ProcessInstanceDooProcessVersion | DOO_PROCESS_VERSION | — | ✅ |
| 9 | ProcessInstanceJeopardyReason | JEOPARDY_REASON | — | ✅ |
| 10 | ProcessInstanceJeopardyReasonTaskInstId | JEOPARDY_REASON_TASK_INST_ID | — | ✅ |
| 11 | ProcessInstanceJeopardyScore | JEOPARDY_SCORE | — | ✅ |
| 12 | ProcessInstanceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | ProcessInstanceLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | ProcessInstanceLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | ProcessInstanceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | ProcessInstanceOrchestrationApplicationId | ORCHESTRATION_APPLICATION_ID | — | ✅ |
| 17 | ProcessInstancePlannedCompletionDate | PLANNED_COMPLETION_DATE | — | ✅ |
| 18 | ProcessInstancePlannedFulfillDate | PLANNED_FULFILL_DATE | — | ✅ |
| 19 | ProcessInstanceProcessActive | PROCESS_ACTIVE | — | ✅ |
| 20 | ProcessInstanceProcessNumber | PROCESS_NUMBER | — | ✅ |
| 21 | ProcessInstanceRequiredFulfillDate | REQUIRED_FULFILL_DATE | — | ✅ |
| 22 | ProcessInstanceStatusCode | STATUS_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
