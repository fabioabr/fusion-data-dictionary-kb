---
id: DOC-OTHER-PVO-CareerDevVersionPVO
doc_type: system-doc
title: "CareerDevVersionPVO — PVO Cross-Module"
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
  - CareerDevVersionPVO
  - careerdevversionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CareerDevVersionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Career Dev Version. Acessa as tabelas: HRG_GOALS, HRG_GOAL_MEASUREMENTS, HRG_GOAL_PLANS_B (+4).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmGoalCoreAM.CareerDevVersionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 243 | 7 | 2 | 18 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[hrg_goals|HRG_GOALS]] — 63 atributos (1 PKs, 6 BICC)
- [[hrg_goal_measurements|HRG_GOAL_MEASUREMENTS]] — 25 atributos (3 BICC)
- [[hrg_goal_plans_b|HRG_GOAL_PLANS_B]] — 92 atributos (1 BICC)
- [[hrg_goal_plan_goals|HRG_GOAL_PLAN_GOALS]] — 17 atributos (1 PKs, 5 BICC)
- [[hrg_goal_plan_sets_b|HRG_GOAL_PLAN_SETS_B]] — 15 atributos (1 BICC)
- [[hrg_goal_plan_set_plans|HRG_GOAL_PLAN_SET_PLANS]] — 11 atributos (1 BICC)
- [[hrg_goal_pln_assignments|HRG_GOAL_PLN_ASSIGNMENTS]] — 20 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hrg_goals|HRG_GOALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalId | GOAL_ID | 🔑 | ✅ |
| 2 | GoalPEOAccessToHierarchyFlag | ACCESS_TO_HIERARCHY_FLAG | — | — |
| 3 | GoalPEOActiveFlag | ACTIVE_FLAG | — | — |
| 4 | GoalPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
| 5 | GoalPEOActualValue | ACTUAL_VALUE | — | — |
| 6 | GoalPEOAllowKeyAttrUpdateFlag | ALLOW_KEY_ATTR_UPDATE_FLAG | — | — |
| 7 | GoalPEOApprovalStatusCode | APPROVAL_STATUS_CODE | — | — |
| 8 | GoalPEOApproverResponseCode | APPROVER_RESPONSE_CODE | — | — |
| 9 | GoalPEOAssignedByPersonId | ASSIGNED_BY_PERSON_ID | — | — |
| 10 | GoalPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 11 | GoalPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 12 | GoalPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 13 | GoalPEOCategoryCode | CATEGORY_CODE | — | — |
| 14 | GoalPEOComments | COMMENTS | — | — |
| 15 | GoalPEOCommentsText | COMMENTS_TEXT | — | — |
| 16 | GoalPEOCreatedBy | CREATED_BY | — | — |
| 17 | GoalPEOCreationDate | CREATION_DATE | — | — |
| 18 | GoalPEODescription | DESCRIPTION | — | — |
| 19 | GoalPEOGoalAccessLevelCode | GOAL_ACCESS_LEVEL_CODE | — | — |
| 20 | GoalPEOGoalApprovalState | GOAL_APPROVAL_STATE | — | — |
| 21 | GoalPEOGoalExtId | GOAL_EXT_ID | — | — |
| 22 | GoalPEOGoalName | GOAL_NAME | — | — |
| 23 | GoalPEOGoalSourceCode | GOAL_SOURCE_CODE | — | — |
| 24 | GoalPEOGoalSubTypeCode | GOAL_SUB_TYPE_CODE | — | — |
| 25 | GoalPEOGoalTypeCode | GOAL_TYPE_CODE | — | ✅ |
| 26 | GoalPEOGoalUrl | GOAL_URL | — | — |
| 27 | GoalPEOGoalVersionTypeCode | GOAL_VERSION_TYPE_CODE | — | — |
| 28 | GoalPEOHrchyAccessGrantDate | HRCHY_ACCESS_GRANT_DATE | — | — |
| 29 | GoalPEOIncludeInPerfdocFlag | INCLUDE_IN_PERFDOC_FLAG | — | — |
| 30 | GoalPEOLastModifiedDate | LAST_MODIFIED_DATE | — | — |
| 31 | GoalPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | GoalPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | GoalPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 34 | GoalPEOLevelCode | LEVEL_CODE | — | — |
| 35 | GoalPEOLevelMeaning | LEVEL_MEANING | — | — |
| 36 | GoalPEOLongDescription | LONG_DESCRIPTION | — | — |
| 37 | GoalPEOMassRequestId | MASS_REQUEST_ID | — | — |
| 38 | GoalPEOMeasureCalcRuleCode | MEASURE_CALC_RULE_CODE | — | — |
| 39 | GoalPEOMeasureComments | MEASURE_COMMENTS | — | — |
| 40 | GoalPEOMeasureName | MEASURE_NAME | — | — |
| 41 | GoalPEOMeasureTypeCode | MEASURE_TYPE_CODE | — | — |
| 42 | GoalPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 43 | GoalPEOOrganizationId | ORGANIZATION_ID | — | — |
| 44 | GoalPEOPercentCompleteCode | PERCENT_COMPLETE_CODE | — | — |
| 45 | GoalPEOPersonId | PERSON_ID | — | ✅ |
| 46 | GoalPEOPreviousStateGoalId | PREVIOUS_STATE_GOAL_ID | — | — |
| 47 | GoalPEOPriorityCode | PRIORITY_CODE | — | — |
| 48 | GoalPEOPrivateFlag | PRIVATE_FLAG | — | — |
| 49 | GoalPEOPublishDate | PUBLISH_DATE | — | — |
| 50 | GoalPEOPublishedFlag | PUBLISHED_FLAG | — | — |
| 51 | GoalPEOReferenceContentItemId | REFERENCE_CONTENT_ITEM_ID | — | — |
| 52 | GoalPEOReferenceGoalId | REFERENCE_GOAL_ID | — | — |
| 53 | GoalPEORequestContext | REQUEST_CONTEXT | — | — |
| 54 | GoalPEORequesterPersonId | REQUESTER_PERSON_ID | — | — |
| 55 | GoalPEOStartDate | START_DATE | — | — |
| 56 | GoalPEOStatusCode | STATUS_CODE | — | ✅ |
| 57 | GoalPEOSuccessCriteria | SUCCESS_CRITERIA | — | — |
| 58 | GoalPEOSuccessCriteriaText | SUCCESS_CRITERIA_TEXT | — | — |
| 59 | GoalPEOTargetCompletionDate | TARGET_COMPLETION_DATE | — | ✅ |
| 60 | GoalPEOTargetType | TARGET_TYPE | — | — |
| 61 | GoalPEOTargetValue | TARGET_VALUE | — | — |
| 62 | GoalPEOUomCode | UOM_CODE | — | — |
| 63 | GoalPEOVersionDate | VERSION_DATE | — | — |

### [[hrg_goal_measurements|HRG_GOAL_MEASUREMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MeasurementPEOAchievedWeight | ACHIEVED_WEIGHT | — | — |
| 2 | MeasurementPEOAchievedWeight_1 | ACHIEVED_WEIGHT | — | — |
| 3 | MeasurementPEOActualValue | ACTUAL_VALUE | — | ✅ |
| 4 | MeasurementPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 5 | MeasurementPEOComments | COMMENTS | — | — |
| 6 | MeasurementPEOCreatedBy | CREATED_BY | — | — |
| 7 | MeasurementPEOCreationDate | CREATION_DATE | — | — |
| 8 | MeasurementPEODisplaySequence | DISPLAY_SEQUENCE | — | — |
| 9 | MeasurementPEOEndDate | END_DATE | — | — |
| 10 | MeasurementPEOGoalId1 | GOAL_ID | — | — |
| 11 | MeasurementPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | MeasurementPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | MeasurementPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | MeasurementPEOMaxTarget | MAX_TARGET | — | — |
| 15 | MeasurementPEOMeasureTypeCode | MEASURE_TYPE_CODE | — | — |
| 16 | MeasurementPEOMeasurementId | MEASUREMENT_ID | — | — |
| 17 | MeasurementPEOMeasurementName | MEASUREMENT_NAME | — | — |
| 18 | MeasurementPEOMinTarget | MIN_TARGET | — | — |
| 19 | MeasurementPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | MeasurementPEOStartDate | START_DATE | — | — |
| 21 | MeasurementPEOTargetPercentage | TARGET_PERCENTAGE | — | — |
| 22 | MeasurementPEOTargetType | TARGET_TYPE | — | — |
| 23 | MeasurementPEOTargetValue | TARGET_VALUE | — | ✅ |
| 24 | MeasurementPEOTargetValue_1 | TARGET_VALUE | — | — |
| 25 | MeasurementPEOUomCode | UOM_CODE | — | — |

### [[hrg_goal_plans_b|HRG_GOAL_PLANS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute1 | ATTRIBUTE1 | — | — |
| 2 | Attribute10 | ATTRIBUTE10 | — | — |
| 3 | Attribute11 | ATTRIBUTE11 | — | — |
| 4 | Attribute12 | ATTRIBUTE12 | — | — |
| 5 | Attribute13 | ATTRIBUTE13 | — | — |
| 6 | Attribute14 | ATTRIBUTE14 | — | — |
| 7 | Attribute15 | ATTRIBUTE15 | — | — |
| 8 | Attribute16 | ATTRIBUTE16 | — | — |
| 9 | Attribute17 | ATTRIBUTE17 | — | — |
| 10 | Attribute18 | ATTRIBUTE18 | — | — |
| 11 | Attribute19 | ATTRIBUTE19 | — | — |
| 12 | Attribute2 | ATTRIBUTE2 | — | — |
| 13 | Attribute20 | ATTRIBUTE20 | — | — |
| 14 | Attribute21 | ATTRIBUTE21 | — | — |
| 15 | Attribute22 | ATTRIBUTE22 | — | — |
| 16 | Attribute23 | ATTRIBUTE23 | — | — |
| 17 | Attribute24 | ATTRIBUTE24 | — | — |
| 18 | Attribute25 | ATTRIBUTE25 | — | — |
| 19 | Attribute26 | ATTRIBUTE26 | — | — |
| 20 | Attribute27 | ATTRIBUTE27 | — | — |
| 21 | Attribute28 | ATTRIBUTE28 | — | — |
| 22 | Attribute29 | ATTRIBUTE29 | — | — |
| 23 | Attribute3 | ATTRIBUTE3 | — | — |
| 24 | Attribute30 | ATTRIBUTE30 | — | — |
| 25 | Attribute4 | ATTRIBUTE4 | — | — |
| 26 | Attribute5 | ATTRIBUTE5 | — | — |
| 27 | Attribute6 | ATTRIBUTE6 | — | — |
| 28 | Attribute7 | ATTRIBUTE7 | — | — |
| 29 | Attribute8 | ATTRIBUTE8 | — | — |
| 30 | Attribute9 | ATTRIBUTE9 | — | — |
| 31 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 32 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 33 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 34 | AttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 35 | AttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 36 | AttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 37 | AttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 38 | AttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 39 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 40 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 41 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 42 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 43 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 44 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 45 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 46 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 47 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 48 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 49 | AttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 50 | AttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 51 | AttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 52 | AttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 53 | AttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 54 | AttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 55 | AttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 56 | AttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 57 | AttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 58 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 59 | AttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 60 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 61 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 62 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 63 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 64 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 65 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 66 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 67 | GoalPlanBPEOAllDepartmentsFlag | ALL_DEPARTMENTS_FLAG | — | — |
| 68 | GoalPlanBPEOAutoAssociateGoalFlag | AUTO_ASSOCIATE_GOAL_FLAG | — | — |
| 69 | GoalPlanBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 70 | GoalPlanBPEOCreatedBy | CREATED_BY | — | — |
| 71 | GoalPlanBPEOCreatedBySystem | CREATED_BY_SYSTEM | — | — |
| 72 | GoalPlanBPEOCreationDate | CREATION_DATE | — | — |
| 73 | GoalPlanBPEOEnableWeightingFlag | ENABLE_WEIGHTING_FLAG | — | — |
| 74 | GoalPlanBPEOEndDate | END_DATE | — | — |
| 75 | GoalPlanBPEOEnforceGoalWeightFlag | ENFORCE_GOAL_WEIGHT_FLAG | — | — |
| 76 | GoalPlanBPEOGoalAccessLevelCode | GOAL_ACCESS_LEVEL_CODE | — | — |
| 77 | GoalPlanBPEOGoalPlanActiveFlag | GOAL_PLAN_ACTIVE_FLAG | — | — |
| 78 | GoalPlanBPEOGoalPlanExtId | GOAL_PLAN_EXT_ID | — | — |
| 79 | GoalPlanBPEOGoalPlanId | GOAL_PLAN_ID | — | — |
| 80 | GoalPlanBPEOGoalPlanTypeCode | GOAL_PLAN_TYPE_CODE | — | — |
| 81 | GoalPlanBPEOGoalSubTypeCode | GOAL_SUB_TYPE_CODE | — | — |
| 82 | GoalPlanBPEOIncludeInPerfdocFlag | INCLUDE_IN_PERFDOC_FLAG | — | — |
| 83 | GoalPlanBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 84 | GoalPlanBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 85 | GoalPlanBPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 86 | GoalPlanBPEOMassRequestId | MASS_REQUEST_ID | — | — |
| 87 | GoalPlanBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 88 | GoalPlanBPEOPreviousGoalPlanId | PREVIOUS_GOAL_PLAN_ID | — | — |
| 89 | GoalPlanBPEOPrimGoalPlanFlag | PRIMARY_GOAL_PLAN_FLAG | — | — |
| 90 | GoalPlanBPEORequestUiContextCode | REQUEST_UI_CONTEXT_CODE | — | — |
| 91 | GoalPlanBPEOReviewPeriodId | REVIEW_PERIOD_ID | — | — |
| 92 | StartDate1 | START_DATE | — | — |

### [[hrg_goal_plan_goals|HRG_GOAL_PLAN_GOALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalPlanGoalId | GOAL_PLAN_GOAL_ID | 🔑 | ✅ |
| 2 | GoalPlanGoalPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | GoalPlanGoalPEOCreatedBy | CREATED_BY | — | — |
| 4 | GoalPlanGoalPEOCreationDate | CREATION_DATE | — | — |
| 5 | GoalPlanGoalPEODisplaySequence | DISPLAY_SEQUENCE | — | — |
| 6 | GoalPlanGoalPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | GoalPlanGoalPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 8 | GoalPlanGoalPEOGoalId | GOAL_ID | — | ✅ |
| 9 | GoalPlanGoalPEOGoalPlanId | GOAL_PLAN_ID | — | ✅ |
| 10 | GoalPlanGoalPEOGoalPlanSetId1 | GOAL_PLAN_SET_ID | — | — |
| 11 | GoalPlanGoalPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | GoalPlanGoalPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | GoalPlanGoalPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | GoalPlanGoalPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | GoalPlanGoalPEOPriorityCode | PRIORITY_CODE | — | — |
| 16 | GoalPlanGoalPEOReviewPeriodId | REVIEW_PERIOD_ID | — | — |
| 17 | GoalPlanGoalPEOWeighting | WEIGHTING | — | — |

### [[hrg_goal_plan_sets_b|HRG_GOAL_PLAN_SETS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalPlanSetBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | GoalPlanSetBPEOCreatedBy | CREATED_BY | — | — |
| 3 | GoalPlanSetBPEOCreationDate | CREATION_DATE | — | — |
| 4 | GoalPlanSetBPEOEndDate | END_DATE | — | — |
| 5 | GoalPlanSetBPEOGoalPlanSetActiveFlag | GOAL_PLAN_SET_ACTIVE_FLAG | — | — |
| 6 | GoalPlanSetBPEOGoalPlanSetExtId | GOAL_PLAN_SET_EXT_ID | — | — |
| 7 | GoalPlanSetBPEOGoalPlanSetId | GOAL_PLAN_SET_ID | — | — |
| 8 | GoalPlanSetBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | GoalPlanSetBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | GoalPlanSetBPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 11 | GoalPlanSetBPEOMassRequestId | MASS_REQUEST_ID | — | — |
| 12 | GoalPlanSetBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | GoalPlanSetBPEORequestUiContextCode | REQUEST_UI_CONTEXT_CODE | — | — |
| 14 | GoalPlanSetBPEOReviewPeriodId | REVIEW_PERIOD_ID | — | — |
| 15 | StartDate | START_DATE | — | — |

### [[hrg_goal_plan_set_plans|HRG_GOAL_PLAN_SET_PLANS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalPlanSetPlanPEOCreatedBy1 | CREATED_BY | — | — |
| 2 | GoalPlanSetPlanPEOCreationDate1 | CREATION_DATE | — | — |
| 3 | GoalPlanSetPlanPEOGoalPlanId | GOAL_PLAN_ID | — | — |
| 4 | GoalPlanSetPlanPEOGoalPlanSetId | GOAL_PLAN_SET_ID | — | — |
| 5 | GoalPlanSetPlanPEOGoalPlanSetPlanId | GOAL_PLAN_SET_PLAN_ID | — | — |
| 6 | GoalPlanSetPlanPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 7 | GoalPlanSetPlanPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 8 | GoalPlanSetPlanPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 9 | GoalPlanSetPlanPEOMassRequestId | MASS_REQUEST_ID | — | — |
| 10 | GoalPlanSetPlanPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 11 | GoalPlanSetPlanPEOWeighting | WEIGHTING | — | — |

### [[hrg_goal_pln_assignments|HRG_GOAL_PLN_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalPlanAssgPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 2 | GoalPlanAssgPEOCreatedBy | CREATED_BY | — | — |
| 3 | GoalPlanAssgPEOCreationDate | CREATION_DATE | — | — |
| 4 | GoalPlanAssgPEOGoalPlanAssignmentId | GOAL_PLAN_ASSIGNMENT_ID | — | — |
| 5 | GoalPlanAssgPEOGoalPlanEndDate | GOAL_PLAN_END_DATE | — | — |
| 6 | GoalPlanAssgPEOGoalPlanId | GOAL_PLAN_ID | — | — |
| 7 | GoalPlanAssgPEOGoalPlanSetEndDate | GOAL_PLAN_SET_END_DATE | — | — |
| 8 | GoalPlanAssgPEOGoalPlanSetId | GOAL_PLAN_SET_ID | — | — |
| 9 | GoalPlanAssgPEOGoalPlanSetStartDate | GOAL_PLAN_SET_START_DATE | — | — |
| 10 | GoalPlanAssgPEOGoalPlanStartDate | GOAL_PLAN_START_DATE | — | — |
| 11 | GoalPlanAssgPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | GoalPlanAssgPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | GoalPlanAssgPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | GoalPlanAssgPEOOrganizationId | ORGANIZATION_ID | — | — |
| 15 | GoalPlanAssgPEOPersonId | PERSON_ID | — | — |
| 16 | GoalPlanAssgPEOStatus | STATUS | — | — |
| 17 | GoalPlanAssgPEOWeighting | WEIGHTING | — | — |
| 18 | GoalPlanAssgnPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 19 | GoalPlanAssgnPEORevPeriodId | REVIEW_PERIOD_ID | — | — |
| 20 | LastUpdatedBy | LAST_UPDATED_BY | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
