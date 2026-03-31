---
id: DOC-OTHER-PVO-CstPerpavgCostExtractPVO
doc_type: system-doc
title: "CstPerpavgCostExtractPVO — PVO Cross-Module"
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
  - CstPerpavgCostExtractPVO
  - cstperpavgcostextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstPerpavgCostExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Perpavg Cost Extract. Acessa as tabelas: CST_PERPAVG_COST.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstPerpavgCostExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 1 | 1 | 26 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_perpavg_cost|CST_PERPAVG_COST]] — 26 atributos (1 PKs, 26 BICC)

---

## ⚙️ Atributos

### [[cst_perpavg_cost|CST_PERPAVG_COST]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstPerpavgCostPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 2 | CstPerpavgCostPEOCostDate | COST_DATE | — | ✅ |
| 3 | CstPerpavgCostPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 4 | CstPerpavgCostPEOCostEndDate | COST_END_DATE | — | ✅ |
| 5 | CstPerpavgCostPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 6 | CstPerpavgCostPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | CstPerpavgCostPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | CstPerpavgCostPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 9 | CstPerpavgCostPEODepTrxnId | DEP_TRXN_ID | — | ✅ |
| 10 | CstPerpavgCostPEOEffDate | EFF_DATE | — | ✅ |
| 11 | CstPerpavgCostPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 12 | CstPerpavgCostPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | CstPerpavgCostPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | CstPerpavgCostPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | CstPerpavgCostPEOPerpavgCostId | PERPAVG_COST_ID | 🔑 | ✅ |
| 16 | CstPerpavgCostPEOQuantityAdjust | QUANTITY_ADJUST | — | ✅ |
| 17 | CstPerpavgCostPEOQuantityNew | QUANTITY_NEW | — | ✅ |
| 18 | CstPerpavgCostPEOQuantityOnhand | QUANTITY_ONHAND | — | ✅ |
| 19 | CstPerpavgCostPEORecTrxnId | REC_TRXN_ID | — | ✅ |
| 20 | CstPerpavgCostPEOTransactionId | TRANSACTION_ID | — | ✅ |
| 21 | CstPerpavgCostPEOUnitCostAdjust | UNIT_COST_ADJUST | — | ✅ |
| 22 | CstPerpavgCostPEOUnitCostAverage | UNIT_COST_AVERAGE | — | ✅ |
| 23 | CstPerpavgCostPEOUnitCostNew | UNIT_COST_NEW | — | ✅ |
| 24 | CstPerpavgCostPEOUnitCostOnhand | UNIT_COST_ONHAND | — | ✅ |
| 25 | CstPerpavgCostPEOUomCode | UOM_CODE | — | ✅ |
| 26 | CstPerpavgCostPEOValUnitId | VAL_UNIT_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
