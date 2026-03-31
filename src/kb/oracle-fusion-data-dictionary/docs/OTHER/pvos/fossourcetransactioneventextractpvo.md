---
id: DOC-OTHER-PVO-FosSourceTransactionEventExtractPVO
doc_type: system-doc
title: "FosSourceTransactionEventExtractPVO — PVO Cross-Module"
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
  - FosSourceTransactionEventExtractPVO
  - fossourcetransactioneventextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosSourceTransactionEventExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos Source Transaction Event Extract. Acessa as tabelas: FOS_SOURCE_TXN_EVENTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosSourceTransactionEventExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 54 | 1 | 1 | 54 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fos_source_txn_events|FOS_SOURCE_TXN_EVENTS]] — 54 atributos (1 PKs, 54 BICC)

---

## ⚙️ Atributos

### [[fos_source_txn_events|FOS_SOURCE_TXN_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SourceTransactionEventPEOConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 2 | SourceTransactionEventPEOCorrectionFlag | CORRECTION_FLAG | — | ✅ |
| 3 | SourceTransactionEventPEOCostCurrencyCode | COST_CURRENCY_CODE | — | ✅ |
| 4 | SourceTransactionEventPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | SourceTransactionEventPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | SourceTransactionEventPEODocumentSourceSystemCode | DOCUMENT_SOURCE_SYSTEM_CODE | — | ✅ |
| 7 | SourceTransactionEventPEODocumentType | DOCUMENT_TYPE | — | ✅ |
| 8 | SourceTransactionEventPEODropshipFlag | DROPSHIP_FLAG | — | ✅ |
| 9 | SourceTransactionEventPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 10 | SourceTransactionEventPEOEventBatchId | EVENT_BATCH_ID | — | ✅ |
| 11 | SourceTransactionEventPEOEventDataId | EVENT_DATA_ID | — | ✅ |
| 12 | SourceTransactionEventPEOEventDate | EVENT_DATE | — | ✅ |
| 13 | SourceTransactionEventPEOEventGroup | EVENT_GROUP | — | ✅ |
| 14 | SourceTransactionEventPEOEventLineNumber | EVENT_LINE_NUMBER | — | ✅ |
| 15 | SourceTransactionEventPEOEventNumber | EVENT_NUMBER | — | ✅ |
| 16 | SourceTransactionEventPEOEventType | EVENT_TYPE | — | ✅ |
| 17 | SourceTransactionEventPEOGroupId | GROUP_ID | — | ✅ |
| 18 | SourceTransactionEventPEOInflightTransactionFlag | INFLIGHT_TRANSACTION_FLAG | — | ✅ |
| 19 | SourceTransactionEventPEOItemCost | ITEM_COST | — | ✅ |
| 20 | SourceTransactionEventPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 21 | SourceTransactionEventPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 22 | SourceTransactionEventPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | SourceTransactionEventPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 24 | SourceTransactionEventPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | SourceTransactionEventPEOMessageType | MESSAGE_TYPE | — | ✅ |
| 26 | SourceTransactionEventPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 27 | SourceTransactionEventPEOOrderedUomQuantity | ORDERED_UOM_QUANTITY | — | ✅ |
| 28 | SourceTransactionEventPEOParentEventDataId | PARENT_EVENT_DATA_ID | — | ✅ |
| 29 | SourceTransactionEventPEOParentEventSystemCode | PARENT_EVENT_SYSTEM_CODE | — | ✅ |
| 30 | SourceTransactionEventPEOParentEventType | PARENT_EVENT_TYPE | — | ✅ |
| 31 | SourceTransactionEventPEOPhysicalShipmentCostedFlag | PHYSICAL_SHIPMENT_COSTED_FLAG | — | ✅ |
| 32 | SourceTransactionEventPEOPreviousStatus | PREVIOUS_STATUS | — | ✅ |
| 33 | SourceTransactionEventPEOProcessBatchId | PROCESS_BATCH_ID | — | ✅ |
| 34 | SourceTransactionEventPEOProcessedFlag | PROCESSED_FLAG | — | ✅ |
| 35 | SourceTransactionEventPEOQuantity | QUANTITY | — | ✅ |
| 36 | SourceTransactionEventPEOReceiptAmount | RECEIPT_AMOUNT | — | ✅ |
| 37 | SourceTransactionEventPEOReceiptCurrencyCode | RECEIPT_CURRENCY_CODE | — | ✅ |
| 38 | SourceTransactionEventPEOReferenceEventDataId | REFERENCE_EVENT_DATA_ID | — | ✅ |
| 39 | SourceTransactionEventPEOReferenceEventSystemCode | REFERENCE_EVENT_SYSTEM_CODE | — | ✅ |
| 40 | SourceTransactionEventPEOReferenceEventType | REFERENCE_EVENT_TYPE | — | ✅ |
| 41 | SourceTransactionEventPEORequestId | REQUEST_ID | — | ✅ |
| 42 | SourceTransactionEventPEOReturnConsignmentFlag | RETURN_CONSIGNMENT_FLAG | — | ✅ |
| 43 | SourceTransactionEventPEOSecondaryQty | SECONDARY_QTY | — | ✅ |
| 44 | SourceTransactionEventPEOSecondaryUom | SECONDARY_UOM | — | ✅ |
| 45 | SourceTransactionEventPEOSourceDocumentId | SOURCE_DOCUMENT_ID | — | ✅ |
| 46 | SourceTransactionEventPEOStatus | STATUS | — | ✅ |
| 47 | SourceTransactionEventPEOSystemCode | SYSTEM_CODE | — | ✅ |
| 48 | SourceTransactionEventPEOTaxInvoiceDate | TAX_INVOICE_DATE | — | ✅ |
| 49 | SourceTransactionEventPEOTaxInvoiceNumber | TAX_INVOICE_NUMBER | — | ✅ |
| 50 | SourceTransactionEventPEOTransactionLogId | TRANSACTION_LOG_ID | 🔑 | ✅ |
| 51 | SourceTransactionEventPEOTransactionOrgCode | TRANSACTION_ORG_CODE | — | ✅ |
| 52 | SourceTransactionEventPEOTransactionTypeId | TRANSACTION_TYPE_ID | — | ✅ |
| 53 | SourceTransactionEventPEOUnreferencedEventFlag | UNREFERENCED_EVENT_FLAG | — | ✅ |
| 54 | SourceTransactionEventPEOUom | UOM | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
