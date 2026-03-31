---
id: DOC-OTHER-PVO-CstWriteoffCostsExtractPVO
doc_type: system-doc
title: "CstWriteoffCostsExtractPVO — PVO Cross-Module"
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
  - CstWriteoffCostsExtractPVO
  - cstwriteoffcostsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstWriteoffCostsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Writeoff Costs Extract. Acessa as tabelas: CST_WRITEOFF_COSTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstWriteoffCostsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 38 | 1 | 1 | 38 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_writeoff_costs|CST_WRITEOFF_COSTS]] — 38 atributos (1 PKs, 38 BICC)

---

## ⚙️ Atributos

### [[cst_writeoff_costs|CST_WRITEOFF_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstWriteoffCostsPEOAbsorptionType | ABSORPTION_TYPE | — | ✅ |
| 2 | CstWriteoffCostsPEOAdditionalProcessingCode | ADDITIONAL_PROCESSING_CODE | — | ✅ |
| 3 | CstWriteoffCostsPEOAdjPostedFlag | ADJ_POSTED_FLAG | — | ✅ |
| 4 | CstWriteoffCostsPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | ✅ |
| 5 | CstWriteoffCostsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 6 | CstWriteoffCostsPEOCostDate | COST_DATE | — | ✅ |
| 7 | CstWriteoffCostsPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 8 | CstWriteoffCostsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 9 | CstWriteoffCostsPEOCostReference | COST_REFERENCE | — | ✅ |
| 10 | CstWriteoffCostsPEOCostSource | COST_SOURCE | — | ✅ |
| 11 | CstWriteoffCostsPEOCostTransactionType | COST_TRANSACTION_TYPE | — | ✅ |
| 12 | CstWriteoffCostsPEOCreatedBy | CREATED_BY | — | ✅ |
| 13 | CstWriteoffCostsPEOCreationDate | CREATION_DATE | — | ✅ |
| 14 | CstWriteoffCostsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 15 | CstWriteoffCostsPEODepTrxnId | DEP_TRXN_ID | — | ✅ |
| 16 | CstWriteoffCostsPEODistributionId | DISTRIBUTION_ID | — | ✅ |
| 17 | CstWriteoffCostsPEODistributionType | DISTRIBUTION_TYPE | — | ✅ |
| 18 | CstWriteoffCostsPEOEffDate | EFF_DATE | — | ✅ |
| 19 | CstWriteoffCostsPEOExpensePoolId | EXPENSE_POOL_ID | — | ✅ |
| 20 | CstWriteoffCostsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 21 | CstWriteoffCostsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | CstWriteoffCostsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 23 | CstWriteoffCostsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | CstWriteoffCostsPEOOnhandQuantity | ONHAND_QUANTITY | — | ✅ |
| 25 | CstWriteoffCostsPEOOnhandValue | ONHAND_VALUE | — | ✅ |
| 26 | CstWriteoffCostsPEOOnhandValueStatusFlag | ONHAND_VALUE_STATUS_FLAG | — | ✅ |
| 27 | CstWriteoffCostsPEOPeriodName | PERIOD_NAME | — | ✅ |
| 28 | CstWriteoffCostsPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 29 | CstWriteoffCostsPEOQuantity | QUANTITY | — | ✅ |
| 30 | CstWriteoffCostsPEORecTrxnId | REC_TRXN_ID | — | ✅ |
| 31 | CstWriteoffCostsPEOTransactionCostId | TRANSACTION_COST_ID | — | ✅ |
| 32 | CstWriteoffCostsPEOTransactionId | TRANSACTION_ID | — | ✅ |
| 33 | CstWriteoffCostsPEOUnitCost | UNIT_COST | — | ✅ |
| 34 | CstWriteoffCostsPEOUomCode | UOM_CODE | — | ✅ |
| 35 | CstWriteoffCostsPEOValOnhandFlag | VAL_ONHAND_FLAG | — | ✅ |
| 36 | CstWriteoffCostsPEOValUnitId | VAL_UNIT_ID | — | ✅ |
| 37 | CstWriteoffCostsPEOWoCostPostedFlag | WO_COST_POSTED_FLAG | — | ✅ |
| 38 | CstWriteoffCostsPEOWriteoffCostId | WRITEOFF_COST_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
