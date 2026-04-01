---
id: DOC-OTHER-PVO-ManagerBudgetsPVO
doc_type: system-doc
title: "ManagerBudgetsPVO — PVO Cross-Module"
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
  - ManagerBudgetsPVO
  - managerbudgetspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ManagerBudgetsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Manager Budgets. Acessa as tabelas: CMP_CWB_PERSON_INFO, CMP_PERSON_BUDGETS_V.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.CompensationAM.ManagerBudgetsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 50 | 2 | 1 | 39 | 78% |

---

## 🔗 Tabelas Relacionadas

- [[cmp_cwb_person_info|CMP_CWB_PERSON_INFO]] — 3 atributos
- [[cmp_person_budgets_v|CMP_PERSON_BUDGETS_V]] — 47 atributos (1 PKs, 39 BICC)

---

## ⚙️ Atributos

### [[cmp_cwb_person_info|CMP_CWB_PERSON_INFO]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonInfoPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 2 | PersonInfoPEOPersonEventId | PERSON_EVENT_ID | — | — |
| 3 | PersonInfoPEOPersonId | PERSON_ID | — | — |

### [[cmp_person_budgets_v|CMP_PERSON_BUDGETS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ManagerBudgetsPEOAccessCd | ACCESS_CD | — | ✅ |
| 2 | ManagerBudgetsPEOBudgetLastUpdDate | BUDGET_LAST_UPD_DATE | — | ✅ |
| 3 | ManagerBudgetsPEOBudgetPopCd | BUDGET_POP_CD | — | ✅ |
| 4 | ManagerBudgetsPEOBudgetValAmount | BUDGET_VAL_AMOUNT | — | — |
| 5 | ManagerBudgetsPEOBudgetValPercent | BUDGET_VAL_PERCENT | — | — |
| 6 | ManagerBudgetsPEOBudgetingStyle | BUDGETING_STYLE | — | ✅ |
| 7 | ManagerBudgetsPEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | ManagerBudgetsPEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | ManagerBudgetsPEODfltDistBudgetVal | DFLT_DIST_BUDGET_VAL | — | — |
| 10 | ManagerBudgetsPEODfltWsBudgetVal | DFLT_WS_BUDGET_VAL | — | — |
| 11 | ManagerBudgetsPEODistBudgetIssueDate | DIST_BUDGET_ISSUE_DATE | — | ✅ |
| 12 | ManagerBudgetsPEODistBudgetIssueVal | DIST_BUDGET_ISSUE_VAL | — | ✅ |
| 13 | ManagerBudgetsPEODistBudgetVal | DIST_BUDGET_VAL | — | ✅ |
| 14 | ManagerBudgetsPEODistBudgetValLastUpdBy | DIST_BUDGET_VAL_LAST_UPD_BY | — | ✅ |
| 15 | ManagerBudgetsPEODistBudgetValLastUpdDate | DIST_BUDGET_VAL_LAST_UPD_DATE | — | ✅ |
| 16 | ManagerBudgetsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | ManagerBudgetsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 18 | ManagerBudgetsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | ManagerBudgetsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | ManagerBudgetsPEOOverallBudgetAmount | OVERALL_BUDGET_AMOUNT | — | ✅ |
| 21 | ManagerBudgetsPEOOverrideOverAllocateCode | OVERRIDE_OVER_ALLOCATE_CODE | — | ✅ |
| 22 | ManagerBudgetsPEOOverrideOverBudgetCode | OVERRIDE_OVER_BUDGET_CODE | — | ✅ |
| 23 | ManagerBudgetsPEOPeriodId | PERIOD_ID | — | — |
| 24 | ManagerBudgetsPEOPlanId | PLAN_ID | — | — |
| 25 | ManagerBudgetsPEOPoolId | POOL_ID | — | — |
| 26 | ManagerBudgetsPEORecMnValAll | REC_MN_VAL_ALL | — | ✅ |
| 27 | ManagerBudgetsPEORecMxValAll | REC_MX_VAL_ALL | — | ✅ |
| 28 | ManagerBudgetsPEORecValAll | REC_VAL_ALL | — | ✅ |
| 29 | ManagerBudgetsPEOTotalDirectWorkers | TOTAL_DIRECT_WORKERS | — | ✅ |
| 30 | ManagerBudgetsPEOTotalEligibleSalary | TOTAL_ELIGIBLE_SALARY | — | ✅ |
| 31 | ManagerBudgetsPEOTotalEligibleWorkers | TOTAL_ELIGIBLE_WORKERS | — | ✅ |
| 32 | ManagerBudgetsPEOUsedBudget | USED_BUDGET | — | ✅ |
| 33 | ManagerBudgetsPEOUserPreferredExchangeRate | USER_PREFERRED_EXCHANGE_RATE | — | ✅ |
| 34 | ManagerBudgetsPEOWsBudgetIssueDate | WS_BUDGET_ISSUE_DATE | — | ✅ |
| 35 | ManagerBudgetsPEOWsBudgetIssueVal | WS_BUDGET_ISSUE_VAL | — | ✅ |
| 36 | ManagerBudgetsPEOWsBudgetVal | WS_BUDGET_VAL | — | ✅ |
| 37 | ManagerBudgetsPEOWsBudgetValLastUpdBy | WS_BUDGET_VAL_LAST_UPD_BY | — | ✅ |
| 38 | ManagerBudgetsPEOWsBudgetValLastUpdDate | WS_BUDGET_VAL_LAST_UPD_DATE | — | ✅ |
| 39 | PersonEventId | PERSON_EVENT_ID | 🔑 | ✅ |
| 40 | PublishedDistBudgetAmount | PUBLISHED_DIST_BUDGET_AMOUNT | — | ✅ |
| 41 | PublishedDistBudgetPct | PUBLISHED_DIST_BUDGET_PCT | — | ✅ |
| 42 | PublishedWsBudgetAmount | PUBLISHED_WS_BUDGET_AMOUNT | — | ✅ |
| 43 | PublishedWsBudgetPct | PUBLISHED_WS_BUDGET_PCT | — | ✅ |
| 44 | UnpublishedDistBudgetAmount | UNPUBLISHED_DIST_BUDGET_AMOUNT | — | ✅ |
| 45 | UnpublishedDistBudgetPct | UNPUBLISHED_DIST_BUDGET_PCT | — | ✅ |
| 46 | UnpublishedWsBudgetAmount | UNPUBLISHED_WS_BUDGET_AMOUNT | — | ✅ |
| 47 | UnpublishedWsBudgetPct | UNPUBLISHED_WS_BUDGET_PCT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
