---
id: DOC-OTHER-PVO-ManagerBudgetsForTopMgrPVO
doc_type: system-doc
title: "ManagerBudgetsForTopMgrPVO — PVO Cross-Module"
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
  - ManagerBudgetsForTopMgrPVO
  - managerbudgetsfortopmgrpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ManagerBudgetsForTopMgrPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Manager Budgets For Top Mgr. Acessa as tabelas: CMP_PERSON_BUDGETS_V.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.CompensationAM.ManagerBudgetsForTopMgrPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 47 | 1 | 1 | 23 | 49% |

---

## 🔗 Tabelas Relacionadas

- [[cmp_person_budgets_v|CMP_PERSON_BUDGETS_V]] — 47 atributos (1 PKs, 23 BICC)

---

## ⚙️ Atributos

### [[cmp_person_budgets_v|CMP_PERSON_BUDGETS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccessCd | ACCESS_CD | — | — |
| 2 | BudgetLastUpdDate | BUDGET_LAST_UPD_DATE | — | — |
| 3 | BudgetPopCd | BUDGET_POP_CD | — | — |
| 4 | BudgetValAmount | BUDGET_VAL_AMOUNT | — | — |
| 5 | BudgetValPercent | BUDGET_VAL_PERCENT | — | — |
| 6 | BudgetingStyle | BUDGETING_STYLE | — | — |
| 7 | CreatedBy | CREATED_BY | — | — |
| 8 | CreationDate | CREATION_DATE | — | — |
| 9 | DfltDistBudgetVal | DFLT_DIST_BUDGET_VAL | — | — |
| 10 | DfltWsBudgetVal | DFLT_WS_BUDGET_VAL | — | — |
| 11 | DistBudgetIssueDate | DIST_BUDGET_ISSUE_DATE | — | — |
| 12 | DistBudgetIssueVal | DIST_BUDGET_ISSUE_VAL | — | ✅ |
| 13 | DistBudgetVal | DIST_BUDGET_VAL | — | ✅ |
| 14 | DistBudgetValLastUpdBy | DIST_BUDGET_VAL_LAST_UPD_BY | — | — |
| 15 | DistBudgetValLastUpdDate | DIST_BUDGET_VAL_LAST_UPD_DATE | — | — |
| 16 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | OverallBudgetAmount | OVERALL_BUDGET_AMOUNT | — | ✅ |
| 21 | OverrideOverAllocateCode | OVERRIDE_OVER_ALLOCATE_CODE | — | — |
| 22 | OverrideOverBudgetCode | OVERRIDE_OVER_BUDGET_CODE | — | — |
| 23 | PeriodId | PERIOD_ID | — | — |
| 24 | PersonEventId | PERSON_EVENT_ID | 🔑 | ✅ |
| 25 | PlanId | PLAN_ID | — | — |
| 26 | PoolId | POOL_ID | — | — |
| 27 | PublishedDistBudgetAmount | PUBLISHED_DIST_BUDGET_AMOUNT | — | ✅ |
| 28 | PublishedDistBudgetPct | PUBLISHED_DIST_BUDGET_PCT | — | ✅ |
| 29 | PublishedWsBudgetAmount | PUBLISHED_WS_BUDGET_AMOUNT | — | ✅ |
| 30 | PublishedWsBudgetPct | PUBLISHED_WS_BUDGET_PCT | — | ✅ |
| 31 | RecMnValAll | REC_MN_VAL_ALL | — | ✅ |
| 32 | RecMxValAll | REC_MX_VAL_ALL | — | ✅ |
| 33 | RecValAll | REC_VAL_ALL | — | ✅ |
| 34 | TotalDirectWorkers | TOTAL_DIRECT_WORKERS | — | ✅ |
| 35 | TotalEligibleSalary | TOTAL_ELIGIBLE_SALARY | — | ✅ |
| 36 | TotalEligibleWorkers | TOTAL_ELIGIBLE_WORKERS | — | ✅ |
| 37 | UnpublishedDistBudgetAmount | UNPUBLISHED_DIST_BUDGET_AMOUNT | — | ✅ |
| 38 | UnpublishedDistBudgetPct | UNPUBLISHED_DIST_BUDGET_PCT | — | ✅ |
| 39 | UnpublishedWsBudgetAmount | UNPUBLISHED_WS_BUDGET_AMOUNT | — | ✅ |
| 40 | UnpublishedWsBudgetPct | UNPUBLISHED_WS_BUDGET_PCT | — | ✅ |
| 41 | UsedBudget | USED_BUDGET | — | ✅ |
| 42 | UserPreferredExchangeRate | USER_PREFERRED_EXCHANGE_RATE | — | ✅ |
| 43 | WsBudgetIssueDate | WS_BUDGET_ISSUE_DATE | — | — |
| 44 | WsBudgetIssueVal | WS_BUDGET_ISSUE_VAL | — | ✅ |
| 45 | WsBudgetVal | WS_BUDGET_VAL | — | ✅ |
| 46 | WsBudgetValLastUpdBy | WS_BUDGET_VAL_LAST_UPD_BY | — | — |
| 47 | WsBudgetValLastUpdDate | WS_BUDGET_VAL_LAST_UPD_DATE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
