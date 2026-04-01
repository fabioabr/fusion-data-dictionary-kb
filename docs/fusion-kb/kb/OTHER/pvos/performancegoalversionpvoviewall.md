---
id: DOC-OTHER-PVO-PerformanceGoalVersionPVOViewAll
doc_type: system-doc
title: "PerformanceGoalVersionPVOViewAll — PVO Cross-Module"
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
  - PerformanceGoalVersionPVOViewAll
  - performancegoalversionpvoviewall
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PerformanceGoalVersionPVOViewAll

## 📌 Visão Geral

View Object para extração BICC de dados de Performance Goal Version View All. Acessa as tabelas: HRD_GOAL_INTENTS, HRD_PERSONAL_INTENTS, HRG_GOALS (+5).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmGoalCoreAM.PerformanceGoalVersionPVOViewAll`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 197 | 8 | 1 | 73 | 37% |

---

## 🔗 Tabelas Relacionadas

- [[hrd_goal_intents|HRD_GOAL_INTENTS]] — 12 atributos (1 BICC)
- [[hrd_personal_intents|HRD_PERSONAL_INTENTS]] — 11 atributos (1 BICC)
- [[hrg_goals|HRG_GOALS]] — 65 atributos (1 PKs, 41 BICC)
- [[hrg_goal_alignments|HRG_GOAL_ALIGNMENTS]] — 4 atributos (1 BICC)
- [[hrg_goal_measurements|HRG_GOAL_MEASUREMENTS]] — 27 atributos (15 BICC)
- [[hrg_goal_plan_goals|HRG_GOAL_PLAN_GOALS]] — 9 atributos (3 BICC)
- [[hrt_profiles_tl|HRT_PROFILES_TL]] — 12 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 57 atributos (10 BICC)

---

## ⚙️ Atributos

### [[hrd_goal_intents|HRD_GOAL_INTENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | GoalId1 | GOAL_ID | — | — |
| 5 | GoalIntentId | GOAL_INTENT_ID | — | — |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | PersonId | PERSON_ID | — | — |
| 11 | ReferenceItemId | REFERENCE_ITEM_ID | — | — |
| 12 | ReferenceType | REFERENCE_TYPE | — | — |

### [[hrd_personal_intents|HRD_PERSONAL_INTENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | CreatedBy1 | CREATED_BY | — | — |
| 3 | CreationDate1 | CREATION_DATE | — | — |
| 4 | IntentName | INTENT_NAME | — | — |
| 5 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 8 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 9 | PersonId1 | PERSON_ID | — | — |
| 10 | PersonalIntentId | PERSONAL_INTENT_ID | — | — |
| 11 | PrivacyFlag | PRIVACY_FLAG | — | — |

### [[hrg_goals|HRG_GOALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalId | GOAL_ID | 🔑 | ✅ |
| 2 | GoalPEOAccessToHierarchyFlag | ACCESS_TO_HIERARCHY_FLAG | — | ✅ |
| 3 | GoalPEOActiveFlag | ACTIVE_FLAG | — | — |
| 4 | GoalPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 5 | GoalPEOActualValue | ACTUAL_VALUE | — | — |
| 6 | GoalPEOAllowDelGoalFlag | ALLOW_DEL_GOAL_FLAG | — | — |
| 7 | GoalPEOAllowKeyAttrUpdateFlag | ALLOW_KEY_ATTR_UPDATE_FLAG | — | ✅ |
| 8 | GoalPEOApprovalStatusCode | APPROVAL_STATUS_CODE | — | — |
| 9 | GoalPEOApproverResponseCode | APPROVER_RESPONSE_CODE | — | ✅ |
| 10 | GoalPEOAssignedByPersonId | ASSIGNED_BY_PERSON_ID | — | ✅ |
| 11 | GoalPEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 12 | GoalPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 13 | GoalPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 14 | GoalPEOCategoryCode | CATEGORY_CODE | — | ✅ |
| 15 | GoalPEOComments | COMMENTS | — | — |
| 16 | GoalPEOCommentsText | COMMENTS_TEXT | — | ✅ |
| 17 | GoalPEOCreatedBy | CREATED_BY | — | ✅ |
| 18 | GoalPEOCreationDate | CREATION_DATE | — | ✅ |
| 19 | GoalPEODescription | DESCRIPTION | — | ✅ |
| 20 | GoalPEOGoalAccessLevelCode | GOAL_ACCESS_LEVEL_CODE | — | ✅ |
| 21 | GoalPEOGoalApprovalState | GOAL_APPROVAL_STATE | — | ✅ |
| 22 | GoalPEOGoalExtId | GOAL_EXT_ID | — | ✅ |
| 23 | GoalPEOGoalName | GOAL_NAME | — | ✅ |
| 24 | GoalPEOGoalSourceCode | GOAL_SOURCE_CODE | — | ✅ |
| 25 | GoalPEOGoalSubTypeCode | GOAL_SUB_TYPE_CODE | — | ✅ |
| 26 | GoalPEOGoalTypeCode | GOAL_TYPE_CODE | — | — |
| 27 | GoalPEOGoalUrl | GOAL_URL | — | ✅ |
| 28 | GoalPEOGoalVersionTypeCode | GOAL_VERSION_TYPE_CODE | — | ✅ |
| 29 | GoalPEOHrchyAccessGrantDate | HRCHY_ACCESS_GRANT_DATE | — | ✅ |
| 30 | GoalPEOIncludeInPerfdocFlag | INCLUDE_IN_PERFDOC_FLAG | — | — |
| 31 | GoalPEOLastModifiedBy | LAST_MODIFIED_BY | — | ✅ |
| 32 | GoalPEOLastModifiedDate | LAST_MODIFIED_DATE | — | ✅ |
| 33 | GoalPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | GoalPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 35 | GoalPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 36 | GoalPEOLevelCode | LEVEL_CODE | — | ✅ |
| 37 | GoalPEOLevelMeaning | LEVEL_MEANING | — | ✅ |
| 38 | GoalPEOLongDescription | LONG_DESCRIPTION | — | — |
| 39 | GoalPEOMassRequestId | MASS_REQUEST_ID | — | — |
| 40 | GoalPEOMeasureCalcRuleCode | MEASURE_CALC_RULE_CODE | — | ✅ |
| 41 | GoalPEOMeasureComments | MEASURE_COMMENTS | — | — |
| 42 | GoalPEOMeasureName | MEASURE_NAME | — | — |
| 43 | GoalPEOMeasureTypeCode | MEASURE_TYPE_CODE | — | — |
| 44 | GoalPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 45 | GoalPEOPercentCompleteCode | PERCENT_COMPLETE_CODE | — | ✅ |
| 46 | GoalPEOPersonId | PERSON_ID | — | ✅ |
| 47 | GoalPEOPreviousStateGoalId | PREVIOUS_STATE_GOAL_ID | — | — |
| 48 | GoalPEOPriorityCode | PRIORITY_CODE | — | ✅ |
| 49 | GoalPEOPrivateFlag | PRIVATE_FLAG | — | — |
| 50 | GoalPEOPublishDate | PUBLISH_DATE | — | — |
| 51 | GoalPEOPublishedFlag | PUBLISHED_FLAG | — | — |
| 52 | GoalPEOReferenceContentItemId | REFERENCE_CONTENT_ITEM_ID | — | ✅ |
| 53 | GoalPEOReferenceGoalId | REFERENCE_GOAL_ID | — | ✅ |
| 54 | GoalPEORequestContext | REQUEST_CONTEXT | — | — |
| 55 | GoalPEORequesterPersonId | REQUESTER_PERSON_ID | — | ✅ |
| 56 | GoalPEOStartDate | START_DATE | — | ✅ |
| 57 | GoalPEOStatusCode | STATUS_CODE | — | ✅ |
| 58 | GoalPEOSuccessCriteria | SUCCESS_CRITERIA | — | — |
| 59 | GoalPEOSuccessCriteriaText | SUCCESS_CRITERIA_TEXT | — | ✅ |
| 60 | GoalPEOTargetCompletionDate | TARGET_COMPLETION_DATE | — | ✅ |
| 61 | GoalPEOTargetType | TARGET_TYPE | — | — |
| 62 | GoalPEOTargetValue | TARGET_VALUE | — | — |
| 63 | GoalPEOUomCode | UOM_CODE | — | — |
| 64 | GoalPEOVersionDate | VERSION_DATE | — | ✅ |
| 65 | OrganizationId | ORGANIZATION_ID | — | ✅ |

### [[hrg_goal_alignments|HRG_GOAL_ALIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalAlignmentPEOAlignedGoalId | ALIGNED_GOAL_ID | — | — |
| 2 | GoalAlignmentPEOGoalAlignmentId | GOAL_ALIGNMENT_ID | — | — |
| 3 | GoalAlignmentPEOGoalId1 | GOAL_ID | — | — |
| 4 | GoalAlignmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[hrg_goal_measurements|HRG_GOAL_MEASUREMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MeasurementPEOAchievedWeight | ACHIEVED_WEIGHT | — | ✅ |
| 2 | MeasurementPEOActualValue | ACTUAL_VALUE | — | ✅ |
| 3 | MeasurementPEOActualValue_1 | ACTUAL_VALUE | — | — |
| 4 | MeasurementPEOBusinessGroupId2_1 | BUSINESS_GROUP_ID | — | — |
| 5 | MeasurementPEOComments1_1 | COMMENTS | — | ✅ |
| 6 | MeasurementPEOCreatedBy2_1 | CREATED_BY | — | — |
| 7 | MeasurementPEOCreationDate2_1 | CREATION_DATE | — | — |
| 8 | MeasurementPEODisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 9 | MeasurementPEOEndDate | END_DATE | — | ✅ |
| 10 | MeasurementPEOGoalId3_1 | GOAL_ID | — | — |
| 11 | MeasurementPEOLastUpdateDate2_1 | LAST_UPDATE_DATE | — | ✅ |
| 12 | MeasurementPEOLastUpdateLogin2_1 | LAST_UPDATE_LOGIN | — | — |
| 13 | MeasurementPEOLastUpdatedBy2_1 | LAST_UPDATED_BY | — | — |
| 14 | MeasurementPEOMaxTarget | MAX_TARGET | — | ✅ |
| 15 | MeasurementPEOMeasureTypeCode | MEASURE_TYPE_CODE | — | ✅ |
| 16 | MeasurementPEOMeasureTypeCode_1 | MEASURE_TYPE_CODE | — | — |
| 17 | MeasurementPEOMeasurementId | MEASUREMENT_ID | — | — |
| 18 | MeasurementPEOMeasurementName | MEASUREMENT_NAME | — | ✅ |
| 19 | MeasurementPEOMinTarget | MIN_TARGET | — | ✅ |
| 20 | MeasurementPEOObjectVersionNumber2_1 | OBJECT_VERSION_NUMBER | — | — |
| 21 | MeasurementPEOStartDate1_1 | START_DATE | — | ✅ |
| 22 | MeasurementPEOTargetPercentage | TARGET_PERCENTAGE | — | ✅ |
| 23 | MeasurementPEOTargetType | TARGET_TYPE | — | ✅ |
| 24 | MeasurementPEOTargetValue | TARGET_VALUE | — | ✅ |
| 25 | MeasurementPEOTargetValue_1 | TARGET_VALUE | — | — |
| 26 | MeasurementPEOUomCode | UOM_CODE | — | ✅ |
| 27 | MeasurementPEOUomCode_1 | UOM_CODE | — | — |

### [[hrg_goal_plan_goals|HRG_GOAL_PLAN_GOALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalPlanGoalPEODisplaySequence | DISPLAY_SEQUENCE | — | — |
| 2 | GoalPlanGoalPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | GoalPlanGoalPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | GoalPlanGoalPEOGoalPlanGoalId | GOAL_PLAN_GOAL_ID | — | — |
| 5 | GoalPlanGoalPEOGoalPlanId | GOAL_PLAN_ID | — | — |
| 6 | GoalPlanGoalPEOGoalPlanSetId | GOAL_PLAN_SET_ID | — | — |
| 7 | GoalPlanGoalPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | GoalPlanGoalPEOReviewPeriodId | REVIEW_PERIOD_ID | — | — |
| 9 | GoalPlanGoalPEOWeighting | WEIGHTING | — | ✅ |

### [[hrt_profiles_tl|HRT_PROFILES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 2 | CreatedBy3 | CREATED_BY | — | — |
| 3 | CreationDate3 | CREATION_DATE | — | — |
| 4 | Description | DESCRIPTION | — | — |
| 5 | Language1 | LANGUAGE | — | — |
| 6 | LastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 9 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 10 | ProfileId | PROFILE_ID | — | — |
| 11 | SourceLang | SOURCE_LANG | — | — |
| 12 | Summary | SUMMARY | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignedByPEOBusinessGroupId5_1 | BUSINESS_GROUP_ID | — | — |
| 2 | AssignedByPEODisplayName2_1 | DISPLAY_NAME | — | — |
| 3 | AssignedByPEOEffectiveEndDate3_1 | EFFECTIVE_END_DATE | — | — |
| 4 | AssignedByPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | AssignedByPEOEffectiveStartDate3_1 | EFFECTIVE_START_DATE | — | ✅ |
| 6 | AssignedByPEOFirstName2_1 | FIRST_NAME | — | — |
| 7 | AssignedByPEOFullName2_1 | FULL_NAME | — | ✅ |
| 8 | AssignedByPEOHonors1_1 | HONORS | — | — |
| 9 | AssignedByPEOKnownAs1_1 | KNOWN_AS | — | — |
| 10 | AssignedByPEOLastName2_1 | LAST_NAME | — | — |
| 11 | AssignedByPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | AssignedByPEOLegislationCode2_1 | LEGISLATION_CODE | — | — |
| 13 | AssignedByPEOListName2_1 | LIST_NAME | — | — |
| 14 | AssignedByPEOMiddleNames2_1 | MIDDLE_NAMES | — | — |
| 15 | AssignedByPEONamInformationCategory2_1 | NAM_INFORMATION_CATEGORY | — | — |
| 16 | AssignedByPEONameType2_1 | NAME_TYPE | — | — |
| 17 | AssignedByPEOOrderName2_1 | ORDER_NAME | — | — |
| 18 | AssignedByPEOPersonId3_1 | PERSON_ID | — | — |
| 19 | AssignedByPEOPersonNameId2_1 | PERSON_NAME_ID | — | — |
| 20 | AssignedByPEOPreviousLastName2_1 | PREVIOUS_LAST_NAME | — | — |
| 21 | AssignedByPEOSuffix2_1 | SUFFIX | — | — |
| 22 | AssignedByPEOTitle2_1 | TITLE | — | — |
| 23 | LastModifiedByPEODisplayName | DISPLAY_NAME | — | — |
| 24 | LastModifiedByPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 25 | LastModifiedByPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 26 | LastModifiedByPEOFirstName | FIRST_NAME | — | — |
| 27 | LastModifiedByPEOFullName | FULL_NAME | — | — |
| 28 | LastModifiedByPEOKnownAs | KNOWN_AS | — | — |
| 29 | LastModifiedByPEOLastName | LAST_NAME | — | — |
| 30 | LastModifiedByPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 31 | LastModifiedByPEOLegislationCode | LEGISLATION_CODE | — | — |
| 32 | LastModifiedByPEOListName | LIST_NAME | — | — |
| 33 | LastModifiedByPEOMiddleNames | MIDDLE_NAMES | — | — |
| 34 | LastModifiedByPEONamInformationCategory | NAM_INFORMATION_CATEGORY | — | — |
| 35 | LastModifiedByPEONameType | NAME_TYPE | — | — |
| 36 | LastModifiedByPEOPersonNameId | PERSON_NAME_ID | — | — |
| 37 | LastModifiedByPEOPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 38 | RequesterPEOBusinessGroupId3_1 | BUSINESS_GROUP_ID | — | — |
| 39 | RequesterPEODisplayName | DISPLAY_NAME | — | — |
| 40 | RequesterPEOEffectiveEndDate1_1 | EFFECTIVE_END_DATE | — | — |
| 41 | RequesterPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 42 | RequesterPEOEffectiveStartDate1_1 | EFFECTIVE_START_DATE | — | ✅ |
| 43 | RequesterPEOFirstName | FIRST_NAME | — | — |
| 44 | RequesterPEOFullName | FULL_NAME | — | ✅ |
| 45 | RequesterPEOLastName | LAST_NAME | — | — |
| 46 | RequesterPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 47 | RequesterPEOLegislationCode | LEGISLATION_CODE | — | — |
| 48 | RequesterPEOListName | LIST_NAME | — | — |
| 49 | RequesterPEOMiddleNames | MIDDLE_NAMES | — | — |
| 50 | RequesterPEONamInformationCategory | NAM_INFORMATION_CATEGORY | — | — |
| 51 | RequesterPEONameType | NAME_TYPE | — | — |
| 52 | RequesterPEOOrderName | ORDER_NAME | — | — |
| 53 | RequesterPEOPersonId1_1 | PERSON_ID | — | — |
| 54 | RequesterPEOPersonNameId | PERSON_NAME_ID | — | — |
| 55 | RequesterPEOPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 56 | RequesterPEORequesterPEOTitle | TITLE | — | — |
| 57 | RequesterPEOSuffix | SUFFIX | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
