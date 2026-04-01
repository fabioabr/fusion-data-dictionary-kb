---
id: DOC-OTHER-PVO-GoalPlanGoalPVO
doc_type: system-doc
title: "GoalPlanGoalPVO — PVO Cross-Module"
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
  - GoalPlanGoalPVO
  - goalplangoalpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GoalPlanGoalPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Goal Plan Goal. Acessa as tabelas: HRG_GOAL_PLAN_GOALS, HRG_GOAL_PLN_ASSIGNMENTS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmGoalCoreAM.GoalPlanGoalPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 38 | 2 | 1 | 14 | 37% |

---

## 🔗 Tabelas Relacionadas

- [[hrg_goal_plan_goals|HRG_GOAL_PLAN_GOALS]] — 18 atributos (1 PKs, 7 BICC)
- [[hrg_goal_pln_assignments|HRG_GOAL_PLN_ASSIGNMENTS]] — 20 atributos (7 BICC)

---

## ⚙️ Atributos

### [[hrg_goal_plan_goals|HRG_GOAL_PLAN_GOALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalPlanGoalId | GOAL_PLAN_GOAL_ID | 🔑 | ✅ |
| 2 | GoalPlanGoalPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 3 | GoalPlanGoalPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | GoalPlanGoalPEOCreatedBy | CREATED_BY | — | — |
| 5 | GoalPlanGoalPEOCreationDate | CREATION_DATE | — | — |
| 6 | GoalPlanGoalPEODisplaySequence | DISPLAY_SEQUENCE | — | — |
| 7 | GoalPlanGoalPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 8 | GoalPlanGoalPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 9 | GoalPlanGoalPEOGoalId | GOAL_ID | — | — |
| 10 | GoalPlanGoalPEOGoalPlanId | GOAL_PLAN_ID | — | ✅ |
| 11 | GoalPlanGoalPEOGoalPlanSetId | GOAL_PLAN_SET_ID | — | — |
| 12 | GoalPlanGoalPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | GoalPlanGoalPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | GoalPlanGoalPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | GoalPlanGoalPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | GoalPlanGoalPEOPriorityCode | PRIORITY_CODE | — | ✅ |
| 17 | GoalPlanGoalPEORevPeriodId | REVIEW_PERIOD_ID | — | — |
| 18 | GoalPlanGoalPEOWeighting | WEIGHTING | — | ✅ |

### [[hrg_goal_pln_assignments|HRG_GOAL_PLN_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalPlanAssgPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 2 | GoalPlanAssgPEOBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 3 | GoalPlanAssgPEOCreatedBy1 | CREATED_BY | — | — |
| 4 | GoalPlanAssgPEOCreationDate1 | CREATION_DATE | — | — |
| 5 | GoalPlanAssgPEOGoalPlanAssignmentId | GOAL_PLAN_ASSIGNMENT_ID | — | — |
| 6 | GoalPlanAssgPEOGoalPlanEndDate | GOAL_PLAN_END_DATE | — | ✅ |
| 7 | GoalPlanAssgPEOGoalPlanId1 | GOAL_PLAN_ID | — | — |
| 8 | GoalPlanAssgPEOGoalPlanSetEndDate | GOAL_PLAN_SET_END_DATE | — | ✅ |
| 9 | GoalPlanAssgPEOGoalPlanSetId1 | GOAL_PLAN_SET_ID | — | — |
| 10 | GoalPlanAssgPEOGoalPlanSetStartDate | GOAL_PLAN_SET_START_DATE | — | ✅ |
| 11 | GoalPlanAssgPEOGoalPlanStartDate | GOAL_PLAN_START_DATE | — | ✅ |
| 12 | GoalPlanAssgPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 13 | GoalPlanAssgPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 14 | GoalPlanAssgPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 15 | GoalPlanAssgPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 16 | GoalPlanAssgPEOOrganizationId | ORGANIZATION_ID | — | — |
| 17 | GoalPlanAssgPEOPersonId | PERSON_ID | — | — |
| 18 | GoalPlanAssgPEORevPeriodId | REVIEW_PERIOD_ID | — | — |
| 19 | GoalPlanAssgPEOStatus | STATUS | — | ✅ |
| 20 | GoalPlanAssgPEOWeighting1 | WEIGHTING | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
