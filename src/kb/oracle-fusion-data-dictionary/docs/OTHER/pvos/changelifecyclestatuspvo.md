---
id: DOC-OTHER-PVO-ChangeLifeCycleStatusPVO
doc_type: system-doc
title: "ChangeLifeCycleStatusPVO — PVO Cross-Module"
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
  - ChangeLifeCycleStatusPVO
  - changelifecyclestatuspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChangeLifeCycleStatusPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Change Life Cycle Status. Acessa as tabelas: EGO_LIFECYCLE_STATUSES.

**Caminho:** `FscmTopModelAM.ChangeObjectsAM.ChangeLifeCycleStatusPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 1 | 1 | 11 | 42% |

---

## 🔗 Tabelas Relacionadas

- [[ego_lifecycle_statuses|EGO_LIFECYCLE_STATUSES]] — 26 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[ego_lifecycle_statuses|EGO_LIFECYCLE_STATUSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | AutoDemoteStatus | AUTO_DEMOTE_STATUS | — | — |
| 3 | AutoPromoteStatus | AUTO_PROMOTE_STATUS | — | — |
| 4 | ChangeEditableFlag | CHANGE_EDITABLE_FLAG | — | — |
| 5 | ChangeLifecycleStatusId | CHANGE_LIFECYCLE_STATUS_ID | 🔑 | ✅ |
| 6 | CompletionDate | COMPLETION_DATE | — | ✅ |
| 7 | CreatedBy | CREATED_BY | — | ✅ |
| 8 | CreationDate | CREATION_DATE | — | ✅ |
| 9 | EntityId1 | ENTITY_ID1 | — | ✅ |
| 10 | EntityId2 | ENTITY_ID2 | — | — |
| 11 | EntityId3 | ENTITY_ID3 | — | — |
| 12 | EntityId4 | ENTITY_ID4 | — | — |
| 13 | EntityId5 | ENTITY_ID5 | — | — |
| 14 | EntityName | ENTITY_NAME | — | ✅ |
| 15 | IterationNumber | ITERATION_NUMBER | — | — |
| 16 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | SequenceNumber | SEQUENCE_NUMBER | — | — |
| 21 | StartDate | START_DATE | — | ✅ |
| 22 | StatusCode | STATUS_CODE | — | ✅ |
| 23 | WfProcessInstanceId | WF_PROCESS_INSTANCE_ID | — | — |
| 24 | WfProcessTemplate | WF_PROCESS_TEMPLATE | — | — |
| 25 | WfSigPolicy | WF_SIG_POLICY | — | — |
| 26 | WorkflowStatus | WORKFLOW_STATUS | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
