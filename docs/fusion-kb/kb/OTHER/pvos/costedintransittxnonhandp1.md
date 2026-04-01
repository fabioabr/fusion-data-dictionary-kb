---
id: DOC-OTHER-PVO-CostedIntransitTxnOnhandP1
doc_type: system-doc
title: "CostedIntransitTxnOnhandP1 — PVO Cross-Module"
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
  - CostedIntransitTxnOnhandP1
  - costedintransittxnonhandp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CostedIntransitTxnOnhandP1

## 📌 Visão Geral

View Object para extração BICC de dados de Costed Intransit Txn Onhand P1. Acessa as tabelas: CST_COSTED_INTR_TXN_ONHAND_V.

**Caminho:** `FscmTopModelAM.OnhandValuationAM.CostedIntransitTxnOnhandP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 7 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_costed_intr_txn_onhand_v|CST_COSTED_INTR_TXN_ONHAND_V]] — 12 atributos (7 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[cst_costed_intr_txn_onhand_v|CST_COSTED_INTR_TXN_ONHAND_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CITOPEOCostBookId | COST_BOOK_ID | 🔑 | ✅ |
| 2 | CITOPEOCostOrgId | COST_ORG_ID | 🔑 | ✅ |
| 3 | CITOPEOInventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 4 | CITOPEOInventoryOrgId | INVENTORY_ORG_ID | 🔑 | ✅ |
| 5 | CITOPEOSnapshotDate | SNAPSHOT_DATE | 🔑 | ✅ |
| 6 | CostedIntransitTxnOnhandPEOEffToDate | EFF_TO_DATE | — | ✅ |
| 7 | CostedIntransitTxnOnhandPEOExpenseTransactionFlag | EXPENSE_TRANSACTION_FLAG | — | ✅ |
| 8 | CostedIntransitTxnOnhandPEOQuantity | QUANTITY | — | ✅ |
| 9 | CostedIntransitTxnOnhandPEOTransactionFlowType | TRANSACTION_FLOW_TYPE | — | ✅ |
| 10 | CostedIntransitTxnOnhandPEOTxnSourceRefDocNumber | TXN_SOURCE_REF_DOC_NUMBER | 🔑 | ✅ |
| 11 | CostedIntransitTxnOnhandPEOTxnSourceRefDocType | TXN_SOURCE_REF_DOC_TYPE | 🔑 | ✅ |
| 12 | CostedIntransitTxnOnhandPEOUomCode | UOM_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
