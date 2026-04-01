---
id: DOC-OTHER-PVO-ManagerPerformanceOverallRatingPVO
doc_type: system-doc
title: "ManagerPerformanceOverallRatingPVO — PVO Cross-Module"
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
  - ManagerPerformanceOverallRatingPVO
  - managerperformanceoverallratingpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ManagerPerformanceOverallRatingPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Manager Performance Overall Rating. Acessa as tabelas: HRA_EVALUATIONS, HRA_EVAL_PARTICIPANTS, HRA_EVAL_RATINGS (+3).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceDocsAM.ManagerPerformanceOverallRatingPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 124 | 6 | 4 | 18 | 15% |

---

## 🔗 Tabelas Relacionadas

- [[hra_evaluations|HRA_EVALUATIONS]] — 29 atributos (1 PKs, 11 BICC)
- [[hra_eval_participants|HRA_EVAL_PARTICIPANTS]] — 7 atributos
- [[hra_eval_ratings|HRA_EVAL_RATINGS]] — 13 atributos (1 PKs, 1 BICC)
- [[hra_eval_sections|HRA_EVAL_SECTIONS]] — 45 atributos (1 PKs, 1 BICC)
- [[hra_tmpl_defns_b|HRA_TMPL_DEFNS_B]] — 15 atributos (2 BICC)
- [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]] — 15 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[hra_evaluations|HRA_EVALUATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | EvaluationId | EVALUATION_ID | 🔑 | ✅ |
| 4 | EvaluationPEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 5 | EvaluationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 6 | EvaluationPEOCalculationRatingsFlag | CALCULATION_RATINGS_FLAG | — | — |
| 7 | EvaluationPEODecimalPlaces | DECIMAL_PLACES | — | — |
| 8 | EvaluationPEOEndDate | END_DATE | — | ✅ |
| 9 | EvaluationPEOEvaluationDate | EVALUATION_DATE | — | — |
| 10 | EvaluationPEOLanguageCode | LANGUAGE_CODE | — | — |
| 11 | EvaluationPEOLockedByUserId | LOCKED_BY_USER_ID | — | — |
| 12 | EvaluationPEOManagerComments | MANAGER_COMMENTS | — | — |
| 13 | EvaluationPEOManagerId | MANAGER_ID | — | ✅ |
| 14 | EvaluationPEOMappingMethodCode | MAPPING_METHOD_CODE | — | — |
| 15 | EvaluationPEOMeetingHeldDate | MEETING_HELD_DATE | — | — |
| 16 | EvaluationPEOPrevStatusCode | PREV_STATUS_CODE | — | — |
| 17 | EvaluationPEORoundingRuleCode | ROUNDING_RULE_CODE | — | — |
| 18 | EvaluationPEOSelectManagerAllowedFlag | SELECT_MANAGER_ALLOWED_FLAG | — | — |
| 19 | EvaluationPEOStarRatingEnabledFlag | STAR_RATING_ENABLED_FLAG | — | — |
| 20 | EvaluationPEOStartDate | START_DATE | — | — |
| 21 | EvaluationPEOStatusCode | STATUS_CODE | — | ✅ |
| 22 | EvaluationPEOTemplateDefnId | TEMPLATE_DEFN_ID | — | — |
| 23 | EvaluationPEOTmplPeriodId | TMPL_PERIOD_ID | — | — |
| 24 | EvaluationPEOWorkerComments | WORKER_COMMENTS | — | — |
| 25 | EvaluationPEOWorkerId | WORKER_ID | — | ✅ |
| 26 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 27 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 28 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 29 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[hra_eval_participants|HRA_EVAL_PARTICIPANTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EvalParticipantPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | EvalParticipantPEOEvalParticipantId | EVAL_PARTICIPANT_ID | — | — |
| 3 | EvalParticipantPEOEvalRoleId | EVAL_ROLE_ID | — | — |
| 4 | EvalParticipantPEOEvaluationId | EVALUATION_ID | — | — |
| 5 | EvalParticipantPEOParticipationStatusCode | PARTICIPATION_STATUS_CODE | — | — |
| 6 | EvalParticipantPEOPersonId | PERSON_ID | — | — |
| 7 | EvalParticipantPEORoleTypeCode | ROLE_TYPE_CODE | — | — |

### [[hra_eval_ratings|HRA_EVAL_RATINGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EvalRatingId | EVAL_RATING_ID | 🔑 | ✅ |
| 2 | EvalRatingOverallPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | EvalRatingOverallPEOCalculatedRating | CALCULATED_RATING | — | — |
| 4 | EvalRatingOverallPEOCommentText | COMMENT_TEXT | — | — |
| 5 | EvalRatingOverallPEOComments | COMMENTS | — | — |
| 6 | EvalRatingOverallPEOEvalParticipantId | EVAL_PARTICIPANT_ID | — | — |
| 7 | EvalRatingOverallPEOEvaluationId | EVALUATION_ID | — | — |
| 8 | EvalRatingOverallPEOPerformanceRatingId | PERFORMANCE_RATING_ID | — | — |
| 9 | EvalRatingOverallPEOProficiencyRatingId | PROFICIENCY_RATING_ID | — | — |
| 10 | EvalRatingOverallPEOReferenceId | REFERENCE_ID | — | — |
| 11 | EvalRatingOverallPEOReferenceType | REFERENCE_TYPE | — | — |
| 12 | EvalRatingOverallPEOReviewPoints | REVIEW_POINTS | — | — |
| 13 | EvalRatingOverallPEORoleTypeCode | ROLE_TYPE_CODE | — | — |

### [[hra_eval_sections|HRA_EVAL_SECTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EvalSectionId | EVAL_SECTION_ID | 🔑 | ✅ |
| 2 | EvalSectionPEOAddItemsConfirmCritFlag | ADD_ITEMS_CONFIRM_CRIT_FLAG | — | — |
| 3 | EvalSectionPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | EvalSectionPEOCalculationRuleCode | CALCULATION_RULE_CODE | — | — |
| 5 | EvalSectionPEOCommentText | COMMENT_TEXT | — | — |
| 6 | EvalSectionPEOComments | COMMENTS | — | — |
| 7 | EvalSectionPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 8 | EvalSectionPEOEnableItems | ENABLE_ITEMS | — | — |
| 9 | EvalSectionPEOEvaluationId | EVALUATION_ID | — | — |
| 10 | EvalSectionPEOFastFormulaId | FAST_FORMULA_ID | — | — |
| 11 | EvalSectionPEOFreeFormAllowedFlag | FREE_FORM_ALLOWED_FLAG | — | — |
| 12 | EvalSectionPEOItemCalculationCode | ITEM_CALCULATION_CODE | — | — |
| 13 | EvalSectionPEOPerfRatingModelId | PERF_RATING_MODEL_ID | — | — |
| 14 | EvalSectionPEOProfileId | PROFILE_ID | — | — |
| 15 | EvalSectionPEOProfileTypeId | PROFILE_TYPE_ID | — | — |
| 16 | EvalSectionPEORateItemFlag | RATE_ITEM_FLAG | — | — |
| 17 | EvalSectionPEORateSectionFlag | RATE_SECTION_FLAG | — | — |
| 18 | EvalSectionPEORatingOverideFlag | RATING_OVERIDE_FLAG | — | — |
| 19 | EvalSectionPEORatingTypeCode | RATING_TYPE_CODE | — | — |
| 20 | EvalSectionPEOSectionMinWeight | SECTION_MIN_WEIGHT | — | — |
| 21 | EvalSectionPEOSectionMinWeightFlag | SECTION_MIN_WEIGHT_FLAG | — | — |
| 22 | EvalSectionPEOSectionRatingModelId | SECTION_RATING_MODEL_ID | — | — |
| 23 | EvalSectionPEOSectionTypeCode | SECTION_TYPE_CODE | — | — |
| 24 | EvalSectionPEOSectionWeight | SECTION_WEIGHT | — | — |
| 25 | EvalSectionPEOSectionWeightFlag | SECTION_WEIGHT_FLAG | — | — |
| 26 | EvalSectionPEOSequenceNumber | SEQUENCE_NUMBER | — | — |
| 27 | EvalSectionPEOShowCritical | SHOW_CRITICAL | — | — |
| 28 | EvalSectionPEOShowDescription | SHOW_DESCRIPTION | — | — |
| 29 | EvalSectionPEOShowDueDate | SHOW_DUE_DATE | — | — |
| 30 | EvalSectionPEOShowMandatory | SHOW_MANDATORY | — | — |
| 31 | EvalSectionPEOShowMeasurement | SHOW_MEASUREMENT | — | — |
| 32 | EvalSectionPEOShowOwnedBy | SHOW_OWNED_BY | — | — |
| 33 | EvalSectionPEOShowPercentComplete | SHOW_PERCENT_COMPLETE | — | — |
| 34 | EvalSectionPEOShowReminderDate | SHOW_REMINDER_DATE | — | — |
| 35 | EvalSectionPEOShowStatus | SHOW_STATUS | — | — |
| 36 | EvalSectionPEOShowTargetPerfRtg | SHOW_TARGET_PERF_RTG | — | — |
| 37 | EvalSectionPEOShowTargetProfLevel | SHOW_TARGET_PROF_LEVEL | — | — |
| 38 | EvalSectionPEOTmplSectionId | TMPL_SECTION_ID | — | — |
| 39 | EvalSectionPEOUseProfileFlag | USE_PROFILE_FLAG | — | — |
| 40 | EvalSectionPEOUseSecrtgForPerfrtgFlag | USE_SECRTG_FOR_PERFRTG_FLAG | — | — |
| 41 | EvalSectionPEOUseSpecContentItemFlag | USE_SPEC_CONTENT_ITEM_FLAG | — | — |
| 42 | EvalSectionPEOUseSpecProfileFlag | USE_SPEC_PROFILE_FLAG | — | — |
| 43 | EvalSectionPEOUseWorkerGoalsFlag | USE_WORKER_GOALS_FLAG | — | — |
| 44 | EvalSectionPEOWeightSectionFlag | WEIGHT_SECTION_FLAG | — | — |
| 45 | ReferenceSectionId | REFERENCE_SECTION_ID | — | — |

### [[hra_tmpl_defns_b|HRA_TMPL_DEFNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TemplateDefnBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | TemplateDefnBPEOCalculateRatingsFlag | CALCULATE_RATINGS_FLAG | — | — |
| 3 | TemplateDefnBPEODateFrom | DATE_FROM | — | — |
| 4 | TemplateDefnBPEODateTo | DATE_TO | — | — |
| 5 | TemplateDefnBPEODecimalPlaces | DECIMAL_PLACES | — | — |
| 6 | TemplateDefnBPEODocTypeId | DOC_TYPE_ID | — | ✅ |
| 7 | TemplateDefnBPEOMappingMethodCode | MAPPING_METHOD_CODE | — | — |
| 8 | TemplateDefnBPEOProcessFlowId | PROCESS_FLOW_ID | — | — |
| 9 | TemplateDefnBPEORoundingRuleCode | ROUNDING_RULE_CODE | — | — |
| 10 | TemplateDefnBPEOSelectMgrAllowedFlag | SELECT_MGR_ALLOWED_FLAG | — | — |
| 11 | TemplateDefnBPEOSetId | SET_ID | — | — |
| 12 | TemplateDefnBPEOShowParticipantNames | SHOW_PARTICIPANT_NAMES | — | — |
| 13 | TemplateDefnBPEOStarRatingEnabledFlag | STAR_RATING_ENABLED_FLAG | — | — |
| 14 | TemplateDefnBPEOStatusCode | STATUS_CODE | — | — |
| 15 | TemplateDefnBPEOTemplateDefnId | TEMPLATE_DEFN_ID | — | ✅ |

### [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RatingLevelBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | RatingLevelBPEOCareerStrDev | CAREER_STR_DEV | — | — |
| 3 | RatingLevelBPEODateFrom | DATE_FROM | — | — |
| 4 | RatingLevelBPEODateTo | DATE_TO | — | — |
| 5 | RatingLevelBPEOFromPoints | FROM_POINTS | — | — |
| 6 | RatingLevelBPEOMaxRatingDistribution | MAX_RATING_DISTRIBUTION | — | — |
| 7 | RatingLevelBPEOMinRatingDistribution | MIN_RATING_DISTRIBUTION | — | — |
| 8 | RatingLevelBPEOModuleId | MODULE_ID | — | — |
| 9 | RatingLevelBPEONumericRating | NUMERIC_RATING | — | — |
| 10 | RatingLevelBPEORatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 11 | RatingLevelBPEORatingModelId | RATING_MODEL_ID | — | ✅ |
| 12 | RatingLevelBPEOReviewPoints | REVIEW_POINTS | — | — |
| 13 | RatingLevelBPEOStarRating | STAR_RATING | — | — |
| 14 | RatingLevelBPEOToPoints | TO_POINTS | — | — |
| 15 | RatingLevelId | RATING_LEVEL_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
