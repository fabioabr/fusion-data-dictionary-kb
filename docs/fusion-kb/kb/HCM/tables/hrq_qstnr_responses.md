---
id: DOC-HCM-188
doc_type: system-doc
title: "HRQ_QSTNR_RESPONSES — Respostas Consolidadas de Questionários"
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
  - questionnaires
  - responses
aliases:
  - HRQ_QSTNR_RESPONSES
  - hrq_qstnr_responses
  - respostas-consolidadas-de-questionários
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRQ_QSTNR_RESPONSES

## 📌 Visão Geral

Armazena **respostas consolidadas** por questionário/participante.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro consolidado:** Status de preenchimento.
- **Rastreamento de submissão:** Quando foi submetido.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | QSTNR_RESPONSE_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | QUESTIONNAIRE_ID | NUMBER(18) | NOT NULL | FK | Questionário | [[hrq_questionnaires_b]] | 🟢 90% |
| 3 | PARTICIPANT_ID | NUMBER(18) | NOT NULL | FK | Participante | [[hrq_qstnr_participants]] | 🟢 85% |
| 4 | RESPONSE_STATUS | VARCHAR2(30) | NULL | Classificação | Status (DRAFT, SUBMITTED, LOCKED) | — | 🟡 75% |
| 5 | SUBMITTED_DATE | TIMESTAMP | NULL | Data | Data de submissão | — | 🟡 75% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 11 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai

---

## 📎 Uso Típico

### Respostas submetidas
```sql
SELECT qr.RESPONSE_STATUS, qr.SUBMITTED_DATE
FROM   HRQ_QSTNR_RESPONSES qr
WHERE  qr.QUESTIONNAIRE_ID = :p_id AND qr.RESPONSE_STATUS = 'SUBMITTED';
```

---

## 🔒 Observações

- Ciclo: DRAFT -> SUBMITTED -> LOCKED.

---

## 🔗 PVOs Relacionados

### [[participantquestionnairequestionresponsepvo|ParticipantQuestionnaireQuestionResponsePVO]] (HCM · BICC: 9/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTEMPT_NUM | QuestionnaireResponsePEOAttemptNum | ✅ |
| BUSINESS_GROUP_ID | QuestionnaireResponsePEOBusinessGroupId | ✅ |
| CREATED_BY | QuestionnaireResponsePEOCreatedBy | ✅ |
| CREATION_DATE | QuestionnaireResponsePEOCreationDate | ✅ |
| LAST_UPDATE_DATE | QuestionnaireResponsePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireResponsePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionnaireResponsePEOLastUpdatedBy | ✅ |
| LATEST_ATTEMPT_FLAG | LatestAttemptFlag | — |
| OBJECT_VERSION_NUMBER | QuestionnaireResponsePEOObjectVersionNumber | — |
| QSTNR_PARTICIPANT_ID | QuestionnaireResponsePEOQstnrParticipantId | — |
| QSTNR_RESPONSE_ID | QuestionnaireResponsePEOQstnrResponseId | ✅ |
| QSTNR_VERSION_NUM | QuestionnaireResponsePEOQstnrVersionNum | — |
| STATUS | QuestionnaireResponsePEOStatus | ✅ |
| SUBMITTED_DATE_TIME | QuestionnaireResponsePEOSubmittedDateTime | ✅ |
| TOTAL_SCORE | QuestionnaireResponsePEOTotalScore | — |

### [[participantresponsepvo|ParticipantResponsePVO]] (HCM · BICC: 10/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTEMPT_NUM | QuestionnaireResponsePEOAttemptNum | ✅ |
| BUSINESS_GROUP_ID | QuestionnaireResponsePEOBusinessGroupId | ✅ |
| CREATED_BY | QuestionnaireResponsePEOCreatedBy | ✅ |
| CREATION_DATE | QuestionnaireResponsePEOCreationDate | — |
| LAST_UPDATE_DATE | QuestionnaireResponsePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireResponsePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionnaireResponsePEOLastUpdatedBy | — |
| LATEST_ATTEMPT_FLAG | LatestAttemptFlag | ✅ |
| OBJECT_VERSION_NUMBER | QuestionnaireResponsePEOObjectVersionNumber | ✅ |
| QSTNR_PARTICIPANT_ID | QuestionnaireResponsePEOQstnrParticipantId | — |
| QSTNR_RESPONSE_ID | QuestionnaireResponsePEOQstnrResponseId | ✅ |
| QSTNR_VERSION_NUM | QuestionnaireResponsePEOQstnrVersionNum | — |
| STATUS | QuestionnaireResponsePEOStatus | ✅ |
| SUBMITTED_DATE_TIME | QuestionnaireResponsePEOSubmittedDateTime | ✅ |
| TOTAL_SCORE | QuestionnaireResponsePEOTotalScore | ✅ |

### [[questionnairequestionresponsepvo|QuestionnaireQuestionResponsePVO]] (HCM · BICC: 7/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTEMPT_NUM | QuestionnaireResponsePEOAttemptNum | ✅ |
| BUSINESS_GROUP_ID | QuestionnaireResponsePEOBusinessGroupId | ✅ |
| CREATED_BY | QuestionnaireResponsePEOCreatedBy | — |
| CREATION_DATE | QuestionnaireResponsePEOCreationDate | — |
| LAST_UPDATE_DATE | QuestionnaireResponsePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireResponsePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionnaireResponsePEOLastUpdatedBy | — |
| LATEST_ATTEMPT_FLAG | LatestAttemptFlag | — |
| OBJECT_VERSION_NUMBER | QuestionnaireResponsePEOObjectVersionNumber | — |
| QSTNR_PARTICIPANT_ID | QuestionnaireResponsePEOQstnrParticipantId | ✅ |
| QSTNR_RESPONSE_ID | QuestionnaireResponsePEOQstnrResponseId | ✅ |
| QSTNR_VERSION_NUM | QuestionnaireResponsePEOQstnrVersionNum | — |
| STATUS | QuestionnaireResponsePEOStatus | ✅ |
| SUBMITTED_DATE_TIME | QuestionnaireResponsePEOSubmittedDateTime | ✅ |
| TOTAL_SCORE | QuestionnaireResponsePEOTotalScore | — |

### [[questionnaireresponse|QuestionnaireResponse]] (HCM · BICC: 15/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTEMPT_NUM | AttemptNum | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LATEST_ATTEMPT_FLAG | LatestAttemptFlag | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| QSTNR_PARTICIPANT_ID | QstnrParticipantId | ✅ |
| QSTNR_RESPONSE_ID | QstnrResponseId | ✅ |
| QSTNR_VERSION_NUM | QstnrVersionNum | ✅ |
| STATUS | Status | ✅ |
| SUBMITTED_DATE_TIME | SubmittedDateTime | ✅ |
| TOTAL_SCORE | TotalScore | ✅ |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
