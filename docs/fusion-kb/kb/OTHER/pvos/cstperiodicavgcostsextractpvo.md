---
id: DOC-OTHER-PVO-CstPeriodicAvgCostsExtractPVO
doc_type: system-doc
title: "CstPeriodicAvgCostsExtractPVO — PVO Cross-Module"
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
  - CstPeriodicAvgCostsExtractPVO
  - cstperiodicavgcostsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstPeriodicAvgCostsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Periodic Avg Costs Extract. Acessa as tabelas: CST_PERIODIC_AVG_COSTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstPeriodicAvgCostsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 1 | 1 | 30 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_periodic_avg_costs|CST_PERIODIC_AVG_COSTS]] — 30 atributos (1 PKs, 30 BICC)

---

## ⚙️ Atributos

### [[cst_periodic_avg_costs|CST_PERIODIC_AVG_COSTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstPeriodicAvgCostPEOAdjustedPriorPeriodCost | ADJUSTED_PRIOR_PERIOD_COST | — | ✅ |
| 2 | CstPeriodicAvgCostPEOAdjustmentAmount | ADJUSTMENT_AMOUNT | — | ✅ |
| 3 | CstPeriodicAvgCostPEOCalculatedPeriodicAvgCost | CALCULATED_PERIODIC_AVG_COST | — | ✅ |
| 4 | CstPeriodicAvgCostPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 5 | CstPeriodicAvgCostPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 6 | CstPeriodicAvgCostPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 7 | CstPeriodicAvgCostPEOCostOwnedTxnAmount | COST_OWNED_TXN_AMOUNT | — | ✅ |
| 8 | CstPeriodicAvgCostPEOCostOwnedTxnQuantity | COST_OWNED_TXN_QUANTITY | — | ✅ |
| 9 | CstPeriodicAvgCostPEOCreatedBy | CREATED_BY | — | ✅ |
| 10 | CstPeriodicAvgCostPEOCreationDate | CREATION_DATE | — | ✅ |
| 11 | CstPeriodicAvgCostPEOCreationSource | CREATION_SOURCE | — | ✅ |
| 12 | CstPeriodicAvgCostPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 13 | CstPeriodicAvgCostPEOCurrentPeriodOnhand | CURRENT_PERIOD_ONHAND | — | ✅ |
| 14 | CstPeriodicAvgCostPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 15 | CstPeriodicAvgCostPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | CstPeriodicAvgCostPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | CstPeriodicAvgCostPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | CstPeriodicAvgCostPEONewCostElementFlag | NEW_COST_ELEMENT_FLAG | — | ✅ |
| 19 | CstPeriodicAvgCostPEOPeriodName | PERIOD_NAME | — | ✅ |
| 20 | CstPeriodicAvgCostPEOPeriodicAvgCost | PERIODIC_AVG_COST | — | ✅ |
| 21 | CstPeriodicAvgCostPEOPeriodicAvgCostAdjVariance | PERIODIC_AVG_COST_ADJ_VARIANCE | — | ✅ |
| 22 | CstPeriodicAvgCostPEOPeriodicCostId | PERIODIC_COST_ID | 🔑 | ✅ |
| 23 | CstPeriodicAvgCostPEOPriorPeriodCost | PRIOR_PERIOD_COST | — | ✅ |
| 24 | CstPeriodicAvgCostPEOPriorPeriodOnhand | PRIOR_PERIOD_ONHAND | — | ✅ |
| 25 | CstPeriodicAvgCostPEOPriorPeriodicCostId | PRIOR_PERIODIC_COST_ID | — | ✅ |
| 26 | CstPeriodicAvgCostPEOPropPacToNextPeriod | PROP_PAC_TO_NEXT_PERIOD | — | ✅ |
| 27 | CstPeriodicAvgCostPEOTxnAdjustmentAmount | TXN_ADJUSTMENT_AMOUNT | — | ✅ |
| 28 | CstPeriodicAvgCostPEOUomCode | UOM_CODE | — | ✅ |
| 29 | CstPeriodicAvgCostPEOValUnitId | VAL_UNIT_ID | — | ✅ |
| 30 | CstPeriodicAvgCostPEOValueAdjustmentAmount | VALUE_ADJUSTMENT_AMOUNT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
