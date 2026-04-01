---
id: DOC-AP-PVO-HcmApprovalsTaskP1
doc_type: system-doc
title: "HcmApprovalsTaskP1 — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - HcmApprovalsTaskP1
  - hcmapprovalstaskp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HcmApprovalsTaskP1

## 📌 Visão Geral

Extrai as tarefas de aprovação de transações de RH, incluindo status, responsáveis, histórico de ações e datas. Fundamental para monitorar SLAs de aprovação, identificar gargalos e garantir conformidade nos processos de gestão de pessoas.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmApprovalsReportingAM.HcmApprovalsTaskP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 83 | 3 | 2 | 37 | 45% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_bpm_task_assignee|FND_BPM_TASK_ASSIGNEE]] — 14 atributos (6 BICC)
- [[fnd_bpm_task_history_vl|FND_BPM_TASK_HISTORY_VL]] — 25 atributos (1 PKs, 13 BICC)
- [[hrc_txn_fnd_bpm_task_vl|HRC_TXN_FND_BPM_TASK_VL]] — 44 atributos (1 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[fnd_bpm_task_assignee|FND_BPM_TASK_ASSIGNEE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FndBpmTaskAssigneePEOAssignee | ASSIGNEE | — | ✅ |
| 2 | FndBpmTaskAssigneePEOAssigneeGroupOrRole | ASSIGNEE_GROUP_OR_ROLE | — | ✅ |
| 3 | FndBpmTaskAssigneePEOAssigneeType | ASSIGNEE_TYPE | — | ✅ |
| 4 | FndBpmTaskAssigneePEOCreatedBy4 | CREATED_BY | — | — |
| 5 | FndBpmTaskAssigneePEOCreationDate4 | CREATION_DATE | — | — |
| 6 | FndBpmTaskAssigneePEODomain5 | DOMAIN | — | — |
| 7 | FndBpmTaskAssigneePEOInitiatedDate5 | INITIATED_DATE | — | — |
| 8 | FndBpmTaskAssigneePEOLastUpdateDate4 | LAST_UPDATE_DATE | — | ✅ |
| 9 | FndBpmTaskAssigneePEOLastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 10 | FndBpmTaskAssigneePEOLastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 11 | FndBpmTaskAssigneePEOOriginalAssigneeUser | ORIGINAL_ASSIGNEE_USER | — | ✅ |
| 12 | FndBpmTaskAssigneePEOSequence | SEQUENCE | — | ✅ |
| 13 | FndBpmTaskAssigneePEOTaskId5 | TASK_ID | — | — |
| 14 | FndBpmTaskAssigneePEOVersion1 | VERSION | — | — |

### [[fnd_bpm_task_history_vl|FND_BPM_TASK_HISTORY_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FndBpmTaskHistoryPEOAcquiredBy | ACQUIRED_BY | — | ✅ |
| 2 | FndBpmTaskHistoryPEOCompletedDate2 | COMPLETED_DATE | — | — |
| 3 | FndBpmTaskHistoryPEOCreatedBy3 | CREATED_BY | — | — |
| 4 | FndBpmTaskHistoryPEOCreationDate3 | CREATION_DATE | — | — |
| 5 | FndBpmTaskHistoryPEODomain4 | DOMAIN | — | — |
| 6 | FndBpmTaskHistoryPEOFromUser | FROM_USER | — | ✅ |
| 7 | FndBpmTaskHistoryPEOIdentificationKey1 | IDENTIFICATION_KEY | — | — |
| 8 | FndBpmTaskHistoryPEOInitiatedDate4 | INITIATED_DATE | — | — |
| 9 | FndBpmTaskHistoryPEOLastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 10 | FndBpmTaskHistoryPEOLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 11 | FndBpmTaskHistoryPEOLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 12 | FndBpmTaskHistoryPEOOutcome1 | OUTCOME | — | ✅ |
| 13 | FndBpmTaskHistoryPEOOutcomeCode1 | OUTCOME_CODE | — | ✅ |
| 14 | FndBpmTaskHistoryPEOParentTaskId1 | PARENT_TASK_ID | — | — |
| 15 | FndBpmTaskHistoryPEOParticipant | PARTICIPANT | — | ✅ |
| 16 | FndBpmTaskHistoryPEOParticipantCode | PARTICIPANT_CODE | — | ✅ |
| 17 | FndBpmTaskHistoryPEORootTaskId3 | ROOT_TASK_ID | — | — |
| 18 | FndBpmTaskHistoryPEOStage | STAGE | — | ✅ |
| 19 | FndBpmTaskHistoryPEOStageCode | STAGE_CODE | — | ✅ |
| 20 | FndBpmTaskHistoryPEOStatusCode1 | STATUS_CODE | — | ✅ |
| 21 | FndBpmTaskHistoryPEOTaskId4 | TASK_ID | — | — |
| 22 | FndBpmTaskHistoryPEOTaskNumber1 | TASK_NUMBER | — | ✅ |
| 23 | FndBpmTaskHistoryPEOVersion | VERSION | 🔑 | ✅ |
| 24 | FndBpmTaskHistoryPEOVersionReason | VERSION_REASON | — | ✅ |
| 25 | FndBpmTaskHistoryPEOWorkflowpatternCode | WORKFLOWPATTERN_CODE | — | — |

### [[hrc_txn_fnd_bpm_task_vl|HRC_TXN_FND_BPM_TASK_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HcmApprovalsTaskPEOActive | ACTIVE | — | — |
| 2 | HcmApprovalsTaskPEOArmProcessCreatedBy | ARM_PROCESS_CREATED_BY | — | — |
| 3 | HcmApprovalsTaskPEOArmProcessCreationDate | ARM_PROCESS_CREATION_DATE | — | — |
| 4 | HcmApprovalsTaskPEOArmProcessLastUpdateDate | ARM_PROCESS_LAST_UPDATE_DATE | — | ✅ |
| 5 | HcmApprovalsTaskPEOArmProcessLastUpdateLogin | ARM_PROCESS_LAST_UPDATE_LOGIN | — | — |
| 6 | HcmApprovalsTaskPEOArmProcessLastUpdatedBy | ARM_PROCESS_LAST_UPDATED_BY | — | — |
| 7 | HcmApprovalsTaskPEOArmProcessObjVersionNumber | ARM_PROCESS_OBJ_VERSION_NUMBER | — | — |
| 8 | HcmApprovalsTaskPEOCategory | CATEGORY | — | ✅ |
| 9 | HcmApprovalsTaskPEOCategoryCode | CATEGORY_CODE | — | ✅ |
| 10 | HcmApprovalsTaskPEOCompletedBy | COMPLETED_BY | — | ✅ |
| 11 | HcmApprovalsTaskPEOCompletedDate | COMPLETED_DATE | — | — |
| 12 | HcmApprovalsTaskPEOCompositeId | COMPOSITE_ID | — | — |
| 13 | HcmApprovalsTaskPEOCompositeName | COMPOSITE_NAME | — | — |
| 14 | HcmApprovalsTaskPEOCompositeVersion | COMPOSITE_VERSION | — | — |
| 15 | HcmApprovalsTaskPEODescription | DESCRIPTION | — | — |
| 16 | HcmApprovalsTaskPEODomain | DOMAIN | — | — |
| 17 | HcmApprovalsTaskPEODueDate | DUE_DATE | — | ✅ |
| 18 | HcmApprovalsTaskPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 19 | HcmApprovalsTaskPEOExpirationDate | EXPIRATION_DATE | — | ✅ |
| 20 | HcmApprovalsTaskPEOIdentificationKey | IDENTIFICATION_KEY | — | ✅ |
| 21 | HcmApprovalsTaskPEOInitiatedBy | INITIATED_BY | — | ✅ |
| 22 | HcmApprovalsTaskPEOInitiatedDate | INITIATED_DATE | — | — |
| 23 | HcmApprovalsTaskPEOModuleId | MODULE_ID | — | — |
| 24 | HcmApprovalsTaskPEOName | NAME | — | ✅ |
| 25 | HcmApprovalsTaskPEOObjectId | OBJECT_ID | — | ✅ |
| 26 | HcmApprovalsTaskPEOOutcome | OUTCOME | — | ✅ |
| 27 | HcmApprovalsTaskPEOOutcomeCode | OUTCOME_CODE | — | ✅ |
| 28 | HcmApprovalsTaskPEOParentTaskId | PARENT_TASK_ID | — | — |
| 29 | HcmApprovalsTaskPEOProcessId | PROCESS_ID | — | — |
| 30 | HcmApprovalsTaskPEORootTaskId | ROOT_TASK_ID | — | — |
| 31 | HcmApprovalsTaskPEORuleFileName | RULE_FILE_NAME | — | — |
| 32 | HcmApprovalsTaskPEOStatusCode | STATUS_CODE | — | ✅ |
| 33 | HcmApprovalsTaskPEOTaskCreatedBy | TASK_CREATED_BY | — | — |
| 34 | HcmApprovalsTaskPEOTaskCreationDate | TASK_CREATION_DATE | — | — |
| 35 | HcmApprovalsTaskPEOTaskDefinitionName | TASK_DEFINITION_NAME | — | ✅ |
| 36 | HcmApprovalsTaskPEOTaskFileName | TASK_FILE_NAME | — | — |
| 37 | HcmApprovalsTaskPEOTaskId | TASK_ID | 🔑 | ✅ |
| 38 | HcmApprovalsTaskPEOTaskLastUpdateDate | TASK_LAST_UPDATE_DATE | — | ✅ |
| 39 | HcmApprovalsTaskPEOTaskLastUpdateLogin | TASK_LAST_UPDATE_LOGIN | — | — |
| 40 | HcmApprovalsTaskPEOTaskLastUpdatedBy | TASK_LAST_UPDATED_BY | — | — |
| 41 | HcmApprovalsTaskPEOTaskNumber | TASK_NUMBER | — | ✅ |
| 42 | HcmApprovalsTaskPEOTaskQname | TASK_QNAME | — | — |
| 43 | HcmApprovalsTaskPEOTaskTitle | TASK_TITLE | — | ✅ |
| 44 | HcmApprovalsTaskPEOTxnModuleIdentifier | TXN_MODULE_IDENTIFIER | — | — |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
