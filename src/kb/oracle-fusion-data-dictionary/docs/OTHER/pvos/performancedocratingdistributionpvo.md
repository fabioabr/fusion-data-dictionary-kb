---
id: DOC-OTHER-PVO-PerformanceDocRatingDistributionPVO
doc_type: system-doc
title: "PerformanceDocRatingDistributionPVO — PVO Cross-Module"
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
  - PerformanceDocRatingDistributionPVO
  - performancedocratingdistributionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PerformanceDocRatingDistributionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Performance Doc Rating Distribution. Acessa as tabelas: HRA_EVALUATIONS, HRA_EVAL_PARTICIPANTS, HRA_EVAL_RATINGS (+5).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceDocsAM.PerformanceDocRatingDistributionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 125 | 8 | 5 | 13 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[hra_evaluations|HRA_EVALUATIONS]] — 28 atributos (1 PKs, 4 BICC)
- [[hra_eval_participants|HRA_EVAL_PARTICIPANTS]] — 2 atributos
- [[hra_eval_ratings|HRA_EVAL_RATINGS]] — 13 atributos (1 PKs, 1 BICC)
- [[hra_eval_sections|HRA_EVAL_SECTIONS]] — 45 atributos (1 PKs, 1 BICC)
- [[hra_tmpl_periods_b|HRA_TMPL_PERIODS_B]] — 12 atributos (2 PKs, 3 BICC)
- [[hrt_obj_rating_dist_b|HRT_OBJ_RATING_DIST_B]] — 6 atributos
- [[hrt_rating_distributions|HRT_RATING_DISTRIBUTIONS]] — 4 atributos (2 BICC)
- [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]] — 15 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hra_evaluations|HRA_EVALUATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | EvaluationId | EVALUATION_ID | 🔑 | ✅ |
| 4 | EvaluationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 5 | EvaluationPEOCalculationRatingsFlag | CALCULATION_RATINGS_FLAG | — | — |
| 6 | EvaluationPEODecimalPlaces | DECIMAL_PLACES | — | — |
| 7 | EvaluationPEOEndDate | END_DATE | — | — |
| 8 | EvaluationPEOEvaluationDate | EVALUATION_DATE | — | — |
| 9 | EvaluationPEOLanguageCode | LANGUAGE_CODE | — | — |
| 10 | EvaluationPEOLockedByUserId | LOCKED_BY_USER_ID | — | — |
| 11 | EvaluationPEOManagerComments | MANAGER_COMMENTS | — | — |
| 12 | EvaluationPEOManagerId | MANAGER_ID | — | — |
| 13 | EvaluationPEOMappingMethodCode | MAPPING_METHOD_CODE | — | — |
| 14 | EvaluationPEOMeetingHeldDate | MEETING_HELD_DATE | — | — |
| 15 | EvaluationPEOPrevStatusCode | PREV_STATUS_CODE | — | — |
| 16 | EvaluationPEORoundingRuleCode | ROUNDING_RULE_CODE | — | — |
| 17 | EvaluationPEOSelectManagerAllowedFlag | SELECT_MANAGER_ALLOWED_FLAG | — | — |
| 18 | EvaluationPEOStarRatingEnabledFlag | STAR_RATING_ENABLED_FLAG | — | — |
| 19 | EvaluationPEOStartDate | START_DATE | — | — |
| 20 | EvaluationPEOStatusCode | STATUS_CODE | — | ✅ |
| 21 | EvaluationPEOTemplateDefnId | TEMPLATE_DEFN_ID | — | — |
| 22 | EvaluationPEOTmplPeriodId | TMPL_PERIOD_ID | — | ✅ |
| 23 | EvaluationPEOWorkerComments | WORKER_COMMENTS | — | — |
| 24 | EvaluationPEOWorkerId | WORKER_ID | — | — |
| 25 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 27 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 28 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[hra_eval_participants|HRA_EVAL_PARTICIPANTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EvalParticipantPEOEvalParticipantId | EVAL_PARTICIPANT_ID | — | — |
| 2 | EvalParticipantPEORoleTypeCode | ROLE_TYPE_CODE | — | — |

### [[hra_eval_ratings|HRA_EVAL_RATINGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EvalRatingId | EVAL_RATING_ID | 🔑 | ✅ |
| 2 | EvalRatingPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | EvalRatingPEOCalculatedRating | CALCULATED_RATING | — | — |
| 4 | EvalRatingPEOCommentText | COMMENT_TEXT | — | — |
| 5 | EvalRatingPEOComments | COMMENTS | — | — |
| 6 | EvalRatingPEOEvalParticipantId | EVAL_PARTICIPANT_ID | — | — |
| 7 | EvalRatingPEOEvaluationId | EVALUATION_ID | — | — |
| 8 | EvalRatingPEOPerformanceRatingId | PERFORMANCE_RATING_ID | — | — |
| 9 | EvalRatingPEOProficiencyRatingId | PROFICIENCY_RATING_ID | — | — |
| 10 | EvalRatingPEOReferenceId | REFERENCE_ID | — | — |
| 11 | EvalRatingPEOReferenceType | REFERENCE_TYPE | — | — |
| 12 | EvalRatingPEOReviewPoints | REVIEW_POINTS | — | — |
| 13 | EvalRatingPEORoleTypeCode | ROLE_TYPE_CODE | — | — |

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

### [[hra_tmpl_periods_b|HRA_TMPL_PERIODS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TemplatePeriodBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | TemplatePeriodBPEOCreatedBy | CREATED_BY | — | — |
| 3 | TemplatePeriodBPEOCreationDate | CREATION_DATE | — | — |
| 4 | TemplatePeriodBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | TemplatePeriodBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | TemplatePeriodBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | TemplatePeriodBPEONominalFromDate | NOMINAL_FROM_DATE | — | — |
| 8 | TemplatePeriodBPEONominalToDate | NOMINAL_TO_DATE | — | — |
| 9 | TemplatePeriodBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | TemplatePeriodBPEOReviewPeriodId | REVIEW_PERIOD_ID | — | — |
| 11 | TemplatePeriodBPEOTemplateDefnId | TEMPLATE_DEFN_ID | — | — |
| 12 | TemplatePeriodBPEOTmplPeriodId | TMPL_PERIOD_ID | 🔑 | ✅ |

### [[hrt_obj_rating_dist_b|HRT_OBJ_RATING_DIST_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectRatingDistributionBPEODateFrom | DATE_FROM | — | — |
| 2 | ObjectRatingDistributionBPEODateTo | DATE_TO | — | — |
| 3 | ObjectRatingDistributionBPEOObjRatingDistId | OBJ_RATING_DIST_ID | — | — |
| 4 | ObjectRatingDistributionBPEOObjectId | OBJECT_ID | — | — |
| 5 | ObjectRatingDistributionBPEOObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 6 | ObjectRatingDistributionBPEORatingModelId | RATING_MODEL_ID | — | — |

### [[hrt_rating_distributions|HRT_RATING_DISTRIBUTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RatingDistributionPEODistributionPct | DISTRIBUTION_PCT | — | ✅ |
| 2 | RatingDistributionPEOObjRatingDistId | OBJ_RATING_DIST_ID | — | — |
| 3 | RatingDistributionPEORatingDistributionId | RATING_DISTRIBUTION_ID | — | — |
| 4 | RatingDistributionPEORatingLevelId | RATING_LEVEL_ID | — | ✅ |

### [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RatingLevelBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | RatingLevelBPEOCareerStrDev | CAREER_STR_DEV | — | — |
| 3 | RatingLevelBPEODateFrom | DATE_FROM | — | — |
| 4 | RatingLevelBPEODateTo | DATE_TO | — | — |
| 5 | RatingLevelBPEOFromPoints | FROM_POINTS | — | — |
| 6 | RatingLevelBPEOMaxRatingDistribution | MAX_RATING_DISTRIBUTION | — | ✅ |
| 7 | RatingLevelBPEOMinRatingDistribution | MIN_RATING_DISTRIBUTION | — | ✅ |
| 8 | RatingLevelBPEOModuleId | MODULE_ID | — | — |
| 9 | RatingLevelBPEONumericRating | NUMERIC_RATING | — | — |
| 10 | RatingLevelBPEORatingLevelCode | RATING_LEVEL_CODE | — | — |
| 11 | RatingLevelBPEORatingLevelId | RATING_LEVEL_ID | — | — |
| 12 | RatingLevelBPEORatingModelId | RATING_MODEL_ID | — | — |
| 13 | RatingLevelBPEOReviewPoints | REVIEW_POINTS | — | — |
| 14 | RatingLevelBPEOStarRating | STAR_RATING | — | — |
| 15 | RatingLevelBPEOToPoints | TO_POINTS | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
