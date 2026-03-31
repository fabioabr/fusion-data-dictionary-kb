---
id: DOC-OTHER-PVO-CstOperationTxnCostsExtractPVO
doc_type: system-doc
title: "CstOperationTxnCostsExtractPVO — PVO Cross-Module"
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
  - CstOperationTxnCostsExtractPVO
  - cstoperationtxncostsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstOperationTxnCostsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Operation Txn Costs Extract. Acessa as tabelas: CST_OPERATION_TXN_COSTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstOperationTxnCostsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 1 | 1 | 28 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_operation_txn_costs|CST_OPERATION_TXN_COSTS]] — 28 atributos (1 PKs, 28 BICC)

---

## ⚙️ Atributos

### [[cst_operation_txn_costs|CST_OPERATION_TXN_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstOperationTxnCostsPEOAbsorptionType | ABSORPTION_TYPE | — | ✅ |
| 2 | CstOperationTxnCostsPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | ✅ |
| 3 | CstOperationTxnCostsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 4 | CstOperationTxnCostsPEOCostDate | COST_DATE | — | ✅ |
| 5 | CstOperationTxnCostsPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 6 | CstOperationTxnCostsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 7 | CstOperationTxnCostsPEOCostReference | COST_REFERENCE | — | ✅ |
| 8 | CstOperationTxnCostsPEOCostSource | COST_SOURCE | — | ✅ |
| 9 | CstOperationTxnCostsPEOCostTransactionType | COST_TRANSACTION_TYPE | — | ✅ |
| 10 | CstOperationTxnCostsPEOCreatedBy | CREATED_BY | — | ✅ |
| 11 | CstOperationTxnCostsPEOCreationDate | CREATION_DATE | — | ✅ |
| 12 | CstOperationTxnCostsPEOCstWorkOrderId | CST_WORK_ORDER_ID | — | ✅ |
| 13 | CstOperationTxnCostsPEOCstWorkOrderOperationId | CST_WORK_ORDER_OPERATION_ID | — | ✅ |
| 14 | CstOperationTxnCostsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 15 | CstOperationTxnCostsPEODistributionId | DISTRIBUTION_ID | — | ✅ |
| 16 | CstOperationTxnCostsPEOEffDate | EFF_DATE | — | ✅ |
| 17 | CstOperationTxnCostsPEOExpensePoolId | EXPENSE_POOL_ID | — | ✅ |
| 18 | CstOperationTxnCostsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 19 | CstOperationTxnCostsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | CstOperationTxnCostsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 21 | CstOperationTxnCostsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 22 | CstOperationTxnCostsPEOOperationAdjTxnId | OPERATION_ADJ_TXN_ID | — | ✅ |
| 23 | CstOperationTxnCostsPEOOperationTransactionId | OPERATION_TRANSACTION_ID | — | ✅ |
| 24 | CstOperationTxnCostsPEOOperationTxnCostId | OPERATION_TXN_COST_ID | 🔑 | ✅ |
| 25 | CstOperationTxnCostsPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 26 | CstOperationTxnCostsPEOQuantity | QUANTITY | — | ✅ |
| 27 | CstOperationTxnCostsPEOUnitCost | UNIT_COST | — | ✅ |
| 28 | CstOperationTxnCostsPEOUomCode | UOM_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
