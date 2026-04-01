---
id: DOC-OTHER-PVO-CstOperationAdjTxnsExtractPVO
doc_type: system-doc
title: "CstOperationAdjTxnsExtractPVO — PVO Cross-Module"
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
  - CstOperationAdjTxnsExtractPVO
  - cstoperationadjtxnsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstOperationAdjTxnsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Operation Adj Txns Extract. Acessa as tabelas: CST_OPERATION_ADJ_TXNS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstOperationAdjTxnsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_operation_adj_txns|CST_OPERATION_ADJ_TXNS]] — 16 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[cst_operation_adj_txns|CST_OPERATION_ADJ_TXNS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstOperationAdjTxnsPEOAccountingStatus | ACCOUNTING_STATUS | — | ✅ |
| 2 | CstOperationAdjTxnsPEOBaseTxnActionId | BASE_TXN_ACTION_ID | — | ✅ |
| 3 | CstOperationAdjTxnsPEOBaseTxnSourceTypeId | BASE_TXN_SOURCE_TYPE_ID | — | ✅ |
| 4 | CstOperationAdjTxnsPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | ✅ |
| 5 | CstOperationAdjTxnsPEOCostDate | COST_DATE | — | ✅ |
| 6 | CstOperationAdjTxnsPEOCostingStatus | COSTING_STATUS | — | ✅ |
| 7 | CstOperationAdjTxnsPEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | CstOperationAdjTxnsPEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | CstOperationAdjTxnsPEOEffDate | EFF_DATE | — | ✅ |
| 10 | CstOperationAdjTxnsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | CstOperationAdjTxnsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | CstOperationAdjTxnsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | CstOperationAdjTxnsPEOOperationAdjTxnId | OPERATION_ADJ_TXN_ID | 🔑 | ✅ |
| 14 | CstOperationAdjTxnsPEOOperationTransactionId | OPERATION_TRANSACTION_ID | — | ✅ |
| 15 | CstOperationAdjTxnsPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 16 | CstOperationAdjTxnsPEOWoUpdateEventTxnId | WO_UPDATE_EVENT_TXN_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
