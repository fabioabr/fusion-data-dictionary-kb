---
id: DOC-HCM-141
doc_type: system-doc
title: "HRA_EVAL_PARTICIPANTS — Participantes de Avaliação"
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
  - eval-participant
  - avaliacao
  - hra
aliases:
  - HRA_EVAL_PARTICIPANTS
  - hra_eval_participants
  - hra-eval-participants
  - DOC-HCM-141
  - participantes-de-avaliação
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_EVAL_PARTICIPANTS

## 📌 Visão Geral

Armazena os **registros de participantes de avaliações** no módulo de Performance Management. Cada registro contém dados operacionais do processo de avaliação e gestão de performance.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de participantes de avaliações:** Registro e controle operacional.
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
| 1 | EVAL_PARTICIPANT_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
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
- [[per_all_people_f]] — via `PERSON_ID` (participante da avaliacao)
- [[hra_evaluations]] — via `EVALUATION_ID` (avaliacao do participante)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Registros por avaliação
```sql
SELECT r.EVAL_PARTICIPANT_ID, r.PERSON_ID, r.STATUS, r.DESCRIPTION
FROM   HRA_EVAL_PARTICIPANTS r
WHERE  r.EVALUATION_ID = :p_evaluation_id;
```

### Registros por pessoa
```sql
SELECT r.EVAL_PARTICIPANT_ID, r.EVALUATION_ID, r.STATUS
FROM   HRA_EVAL_PARTICIPANTS r
WHERE  r.PERSON_ID = :p_person_id;
```

---

## 🔒 Observações

- Tabela operacional do processo de participantes de avaliações.
- Integra-se com o workflow de avaliação de performance.
- O `STATUS` controla o ciclo de vida do registro.
- Dados são consumidos por relatórios e dashboards de Talent Management.

---

## 🔗 PVOs Relacionados

### [[evaluationparticipantratingpvo|EvaluationParticipantRatingPVO]] (HCM · BICC: 2/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDED_BY_PERSON_ID | EvalParticipantPEOAddedByPersonId | — |
| ADDED_BY_ROLE | EvalParticipantPEOAddedByRole | — |
| EVAL_PARTICIPANT_ID | EvalParticipantId | ✅ |
| EVAL_ROLE_ID | EvalParticipantPEOEvalRoleId | — |
| FDBACK_COMPLETION_DATE | EvalParticipantPEOFdbackCompletionDate | — |
| FDBACK_SENT_BACK_FLAG | EvalParticipantPEOFdbackSentBackFlag | — |
| FDBACK_STARTED_FLAG | EvalParticipantPEOFdbackStartedFlag | — |
| LAST_UPDATE_DATE | EvalRatingPEOLastUpdateDate | ✅ |
| LOCKED_OUT_DATE | EvalParticipantPEOLockedOutDate | — |
| LOCKED_OUT_FLAG | EvalParticipantPEOLockedOutFlag | — |
| NOTIFIED_BY_PERSON_ID | EvalParticipantPEONotifiedByPersonId | — |
| NOTIFIED_BY_ROLE | EvalParticipantPEONotifiedByRole | — |
| NOTIFIED_FLAG | EvalParticipantPEONotifiedFlag | — |
| PARTICIPATION_STATUS_CODE | EvalParticipantPEOParticipationStatus | — |
| PCPN_COMMENT_TEXT_FOR_WRK | EvalParticipantPEOPcpnCommentTextForWrk | — |
| PCPN_COMMENTS_FOR_WRK | EvalParticipantPEOPcpnCommentsForWrk | — |
| PERSON_ID | EvalParticipantPEOPersonId | — |
| QUESTIONNAIRE_ID | EvalParticipantPEOQuestionnaireId | — |
| ROLE_TYPE_CODE | EvalParticipantPEORoleTypeCode | — |
| STATUS_UPDATE_DATE | EvalParticipantPEOStatusUpdateDate | — |

### [[evaluationparticipantrolepvo|EvaluationParticipantRolePVO]] (HCM · BICC: 23/31)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | ActionCode | — |
| ACTION_PERFORMED_BY | ActionPerformedBy | — |
| ACTION_PERFORMED_DATE | ActionPerformedDate | — |
| ACTION_REASON | ActionReason | — |
| ADDED_BY_PERSON_ID | EvalParticipantPEOAddedByPersonId | ✅ |
| ADDED_BY_ROLE | EvalParticipantPEOAddedByRole | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DUE_DATE | EvalParticipantPEODueDate | ✅ |
| EVAL_PARTICIPANT_ID | EvalParticipantId | ✅ |
| EVAL_ROLE_ID | EvalParticipantPEOEvalRoleId | ✅ |
| EVALUATION_ID | EvalParticipantPEOEvaluationId | — |
| FDBACK_COMPLETION_DATE | EvalParticipantPEOFdbackCompletionDate | ✅ |
| FDBACK_SENT_BACK_FLAG | EvalParticipantPEOFdbackSentBackFlag | ✅ |
| FDBACK_STARTED_FLAG | EvalParticipantPEOFdbackStartedFlag | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LOCKED_OUT_DATE | EvalParticipantPEOLockedOutDate | ✅ |
| LOCKED_OUT_FLAG | EvalParticipantPEOLockedOutFlag | ✅ |
| NOTIFIED_BY_PERSON_ID | EvalParticipantPEONotifiedByPersonId | ✅ |
| NOTIFIED_BY_ROLE | EvalParticipantPEONotifiedByRole | ✅ |
| NOTIFIED_FLAG | EvalParticipantPEONotifiedFlag | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PARTICIPATION_STATUS_CODE | EvalParticipantPEOParticipationStatus | ✅ |
| PCPN_COMMENT_TEXT_FOR_WRK | EvalParticipantPEOPcpnCommentTextForWrk | ✅ |
| PCPN_COMMENTS_FOR_WRK | EvalParticipantPEOPcpnCommentsForWrk | ✅ |
| PERSON_ID | EvalParticipantPEOPersonId | ✅ |
| QUESTIONNAIRE_ID | EvalParticipantPEOQuestionnaireId | — |
| ROLE_TYPE_CODE | EvalParticipantPEORoleTypeCode | — |
| STATUS_UPDATE_DATE | EvalParticipantPEOStatusUpdateDate | ✅ |

### [[managerperformanceoverallratingpvo|ManagerPerformanceOverallRatingPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EvalParticipantPEOBusinessGroupId | — |
| EVAL_PARTICIPANT_ID | EvalParticipantPEOEvalParticipantId | — |
| EVAL_ROLE_ID | EvalParticipantPEOEvalRoleId | — |
| EVALUATION_ID | EvalParticipantPEOEvaluationId | — |
| PARTICIPATION_STATUS_CODE | EvalParticipantPEOParticipationStatusCode | — |
| PERSON_ID | EvalParticipantPEOPersonId | — |
| ROLE_TYPE_CODE | EvalParticipantPEORoleTypeCode | — |

### [[performancedocratingdistributionpvo|PerformanceDocRatingDistributionPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EVAL_PARTICIPANT_ID | EvalParticipantPEOEvalParticipantId | — |
| ROLE_TYPE_CODE | EvalParticipantPEORoleTypeCode | — |

### [[performancefinalfeedbackpvoformanager|PerformanceFinalFeedbackPVOForManager]] (HCM · BICC: 2/28)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDED_BY_PERSON_ID | EvalParticipantPEOAddedByPersonId | — |
| ADDED_BY_ROLE | EvalParticipantPEOAddedByRole | — |
| BUSINESS_GROUP_ID | EvalParticipantPEOBusinessGroupId | — |
| CREATED_BY | EvalParticipantPEOCreatedBy | — |
| CREATION_DATE | EvalParticipantPEOCreationDate | — |
| DUE_DATE | EvalParticipantPEODueDate | — |
| EVAL_PARTICIPANT_ID | EvalParticipantId | ✅ |
| EVAL_ROLE_ID | EvalParticipantPEOEvalRoleId | — |
| EVALUATION_ID | EvaluationId | — |
| FDBACK_COMPLETION_DATE | EvalParticipantPEOFdbackCompletionDate | — |
| FDBACK_SENT_BACK_FLAG | EvalParticipantPEOFdbackSentBackFlag | — |
| FDBACK_STARTED_FLAG | EvalParticipantPEOFdbackStartedFlag | — |
| LAST_UPDATE_DATE | EvalParticipantPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | EvalParticipantPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | EvalParticipantPEOLastUpdatedBy | — |
| LOCKED_OUT_DATE | EvalParticipantPEOLockedOutDate | — |
| LOCKED_OUT_FLAG | EvalParticipantPEOLockedOutFlag | — |
| NOTIFIED_BY_PERSON_ID | EvalParticipantPEONotifiedByPersonId | — |
| NOTIFIED_BY_ROLE | EvalParticipantPEONotifiedByRole | — |
| NOTIFIED_FLAG | EvalParticipantPEONotifiedFlag | — |
| OBJECT_VERSION_NUMBER | EvalParticipantPEOObjectVersionNumber | — |
| PARTICIPATION_STATUS_CODE | EvalParticipantPEOParticipationStatusCode | — |
| PCPN_COMMENT_TEXT_FOR_WRK | EvalParticipantPEOPcpnCommentTextForWrk | — |
| PCPN_COMMENTS_FOR_WRK | EvalParticipantPEOPcpnCommentsForWrk | — |
| PERSON_ID | EvalParticipantPEOPersonId | — |
| QUESTIONNAIRE_ID | EvalParticipantPEOQuestionnaireId | — |
| ROLE_TYPE_CODE | EvalParticipantPEORoleTypeCode | — |
| STATUS_UPDATE_DATE | EvalParticipantPEOStatusUpdateDate | — |

### [[performancefinalfeedbackpvoforworker|PerformanceFinalFeedbackPVOForWorker]] (HCM · BICC: 2/28)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDED_BY_PERSON_ID | EvalParticipantPEOAddedByPersonId | — |
| ADDED_BY_ROLE | EvalParticipantPEOAddedByRole | — |
| BUSINESS_GROUP_ID | EvalParticipantPEOBusinessGroupId | — |
| CREATED_BY | EvalParticipantPEOCreatedBy | — |
| CREATION_DATE | EvalParticipantPEOCreationDate | — |
| DUE_DATE | EvalParticipantPEODueDate | — |
| EVAL_PARTICIPANT_ID | EvalParticipantId | ✅ |
| EVAL_ROLE_ID | EvalParticipantPEOEvalRoleId | — |
| EVALUATION_ID | EvaluationId | — |
| FDBACK_COMPLETION_DATE | EvalParticipantPEOFdbackCompletionDate | — |
| FDBACK_SENT_BACK_FLAG | EvalParticipantPEOFdbackSentBackFlag | — |
| FDBACK_STARTED_FLAG | EvalParticipantPEOFdbackStartedFlag | — |
| LAST_UPDATE_DATE | EvalParticipantPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | EvalParticipantPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | EvalParticipantPEOLastUpdatedBy | — |
| LOCKED_OUT_DATE | EvalParticipantPEOLockedOutDate | — |
| LOCKED_OUT_FLAG | EvalParticipantPEOLockedOutFlag | — |
| NOTIFIED_BY_PERSON_ID | EvalParticipantPEONotifiedByPersonId | — |
| NOTIFIED_BY_ROLE | EvalParticipantPEONotifiedByRole | — |
| NOTIFIED_FLAG | EvalParticipantPEONotifiedFlag | — |
| OBJECT_VERSION_NUMBER | EvalParticipantPEOObjectVersionNumber | — |
| PARTICIPATION_STATUS_CODE | EvalParticipantPEOParticipationStatusCode | — |
| PCPN_COMMENT_TEXT_FOR_WRK | EvalParticipantPEOPcpnCommentTextForWrk | — |
| PCPN_COMMENTS_FOR_WRK | EvalParticipantPEOPcpnCommentsForWrk | — |
| PERSON_ID | EvalParticipantPEOPersonId | — |
| QUESTIONNAIRE_ID | EvalParticipantPEOQuestionnaireId | — |
| ROLE_TYPE_CODE | EvalParticipantPEORoleTypeCode | — |
| STATUS_UPDATE_DATE | EvalParticipantPEOStatusUpdateDate | — |

### [[performanceitemratingpvo|PerformanceItemRatingPVO]] (HCM · BICC: 2/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EvalParticipantPEOBusinessGroupId | — |
| EVAL_PARTICIPANT_ID | EvalParticipantPEOEvalParticipantId | — |
| EVAL_ROLE_ID | EvalParticipantPEOEvalRoleId | — |
| EVALUATION_ID | EvalParticipantPEOEvaluationId | — |
| LAST_UPDATE_DATE | EvalParticipantPEOLastUpdateDate | ✅ |
| PARTICIPATION_STATUS_CODE | EvalParticipantPEOParticipationStatusCode | — |
| PERSON_ID | EvalParticipantPEOPersonId | — |
| QUESTIONNAIRE_ID | EvalParticipantPEOQuestionnaireId | — |
| ROLE_TYPE_CODE | EvalParticipantPEORoleTypeCode | ✅ |

### [[performanceoverallratingpvo|PerformanceOverallRatingPVO]] (HCM · BICC: 2/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EvalParticipantPEOBusinessGroupId | — |
| EVAL_PARTICIPANT_ID | EvalParticipantPEOEvalParticipantId | — |
| EVAL_ROLE_ID | EvalParticipantPEOEvalRoleId | — |
| EVALUATION_ID | EvalParticipantPEOEvaluationId | — |
| LAST_UPDATE_DATE | EvalParticipantPEOLastUpdateDate | ✅ |
| PARTICIPATION_STATUS_CODE | EvalParticipantPEOParticipationStatusCode | — |
| PERSON_ID | EvalParticipantPEOPersonId | — |
| QUESTIONNAIRE_ID | EvalParticipantPEOQuestionnaireId | — |
| ROLE_TYPE_CODE | EvalParticipantPEORoleTypeCode | ✅ |

### [[performancesectionratingpvo|PerformanceSectionRatingPVO]] (HCM · BICC: 2/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EvalParticipantPEOBusinessGroupId | — |
| EVAL_PARTICIPANT_ID | EvalParticipantPEOEvalParticipantId | — |
| EVAL_ROLE_ID | EvalParticipantPEOEvalRoleId | — |
| EVALUATION_ID | EvalParticipantPEOEvaluationId | — |
| LAST_UPDATE_DATE | EvalParticipantPEOLastUpdateDate | ✅ |
| PARTICIPATION_STATUS_CODE | EvalParticipantPEOParticipationStatusCode | — |
| PERSON_ID | EvalParticipantPEOPersonId | — |
| QUESTIONNAIRE_ID | EvalParticipantEOQuestionnaireId | — |
| ROLE_TYPE_CODE | EvalParticipantPEORoleTypeCode | ✅ |

### [[proficiencyitemratingpvo|ProficiencyItemRatingPVO]] (HCM · BICC: 2/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EvalParticipantPEOBusinessGroupId | — |
| EVAL_PARTICIPANT_ID | EvalParticipantPEOEvalParticipantId | — |
| EVAL_ROLE_ID | EvalParticipantPEOEvalRoleId | — |
| EVALUATION_ID | EvalParticipantPEOEvaluationId | — |
| LAST_UPDATE_DATE | EvalParticipantPEOLastUpdateDate | ✅ |
| PARTICIPATION_STATUS_CODE | EvalParticipantPEOParticipationStatusCode | — |
| PERSON_ID | EvalParticipantPEOPersonId | — |
| QUESTIONNAIRE_ID | EvalParticipantPEOQuestionnaireId | — |
| ROLE_TYPE_CODE | EvalParticipantPEORoleTypeCode | ✅ |

---

## 📚 Referências

- [Oracle Docs — HRA_EVAL_PARTICIPANTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hraevalparticipants.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
