---
id: DOC-OTHER-PVO-GoalPlanSetPVO
doc_type: system-doc
title: "GoalPlanSetPVO — PVO Cross-Module"
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
  - GoalPlanSetPVO
  - goalplansetpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GoalPlanSetPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Goal Plan Set. Acessa as tabelas: HRG_GOAL_PLAN_SETS_B, HRG_GOAL_PLAN_SETS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmGoalCoreAM.GoalPlanSetPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 2 | 1 | 18 | 69% |

---

## 🔗 Tabelas Relacionadas

- [[hrg_goal_plan_sets_b|HRG_GOAL_PLAN_SETS_B]] — 14 atributos (1 PKs, 13 BICC)
- [[hrg_goal_plan_sets_tl|HRG_GOAL_PLAN_SETS_TL]] — 12 atributos (5 BICC)

---

## ⚙️ Atributos

### [[hrg_goal_plan_sets_b|HRG_GOAL_PLAN_SETS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalPlanSetBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 2 | GoalPlanSetBPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | GoalPlanSetBPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | GoalPlanSetBPEOEndDate | END_DATE | — | ✅ |
| 5 | GoalPlanSetBPEOGoalPlanSetActiveFlag | GOAL_PLAN_SET_ACTIVE_FLAG | — | ✅ |
| 6 | GoalPlanSetBPEOGoalPlanSetExtId | GOAL_PLAN_SET_EXT_ID | — | ✅ |
| 7 | GoalPlanSetBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | GoalPlanSetBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | GoalPlanSetBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | GoalPlanSetBPEOMassRequestId | MASS_REQUEST_ID | — | ✅ |
| 11 | GoalPlanSetBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | GoalPlanSetBPEORequestUiContextCode | REQUEST_UI_CONTEXT_CODE | — | ✅ |
| 13 | GoalPlanSetBPEOStartDate | START_DATE | — | ✅ |
| 14 | GoalPlanSetId | GOAL_PLAN_SET_ID | 🔑 | ✅ |

### [[hrg_goal_plan_sets_tl|HRG_GOAL_PLAN_SETS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalPlanSetTranslationPEOBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | GoalPlanSetTranslationPEOCreatedBy1 | CREATED_BY | — | — |
| 3 | GoalPlanSetTranslationPEOCreationDate1 | CREATION_DATE | — | — |
| 4 | GoalPlanSetTranslationPEODescription | DESCRIPTION | — | ✅ |
| 5 | GoalPlanSetTranslationPEOGoalPlanSetId1 | GOAL_PLAN_SET_ID | — | — |
| 6 | GoalPlanSetTranslationPEOGoalPlanSetName | GOAL_PLAN_SET_NAME | — | ✅ |
| 7 | GoalPlanSetTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 8 | GoalPlanSetTranslationPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 9 | GoalPlanSetTranslationPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 10 | GoalPlanSetTranslationPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 11 | GoalPlanSetTranslationPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 12 | GoalPlanSetTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
