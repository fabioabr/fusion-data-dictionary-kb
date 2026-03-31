---
id: DOC-HCM-PVO-OrganizationGoalPVO
doc_type: system-doc
title: "OrganizationGoalPVO — PVO Human Capital Management"
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
  - OrganizationGoalPVO
  - organizationgoalpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OrganizationGoalPVO

## 📌 Visão Geral

Extrai metas organizacionais com medições, planos de metas e nomes dos responsáveis. Suporta cascateamento de objetivos estratégicos e acompanhamento de resultados por unidade organizacional.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmGoalCoreAM.OrganizationGoalPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 295 | 4 | 1 | 51 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[hrg_goals|HRG_GOALS]] — 130 atributos (1 PKs, 43 BICC)
- [[hrg_goal_measurements|HRG_GOAL_MEASUREMENTS]] — 23 atributos (7 BICC)
- [[hrg_goal_plan_goals|HRG_GOAL_PLAN_GOALS]] — 18 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 124 atributos

---

## ⚙️ Atributos

### [[hrg_goals|HRG_GOALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute101 | ATTRIBUTE10 | — | — |
| 2 | Attribute110 | ATTRIBUTE1 | — | — |
| 3 | Attribute111 | ATTRIBUTE11 | — | — |
| 4 | Attribute121 | ATTRIBUTE12 | — | — |
| 5 | Attribute131 | ATTRIBUTE13 | — | — |
| 6 | Attribute141 | ATTRIBUTE14 | — | — |
| 7 | Attribute151 | ATTRIBUTE15 | — | — |
| 8 | Attribute161 | ATTRIBUTE16 | — | — |
| 9 | Attribute171 | ATTRIBUTE17 | — | — |
| 10 | Attribute181 | ATTRIBUTE18 | — | — |
| 11 | Attribute191 | ATTRIBUTE19 | — | — |
| 12 | Attribute201 | ATTRIBUTE20 | — | — |
| 13 | Attribute210 | ATTRIBUTE2 | — | — |
| 14 | Attribute211 | ATTRIBUTE21 | — | — |
| 15 | Attribute221 | ATTRIBUTE22 | — | — |
| 16 | Attribute231 | ATTRIBUTE23 | — | — |
| 17 | Attribute241 | ATTRIBUTE24 | — | — |
| 18 | Attribute251 | ATTRIBUTE25 | — | — |
| 19 | Attribute261 | ATTRIBUTE26 | — | — |
| 20 | Attribute271 | ATTRIBUTE27 | — | — |
| 21 | Attribute281 | ATTRIBUTE28 | — | — |
| 22 | Attribute291 | ATTRIBUTE29 | — | — |
| 23 | Attribute301 | ATTRIBUTE30 | — | — |
| 24 | Attribute31 | ATTRIBUTE3 | — | — |
| 25 | Attribute41 | ATTRIBUTE4 | — | — |
| 26 | Attribute51 | ATTRIBUTE5 | — | — |
| 27 | Attribute61 | ATTRIBUTE6 | — | — |
| 28 | Attribute71 | ATTRIBUTE7 | — | — |
| 29 | Attribute81 | ATTRIBUTE8 | — | — |
| 30 | Attribute91 | ATTRIBUTE9 | — | — |
| 31 | AttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 32 | AttributeDate101 | ATTRIBUTE_DATE10 | — | — |
| 33 | AttributeDate111 | ATTRIBUTE_DATE11 | — | — |
| 34 | AttributeDate121 | ATTRIBUTE_DATE12 | — | — |
| 35 | AttributeDate131 | ATTRIBUTE_DATE13 | — | — |
| 36 | AttributeDate141 | ATTRIBUTE_DATE14 | — | — |
| 37 | AttributeDate151 | ATTRIBUTE_DATE15 | — | — |
| 38 | AttributeDate16 | ATTRIBUTE_DATE1 | — | — |
| 39 | AttributeDate21 | ATTRIBUTE_DATE2 | — | — |
| 40 | AttributeDate31 | ATTRIBUTE_DATE3 | — | — |
| 41 | AttributeDate41 | ATTRIBUTE_DATE4 | — | — |
| 42 | AttributeDate51 | ATTRIBUTE_DATE5 | — | — |
| 43 | AttributeDate61 | ATTRIBUTE_DATE6 | — | — |
| 44 | AttributeDate71 | ATTRIBUTE_DATE7 | — | — |
| 45 | AttributeDate81 | ATTRIBUTE_DATE8 | — | — |
| 46 | AttributeDate91 | ATTRIBUTE_DATE9 | — | — |
| 47 | AttributeNumber101 | ATTRIBUTE_NUMBER10 | — | — |
| 48 | AttributeNumber110 | ATTRIBUTE_NUMBER1 | — | — |
| 49 | AttributeNumber111 | ATTRIBUTE_NUMBER11 | — | — |
| 50 | AttributeNumber121 | ATTRIBUTE_NUMBER12 | — | — |
| 51 | AttributeNumber131 | ATTRIBUTE_NUMBER13 | — | — |
| 52 | AttributeNumber141 | ATTRIBUTE_NUMBER14 | — | — |
| 53 | AttributeNumber151 | ATTRIBUTE_NUMBER15 | — | — |
| 54 | AttributeNumber161 | ATTRIBUTE_NUMBER16 | — | — |
| 55 | AttributeNumber171 | ATTRIBUTE_NUMBER17 | — | — |
| 56 | AttributeNumber181 | ATTRIBUTE_NUMBER18 | — | — |
| 57 | AttributeNumber191 | ATTRIBUTE_NUMBER19 | — | — |
| 58 | AttributeNumber201 | ATTRIBUTE_NUMBER20 | — | — |
| 59 | AttributeNumber21 | ATTRIBUTE_NUMBER2 | — | — |
| 60 | AttributeNumber31 | ATTRIBUTE_NUMBER3 | — | — |
| 61 | AttributeNumber41 | ATTRIBUTE_NUMBER4 | — | — |
| 62 | AttributeNumber51 | ATTRIBUTE_NUMBER5 | — | — |
| 63 | AttributeNumber61 | ATTRIBUTE_NUMBER6 | — | — |
| 64 | AttributeNumber71 | ATTRIBUTE_NUMBER7 | — | — |
| 65 | AttributeNumber81 | ATTRIBUTE_NUMBER8 | — | — |
| 66 | AttributeNumber91 | ATTRIBUTE_NUMBER9 | — | — |
| 67 | GoalAccessLevelCode | GOAL_ACCESS_LEVEL_CODE | — | — |
| 68 | GoalExtId | GOAL_EXT_ID | — | — |
| 69 | GoalId | GOAL_ID | 🔑 | ✅ |
| 70 | GoalPEOAccessToHierarchyFlag | ACCESS_TO_HIERARCHY_FLAG | — | ✅ |
| 71 | GoalPEOActiveFlag | ACTIVE_FLAG | — | — |
| 72 | GoalPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 73 | GoalPEOActualValue | ACTUAL_VALUE | — | — |
| 74 | GoalPEOAllowKeyAttrUpdateFlag | ALLOW_KEY_ATTR_UPDATE_FLAG | — | ✅ |
| 75 | GoalPEOApprovalStatusCode | APPROVAL_STATUS_CODE | — | ✅ |
| 76 | GoalPEOApproverResponseCode | APPROVER_RESPONSE_CODE | — | — |
| 77 | GoalPEOAssignedByPersonId | ASSIGNED_BY_PERSON_ID | — | ✅ |
| 78 | GoalPEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 79 | GoalPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 80 | GoalPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 81 | GoalPEOCategoryCode | CATEGORY_CODE | — | ✅ |
| 82 | GoalPEOComments | COMMENTS | — | — |
| 83 | GoalPEOCommentsText | COMMENTS_TEXT | — | ✅ |
| 84 | GoalPEOCreatedBy | CREATED_BY | — | ✅ |
| 85 | GoalPEOCreationDate | CREATION_DATE | — | ✅ |
| 86 | GoalPEODescription | DESCRIPTION | — | ✅ |
| 87 | GoalPEOGoalApprovalState | GOAL_APPROVAL_STATE | — | — |
| 88 | GoalPEOGoalName | GOAL_NAME | — | ✅ |
| 89 | GoalPEOGoalSourceCode | GOAL_SOURCE_CODE | — | ✅ |
| 90 | GoalPEOGoalTypeCode | GOAL_TYPE_CODE | — | ✅ |
| 91 | GoalPEOGoalUrl | GOAL_URL | — | ✅ |
| 92 | GoalPEOGoalVersionTypeCode | GOAL_VERSION_TYPE_CODE | — | ✅ |
| 93 | GoalPEOHrchyAccessGrantDate | HRCHY_ACCESS_GRANT_DATE | — | ✅ |
| 94 | GoalPEOIncludeInPerfdocFlag | INCLUDE_IN_PERFDOC_FLAG | — | ✅ |
| 95 | GoalPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 96 | GoalPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 97 | GoalPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 98 | GoalPEOLevelCode | LEVEL_CODE | — | ✅ |
| 99 | GoalPEOLevelMeaning | LEVEL_MEANING | — | ✅ |
| 100 | GoalPEOLongDescription | LONG_DESCRIPTION | — | — |
| 101 | GoalPEOMassRequestId | MASS_REQUEST_ID | — | ✅ |
| 102 | GoalPEOMeasureComments | MEASURE_COMMENTS | — | — |
| 103 | GoalPEOMeasureName | MEASURE_NAME | — | — |
| 104 | GoalPEOMeasureTypeCode | MEASURE_TYPE_CODE | — | — |
| 105 | GoalPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 106 | GoalPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 107 | GoalPEOPercentCompleteCode | PERCENT_COMPLETE_CODE | — | ✅ |
| 108 | GoalPEOPersonId | PERSON_ID | — | ✅ |
| 109 | GoalPEOPreviousStateGoalId | PREVIOUS_STATE_GOAL_ID | — | — |
| 110 | GoalPEOPriorityCode | PRIORITY_CODE | — | ✅ |
| 111 | GoalPEOPrivateFlag | PRIVATE_FLAG | — | ✅ |
| 112 | GoalPEOPublishDate | PUBLISH_DATE | — | ✅ |
| 113 | GoalPEOPublishedFlag | PUBLISHED_FLAG | — | ✅ |
| 114 | GoalPEOReferenceContentItemId | REFERENCE_CONTENT_ITEM_ID | — | ✅ |
| 115 | GoalPEOReferenceGoalId | REFERENCE_GOAL_ID | — | ✅ |
| 116 | GoalPEORequesterPersonId | REQUESTER_PERSON_ID | — | ✅ |
| 117 | GoalPEOStartDate | START_DATE | — | ✅ |
| 118 | GoalPEOStatusCode | STATUS_CODE | — | ✅ |
| 119 | GoalPEOSuccessCriteria | SUCCESS_CRITERIA | — | — |
| 120 | GoalPEOSuccessCriteriaText | SUCCESS_CRITERIA_TEXT | — | ✅ |
| 121 | GoalPEOTargetCompletionDate | TARGET_COMPLETION_DATE | — | ✅ |
| 122 | GoalPEOTargetType | TARGET_TYPE | — | — |
| 123 | GoalPEOTargetValue | TARGET_VALUE | — | — |
| 124 | GoalPEOUomCode | UOM_CODE | — | — |
| 125 | GoalPEOVersionDate | VERSION_DATE | — | ✅ |
| 126 | GoalSubTypeCode | GOAL_SUB_TYPE_CODE | — | — |
| 127 | LastModifiedBy | LAST_MODIFIED_BY | — | — |
| 128 | LastModifiedDate | LAST_MODIFIED_DATE | — | — |
| 129 | MeasureCalcRuleCode | MEASURE_CALC_RULE_CODE | — | — |
| 130 | RequestContext | REQUEST_CONTEXT | — | — |

### [[hrg_goal_measurements|HRG_GOAL_MEASUREMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MeasurementPEOAchievedWeight | ACHIEVED_WEIGHT | — | — |
| 2 | MeasurementPEOActualValue | ACTUAL_VALUE | — | ✅ |
| 3 | MeasurementPEOBusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 4 | MeasurementPEOComments | COMMENTS | — | ✅ |
| 5 | MeasurementPEOCreatedBy3 | CREATED_BY | — | — |
| 6 | MeasurementPEOCreationDate3 | CREATION_DATE | — | — |
| 7 | MeasurementPEODisplaySequence | DISPLAY_SEQUENCE | — | — |
| 8 | MeasurementPEOEndDate | END_DATE | — | — |
| 9 | MeasurementPEOGoalId2 | GOAL_ID | — | — |
| 10 | MeasurementPEOLastUpdateDate3 | LAST_UPDATE_DATE | — | — |
| 11 | MeasurementPEOLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 12 | MeasurementPEOLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 13 | MeasurementPEOMaxTarget | MAX_TARGET | — | — |
| 14 | MeasurementPEOMeasureTypeCode | MEASURE_TYPE_CODE | — | ✅ |
| 15 | MeasurementPEOMeasurementId | MEASUREMENT_ID | — | — |
| 16 | MeasurementPEOMeasurementName | MEASUREMENT_NAME | — | ✅ |
| 17 | MeasurementPEOMinTarget | MIN_TARGET | — | — |
| 18 | MeasurementPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 19 | MeasurementPEOStartDate | START_DATE | — | — |
| 20 | MeasurementPEOTargetPercentage | TARGET_PERCENTAGE | — | — |
| 21 | MeasurementPEOTargetType | TARGET_TYPE | — | ✅ |
| 22 | MeasurementPEOTargetValue | TARGET_VALUE | — | ✅ |
| 23 | MeasurementPEOUomCode | UOM_CODE | — | ✅ |

### [[hrg_goal_plan_goals|HRG_GOAL_PLAN_GOALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | EffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 5 | EffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 6 | GoalPEOGoalPlanId | GOAL_PLAN_ID | — | ✅ |
| 7 | GoalPEOWeighting | WEIGHTING | — | — |
| 8 | GoalPlanGoalId | GOAL_PLAN_GOAL_ID | — | — |
| 9 | GoalPlanGoalPEODisplaySequence | DISPLAY_SEQUENCE | — | — |
| 10 | GoalPlanGoalPEOGoalId | GOAL_ID | — | — |
| 11 | GoalPlanGoalPEORevPeriodId | REVIEW_PERIOD_ID | — | — |
| 12 | GoalPlanSetId | GOAL_PLAN_SET_ID | — | — |
| 13 | GoalPlanSetId1 | GOAL_PLAN_SET_ID | — | — |
| 14 | LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 15 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | PriorityCode | PRIORITY_CODE | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

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
| 67 | BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 68 | CreatedBy1 | CREATED_BY | — | — |
| 69 | CreationDate1 | CREATION_DATE | — | — |
| 70 | DisplayName | DISPLAY_NAME | — | — |
| 71 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 72 | EffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 73 | FirstName | FIRST_NAME | — | — |
| 74 | FullName | FULL_NAME | — | — |
| 75 | Honors | HONORS | — | — |
| 76 | KnownAs | KNOWN_AS | — | — |
| 77 | LastName | LAST_NAME | — | — |
| 78 | LastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 79 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 80 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 81 | LegislationCode | LEGISLATION_CODE | — | — |
| 82 | ListName | LIST_NAME | — | — |
| 83 | MiddleNames | MIDDLE_NAMES | — | — |
| 84 | MilitaryRank | MILITARY_RANK | — | — |
| 85 | NamInformation1 | NAM_INFORMATION1 | — | — |
| 86 | NamInformation10 | NAM_INFORMATION10 | — | — |
| 87 | NamInformation11 | NAM_INFORMATION11 | — | — |
| 88 | NamInformation12 | NAM_INFORMATION12 | — | — |
| 89 | NamInformation13 | NAM_INFORMATION13 | — | — |
| 90 | NamInformation14 | NAM_INFORMATION14 | — | — |
| 91 | NamInformation15 | NAM_INFORMATION15 | — | — |
| 92 | NamInformation16 | NAM_INFORMATION16 | — | — |
| 93 | NamInformation17 | NAM_INFORMATION17 | — | — |
| 94 | NamInformation18 | NAM_INFORMATION18 | — | — |
| 95 | NamInformation19 | NAM_INFORMATION19 | — | — |
| 96 | NamInformation2 | NAM_INFORMATION2 | — | — |
| 97 | NamInformation20 | NAM_INFORMATION20 | — | — |
| 98 | NamInformation21 | NAM_INFORMATION21 | — | — |
| 99 | NamInformation22 | NAM_INFORMATION22 | — | — |
| 100 | NamInformation23 | NAM_INFORMATION23 | — | — |
| 101 | NamInformation24 | NAM_INFORMATION24 | — | — |
| 102 | NamInformation25 | NAM_INFORMATION25 | — | — |
| 103 | NamInformation26 | NAM_INFORMATION26 | — | — |
| 104 | NamInformation27 | NAM_INFORMATION27 | — | — |
| 105 | NamInformation28 | NAM_INFORMATION28 | — | — |
| 106 | NamInformation29 | NAM_INFORMATION29 | — | — |
| 107 | NamInformation3 | NAM_INFORMATION3 | — | — |
| 108 | NamInformation30 | NAM_INFORMATION30 | — | — |
| 109 | NamInformation4 | NAM_INFORMATION4 | — | — |
| 110 | NamInformation5 | NAM_INFORMATION5 | — | — |
| 111 | NamInformation6 | NAM_INFORMATION6 | — | — |
| 112 | NamInformation7 | NAM_INFORMATION7 | — | — |
| 113 | NamInformation8 | NAM_INFORMATION8 | — | — |
| 114 | NamInformation9 | NAM_INFORMATION9 | — | — |
| 115 | NamInformationCategory | NAM_INFORMATION_CATEGORY | — | — |
| 116 | NameType | NAME_TYPE | — | — |
| 117 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 118 | OrderName | ORDER_NAME | — | — |
| 119 | PersonId | PERSON_ID | — | — |
| 120 | PersonNameId | PERSON_NAME_ID | — | — |
| 121 | PreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 122 | PreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 123 | Suffix | SUFFIX | — | — |
| 124 | Title | TITLE | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
