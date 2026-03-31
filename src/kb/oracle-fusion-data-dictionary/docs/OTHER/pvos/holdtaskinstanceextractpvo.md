---
id: DOC-OTHER-PVO-HoldTaskInstanceExtractPVO
doc_type: system-doc
title: "HoldTaskInstanceExtractPVO — PVO Cross-Module"
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
  - HoldTaskInstanceExtractPVO
  - holdtaskinstanceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HoldTaskInstanceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Hold Task Instance Extract. Acessa as tabelas: DOO_HOLD_TASK_INSTANCES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.HoldTaskInstanceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 4 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_hold_task_instances|DOO_HOLD_TASK_INSTANCES]] — 12 atributos (4 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[doo_hold_task_instances|DOO_HOLD_TASK_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HoldTaskInstanceCreatedBy | CREATED_BY | — | ✅ |
| 2 | HoldTaskInstanceCreationDate | CREATION_DATE | — | ✅ |
| 3 | HoldTaskInstanceDeletedFlag | DELETED_FLAG | — | ✅ |
| 4 | HoldTaskInstanceHoldInstanceId | HOLD_INSTANCE_ID | 🔑 | ✅ |
| 5 | HoldTaskInstanceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | HoldTaskInstanceLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | HoldTaskInstanceLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | HoldTaskInstanceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | HoldTaskInstancePendingFlag | PENDING_FLAG | — | ✅ |
| 10 | HoldTaskInstanceTaskInstanceId | TASK_INSTANCE_ID | 🔑 | ✅ |
| 11 | HoldTaskInstanceTransactionEntityId | TRANSACTION_ENTITY_ID | 🔑 | ✅ |
| 12 | HoldTaskInstanceTransactionEntityName | TRANSACTION_ENTITY_NAME | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
