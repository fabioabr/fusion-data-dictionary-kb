---
id: DOC-OTHER-PVO-CstLayerInventoryValuationExtractPVO
doc_type: system-doc
title: "CstLayerInventoryValuationExtractPVO — PVO Cross-Module"
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
  - CstLayerInventoryValuationExtractPVO
  - cstlayerinventoryvaluationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstLayerInventoryValuationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Layer Inventory Valuation Extract. Acessa as tabelas: CST_DEL_ONHAND_VALUATIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstLayerInventoryValuationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 1 | 1 | 28 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_del_onhand_valuations|CST_DEL_ONHAND_VALUATIONS]] — 28 atributos (1 PKs, 28 BICC)

---

## ⚙️ Atributos

### [[cst_del_onhand_valuations|CST_DEL_ONHAND_VALUATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstLayerInventoryValuationPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 2 | CstLayerInventoryValuationPEOCostMethodCode | COST_METHOD_CODE | — | ✅ |
| 3 | CstLayerInventoryValuationPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 4 | CstLayerInventoryValuationPEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 5 | CstLayerInventoryValuationPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | CstLayerInventoryValuationPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | CstLayerInventoryValuationPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 8 | CstLayerInventoryValuationPEOEndDate | END_DATE | — | ✅ |
| 9 | CstLayerInventoryValuationPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 10 | CstLayerInventoryValuationPEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 11 | CstLayerInventoryValuationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | CstLayerInventoryValuationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | CstLayerInventoryValuationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | CstLayerInventoryValuationPEOLocatorId | LOCATOR_ID | — | ✅ |
| 15 | CstLayerInventoryValuationPEOPeriodName | PERIOD_NAME | — | ✅ |
| 16 | CstLayerInventoryValuationPEOPerpAverageCost | PERP_AVERAGE_COST | — | ✅ |
| 17 | CstLayerInventoryValuationPEOPriorValuationId | PRIOR_VALUATION_ID | — | ✅ |
| 18 | CstLayerInventoryValuationPEOProjectId | PROJECT_ID | — | ✅ |
| 19 | CstLayerInventoryValuationPEOQuantityOnhand | QUANTITY_ONHAND | — | ✅ |
| 20 | CstLayerInventoryValuationPEORecTrxnId | REC_TRXN_ID | — | ✅ |
| 21 | CstLayerInventoryValuationPEOStandardCost | STANDARD_COST | — | ✅ |
| 22 | CstLayerInventoryValuationPEOStartDate | START_DATE | — | ✅ |
| 23 | CstLayerInventoryValuationPEOSubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 24 | CstLayerInventoryValuationPEOTaskId | TASK_ID | — | ✅ |
| 25 | CstLayerInventoryValuationPEOUnitCost | UNIT_COST | — | ✅ |
| 26 | CstLayerInventoryValuationPEOUomCode | UOM_CODE | — | ✅ |
| 27 | CstLayerInventoryValuationPEOValUnitId | VAL_UNIT_ID | — | ✅ |
| 28 | CstLayerInventoryValuationPEOValuationId | VALUATION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
