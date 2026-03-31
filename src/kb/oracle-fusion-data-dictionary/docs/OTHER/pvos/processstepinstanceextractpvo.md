---
id: DOC-OTHER-PVO-ProcessStepInstanceExtractPVO
doc_type: system-doc
title: "ProcessStepInstanceExtractPVO — PVO Cross-Module"
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
  - ProcessStepInstanceExtractPVO
  - processstepinstanceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProcessStepInstanceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Process Step Instance Extract. Acessa as tabelas: DOO_PROCESS_STEP_INSTANCES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.ProcessStepInstanceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 1 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_process_step_instances|DOO_PROCESS_STEP_INSTANCES]] — 22 atributos (1 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[doo_process_step_instances|DOO_PROCESS_STEP_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessStepInstanceActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 2 | ProcessStepInstanceActualStartDate | ACTUAL_START_DATE | — | ✅ |
| 3 | ProcessStepInstanceCreatedBy | CREATED_BY | — | ✅ |
| 4 | ProcessStepInstanceCreationDate | CREATION_DATE | — | ✅ |
| 5 | ProcessStepInstanceDooProcessInstanceId | DOO_PROCESS_INSTANCE_ID | — | ✅ |
| 6 | ProcessStepInstanceGroupId | GROUP_ID | — | ✅ |
| 7 | ProcessStepInstanceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ProcessStepInstanceLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | ProcessStepInstanceLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ProcessStepInstanceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ProcessStepInstancePlannedCompletionDate | PLANNED_COMPLETION_DATE | — | ✅ |
| 12 | ProcessStepInstancePlannedStartDate | PLANNED_START_DATE | — | ✅ |
| 13 | ProcessStepInstanceReferenceStepInstanceId | REFERENCE_STEP_INSTANCE_ID | — | ✅ |
| 14 | ProcessStepInstanceRequiredCompletionDate | REQUIRED_COMPLETION_DATE | — | ✅ |
| 15 | ProcessStepInstanceRequiredStartDate | REQUIRED_START_DATE | — | ✅ |
| 16 | ProcessStepInstanceScheduledCompletionDate | SCHEDULED_COMPLETION_DATE | — | ✅ |
| 17 | ProcessStepInstanceScheduledStartDate | SCHEDULED_START_DATE | — | ✅ |
| 18 | ProcessStepInstanceStepActive | STEP_ACTIVE | — | ✅ |
| 19 | ProcessStepInstanceStepId | STEP_ID | — | ✅ |
| 20 | ProcessStepInstanceStepInstanceId | STEP_INSTANCE_ID | 🔑 | ✅ |
| 21 | ProcessStepInstanceStepStatus | STEP_STATUS | — | ✅ |
| 22 | ProcessStepInstanceTaskInstanceId | TASK_INSTANCE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
