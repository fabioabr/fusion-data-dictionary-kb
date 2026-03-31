---
id: DOC-OTHER-PVO-CstTransferTransactionLayersExtractPVO
doc_type: system-doc
title: "CstTransferTransactionLayersExtractPVO — PVO Cross-Module"
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
  - CstTransferTransactionLayersExtractPVO
  - csttransfertransactionlayersextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstTransferTransactionLayersExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Transfer Transaction Layers Extract. Acessa as tabelas: CST_TRANSFERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstTransferTransactionLayersExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 1 | 3 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_transfers|CST_TRANSFERS]] — 21 atributos (3 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[cst_transfers|CST_TRANSFERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstTransferTransactionLayersPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 2 | CstTransferTransactionLayersPEOCostDate | COST_DATE | — | ✅ |
| 3 | CstTransferTransactionLayersPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 4 | CstTransferTransactionLayersPEOCostTransactionType | COST_TRANSACTION_TYPE | — | ✅ |
| 5 | CstTransferTransactionLayersPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | CstTransferTransactionLayersPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | CstTransferTransactionLayersPEODepTrxnId | DEP_TRXN_ID | 🔑 | ✅ |
| 8 | CstTransferTransactionLayersPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 9 | CstTransferTransactionLayersPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | CstTransferTransactionLayersPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | CstTransferTransactionLayersPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | CstTransferTransactionLayersPEOPeriodName | PERIOD_NAME | — | ✅ |
| 13 | CstTransferTransactionLayersPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 14 | CstTransferTransactionLayersPEOQuantity | QUANTITY | — | ✅ |
| 15 | CstTransferTransactionLayersPEORecTrxnId | REC_TRXN_ID | 🔑 | ✅ |
| 16 | CstTransferTransactionLayersPEOStagedForConvFlag | STAGED_FOR_CONV_FLAG | — | ✅ |
| 17 | CstTransferTransactionLayersPEOTransactionId | TRANSACTION_ID | 🔑 | ✅ |
| 18 | CstTransferTransactionLayersPEOTransferCostOrgId | TRANSFER_COST_ORG_ID | — | ✅ |
| 19 | CstTransferTransactionLayersPEOUomCode | UOM_CODE | — | ✅ |
| 20 | CstTransferTransactionLayersPEOValOnhandFlag | VAL_ONHAND_FLAG | — | ✅ |
| 21 | CstTransferTransactionLayersPEOValUnitId | VAL_UNIT_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
