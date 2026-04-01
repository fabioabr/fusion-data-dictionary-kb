---
id: DOC-OTHER-PVO-ControlBudgetExtractPVO
doc_type: system-doc
title: "ControlBudgetExtractPVO — PVO Cross-Module"
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
  - ControlBudgetExtractPVO
  - controlbudgetextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ControlBudgetExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Control Budget Extract. Acessa as tabelas: XCC_CONTROL_BUDGETS.

**Caminho:** `FscmTopModelAM.FinExtractAM.XccBiccExtractAM.ControlBudgetExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 71 | 1 | 1 | 42 | 59% |

---

## 🔗 Tabelas Relacionadas

- [[xcc_control_budgets|XCC_CONTROL_BUDGETS]] — 71 atributos (1 PKs, 42 BICC)

---

## ⚙️ Atributos

### [[xcc_control_budgets|XCC_CONTROL_BUDGETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllowOverridesFlag | ALLOW_OVERRIDES_FLAG | — | ✅ |
| 2 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 3 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 4 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 5 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 6 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 7 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 8 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 9 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 10 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 11 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 12 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 13 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 14 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 15 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 16 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 17 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 18 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 19 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 20 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 21 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 22 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 23 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 24 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 25 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 26 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 27 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 28 | BalanceDecreasesAllowedFlag | BALANCE_DECREASES_ALLOWED_FLAG | — | ✅ |
| 29 | BalanceIncreasesAllowedFlag | BALANCE_INCREASES_ALLOWED_FLAG | — | ✅ |
| 30 | BudgetChartOfAccountsId | BUDGET_CHART_OF_ACCOUNTS_ID | — | ✅ |
| 31 | BudgetManagerId | BUDGET_MANAGER_ID | — | ✅ |
| 32 | ChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | ✅ |
| 33 | ControlBudgetId | CONTROL_BUDGET_ID | 🔑 | ✅ |
| 34 | ControlLevelCode | CONTROL_LEVEL_CODE | — | ✅ |
| 35 | CreatedBy | CREATED_BY | — | ✅ |
| 36 | CreationDate | CREATION_DATE | — | ✅ |
| 37 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 38 | DefaultRateType | DEFAULT_RATE_TYPE | — | ✅ |
| 39 | Description | DESCRIPTION | — | ✅ |
| 40 | EndDate | END_DATE | — | ✅ |
| 41 | EndEffPeriodNum | END_EFF_PERIOD_NUM | — | ✅ |
| 42 | EndPeriodName | END_PERIOD_NAME | — | ✅ |
| 43 | FundsReleaseTimeframe | FUNDS_RELEASE_TIMEFRAME | — | ✅ |
| 44 | FvTypeCode | FV_TYPE_CODE | — | — |
| 45 | InternalBudgetTypeCode | INTERNAL_BUDGET_TYPE_CODE | — | — |
| 46 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 47 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 48 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 49 | LedgerId | LEDGER_ID | — | ✅ |
| 50 | MaximumOverrideAmount | MAXIMUM_OVERRIDE_AMOUNT | — | ✅ |
| 51 | Name | NAME | — | ✅ |
| 52 | NegativeBalancesAllowedFlag | NEGATIVE_BALANCES_ALLOWED_FLAG | — | ✅ |
| 53 | NoOverridesNotifyFlag | NO_OVERRIDES_NOTIFY_FLAG | — | ✅ |
| 54 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 55 | OfflineReasonCode | OFFLINE_REASON_CODE | — | — |
| 56 | OverridesTakenNotifyFlag | OVERRIDES_TAKEN_NOTIFY_FLAG | — | ✅ |
| 57 | ParentSourceBudget | PARENT_SOURCE_BUDGET | — | ✅ |
| 58 | ParentSourceSystem | PARENT_SOURCE_SYSTEM | — | ✅ |
| 59 | PeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 60 | PeriodType | PERIOD_TYPE | — | ✅ |
| 61 | PjcContractId | PJC_CONTRACT_ID | — | ✅ |
| 62 | ProjectId | PROJECT_ID | — | ✅ |
| 63 | SourceBudget | SOURCE_BUDGET | — | ✅ |
| 64 | SourceBudgetSystemCode | SOURCE_BUDGET_SYSTEM_CODE | — | ✅ |
| 65 | StartDate | START_DATE | — | ✅ |
| 66 | StartEffPeriodNum | START_EFF_PERIOD_NUM | — | ✅ |
| 67 | StartPeriodName | START_PERIOD_NAME | — | ✅ |
| 68 | StatusCode | STATUS_CODE | — | ✅ |
| 69 | ToleranceAmount | TOLERANCE_AMOUNT | — | ✅ |
| 70 | TolerancePercent | TOLERANCE_PERCENT | — | ✅ |
| 71 | UomCode | UOM_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
