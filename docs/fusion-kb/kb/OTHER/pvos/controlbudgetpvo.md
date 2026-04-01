---
id: DOC-OTHER-PVO-ControlBudgetPVO
doc_type: system-doc
title: "ControlBudgetPVO — PVO Cross-Module"
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
  - ControlBudgetPVO
  - controlbudgetpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ControlBudgetPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Control Budget. Acessa as tabelas: PJF_PROJECTS_ALL_B, XCC_CONTROL_BUDGETS.

**Caminho:** `FscmTopModelAM.FinCcControlEnginePublicModelAM.ControlBudgetPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 50 | 2 | 1 | 12 | 24% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]] — 2 atributos
- [[xcc_control_budgets|XCC_CONTROL_BUDGETS]] — 48 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[pjf_projects_all_b|PJF_PROJECTS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectBaseProjectId | PROJECT_ID | — | — |
| 2 | ProjectBaseSegment1 | SEGMENT1 | — | — |

### [[xcc_control_budgets|XCC_CONTROL_BUDGETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ControlBudgetId | CONTROL_BUDGET_ID | 🔑 | ✅ |
| 2 | ControlBudgetUnsecuredAccountCreationAllowedFlag | ACCOUNT_CREATION_ALLOWED_FLAG | — | — |
| 3 | ControlBudgetUnsecuredAllowOverridesFlag | ALLOW_OVERRIDES_FLAG | — | — |
| 4 | ControlBudgetUnsecuredBalanceDecreasesAllowedFlag | BALANCE_DECREASES_ALLOWED_FLAG | — | — |
| 5 | ControlBudgetUnsecuredBalanceIncreasesAllowedFlag | BALANCE_INCREASES_ALLOWED_FLAG | — | — |
| 6 | ControlBudgetUnsecuredBdgAmtNotFoundResultCode | BDG_AMT_NOT_FOUND_RESULT_CODE | — | — |
| 7 | ControlBudgetUnsecuredBudgetChartOfAccountsId | BUDGET_CHART_OF_ACCOUNTS_ID | — | — |
| 8 | ControlBudgetUnsecuredBudgetManagerId | BUDGET_MANAGER_ID | — | — |
| 9 | ControlBudgetUnsecuredChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 10 | ControlBudgetUnsecuredControlLevelCode | CONTROL_LEVEL_CODE | — | ✅ |
| 11 | ControlBudgetUnsecuredCreatedBy | CREATED_BY | — | — |
| 12 | ControlBudgetUnsecuredCreationDate | CREATION_DATE | — | ✅ |
| 13 | ControlBudgetUnsecuredCurrencyCode | CURRENCY_CODE | — | ✅ |
| 14 | ControlBudgetUnsecuredDefaultRateType | DEFAULT_RATE_TYPE | — | — |
| 15 | ControlBudgetUnsecuredDescription | DESCRIPTION | — | ✅ |
| 16 | ControlBudgetUnsecuredEndDate | END_DATE | — | — |
| 17 | ControlBudgetUnsecuredEndEffPeriodNum | END_EFF_PERIOD_NUM | — | — |
| 18 | ControlBudgetUnsecuredEndPeriodName | END_PERIOD_NAME | — | — |
| 19 | ControlBudgetUnsecuredFundsReleaseTimeframe | FUNDS_RELEASE_TIMEFRAME | — | ✅ |
| 20 | ControlBudgetUnsecuredLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | ControlBudgetUnsecuredLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 22 | ControlBudgetUnsecuredLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 23 | ControlBudgetUnsecuredLedgerId | LEDGER_ID | — | — |
| 24 | ControlBudgetUnsecuredMaximumOverrideAmount | MAXIMUM_OVERRIDE_AMOUNT | — | — |
| 25 | ControlBudgetUnsecuredName | NAME | — | ✅ |
| 26 | ControlBudgetUnsecuredNegativeBalancesAllowedFlag | NEGATIVE_BALANCES_ALLOWED_FLAG | — | — |
| 27 | ControlBudgetUnsecuredObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 28 | ControlBudgetUnsecuredOverridesTakenNotifyFlag | OVERRIDES_TAKEN_NOTIFY_FLAG | — | — |
| 29 | ControlBudgetUnsecuredParentSourceSystem | PARENT_SOURCE_SYSTEM | — | — |
| 30 | ControlBudgetUnsecuredPeriodSetName | PERIOD_SET_NAME | — | — |
| 31 | ControlBudgetUnsecuredPeriodType | PERIOD_TYPE | — | — |
| 32 | ControlBudgetUnsecuredPjcContractId | PJC_CONTRACT_ID | — | — |
| 33 | ControlBudgetUnsecuredPreviousStatusCode | PREVIOUS_STATUS_CODE | — | — |
| 34 | ControlBudgetUnsecuredProjectId | PROJECT_ID | — | — |
| 35 | ControlBudgetUnsecuredRequestId | REQUEST_ID | — | — |
| 36 | ControlBudgetUnsecuredRuleSql | RULE_SQL | — | — |
| 37 | ControlBudgetUnsecuredSourceBudget | SOURCE_BUDGET | — | — |
| 38 | ControlBudgetUnsecuredSourceBudgetSystemCode | SOURCE_BUDGET_SYSTEM_CODE | — | ✅ |
| 39 | ControlBudgetUnsecuredStartDate | START_DATE | — | — |
| 40 | ControlBudgetUnsecuredStartEffPeriodNum | START_EFF_PERIOD_NUM | — | — |
| 41 | ControlBudgetUnsecuredStartPeriodName | START_PERIOD_NAME | — | — |
| 42 | ControlBudgetUnsecuredStatusCode | STATUS_CODE | — | ✅ |
| 43 | ControlBudgetUnsecuredToleranceAmount | TOLERANCE_AMOUNT | — | ✅ |
| 44 | ControlBudgetUnsecuredTolerancePercent | TOLERANCE_PERCENT | — | ✅ |
| 45 | ControlBudgetUnsecuredUomCode | UOM_CODE | — | — |
| 46 | MasterControlBudgetControlBudgetId | CONTROL_BUDGET_ID | — | — |
| 47 | MasterControlBudgetName | NAME | — | — |
| 48 | NoOverridesNotifyFlag | NO_OVERRIDES_NOTIFY_FLAG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
