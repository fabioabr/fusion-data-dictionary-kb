---
id: DOC-HCM-PVO-GoalTargetOutcomeProfilesPVO
doc_type: system-doc
title: "GoalTargetOutcomeProfilesPVO — PVO Human Capital Management"
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
  - GoalTargetOutcomeProfilesPVO
  - goaltargetoutcomeprofilespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GoalTargetOutcomeProfilesPVO

## 📌 Visão Geral

Vincula metas a perfis de competência de resultado esperado. Suporta alinhamento entre objetivos e desenvolvimento de competências.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmGoalCoreAM.GoalTargetOutcomeProfilesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 154 | 6 | 2 | 28 | 18% |

---

## 🔗 Tabelas Relacionadas

- [[hrg_goals|HRG_GOALS]] — 38 atributos (4 BICC)
- [[hrt_content_items_b|HRT_CONTENT_ITEMS_B]] — 8 atributos (5 BICC)
- [[hrt_profiles_b|HRT_PROFILES_B]] — 1 atributos (1 PKs, 1 BICC)
- [[hrt_profile_items|HRT_PROFILE_ITEMS]] — 89 atributos (1 PKs, 7 BICC)
- [[hrt_profile_relations|HRT_PROFILE_RELATIONS]] — 3 atributos
- [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]] — 15 atributos (11 BICC)

---

## ⚙️ Atributos

### [[hrg_goals|HRG_GOALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalId | GOAL_ID | — | ✅ |
| 2 | GoalPEOActiveFlag | ACTIVE_FLAG | — | — |
| 3 | GoalPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 4 | GoalPEOActualValue | ACTUAL_VALUE | — | — |
| 5 | GoalPEOAllowKeyAttrUpdateFlag | ALLOW_KEY_ATTR_UPDATE_FLAG | — | — |
| 6 | GoalPEOApprovalStatusCode | APPROVAL_STATUS_CODE | — | — |
| 7 | GoalPEOApproverResponseCode | APPROVER_RESPONSE_CODE | — | — |
| 8 | GoalPEOAssignedByPersonId | ASSIGNED_BY_PERSON_ID | — | — |
| 9 | GoalPEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 10 | GoalPEOComments | COMMENTS | — | — |
| 11 | GoalPEOCommentsText | COMMENTS_TEXT | — | — |
| 12 | GoalPEODescription | DESCRIPTION | — | — |
| 13 | GoalPEOGoalAccessLevelCode | GOAL_ACCESS_LEVEL_CODE | — | — |
| 14 | GoalPEOGoalApprovalState | GOAL_APPROVAL_STATE | — | — |
| 15 | GoalPEOGoalName | GOAL_NAME | — | — |
| 16 | GoalPEOGoalSourceCode | GOAL_SOURCE_CODE | — | — |
| 17 | GoalPEOGoalSubTypeCode | GOAL_SUB_TYPE_CODE | — | — |
| 18 | GoalPEOGoalTypeCode | GOAL_TYPE_CODE | — | — |
| 19 | GoalPEOGoalUrl | GOAL_URL | — | — |
| 20 | GoalPEOGoalVersionTypeCode | GOAL_VERSION_TYPE_CODE | — | — |
| 21 | GoalPEOLevelCode | LEVEL_CODE | — | — |
| 22 | GoalPEOLevelMeaning | LEVEL_MEANING | — | — |
| 23 | GoalPEOLongDescription | LONG_DESCRIPTION | — | — |
| 24 | GoalPEOMeasureCalcRuleCode | MEASURE_CALC_RULE_CODE | — | — |
| 25 | GoalPEOMeasureComments | MEASURE_COMMENTS | — | — |
| 26 | GoalPEOMeasureName | MEASURE_NAME | — | — |
| 27 | GoalPEOOrganizationId | ORGANIZATION_ID | — | — |
| 28 | GoalPEOPriorityCode | PRIORITY_CODE | — | — |
| 29 | GoalPEOPublishedFlag | PUBLISHED_FLAG | — | — |
| 30 | GoalPEORequesterPersonId | REQUESTER_PERSON_ID | — | — |
| 31 | GoalPEOStartDate | START_DATE | — | — |
| 32 | GoalPEOStatusCode | STATUS_CODE | — | — |
| 33 | GoalPEOSuccessCriteria | SUCCESS_CRITERIA | — | — |
| 34 | GoalPEOSuccessCriteriaText | SUCCESS_CRITERIA_TEXT | — | — |
| 35 | GoalPEOTargetCompletionDate | TARGET_COMPLETION_DATE | — | — |
| 36 | GoalPEOTargetType | TARGET_TYPE | — | — |
| 37 | GoalPEOTargetValue | TARGET_VALUE | — | — |
| 38 | PersonId | PERSON_ID | — | ✅ |

### [[hrt_content_items_b|HRT_CONTENT_ITEMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentItemBPEOBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | ContentItemBPEOContentItemCode | CONTENT_ITEM_CODE | — | ✅ |
| 3 | ContentItemBPEOContentItemId | CONTENT_ITEM_ID | — | ✅ |
| 4 | ContentItemBPEOContentSupplierCode | CONTENT_SUPPLIER_CODE | — | ✅ |
| 5 | ContentItemBPEOContentTypeId | CONTENT_TYPE_ID | — | — |
| 6 | ContentItemBPEOContentTypeId1 | CONTENT_TYPE_ID | — | ✅ |
| 7 | ContentItemBPEORatingModelId | RATING_MODEL_ID | — | ✅ |
| 8 | ContentItemBPEOStateProvinceId1 | STATE_PROVINCE_ID | — | — |

### [[hrt_profiles_b|HRT_PROFILES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProfileId | PROFILE_ID | 🔑 | ✅ |

### [[hrt_profile_items|HRT_PROFILE_ITEMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProfileItemId | PROFILE_ITEM_ID | 🔑 | ✅ |
| 2 | ProfileItemPEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | ProfileItemPEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | ProfileItemPEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | ProfileItemPEOAttribute12 | ATTRIBUTE12 | — | — |
| 6 | ProfileItemPEOAttribute13 | ATTRIBUTE13 | — | — |
| 7 | ProfileItemPEOAttribute14 | ATTRIBUTE14 | — | — |
| 8 | ProfileItemPEOAttribute15 | ATTRIBUTE15 | — | — |
| 9 | ProfileItemPEOAttribute16 | ATTRIBUTE16 | — | — |
| 10 | ProfileItemPEOAttribute17 | ATTRIBUTE17 | — | — |
| 11 | ProfileItemPEOAttribute18 | ATTRIBUTE18 | — | — |
| 12 | ProfileItemPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 13 | ProfileItemPEOCreatedBy | CREATED_BY | — | ✅ |
| 14 | ProfileItemPEOCreationDate | CREATION_DATE | — | ✅ |
| 15 | ProfileItemPEOItemClob1 | ITEM_CLOB_1 | — | ✅ |
| 16 | ProfileItemPEOItemClob2 | ITEM_CLOB_2 | — | — |
| 17 | ProfileItemPEOItemClob3 | ITEM_CLOB_3 | — | — |
| 18 | ProfileItemPEOItemClob4 | ITEM_CLOB_4 | — | — |
| 19 | ProfileItemPEOItemClob5 | ITEM_CLOB_5 | — | — |
| 20 | ProfileItemPEOItemDecimal2 | ITEM_DECIMAL_2 | — | — |
| 21 | ProfileItemPEOItemDecimal3 | ITEM_DECIMAL_3 | — | — |
| 22 | ProfileItemPEOItemDecimal4 | ITEM_DECIMAL_4 | — | — |
| 23 | ProfileItemPEOItemNumber1 | ITEM_NUMBER_1 | — | — |
| 24 | ProfileItemPEOItemNumber10 | ITEM_NUMBER_10 | — | — |
| 25 | ProfileItemPEOItemNumber2 | ITEM_NUMBER_2 | — | — |
| 26 | ProfileItemPEOItemNumber3 | ITEM_NUMBER_3 | — | — |
| 27 | ProfileItemPEOItemNumber4 | ITEM_NUMBER_4 | — | — |
| 28 | ProfileItemPEOItemNumber5 | ITEM_NUMBER_5 | — | — |
| 29 | ProfileItemPEOItemNumber6 | ITEM_NUMBER_6 | — | — |
| 30 | ProfileItemPEOItemNumber7 | ITEM_NUMBER_7 | — | — |
| 31 | ProfileItemPEOItemNumber8 | ITEM_NUMBER_8 | — | — |
| 32 | ProfileItemPEOItemNumber9 | ITEM_NUMBER_9 | — | — |
| 33 | ProfileItemPEOItemText20001 | ITEM_TEXT2000_1 | — | — |
| 34 | ProfileItemPEOItemText20002 | ITEM_TEXT2000_2 | — | — |
| 35 | ProfileItemPEOItemText20003 | ITEM_TEXT2000_3 | — | — |
| 36 | ProfileItemPEOItemText20004 | ITEM_TEXT2000_4 | — | — |
| 37 | ProfileItemPEOItemText20005 | ITEM_TEXT2000_5 | — | — |
| 38 | ProfileItemPEOItemText2401 | ITEM_TEXT240_1 | — | — |
| 39 | ProfileItemPEOItemText24010 | ITEM_TEXT240_10 | — | — |
| 40 | ProfileItemPEOItemText24011 | ITEM_TEXT240_11 | — | — |
| 41 | ProfileItemPEOItemText24012 | ITEM_TEXT240_12 | — | — |
| 42 | ProfileItemPEOItemText24013 | ITEM_TEXT240_13 | — | — |
| 43 | ProfileItemPEOItemText24014 | ITEM_TEXT240_14 | — | — |
| 44 | ProfileItemPEOItemText24015 | ITEM_TEXT240_15 | — | — |
| 45 | ProfileItemPEOItemText2402 | ITEM_TEXT240_2 | — | — |
| 46 | ProfileItemPEOItemText2403 | ITEM_TEXT240_3 | — | — |
| 47 | ProfileItemPEOItemText2404 | ITEM_TEXT240_4 | — | — |
| 48 | ProfileItemPEOItemText2405 | ITEM_TEXT240_5 | — | — |
| 49 | ProfileItemPEOItemText2406 | ITEM_TEXT240_6 | — | — |
| 50 | ProfileItemPEOItemText2407 | ITEM_TEXT240_7 | — | — |
| 51 | ProfileItemPEOItemText2408 | ITEM_TEXT240_8 | — | — |
| 52 | ProfileItemPEOItemText2409 | ITEM_TEXT240_9 | — | — |
| 53 | ProfileItemPEOItemText301 | ITEM_TEXT30_1 | — | — |
| 54 | ProfileItemPEOItemText3010 | ITEM_TEXT30_10 | — | — |
| 55 | ProfileItemPEOItemText3011 | ITEM_TEXT30_11 | — | — |
| 56 | ProfileItemPEOItemText3012 | ITEM_TEXT30_12 | — | — |
| 57 | ProfileItemPEOItemText3013 | ITEM_TEXT30_13 | — | — |
| 58 | ProfileItemPEOItemText3014 | ITEM_TEXT30_14 | — | — |
| 59 | ProfileItemPEOItemText3015 | ITEM_TEXT30_15 | — | — |
| 60 | ProfileItemPEOItemText302 | ITEM_TEXT30_2 | — | — |
| 61 | ProfileItemPEOItemText303 | ITEM_TEXT30_3 | — | — |
| 62 | ProfileItemPEOItemText304 | ITEM_TEXT30_4 | — | — |
| 63 | ProfileItemPEOItemText305 | ITEM_TEXT30_5 | — | — |
| 64 | ProfileItemPEOItemText306 | ITEM_TEXT30_6 | — | — |
| 65 | ProfileItemPEOItemText307 | ITEM_TEXT30_7 | — | — |
| 66 | ProfileItemPEOItemText308 | ITEM_TEXT30_8 | — | — |
| 67 | ProfileItemPEOItemText309 | ITEM_TEXT30_9 | — | — |
| 68 | ProfileItemPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 69 | ProfileItemPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 70 | ProfileItemPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 71 | ProfileItemPEOMandatory | MANDATORY | — | — |
| 72 | ProfileItemPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 73 | ProfileItemPEOParentProfileItemId | PARENT_PROFILE_ITEM_ID | — | — |
| 74 | ProfileItemPEOProfileId1 | PROFILE_ID | — | — |
| 75 | ProfileItemPEOQualifierId1 | QUALIFIER_ID1 | — | — |
| 76 | ProfileItemPEOQualifierId2 | QUALIFIER_ID2 | — | — |
| 77 | ProfileItemPEORatingLevelId1 | RATING_LEVEL_ID1 | — | — |
| 78 | ProfileItemPEORatingLevelId2 | RATING_LEVEL_ID2 | — | — |
| 79 | ProfileItemPEORatingModelId1 | RATING_MODEL_ID1 | — | — |
| 80 | ProfileItemPEORatingModelId2 | RATING_MODEL_ID2 | — | — |
| 81 | ProfileItemPEORatingModelId3 | RATING_MODEL_ID3 | — | — |
| 82 | ProfileItemPEOSectionId | SECTION_ID | — | — |
| 83 | ProfileItemPEOSourceId | SOURCE_ID | — | — |
| 84 | ProfileItemPEOSourceKey1 | SOURCE_KEY1 | — | — |
| 85 | ProfileItemPEOSourceKey3 | SOURCE_KEY3 | — | — |
| 86 | ProfileItemPEOSourceType | SOURCE_TYPE | — | — |
| 87 | ProfileItemPEOStateProvinceId | STATE_PROVINCE_ID | — | — |
| 88 | RatingLevelId3 | RATING_LEVEL_ID3 | — | — |
| 89 | SourceKey2 | SOURCE_KEY2 | — | — |

### [[hrt_profile_relations|HRT_PROFILE_RELATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProfileRelationPEOObjectId | OBJECT_ID | — | — |
| 2 | ProfileRelationPEOProfileRelationId | PROFILE_RELATION_ID | — | — |
| 3 | ProfileRelationPEORelationId | RELATION_ID | — | — |

### [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RatingLevelBPEOBusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 2 | RatingLevelBPEOCareerStrDev | CAREER_STR_DEV | — | ✅ |
| 3 | RatingLevelBPEODateFrom1 | DATE_FROM | — | ✅ |
| 4 | RatingLevelBPEODateTo1 | DATE_TO | — | ✅ |
| 5 | RatingLevelBPEOFromPoints | FROM_POINTS | — | ✅ |
| 6 | RatingLevelBPEOMaxRatingDistribution | MAX_RATING_DISTRIBUTION | — | ✅ |
| 7 | RatingLevelBPEOMinRatingDistribution | MIN_RATING_DISTRIBUTION | — | ✅ |
| 8 | RatingLevelBPEONumericRating | NUMERIC_RATING | — | ✅ |
| 9 | RatingLevelBPEORatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 10 | RatingLevelBPEORatingLevelId | RATING_LEVEL_ID | — | — |
| 11 | RatingLevelBPEORatingModelId4 | RATING_MODEL_ID | — | — |
| 12 | RatingLevelBPEOReviewPoints | REVIEW_POINTS | — | ✅ |
| 13 | RatingLevelBPEOStarRating | STAR_RATING | — | ✅ |
| 14 | RatingLevelBPEOToPoints | TO_POINTS | — | ✅ |
| 15 | RatingLevelId | RATING_LEVEL_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
