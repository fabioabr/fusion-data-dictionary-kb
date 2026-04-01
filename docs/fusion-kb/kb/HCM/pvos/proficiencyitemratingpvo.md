---
id: DOC-HCM-PVO-ProficiencyItemRatingPVO
doc_type: system-doc
title: "ProficiencyItemRatingPVO — PVO Human Capital Management"
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
  - ProficiencyItemRatingPVO
  - proficiencyitemratingpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProficiencyItemRatingPVO

## 📌 Visão Geral

Extrai avaliações de proficiência por item, incluindo notas, participantes e seções de avaliação. Fundamental para análise de desempenho individual e calibração.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceDocsAM.ProficiencyItemRatingPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 127 | 8 | 6 | 18 | 14% |

---

## 🔗 Tabelas Relacionadas

- [[hra_evaluations|HRA_EVALUATIONS]] — 28 atributos (1 PKs, 3 BICC)
- [[hra_eval_items|HRA_EVAL_ITEMS]] — 26 atributos (2 PKs, 3 BICC)
- [[hra_eval_participants|HRA_EVAL_PARTICIPANTS]] — 9 atributos (2 BICC)
- [[hra_eval_ratings|HRA_EVAL_RATINGS]] — 14 atributos (1 PKs, 2 BICC)
- [[hra_eval_sections|HRA_EVAL_SECTIONS]] — 6 atributos (1 BICC)
- [[hra_tmpl_defns_b|HRA_TMPL_DEFNS_B]] — 16 atributos (1 BICC)
- [[hra_tmpl_periods_b|HRA_TMPL_PERIODS_B]] — 12 atributos (2 PKs, 3 BICC)
- [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]] — 16 atributos (3 BICC)

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
| 22 | EvaluationPEOTmplPeriodId | TMPL_PERIOD_ID | — | — |
| 23 | EvaluationPEOWorkerComments | WORKER_COMMENTS | — | — |
| 24 | EvaluationPEOWorkerId | WORKER_ID | — | — |
| 25 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 27 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 28 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[hra_eval_items|HRA_EVAL_ITEMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EvalItemId | EVAL_ITEM_ID | 🔑 | ✅ |
| 2 | EvalItemPEOAchievementDate | ACHIEVEMENT_DATE | — | — |
| 3 | EvalItemPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | EvalItemPEOCriticalFlag | CRITICAL_FLAG | — | — |
| 5 | EvalItemPEODescription | DESCRIPTION | — | — |
| 6 | EvalItemPEODueDate | DUE_DATE | — | — |
| 7 | EvalItemPEOEvalSectionId | EVAL_SECTION_ID | — | — |
| 8 | EvalItemPEOEvaluationId | EVALUATION_ID | — | — |
| 9 | EvalItemPEOItemName | ITEM_NAME | — | — |
| 10 | EvalItemPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | EvalItemPEOMandatoryFlag | MANDATORY_FLAG | — | — |
| 12 | EvalItemPEOMeasurement | MEASUREMENT | — | — |
| 13 | EvalItemPEOMinWeight | MIN_WEIGHT | — | — |
| 14 | EvalItemPEOOwnedBy | OWNED_BY | — | — |
| 15 | EvalItemPEOParentItemId | PARENT_ITEM_ID | — | — |
| 16 | EvalItemPEOPercentCompleted | PERCENT_COMPLETED | — | — |
| 17 | EvalItemPEOPerfRatingModelId | PERF_RATING_MODEL_ID | — | — |
| 18 | EvalItemPEOProfRatingModelId | PROF_RATING_MODEL_ID | — | — |
| 19 | EvalItemPEORatingOverideFlag | RATING_OVERIDE_FLAG | — | — |
| 20 | EvalItemPEOReminderDate | REMINDER_DATE | — | — |
| 21 | EvalItemPEOStartDate | START_DATE | — | — |
| 22 | EvalItemPEOTargetDate | TARGET_DATE | — | — |
| 23 | EvalItemPEOTargetPerfRevRatingId | TARGET_PERF_REV_RATING_ID | — | — |
| 24 | EvalItemPEOTargetProfRevRatingId | TARGET_PROF_REV_RATING_ID | — | — |
| 25 | EvalItemPEOWeight | WEIGHT | — | — |
| 26 | ReferenceItemId | REFERENCE_ITEM_ID | 🔑 | ✅ |

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
| 2 | EvalRatingProficiencyPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | EvalRatingProficiencyPEOCalculatedRating | CALCULATED_RATING | — | — |
| 4 | EvalRatingProficiencyPEOCommentText | COMMENT_TEXT | — | — |
| 5 | EvalRatingProficiencyPEOComments | COMMENTS | — | — |
| 6 | EvalRatingProficiencyPEOEvalParticipantId | EVAL_PARTICIPANT_ID | — | — |
| 7 | EvalRatingProficiencyPEOEvaluationId | EVALUATION_ID | — | — |
| 8 | EvalRatingProficiencyPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | EvalRatingProficiencyPEOPerformanceRatingId | PERFORMANCE_RATING_ID | — | — |
| 10 | EvalRatingProficiencyPEOProficiencyRatingId | PROFICIENCY_RATING_ID | — | — |
| 11 | EvalRatingProficiencyPEOReferenceId | REFERENCE_ID | — | — |
| 12 | EvalRatingProficiencyPEOReferenceType | REFERENCE_TYPE | — | — |
| 13 | EvalRatingProficiencyPEOReviewPoints | REVIEW_POINTS | — | — |
| 14 | EvalRatingProficiencyPEORoleTypeCode | ROLE_TYPE_CODE | — | — |

### [[hra_eval_sections|HRA_EVAL_SECTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EvalSectionId | EVAL_SECTION_ID | — | — |
| 2 | EvalSectionPEOCommentText | COMMENT_TEXT | — | — |
| 3 | EvalSectionPEOComments | COMMENTS | — | — |
| 4 | EvalSectionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | EvalSectionPEOSectionTypeCode | SECTION_TYPE_CODE | — | — |
| 6 | ReferenceSectionId | REFERENCE_SECTION_ID | — | — |

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
| 1 | RatingLevelBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
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
| 12 | RatingLevelBPEORatingLevelId | RATING_LEVEL_ID | — | — |
| 13 | RatingLevelBPEORatingModelId | RATING_MODEL_ID | — | — |
| 14 | RatingLevelBPEOReviewPoints | REVIEW_POINTS | — | — |
| 15 | RatingLevelBPEOStarRating | STAR_RATING | — | — |
| 16 | RatingLevelBPEOToPoints | TO_POINTS | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
