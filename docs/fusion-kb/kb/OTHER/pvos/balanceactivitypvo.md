---
id: DOC-OTHER-PVO-BalanceActivityPVO
doc_type: system-doc
title: "BalanceActivityPVO — PVO Cross-Module"
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
  - BalanceActivityPVO
  - balanceactivitypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BalanceActivityPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Balance Activity. Acessa as tabelas: FUN_BU_PERF_V, GL_DAILY_CONVERSION_TYPES, GL_LEDGERS (+9).

**Caminho:** `FscmTopModelAM.FinCcControlEnginePublicModelAM.BalanceActivityPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 278 | 12 | 3 | 57 | 21% |

---

## 🔗 Tabelas Relacionadas

- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 2 atributos (1 BICC)
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 3 atributos
- [[gl_ledgers|GL_LEDGERS]] — 3 atributos (1 BICC)
- [[inv_units_of_measure_vl|INV_UNITS_OF_MEASURE_VL]] — 4 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 16 atributos (3 BICC)
- [[per_users|PER_USERS]] — 14 atributos
- [[xcc_balances_v|XCC_BALANCES_V]] — 23 atributos (1 BICC)
- [[xcc_balance_activities|XCC_BALANCE_ACTIVITIES]] — 40 atributos (3 PKs, 18 BICC)
- [[xcc_control_budgets|XCC_CONTROL_BUDGETS]] — 10 atributos (1 BICC)
- [[xcc_data_sets|XCC_DATA_SETS]] — 4 atributos (2 BICC)
- [[xcc_tr_headers|XCC_TR_HEADERS]] — 27 atributos (10 BICC)
- [[xcc_tr_lines|XCC_TR_LINES]] — 132 atributos (18 BICC)

---

## ⚙️ Atributos

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBuId | BU_ID | — | — |
| 2 | BusinessUnitName | BU_NAME | — | ✅ |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConversionType | CONVERSION_TYPE | — | — |
| 2 | GLDailyConversionTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | UserConversionType | USER_CONVERSION_TYPE | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgerCurrencyCode | CURRENCY_CODE | — | ✅ |
| 2 | LedgerId | LEDGER_ID | — | — |
| 3 | LedgerObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[inv_units_of_measure_vl|INV_UNITS_OF_MEASURE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UnitOfMeasureDescription | DESCRIPTION | — | ✅ |
| 3 | UnitOfMeasureUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 4 | UnitOfMeasureUomCode | UOM_CODE | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BalActPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | BalActPersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | BalActPersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | BalActPersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | BalActPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonNameDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | PersonNameEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonNameEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | PersonNameObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | PersonNamePersonId | PERSON_ID | — | — |
| 11 | PersonNamePersonNameId | PERSON_NAME_ID | — | — |
| 12 | TrHdrPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 13 | TrHdrPersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 14 | TrHdrPersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 15 | TrHdrPersonCreatedByPersonId | PERSON_ID | — | — |
| 16 | TrHdrPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BalActUserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | BalActUserCreatedByPersonId | PERSON_ID | — | — |
| 3 | BalActUserCreatedByUserGuid | USER_GUID | — | — |
| 4 | BalActUserCreatedByUserId | USER_ID | — | — |
| 5 | BalActUserCreatedByUsername | USERNAME | — | — |
| 6 | TrHdrUserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | TrHdrUserCreatedByPersonId | PERSON_ID | — | — |
| 8 | TrHdrUserCreatedByUserGuid | USER_GUID | — | — |
| 9 | TrHdrUserCreatedByUserId | USER_ID | — | — |
| 10 | TrHdrUserCreatedByUsername | USERNAME | — | — |
| 11 | UserObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | UserPersonId | PERSON_ID | — | — |
| 13 | UserUserGuid | USER_GUID | — | — |
| 14 | UserUserId | USER_ID | — | — |

### [[xcc_balances_v|XCC_BALANCES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BalancesAccountedPayablesAmount | ACCOUNTED_PAYABLES_AMOUNT | — | — |
| 2 | BalancesAccountedProjectAmount | ACCOUNTED_PROJECT_AMOUNT | — | — |
| 3 | BalancesAccountedReceiptsAmount | ACCOUNTED_RECEIPTS_AMOUNT | — | — |
| 4 | BalancesActualAmount | ACTUAL_AMOUNT | — | — |
| 5 | BalancesApprovedCommitmentAmount | APPROVED_COMMITMENT_AMOUNT | — | — |
| 6 | BalancesApprovedObligationAmount | APPROVED_OBLIGATION_AMOUNT | — | — |
| 7 | BalancesApprovedProjectAmount | APPROVED_PROJECT_AMOUNT | — | — |
| 8 | BalancesBudgetAmount | BUDGET_AMOUNT | — | — |
| 9 | BalancesBudgetCcid | BUDGET_CCID | — | — |
| 10 | BalancesCommitmentAmount | COMMITMENT_AMOUNT | — | — |
| 11 | BalancesControlBudgetId | CONTROL_BUDGET_ID | — | — |
| 12 | BalancesCreatedBy | CREATED_BY | — | — |
| 13 | BalancesCreationDate | CREATION_DATE | — | — |
| 14 | BalancesDetailOtherAmount | DETAIL_OTHER_AMOUNT | — | — |
| 15 | BalancesFundsAvailableAmount | FUNDS_AVAILABLE_AMOUNT | — | — |
| 16 | BalancesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | BalancesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | BalancesLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | BalancesMiscExpendituresAmount | MISC_EXPENDITURES_AMOUNT | — | — |
| 20 | BalancesObligationAmount | OBLIGATION_AMOUNT | — | — |
| 21 | BalancesOtherAmount | OTHER_AMOUNT | — | — |
| 22 | BalancesPeriodName | PERIOD_NAME | — | — |
| 23 | BalancesValidatedPayablesAmount | VALIDATED_PAYABLES_AMOUNT | — | — |

### [[xcc_balance_activities|XCC_BALANCE_ACTIVITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BalanceActivityActivityTypeCode | ACTIVITY_TYPE_CODE | — | ✅ |
| 2 | BalanceActivityActualAmount | ACTUAL_AMOUNT | — | — |
| 3 | BalanceActivityAllocHeaderNum | ALLOC_HEADER_NUM | — | — |
| 4 | BalanceActivityAllocLineNum | ALLOC_LINE_NUM | — | — |
| 5 | BalanceActivityAmount | AMOUNT | — | ✅ |
| 6 | BalanceActivityBackoutHeaderNum | BACKOUT_HEADER_NUM | — | — |
| 7 | BalanceActivityBackoutLineNum | BACKOUT_LINE_NUM | — | — |
| 8 | BalanceActivityBalanceTypeCode | BALANCE_TYPE_CODE | — | ✅ |
| 9 | BalanceActivityBudgetAmount | BUDGET_AMOUNT | — | — |
| 10 | BalanceActivityBudgetCcid | BUDGET_CCID | — | — |
| 11 | BalanceActivityBudgetDate | BUDGET_DATE | — | ✅ |
| 12 | BalanceActivityBurdenLineFlag | BURDEN_LINE_FLAG | — | ✅ |
| 13 | BalanceActivityCommitmentAmount | COMMITMENT_AMOUNT | — | — |
| 14 | BalanceActivityControlBudgetId | CONTROL_BUDGET_ID | — | — |
| 15 | BalanceActivityControlLevelCode | CONTROL_LEVEL_CODE | — | ✅ |
| 16 | BalanceActivityConversionRate | CONVERSION_RATE | — | — |
| 17 | BalanceActivityConversionTypeCode | CONVERSION_TYPE_CODE | — | — |
| 18 | BalanceActivityCreatedBy | CREATED_BY | — | ✅ |
| 19 | BalanceActivityCreationDate | CREATION_DATE | — | ✅ |
| 20 | BalanceActivityEnteredAmount | ENTERED_AMOUNT | — | ✅ |
| 21 | BalanceActivityEnteredCurrency | ENTERED_CURRENCY | — | ✅ |
| 22 | BalanceActivityFundsAvailableAmount | FUNDS_AVAILABLE_AMOUNT | — | — |
| 23 | BalanceActivityLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | BalanceActivityLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 25 | BalanceActivityLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 26 | BalanceActivityNetToleranceAmount | NET_TOLERANCE_AMOUNT | — | — |
| 27 | BalanceActivityObligationAmount | OBLIGATION_AMOUNT | — | — |
| 28 | BalanceActivityOtherAmount | OTHER_AMOUNT | — | — |
| 29 | BalanceActivityOtherLinesAmount | OTHER_LINES_AMOUNT | — | — |
| 30 | BalanceActivityOverrideClosedPeriodFlag | OVERRIDE_CLOSED_PERIOD_FLAG | — | ✅ |
| 31 | BalanceActivityOverrideFundsFlag | OVERRIDE_FUNDS_FLAG | — | ✅ |
| 32 | BalanceActivityPendingAmount | PENDING_AMOUNT | — | — |
| 33 | BalanceActivityPeriodName | PERIOD_NAME | — | — |
| 34 | BalanceActivityResultCode | RESULT_CODE | — | ✅ |
| 35 | BalanceActivitySubBalanceTypeCode | SUB_BALANCE_TYPE_CODE | — | — |
| 36 | BalanceActivityToleranceAmount | TOLERANCE_AMOUNT | — | ✅ |
| 37 | BalanceActivityTolerancePercent | TOLERANCE_PERCENT | — | — |
| 38 | BalanceLineOrder | BALANCE_LINE_ORDER | 🔑 | ✅ |
| 39 | HeaderNum | HEADER_NUM | 🔑 | ✅ |
| 40 | LineNum | LINE_NUM | 🔑 | ✅ |

### [[xcc_control_budgets|XCC_CONTROL_BUDGETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ControlBudgetBudgetChartOfAccountsId | BUDGET_CHART_OF_ACCOUNTS_ID | — | — |
| 2 | ControlBudgetChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 3 | ControlBudgetControlBudgetId | CONTROL_BUDGET_ID | — | — |
| 4 | ControlBudgetCurrencyCode | CURRENCY_CODE | — | ✅ |
| 5 | ControlBudgetFundsReleaseTimeframe | FUNDS_RELEASE_TIMEFRAME | — | — |
| 6 | ControlBudgetLedgerId | LEDGER_ID | — | — |
| 7 | ControlBudgetName | NAME | — | — |
| 8 | ControlBudgetObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ControlBudgetPjcContractId | PJC_CONTRACT_ID | — | — |
| 10 | ControlBudgetProjectId | PROJECT_ID | — | — |

### [[xcc_data_sets|XCC_DATA_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | XccDataSetsDataSetId | DATA_SET_ID | — | — |
| 2 | XccDataSetsOverrideFlag | OVERRIDE_FLAG | — | ✅ |
| 3 | XccDataSetsOverrideReason | OVERRIDE_REASON | — | ✅ |
| 4 | XccDataSetsOverrideUserGuid | OVERRIDE_USER_GUID | — | — |

### [[xcc_tr_headers|XCC_TR_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LiquidatedTransactionHeaderHeaderNum | HEADER_NUM | — | — |
| 2 | LiquidatedTransactionHeaderTransactionNumber | TRANSACTION_NUMBER | — | ✅ |
| 3 | TransactionHeaderArrivalOrder | ARRIVAL_ORDER | — | — |
| 4 | TransactionHeaderBudgetFlag | BUDGET_FLAG | — | — |
| 5 | TransactionHeaderBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 6 | TransactionHeaderCreatedBy | CREATED_BY | — | ✅ |
| 7 | TransactionHeaderCreationDate | CREATION_DATE | — | ✅ |
| 8 | TransactionHeaderDataSetId | DATA_SET_ID | — | — |
| 9 | TransactionHeaderDestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 10 | TransactionHeaderDocumentTypeCode | DOCUMENT_TYPE_CODE | — | — |
| 11 | TransactionHeaderDraftFlag | DRAFT_FLAG | — | ✅ |
| 12 | TransactionHeaderHeaderNum | HEADER_NUM | — | — |
| 13 | TransactionHeaderJeSourceCode | JE_SOURCE_CODE | — | — |
| 14 | TransactionHeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | TransactionHeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | TransactionHeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | TransactionHeaderLedgerId | LEDGER_ID | — | — |
| 18 | TransactionHeaderLiquidationDateCode | LIQUIDATION_DATE_CODE | — | — |
| 19 | TransactionHeaderOverrideFlag | OVERRIDE_FLAG | — | — |
| 20 | TransactionHeaderPartialReservationFlag | PARTIAL_RESERVATION_FLAG | — | ✅ |
| 21 | TransactionHeaderResultCode | RESULT_CODE | — | — |
| 22 | TransactionHeaderSourceActionCode | SOURCE_ACTION_CODE | — | ✅ |
| 23 | TransactionHeaderSourceHeaderId1 | SOURCE_HEADER_ID_1 | — | — |
| 24 | TransactionHeaderSourceHeaderId2 | SOURCE_HEADER_ID_2 | — | — |
| 25 | TransactionHeaderTransactionNumber | TRANSACTION_NUMBER | — | ✅ |
| 26 | TransactionHeaderTransactionSourceCode | TRANSACTION_SOURCE_CODE | — | — |
| 27 | TransactionHeaderTransactionTypeCode | TRANSACTION_TYPE_CODE | — | ✅ |

### [[xcc_tr_lines|XCC_TR_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LiquidationTransactionAccountingDate | ACCOUNTING_DATE | — | — |
| 2 | LiquidationTransactionBackedOutFlag | BACKED_OUT_FLAG | — | — |
| 3 | LiquidationTransactionBudgetCcid | BUDGET_CCID | — | — |
| 4 | LiquidationTransactionBudgetDate | BUDGET_DATE | — | — |
| 5 | LiquidationTransactionBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 6 | LiquidationTransactionCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 7 | LiquidationTransactionControlBudgetId | CONTROL_BUDGET_ID | — | — |
| 8 | LiquidationTransactionConversionDate | CONVERSION_DATE | — | — |
| 9 | LiquidationTransactionConversionTypeCode | CONVERSION_TYPE_CODE | — | — |
| 10 | LiquidationTransactionCreatedBy | CREATED_BY | — | — |
| 11 | LiquidationTransactionCreationDate | CREATION_DATE | — | — |
| 12 | LiquidationTransactionDataPurgedFlag | DATA_PURGED_FLAG | — | — |
| 13 | LiquidationTransactionDataSetId | DATA_SET_ID | — | — |
| 14 | LiquidationTransactionDraftFlag | DRAFT_FLAG | — | — |
| 15 | LiquidationTransactionEncumbranceTypeCode | ENCUMBRANCE_TYPE_CODE | — | — |
| 16 | LiquidationTransactionEnteredAmount | ENTERED_AMOUNT | — | — |
| 17 | LiquidationTransactionEnteredCurrency | ENTERED_CURRENCY | — | — |
| 18 | LiquidationTransactionHeaderNum1 | HEADER_NUM | — | — |
| 19 | LiquidationTransactionInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 20 | LiquidationTransactionJeCategoryCode | JE_CATEGORY_CODE | — | — |
| 21 | LiquidationTransactionJeSourceCode | JE_SOURCE_CODE | — | — |
| 22 | LiquidationTransactionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | LiquidationTransactionLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | LiquidationTransactionLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 25 | LiquidationTransactionLedgerAmount | LEDGER_AMOUNT | — | — |
| 26 | LiquidationTransactionLedgerId1 | LEDGER_ID | — | — |
| 27 | LiquidationTransactionLineGroupCode | LINE_GROUP_CODE | — | — |
| 28 | LiquidationTransactionLineNum1 | LINE_NUM | — | ✅ |
| 29 | LiquidationTransactionLiquidationAmount | LIQUIDATION_AMOUNT | — | — |
| 30 | LiquidationTransactionLiquidationDate | LIQUIDATION_DATE | — | — |
| 31 | LiquidationTransactionLiquidationDateCode | LIQUIDATION_DATE_CODE | — | — |
| 32 | LiquidationTransactionLiquidationLineId1 | LIQUIDATION_LINE_ID_1 | — | — |
| 33 | LiquidationTransactionLiquidationLineId2 | LIQUIDATION_LINE_ID_2 | — | — |
| 34 | LiquidationTransactionLiquidationLineId3 | LIQUIDATION_LINE_ID_3 | — | — |
| 35 | LiquidationTransactionLiquidationLineId4 | LIQUIDATION_LINE_ID_4 | — | — |
| 36 | LiquidationTransactionLiquidationLineId5 | LIQUIDATION_LINE_ID_5 | — | — |
| 37 | LiquidationTransactionLiquidationLineId6 | LIQUIDATION_LINE_ID_6 | — | — |
| 38 | LiquidationTransactionLiquidationQuantity | LIQUIDATION_QUANTITY | — | — |
| 39 | LiquidationTransactionLiquidationTransTypeCode | LIQUIDATION_TRANS_TYPE_CODE | — | — |
| 40 | LiquidationTransactionNeedsAccountFlag | NEEDS_ACCOUNT_FLAG | — | — |
| 41 | LiquidationTransactionNeedsResourceFlag | NEEDS_RESOURCE_FLAG | — | — |
| 42 | LiquidationTransactionOrderTypeInfo | ORDER_TYPE_INFO | — | — |
| 43 | LiquidationTransactionOverridableCode | OVERRIDABLE_CODE | — | — |
| 44 | LiquidationTransactionOverrideFlag | OVERRIDE_FLAG | — | — |
| 45 | LiquidationTransactionPartialReservationFlag | PARTIAL_RESERVATION_FLAG | — | — |
| 46 | LiquidationTransactionPjcBillableFlag | PJC_BILLABLE_FLAG | — | — |
| 47 | LiquidationTransactionPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | — |
| 48 | LiquidationTransactionPjcContractId | PJC_CONTRACT_ID | — | — |
| 49 | LiquidationTransactionPjcContractLineId | PJC_CONTRACT_LINE_ID | — | — |
| 50 | LiquidationTransactionPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 51 | LiquidationTransactionPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | — |
| 52 | LiquidationTransactionPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | — |
| 53 | LiquidationTransactionPjcOrganizationId | PJC_ORGANIZATION_ID | — | — |
| 54 | LiquidationTransactionPjcProjectId | PJC_PROJECT_ID | — | — |
| 55 | LiquidationTransactionPjcResourceId | PJC_RESOURCE_ID | — | — |
| 56 | LiquidationTransactionPjcTaskId | PJC_TASK_ID | — | — |
| 57 | LiquidationTransactionPjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |
| 58 | LiquidationTransactionPrice | PRICE | — | — |
| 59 | LiquidationTransactionQuantity | QUANTITY | — | — |
| 60 | LiquidationTransactionResultCode | RESULT_CODE | — | — |
| 61 | LiquidationTransactionSourceLineId1 | SOURCE_LINE_ID_1 | — | — |
| 62 | LiquidationTransactionSourceLineId2 | SOURCE_LINE_ID_2 | — | — |
| 63 | LiquidationTransactionSourceLineId3 | SOURCE_LINE_ID_3 | — | — |
| 64 | LiquidationTransactionSourceLineId4 | SOURCE_LINE_ID_4 | — | — |
| 65 | LiquidationTransactionSourceLineId5 | SOURCE_LINE_ID_5 | — | — |
| 66 | LiquidationTransactionSourceLineId6 | SOURCE_LINE_ID_6 | — | — |
| 67 | LiquidationTransactionSourceTransactionTypeCode | SOURCE_TRANSACTION_TYPE_CODE | — | — |
| 68 | LiquidationTransactionStatisticalAmount | STATISTICAL_AMOUNT | — | — |
| 69 | LiquidationTransactionTransactionSubtypeCode | TRANSACTION_SUBTYPE_CODE | — | — |
| 70 | LiquidationTransactionUomCode | UOM_CODE | — | — |
| 71 | LiquidationTransactionVendorId | VENDOR_ID | — | — |
| 72 | TransactionLineAccountingDate | ACCOUNTING_DATE | — | — |
| 73 | TransactionLineBackedOutFlag | BACKED_OUT_FLAG | — | — |
| 74 | TransactionLineBudgetCcid | BUDGET_CCID | — | — |
| 75 | TransactionLineBudgetDate | BUDGET_DATE | — | ✅ |
| 76 | TransactionLineBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 77 | TransactionLineCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 78 | TransactionLineControlBudgetId | CONTROL_BUDGET_ID | — | — |
| 79 | TransactionLineConversionDate | CONVERSION_DATE | — | ✅ |
| 80 | TransactionLineConversionTypeCode | CONVERSION_TYPE_CODE | — | ✅ |
| 81 | TransactionLineCreatedBy | CREATED_BY | — | — |
| 82 | TransactionLineCreationDate | CREATION_DATE | — | — |
| 83 | TransactionLineDataSetId | DATA_SET_ID | — | — |
| 84 | TransactionLineDraftFlag | DRAFT_FLAG | — | — |
| 85 | TransactionLineEncumbranceTypeCode | ENCUMBRANCE_TYPE_CODE | — | — |
| 86 | TransactionLineEnteredAmount | ENTERED_AMOUNT | — | ✅ |
| 87 | TransactionLineEnteredCurrency | ENTERED_CURRENCY | — | ✅ |
| 88 | TransactionLineHeaderNum | HEADER_NUM | — | — |
| 89 | TransactionLineJeCategoryCode | JE_CATEGORY_CODE | — | — |
| 90 | TransactionLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 91 | TransactionLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 92 | TransactionLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 93 | TransactionLineLedgerAmount | LEDGER_AMOUNT | — | ✅ |
| 94 | TransactionLineLedgerId | LEDGER_ID | — | — |
| 95 | TransactionLineLineGroupCode | LINE_GROUP_CODE | — | — |
| 96 | TransactionLineLineNum | LINE_NUM | — | — |
| 97 | TransactionLineLiquidationAmount | LIQUIDATION_AMOUNT | — | ✅ |
| 98 | TransactionLineLiquidationDate | LIQUIDATION_DATE | — | ✅ |
| 99 | TransactionLineLiquidationDateCode | LIQUIDATION_DATE_CODE | — | — |
| 100 | TransactionLineLiquidationLineId1 | LIQUIDATION_LINE_ID_1 | — | — |
| 101 | TransactionLineLiquidationLineId2 | LIQUIDATION_LINE_ID_2 | — | — |
| 102 | TransactionLineLiquidationLineId3 | LIQUIDATION_LINE_ID_3 | — | — |
| 103 | TransactionLineLiquidationLineId4 | LIQUIDATION_LINE_ID_4 | — | — |
| 104 | TransactionLineLiquidationLineId5 | LIQUIDATION_LINE_ID_5 | — | — |
| 105 | TransactionLineLiquidationLineId6 | LIQUIDATION_LINE_ID_6 | — | — |
| 106 | TransactionLineLiquidationQuantity | LIQUIDATION_QUANTITY | — | ✅ |
| 107 | TransactionLineLiquidationTransTypeCode | LIQUIDATION_TRANS_TYPE_CODE | — | ✅ |
| 108 | TransactionLinePartialReservationFlag | PARTIAL_RESERVATION_FLAG | — | — |
| 109 | TransactionLinePjcBillableFlag | PJC_BILLABLE_FLAG | — | — |
| 110 | TransactionLinePjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | — |
| 111 | TransactionLinePjcContractId | PJC_CONTRACT_ID | — | — |
| 112 | TransactionLinePjcContractLineId | PJC_CONTRACT_LINE_ID | — | — |
| 113 | TransactionLinePjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 114 | TransactionLinePjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | — |
| 115 | TransactionLinePjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | — |
| 116 | TransactionLinePjcOrganizationId | PJC_ORGANIZATION_ID | — | — |
| 117 | TransactionLinePjcProjectId | PJC_PROJECT_ID | — | — |
| 118 | TransactionLinePjcResourceId | PJC_RESOURCE_ID | — | — |
| 119 | TransactionLinePjcTaskId | PJC_TASK_ID | — | — |
| 120 | TransactionLinePjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |
| 121 | TransactionLinePrice | PRICE | — | ✅ |
| 122 | TransactionLineQuantity | QUANTITY | — | ✅ |
| 123 | TransactionLineResultCode | RESULT_CODE | — | — |
| 124 | TransactionLineSourceLineId1 | SOURCE_LINE_ID_1 | — | — |
| 125 | TransactionLineSourceLineId2 | SOURCE_LINE_ID_2 | — | — |
| 126 | TransactionLineSourceLineId3 | SOURCE_LINE_ID_3 | — | — |
| 127 | TransactionLineSourceLineId4 | SOURCE_LINE_ID_4 | — | — |
| 128 | TransactionLineSourceLineId5 | SOURCE_LINE_ID_5 | — | — |
| 129 | TransactionLineSourceTransactionTypeCode | SOURCE_TRANSACTION_TYPE_CODE | — | — |
| 130 | TransactionLineStatisticalAmount | STATISTICAL_AMOUNT | — | ✅ |
| 131 | TransactionLineTransactionSubtypeCode | TRANSACTION_SUBTYPE_CODE | — | ✅ |
| 132 | TransactionLineUomCode | UOM_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
