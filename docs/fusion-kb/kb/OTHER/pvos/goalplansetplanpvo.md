---
id: DOC-OTHER-PVO-GoalPlanSetPlanPVO
doc_type: system-doc
title: "GoalPlanSetPlanPVO — PVO Cross-Module"
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
  - GoalPlanSetPlanPVO
  - goalplansetplanpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GoalPlanSetPlanPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Goal Plan Set Plan. Acessa as tabelas: HRG_GOAL_PLAN_SET_PLANS, HRG_GOAL_PLN_ASSIGNMENTS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmGoalCoreAM.GoalPlanSetPlanPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 32 | 2 | 1 | 11 | 34% |

---

## 🔗 Tabelas Relacionadas

- [[hrg_goal_plan_set_plans|HRG_GOAL_PLAN_SET_PLANS]] — 12 atributos (1 PKs, 4 BICC)
- [[hrg_goal_pln_assignments|HRG_GOAL_PLN_ASSIGNMENTS]] — 20 atributos (7 BICC)

---

## ⚙️ Atributos

### [[hrg_goal_plan_set_plans|HRG_GOAL_PLAN_SET_PLANS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GoalPlanSetPlanId | GOAL_PLAN_SET_PLAN_ID | 🔑 | ✅ |
| 2 | GoalPlanSetPlanPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | GoalPlanSetPlanPEOCreatedBy | CREATED_BY | — | — |
| 4 | GoalPlanSetPlanPEOCreationDate | CREATION_DATE | — | — |
| 5 | GoalPlanSetPlanPEOGoalPlanId | GOAL_PLAN_ID | — | — |
| 6 | GoalPlanSetPlanPEOGoalPlanSetId | GOAL_PLAN_SET_ID | — | — |
| 7 | GoalPlanSetPlanPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | GoalPlanSetPlanPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | GoalPlanSetPlanPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | GoalPlanSetPlanPEOMassRequestId | MASS_REQUEST_ID | — | ✅ |
| 11 | GoalPlanSetPlanPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | GoalPlanSetPlanPEOWeighting | WEIGHTING | — | ✅ |

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
