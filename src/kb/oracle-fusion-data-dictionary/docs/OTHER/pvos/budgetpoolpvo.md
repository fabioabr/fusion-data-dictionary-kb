---
id: DOC-OTHER-PVO-BudgetPoolPVO
doc_type: system-doc
title: "BudgetPoolPVO — PVO Cross-Module"
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
  - BudgetPoolPVO
  - budgetpoolpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BudgetPoolPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Budget Pool. Acessa as tabelas: CMP_BUDGET_POOLS_B, CMP_BUDGET_POOLS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.CompensationAM.BudgetPoolPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 2 | 1 | 29 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cmp_budget_pools_b|CMP_BUDGET_POOLS_B]] — 18 atributos (1 PKs, 18 BICC)
- [[cmp_budget_pools_tl|CMP_BUDGET_POOLS_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[cmp_budget_pools_b|CMP_BUDGET_POOLS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BudgetPoolPEOAutoIssueFlag | AUTO_ISSUE_FLAG | — | ✅ |
| 2 | BudgetPoolPEOBudgetingStyle | BUDGETING_STYLE | — | ✅ |
| 3 | BudgetPoolPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | BudgetPoolPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | BudgetPoolPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | BudgetPoolPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | BudgetPoolPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | BudgetPoolPEONonMonetaryUom | NON_MONETARY_UOM | — | ✅ |
| 9 | BudgetPoolPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | BudgetPoolPEOOrderNum | ORDER_NUM | — | ✅ |
| 11 | BudgetPoolPEOOverAllocateTolerance | OVER_ALLOCATE_TOLERANCE | — | ✅ |
| 12 | BudgetPoolPEOOverBudgetTolerance | OVER_BUDGET_TOLERANCE | — | ✅ |
| 13 | BudgetPoolPEOPlanId | PLAN_ID | — | ✅ |
| 14 | BudgetPoolPEOPreventOverAllocateFlag | PREVENT_OVER_ALLOCATE_FLAG | — | ✅ |
| 15 | BudgetPoolPEOPreventOverBudgetFlag | PREVENT_OVER_BUDGET_FLAG | — | ✅ |
| 16 | BudgetPoolPEOPrimaryComponentId | PRIMARY_COMPONENT_ID | — | ✅ |
| 17 | BudgetPoolPEOSystemOrderNum | SYSTEM_ORDER_NUM | — | ✅ |
| 18 | PoolId | POOL_ID | 🔑 | ✅ |

### [[cmp_budget_pools_tl|CMP_BUDGET_POOLS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BudgetPoolTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | BudgetPoolTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | BudgetPoolTLPEOLanguage | LANGUAGE | — | ✅ |
| 4 | BudgetPoolTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | BudgetPoolTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | BudgetPoolTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | BudgetPoolTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | BudgetPoolTLPEOPoolId1 | POOL_ID | — | ✅ |
| 9 | BudgetPoolTLPEOPoolName | POOL_NAME | — | ✅ |
| 10 | BudgetPoolTLPEOSourceLang | SOURCE_LANG | — | ✅ |
| 11 | PlanId | PLAN_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
