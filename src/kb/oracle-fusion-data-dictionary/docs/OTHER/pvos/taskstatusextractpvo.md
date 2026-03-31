---
id: DOC-OTHER-PVO-TaskStatusExtractPVO
doc_type: system-doc
title: "TaskStatusExtractPVO — PVO Cross-Module"
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
  - TaskStatusExtractPVO
  - taskstatusextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaskStatusExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Task Status Extract. Acessa as tabelas: DOO_TASK_STATUSES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.TaskStatusExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_task_statuses|DOO_TASK_STATUSES]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[doo_task_statuses|DOO_TASK_STATUSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskStatusCreatedBy | CREATED_BY | — | ✅ |
| 2 | TaskStatusCreationDate | CREATION_DATE | — | ✅ |
| 3 | TaskStatusLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | TaskStatusLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | TaskStatusLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | TaskStatusObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | TaskStatusOrchestrationApplicationId | ORCHESTRATION_APPLICATION_ID | — | ✅ |
| 8 | TaskStatusSeededFlag | SEEDED_FLAG | — | ✅ |
| 9 | TaskStatusSplitPriority | SPLIT_PRIORITY | — | ✅ |
| 10 | TaskStatusStatusCode | STATUS_CODE | — | ✅ |
| 11 | TaskStatusTaskStatusId | TASK_STATUS_ID | 🔑 | ✅ |
| 12 | TaskStatusTaskTypeId | TASK_TYPE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
