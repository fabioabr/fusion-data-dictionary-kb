---
id: DOC-OTHER-PVO-CstInventoryValuationExtractPVO
doc_type: system-doc
title: "CstInventoryValuationExtractPVO — PVO Cross-Module"
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
  - CstInventoryValuationExtractPVO
  - cstinventoryvaluationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstInventoryValuationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Inventory Valuation Extract. Acessa as tabelas: CST_ATTR_ONHAND_VALUATIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstInventoryValuationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 41 | 1 | 1 | 41 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_attr_onhand_valuations|CST_ATTR_ONHAND_VALUATIONS]] — 41 atributos (1 PKs, 41 BICC)

---

## ⚙️ Atributos

### [[cst_attr_onhand_valuations|CST_ATTR_ONHAND_VALUATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstAttrOnhandValuationsPEOAcctdAmount | ACCTD_AMOUNT | — | ✅ |
| 2 | CstAttrOnhandValuationsPEOAcctdWriteoffAmount | ACCTD_WRITEOFF_AMOUNT | — | ✅ |
| 3 | CstAttrOnhandValuationsPEOAmount | AMOUNT | — | ✅ |
| 4 | CstAttrOnhandValuationsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 5 | CstAttrOnhandValuationsPEOCostMethodCode | COST_METHOD_CODE | — | ✅ |
| 6 | CstAttrOnhandValuationsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 7 | CstAttrOnhandValuationsPEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 8 | CstAttrOnhandValuationsPEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | CstAttrOnhandValuationsPEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | CstAttrOnhandValuationsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 11 | CstAttrOnhandValuationsPEOEndDate | END_DATE | — | ✅ |
| 12 | CstAttrOnhandValuationsPEOExclFromAcctgAmount | EXCL_FROM_ACCTG_AMOUNT | — | ✅ |
| 13 | CstAttrOnhandValuationsPEOExclFromAcctgWoAmount | EXCL_FROM_ACCTG_WO_AMOUNT | — | ✅ |
| 14 | CstAttrOnhandValuationsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 15 | CstAttrOnhandValuationsPEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 16 | CstAttrOnhandValuationsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | CstAttrOnhandValuationsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 18 | CstAttrOnhandValuationsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | CstAttrOnhandValuationsPEOLocatorId | LOCATOR_ID | — | ✅ |
| 20 | CstAttrOnhandValuationsPEONewIssueQuantity | NEW_ISSUE_QUANTITY | — | ✅ |
| 21 | CstAttrOnhandValuationsPEONewReceiptQuantity | NEW_RECEIPT_QUANTITY | — | ✅ |
| 22 | CstAttrOnhandValuationsPEOPeriodName | PERIOD_NAME | — | ✅ |
| 23 | CstAttrOnhandValuationsPEOPerpAverageCost | PERP_AVERAGE_COST | — | ✅ |
| 24 | CstAttrOnhandValuationsPEOPriorValuationId | PRIOR_VALUATION_ID | — | ✅ |
| 25 | CstAttrOnhandValuationsPEOProjectId | PROJECT_ID | — | ✅ |
| 26 | CstAttrOnhandValuationsPEOQuantityOnhand | QUANTITY_ONHAND | — | ✅ |
| 27 | CstAttrOnhandValuationsPEOStandardCost | STANDARD_COST | — | ✅ |
| 28 | CstAttrOnhandValuationsPEOStartDate | START_DATE | — | ✅ |
| 29 | CstAttrOnhandValuationsPEOStartingQuantity | STARTING_QUANTITY | — | ✅ |
| 30 | CstAttrOnhandValuationsPEOSubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 31 | CstAttrOnhandValuationsPEOTaskId | TASK_ID | — | ✅ |
| 32 | CstAttrOnhandValuationsPEOUnitCost | UNIT_COST | — | ✅ |
| 33 | CstAttrOnhandValuationsPEOUomCode | UOM_CODE | — | ✅ |
| 34 | CstAttrOnhandValuationsPEOValUnitId | VAL_UNIT_ID | — | ✅ |
| 35 | CstAttrOnhandValuationsPEOValuationId | VALUATION_ID | 🔑 | ✅ |
| 36 | CstAttrOnhandValuationsPEOVuAmount | VU_AMOUNT | — | ✅ |
| 37 | CstAttrOnhandValuationsPEOVuQuantityOnhand | VU_QUANTITY_ONHAND | — | ✅ |
| 38 | CstAttrOnhandValuationsPEOVuUnitCost | VU_UNIT_COST | — | ✅ |
| 39 | CstAttrOnhandValuationsPEOVuValuationId | VU_VALUATION_ID | — | ✅ |
| 40 | CstAttrOnhandValuationsPEOVuWriteoffAmount | VU_WRITEOFF_AMOUNT | — | ✅ |
| 41 | CstAttrOnhandValuationsPEOWriteoffAmount | WRITEOFF_AMOUNT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
