---
id: DOC-HCM-PVO-TaskPVO
doc_type: system-doc
title: "TaskPVO — PVO Human Capital Management"
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
  - TaskPVO
  - taskpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaskPVO

## 📌 Visão Geral

Disponibiliza tarefas (ações) vinculadas a metas no Goal Management. Suporta rastreamento de planos de ação e atividades para cumprimento de objetivos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmGoalCoreAM.TaskPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 77 | 2 | 1 | 19 | 25% |

---

## 🔗 Tabelas Relacionadas

- [[hrg_goals|HRG_GOALS]] — 53 atributos (1 BICC)
- [[hrg_goal_actions|HRG_GOAL_ACTIONS]] — 24 atributos (1 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[hrg_goals|HRG_GOALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalPEOAccessToHierarchyFlag | ACCESS_TO_HIERARCHY_FLAG | — | — |
| 2 | GoalPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
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
| 17 | GoalPEOGoalId | GOAL_ID | — | — |
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
| 42 | GoalPEOReferenceContentItemId | REFERENCE_CONTENT_ITEM_ID | — | — |
| 43 | GoalPEOReferenceGoalId | REFERENCE_GOAL_ID | — | — |
| 44 | GoalPEORequesterPersonId | REQUESTER_PERSON_ID | — | — |
| 45 | GoalPEOStartDate | START_DATE | — | — |
| 46 | GoalPEOStatusCode | STATUS_CODE | — | — |
| 47 | GoalPEOSuccessCriteria | SUCCESS_CRITERIA | — | — |
| 48 | GoalPEOSuccessCriteriaText | SUCCESS_CRITERIA_TEXT | — | — |
| 49 | GoalPEOTargetCompletionDate | TARGET_COMPLETION_DATE | — | — |
| 50 | GoalPEOTargetType | TARGET_TYPE | — | — |
| 51 | GoalPEOTargetValue | TARGET_VALUE | — | — |
| 52 | GoalPEOUomCode | UOM_CODE | — | — |
| 53 | GoalPEOVersionDate | VERSION_DATE | — | — |

### [[hrg_goal_actions|HRG_GOAL_ACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalActionId | GOAL_ACTION_ID | 🔑 | ✅ |
| 2 | GoalActionPEOActionName | ACTION_NAME | — | ✅ |
| 3 | GoalActionPEOActionTypeCode | ACTION_TYPE_CODE | — | ✅ |
| 4 | GoalActionPEOActionUrl | ACTION_URL | — | ✅ |
| 5 | GoalActionPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
| 6 | GoalActionPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 7 | GoalActionPEOComments | COMMENTS | — | ✅ |
| 8 | GoalActionPEOCompletionStatus | COMPLETION_STATUS | — | — |
| 9 | GoalActionPEOCreatedBy | CREATED_BY | — | ✅ |
| 10 | GoalActionPEOCreationDate | CREATION_DATE | — | ✅ |
| 11 | GoalActionPEODescription | DESCRIPTION | — | — |
| 12 | GoalActionPEOGoalId | GOAL_ID | — | ✅ |
| 13 | GoalActionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | GoalActionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | GoalActionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | GoalActionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | GoalActionPEOPercentCompleteCode | PERCENT_COMPLETE_CODE | — | ✅ |
| 18 | GoalActionPEOPriorityCode | PRIORITY_CODE | — | ✅ |
| 19 | GoalActionPEOStartDate | START_DATE | — | ✅ |
| 20 | GoalActionPEOStatusCode | STATUS_CODE | — | ✅ |
| 21 | GoalActionPEOTargetCompletionDate | TARGET_COMPLETION_DATE | — | ✅ |
| 22 | GoalActionPEOTargetType | TARGET_TYPE | — | — |
| 23 | GoalActionPEOTargetValue | TARGET_VALUE | — | — |
| 24 | GoalActionPEOUomCode | UOM_CODE | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
