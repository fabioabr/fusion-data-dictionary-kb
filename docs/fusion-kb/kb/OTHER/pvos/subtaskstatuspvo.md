---
id: DOC-OTHER-PVO-SubTaskStatusPVO
doc_type: system-doc
title: "SubTaskStatusPVO — PVO Cross-Module"
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
  - SubTaskStatusPVO
  - subtaskstatuspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SubTaskStatusPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Sub Task Status. Acessa as tabelas: HRA_EVAL_STEPS, HRA_PF_TASK_ROLES_B, HRA_PF_TASK_ROLES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceDocsAM.SubTaskStatusPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 43 | 3 | 4 | 10 | 23% |

---

## 🔗 Tabelas Relacionadas

- [[hra_eval_steps|HRA_EVAL_STEPS]] — 32 atributos (2 PKs, 4 BICC)
- [[hra_pf_task_roles_b|HRA_PF_TASK_ROLES_B]] — 5 atributos (1 PKs, 3 BICC)
- [[hra_pf_task_roles_tl|HRA_PF_TASK_ROLES_TL]] — 6 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[hra_eval_steps|HRA_EVAL_STEPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | EvalStepId | EVAL_STEP_ID | 🔑 | ✅ |
| 4 | EvalStepPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 5 | EvalStepPEOCriticalAlertDays | CRITICAL_ALERT_DAYS | — | — |
| 6 | EvalStepPEODueDate | DUE_DATE | — | — |
| 7 | EvalStepPEOEvalParticipantId | EVAL_PARTICIPANT_ID | — | — |
| 8 | EvalStepPEOEvaluationId | EVALUATION_ID | — | — |
| 9 | EvalStepPEOParentStepId | PARENT_STEP_ID | — | — |
| 10 | EvalStepPEOSequenceNumber | SEQUENCE_NUMBER | — | — |
| 11 | EvalStepPEOStandardAlertDays | STANDARD_ALERT_DAYS | — | — |
| 12 | EvalStepPEOStepCode | STEP_CODE | — | — |
| 13 | EvalStepPEOStepCompletedBy | STEP_COMPLETED_BY | — | — |
| 14 | EvalStepPEOStepCompletionDate | STEP_COMPLETION_DATE | — | — |
| 15 | EvalStepPEOStepStatus | STEP_STATUS | — | — |
| 16 | EvalStepSubPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 17 | EvalStepSubPEOCriticalAlertDays | CRITICAL_ALERT_DAYS | — | — |
| 18 | EvalStepSubPEODueDate | DUE_DATE | — | — |
| 19 | EvalStepSubPEOEvalParticipantId | EVAL_PARTICIPANT_ID | — | — |
| 20 | EvalStepSubPEOEvalStepId | EVAL_STEP_ID | 🔑 | ✅ |
| 21 | EvalStepSubPEOEvaluationId | EVALUATION_ID | — | — |
| 22 | EvalStepSubPEOParentStepId | PARENT_STEP_ID | — | — |
| 23 | EvalStepSubPEOSequenceNumber | SEQUENCE_NUMBER | — | — |
| 24 | EvalStepSubPEOStandardAlertDays | STANDARD_ALERT_DAYS | — | — |
| 25 | EvalStepSubPEOStepCode | STEP_CODE | — | — |
| 26 | EvalStepSubPEOStepCompletedBy | STEP_COMPLETED_BY | — | — |
| 27 | EvalStepSubPEOStepCompletionDate | STEP_COMPLETION_DATE | — | — |
| 28 | EvalStepSubPEOStepStatus | STEP_STATUS | — | ✅ |
| 29 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 31 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 32 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[hra_pf_task_roles_b|HRA_PF_TASK_ROLES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessTaskRoleBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ProcessTaskRoleBPEOProcessFlowId | PROCESS_FLOW_ID | — | — |
| 3 | ProcessTaskRoleBPEOSequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 4 | ProcessTaskRoleBPEOTaskCode | TASK_CODE | — | ✅ |
| 5 | ProcessTaskRoleId | PROCESS_TASK_ROLE_ID | 🔑 | ✅ |

### [[hra_pf_task_roles_tl|HRA_PF_TASK_ROLES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | ProcessTaskRoleTransPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | ProcessTaskRoleTransPEOMgrTaskName | MGR_TASK_NAME | — | ✅ |
| 4 | ProcessTaskRoleTransPEOProcessTaskRoleId | PROCESS_TASK_ROLE_ID | — | — |
| 5 | ProcessTaskRoleTransPEOWkrTaskName | WKR_TASK_NAME | — | ✅ |
| 6 | SourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
