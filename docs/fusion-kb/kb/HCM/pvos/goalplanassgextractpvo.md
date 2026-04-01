---
id: DOC-HCM-PVO-GoalPlanAssgExtractPVO
doc_type: system-doc
title: "GoalPlanAssgExtractPVO — PVO Human Capital Management"
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
  - GoalPlanAssgExtractPVO
  - goalplanassgextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GoalPlanAssgExtractPVO

## 📌 Visão Geral

Extrai atribuições de planos de metas a colaboradores. Utilizado para rastrear quem está vinculado a cada plano de objetivos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.GoalBiccExtractAM.GoalPlanAssgExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 1 | 1 | 20 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hrg_goal_pln_assignments|HRG_GOAL_PLN_ASSIGNMENTS]] — 20 atributos (1 PKs, 20 BICC)

---

## ⚙️ Atributos

### [[hrg_goal_pln_assignments|HRG_GOAL_PLN_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentId | ASSIGNMENT_ID | — | ✅ |
| 2 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | GoalPlanAssignmentId | GOAL_PLAN_ASSIGNMENT_ID | 🔑 | ✅ |
| 6 | GoalPlanEndDate | GOAL_PLAN_END_DATE | — | ✅ |
| 7 | GoalPlanId | GOAL_PLAN_ID | — | ✅ |
| 8 | GoalPlanSetEndDate | GOAL_PLAN_SET_END_DATE | — | ✅ |
| 9 | GoalPlanSetId | GOAL_PLAN_SET_ID | — | ✅ |
| 10 | GoalPlanSetStartDate | GOAL_PLAN_SET_START_DATE | — | ✅ |
| 11 | GoalPlanStartDate | GOAL_PLAN_START_DATE | — | ✅ |
| 12 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 17 | PersonId | PERSON_ID | — | ✅ |
| 18 | ReviewPeriodId | REVIEW_PERIOD_ID | — | ✅ |
| 19 | Status | STATUS | — | ✅ |
| 20 | Weighting | WEIGHTING | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
