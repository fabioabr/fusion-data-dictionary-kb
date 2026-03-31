---
id: DOC-OTHER-PVO-BalanceActivityExtractPVO
doc_type: system-doc
title: "BalanceActivityExtractPVO — PVO Cross-Module"
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
  - BalanceActivityExtractPVO
  - balanceactivityextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BalanceActivityExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Balance Activity Extract. Acessa as tabelas: XCC_BALANCE_ACTIVITIES.

**Caminho:** `FscmTopModelAM.FinExtractAM.XccBiccExtractAM.BalanceActivityExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 50 | 1 | 3 | 49 | 98% |

---

## 🔗 Tabelas Relacionadas

- [[xcc_balance_activities|XCC_BALANCE_ACTIVITIES]] — 50 atributos (3 PKs, 49 BICC)

---

## ⚙️ Atributos

### [[xcc_balance_activities|XCC_BALANCE_ACTIVITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActivityTypeCode | ACTIVITY_TYPE_CODE | — | ✅ |
| 2 | ActualAmount | ACTUAL_AMOUNT | — | ✅ |
| 3 | AllocHeaderNum | ALLOC_HEADER_NUM | — | ✅ |
| 4 | AllocLineNum | ALLOC_LINE_NUM | — | ✅ |
| 5 | Amount | AMOUNT | — | ✅ |
| 6 | BackoutHeaderNum | BACKOUT_HEADER_NUM | — | ✅ |
| 7 | BackoutLineNum | BACKOUT_LINE_NUM | — | ✅ |
| 8 | BalanceLineOrder | BALANCE_LINE_ORDER | 🔑 | ✅ |
| 9 | BalanceTypeCode | BALANCE_TYPE_CODE | — | ✅ |
| 10 | BudgetAdjustmentAmount | BUDGET_ADJUSTMENT_AMOUNT | — | ✅ |
| 11 | BudgetAmount | BUDGET_AMOUNT | — | ✅ |
| 12 | BudgetCcid | BUDGET_CCID | — | ✅ |
| 13 | BudgetDate | BUDGET_DATE | — | ✅ |
| 14 | BurdenLineFlag | BURDEN_LINE_FLAG | — | ✅ |
| 15 | CodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 16 | CommitmentAmount | COMMITMENT_AMOUNT | — | ✅ |
| 17 | ControlBudgetId | CONTROL_BUDGET_ID | — | ✅ |
| 18 | ControlLevelCode | CONTROL_LEVEL_CODE | — | ✅ |
| 19 | ConversionRate | CONVERSION_RATE | — | ✅ |
| 20 | ConversionTypeCode | CONVERSION_TYPE_CODE | — | ✅ |
| 21 | CreatedBy | CREATED_BY | — | ✅ |
| 22 | CreationDate | CREATION_DATE | — | ✅ |
| 23 | EnteredAmount | ENTERED_AMOUNT | — | ✅ |
| 24 | EnteredCurrency | ENTERED_CURRENCY | — | ✅ |
| 25 | EstimatedOverrideAmount | ESTIMATED_OVERRIDE_AMOUNT | — | ✅ |
| 26 | EstimatedToleranceAmount | ESTIMATED_TOLERANCE_AMOUNT | — | ✅ |
| 27 | FundsAvailableAmount | FUNDS_AVAILABLE_AMOUNT | — | ✅ |
| 28 | HeaderNum | HEADER_NUM | 🔑 | ✅ |
| 29 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 31 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 32 | LedgerAmount | LEDGER_AMOUNT | — | ✅ |
| 33 | LineNum | LINE_NUM | 🔑 | ✅ |
| 34 | NetToleranceAmount | NET_TOLERANCE_AMOUNT | — | ✅ |
| 35 | ObligationAmount | OBLIGATION_AMOUNT | — | ✅ |
| 36 | OtherAmount | OTHER_AMOUNT | — | ✅ |
| 37 | OtherLinesAmount | OTHER_LINES_AMOUNT | — | ✅ |
| 38 | OverrideClosedPeriodFlag | OVERRIDE_CLOSED_PERIOD_FLAG | — | ✅ |
| 39 | OverrideFundsFlag | OVERRIDE_FUNDS_FLAG | — | ✅ |
| 40 | PendingAmount | PENDING_AMOUNT | — | ✅ |
| 41 | PendingHeaderGroupAmount | PENDING_HEADER_GROUP_AMOUNT | — | — |
| 42 | PeriodChangeForUndoFlag | PERIOD_CHANGE_FOR_UNDO_FLAG | — | ✅ |
| 43 | PeriodName | PERIOD_NAME | — | ✅ |
| 44 | PjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | ✅ |
| 45 | PjcResourceId | PJC_RESOURCE_ID | — | ✅ |
| 46 | ProcessedForEssbaseFlag | PROCESSED_FOR_ESSBASE_FLAG | — | ✅ |
| 47 | ResultCode | RESULT_CODE | — | ✅ |
| 48 | SubBalanceTypeCode | SUB_BALANCE_TYPE_CODE | — | ✅ |
| 49 | ToleranceAmount | TOLERANCE_AMOUNT | — | ✅ |
| 50 | TolerancePercent | TOLERANCE_PERCENT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
