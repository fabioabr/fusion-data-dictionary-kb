---
id: DOC-OTHER-PVO-TransactionEventPVO
doc_type: system-doc
title: "TransactionEventPVO — PVO Cross-Module"
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
  - TransactionEventPVO
  - transactioneventpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionEventPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transaction Event. Acessa as tabelas: AP_INVOICES_ALL, AP_INVOICE_LINES_ALL, DOO_FULFILL_LINE_DETAILS (+8).

**Caminho:** `FscmTopModelAM.FosOrchestrationProcessAM.TransactionEventPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 227 | 11 | 1 | 213 | 94% |

---

## 🔗 Tabelas Relacionadas

- [[ap_invoices_all|AP_INVOICES_ALL]] — 8 atributos (8 BICC)
- [[ap_invoice_lines_all|AP_INVOICE_LINES_ALL]] — 14 atributos (14 BICC)
- [[doo_fulfill_line_details|DOO_FULFILL_LINE_DETAILS]] — 2 atributos (2 BICC)
- [[fos_doc_flow_assignment|FOS_DOC_FLOW_ASSIGNMENT]] — 3 atributos
- [[fos_event_doc_info|FOS_EVENT_DOC_INFO]] — 82 atributos (77 BICC)
- [[fos_flow_instances|FOS_FLOW_INSTANCES]] — 30 atributos (30 BICC)
- [[fos_task_type_vl|FOS_TASK_TYPE_VL]] — 4 atributos (4 BICC)
- [[fos_txn_events|FOS_TXN_EVENTS]] — 45 atributos (1 PKs, 42 BICC)
- [[po_headers_all|PO_HEADERS_ALL]] — 6 atributos (6 BICC)
- [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]] — 10 atributos (7 BICC)
- [[zx_lines_v|ZX_LINES_V]] — 23 atributos (23 BICC)

---

## ⚙️ Atributos

### [[ap_invoices_all|AP_INVOICES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApInvoicesAllExchangeRate | EXCHANGE_RATE | — | ✅ |
| 2 | ApInvoicesAllInvoiceAmount | INVOICE_AMOUNT | — | ✅ |
| 3 | ApInvoicesAllInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 4 | ApInvoicesAllInvoiceDate | INVOICE_DATE | — | ✅ |
| 5 | ApInvoicesAllInvoiceId | INVOICE_ID | — | ✅ |
| 6 | ApInvoicesAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | ApInvoicesAllVendorId | VENDOR_ID | — | ✅ |
| 8 | ApInvoicesAllVendorSiteId | VENDOR_SITE_ID | — | ✅ |

### [[ap_invoice_lines_all|AP_INVOICE_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApInvoiceLinesAllAssessableValue | ASSESSABLE_VALUE | — | ✅ |
| 2 | ApInvoiceLinesAllControlAmount | CONTROL_AMOUNT | — | ✅ |
| 3 | ApInvoiceLinesAllInvoiceId | INVOICE_ID | — | ✅ |
| 4 | ApInvoiceLinesAllLineNumber | LINE_NUMBER | — | ✅ |
| 5 | ApInvoiceLinesAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 6 | ApInvoiceLinesAllPrimaryIntendedUse | PRIMARY_INTENDED_USE | — | ✅ |
| 7 | ApInvoiceLinesAllProductCategory | PRODUCT_CATEGORY | — | ✅ |
| 8 | ApInvoiceLinesAllProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | ✅ |
| 9 | ApInvoiceLinesAllProductType | PRODUCT_TYPE | — | ✅ |
| 10 | ApInvoiceLinesAllShipFromLocationId | SHIP_FROM_LOCATION_ID | — | ✅ |
| 11 | ApInvoiceLinesAllShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 12 | ApInvoiceLinesAllTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | ✅ |
| 13 | ApInvoiceLinesAllTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 14 | ApInvoiceLinesAllUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |

### [[doo_fulfill_line_details|DOO_FULFILL_LINE_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FulfillLineDetailPEOCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | ✅ |
| 2 | FulfillLineDetailPEOFulfillLineDetailId | FULFILL_LINE_DETAIL_ID | — | ✅ |

### [[fos_doc_flow_assignment|FOS_DOC_FLOW_ASSIGNMENT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FlowAssignmentPEODocumentFlowAssignmentId | DOCUMENT_FLOW_ASSIGNMENT_ID | — | — |
| 2 | FlowAssignmentPEOEffectiveDocumentDate | EFFECTIVE_DOCUMENT_DATE | — | — |
| 3 | FlowAssignmentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[fos_event_doc_info|FOS_EVENT_DOC_INFO]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventDocInfoPEOAgreementPtrId | AGREEMENT_PTR_ID | — | ✅ |
| 2 | EventDocInfoPEOAgreementType | AGREEMENT_TYPE | — | ✅ |
| 3 | EventDocInfoPEOAutoCreatedConfigFlag | AUTO_CREATED_CONFIG_FLAG | — | ✅ |
| 4 | EventDocInfoPEOBaseInventoryItemId | BASE_INVENTORY_ITEM_ID | — | — |
| 5 | EventDocInfoPEOBaseItemNumber | BASE_ITEM_NUMBER | — | ✅ |
| 6 | EventDocInfoPEOBillToCustomerAccntNumber | BILL_TO_CUSTOMER_ACCNT_NUMBER | — | ✅ |
| 7 | EventDocInfoPEOBillToLocationCode | BILL_TO_LOCATION_CODE | — | ✅ |
| 8 | EventDocInfoPEOCategoryCode | CATEGORY_CODE | — | ✅ |
| 9 | EventDocInfoPEOConsignedFlag1 | CONSIGNED_FLAG | — | ✅ |
| 10 | EventDocInfoPEOCreatedBy | CREATED_BY | — | ✅ |
| 11 | EventDocInfoPEOCreationDate | CREATION_DATE | — | ✅ |
| 12 | EventDocInfoPEOCustomerDeliverToLocation | CUSTOMER_DELIVER_TO_LOCATION | — | ✅ |
| 13 | EventDocInfoPEOCustomerShipToLocation | CUSTOMER_SHIP_TO_LOCATION | — | ✅ |
| 14 | EventDocInfoPEODeliverToPartyNumber | DELIVER_TO_PARTY_NUMBER | — | ✅ |
| 15 | EventDocInfoPEODeliverToPartySiteNumber | DELIVER_TO_PARTY_SITE_NUMBER | — | ✅ |
| 16 | EventDocInfoPEODeliveryTransactionId | DELIVERY_TRANSACTION_ID | — | ✅ |
| 17 | EventDocInfoPEODestinationType | DESTINATION_TYPE | — | ✅ |
| 18 | EventDocInfoPEODocumentDate | DOCUMENT_DATE | — | ✅ |
| 19 | EventDocInfoPEODocumentHeaderId | DOCUMENT_HEADER_ID | — | ✅ |
| 20 | EventDocInfoPEODocumentLineDetailId | DOCUMENT_LINE_DETAIL_ID | — | ✅ |
| 21 | EventDocInfoPEODocumentLineDetailNumber | DOCUMENT_LINE_DETAIL_NUMBER | — | ✅ |
| 22 | EventDocInfoPEODocumentLineId | DOCUMENT_LINE_ID | — | ✅ |
| 23 | EventDocInfoPEODocumentLineNumber | DOCUMENT_LINE_NUMBER | — | ✅ |
| 24 | EventDocInfoPEODocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 25 | EventDocInfoPEODocumentRevision | DOCUMENT_REVISION | — | ✅ |
| 26 | EventDocInfoPEODocumentSourceSystemId | DOCUMENT_SOURCE_SYSTEM_ID | — | ✅ |
| 27 | EventDocInfoPEODocumentType | DOCUMENT_TYPE | — | ✅ |
| 28 | EventDocInfoPEODropshipFlag | DROPSHIP_FLAG | — | ✅ |
| 29 | EventDocInfoPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 30 | EventDocInfoPEOEventDocInfoId | EVENT_DOC_INFO_ID | — | ✅ |
| 31 | EventDocInfoPEOFromBuId | FROM_BU_ID | — | ✅ |
| 32 | EventDocInfoPEOFromLeCode | FROM_LE_CODE | — | ✅ |
| 33 | EventDocInfoPEOFromLeId | FROM_LE_ID | — | ✅ |
| 34 | EventDocInfoPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 35 | EventDocInfoPEOItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 36 | EventDocInfoPEOItemNumber | ITEM_NUMBER | — | ✅ |
| 37 | EventDocInfoPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 38 | EventDocInfoPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 39 | EventDocInfoPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 40 | EventDocInfoPEOLineType | LINE_TYPE | — | ✅ |
| 41 | EventDocInfoPEOLinkToDocumentId | LINK_TO_DOCUMENT_ID | — | ✅ |
| 42 | EventDocInfoPEOLinkToDocumentSystemId | LINK_TO_DOCUMENT_SYSTEM_ID | — | ✅ |
| 43 | EventDocInfoPEOLinkToDocumentType | LINK_TO_DOCUMENT_TYPE | — | ✅ |
| 44 | EventDocInfoPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 45 | EventDocInfoPEOOrderTypeCode | ORDER_TYPE_CODE | — | ✅ |
| 46 | EventDocInfoPEOOrderedAmount | ORDERED_AMOUNT | — | ✅ |
| 47 | EventDocInfoPEOOrderedCurrencyCode | ORDERED_CURRENCY_CODE | — | ✅ |
| 48 | EventDocInfoPEOOrderedQuantity | ORDERED_QUANTITY | — | ✅ |
| 49 | EventDocInfoPEOOrderedUom | ORDERED_UOM | — | ✅ |
| 50 | EventDocInfoPEOPriceCurrencyCode | PRICE_CURRENCY_CODE | — | ✅ |
| 51 | EventDocInfoPEOPricingUomType | PRICING_UOM_TYPE | — | — |
| 52 | EventDocInfoPEOPrjRefEnabledFlag | PRJ_REF_ENABLED_FLAG | — | — |
| 53 | EventDocInfoPEOProcurementBuId | PROCUREMENT_BU_ID | — | ✅ |
| 54 | EventDocInfoPEOPurchasingCategory | PURCHASING_CATEGORY | — | ✅ |
| 55 | EventDocInfoPEOReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | ✅ |
| 56 | EventDocInfoPEORefDocumentId | REF_DOCUMENT_ID | — | ✅ |
| 57 | EventDocInfoPEORefDocumentSystemId | REF_DOCUMENT_SYSTEM_ID | — | ✅ |
| 58 | EventDocInfoPEORefDocumentType | REF_DOCUMENT_TYPE | — | ✅ |
| 59 | EventDocInfoPEORefSalesOrderLineNumber | REF_SALES_ORDER_LINE_NUMBER | — | ✅ |
| 60 | EventDocInfoPEORefSalesOrderNumber | REF_SALES_ORDER_NUMBER | — | ✅ |
| 61 | EventDocInfoPEORefSalesOrderSystemCode | REF_SALES_ORDER_SYSTEM_CODE | — | ✅ |
| 62 | EventDocInfoPEOReferencedRmaFlag | REFERENCED_RMA_FLAG | — | ✅ |
| 63 | EventDocInfoPEOShipFromOrganizationCode | SHIP_FROM_ORGANIZATION_CODE | — | ✅ |
| 64 | EventDocInfoPEOShipToCustomerAccntNumber | SHIP_TO_CUSTOMER_ACCNT_NUMBER | — | ✅ |
| 65 | EventDocInfoPEOShipToCustomerNumber | SHIP_TO_CUSTOMER_NUMBER | — | ✅ |
| 66 | EventDocInfoPEOShipToLocationCode | SHIP_TO_LOCATION_CODE | — | ✅ |
| 67 | EventDocInfoPEOShipToOrganizationCode | SHIP_TO_ORGANIZATION_CODE | — | ✅ |
| 68 | EventDocInfoPEOShipToPartyNumber | SHIP_TO_PARTY_NUMBER | — | ✅ |
| 69 | EventDocInfoPEOShipToPartySiteNumber | SHIP_TO_PARTY_SITE_NUMBER | — | ✅ |
| 70 | EventDocInfoPEOSoldToCustomerAccntNumber | SOLD_TO_CUSTOMER_ACCNT_NUMBER | — | ✅ |
| 71 | EventDocInfoPEOSoldToCustomerNumber | SOLD_TO_CUSTOMER_NUMBER | — | ✅ |
| 72 | EventDocInfoPEOSoldToPartyNumber | SOLD_TO_PARTY_NUMBER | — | ✅ |
| 73 | EventDocInfoPEOSourceDocumentId | SOURCE_DOCUMENT_ID | — | ✅ |
| 74 | EventDocInfoPEOStatus | STATUS | — | ✅ |
| 75 | EventDocInfoPEOSupplierNumber | SUPPLIER_NUMBER | — | ✅ |
| 76 | EventDocInfoPEOSupplierSiteCode | SUPPLIER_SITE_CODE | — | ✅ |
| 77 | EventDocInfoPEOToBuId | TO_BU_ID | — | ✅ |
| 78 | EventDocInfoPEOToLeCode | TO_LE_CODE | — | ✅ |
| 79 | EventDocInfoPEOToLeId | TO_LE_ID | — | ✅ |
| 80 | EventDocInfoPEOTransactionOrgId | TRANSACTION_ORG_ID | — | — |
| 81 | EventDocInfoPEOTransferOrderFlag | TRANSFER_ORDER_FLAG | — | ✅ |
| 82 | EventDocInfoPEOUnitPrice | UNIT_PRICE | — | ✅ |

### [[fos_flow_instances|FOS_FLOW_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FlowInstancePEOAgreementFtrId | AGREEMENT_FTR_ID | — | ✅ |
| 2 | FlowInstancePEOAgreementPtrId | AGREEMENT_PTR_ID | — | ✅ |
| 3 | FlowInstancePEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | FlowInstancePEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | FlowInstancePEODocumentFlowAssignmentId | DOCUMENT_FLOW_ASSIGNMENT_ID | — | ✅ |
| 6 | FlowInstancePEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 7 | FlowInstancePEOEventDataId | EVENT_DATA_ID | — | ✅ |
| 8 | FlowInstancePEOEventDefinitionId | EVENT_DEFINITION_ID | — | ✅ |
| 9 | FlowInstancePEOFlowInstanceId | FLOW_INSTANCE_ID | — | ✅ |
| 10 | FlowInstancePEOFlowType | FLOW_TYPE | — | ✅ |
| 11 | FlowInstancePEOImportDate | IMPORT_DATE | — | ✅ |
| 12 | FlowInstancePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | FlowInstancePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | FlowInstancePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | FlowInstancePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | FlowInstancePEOProcessBatchId | PROCESS_BATCH_ID | — | ✅ |
| 17 | FlowInstancePEOStatus | STATUS | — | ✅ |
| 18 | FlowInstancePEOSystemId | SYSTEM_ID | — | ✅ |
| 19 | FlowInstancePEOTaDocumentId | TA_DOCUMENT_ID | — | ✅ |
| 20 | FlowInstancePEOTargetDocumentDetail | TARGET_DOCUMENT_DETAIL | — | ✅ |
| 21 | FlowInstancePEOTargetDocumentDetailId | TARGET_DOCUMENT_DETAIL_ID | — | ✅ |
| 22 | FlowInstancePEOTargetDocumentHeader | TARGET_DOCUMENT_HEADER | — | ✅ |
| 23 | FlowInstancePEOTargetDocumentHeaderId | TARGET_DOCUMENT_HEADER_ID | — | ✅ |
| 24 | FlowInstancePEOTargetDocumentLine | TARGET_DOCUMENT_LINE | — | ✅ |
| 25 | FlowInstancePEOTargetDocumentLineId | TARGET_DOCUMENT_LINE_ID | — | ✅ |
| 26 | FlowInstancePEOTargetSystemId | TARGET_SYSTEM_ID | — | ✅ |
| 27 | FlowInstancePEOTaskGroup | TASK_GROUP | — | ✅ |
| 28 | FlowInstancePEOTaskSequence | TASK_SEQUENCE | — | ✅ |
| 29 | FlowInstancePEOTaskType | TASK_TYPE | — | ✅ |
| 30 | FlowInstancePEOTransactionType | TRANSACTION_TYPE | — | ✅ |

### [[fos_task_type_vl|FOS_TASK_TYPE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaskTypePEODescription | DESCRIPTION | — | ✅ |
| 2 | TaskTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 3 | TaskTypePEOTaskName | TASK_NAME | — | ✅ |
| 4 | TaskTypePEOTaskTypeId | TASK_TYPE_ID | — | ✅ |

### [[fos_txn_events|FOS_TXN_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TransactionEventPEOConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 2 | TransactionEventPEOCorrectionFlag | CORRECTION_FLAG | — | ✅ |
| 3 | TransactionEventPEOCostCurrencyCode | COST_CURRENCY_CODE | — | ✅ |
| 4 | TransactionEventPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | TransactionEventPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | TransactionEventPEODocumentSourceSystemId | DOCUMENT_SOURCE_SYSTEM_ID | — | ✅ |
| 7 | TransactionEventPEODocumentType | DOCUMENT_TYPE | — | ✅ |
| 8 | TransactionEventPEODropshipFlag | DROPSHIP_FLAG | — | ✅ |
| 9 | TransactionEventPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 10 | TransactionEventPEOEventDataId | EVENT_DATA_ID | — | ✅ |
| 11 | TransactionEventPEOEventDate | EVENT_DATE | — | ✅ |
| 12 | TransactionEventPEOEventDefinitionId | EVENT_DEFINITION_ID | — | ✅ |
| 13 | TransactionEventPEOEventLineNumber | EVENT_LINE_NUMBER | — | ✅ |
| 14 | TransactionEventPEOEventNumber | EVENT_NUMBER | — | ✅ |
| 15 | TransactionEventPEOItemCost | ITEM_COST | — | ✅ |
| 16 | TransactionEventPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 17 | TransactionEventPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 18 | TransactionEventPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | TransactionEventPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 20 | TransactionEventPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 21 | TransactionEventPEOMessageType | MESSAGE_TYPE | — | — |
| 22 | TransactionEventPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 23 | TransactionEventPEOParentEventDataId | PARENT_EVENT_DATA_ID | — | ✅ |
| 24 | TransactionEventPEOParentEventDefinitionId | PARENT_EVENT_DEFINITION_ID | — | ✅ |
| 25 | TransactionEventPEOParentEventSystemId | PARENT_EVENT_SYSTEM_ID | — | ✅ |
| 26 | TransactionEventPEOQuantity | QUANTITY | — | ✅ |
| 27 | TransactionEventPEOReceiptAmount | RECEIPT_AMOUNT | — | ✅ |
| 28 | TransactionEventPEOReceiptCurrencyCode | RECEIPT_CURRENCY_CODE | — | ✅ |
| 29 | TransactionEventPEOReferenceEventDataId | REFERENCE_EVENT_DATA_ID | — | ✅ |
| 30 | TransactionEventPEOReferenceEventDefinitionId | REFERENCE_EVENT_DEFINITION_ID | — | ✅ |
| 31 | TransactionEventPEOReferenceEventSystemId | REFERENCE_EVENT_SYSTEM_ID | — | ✅ |
| 32 | TransactionEventPEORequestId | REQUEST_ID | — | ✅ |
| 33 | TransactionEventPEOReturnConsignmentStockFlag | RETURN_CONSIGNMENT_STOCK_FLAG | — | ✅ |
| 34 | TransactionEventPEOSecondaryQty | SECONDARY_QTY | — | ✅ |
| 35 | TransactionEventPEOSecondaryUom | SECONDARY_UOM | — | ✅ |
| 36 | TransactionEventPEOSourceDocumentId | SOURCE_DOCUMENT_ID | — | ✅ |
| 37 | TransactionEventPEOSourceTxnEventId | SOURCE_TXN_EVENT_ID | — | ✅ |
| 38 | TransactionEventPEOStatus | STATUS | — | ✅ |
| 39 | TransactionEventPEOSystemId | SYSTEM_ID | — | ✅ |
| 40 | TransactionEventPEOTaxInvoiceDate | TAX_INVOICE_DATE | — | — |
| 41 | TransactionEventPEOTaxInvoiceNumber | TAX_INVOICE_NUMBER | — | — |
| 42 | TransactionEventPEOTransactionEventId | TRANSACTION_EVENT_ID | 🔑 | ✅ |
| 43 | TransactionEventPEOTransactionOrgCode | TRANSACTION_ORG_CODE | — | ✅ |
| 44 | TransactionEventPEOUnreferencedEventFlag | UNREFERENCED_EVENT_FLAG | — | ✅ |
| 45 | TransactionEventPEOUom | UOM | — | ✅ |

### [[po_headers_all|PO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PoHeadersAllBillToLocationId | BILL_TO_LOCATION_ID | — | ✅ |
| 2 | PoHeadersAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 3 | PoHeadersAllPoHeaderId | PO_HEADER_ID | — | ✅ |
| 4 | PoHeadersAllPrcBuId | PRC_BU_ID | — | ✅ |
| 5 | PoHeadersAllVendorId | VENDOR_ID | — | ✅ |
| 6 | PoHeadersAllVendorSiteId | VENDOR_SITE_ID | — | ✅ |

### [[ra_customer_trx_all|RA_CUSTOMER_TRX_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RaCustomerTrxAllBillToSiteUseId | BILL_TO_SITE_USE_ID | — | ✅ |
| 2 | RaCustomerTrxAllCustomerTrxId | CUSTOMER_TRX_ID | — | ✅ |
| 3 | RaCustomerTrxAllExchangeRate | EXCHANGE_RATE | — | ✅ |
| 4 | RaCustomerTrxAllInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 5 | RaCustomerTrxAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 6 | RaCustomerTrxAllTrxDate | TRX_DATE | — | ✅ |
| 7 | TransactionHeaderPEOCustomerTrxId | CUSTOMER_TRX_ID | — | — |
| 8 | TransactionHeaderPEOExchangeRate | EXCHANGE_RATE | — | — |
| 9 | TransactionHeaderPEOInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 10 | TransactionHeaderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[zx_lines_v|ZX_LINES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ZxLinesPEOTaxLineId | TAX_LINE_ID | — | ✅ |
| 2 | ZxLinesPEOTaxLineNumber | TAX_LINE_NUMBER | — | ✅ |
| 3 | ZxLinesPEOTaxRate | TAX_RATE | — | ✅ |
| 4 | ZxLinesPEOTaxRateCode | TAX_RATE_CODE | — | ✅ |
| 5 | ZxLinesPEOTaxRateName | TAX_RATE_NAME | — | ✅ |
| 6 | ZxLinesPEOUnroundedTaxAmt | UNROUNDED_TAX_AMT | — | ✅ |
| 7 | ZxLinesVPEOTaxLineId | TAX_LINE_ID | — | ✅ |
| 8 | ZxLinesVPEOTaxLineNumber | TAX_LINE_NUMBER | — | ✅ |
| 9 | ZxLinesVPEOTaxRate | TAX_RATE | — | ✅ |
| 10 | ZxLinesVPEOTaxRateCode | TAX_RATE_CODE | — | ✅ |
| 11 | ZxLinesVPEOTaxRateName | TAX_RATE_NAME | — | ✅ |
| 12 | ZxLinesVPEOUnroundedTaxAmt | UNROUNDED_TAX_AMT | — | ✅ |
| 13 | ZxLinesVTax | TAX | — | ✅ |
| 14 | ZxLinesVTaxJurisdictionCode | TAX_JURISDICTION_CODE | — | ✅ |
| 15 | ZxLinesVTaxJurisdictionName | TAX_JURISDICTION_NAME | — | ✅ |
| 16 | ZxLinesVTaxLineId | TAX_LINE_ID | — | ✅ |
| 17 | ZxLinesVTaxRate | TAX_RATE | — | ✅ |
| 18 | ZxLinesVTaxRateCode | TAX_RATE_CODE | — | ✅ |
| 19 | ZxLinesVTaxRateName | TAX_RATE_NAME | — | ✅ |
| 20 | ZxLinesVTaxRegimeCode | TAX_REGIME_CODE | — | ✅ |
| 21 | ZxLinesVTaxRegimeName | TAX_REGIME_NAME | — | ✅ |
| 22 | ZxLinesVTaxStatusCode | TAX_STATUS_CODE | — | ✅ |
| 23 | ZxLinesVTaxStatusName | TAX_STATUS_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
