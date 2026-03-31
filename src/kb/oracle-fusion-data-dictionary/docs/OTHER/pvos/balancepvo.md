---
id: DOC-OTHER-PVO-BalancePVO
doc_type: system-doc
title: "BalancePVO — PVO Cross-Module"
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
  - BalancePVO
  - balancepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BalancePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Balance. Acessa as tabelas: XCC_BALANCES_V, XCC_CONTROL_BUDGETS.

**Caminho:** `FscmTopModelAM.FinCcControlEnginePublicModelAM.BalancePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 64 | 2 | 3 | 22 | 34% |

---

## 🔗 Tabelas Relacionadas

- [[xcc_balances_v|XCC_BALANCES_V]] — 25 atributos (3 PKs, 21 BICC)
- [[xcc_control_budgets|XCC_CONTROL_BUDGETS]] — 39 atributos (1 BICC)

---

## ⚙️ Atributos

### [[xcc_balances_v|XCC_BALANCES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BalanceAccountedPayablesAmount | ACCOUNTED_PAYABLES_AMOUNT | — | ✅ |
| 2 | BalanceAccountedProjectAmount | ACCOUNTED_PROJECT_AMOUNT | — | ✅ |
| 3 | BalanceAccountedReceiptsAmount | ACCOUNTED_RECEIPTS_AMOUNT | — | ✅ |
| 4 | BalanceActualAmount | ACTUAL_AMOUNT | — | ✅ |
| 5 | BalanceApprovedCommitmentAmount | APPROVED_COMMITMENT_AMOUNT | — | ✅ |
| 6 | BalanceApprovedObligationAmount | APPROVED_OBLIGATION_AMOUNT | — | ✅ |
| 7 | BalanceApprovedProjectAmount | APPROVED_PROJECT_AMOUNT | — | — |
| 8 | BalanceBudgetAdjustmentAmount | BUDGET_ADJUSTMENT_AMOUNT | — | ✅ |
| 9 | BalanceBudgetAmount | BUDGET_AMOUNT | — | ✅ |
| 10 | BalanceCommitmentAmount | COMMITMENT_AMOUNT | — | ✅ |
| 11 | BalanceCreatedBy | CREATED_BY | — | ✅ |
| 12 | BalanceCreationDate | CREATION_DATE | — | ✅ |
| 13 | BalanceDetailOtherAmount | DETAIL_OTHER_AMOUNT | — | ✅ |
| 14 | BalanceFundsAvailableAmount | FUNDS_AVAILABLE_AMOUNT | — | ✅ |
| 15 | BalanceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | BalanceLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | BalanceLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | BalanceMiscExpendituresAmount | MISC_EXPENDITURES_AMOUNT | — | ✅ |
| 19 | BalanceObligationAmount | OBLIGATION_AMOUNT | — | ✅ |
| 20 | BalanceOtherAmount | OTHER_AMOUNT | — | ✅ |
| 21 | BalanceUnreleasedBudgetAmount | UNRELEASED_BUDGET_AMOUNT | — | ✅ |
| 22 | BalanceValidatedPayablesAmount | VALIDATED_PAYABLES_AMOUNT | — | — |
| 23 | BudgetCcid | BUDGET_CCID | 🔑 | ✅ |
| 24 | ControlBudgetId | CONTROL_BUDGET_ID | 🔑 | ✅ |
| 25 | PeriodName | PERIOD_NAME | 🔑 | ✅ |

### [[xcc_control_budgets|XCC_CONTROL_BUDGETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ControlBudgetAccountCreationAllowedFlag | ACCOUNT_CREATION_ALLOWED_FLAG | — | — |
| 2 | ControlBudgetBalanceDecreasesAllowedFlag | BALANCE_DECREASES_ALLOWED_FLAG | — | — |
| 3 | ControlBudgetBalanceIncreasesAllowedFlag | BALANCE_INCREASES_ALLOWED_FLAG | — | — |
| 4 | ControlBudgetBdgAmtNotFoundResultCode | BDG_AMT_NOT_FOUND_RESULT_CODE | — | — |
| 5 | ControlBudgetBudgetChartOfAccountsId | BUDGET_CHART_OF_ACCOUNTS_ID | — | — |
| 6 | ControlBudgetBudgetManagerId | BUDGET_MANAGER_ID | — | — |
| 7 | ControlBudgetChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 8 | ControlBudgetControlBudgetId | CONTROL_BUDGET_ID | — | — |
| 9 | ControlBudgetControlLevelCode | CONTROL_LEVEL_CODE | — | — |
| 10 | ControlBudgetCreatedBy | CREATED_BY | — | — |
| 11 | ControlBudgetCreationDate | CREATION_DATE | — | — |
| 12 | ControlBudgetCurrencyCode | CURRENCY_CODE | — | — |
| 13 | ControlBudgetDefaultRateType | DEFAULT_RATE_TYPE | — | — |
| 14 | ControlBudgetDescription | DESCRIPTION | — | — |
| 15 | ControlBudgetEndDate | END_DATE | — | — |
| 16 | ControlBudgetEndEffPeriodNum | END_EFF_PERIOD_NUM | — | — |
| 17 | ControlBudgetEndPeriodName | END_PERIOD_NAME | — | — |
| 18 | ControlBudgetLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | ControlBudgetLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | ControlBudgetLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 21 | ControlBudgetLedgerId | LEDGER_ID | — | — |
| 22 | ControlBudgetName | NAME | — | — |
| 23 | ControlBudgetNegativeBalancesAllowedFlag | NEGATIVE_BALANCES_ALLOWED_FLAG | — | — |
| 24 | ControlBudgetObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 25 | ControlBudgetPcbdErrorCode | PCBD_ERROR_CODE | — | — |
| 26 | ControlBudgetPeriodSetName | PERIOD_SET_NAME | — | — |
| 27 | ControlBudgetPeriodType | PERIOD_TYPE | — | — |
| 28 | ControlBudgetPjcContractId | PJC_CONTRACT_ID | — | — |
| 29 | ControlBudgetProjectId | PROJECT_ID | — | — |
| 30 | ControlBudgetRequestId | REQUEST_ID | — | — |
| 31 | ControlBudgetSourceBudget | SOURCE_BUDGET | — | — |
| 32 | ControlBudgetSourceBudgetSystemCode | SOURCE_BUDGET_SYSTEM_CODE | — | — |
| 33 | ControlBudgetStartDate | START_DATE | — | — |
| 34 | ControlBudgetStartEffPeriodNum | START_EFF_PERIOD_NUM | — | — |
| 35 | ControlBudgetStartPeriodName | START_PERIOD_NAME | — | — |
| 36 | ControlBudgetStatusCode | STATUS_CODE | — | — |
| 37 | ControlBudgetToleranceAmount | TOLERANCE_AMOUNT | — | — |
| 38 | ControlBudgetTolerancePercent | TOLERANCE_PERCENT | — | — |
| 39 | ControlBudgetUomCode | UOM_CODE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
