---
id: DOC-OTHER-PVO-CstLayerValuationDetailsExtractPVO
doc_type: system-doc
title: "CstLayerValuationDetailsExtractPVO — PVO Cross-Module"
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
  - CstLayerValuationDetailsExtractPVO
  - cstlayervaluationdetailsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstLayerValuationDetailsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Layer Valuation Details Extract. Acessa as tabelas: CST_DEL_ONHAND_DETAILS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstLayerValuationDetailsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 1 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_del_onhand_details|CST_DEL_ONHAND_DETAILS]] — 22 atributos (1 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[cst_del_onhand_details|CST_DEL_ONHAND_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstLayerValuationDetailsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 2 | CstLayerValuationDetailsPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 3 | CstLayerValuationDetailsPEOCostMethodCode | COST_METHOD_CODE | — | ✅ |
| 4 | CstLayerValuationDetailsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 5 | CstLayerValuationDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | CstLayerValuationDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | CstLayerValuationDetailsPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 8 | CstLayerValuationDetailsPEOEndDate | END_DATE | — | ✅ |
| 9 | CstLayerValuationDetailsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 10 | CstLayerValuationDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | CstLayerValuationDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | CstLayerValuationDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | CstLayerValuationDetailsPEOPeriodName | PERIOD_NAME | — | ✅ |
| 14 | CstLayerValuationDetailsPEOPerpAverageCost | PERP_AVERAGE_COST | — | ✅ |
| 15 | CstLayerValuationDetailsPEOPriorValDetailId | PRIOR_VAL_DETAIL_ID | — | ✅ |
| 16 | CstLayerValuationDetailsPEORecTrxnId | REC_TRXN_ID | — | ✅ |
| 17 | CstLayerValuationDetailsPEOStandardCost | STANDARD_COST | — | ✅ |
| 18 | CstLayerValuationDetailsPEOStartDate | START_DATE | — | ✅ |
| 19 | CstLayerValuationDetailsPEOUnitCost | UNIT_COST | — | ✅ |
| 20 | CstLayerValuationDetailsPEOUomCode | UOM_CODE | — | ✅ |
| 21 | CstLayerValuationDetailsPEOValDetailId | VAL_DETAIL_ID | 🔑 | ✅ |
| 22 | CstLayerValuationDetailsPEOValUnitId | VAL_UNIT_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
