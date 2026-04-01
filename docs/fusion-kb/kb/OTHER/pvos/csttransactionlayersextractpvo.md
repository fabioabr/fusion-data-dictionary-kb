---
id: DOC-OTHER-PVO-CstTransactionLayersExtractPVO
doc_type: system-doc
title: "CstTransactionLayersExtractPVO — PVO Cross-Module"
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
  - CstTransactionLayersExtractPVO
  - csttransactionlayersextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstTransactionLayersExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Transaction Layers Extract. Acessa as tabelas: CST_TRANSACTION_LAYERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstTransactionLayersExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 3 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_transaction_layers|CST_TRANSACTION_LAYERS]] — 22 atributos (3 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[cst_transaction_layers|CST_TRANSACTION_LAYERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstTransactionLayersPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 2 | CstTransactionLayersPEOCostDate | COST_DATE | — | ✅ |
| 3 | CstTransactionLayersPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 4 | CstTransactionLayersPEOCostTransactionType | COST_TRANSACTION_TYPE | — | ✅ |
| 5 | CstTransactionLayersPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | CstTransactionLayersPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | CstTransactionLayersPEODepTrxnId | DEP_TRXN_ID | 🔑 | ✅ |
| 8 | CstTransactionLayersPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 9 | CstTransactionLayersPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | CstTransactionLayersPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | CstTransactionLayersPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | CstTransactionLayersPEOPeriodName | PERIOD_NAME | — | ✅ |
| 13 | CstTransactionLayersPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 14 | CstTransactionLayersPEOQuantity | QUANTITY | — | ✅ |
| 15 | CstTransactionLayersPEOQuantityOnhand | QUANTITY_ONHAND | — | ✅ |
| 16 | CstTransactionLayersPEORecOnhand | REC_ONHAND | — | ✅ |
| 17 | CstTransactionLayersPEORecOnhandAvailFlag | REC_ONHAND_AVAIL_FLAG | — | ✅ |
| 18 | CstTransactionLayersPEORecTrxnId | REC_TRXN_ID | 🔑 | ✅ |
| 19 | CstTransactionLayersPEOTransactionId | TRANSACTION_ID | 🔑 | ✅ |
| 20 | CstTransactionLayersPEOUomCode | UOM_CODE | — | ✅ |
| 21 | CstTransactionLayersPEOValOnhandFlag | VAL_ONHAND_FLAG | — | ✅ |
| 22 | CstTransactionLayersPEOValUnitId | VAL_UNIT_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
