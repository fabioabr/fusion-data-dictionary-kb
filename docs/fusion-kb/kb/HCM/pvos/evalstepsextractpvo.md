---
id: DOC-HCM-PVO-EvalStepsExtractPVO
doc_type: system-doc
title: "EvalStepsExtractPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - EvalStepsExtractPVO
  - evalstepsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EvalStepsExtractPVO

## 📌 Visão Geral

Extrai etapas do fluxo de avaliação de desempenho com ações, responsáveis e datas. Utilizado para rastrear progresso e SLA de ciclos de performance.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.PerformanceBiccExtractAM.EvalStepsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 1 | 1 | 27 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hra_eval_steps|HRA_EVAL_STEPS]] — 27 atributos (1 PKs, 27 BICC)

---

## ⚙️ Atributos

### [[hra_eval_steps|HRA_EVAL_STEPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionPerformedBy | ACTION_PERFORMED_BY | — | ✅ |
| 2 | ActionPerformedDate | ACTION_PERFORMED_DATE | — | ✅ |
| 3 | ActionReason | ACTION_REASON | — | ✅ |
| 4 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | CriticalAlertDays | CRITICAL_ALERT_DAYS | — | ✅ |
| 8 | DueDate | DUE_DATE | — | ✅ |
| 9 | EvalParticipantId | EVAL_PARTICIPANT_ID | — | ✅ |
| 10 | EvalStepId | EVAL_STEP_ID | 🔑 | ✅ |
| 11 | EvaluationId | EVALUATION_ID | — | ✅ |
| 12 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | ParentStepId | PARENT_STEP_ID | — | ✅ |
| 17 | SequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 18 | StandardAlertDays | STANDARD_ALERT_DAYS | — | ✅ |
| 19 | StepCode | STEP_CODE | — | ✅ |
| 20 | StepCompletedBy | STEP_COMPLETED_BY | — | ✅ |
| 21 | StepCompletionDate | STEP_COMPLETION_DATE | — | ✅ |
| 22 | StepStatus | STEP_STATUS | — | ✅ |
| 23 | StepSubStatus | STEP_SUB_STATUS | — | ✅ |
| 24 | StepUpdActionCode | STEP_UPD_ACTION_CODE | — | ✅ |
| 25 | StepUpdActionPerformedBy | STEP_UPD_ACTION_PERFORMED_BY | — | ✅ |
| 26 | StepUpdActionPerformedDate | STEP_UPD_ACTION_PERFORMED_DATE | — | ✅ |
| 27 | StepUpdActionReason | STEP_UPD_ACTION_REASON | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
