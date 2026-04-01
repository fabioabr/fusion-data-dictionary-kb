---
id: DOC-OTHER-PVO-PerformanceGoalPlanPVO
doc_type: system-doc
title: "PerformanceGoalPlanPVO — PVO Cross-Module"
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
  - PerformanceGoalPlanPVO
  - performancegoalplanpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PerformanceGoalPlanPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Performance Goal Plan. Acessa as tabelas: HRG_GOAL_PLANS_B, HRG_GOAL_PLANS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmGoalCoreAM.PerformanceGoalPlanPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 42 | 2 | 1 | 30 | 71% |

---

## 🔗 Tabelas Relacionadas

- [[hrg_goal_plans_b|HRG_GOAL_PLANS_B]] — 30 atributos (1 PKs, 25 BICC)
- [[hrg_goal_plans_tl|HRG_GOAL_PLANS_TL]] — 12 atributos (5 BICC)

---

## ⚙️ Atributos

### [[hrg_goal_plans_b|HRG_GOAL_PLANS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalPlanBPEOAllDepartmentsFlag | ALL_DEPARTMENTS_FLAG | — | — |
| 2 | GoalPlanBPEOAllowPvtGoalMaxGoalFlag | ALLOW_PVT_GOAL_MAX_GOAL_FLAG | — | — |
| 3 | GoalPlanBPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 4 | GoalPlanBPEOAutoAssociateGoalFlag | AUTO_ASSOCIATE_GOAL_FLAG | — | ✅ |
| 5 | GoalPlanBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 6 | GoalPlanBPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | GoalPlanBPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | GoalPlanBPEOEnableWeightingFlag | ENABLE_WEIGHTING_FLAG | — | ✅ |
| 9 | GoalPlanBPEOEndDate | END_DATE | — | ✅ |
| 10 | GoalPlanBPEOEnforceGoalWeightFlag | ENFORCE_GOAL_WEIGHT_FLAG | — | ✅ |
| 11 | GoalPlanBPEOEnforceMaxGoalsInGpFlag | ENFORCE_MAX_GOALS_IN_GP_FLAG | — | — |
| 12 | GoalPlanBPEOEvaluationType | EVALUATION_TYPE | — | ✅ |
| 13 | GoalPlanBPEOGoalAccessLevelCode | GOAL_ACCESS_LEVEL_CODE | — | ✅ |
| 14 | GoalPlanBPEOGoalPlanActiveFlag | GOAL_PLAN_ACTIVE_FLAG | — | ✅ |
| 15 | GoalPlanBPEOGoalPlanExtId | GOAL_PLAN_EXT_ID | — | ✅ |
| 16 | GoalPlanBPEOGoalPlanTypeCode | GOAL_PLAN_TYPE_CODE | — | ✅ |
| 17 | GoalPlanBPEOGoalSubTypeCode | GOAL_SUB_TYPE_CODE | — | ✅ |
| 18 | GoalPlanBPEOIncludeInPerfdocFlag | INCLUDE_IN_PERFDOC_FLAG | — | ✅ |
| 19 | GoalPlanBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | GoalPlanBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 21 | GoalPlanBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 22 | GoalPlanBPEOMassRequestId | MASS_REQUEST_ID | — | ✅ |
| 23 | GoalPlanBPEOMaxGoalsNumInGoalPlan | MAX_GOALS_NUM_IN_GOAL_PLAN | — | — |
| 24 | GoalPlanBPEOMinGoalsNumInGoalPlan | MIN_GOALS_NUM_IN_GOAL_PLAN | — | — |
| 25 | GoalPlanBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 26 | GoalPlanBPEOPreviousGoalPlanId | PREVIOUS_GOAL_PLAN_ID | — | ✅ |
| 27 | GoalPlanBPEOPrimGoalPlanFlag | PRIMARY_GOAL_PLAN_FLAG | — | ✅ |
| 28 | GoalPlanBPEORequestUiContextCode | REQUEST_UI_CONTEXT_CODE | — | ✅ |
| 29 | GoalPlanBPEOStartDate | START_DATE | — | ✅ |
| 30 | GoalPlanId | GOAL_PLAN_ID | 🔑 | ✅ |

### [[hrg_goal_plans_tl|HRG_GOAL_PLANS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalPlanTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | GoalPlanTranslationPEOCreatedBy | CREATED_BY | — | — |
| 3 | GoalPlanTranslationPEOCreationDate | CREATION_DATE | — | — |
| 4 | GoalPlanTranslationPEODescription | DESCRIPTION | — | ✅ |
| 5 | GoalPlanTranslationPEOGoalPlanId | GOAL_PLAN_ID | — | — |
| 6 | GoalPlanTranslationPEOGoalPlanName | GOAL_PLAN_NAME | — | ✅ |
| 7 | GoalPlanTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 8 | GoalPlanTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | GoalPlanTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | GoalPlanTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | GoalPlanTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | GoalPlanTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
