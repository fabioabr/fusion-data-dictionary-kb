---
id: DOC-HCM-PVO-ContentItemValuePVO
doc_type: system-doc
title: "ContentItemValuePVO — PVO Human Capital Management"
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
  - ContentItemValuePVO
  - contentitemvaluepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContentItemValuePVO

## 📌 Visão Geral

Relaciona itens de conteudo a metas e outcomes-alvo com valores mensuraveis. Suporta vinculacao entre competencias/certificacoes e objetivos de desempenho.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmGoalCoreAM.ContentItemValuePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 124 | 5 | 4 | 34 | 27% |

---

## 🔗 Tabelas Relacionadas

- [[hrg_goals|HRG_GOALS]] — 54 atributos (3 BICC)
- [[hrg_goal_target_outcomes|HRG_GOAL_TARGET_OUTCOMES]] — 19 atributos (1 PKs, 9 BICC)
- [[hrt_content_items_b|HRT_CONTENT_ITEMS_B]] — 16 atributos (2 PKs, 7 BICC)
- [[hrt_content_items_tl|HRT_CONTENT_ITEMS_TL]] — 13 atributos (1 PKs, 2 BICC)
- [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]] — 22 atributos (13 BICC)

---

## ⚙️ Atributos

### [[hrg_goals|HRG_GOALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalPEOAccessToHierarchyFlag | ACCESS_TO_HIERARCHY_FLAG | — | — |
| 2 | GoalPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 3 | GoalPEOActualValue | ACTUAL_VALUE | — | — |
| 4 | GoalPEOAllowKeyAttrUpdateFlag | ALLOW_KEY_ATTR_UPDATE_FLAG | — | — |
| 5 | GoalPEOApprovalStatusCode | APPROVAL_STATUS_CODE | — | — |
| 6 | GoalPEOAssignedByPersonId | ASSIGNED_BY_PERSON_ID | — | — |
| 7 | GoalPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 8 | GoalPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 9 | GoalPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 10 | GoalPEOCategoryCode | CATEGORY_CODE | — | — |
| 11 | GoalPEOComments | COMMENTS | — | — |
| 12 | GoalPEOCommentsText | COMMENTS_TEXT | — | — |
| 13 | GoalPEOCreatedBy | CREATED_BY | — | — |
| 14 | GoalPEOCreationDate | CREATION_DATE | — | — |
| 15 | GoalPEODescription | DESCRIPTION | — | — |
| 16 | GoalPEOGoalApprovalState | GOAL_APPROVAL_STATE | — | — |
| 17 | GoalPEOGoalId | GOAL_ID | — | ✅ |
| 18 | GoalPEOGoalName | GOAL_NAME | — | — |
| 19 | GoalPEOGoalSourceCode | GOAL_SOURCE_CODE | — | — |
| 20 | GoalPEOGoalTypeCode | GOAL_TYPE_CODE | — | — |
| 21 | GoalPEOGoalUrl | GOAL_URL | — | — |
| 22 | GoalPEOGoalVersionTypeCode | GOAL_VERSION_TYPE_CODE | — | — |
| 23 | GoalPEOHrchyAccessGrantDate | HRCHY_ACCESS_GRANT_DATE | — | — |
| 24 | GoalPEOIncludeInPerfdocFlag | INCLUDE_IN_PERFDOC_FLAG | — | — |
| 25 | GoalPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | GoalPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 27 | GoalPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 28 | GoalPEOLevelCode | LEVEL_CODE | — | — |
| 29 | GoalPEOLevelMeaning | LEVEL_MEANING | — | — |
| 30 | GoalPEOLongDescription | LONG_DESCRIPTION | — | — |
| 31 | GoalPEOMassRequestId | MASS_REQUEST_ID | — | — |
| 32 | GoalPEOMeasureComments | MEASURE_COMMENTS | — | — |
| 33 | GoalPEOMeasureName | MEASURE_NAME | — | — |
| 34 | GoalPEOMeasureTypeCode | MEASURE_TYPE_CODE | — | — |
| 35 | GoalPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 36 | GoalPEOOrganizationId | ORGANIZATION_ID | — | — |
| 37 | GoalPEOPercentCompleteCode | PERCENT_COMPLETE_CODE | — | — |
| 38 | GoalPEOPersonId | PERSON_ID | — | — |
| 39 | GoalPEOPriorityCode | PRIORITY_CODE | — | — |
| 40 | GoalPEOPrivateFlag | PRIVATE_FLAG | — | — |
| 41 | GoalPEOPublishDate | PUBLISH_DATE | — | — |
| 42 | GoalPEOPublishedFlag | PUBLISHED_FLAG | — | — |
| 43 | GoalPEOReferenceContentItemId | REFERENCE_CONTENT_ITEM_ID | — | — |
| 44 | GoalPEOReferenceGoalId | REFERENCE_GOAL_ID | — | — |
| 45 | GoalPEORequesterPersonId | REQUESTER_PERSON_ID | — | — |
| 46 | GoalPEOStartDate | START_DATE | — | — |
| 47 | GoalPEOStatusCode | STATUS_CODE | — | — |
| 48 | GoalPEOSuccessCriteria | SUCCESS_CRITERIA | — | — |
| 49 | GoalPEOSuccessCriteriaText | SUCCESS_CRITERIA_TEXT | — | — |
| 50 | GoalPEOTargetCompletionDate | TARGET_COMPLETION_DATE | — | — |
| 51 | GoalPEOTargetType | TARGET_TYPE | — | — |
| 52 | GoalPEOTargetValue | TARGET_VALUE | — | — |
| 53 | GoalPEOUomCode | UOM_CODE | — | — |
| 54 | GoalPEOVersionDate | VERSION_DATE | — | — |

### [[hrg_goal_target_outcomes|HRG_GOAL_TARGET_OUTCOMES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalTargetOutcomeId | GOAL_TARGET_OUTCOME_ID | 🔑 | ✅ |
| 2 | GoalTargetOutcomePEOApprovedRatingId | APPROVED_RATING_ID | — | — |
| 3 | GoalTargetOutcomePEOApprovedRatingId2 | APPROVED_RATING_ID2 | — | — |
| 4 | GoalTargetOutcomePEOApprovedRatingId3 | APPROVED_RATING_ID3 | — | — |
| 5 | GoalTargetOutcomePEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 6 | GoalTargetOutcomePEOComments | COMMENTS | — | ✅ |
| 7 | GoalTargetOutcomePEOContentItemId | CONTENT_ITEM_ID | — | — |
| 8 | GoalTargetOutcomePEOContentItemTypeId | CONTENT_ITEM_TYPE_ID | — | — |
| 9 | GoalTargetOutcomePEOContentSourceCode | CONTENT_SOURCE_CODE | — | ✅ |
| 10 | GoalTargetOutcomePEOCreatedBy | CREATED_BY | — | ✅ |
| 11 | GoalTargetOutcomePEOCreationDate | CREATION_DATE | — | ✅ |
| 12 | GoalTargetOutcomePEOGoalId | GOAL_ID | — | — |
| 13 | GoalTargetOutcomePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | GoalTargetOutcomePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | GoalTargetOutcomePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | GoalTargetOutcomePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | GoalTargetOutcomePEOTargetRatingLevelId | TARGET_RATING_LEVEL_ID | — | — |
| 18 | GoalTargetOutcomePEOTargetRatingLevelId2 | TARGET_RATING_LEVEL_ID2 | — | — |
| 19 | GoalTargetOutcomePEOTargetRatingLevelId3 | TARGET_RATING_LEVEL_ID3 | — | — |

### [[hrt_content_items_b|HRT_CONTENT_ITEMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | ContentItemBPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 3 | ContentItemBPEOContentItemCode | CONTENT_ITEM_CODE | — | ✅ |
| 4 | ContentItemBPEOContentKeyflexId | CONTENT_KEYFLEX_ID | — | — |
| 5 | ContentItemBPEOContentSupplierCode | CONTENT_SUPPLIER_CODE | — | ✅ |
| 6 | ContentItemBPEOContentTypeId | CONTENT_TYPE_ID | — | ✅ |
| 7 | ContentItemBPEOCreatedBy | CREATED_BY | — | — |
| 8 | ContentItemBPEOCreationDate | CREATION_DATE | — | — |
| 9 | ContentItemBPEODateFrom | DATE_FROM | — | — |
| 10 | ContentItemBPEODateTo | DATE_TO | — | — |
| 11 | ContentItemBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | ContentItemBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | ContentItemBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | ContentItemBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | ContentItemBPEORatingModelId | RATING_MODEL_ID | — | ✅ |
| 16 | ContentItemId | CONTENT_ITEM_ID | 🔑 | ✅ |

### [[hrt_content_items_tl|HRT_CONTENT_ITEMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContentItemTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ContentItemTranslationPEOContentItemId | CONTENT_ITEM_ID | — | — |
| 3 | ContentItemTranslationPEOCreatedBy | CREATED_BY | — | — |
| 4 | ContentItemTranslationPEOCreationDate | CREATION_DATE | — | — |
| 5 | ContentItemTranslationPEOItemDescription | ITEM_DESCRIPTION | — | — |
| 6 | ContentItemTranslationPEOItemDescrlong | ITEM_DESCRLONG | — | — |
| 7 | ContentItemTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ContentItemTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ContentItemTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ContentItemTranslationPEOName | NAME | — | — |
| 11 | ContentItemTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ContentItemTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 13 | Language | LANGUAGE | 🔑 | ✅ |

### [[hrt_rating_levels_b|HRT_RATING_LEVELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RatingLevelBPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 2 | RatingLevelBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | RatingLevelBPEOCareerStrDev | CAREER_STR_DEV | — | ✅ |
| 4 | RatingLevelBPEOCreatedBy | CREATED_BY | — | — |
| 5 | RatingLevelBPEOCreationDate | CREATION_DATE | — | — |
| 6 | RatingLevelBPEODateFrom | DATE_FROM | — | ✅ |
| 7 | RatingLevelBPEODateTo | DATE_TO | — | ✅ |
| 8 | RatingLevelBPEOFromPoints | FROM_POINTS | — | ✅ |
| 9 | RatingLevelBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | RatingLevelBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | RatingLevelBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | RatingLevelBPEOMaxRatingDistribution | MAX_RATING_DISTRIBUTION | — | ✅ |
| 13 | RatingLevelBPEOMinRatingDistribution | MIN_RATING_DISTRIBUTION | — | ✅ |
| 14 | RatingLevelBPEOModuleId | MODULE_ID | — | — |
| 15 | RatingLevelBPEONumericRating | NUMERIC_RATING | — | ✅ |
| 16 | RatingLevelBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | RatingLevelBPEORatingLevelCode | RATING_LEVEL_CODE | — | ✅ |
| 18 | RatingLevelBPEORatingLevelId | RATING_LEVEL_ID | — | — |
| 19 | RatingLevelBPEORatingModelId | RATING_MODEL_ID | — | — |
| 20 | RatingLevelBPEOReviewPoints | REVIEW_POINTS | — | ✅ |
| 21 | RatingLevelBPEOStarRating | STAR_RATING | — | ✅ |
| 22 | RatingLevelBPEOToPoints | TO_POINTS | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
