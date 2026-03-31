---
id: DOC-HCM-PVO-GoalItemPVO
doc_type: system-doc
title: "GoalItemPVO — PVO Human Capital Management"
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
  - GoalItemPVO
  - goalitempvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GoalItemPVO

## 📌 Visão Geral

Consolida itens de meta em avaliações de desempenho, cruzando metas com seções e medições. Suporta scoring de metas em performance reviews.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceDocsAM.GoalItemPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 126 | 4 | 4 | 51 | 40% |

---

## 🔗 Tabelas Relacionadas

- [[hra_eval_items|HRA_EVAL_ITEMS]] — 31 atributos (2 PKs, 23 BICC)
- [[hra_eval_sections|HRA_EVAL_SECTIONS]] — 46 atributos (1 PKs, 2 BICC)
- [[hrg_goals|HRG_GOALS]] — 39 atributos (1 PKs, 18 BICC)
- [[hrg_goal_measurements|HRG_GOAL_MEASUREMENTS]] — 10 atributos (8 BICC)

---

## ⚙️ Atributos

### [[hra_eval_items|HRA_EVAL_ITEMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | EvalItemId | EVAL_ITEM_ID | 🔑 | ✅ |
| 4 | EvalItemPEOAchievementDate | ACHIEVEMENT_DATE | — | ✅ |
| 5 | EvalItemPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 6 | EvalItemPEOCriticalFlag | CRITICAL_FLAG | — | ✅ |
| 7 | EvalItemPEODescription | DESCRIPTION | — | ✅ |
| 8 | EvalItemPEODueDate | DUE_DATE | — | ✅ |
| 9 | EvalItemPEOEvalSectionId | EVAL_SECTION_ID | — | — |
| 10 | EvalItemPEOEvaluationId | EVALUATION_ID | — | — |
| 11 | EvalItemPEOItemName | ITEM_NAME | — | ✅ |
| 12 | EvalItemPEOMandatoryFlag | MANDATORY_FLAG | — | ✅ |
| 13 | EvalItemPEOMeasurement | MEASUREMENT | — | ✅ |
| 14 | EvalItemPEOMinWeight | MIN_WEIGHT | — | ✅ |
| 15 | EvalItemPEOOwnedBy | OWNED_BY | — | ✅ |
| 16 | EvalItemPEOParentItemId | PARENT_ITEM_ID | — | — |
| 17 | EvalItemPEOPercentCompleted | PERCENT_COMPLETED | — | ✅ |
| 18 | EvalItemPEOPerfRatingModelId | PERF_RATING_MODEL_ID | — | ✅ |
| 19 | EvalItemPEOProfRatingModelId | PROF_RATING_MODEL_ID | — | ✅ |
| 20 | EvalItemPEORatingOverideFlag | RATING_OVERIDE_FLAG | — | ✅ |
| 21 | EvalItemPEOReminderDate | REMINDER_DATE | — | ✅ |
| 22 | EvalItemPEOStartDate | START_DATE | — | ✅ |
| 23 | EvalItemPEOTargetDate | TARGET_DATE | — | ✅ |
| 24 | EvalItemPEOTargetPerfRevRatingId | TARGET_PERF_REV_RATING_ID | — | ✅ |
| 25 | EvalItemPEOTargetProfRevRatingId | TARGET_PROF_REV_RATING_ID | — | ✅ |
| 26 | EvalItemPEOWeight | WEIGHT | — | ✅ |
| 27 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 29 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 30 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 31 | ReferenceItemId | REFERENCE_ITEM_ID | 🔑 | ✅ |

### [[hra_eval_sections|HRA_EVAL_SECTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EvalSectionId | EVAL_SECTION_ID | 🔑 | ✅ |
| 2 | EvalSectionPEOAddItemsConfirmCritFlag | ADD_ITEMS_CONFIRM_CRIT_FLAG | — | — |
| 3 | EvalSectionPEOBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
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

### [[hrg_goals|HRG_GOALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalId | GOAL_ID | 🔑 | ✅ |
| 2 | GoalPEOAccessToHierarchyFlag | ACCESS_TO_HIERARCHY_FLAG | — | — |
| 3 | GoalPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 4 | GoalPEOAllowKeyAttrUpdateFlag | ALLOW_KEY_ATTR_UPDATE_FLAG | — | — |
| 5 | GoalPEOApprovalStatusCode | APPROVAL_STATUS_CODE | — | — |
| 6 | GoalPEOAssignedByPersonId | ASSIGNED_BY_PERSON_ID | — | — |
| 7 | GoalPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 8 | GoalPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 9 | GoalPEOCategoryCode | CATEGORY_CODE | — | ✅ |
| 10 | GoalPEOComments | COMMENTS | — | — |
| 11 | GoalPEOCommentsText | COMMENTS_TEXT | — | ✅ |
| 12 | GoalPEODescription | DESCRIPTION | — | ✅ |
| 13 | GoalPEOGoalName | GOAL_NAME | — | ✅ |
| 14 | GoalPEOGoalSourceCode | GOAL_SOURCE_CODE | — | ✅ |
| 15 | GoalPEOGoalTypeCode | GOAL_TYPE_CODE | — | ✅ |
| 16 | GoalPEOGoalUrl | GOAL_URL | — | ✅ |
| 17 | GoalPEOGoalVersionTypeCode | GOAL_VERSION_TYPE_CODE | — | — |
| 18 | GoalPEOHrchyAccessGrantDate | HRCHY_ACCESS_GRANT_DATE | — | — |
| 19 | GoalPEOIncludeInPerfdocFlag | INCLUDE_IN_PERFDOC_FLAG | — | — |
| 20 | GoalPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | GoalPEOLevelCode | LEVEL_CODE | — | ✅ |
| 22 | GoalPEOLevelMeaning | LEVEL_MEANING | — | ✅ |
| 23 | GoalPEOMassRequestId | MASS_REQUEST_ID | — | — |
| 24 | GoalPEOOrganizationId | ORGANIZATION_ID | — | — |
| 25 | GoalPEOPercentCompleteCode | PERCENT_COMPLETE_CODE | — | ✅ |
| 26 | GoalPEOPersonId | PERSON_ID | — | — |
| 27 | GoalPEOPriorityCode | PRIORITY_CODE | — | ✅ |
| 28 | GoalPEOPrivateFlag | PRIVATE_FLAG | — | — |
| 29 | GoalPEOPublishDate | PUBLISH_DATE | — | — |
| 30 | GoalPEOPublishedFlag | PUBLISHED_FLAG | — | — |
| 31 | GoalPEOReferenceContentItemId | REFERENCE_CONTENT_ITEM_ID | — | — |
| 32 | GoalPEOReferenceGoalId | REFERENCE_GOAL_ID | — | — |
| 33 | GoalPEORequesterPersonId | REQUESTER_PERSON_ID | — | — |
| 34 | GoalPEOStartDate | START_DATE | — | ✅ |
| 35 | GoalPEOStatusCode | STATUS_CODE | — | ✅ |
| 36 | GoalPEOSuccessCriteria | SUCCESS_CRITERIA | — | — |
| 37 | GoalPEOSuccessCriteriaText | SUCCESS_CRITERIA_TEXT | — | ✅ |
| 38 | GoalPEOTargetCompletionDate | TARGET_COMPLETION_DATE | — | ✅ |
| 39 | GoalPEOVersionDate | VERSION_DATE | — | — |

### [[hrg_goal_measurements|HRG_GOAL_MEASUREMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DisplaySequence | DISPLAY_SEQUENCE | — | — |
| 2 | GoalPEOActualValue | ACTUAL_VALUE | — | ✅ |
| 3 | GoalPEOMeasureComments | COMMENTS | — | ✅ |
| 4 | GoalPEOMeasureName | MEASUREMENT_NAME | — | ✅ |
| 5 | GoalPEOMeasureTypeCode | MEASURE_TYPE_CODE | — | ✅ |
| 6 | GoalPEOTargetType | TARGET_TYPE | — | ✅ |
| 7 | GoalPEOTargetValue | TARGET_VALUE | — | ✅ |
| 8 | GoalPEOUomCode | UOM_CODE | — | ✅ |
| 9 | MeasurementId | MEASUREMENT_ID | — | — |
| 10 | MeasurementPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
