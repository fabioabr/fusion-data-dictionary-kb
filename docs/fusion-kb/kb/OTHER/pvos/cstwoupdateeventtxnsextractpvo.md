---
id: DOC-OTHER-PVO-CstWOUpdateEventTxnsExtractPVO
doc_type: system-doc
title: "CstWOUpdateEventTxnsExtractPVO — PVO Cross-Module"
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
  - CstWOUpdateEventTxnsExtractPVO
  - cstwoupdateeventtxnsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstWOUpdateEventTxnsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst WOUpdate Event Txns Extract. Acessa as tabelas: CST_WO_UPDATE_EVENT_TXNS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstWOUpdateEventTxnsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 44 | 1 | 1 | 44 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_wo_update_event_txns|CST_WO_UPDATE_EVENT_TXNS]] — 44 atributos (1 PKs, 44 BICC)

---

## ⚙️ Atributos

### [[cst_wo_update_event_txns|CST_WO_UPDATE_EVENT_TXNS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstWOUpdateEventTxnsPEOAccountingStatus | ACCOUNTING_STATUS | — | ✅ |
| 2 | CstWOUpdateEventTxnsPEOBaseTxnActionId | BASE_TXN_ACTION_ID | — | ✅ |
| 3 | CstWOUpdateEventTxnsPEOBaseTxnSourceTypeId | BASE_TXN_SOURCE_TYPE_ID | — | ✅ |
| 4 | CstWOUpdateEventTxnsPEOBaseTxnTypeId | BASE_TXN_TYPE_ID | — | ✅ |
| 5 | CstWOUpdateEventTxnsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 6 | CstWOUpdateEventTxnsPEOCostDate | COST_DATE | — | ✅ |
| 7 | CstWOUpdateEventTxnsPEOCostMethodCode | COST_METHOD_CODE | — | ✅ |
| 8 | CstWOUpdateEventTxnsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 9 | CstWOUpdateEventTxnsPEOCostProfileId | COST_PROFILE_ID | — | ✅ |
| 10 | CstWOUpdateEventTxnsPEOCostingStatus | COSTING_STATUS | — | ✅ |
| 11 | CstWOUpdateEventTxnsPEOCreatedBy | CREATED_BY | — | ✅ |
| 12 | CstWOUpdateEventTxnsPEOCreationDate | CREATION_DATE | — | ✅ |
| 13 | CstWOUpdateEventTxnsPEOCstWoUpdateEventId | CST_WO_UPDATE_EVENT_ID | — | ✅ |
| 14 | CstWOUpdateEventTxnsPEOCstWorkOrderId | CST_WORK_ORDER_ID | — | ✅ |
| 15 | CstWOUpdateEventTxnsPEOErrorCode | ERROR_CODE | — | ✅ |
| 16 | CstWOUpdateEventTxnsPEOEventDate | EVENT_DATE | — | ✅ |
| 17 | CstWOUpdateEventTxnsPEOExpenseReversedFlag | EXPENSE_REVERSED_FLAG | — | ✅ |
| 18 | CstWOUpdateEventTxnsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 19 | CstWOUpdateEventTxnsPEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | ✅ |
| 20 | CstWOUpdateEventTxnsPEOItemCostProfileId | ITEM_COST_PROFILE_ID | — | ✅ |
| 21 | CstWOUpdateEventTxnsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | CstWOUpdateEventTxnsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 23 | CstWOUpdateEventTxnsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | CstWOUpdateEventTxnsPEOLeTimezoneCode | LE_TIMEZONE_CODE | — | ✅ |
| 25 | CstWOUpdateEventTxnsPEOLogicalCloseDate | LOGICAL_CLOSE_DATE | — | ✅ |
| 26 | CstWOUpdateEventTxnsPEOPeriodName | PERIOD_NAME | — | ✅ |
| 27 | CstWOUpdateEventTxnsPEOPostedFlag | POSTED_FLAG | — | ✅ |
| 28 | CstWOUpdateEventTxnsPEOPreprocessingStatus | PREPROCESSING_STATUS | — | ✅ |
| 29 | CstWOUpdateEventTxnsPEOPriorWoSystemStatusCode | PRIOR_WO_SYSTEM_STATUS_CODE | — | ✅ |
| 30 | CstWOUpdateEventTxnsPEOPriorWorkOrderStatusId | PRIOR_WORK_ORDER_STATUS_ID | — | ✅ |
| 31 | CstWOUpdateEventTxnsPEOProductAdjProcessedFlag | PRODUCT_ADJ_PROCESSED_FLAG | — | ✅ |
| 32 | CstWOUpdateEventTxnsPEOReversalCostDate | REVERSAL_COST_DATE | — | ✅ |
| 33 | CstWOUpdateEventTxnsPEOScrapAdjProcessedFlag | SCRAP_ADJ_PROCESSED_FLAG | — | ✅ |
| 34 | CstWOUpdateEventTxnsPEOTotalCompletionQuantity | TOTAL_COMPLETION_QUANTITY | — | ✅ |
| 35 | CstWOUpdateEventTxnsPEOTotalScrapQuantity | TOTAL_SCRAP_QUANTITY | — | ✅ |
| 36 | CstWOUpdateEventTxnsPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 37 | CstWOUpdateEventTxnsPEOTxnSourceDocNumber | TXN_SOURCE_DOC_NUMBER | — | ✅ |
| 38 | CstWOUpdateEventTxnsPEOTxnSourceDocType | TXN_SOURCE_DOC_TYPE | — | ✅ |
| 39 | CstWOUpdateEventTxnsPEOTxnSourceRefDocNumber | TXN_SOURCE_REF_DOC_NUMBER | — | ✅ |
| 40 | CstWOUpdateEventTxnsPEOTxnSourceRefDocType | TXN_SOURCE_REF_DOC_TYPE | — | ✅ |
| 41 | CstWOUpdateEventTxnsPEOUomCode | UOM_CODE | — | ✅ |
| 42 | CstWOUpdateEventTxnsPEOWoSystemStatusCode | WO_SYSTEM_STATUS_CODE | — | ✅ |
| 43 | CstWOUpdateEventTxnsPEOWoUpdateEventTxnId | WO_UPDATE_EVENT_TXN_ID | 🔑 | ✅ |
| 44 | CstWOUpdateEventTxnsPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
