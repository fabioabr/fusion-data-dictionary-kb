---
id: DOC-OTHER-PVO-CstLayerCostsExtractPVO
doc_type: system-doc
title: "CstLayerCostsExtractPVO — PVO Cross-Module"
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
  - CstLayerCostsExtractPVO
  - cstlayercostsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstLayerCostsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Layer Costs Extract. Acessa as tabelas: CST_LAYER_COSTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstLayerCostsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 40 | 1 | 1 | 40 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_layer_costs|CST_LAYER_COSTS]] — 40 atributos (1 PKs, 40 BICC)

---

## ⚙️ Atributos

### [[cst_layer_costs|CST_LAYER_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstLayerCostsPEOAbsorptionType | ABSORPTION_TYPE | — | ✅ |
| 2 | CstLayerCostsPEOAdditionalProcessingCode | ADDITIONAL_PROCESSING_CODE | — | ✅ |
| 3 | CstLayerCostsPEOAdjPostedFlag | ADJ_POSTED_FLAG | — | ✅ |
| 4 | CstLayerCostsPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | ✅ |
| 5 | CstLayerCostsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 6 | CstLayerCostsPEOCostDate | COST_DATE | — | ✅ |
| 7 | CstLayerCostsPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 8 | CstLayerCostsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 9 | CstLayerCostsPEOCostReference | COST_REFERENCE | — | ✅ |
| 10 | CstLayerCostsPEOCostSource | COST_SOURCE | — | ✅ |
| 11 | CstLayerCostsPEOCostTransactionType | COST_TRANSACTION_TYPE | — | ✅ |
| 12 | CstLayerCostsPEOCreatedBy | CREATED_BY | — | ✅ |
| 13 | CstLayerCostsPEOCreationDate | CREATION_DATE | — | ✅ |
| 14 | CstLayerCostsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 15 | CstLayerCostsPEODepTrxnId | DEP_TRXN_ID | — | ✅ |
| 16 | CstLayerCostsPEODistributionId | DISTRIBUTION_ID | — | ✅ |
| 17 | CstLayerCostsPEODistributionType | DISTRIBUTION_TYPE | — | ✅ |
| 18 | CstLayerCostsPEOEffDate | EFF_DATE | — | ✅ |
| 19 | CstLayerCostsPEOExpensePoolId | EXPENSE_POOL_ID | — | ✅ |
| 20 | CstLayerCostsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 21 | CstLayerCostsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | CstLayerCostsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 23 | CstLayerCostsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | CstLayerCostsPEOLayerCostId | LAYER_COST_ID | 🔑 | ✅ |
| 25 | CstLayerCostsPEOOnhandQuantity | ONHAND_QUANTITY | — | ✅ |
| 26 | CstLayerCostsPEOOnhandValue | ONHAND_VALUE | — | ✅ |
| 27 | CstLayerCostsPEOOnhandValueStatusFlag | ONHAND_VALUE_STATUS_FLAG | — | ✅ |
| 28 | CstLayerCostsPEOPeriodName | PERIOD_NAME | — | ✅ |
| 29 | CstLayerCostsPEOPerpavgCostId | PERPAVG_COST_ID | — | ✅ |
| 30 | CstLayerCostsPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 31 | CstLayerCostsPEOQuantity | QUANTITY | — | ✅ |
| 32 | CstLayerCostsPEORecTrxnId | REC_TRXN_ID | — | ✅ |
| 33 | CstLayerCostsPEOStdCostId | STD_COST_ID | — | ✅ |
| 34 | CstLayerCostsPEOTransactionCostId | TRANSACTION_COST_ID | — | ✅ |
| 35 | CstLayerCostsPEOTransactionId | TRANSACTION_ID | — | ✅ |
| 36 | CstLayerCostsPEOUnitCost | UNIT_COST | — | ✅ |
| 37 | CstLayerCostsPEOUomCode | UOM_CODE | — | ✅ |
| 38 | CstLayerCostsPEOValOnhandFlag | VAL_ONHAND_FLAG | — | ✅ |
| 39 | CstLayerCostsPEOValUnitId | VAL_UNIT_ID | — | ✅ |
| 40 | CstLayerCostsPEOWoCostPostedFlag | WO_COST_POSTED_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
