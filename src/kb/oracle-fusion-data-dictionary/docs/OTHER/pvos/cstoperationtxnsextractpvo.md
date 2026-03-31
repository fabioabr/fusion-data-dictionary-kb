---
id: DOC-OTHER-PVO-CstOperationTxnsExtractPVO
doc_type: system-doc
title: "CstOperationTxnsExtractPVO — PVO Cross-Module"
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
  - CstOperationTxnsExtractPVO
  - cstoperationtxnsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstOperationTxnsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Operation Txns Extract. Acessa as tabelas: CST_OPERATION_TRANSACTIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstOperationTxnsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 45 | 1 | 1 | 45 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_operation_transactions|CST_OPERATION_TRANSACTIONS]] — 45 atributos (1 PKs, 45 BICC)

---

## ⚙️ Atributos

### [[cst_operation_transactions|CST_OPERATION_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstOperationTxnsPEOAccountingStatus | ACCOUNTING_STATUS | — | ✅ |
| 2 | CstOperationTxnsPEOBaseTxnActionId | BASE_TXN_ACTION_ID | — | ✅ |
| 3 | CstOperationTxnsPEOBaseTxnSourceTypeId | BASE_TXN_SOURCE_TYPE_ID | — | ✅ |
| 4 | CstOperationTxnsPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | ✅ |
| 5 | CstOperationTxnsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 6 | CstOperationTxnsPEOCostDate | COST_DATE | — | ✅ |
| 7 | CstOperationTxnsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 8 | CstOperationTxnsPEOCostProfileId | COST_PROFILE_ID | — | ✅ |
| 9 | CstOperationTxnsPEOCostTransactionType | COST_TRANSACTION_TYPE | — | ✅ |
| 10 | CstOperationTxnsPEOCostingStatus | COSTING_STATUS | — | ✅ |
| 11 | CstOperationTxnsPEOCreatedBy | CREATED_BY | — | ✅ |
| 12 | CstOperationTxnsPEOCreationDate | CREATION_DATE | — | ✅ |
| 13 | CstOperationTxnsPEOCstWoOperationTxnId | CST_WO_OPERATION_TXN_ID | — | ✅ |
| 14 | CstOperationTxnsPEOCstWorkOrderId | CST_WORK_ORDER_ID | — | ✅ |
| 15 | CstOperationTxnsPEOCstWorkOrderOperationId | CST_WORK_ORDER_OPERATION_ID | — | ✅ |
| 16 | CstOperationTxnsPEOErrorCode | ERROR_CODE | — | ✅ |
| 17 | CstOperationTxnsPEOFromDispatchState | FROM_DISPATCH_STATE | — | ✅ |
| 18 | CstOperationTxnsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 19 | CstOperationTxnsPEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | ✅ |
| 20 | CstOperationTxnsPEOItemCostProfileId | ITEM_COST_PROFILE_ID | — | ✅ |
| 21 | CstOperationTxnsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | CstOperationTxnsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 23 | CstOperationTxnsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | CstOperationTxnsPEOLeTimezoneCode | LE_TIMEZONE_CODE | — | ✅ |
| 25 | CstOperationTxnsPEOOperationScrapCostType | OPERATION_SCRAP_COST_TYPE | — | ✅ |
| 26 | CstOperationTxnsPEOOperationScrapValuationType | OPERATION_SCRAP_VALUATION_TYPE | — | ✅ |
| 27 | CstOperationTxnsPEOOperationSeqNumber | OPERATION_SEQ_NUMBER | — | ✅ |
| 28 | CstOperationTxnsPEOOperationTransactionId | OPERATION_TRANSACTION_ID | 🔑 | ✅ |
| 29 | CstOperationTxnsPEOPeriodName | PERIOD_NAME | — | ✅ |
| 30 | CstOperationTxnsPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 31 | CstOperationTxnsPEOPreprocessingStatus | PREPROCESSING_STATUS | — | ✅ |
| 32 | CstOperationTxnsPEOPrimaryQuantity | PRIMARY_QUANTITY | — | ✅ |
| 33 | CstOperationTxnsPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 34 | CstOperationTxnsPEOProvisionalCompletionType | PROVISIONAL_COMPLETION_TYPE | — | ✅ |
| 35 | CstOperationTxnsPEOReasonCode | REASON_CODE | — | ✅ |
| 36 | CstOperationTxnsPEOToDispatchState | TO_DISPATCH_STATE | — | ✅ |
| 37 | CstOperationTxnsPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 38 | CstOperationTxnsPEOTransactionQuantity | TRANSACTION_QUANTITY | — | ✅ |
| 39 | CstOperationTxnsPEOTransactionUomCode | TRANSACTION_UOM_CODE | — | ✅ |
| 40 | CstOperationTxnsPEOTxnSourceDocNumber | TXN_SOURCE_DOC_NUMBER | — | ✅ |
| 41 | CstOperationTxnsPEOTxnSourceDocType | TXN_SOURCE_DOC_TYPE | — | ✅ |
| 42 | CstOperationTxnsPEOTxnSourceRefDocNumber | TXN_SOURCE_REF_DOC_NUMBER | — | ✅ |
| 43 | CstOperationTxnsPEOTxnSourceRefDocType | TXN_SOURCE_REF_DOC_TYPE | — | ✅ |
| 44 | CstOperationTxnsPEOWoUpdateEventTxnId | WO_UPDATE_EVENT_TXN_ID | — | ✅ |
| 45 | CstOperationTxnsPEOWorkCenterId | WORK_CENTER_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
