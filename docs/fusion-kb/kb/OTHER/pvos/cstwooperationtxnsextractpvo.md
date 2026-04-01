---
id: DOC-OTHER-PVO-CstWOOperationTxnsExtractPVO
doc_type: system-doc
title: "CstWOOperationTxnsExtractPVO — PVO Cross-Module"
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
  - CstWOOperationTxnsExtractPVO
  - cstwooperationtxnsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstWOOperationTxnsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst WOOperation Txns Extract. Acessa as tabelas: CST_WO_OPERATION_TXNS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstWOOperationTxnsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 1 | 1 | 29 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_wo_operation_txns|CST_WO_OPERATION_TXNS]] — 29 atributos (1 PKs, 29 BICC)

---

## ⚙️ Atributos

### [[cst_wo_operation_txns|CST_WO_OPERATION_TXNS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstWOOperationTxnsPEOBaseTxnActionId | BASE_TXN_ACTION_ID | — | ✅ |
| 2 | CstWOOperationTxnsPEOBaseTxnSourceTypeId | BASE_TXN_SOURCE_TYPE_ID | — | ✅ |
| 3 | CstWOOperationTxnsPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | ✅ |
| 4 | CstWOOperationTxnsPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | CstWOOperationTxnsPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | CstWOOperationTxnsPEOCstWoOperationTxnId | CST_WO_OPERATION_TXN_ID | 🔑 | ✅ |
| 7 | CstWOOperationTxnsPEOCstWorkOrderId | CST_WORK_ORDER_ID | — | ✅ |
| 8 | CstWOOperationTxnsPEOCstWorkOrderOperationId | CST_WORK_ORDER_OPERATION_ID | — | ✅ |
| 9 | CstWOOperationTxnsPEOExternalSystemRefId | EXTERNAL_SYSTEM_REF_ID | — | ✅ |
| 10 | CstWOOperationTxnsPEOExternalSystemReference | EXTERNAL_SYSTEM_REFERENCE | — | ✅ |
| 11 | CstWOOperationTxnsPEOFromDispatchState | FROM_DISPATCH_STATE | — | ✅ |
| 12 | CstWOOperationTxnsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 13 | CstWOOperationTxnsPEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | ✅ |
| 14 | CstWOOperationTxnsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | CstWOOperationTxnsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | CstWOOperationTxnsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | CstWOOperationTxnsPEOOperationSeqNumber | OPERATION_SEQ_NUMBER | — | ✅ |
| 18 | CstWOOperationTxnsPEOPrimaryQuantity | PRIMARY_QUANTITY | — | ✅ |
| 19 | CstWOOperationTxnsPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 20 | CstWOOperationTxnsPEOProcessedByCaFlag | PROCESSED_BY_CA_FLAG | — | ✅ |
| 21 | CstWOOperationTxnsPEOReasonCode | REASON_CODE | — | ✅ |
| 22 | CstWOOperationTxnsPEOToDispatchState | TO_DISPATCH_STATE | — | ✅ |
| 23 | CstWOOperationTxnsPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 24 | CstWOOperationTxnsPEOTransactionQuantity | TRANSACTION_QUANTITY | — | ✅ |
| 25 | CstWOOperationTxnsPEOTransactionTypeCode | TRANSACTION_TYPE_CODE | — | ✅ |
| 26 | CstWOOperationTxnsPEOTransactionUomCode | TRANSACTION_UOM_CODE | — | ✅ |
| 27 | CstWOOperationTxnsPEOWorkCenterId | WORK_CENTER_ID | — | ✅ |
| 28 | CstWOOperationTxnsPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 29 | CstWOOperationTxnsPEOWorkOrderOperationId | WORK_ORDER_OPERATION_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
