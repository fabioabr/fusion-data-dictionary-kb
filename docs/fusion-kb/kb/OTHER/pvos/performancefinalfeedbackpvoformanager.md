---
id: DOC-OTHER-PVO-PerformanceFinalFeedbackPVOForManager
doc_type: system-doc
title: "PerformanceFinalFeedbackPVOForManager — PVO Cross-Module"
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
  - PerformanceFinalFeedbackPVOForManager
  - performancefinalfeedbackpvoformanager
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PerformanceFinalFeedbackPVOForManager

## 📌 Visão Geral

View Object para extração BICC de dados de Performance Final Feedback For Manager. Acessa as tabelas: HRA_EVAL_PARTICIPANTS, HRA_EVAL_SECTIONS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceDocsAM.PerformanceFinalFeedbackPVOForManager`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 79 | 2 | 2 | 5 | 6% |

---

## 🔗 Tabelas Relacionadas

- [[hra_eval_participants|HRA_EVAL_PARTICIPANTS]] — 28 atributos (1 PKs, 2 BICC)
- [[hra_eval_sections|HRA_EVAL_SECTIONS]] — 51 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[hra_eval_participants|HRA_EVAL_PARTICIPANTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EvalParticipantId | EVAL_PARTICIPANT_ID | 🔑 | ✅ |
| 2 | EvalParticipantPEOAddedByPersonId | ADDED_BY_PERSON_ID | — | — |
| 3 | EvalParticipantPEOAddedByRole | ADDED_BY_ROLE | — | — |
| 4 | EvalParticipantPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 5 | EvalParticipantPEOCreatedBy | CREATED_BY | — | — |
| 6 | EvalParticipantPEOCreationDate | CREATION_DATE | — | — |
| 7 | EvalParticipantPEODueDate | DUE_DATE | — | — |
| 8 | EvalParticipantPEOEvalRoleId | EVAL_ROLE_ID | — | — |
| 9 | EvalParticipantPEOFdbackCompletionDate | FDBACK_COMPLETION_DATE | — | — |
| 10 | EvalParticipantPEOFdbackSentBackFlag | FDBACK_SENT_BACK_FLAG | — | — |
| 11 | EvalParticipantPEOFdbackStartedFlag | FDBACK_STARTED_FLAG | — | — |
| 12 | EvalParticipantPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | EvalParticipantPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | EvalParticipantPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | EvalParticipantPEOLockedOutDate | LOCKED_OUT_DATE | — | — |
| 16 | EvalParticipantPEOLockedOutFlag | LOCKED_OUT_FLAG | — | — |
| 17 | EvalParticipantPEONotifiedByPersonId | NOTIFIED_BY_PERSON_ID | — | — |
| 18 | EvalParticipantPEONotifiedByRole | NOTIFIED_BY_ROLE | — | — |
| 19 | EvalParticipantPEONotifiedFlag | NOTIFIED_FLAG | — | — |
| 20 | EvalParticipantPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | EvalParticipantPEOParticipationStatusCode | PARTICIPATION_STATUS_CODE | — | — |
| 22 | EvalParticipantPEOPcpnCommentTextForWrk | PCPN_COMMENT_TEXT_FOR_WRK | — | — |
| 23 | EvalParticipantPEOPcpnCommentsForWrk | PCPN_COMMENTS_FOR_WRK | — | — |
| 24 | EvalParticipantPEOPersonId | PERSON_ID | — | — |
| 25 | EvalParticipantPEOQuestionnaireId | QUESTIONNAIRE_ID | — | — |
| 26 | EvalParticipantPEORoleTypeCode | ROLE_TYPE_CODE | — | — |
| 27 | EvalParticipantPEOStatusUpdateDate | STATUS_UPDATE_DATE | — | — |
| 28 | EvaluationId | EVALUATION_ID | — | — |

### [[hra_eval_sections|HRA_EVAL_SECTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EvalSectionPEOAddItemsConfirmCritFlag | ADD_ITEMS_CONFIRM_CRIT_FLAG | — | — |
| 2 | EvalSectionPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | EvalSectionPEOCalculationRuleCode | CALCULATION_RULE_CODE | — | — |
| 4 | EvalSectionPEOCommentText | COMMENT_TEXT | — | ✅ |
| 5 | EvalSectionPEOComments | COMMENTS | — | — |
| 6 | EvalSectionPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 7 | EvalSectionPEOCreatedBy | CREATED_BY | — | — |
| 8 | EvalSectionPEOCreationDate | CREATION_DATE | — | — |
| 9 | EvalSectionPEOEnableItems | ENABLE_ITEMS | — | — |
| 10 | EvalSectionPEOEvalSectionId | EVAL_SECTION_ID | 🔑 | ✅ |
| 11 | EvalSectionPEOEvaluationId | EVALUATION_ID | — | — |
| 12 | EvalSectionPEOFastFormulaId | FAST_FORMULA_ID | — | — |
| 13 | EvalSectionPEOFreeFormAllowedFlag | FREE_FORM_ALLOWED_FLAG | — | — |
| 14 | EvalSectionPEOItemCalculationCode | ITEM_CALCULATION_CODE | — | — |
| 15 | EvalSectionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | EvalSectionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | EvalSectionPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | EvalSectionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | EvalSectionPEOPerfRatingModelId | PERF_RATING_MODEL_ID | — | — |
| 20 | EvalSectionPEOProfileId | PROFILE_ID | — | — |
| 21 | EvalSectionPEOProfileTypeId | PROFILE_TYPE_ID | — | — |
| 22 | EvalSectionPEORateItemFlag | RATE_ITEM_FLAG | — | — |
| 23 | EvalSectionPEORateSectionFlag | RATE_SECTION_FLAG | — | — |
| 24 | EvalSectionPEORatingOverideFlag | RATING_OVERIDE_FLAG | — | — |
| 25 | EvalSectionPEORatingTypeCode | RATING_TYPE_CODE | — | — |
| 26 | EvalSectionPEOSectionMinWeight | SECTION_MIN_WEIGHT | — | — |
| 27 | EvalSectionPEOSectionMinWeightFlag | SECTION_MIN_WEIGHT_FLAG | — | — |
| 28 | EvalSectionPEOSectionRatingModelId | SECTION_RATING_MODEL_ID | — | — |
| 29 | EvalSectionPEOSectionTypeCode | SECTION_TYPE_CODE | — | — |
| 30 | EvalSectionPEOSectionWeight | SECTION_WEIGHT | — | — |
| 31 | EvalSectionPEOSectionWeightFlag | SECTION_WEIGHT_FLAG | — | — |
| 32 | EvalSectionPEOSequenceNumber | SEQUENCE_NUMBER | — | — |
| 33 | EvalSectionPEOShowCritical | SHOW_CRITICAL | — | — |
| 34 | EvalSectionPEOShowDescription | SHOW_DESCRIPTION | — | — |
| 35 | EvalSectionPEOShowDueDate | SHOW_DUE_DATE | — | — |
| 36 | EvalSectionPEOShowMandatory | SHOW_MANDATORY | — | — |
| 37 | EvalSectionPEOShowMeasurement | SHOW_MEASUREMENT | — | — |
| 38 | EvalSectionPEOShowOwnedBy | SHOW_OWNED_BY | — | — |
| 39 | EvalSectionPEOShowPercentComplete | SHOW_PERCENT_COMPLETE | — | — |
| 40 | EvalSectionPEOShowReminderDate | SHOW_REMINDER_DATE | — | — |
| 41 | EvalSectionPEOShowStatus | SHOW_STATUS | — | — |
| 42 | EvalSectionPEOShowTargetPerfRtg | SHOW_TARGET_PERF_RTG | — | — |
| 43 | EvalSectionPEOShowTargetProfLevel | SHOW_TARGET_PROF_LEVEL | — | — |
| 44 | EvalSectionPEOTmplSectionId | TMPL_SECTION_ID | — | — |
| 45 | EvalSectionPEOUseProfileFlag | USE_PROFILE_FLAG | — | — |
| 46 | EvalSectionPEOUseSecrtgForPerfrtgFlag | USE_SECRTG_FOR_PERFRTG_FLAG | — | — |
| 47 | EvalSectionPEOUseSpecContentItemFlag | USE_SPEC_CONTENT_ITEM_FLAG | — | — |
| 48 | EvalSectionPEOUseSpecProfileFlag | USE_SPEC_PROFILE_FLAG | — | — |
| 49 | EvalSectionPEOUseWorkerGoalsFlag | USE_WORKER_GOALS_FLAG | — | — |
| 50 | EvalSectionPEOWeightSectionFlag | WEIGHT_SECTION_FLAG | — | — |
| 51 | ReferenceSectionId | REFERENCE_SECTION_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
