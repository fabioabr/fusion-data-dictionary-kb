---
id: DOC-OTHER-PVO-EvaluationParticipantRolePVO
doc_type: system-doc
title: "EvaluationParticipantRolePVO — PVO Cross-Module"
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
  - EvaluationParticipantRolePVO
  - evaluationparticipantrolepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EvaluationParticipantRolePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Evaluation Participant Role. Acessa as tabelas: HRA_EVAL_PARTICIPANTS, HRA_EVAL_ROLES.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceDocsAM.EvaluationParticipantRolePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 36 | 2 | 2 | 26 | 72% |

---

## 🔗 Tabelas Relacionadas

- [[hra_eval_participants|HRA_EVAL_PARTICIPANTS]] — 31 atributos (1 PKs, 23 BICC)
- [[hra_eval_roles|HRA_EVAL_ROLES]] — 5 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[hra_eval_participants|HRA_EVAL_PARTICIPANTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionCode | ACTION_CODE | — | — |
| 2 | ActionPerformedBy | ACTION_PERFORMED_BY | — | — |
| 3 | ActionPerformedDate | ACTION_PERFORMED_DATE | — | — |
| 4 | ActionReason | ACTION_REASON | — | — |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | EvalParticipantId | EVAL_PARTICIPANT_ID | 🔑 | ✅ |
| 8 | EvalParticipantPEOAddedByPersonId | ADDED_BY_PERSON_ID | — | ✅ |
| 9 | EvalParticipantPEOAddedByRole | ADDED_BY_ROLE | — | ✅ |
| 10 | EvalParticipantPEODueDate | DUE_DATE | — | ✅ |
| 11 | EvalParticipantPEOEvalRoleId | EVAL_ROLE_ID | — | ✅ |
| 12 | EvalParticipantPEOEvaluationId | EVALUATION_ID | — | — |
| 13 | EvalParticipantPEOFdbackCompletionDate | FDBACK_COMPLETION_DATE | — | ✅ |
| 14 | EvalParticipantPEOFdbackSentBackFlag | FDBACK_SENT_BACK_FLAG | — | ✅ |
| 15 | EvalParticipantPEOFdbackStartedFlag | FDBACK_STARTED_FLAG | — | ✅ |
| 16 | EvalParticipantPEOLockedOutDate | LOCKED_OUT_DATE | — | ✅ |
| 17 | EvalParticipantPEOLockedOutFlag | LOCKED_OUT_FLAG | — | ✅ |
| 18 | EvalParticipantPEONotifiedByPersonId | NOTIFIED_BY_PERSON_ID | — | ✅ |
| 19 | EvalParticipantPEONotifiedByRole | NOTIFIED_BY_ROLE | — | ✅ |
| 20 | EvalParticipantPEONotifiedFlag | NOTIFIED_FLAG | — | ✅ |
| 21 | EvalParticipantPEOParticipationStatus | PARTICIPATION_STATUS_CODE | — | ✅ |
| 22 | EvalParticipantPEOPcpnCommentTextForWrk | PCPN_COMMENT_TEXT_FOR_WRK | — | ✅ |
| 23 | EvalParticipantPEOPcpnCommentsForWrk | PCPN_COMMENTS_FOR_WRK | — | ✅ |
| 24 | EvalParticipantPEOPersonId | PERSON_ID | — | ✅ |
| 25 | EvalParticipantPEOQuestionnaireId | QUESTIONNAIRE_ID | — | — |
| 26 | EvalParticipantPEORoleTypeCode | ROLE_TYPE_CODE | — | — |
| 27 | EvalParticipantPEOStatusUpdateDate | STATUS_UPDATE_DATE | — | ✅ |
| 28 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 29 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 30 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 31 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[hra_eval_roles|HRA_EVAL_ROLES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EvalRoleId | EVAL_ROLE_ID | 🔑 | ✅ |
| 2 | EvalRolePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | EvalRolePEOMinimumNumPcpns | MINIMUM_NUM_PCPNS | — | — |
| 4 | EvalRolePEORoleTypeCode | ROLE_TYPE_CODE | — | ✅ |
| 5 | EvalRolePEOTmplRoleId | TMPL_ROLE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
