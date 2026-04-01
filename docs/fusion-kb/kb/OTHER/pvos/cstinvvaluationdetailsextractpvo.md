---
id: DOC-OTHER-PVO-CstInvValuationDetailsExtractPVO
doc_type: system-doc
title: "CstInvValuationDetailsExtractPVO — PVO Cross-Module"
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
  - CstInvValuationDetailsExtractPVO
  - cstinvvaluationdetailsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstInvValuationDetailsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Inv Valuation Details Extract. Acessa as tabelas: CST_ATTR_ONHAND_DETAILS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstInvValuationDetailsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 43 | 1 | 1 | 43 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_attr_onhand_details|CST_ATTR_ONHAND_DETAILS]] — 43 atributos (1 PKs, 43 BICC)

---

## ⚙️ Atributos

### [[cst_attr_onhand_details|CST_ATTR_ONHAND_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstAttrOnhandDetailsPEOAcctdAmount | ACCTD_AMOUNT | — | ✅ |
| 2 | CstAttrOnhandDetailsPEOAcctdWriteoffAmount | ACCTD_WRITEOFF_AMOUNT | — | ✅ |
| 3 | CstAttrOnhandDetailsPEOAmount | AMOUNT | — | ✅ |
| 4 | CstAttrOnhandDetailsPEOAttrValuationId | ATTR_VALUATION_ID | — | ✅ |
| 5 | CstAttrOnhandDetailsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 6 | CstAttrOnhandDetailsPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 7 | CstAttrOnhandDetailsPEOCostMethodCode | COST_METHOD_CODE | — | ✅ |
| 8 | CstAttrOnhandDetailsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 9 | CstAttrOnhandDetailsPEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 10 | CstAttrOnhandDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 11 | CstAttrOnhandDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 12 | CstAttrOnhandDetailsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 13 | CstAttrOnhandDetailsPEOEndDate | END_DATE | — | ✅ |
| 14 | CstAttrOnhandDetailsPEOExclFromAcctgAmount | EXCL_FROM_ACCTG_AMOUNT | — | ✅ |
| 15 | CstAttrOnhandDetailsPEOExclFromAcctgWoAmount | EXCL_FROM_ACCTG_WO_AMOUNT | — | ✅ |
| 16 | CstAttrOnhandDetailsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 17 | CstAttrOnhandDetailsPEOInventoryOrgId | INVENTORY_ORG_ID | — | ✅ |
| 18 | CstAttrOnhandDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | CstAttrOnhandDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 20 | CstAttrOnhandDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 21 | CstAttrOnhandDetailsPEOLocatorId | LOCATOR_ID | — | ✅ |
| 22 | CstAttrOnhandDetailsPEONewIssueQuantity | NEW_ISSUE_QUANTITY | — | ✅ |
| 23 | CstAttrOnhandDetailsPEONewReceiptQuantity | NEW_RECEIPT_QUANTITY | — | ✅ |
| 24 | CstAttrOnhandDetailsPEOPeriodName | PERIOD_NAME | — | ✅ |
| 25 | CstAttrOnhandDetailsPEOPerpAverageCost | PERP_AVERAGE_COST | — | ✅ |
| 26 | CstAttrOnhandDetailsPEOPriorValDetailId | PRIOR_VAL_DETAIL_ID | — | ✅ |
| 27 | CstAttrOnhandDetailsPEOProjectId | PROJECT_ID | — | ✅ |
| 28 | CstAttrOnhandDetailsPEOQuantityOnhand | QUANTITY_ONHAND | — | ✅ |
| 29 | CstAttrOnhandDetailsPEOStandardCost | STANDARD_COST | — | ✅ |
| 30 | CstAttrOnhandDetailsPEOStartDate | START_DATE | — | ✅ |
| 31 | CstAttrOnhandDetailsPEOStartingQuantity | STARTING_QUANTITY | — | ✅ |
| 32 | CstAttrOnhandDetailsPEOSubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 33 | CstAttrOnhandDetailsPEOTaskId | TASK_ID | — | ✅ |
| 34 | CstAttrOnhandDetailsPEOUnitCost | UNIT_COST | — | ✅ |
| 35 | CstAttrOnhandDetailsPEOUomCode | UOM_CODE | — | ✅ |
| 36 | CstAttrOnhandDetailsPEOValDetailId | VAL_DETAIL_ID | 🔑 | ✅ |
| 37 | CstAttrOnhandDetailsPEOValUnitId | VAL_UNIT_ID | — | ✅ |
| 38 | CstAttrOnhandDetailsPEOVuAmount | VU_AMOUNT | — | ✅ |
| 39 | CstAttrOnhandDetailsPEOVuQuantityOnhand | VU_QUANTITY_ONHAND | — | ✅ |
| 40 | CstAttrOnhandDetailsPEOVuUnitCost | VU_UNIT_COST | — | ✅ |
| 41 | CstAttrOnhandDetailsPEOVuValuationId | VU_VALUATION_ID | — | ✅ |
| 42 | CstAttrOnhandDetailsPEOVuWriteoffAmount | VU_WRITEOFF_AMOUNT | — | ✅ |
| 43 | CstAttrOnhandDetailsPEOWriteoffAmount | WRITEOFF_AMOUNT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
