---
id: DOC-OTHER-PVO-CstWorkOrderCostsExtractPVO
doc_type: system-doc
title: "CstWorkOrderCostsExtractPVO — PVO Cross-Module"
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
  - CstWorkOrderCostsExtractPVO
  - cstworkordercostsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstWorkOrderCostsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Work Order Costs Extract. Acessa as tabelas: CST_WORK_ORDER_COSTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstWorkOrderCostsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 1 | 1 | 28 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_work_order_costs|CST_WORK_ORDER_COSTS]] — 28 atributos (1 PKs, 28 BICC)

---

## ⚙️ Atributos

### [[cst_work_order_costs|CST_WORK_ORDER_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstWorkOrderCostsPEOAbsorptionType | ABSORPTION_TYPE | — | ✅ |
| 2 | CstWorkOrderCostsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 3 | CstWorkOrderCostsPEOCostDate | COST_DATE | — | ✅ |
| 4 | CstWorkOrderCostsPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 5 | CstWorkOrderCostsPEOCostId | COST_ID | — | ✅ |
| 6 | CstWorkOrderCostsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 7 | CstWorkOrderCostsPEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | CstWorkOrderCostsPEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | CstWorkOrderCostsPEOCstWorkOrderId | CST_WORK_ORDER_ID | — | ✅ |
| 10 | CstWorkOrderCostsPEOCstWorkOrderOperationId | CST_WORK_ORDER_OPERATION_ID | — | ✅ |
| 11 | CstWorkOrderCostsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 12 | CstWorkOrderCostsPEOExpensePoolId | EXPENSE_POOL_ID | — | ✅ |
| 13 | CstWorkOrderCostsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 14 | CstWorkOrderCostsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | CstWorkOrderCostsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | CstWorkOrderCostsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | CstWorkOrderCostsPEOPoItemDescription | PO_ITEM_DESCRIPTION | — | ✅ |
| 18 | CstWorkOrderCostsPEOQuantity | QUANTITY | — | ✅ |
| 19 | CstWorkOrderCostsPEORecloseFlag | RECLOSE_FLAG | — | ✅ |
| 20 | CstWorkOrderCostsPEOResourceId | RESOURCE_ID | — | ✅ |
| 21 | CstWorkOrderCostsPEOSourceTable | SOURCE_TABLE | — | ✅ |
| 22 | CstWorkOrderCostsPEOTransactionId | TRANSACTION_ID | — | ✅ |
| 23 | CstWorkOrderCostsPEOUnitCost | UNIT_COST | — | ✅ |
| 24 | CstWorkOrderCostsPEOUomCode | UOM_CODE | — | ✅ |
| 25 | CstWorkOrderCostsPEOWipCostType | WIP_COST_TYPE | — | ✅ |
| 26 | CstWorkOrderCostsPEOWipTxnSign | WIP_TXN_SIGN | — | ✅ |
| 27 | CstWorkOrderCostsPEOWoCostAllocationBasis | WO_COST_ALLOCATION_BASIS | — | ✅ |
| 28 | CstWorkOrderCostsPEOWorkOrderCostId | WORK_ORDER_COST_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
