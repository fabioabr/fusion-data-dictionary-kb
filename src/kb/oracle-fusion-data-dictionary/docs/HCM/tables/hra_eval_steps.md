---
id: DOC-HCM-146
doc_type: system-doc
title: "HRA_EVAL_STEPS — Etapas de Avaliação"
system: Oracle Fusion Cloud HCM
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
  - performance-management
  - eval-step
  - avaliacao
  - hra
aliases:
  - HRA_EVAL_STEPS
  - hra_eval_steps
  - hra-eval-steps
  - DOC-HCM-146
  - etapas-de-avaliação
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_EVAL_STEPS

## 📌 Visão Geral

Armazena os **registros de etapas do workflow de avaliação** no módulo de Performance Management. Cada registro contém dados operacionais do processo de avaliação e gestão de performance.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de etapas do workflow de avaliação:** Registro e controle operacional.
- **Workflow de avaliação:** Suporte ao processo de avaliação de performance.
- **Rastreabilidade:** Histórico completo de ações e decisões.
- **Relatórios de performance:** Dados para dashboards e análises.
- **Compliance:** Documentação de processos de avaliação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EVAL_STEP_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NULL | FK | Pessoa associada | [[per_all_people_f]] | 🟡 80% |
| 3 | EVALUATION_ID | NUMBER(18) | NULL | FK | Avaliação associada | [[hra_evaluations]] | 🟡 80% |
| 4 | STATUS | VARCHAR2(30) | NULL | Status | Status do registro | — | 🟡 75% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Texto | Descrição | — | 🟡 75% |
| 6 | EFFECTIVE_DATE | DATE | NULL | Data | Data de efetividade | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador da etapa de avaliacao)
- [[hra_evaluations]] — via `EVALUATION_ID` (avaliacao da etapa do fluxo)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Registros por avaliação
```sql
SELECT r.EVAL_STEP_ID, r.PERSON_ID, r.STATUS, r.DESCRIPTION
FROM   HRA_EVAL_STEPS r
WHERE  r.EVALUATION_ID = :p_evaluation_id;
```

### Registros por pessoa
```sql
SELECT r.EVAL_STEP_ID, r.EVALUATION_ID, r.STATUS
FROM   HRA_EVAL_STEPS r
WHERE  r.PERSON_ID = :p_person_id;
```

---

## 🔒 Observações

- Tabela operacional do processo de etapas do workflow de avaliação.
- Integra-se com o workflow de avaliação de performance.
- O `STATUS` controla o ciclo de vida do registro.
- Dados são consumidos por relatórios e dashboards de Talent Management.

---

## 🔗 PVOs Relacionados

### [[evalstepsextractpvo|EvalStepsExtractPVO]] (HCM · BICC: 27/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_PERFORMED_BY | ActionPerformedBy | ✅ |
| ACTION_PERFORMED_DATE | ActionPerformedDate | ✅ |
| ACTION_REASON | ActionReason | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CRITICAL_ALERT_DAYS | CriticalAlertDays | ✅ |
| DUE_DATE | DueDate | ✅ |
| EVAL_PARTICIPANT_ID | EvalParticipantId | ✅ |
| EVAL_STEP_ID | EvalStepId | ✅ |
| EVALUATION_ID | EvaluationId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PARENT_STEP_ID | ParentStepId | ✅ |
| SEQUENCE_NUMBER | SequenceNumber | ✅ |
| STANDARD_ALERT_DAYS | StandardAlertDays | ✅ |
| STEP_CODE | StepCode | ✅ |
| STEP_COMPLETED_BY | StepCompletedBy | ✅ |
| STEP_COMPLETION_DATE | StepCompletionDate | ✅ |
| STEP_STATUS | StepStatus | ✅ |
| STEP_SUB_STATUS | StepSubStatus | ✅ |
| STEP_UPD_ACTION_CODE | StepUpdActionCode | ✅ |
| STEP_UPD_ACTION_PERFORMED_BY | StepUpdActionPerformedBy | ✅ |
| STEP_UPD_ACTION_PERFORMED_DATE | StepUpdActionPerformedDate | ✅ |
| STEP_UPD_ACTION_REASON | StepUpdActionReason | ✅ |

### [[performancesubtaskstatuspvo|PerformanceSubTaskStatusPVO]] (HCM · BICC: 10/40)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_PERFORMED_BY | ActionPerformedBy | ✅ |
| ACTION_PERFORMED_DATE | ActionPerformedDate | ✅ |
| ACTION_REASON | ActionReason | ✅ |
| BUSINESS_GROUP_ID | EvalStepPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | EvalStepSubPEOBusinessGroupId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| CRITICAL_ALERT_DAYS | EvalStepPEOCriticalAlertDays | — |
| CRITICAL_ALERT_DAYS | EvalStepSubPEOCriticalAlertDays | — |
| DUE_DATE | EvalStepPEODueDate | — |
| DUE_DATE | EvalStepSubPEODueDate | — |
| EVAL_PARTICIPANT_ID | EvalStepPEOEvalParticipantId | ✅ |
| EVAL_PARTICIPANT_ID | EvalStepSubPEOEvalParticipantId | — |
| EVAL_STEP_ID | EvalStepId | ✅ |
| EVAL_STEP_ID | EvalStepSubPEOEvalStepId | ✅ |
| EVALUATION_ID | EvalStepPEOEvaluationId | — |
| EVALUATION_ID | EvalStepSubPEOEvaluationId | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PARENT_STEP_ID | EvalStepPEOParentStepId | ✅ |
| PARENT_STEP_ID | EvalStepSubPEOParentStepId | — |
| SEQUENCE_NUMBER | EvalStepPEOSequenceNumber | — |
| SEQUENCE_NUMBER | EvalStepSubPEOSequenceNumber | — |
| STANDARD_ALERT_DAYS | EvalStepPEOStandardAlertDays | — |
| STANDARD_ALERT_DAYS | EvalStepSubPEOStandardAlertDays | — |
| STEP_CODE | EvalStepPEOStepCode | — |
| STEP_CODE | EvalStepSubPEOStepCode | — |
| STEP_COMPLETED_BY | EvalStepPEOStepCompletedBy | — |
| STEP_COMPLETED_BY | EvalStepSubPEOStepCompletedBy | — |
| STEP_COMPLETION_DATE | EvalStepPEOStepCompletionDate | — |
| STEP_COMPLETION_DATE | EvalStepSubPEOStepCompletionDate | — |
| STEP_STATUS | EvalStepPEOStepStatus | — |
| STEP_STATUS | EvalStepSubPEOStepStatus | ✅ |
| STEP_SUB_STATUS | StepSubStatus | ✅ |
| STEP_UPD_ACTION_CODE | StepUpdActionCode | — |
| STEP_UPD_ACTION_PERFORMED_BY | StepUpdActionPerformedBy | — |
| STEP_UPD_ACTION_PERFORMED_DATE | StepUpdActionPerformedDate | — |
| STEP_UPD_ACTION_REASON | StepUpdActionReason | — |

### [[performancetaskstatuspvo|PerformanceTaskStatusPVO]] (HCM · BICC: 15/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_PERFORMED_BY | ActionPerformedBy | ✅ |
| ACTION_PERFORMED_DATE | ActionPerformedDate | ✅ |
| ACTION_REASON | ActionReason | ✅ |
| BUSINESS_GROUP_ID | EvalStepPEOBusinessGroupId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| CRITICAL_ALERT_DAYS | EvalStepPEOCriticalAlertDays | ✅ |
| DUE_DATE | EvalStepPEODueDate | ✅ |
| EVAL_PARTICIPANT_ID | EvalStepPEOEvalParticipantId | ✅ |
| EVAL_STEP_ID | EvalStepId | ✅ |
| EVALUATION_ID | EvalStepPEOEvaluationId | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PARENT_STEP_ID | EvalStepPEOParentStepId | ✅ |
| SEQUENCE_NUMBER | EvalStepPEOSequenceNumber | ✅ |
| STANDARD_ALERT_DAYS | EvalStepPEOStandardAlertDays | ✅ |
| STEP_CODE | EvalStepPEOStepCode | — |
| STEP_COMPLETED_BY | EvalStepPEOStepCompletedBy | ✅ |
| STEP_COMPLETION_DATE | EvalStepPEOStepCompletionDate | ✅ |
| STEP_STATUS | EvalStepPEOStepStatus | ✅ |
| STEP_SUB_STATUS | StepSubStatus | ✅ |
| STEP_UPD_ACTION_CODE | StepUpdActionCode | — |
| STEP_UPD_ACTION_PERFORMED_BY | StepUpdActionPerformedBy | — |
| STEP_UPD_ACTION_PERFORMED_DATE | StepUpdActionPerformedDate | — |
| STEP_UPD_ACTION_REASON | StepUpdActionReason | — |

### [[subtaskstatuspvo|SubTaskStatusPVO]] (HCM · BICC: 4/32)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EvalStepPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | EvalStepSubPEOBusinessGroupId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| CRITICAL_ALERT_DAYS | EvalStepPEOCriticalAlertDays | — |
| CRITICAL_ALERT_DAYS | EvalStepSubPEOCriticalAlertDays | — |
| DUE_DATE | EvalStepPEODueDate | — |
| DUE_DATE | EvalStepSubPEODueDate | — |
| EVAL_PARTICIPANT_ID | EvalStepPEOEvalParticipantId | — |
| EVAL_PARTICIPANT_ID | EvalStepSubPEOEvalParticipantId | — |
| EVAL_STEP_ID | EvalStepId | ✅ |
| EVAL_STEP_ID | EvalStepSubPEOEvalStepId | ✅ |
| EVALUATION_ID | EvalStepPEOEvaluationId | — |
| EVALUATION_ID | EvalStepSubPEOEvaluationId | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PARENT_STEP_ID | EvalStepPEOParentStepId | — |
| PARENT_STEP_ID | EvalStepSubPEOParentStepId | — |
| SEQUENCE_NUMBER | EvalStepPEOSequenceNumber | — |
| SEQUENCE_NUMBER | EvalStepSubPEOSequenceNumber | — |
| STANDARD_ALERT_DAYS | EvalStepPEOStandardAlertDays | — |
| STANDARD_ALERT_DAYS | EvalStepSubPEOStandardAlertDays | — |
| STEP_CODE | EvalStepPEOStepCode | — |
| STEP_CODE | EvalStepSubPEOStepCode | — |
| STEP_COMPLETED_BY | EvalStepPEOStepCompletedBy | — |
| STEP_COMPLETED_BY | EvalStepSubPEOStepCompletedBy | — |
| STEP_COMPLETION_DATE | EvalStepPEOStepCompletionDate | — |
| STEP_COMPLETION_DATE | EvalStepSubPEOStepCompletionDate | — |
| STEP_STATUS | EvalStepPEOStepStatus | — |
| STEP_STATUS | EvalStepSubPEOStepStatus | ✅ |

### [[taskstatuspvo|TaskStatusPVO]] (HCM · BICC: 3/19)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EvalStepPEOBusinessGroupId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| CRITICAL_ALERT_DAYS | EvalStepPEOCriticalAlertDays | — |
| DUE_DATE | EvalStepPEODueDate | — |
| EVAL_PARTICIPANT_ID | EvalStepPEOEvalParticipantId | — |
| EVAL_STEP_ID | EvalStepId | ✅ |
| EVALUATION_ID | EvalStepPEOEvaluationId | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PARENT_STEP_ID | EvalStepPEOParentStepId | — |
| SEQUENCE_NUMBER | EvalStepPEOSequenceNumber | — |
| STANDARD_ALERT_DAYS | EvalStepPEOStandardAlertDays | — |
| STEP_CODE | EvalStepPEOStepCode | — |
| STEP_COMPLETED_BY | EvalStepPEOStepCompletedBy | — |
| STEP_COMPLETION_DATE | EvalStepPEOStepCompletionDate | — |
| STEP_STATUS | EvalStepPEOStepStatus | ✅ |

---

## 📚 Referências

- [Oracle Docs — HRA_EVAL_STEPS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hraevalsteps.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
