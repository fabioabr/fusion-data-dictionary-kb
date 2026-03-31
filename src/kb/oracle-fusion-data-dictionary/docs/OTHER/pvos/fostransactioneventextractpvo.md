---
id: DOC-OTHER-PVO-FosTransactionEventExtractPVO
doc_type: system-doc
title: "FosTransactionEventExtractPVO — PVO Cross-Module"
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
  - FosTransactionEventExtractPVO
  - fostransactioneventextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosTransactionEventExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos Transaction Event Extract. Acessa as tabelas: FOS_TXN_EVENTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosTransactionEventExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 51 | 1 | 1 | 51 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fos_txn_events|FOS_TXN_EVENTS]] — 51 atributos (1 PKs, 51 BICC)

---

## ⚙️ Atributos

### [[fos_txn_events|FOS_TXN_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionEventPEOAccessKeyNumber | ACCESS_KEY_NUMBER | — | ✅ |
| 2 | TransactionEventPEOConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 3 | TransactionEventPEOCorrectionFlag | CORRECTION_FLAG | — | ✅ |
| 4 | TransactionEventPEOCostCurrencyCode | COST_CURRENCY_CODE | — | ✅ |
| 5 | TransactionEventPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | TransactionEventPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | TransactionEventPEODocumentHeaderId | DOCUMENT_HEADER_ID | — | ✅ |
| 8 | TransactionEventPEODocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 9 | TransactionEventPEODocumentSourceSystemId | DOCUMENT_SOURCE_SYSTEM_ID | — | ✅ |
| 10 | TransactionEventPEODocumentType | DOCUMENT_TYPE | — | ✅ |
| 11 | TransactionEventPEODropshipFlag | DROPSHIP_FLAG | — | ✅ |
| 12 | TransactionEventPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 13 | TransactionEventPEOEventDataId | EVENT_DATA_ID | — | ✅ |
| 14 | TransactionEventPEOEventDate | EVENT_DATE | — | ✅ |
| 15 | TransactionEventPEOEventDefinitionId | EVENT_DEFINITION_ID | — | ✅ |
| 16 | TransactionEventPEOEventLineNumber | EVENT_LINE_NUMBER | — | ✅ |
| 17 | TransactionEventPEOEventNumber | EVENT_NUMBER | — | ✅ |
| 18 | TransactionEventPEOFiscalDocLineId | FISCAL_DOC_LINE_ID | — | ✅ |
| 19 | TransactionEventPEOFiscalDocScheduleId | FISCAL_DOC_SCHEDULE_ID | — | ✅ |
| 20 | TransactionEventPEOGroupId | GROUP_ID | — | ✅ |
| 21 | TransactionEventPEOItemCost | ITEM_COST | — | ✅ |
| 22 | TransactionEventPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 23 | TransactionEventPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 24 | TransactionEventPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | TransactionEventPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 26 | TransactionEventPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 27 | TransactionEventPEOMessageType | MESSAGE_TYPE | — | ✅ |
| 28 | TransactionEventPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 29 | TransactionEventPEOParentEventDataId | PARENT_EVENT_DATA_ID | — | ✅ |
| 30 | TransactionEventPEOParentEventDefinitionId | PARENT_EVENT_DEFINITION_ID | — | ✅ |
| 31 | TransactionEventPEOParentEventSystemId | PARENT_EVENT_SYSTEM_ID | — | ✅ |
| 32 | TransactionEventPEOQuantity | QUANTITY | — | ✅ |
| 33 | TransactionEventPEOReceiptAmount | RECEIPT_AMOUNT | — | ✅ |
| 34 | TransactionEventPEOReceiptCurrencyCode | RECEIPT_CURRENCY_CODE | — | ✅ |
| 35 | TransactionEventPEOReferenceEventDataId | REFERENCE_EVENT_DATA_ID | — | ✅ |
| 36 | TransactionEventPEOReferenceEventDefinitionId | REFERENCE_EVENT_DEFINITION_ID | — | ✅ |
| 37 | TransactionEventPEOReferenceEventSystemId | REFERENCE_EVENT_SYSTEM_ID | — | ✅ |
| 38 | TransactionEventPEORequestId | REQUEST_ID | — | ✅ |
| 39 | TransactionEventPEOReturnConsignmentStockFlag | RETURN_CONSIGNMENT_STOCK_FLAG | — | ✅ |
| 40 | TransactionEventPEOSecondaryQty | SECONDARY_QTY | — | ✅ |
| 41 | TransactionEventPEOSecondaryUom | SECONDARY_UOM | — | ✅ |
| 42 | TransactionEventPEOSourceDocumentId | SOURCE_DOCUMENT_ID | — | ✅ |
| 43 | TransactionEventPEOSourceTxnEventId | SOURCE_TXN_EVENT_ID | — | ✅ |
| 44 | TransactionEventPEOStatus | STATUS | — | ✅ |
| 45 | TransactionEventPEOSystemId | SYSTEM_ID | — | ✅ |
| 46 | TransactionEventPEOTaxInvoiceDate | TAX_INVOICE_DATE | — | ✅ |
| 47 | TransactionEventPEOTaxInvoiceNumber | TAX_INVOICE_NUMBER | — | ✅ |
| 48 | TransactionEventPEOTransactionEventId | TRANSACTION_EVENT_ID | 🔑 | ✅ |
| 49 | TransactionEventPEOTransactionOrgCode | TRANSACTION_ORG_CODE | — | ✅ |
| 50 | TransactionEventPEOUnreferencedEventFlag | UNREFERENCED_EVENT_FLAG | — | ✅ |
| 51 | TransactionEventPEOUom | UOM | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
