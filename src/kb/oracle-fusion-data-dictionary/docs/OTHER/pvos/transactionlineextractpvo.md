---
id: DOC-OTHER-PVO-TransactionLineExtractPVO
doc_type: system-doc
title: "TransactionLineExtractPVO — PVO Cross-Module"
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
  - TransactionLineExtractPVO
  - transactionlineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction Line Extract. Acessa as tabelas: XCC_TR_LINES.

**Caminho:** `FscmTopModelAM.FinExtractAM.XccBiccExtractAM.TransactionLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 74 | 1 | 2 | 67 | 91% |

---

## 🔗 Tabelas Relacionadas

- [[xcc_tr_lines|XCC_TR_LINES]] — 74 atributos (2 PKs, 67 BICC)

---

## ⚙️ Atributos

### [[xcc_tr_lines|XCC_TR_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccountingDate | ACCOUNTING_DATE | — | ✅ |
| 2 | BackedOutFlag | BACKED_OUT_FLAG | — | ✅ |
| 3 | BudgetCcid | BUDGET_CCID | — | ✅ |
| 4 | BudgetDate | BUDGET_DATE | — | ✅ |
| 5 | BurdenFailureFlag | BURDEN_FAILURE_FLAG | — | — |
| 6 | BusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 7 | CashCodeCombinationId | CASH_CODE_COMBINATION_ID | — | — |
| 8 | CodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 9 | ControlBudgetId | CONTROL_BUDGET_ID | — | ✅ |
| 10 | ConversionDate | CONVERSION_DATE | — | ✅ |
| 11 | ConversionTypeCode | CONVERSION_TYPE_CODE | — | ✅ |
| 12 | CreatedBy | CREATED_BY | — | ✅ |
| 13 | CreationDate | CREATION_DATE | — | ✅ |
| 14 | DataPurgedFlag | DATA_PURGED_FLAG | — | ✅ |
| 15 | DataSetId | DATA_SET_ID | — | ✅ |
| 16 | DraftFlag | DRAFT_FLAG | — | ✅ |
| 17 | EncumbranceTypeCode | ENCUMBRANCE_TYPE_CODE | — | ✅ |
| 18 | EnteredAmount | ENTERED_AMOUNT | — | ✅ |
| 19 | EnteredCurrency | ENTERED_CURRENCY | — | ✅ |
| 20 | FailureReasonCode | FAILURE_REASON_CODE | — | — |
| 21 | HeaderNum | HEADER_NUM | 🔑 | ✅ |
| 22 | InventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 23 | JeCashAccountLineFlag | JE_CASH_ACCOUNT_LINE_FLAG | — | — |
| 24 | JeCategoryCode | JE_CATEGORY_CODE | — | ✅ |
| 25 | JeSourceCode | JE_SOURCE_CODE | — | ✅ |
| 26 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 27 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 28 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 29 | LedgerAmount | LEDGER_AMOUNT | — | ✅ |
| 30 | LedgerId | LEDGER_ID | — | ✅ |
| 31 | LineGroupCode | LINE_GROUP_CODE | — | ✅ |
| 32 | LineNum | LINE_NUM | 🔑 | ✅ |
| 33 | LiquidationAmount | LIQUIDATION_AMOUNT | — | ✅ |
| 34 | LiquidationDate | LIQUIDATION_DATE | — | ✅ |
| 35 | LiquidationDateCode | LIQUIDATION_DATE_CODE | — | ✅ |
| 36 | LiquidationLineId1 | LIQUIDATION_LINE_ID_1 | — | ✅ |
| 37 | LiquidationLineId2 | LIQUIDATION_LINE_ID_2 | — | ✅ |
| 38 | LiquidationLineId3 | LIQUIDATION_LINE_ID_3 | — | ✅ |
| 39 | LiquidationLineId4 | LIQUIDATION_LINE_ID_4 | — | ✅ |
| 40 | LiquidationLineId5 | LIQUIDATION_LINE_ID_5 | — | ✅ |
| 41 | LiquidationLineId6 | LIQUIDATION_LINE_ID_6 | — | ✅ |
| 42 | LiquidationQuantity | LIQUIDATION_QUANTITY | — | ✅ |
| 43 | LiquidationTransTypeCode | LIQUIDATION_TRANS_TYPE_CODE | — | ✅ |
| 44 | OrderTypeInfo | ORDER_TYPE_INFO | — | ✅ |
| 45 | OverridableCode | OVERRIDABLE_CODE | — | ✅ |
| 46 | OverrideFlag | OVERRIDE_FLAG | — | ✅ |
| 47 | PartialReservationFlag | PARTIAL_RESERVATION_FLAG | — | ✅ |
| 48 | PjcBillableFlag | PJC_BILLABLE_FLAG | — | ✅ |
| 49 | PjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | ✅ |
| 50 | PjcContractId | PJC_CONTRACT_ID | — | ✅ |
| 51 | PjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | ✅ |
| 52 | PjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | ✅ |
| 53 | PjcFundingSourceId | PJC_FUNDING_SOURCE_ID | — | — |
| 54 | PjcOrganizationId | PJC_ORGANIZATION_ID | — | ✅ |
| 55 | PjcProjectId | PJC_PROJECT_ID | — | ✅ |
| 56 | PjcResourceId | PJC_RESOURCE_ID | — | ✅ |
| 57 | PjcTaskId | PJC_TASK_ID | — | ✅ |
| 58 | PjcWorkTypeId | PJC_WORK_TYPE_ID | — | ✅ |
| 59 | Price | PRICE | — | ✅ |
| 60 | Quantity | QUANTITY | — | ✅ |
| 61 | ResultCode | RESULT_CODE | — | ✅ |
| 62 | RevenueCodeCombinationId | REVENUE_CODE_COMBINATION_ID | — | — |
| 63 | SourceLineId1 | SOURCE_LINE_ID_1 | — | ✅ |
| 64 | SourceLineId2 | SOURCE_LINE_ID_2 | — | ✅ |
| 65 | SourceLineId3 | SOURCE_LINE_ID_3 | — | ✅ |
| 66 | SourceLineId4 | SOURCE_LINE_ID_4 | — | ✅ |
| 67 | SourceLineId5 | SOURCE_LINE_ID_5 | — | ✅ |
| 68 | SourceLineId6 | SOURCE_LINE_ID_6 | — | ✅ |
| 69 | SourceTransactionTypeCode | SOURCE_TRANSACTION_TYPE_CODE | — | ✅ |
| 70 | StatisticalAmount | STATISTICAL_AMOUNT | — | ✅ |
| 71 | SuccessReasonCode | SUCCESS_REASON_CODE | — | — |
| 72 | TransactionSubtypeCode | TRANSACTION_SUBTYPE_CODE | — | ✅ |
| 73 | UomCode | UOM_CODE | — | ✅ |
| 74 | VendorId | VENDOR_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
