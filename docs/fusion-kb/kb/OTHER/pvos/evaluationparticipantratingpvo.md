---
id: DOC-OTHER-PVO-EvaluationParticipantRatingPVO
doc_type: system-doc
title: "EvaluationParticipantRatingPVO — PVO Cross-Module"
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
  - EvaluationParticipantRatingPVO
  - evaluationparticipantratingpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EvaluationParticipantRatingPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Evaluation Participant Rating. Acessa as tabelas: HRA_EVALUATIONS, HRA_EVAL_PARTICIPANTS, HRA_EVAL_RATINGS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceDocsAM.EvaluationParticipantRatingPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 59 | 3 | 3 | 19 | 32% |

---

## 🔗 Tabelas Relacionadas

- [[hra_evaluations|HRA_EVALUATIONS]] — 28 atributos (1 PKs, 14 BICC)
- [[hra_eval_participants|HRA_EVAL_PARTICIPANTS]] — 20 atributos (1 PKs, 2 BICC)
- [[hra_eval_ratings|HRA_EVAL_RATINGS]] — 11 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[hra_evaluations|HRA_EVALUATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | EvaluationId | EVALUATION_ID | 🔑 | ✅ |
| 4 | EvaluationPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 5 | EvaluationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 6 | EvaluationPEOCalculationRatingsFlag | CALCULATION_RATINGS_FLAG | — | ✅ |
| 7 | EvaluationPEODecimalPlaces | DECIMAL_PLACES | — | — |
| 8 | EvaluationPEOEndDate | END_DATE | — | ✅ |
| 9 | EvaluationPEOEvaluationDate | EVALUATION_DATE | — | ✅ |
| 10 | EvaluationPEOLockedByUserId | LOCKED_BY_USER_ID | — | — |
| 11 | EvaluationPEOManagerComments | MANAGER_COMMENTS | — | — |
| 12 | EvaluationPEOManagerId | MANAGER_ID | — | ✅ |
| 13 | EvaluationPEOMappingMethodCode | MAPPING_METHOD_CODE | — | ✅ |
| 14 | EvaluationPEOMeetingHeldDate | MEETING_HELD_DATE | — | ✅ |
| 15 | EvaluationPEOPrevStatusCode | PREV_STATUS_CODE | — | ✅ |
| 16 | EvaluationPEORoundingRuleCode | ROUNDING_RULE_CODE | — | ✅ |
| 17 | EvaluationPEOSelectManagerAllowedFlag | SELECT_MANAGER_ALLOWED_FLAG | — | ✅ |
| 18 | EvaluationPEOStarRatingEnabledFlag | STAR_RATING_ENABLED_FLAG | — | ✅ |
| 19 | EvaluationPEOStartDate | START_DATE | — | ✅ |
| 20 | EvaluationPEOStatusCode | STATUS_CODE | — | ✅ |
| 21 | EvaluationPEOTemplateDefnId | TEMPLATE_DEFN_ID | — | — |
| 22 | EvaluationPEOTmplPeriodId | TMPL_PERIOD_ID | — | — |
| 23 | EvaluationPEOWorkerComments | WORKER_COMMENTS | — | — |
| 24 | EvaluationPEOWorkerId | WORKER_ID | — | — |
| 25 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 27 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 28 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[hra_eval_participants|HRA_EVAL_PARTICIPANTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EvalParticipantId | EVAL_PARTICIPANT_ID | 🔑 | ✅ |
| 2 | EvalParticipantPEOAddedByPersonId | ADDED_BY_PERSON_ID | — | — |
| 3 | EvalParticipantPEOAddedByRole | ADDED_BY_ROLE | — | — |
| 4 | EvalParticipantPEOEvalRoleId | EVAL_ROLE_ID | — | — |
| 5 | EvalParticipantPEOFdbackCompletionDate | FDBACK_COMPLETION_DATE | — | — |
| 6 | EvalParticipantPEOFdbackSentBackFlag | FDBACK_SENT_BACK_FLAG | — | — |
| 7 | EvalParticipantPEOFdbackStartedFlag | FDBACK_STARTED_FLAG | — | — |
| 8 | EvalParticipantPEOLockedOutDate | LOCKED_OUT_DATE | — | — |
| 9 | EvalParticipantPEOLockedOutFlag | LOCKED_OUT_FLAG | — | — |
| 10 | EvalParticipantPEONotifiedByPersonId | NOTIFIED_BY_PERSON_ID | — | — |
| 11 | EvalParticipantPEONotifiedByRole | NOTIFIED_BY_ROLE | — | — |
| 12 | EvalParticipantPEONotifiedFlag | NOTIFIED_FLAG | — | — |
| 13 | EvalParticipantPEOParticipationStatus | PARTICIPATION_STATUS_CODE | — | — |
| 14 | EvalParticipantPEOPcpnCommentTextForWrk | PCPN_COMMENT_TEXT_FOR_WRK | — | — |
| 15 | EvalParticipantPEOPcpnCommentsForWrk | PCPN_COMMENTS_FOR_WRK | — | — |
| 16 | EvalParticipantPEOPersonId | PERSON_ID | — | — |
| 17 | EvalParticipantPEOQuestionnaireId | QUESTIONNAIRE_ID | — | — |
| 18 | EvalParticipantPEORoleTypeCode | ROLE_TYPE_CODE | — | — |
| 19 | EvalParticipantPEOStatusUpdateDate | STATUS_UPDATE_DATE | — | — |
| 20 | EvalRatingPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hra_eval_ratings|HRA_EVAL_RATINGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EvalRatingId | EVAL_RATING_ID | 🔑 | ✅ |
| 2 | EvalRatingPEOCalculatedRating | CALCULATED_RATING | — | — |
| 3 | EvalRatingPEOCommentText | COMMENT_TEXT | — | ✅ |
| 4 | EvalRatingPEOComments | COMMENTS | — | — |
| 5 | EvalRatingPEOPerformanceRatingId | PERFORMANCE_RATING_ID | — | — |
| 6 | EvalRatingPEOProficiencyRatingId | PROFICIENCY_RATING_ID | — | — |
| 7 | EvalRatingPEOReferenceId | REFERENCE_ID | — | — |
| 8 | EvalRatingPEOReferenceType | REFERENCE_TYPE | — | — |
| 9 | EvalRatingPEOReviewPoints | REVIEW_POINTS | — | — |
| 10 | EvalRatingPEORoleTypeCode | ROLE_TYPE_CODE | — | — |
| 11 | EvalSectionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
