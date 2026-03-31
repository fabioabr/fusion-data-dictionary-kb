---
id: DOC-OTHER-PVO-ChangeLifecycleStatusExtractPVO
doc_type: system-doc
title: "ChangeLifecycleStatusExtractPVO — PVO Cross-Module"
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
  - ChangeLifecycleStatusExtractPVO
  - changelifecyclestatusextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChangeLifecycleStatusExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Change Lifecycle Status Extract. Acessa as tabelas: EGO_LIFECYCLE_STATUSES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgoBiccExtractAM.ChangeLifecycleStatusExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 1 | 1 | 27 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ego_lifecycle_statuses|EGO_LIFECYCLE_STATUSES]] — 27 atributos (1 PKs, 27 BICC)

---

## ⚙️ Atributos

### [[ego_lifecycle_statuses|EGO_LIFECYCLE_STATUSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeLifeCycleStatusPEOActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | ChangeLifeCycleStatusPEOAutoDemoteStatus | AUTO_DEMOTE_STATUS | — | ✅ |
| 3 | ChangeLifeCycleStatusPEOAutoPromoteStatus | AUTO_PROMOTE_STATUS | — | ✅ |
| 4 | ChangeLifeCycleStatusPEOChangeEditableFlag | CHANGE_EDITABLE_FLAG | — | ✅ |
| 5 | ChangeLifeCycleStatusPEOChangeLifecycleStatusId | CHANGE_LIFECYCLE_STATUS_ID | 🔑 | ✅ |
| 6 | ChangeLifeCycleStatusPEOCompletionDate | COMPLETION_DATE | — | ✅ |
| 7 | ChangeLifeCycleStatusPEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | ChangeLifeCycleStatusPEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | ChangeLifeCycleStatusPEOEntityId1 | ENTITY_ID1 | — | ✅ |
| 10 | ChangeLifeCycleStatusPEOEntityId2 | ENTITY_ID2 | — | ✅ |
| 11 | ChangeLifeCycleStatusPEOEntityId3 | ENTITY_ID3 | — | ✅ |
| 12 | ChangeLifeCycleStatusPEOEntityId4 | ENTITY_ID4 | — | ✅ |
| 13 | ChangeLifeCycleStatusPEOEntityId5 | ENTITY_ID5 | — | ✅ |
| 14 | ChangeLifeCycleStatusPEOEntityName | ENTITY_NAME | — | ✅ |
| 15 | ChangeLifeCycleStatusPEOEntryCriteriaRuleSetName | ENTRY_CRITERIA_RULE_SET_NAME | — | ✅ |
| 16 | ChangeLifeCycleStatusPEOExitCriteriaRuleSetName | EXIT_CRITERIA_RULE_SET_NAME | — | ✅ |
| 17 | ChangeLifeCycleStatusPEOIterationNumber | ITERATION_NUMBER | — | ✅ |
| 18 | ChangeLifeCycleStatusPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | ChangeLifeCycleStatusPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 20 | ChangeLifeCycleStatusPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 21 | ChangeLifeCycleStatusPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 22 | ChangeLifeCycleStatusPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 23 | ChangeLifeCycleStatusPEOSequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 24 | ChangeLifeCycleStatusPEOSkipRequestComment | SKIP_REQUEST_COMMENT | — | ✅ |
| 25 | ChangeLifeCycleStatusPEOStartDate | START_DATE | — | ✅ |
| 26 | ChangeLifeCycleStatusPEOStatusCode | STATUS_CODE | — | ✅ |
| 27 | ChangeLifeCycleStatusPEOWorkflowStatus | WORKFLOW_STATUS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
