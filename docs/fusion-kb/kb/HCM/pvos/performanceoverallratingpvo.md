---
id: DOC-HCM-PVO-PerformanceOverallRatingPVO
doc_type: system-doc
title: "PerformanceOverallRatingPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
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
  - pvo
  - bicc
aliases:
  - PerformanceOverallRatingPVO
  - performanceoverallratingpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PerformanceOverallRatingPVO

## 📌 Visão Geral

Disponibiliza o rating geral (overall) de documentos de avaliação de desempenho por participante e papel. Métrica final consolidada para análise de distribuição de performance organizacional.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceDocsAM.PerformanceOverallRatingPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 141 | 7 | 7 | 21 | 15% |

---

## 🔗 Tabelas Relacionadas

- [[hra_evaluations|HRA_EVALUATIONS]] — 28 atributos (1 PKs, 5 BICC)
- [[hra_eval_participants|HRA_EVAL_PARTICIPANTS]] — 9 atributos (2 BICC)
- [[hra_eval_ratings|HRA_EVAL_RATINGS]] — 14 atributos (1 PKs, 3 BICC)
- [[hra_eval_sections|HRA_EVAL_SECTIONS]] — 46 atributos (1 PKs, 2 BICC)
- [[hra_tmpl_defns_b|HRA_TMPL_DEFNS_B]] — 16 atributos (1 BICC)
- [[hra_tmpl_periods_b|HRA_TMPL_PERIODS_B]] — 12 atributos (2 PKs, 3 BICC)
- [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]] — 16 atributos (2 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[hra_evaluations|HRA_EVALUATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
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
| 22 | EvaluationPEOTmplPeriodId | TMPL_PERIOD_ID | — | — |
| 23 | EvaluationPEOWorkerComments | WORKER_COMMENTS | — | — |
| 24 | EvaluationPEOWorkerId | WORKER_ID | — | ✅ |
| 25 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 27 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 28 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[hra_eval_participants|HRA_EVAL_PARTICIPANTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EvalParticipantPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | EvalParticipantPEOEvalParticipantId | EVAL_PARTICIPANT_ID | — | — |
| 3 | EvalParticipantPEOEvalRoleId | EVAL_ROLE_ID | — | — |
| 4 | EvalParticipantPEOEvaluationId | EVALUATION_ID | — | — |
| 5 | EvalParticipantPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | EvalParticipantPEOParticipationStatusCode | PARTICIPATION_STATUS_CODE | — | — |
| 7 | EvalParticipantPEOPersonId | PERSON_ID | — | — |
| 8 | EvalParticipantPEOQuestionnaireId | QUESTIONNAIRE_ID | — | — |
| 9 | EvalParticipantPEORoleTypeCode | ROLE_TYPE_CODE | — | ✅ |

### [[hra_eval_ratings|HRA_EVAL_RATINGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EvalRatingId | EVAL_RATING_ID | 🔑 | ✅ |
| 2 | EvalRatingOverallPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | EvalRatingOverallPEOCalculatedRating | CALCULATED_RATING | — | ✅ |
| 4 | EvalRatingOverallPEOCommentText | COMMENT_TEXT | — | — |
| 5 | EvalRatingOverallPEOComments | COMMENTS | — | — |
| 6 | EvalRatingOverallPEOEvalParticipantId | EVAL_PARTICIPANT_ID | — | — |
| 7 | EvalRatingOverallPEOEvaluationId | EVALUATION_ID | — | — |
| 8 | EvalRatingOverallPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | EvalRatingOverallPEOPerformanceRatingId | PERFORMANCE_RATING_ID | — | — |
| 10 | EvalRatingOverallPEOProficiencyRatingId | PROFICIENCY_RATING_ID | — | — |
| 11 | EvalRatingOverallPEOReferenceId | REFERENCE_ID | — | — |
| 12 | EvalRatingOverallPEOReferenceType | REFERENCE_TYPE | — | — |
| 13 | EvalRatingOverallPEOReviewPoints | REVIEW_POINTS | — | — |
| 14 | EvalRatingOverallPEORoleTypeCode | ROLE_TYPE_CODE | — | — |

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
| 13 | EvalSectionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | EvalSectionPEOPerfRatingModelId | PERF_RATING_MODEL_ID | — | — |
| 15 | EvalSectionPEOProfileId | PROFILE_ID | — | — |
| 16 | EvalSectionPEOProfileTypeId | PROFILE_TYPE_ID | — | — |
| 17 | EvalSectionPEORateItemFlag | RATE_ITEM_FLAG | — | — |
| 18 | EvalSectionPEORateSectionFlag | RATE_SECTION_FLAG | — | — |
| 19 | EvalSectionPEORatingOverideFlag | RATING_OVERIDE_FLAG | — | — |
| 20 | EvalSectionPEORatingTypeCode | RATING_TYPE_CODE | — | — |
| 21 | EvalSectionPEOSectionMinWeight | SECTION_MIN_WEIGHT | — | — |
| 22 | EvalSectionPEOSectionMinWeightFlag | SECTION_MIN_WEIGHT_FLAG | — | — |
| 23 | EvalSectionPEOSectionRatingModelId | SECTION_RATING_MODEL_ID | — | — |
| 24 | EvalSectionPEOSectionTypeCode | SECTION_TYPE_CODE | — | — |
| 25 | EvalSectionPEOSectionWeight | SECTION_WEIGHT | — | — |
| 26 | EvalSectionPEOSectionWeightFlag | SECTION_WEIGHT_FLAG | — | — |
| 27 | EvalSectionPEOSequenceNumber | SEQUENCE_NUMBER | — | — |
| 28 | EvalSectionPEOShowCritical | SHOW_CRITICAL | — | — |
| 29 | EvalSectionPEOShowDescription | SHOW_DESCRIPTION | — | — |
| 30 | EvalSectionPEOShowDueDate | SHOW_DUE_DATE | — | — |
| 31 | EvalSectionPEOShowMandatory | SHOW_MANDATORY | — | — |
| 32 | EvalSectionPEOShowMeasurement | SHOW_MEASUREMENT | — | — |
| 33 | EvalSectionPEOShowOwnedBy | SHOW_OWNED_BY | — | — |
| 34 | EvalSectionPEOShowPercentComplete | SHOW_PERCENT_COMPLETE | — | — |
| 35 | EvalSectionPEOShowReminderDate | SHOW_REMINDER_DATE | — | — |
| 36 | EvalSectionPEOShowStatus | SHOW_STATUS | — | — |
| 37 | EvalSectionPEOShowTargetPerfRtg | SHOW_TARGET_PERF_RTG | — | — |
| 38 | EvalSectionPEOShowTargetProfLevel | SHOW_TARGET_PROF_LEVEL | — | — |
| 39 | EvalSectionPEOTmplSectionId | TMPL_SECTION_ID | — | — |
| 40 | EvalSectionPEOUseProfileFlag | USE_PROFILE_FLAG | — | — |
| 41 | EvalSectionPEOUseSecrtgForPerfrtgFlag | USE_SECRTG_FOR_PERFRTG_FLAG | — | — |
| 42 | EvalSectionPEOUseSpecContentItemFlag | USE_SPEC_CONTENT_ITEM_FLAG | — | — |
| 43 | EvalSectionPEOUseSpecProfileFlag | USE_SPEC_PROFILE_FLAG | — | — |
| 44 | EvalSectionPEOUseWorkerGoalsFlag | USE_WORKER_GOALS_FLAG | — | — |
| 45 | EvalSectionPEOWeightSectionFlag | WEIGHT_SECTION_FLAG | — | — |
| 46 | ReferenceSectionId | REFERENCE_SECTION_ID | — | — |

### [[hra_tmpl_defns_b|HRA_TMPL_DEFNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TemplateDefnBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | TemplateDefnBPEOCalculateRatingsFlag | CALCULATE_RATINGS_FLAG | — | — |
| 3 | TemplateDefnBPEODateFrom | DATE_FROM | — | — |
| 4 | TemplateDefnBPEODateTo | DATE_TO | — | — |
| 5 | TemplateDefnBPEODecimalPlaces | DECIMAL_PLACES | — | — |
| 6 | TemplateDefnBPEODocTypeId | DOC_TYPE_ID | — | — |
| 7 | TemplateDefnBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | TemplateDefnBPEOMappingMethodCode | MAPPING_METHOD_CODE | — | — |
| 9 | TemplateDefnBPEOProcessFlowId | PROCESS_FLOW_ID | — | — |
| 10 | TemplateDefnBPEORoundingRuleCode | ROUNDING_RULE_CODE | — | — |
| 11 | TemplateDefnBPEOSelectMgrAllowedFlag | SELECT_MGR_ALLOWED_FLAG | — | — |
| 12 | TemplateDefnBPEOSetId | SET_ID | — | — |
| 13 | TemplateDefnBPEOShowParticipantNames | SHOW_PARTICIPANT_NAMES | — | — |
| 14 | TemplateDefnBPEOStarRatingEnabledFlag | STAR_RATING_ENABLED_FLAG | — | — |
| 15 | TemplateDefnBPEOStatusCode | STATUS_CODE | — | — |
| 16 | TemplateDefnBPEOTemplateDefnId | TEMPLATE_DEFN_ID | — | — |

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

### [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RatingLevelBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | RatingLevelBPEOCareerStrDev | CAREER_STR_DEV | — | — |
| 3 | RatingLevelBPEODateFrom | DATE_FROM | — | — |
| 4 | RatingLevelBPEODateTo | DATE_TO | — | — |
| 5 | RatingLevelBPEOFromPoints | FROM_POINTS | — | — |
| 6 | RatingLevelBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RatingLevelBPEOMaxRatingDistribution | MAX_RATING_DISTRIBUTION | — | — |
| 8 | RatingLevelBPEOMinRatingDistribution | MIN_RATING_DISTRIBUTION | — | — |
| 9 | RatingLevelBPEOModuleId | MODULE_ID | — | — |
| 10 | RatingLevelBPEONumericRating | NUMERIC_RATING | — | ✅ |
| 11 | RatingLevelBPEORatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 12 | RatingLevelBPEORatingModelId | RATING_MODEL_ID | — | — |
| 13 | RatingLevelBPEOReviewPoints | REVIEW_POINTS | — | — |
| 14 | RatingLevelBPEOStarRating | STAR_RATING | — | — |
| 15 | RatingLevelBPEOToPoints | TO_POINTS | — | — |
| 16 | RatingLevelId | RATING_LEVEL_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
