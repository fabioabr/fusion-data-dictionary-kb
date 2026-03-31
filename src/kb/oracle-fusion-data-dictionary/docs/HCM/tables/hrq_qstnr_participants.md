---
id: DOC-HCM-186
doc_type: system-doc
title: "HRQ_QSTNR_PARTICIPANTS — Participantes de Questionários"
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
  - participants
aliases:
  - HRQ_QSTNR_PARTICIPANTS
  - hrq_qstnr_participants
  - participantes-de-questionários
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRQ_QSTNR_PARTICIPANTS

## 📌 Visão Geral

Armazena **participantes** de questionários HCM. Quem foi convidado e status da participação.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão:** Participantes e status.
- **Rastreamento:** Completude de respostas.
- **Notificações:** Lembretes para participantes.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PARTICIPANT_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | QUESTIONNAIRE_ID | NUMBER(18) | NOT NULL | FK | Questionário | [[hrq_questionnaires_b]] | 🟢 90% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Pessoa | [[per_all_people_f]] | 🟢 90% |
| 4 | PARTICIPANT_ROLE | VARCHAR2(30) | NULL | Classificação | Papel (RESPONDENT, REVIEWER) | — | 🟡 70% |
| 5 | STATUS_CODE | VARCHAR2(30) | NULL | Classificação | Status (INVITED, IN_PROGRESS, COMPLETED) | — | 🟡 75% |
| 6 | COMPLETION_DATE | TIMESTAMP | NULL | Data | Data de conclusão | — | 🟡 70% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrq_questionnaires_b]] — via `QUESTIONNAIRE_ID` (questionario do participante)
- [[per_all_people_f]] — via `PERSON_ID` (participante do questionario)

---

## 📎 Uso Típico

### Participantes com respostas completas
```sql
SELECT p.PERSON_ID, p.PARTICIPANT_ROLE, p.STATUS_CODE
FROM   HRQ_QSTNR_PARTICIPANTS p
WHERE  p.QUESTIONNAIRE_ID = :p_id AND p.STATUS_CODE = 'COMPLETED';
```

---

## 🔒 Observações

- Ciclo: INVITED -> IN_PROGRESS -> COMPLETED/DECLINED.

---

## 🔗 PVOs Relacionados

### [[managerquestionnairequestionpvo|ManagerQuestionnaireQuestionPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnaireParticipantPEOBusinessGroupId | — |
| LAST_UPDATE_DATE | QuestionnaireBPEOLastUpdateDate | — |
| PARTICIPANT_ID | QuestionnaireParticipantPEOParticipantId | — |
| PARTICIPANT_TYPE | QuestionnaireParticipantPEOParticipantType | — |
| QSTNR_PARTICIPANT_ID | QuestionnaireParticipantPEOQstnrParticipantId | — |
| QUESTIONNAIRE_ID | QuestionnaireParticipantPEOQuestionnaireId | — |
| STATUS | QuestionnaireParticipantPEOStatus | — |
| SUBJECT_CODE | QuestionnaireParticipantPEOSubjectCode | — |
| SUBJECT_ID | QuestionnaireParticipantPEOSubjectId | — |
| SUBMITTED_DATE_TIME | QuestionnaireParticipantPEOSubmittedDateTime | — |
| SUBSCRIBER_ID | QuestionnaireParticipantPEOSubscriberId | — |

### [[participantquestionnairequestionpvo|ParticipantQuestionnaireQuestionPVO]] (HCM · BICC: 4/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnaireParticipantPEOBusinessGroupId | ✅ |
| LAST_UPDATE_DATE | QuestionnaireBPEOLastUpdateDate | — |
| PARTICIPANT_ID | QuestionnaireParticipantPEOParticipantId | — |
| PARTICIPANT_TYPE | QuestionnaireParticipantPEOParticipantType | — |
| QSTNR_PARTICIPANT_ID | QuestionnaireParticipantPEOQstnrParticipantId | ✅ |
| QUESTIONNAIRE_ID | QuestionnaireParticipantPEOQuestionnaireId | ✅ |
| STATUS | QuestionnaireParticipantPEOStatus | — |
| SUBJECT_CODE | QuestionnaireParticipantPEOSubjectCode | — |
| SUBJECT_ID | QuestionnaireParticipantPEOSubjectId | ✅ |
| SUBMITTED_DATE_TIME | QuestionnaireParticipantPEOSubmittedDateTime | — |
| SUBSCRIBER_ID | QuestionnaireParticipantPEOSubscriberId | — |

### [[participantquestionnairequestionpvoforpotentialassessement|ParticipantQuestionnaireQuestionPVOForPotentialAssessement]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnaireParticipantPEOBusinessGroupId | — |
| LAST_UPDATE_DATE | QuestionnaireBPEOLastUpdateDate | — |
| PARTICIPANT_ID | QuestionnaireParticipantPEOParticipantId | — |
| PARTICIPANT_TYPE | QuestionnaireParticipantPEOParticipantType | — |
| QSTNR_PARTICIPANT_ID | QuestionnaireParticipantPEOQstnrParticipantId | — |
| QUESTIONNAIRE_ID | QuestionnaireParticipantPEOQuestionnaireId | — |
| STATUS | QuestionnaireParticipantPEOStatus | — |
| SUBJECT_CODE | QuestionnaireParticipantPEOSubjectCode | — |
| SUBJECT_ID | QuestionnaireParticipantPEOSubjectId | — |
| SUBMITTED_DATE_TIME | QuestionnaireParticipantPEOSubmittedDateTime | — |
| SUBSCRIBER_ID | QuestionnaireParticipantPEOSubscriberId | — |

### [[participantquestionnairequestionresponsepvo|ParticipantQuestionnaireQuestionResponsePVO]] (HCM · BICC: 4/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnairePartcipantPEOBusinessGroupId | ✅ |
| CREATED_BY | QuestionnaireParticipantPEOCreatedBy | — |
| CREATION_DATE | QuestionnaireParticipantPEOCreationDate | — |
| LAST_UPDATE_DATE | QuestionnaireParticipantPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireParticipantPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionnaireParticipantPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | QuestionnaireParticipantPEOObjectVersionNumber | — |
| PARTICIPANT_ID | QuestionnairePartcipantPEOParticipantId | — |
| PARTICIPANT_TYPE | QuestionnaireParticipantPEOParticipantType | — |
| QSTNR_PARTICIPANT_ID | QuestionnairePartcipantPEOQstnrParticipantId | ✅ |
| QUESTIONNAIRE_ID | QuestionnairePartcipantPEOQuestionnaireId | — |
| STATUS | QuestionnaireParticipantPEOStatus | — |
| SUBJECT_CODE | QuestionnaireParticipantPEOSubjectCode | — |
| SUBJECT_ID | QuestionnairePartcipantPEOSubjectId | — |
| SUBMITTED_DATE_TIME | QuestionnaireParticipantPEOSubmittedDateTime | ✅ |
| SUBSCRIBER_ID | QuestionnairePartcipantPEOSubscriberId | — |

### [[participantresponsepvo|ParticipantResponsePVO]] (HCM · BICC: 6/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnairePartcipantPEOBusinessGroupId | ✅ |
| CREATED_BY | QuestionnaireParticipantPEOCreatedBy | — |
| CREATION_DATE | QuestionnaireParticipantPEOCreationDate | — |
| LAST_UPDATE_DATE | QuestionnaireParticipantPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireParticipantPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionnaireParticipantPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | QuestionnaireParticipantPEOObjectVersionNumber | — |
| PARTICIPANT_ID | QuestionnairePartcipantPEOParticipantId | ✅ |
| PARTICIPANT_TYPE | QuestionnaireParticipantPEOParticipantType | — |
| QSTNR_PARTICIPANT_ID | QuestionnairePartcipantPEOQstnrParticipantId | ✅ |
| QUESTIONNAIRE_ID | QuestionnairePartcipantPEOQuestionnaireId | — |
| STATUS | QuestionnaireParticipantPEOStatus | — |
| SUBJECT_CODE | QuestionnaireParticipantPEOSubjectCode | — |
| SUBJECT_ID | QuestionnairePartcipantPEOSubjectId | ✅ |
| SUBMITTED_DATE_TIME | QuestionnaireParticipantPEOSubmittedDateTime | ✅ |
| SUBSCRIBER_ID | QuestionnairePartcipantPEOSubscriberId | — |

### [[questionnairequestionresponsepvo|QuestionnaireQuestionResponsePVO]] (HCM · BICC: 4/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnairePartcipantPEOBusinessGroupId | ✅ |
| CREATED_BY | QuestionnaireParticipantPEOCreatedBy | — |
| CREATION_DATE | QuestionnaireParticipantPEOCreationDate | — |
| LAST_UPDATE_DATE | QuestionnaireParticipantPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireParticipantPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionnaireParticipantPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | QuestionnaireParticipantPEOObjectVersionNumber | — |
| PARTICIPANT_ID | QuestionnairePartcipantPEOParticipantId | — |
| PARTICIPANT_TYPE | QuestionnaireParticipantPEOParticipantType | — |
| QSTNR_PARTICIPANT_ID | QuestionnairePartcipantPEOQstnrParticipantId | ✅ |
| QUESTIONNAIRE_ID | QuestionnairePartcipantPEOQuestionnaireId | — |
| STATUS | QuestionnaireParticipantPEOStatus | — |
| SUBJECT_CODE | QuestionnaireParticipantPEOSubjectCode | — |
| SUBJECT_ID | QuestionnairePartcipantPEOSubjectId | ✅ |
| SUBMITTED_DATE_TIME | QuestionnaireParticipantPEOSubmittedDateTime | — |
| SUBSCRIBER_ID | QuestionnairePartcipantPEOSubscriberId | — |

### [[workerquestionnairequestionpvo|WorkerQuestionnaireQuestionPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnaireParticipantPEOBusinessGroupId | — |
| LAST_UPDATE_DATE | QuestionnaireBPEOLastUpdateDate | — |
| PARTICIPANT_ID | QuestionnaireParticipantPEOParticipantId | — |
| PARTICIPANT_TYPE | QuestionnaireParticipantPEOParticipantType | — |
| QSTNR_PARTICIPANT_ID | QuestionnaireParticipantPEOQstnrParticipantId | — |
| QUESTIONNAIRE_ID | QuestionnaireParticipantPEOQuestionnaireId | — |
| STATUS | QuestionnaireParticipantPEOStatus | — |
| SUBJECT_CODE | QuestionnaireParticipantPEOSubjectCode | — |
| SUBJECT_ID | QuestionnaireParticipantPEOSubjectId | — |
| SUBMITTED_DATE_TIME | QuestionnaireParticipantPEOSubmittedDateTime | — |
| SUBSCRIBER_ID | QuestionnaireParticipantPEOSubscriberId | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
