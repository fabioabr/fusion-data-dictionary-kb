---
id: DOC-OTHER-PVO-ParticipantResponsePVO
doc_type: system-doc
title: "ParticipantResponsePVO — PVO Cross-Module"
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
  - ParticipantResponsePVO
  - participantresponsepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ParticipantResponsePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Participant Response. Acessa as tabelas: HRQ_ALL_QSTN_RESPONSES_V, HRQ_QSTNR_PARTICIPANTS, HRQ_QSTNR_RESPONSES (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.QuestionnaireAM.ParticipantResponsePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 56 | 4 | 2 | 26 | 46% |

---

## 🔗 Tabelas Relacionadas

- [[hrq_all_qstn_responses_v|HRQ_ALL_QSTN_RESPONSES_V]] — 8 atributos (5 BICC)
- [[hrq_qstnr_participants|HRQ_QSTNR_PARTICIPANTS]] — 16 atributos (2 PKs, 6 BICC)
- [[hrq_qstnr_responses|HRQ_QSTNR_RESPONSES]] — 15 atributos (10 BICC)
- [[hrq_qstn_responses|HRQ_QSTN_RESPONSES]] — 17 atributos (5 BICC)

---

## ⚙️ Atributos

### [[hrq_all_qstn_responses_v|HRQ_ALL_QSTN_RESPONSES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QuestionResponsePEOAnswerClob | ANSWER_CLOB | — | ✅ |
| 2 | QuestionResponsePEOAnswerId | ANSWER_ID | — | ✅ |
| 3 | QuestionResponsePEOAnswerText | ANSWER_TEXT | — | — |
| 4 | QuestionResponsePEOAnswerType | ANSWER_TYPE | — | — |
| 5 | QuestionResponsePEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 6 | QuestionResponsePEOQstnResponseId | QSTN_RESPONSE_ID | — | ✅ |
| 7 | QuestionResponsePEOQstnrQuestionId | QSTNR_QUESTION_ID | — | ✅ |
| 8 | QuestionResponsePEOQstnrResponseId | QSTNR_RESPONSE_ID | — | — |

### [[hrq_qstnr_participants|HRQ_QSTNR_PARTICIPANTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QuestionnairePartcipantPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | QuestionnairePartcipantPEOParticipantId | PARTICIPANT_ID | — | ✅ |
| 3 | QuestionnairePartcipantPEOQstnrParticipantId | QSTNR_PARTICIPANT_ID | 🔑 | ✅ |
| 4 | QuestionnairePartcipantPEOQuestionnaireId | QUESTIONNAIRE_ID | — | — |
| 5 | QuestionnairePartcipantPEOSubjectId | SUBJECT_ID | — | ✅ |
| 6 | QuestionnairePartcipantPEOSubscriberId | SUBSCRIBER_ID | — | — |
| 7 | QuestionnaireParticipantPEOCreatedBy | CREATED_BY | — | — |
| 8 | QuestionnaireParticipantPEOCreationDate | CREATION_DATE | — | — |
| 9 | QuestionnaireParticipantPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | QuestionnaireParticipantPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | QuestionnaireParticipantPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | QuestionnaireParticipantPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | QuestionnaireParticipantPEOParticipantType | PARTICIPANT_TYPE | — | — |
| 14 | QuestionnaireParticipantPEOStatus | STATUS | — | — |
| 15 | QuestionnaireParticipantPEOSubjectCode | SUBJECT_CODE | — | — |
| 16 | QuestionnaireParticipantPEOSubmittedDateTime | SUBMITTED_DATE_TIME | — | ✅ |

### [[hrq_qstnr_responses|HRQ_QSTNR_RESPONSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LatestAttemptFlag | LATEST_ATTEMPT_FLAG | — | ✅ |
| 2 | QuestionnaireResponsePEOAttemptNum | ATTEMPT_NUM | — | ✅ |
| 3 | QuestionnaireResponsePEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 4 | QuestionnaireResponsePEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | QuestionnaireResponsePEOCreationDate | CREATION_DATE | — | — |
| 6 | QuestionnaireResponsePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | QuestionnaireResponsePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | QuestionnaireResponsePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | QuestionnaireResponsePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | QuestionnaireResponsePEOQstnrParticipantId | QSTNR_PARTICIPANT_ID | — | — |
| 11 | QuestionnaireResponsePEOQstnrResponseId | QSTNR_RESPONSE_ID | — | ✅ |
| 12 | QuestionnaireResponsePEOQstnrVersionNum | QSTNR_VERSION_NUM | — | — |
| 13 | QuestionnaireResponsePEOStatus | STATUS | — | ✅ |
| 14 | QuestionnaireResponsePEOSubmittedDateTime | SUBMITTED_DATE_TIME | — | ✅ |
| 15 | QuestionnaireResponsePEOTotalScore | TOTAL_SCORE | — | ✅ |

### [[hrq_qstn_responses|HRQ_QSTN_RESPONSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QstnResponsePEOAnswerClob | ANSWER_CLOB | — | — |
| 2 | QstnResponsePEOAnswerComments | ANSWER_COMMENTS | — | — |
| 3 | QstnResponsePEOAnswerList | ANSWER_LIST | — | — |
| 4 | QstnResponsePEOAnswerText | ANSWER_TEXT | — | — |
| 5 | QstnResponsePEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 6 | QstnResponsePEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | QstnResponsePEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | QstnResponsePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | QstnResponsePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | QstnResponsePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | QstnResponsePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | QstnResponsePEOQstnAnswerId | QSTN_ANSWER_ID | — | — |
| 13 | QstnResponsePEOQstnResponseId | QSTN_RESPONSE_ID | — | — |
| 14 | QstnResponsePEOQstnrQuestionId | QSTNR_QUESTION_ID | — | — |
| 15 | QstnResponsePEOQstnrResponseId | QSTNR_RESPONSE_ID | — | — |
| 16 | QstnResponsePEOScore | SCORE | — | ✅ |
| 17 | QstnResponsePEOSubQuestionId | SUB_QUESTION_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
