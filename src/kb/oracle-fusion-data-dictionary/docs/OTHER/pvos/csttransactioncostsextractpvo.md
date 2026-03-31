---
id: DOC-OTHER-PVO-CstTransactionCostsExtractPVO
doc_type: system-doc
title: "CstTransactionCostsExtractPVO — PVO Cross-Module"
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
  - CstTransactionCostsExtractPVO
  - csttransactioncostsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstTransactionCostsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Transaction Costs Extract. Acessa as tabelas: CST_TRANSACTION_COSTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstTransactionCostsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 40 | 1 | 1 | 40 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_transaction_costs|CST_TRANSACTION_COSTS]] — 40 atributos (1 PKs, 40 BICC)

---

## ⚙️ Atributos

### [[cst_transaction_costs|CST_TRANSACTION_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstTransactionCostsPEOAbsorptionType | ABSORPTION_TYPE | — | ✅ |
| 2 | CstTransactionCostsPEOAccountingStatus | ACCOUNTING_STATUS | — | ✅ |
| 3 | CstTransactionCostsPEOAdjustmentDate | ADJUSTMENT_DATE | — | ✅ |
| 4 | CstTransactionCostsPEOAdjustmentTransactionId | ADJUSTMENT_TRANSACTION_ID | — | ✅ |
| 5 | CstTransactionCostsPEOBaseTxnActionId | BASE_TXN_ACTION_ID | — | ✅ |
| 6 | CstTransactionCostsPEOBaseTxnSourceTypeId | BASE_TXN_SOURCE_TYPE_ID | — | ✅ |
| 7 | CstTransactionCostsPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | ✅ |
| 8 | CstTransactionCostsPEOCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 9 | CstTransactionCostsPEOCostDate | COST_DATE | — | ✅ |
| 10 | CstTransactionCostsPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 11 | CstTransactionCostsPEOCostReference | COST_REFERENCE | — | ✅ |
| 12 | CstTransactionCostsPEOCostSource | COST_SOURCE | — | ✅ |
| 13 | CstTransactionCostsPEOCostedQty | COSTED_QTY | — | ✅ |
| 14 | CstTransactionCostsPEOCostingStatus | COSTING_STATUS | — | ✅ |
| 15 | CstTransactionCostsPEOCostingUomCode | COSTING_UOM_CODE | — | ✅ |
| 16 | CstTransactionCostsPEOCreatedBy | CREATED_BY | — | ✅ |
| 17 | CstTransactionCostsPEOCreationDate | CREATION_DATE | — | ✅ |
| 18 | CstTransactionCostsPEOCstInvTransactionId | CST_INV_TRANSACTION_ID | — | ✅ |
| 19 | CstTransactionCostsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 20 | CstTransactionCostsPEOEffDate | EFF_DATE | — | ✅ |
| 21 | CstTransactionCostsPEOExpensePoolId | EXPENSE_POOL_ID | — | ✅ |
| 22 | CstTransactionCostsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | CstTransactionCostsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 24 | CstTransactionCostsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | CstTransactionCostsPEOOverheadGroupId | OVERHEAD_GROUP_ID | — | ✅ |
| 26 | CstTransactionCostsPEOOverheadId | OVERHEAD_ID | — | ✅ |
| 27 | CstTransactionCostsPEOPeriodName | PERIOD_NAME | — | ✅ |
| 28 | CstTransactionCostsPEOPerpavgCostId | PERPAVG_COST_ID | — | ✅ |
| 29 | CstTransactionCostsPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 30 | CstTransactionCostsPEOQuantityOnhand | QUANTITY_ONHAND | — | ✅ |
| 31 | CstTransactionCostsPEOTransactionCostId | TRANSACTION_COST_ID | 🔑 | ✅ |
| 32 | CstTransactionCostsPEOTransactionId | TRANSACTION_ID | — | ✅ |
| 33 | CstTransactionCostsPEOTxnCurrencyCode | TXN_CURRENCY_CODE | — | ✅ |
| 34 | CstTransactionCostsPEOTxnCurrencyConversionDate | TXN_CURRENCY_CONVERSION_DATE | — | ✅ |
| 35 | CstTransactionCostsPEOTxnCurrencyConversionRate | TXN_CURRENCY_CONVERSION_RATE | — | ✅ |
| 36 | CstTransactionCostsPEOTxnCurrencyConversionType | TXN_CURRENCY_CONVERSION_TYPE | — | ✅ |
| 37 | CstTransactionCostsPEOTxnUnitCost | TXN_UNIT_COST | — | ✅ |
| 38 | CstTransactionCostsPEOUnitCost | UNIT_COST | — | ✅ |
| 39 | CstTransactionCostsPEOUserAdjustmentId | USER_ADJUSTMENT_ID | — | ✅ |
| 40 | CstTransactionCostsPEOValidCostFlag | VALID_COST_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
