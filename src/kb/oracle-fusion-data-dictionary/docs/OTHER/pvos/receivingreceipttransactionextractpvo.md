---
id: DOC-OTHER-PVO-ReceivingReceiptTransactionExtractPVO
doc_type: system-doc
title: "ReceivingReceiptTransactionExtractPVO — PVO Cross-Module"
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
  - ReceivingReceiptTransactionExtractPVO
  - receivingreceipttransactionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReceivingReceiptTransactionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Receiving Receipt Transaction Extract. Acessa as tabelas: RCV_SHIPMENT_HEADERS, RCV_SHIPMENT_LINES, RCV_TRANSACTIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.RcvBiccExtractAM.ReceivingReceiptTransactionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 459 | 3 | 1 | 444 | 97% |

---

## 🔗 Tabelas Relacionadas

- [[rcv_shipment_headers|RCV_SHIPMENT_HEADERS]] — 76 atributos (76 BICC)
- [[rcv_shipment_lines|RCV_SHIPMENT_LINES]] — 120 atributos (120 BICC)
- [[rcv_transactions|RCV_TRANSACTIONS]] — 263 atributos (1 PKs, 248 BICC)

---

## ⚙️ Atributos

### [[rcv_shipment_headers|RCV_SHIPMENT_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RcvngShpmntReceiptHdrPEOAsnType | ASN_TYPE | — | ✅ |
| 2 | RcvngShpmntReceiptHdrPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 3 | RcvngShpmntReceiptHdrPEOBillOfLading | BILL_OF_LADING | — | ✅ |
| 4 | RcvngShpmntReceiptHdrPEOCarrierEquipment | CARRIER_EQUIPMENT | — | ✅ |
| 5 | RcvngShpmntReceiptHdrPEOCarrierMethod | CARRIER_METHOD | — | ✅ |
| 6 | RcvngShpmntReceiptHdrPEOComments | COMMENTS | — | ✅ |
| 7 | RcvngShpmntReceiptHdrPEOConversionDate | CONVERSION_DATE | — | ✅ |
| 8 | RcvngShpmntReceiptHdrPEOConversionRate | CONVERSION_RATE | — | ✅ |
| 9 | RcvngShpmntReceiptHdrPEOConversionRateType | CONVERSION_RATE_TYPE | — | ✅ |
| 10 | RcvngShpmntReceiptHdrPEOCreatedBy | CREATED_BY | — | ✅ |
| 11 | RcvngShpmntReceiptHdrPEOCreationDate | CREATION_DATE | — | ✅ |
| 12 | RcvngShpmntReceiptHdrPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 13 | RcvngShpmntReceiptHdrPEOCustomerId | CUSTOMER_ID | — | ✅ |
| 14 | RcvngShpmntReceiptHdrPEOCustomerSiteId | CUSTOMER_SITE_ID | — | ✅ |
| 15 | RcvngShpmntReceiptHdrPEOEdiControlNum | EDI_CONTROL_NUM | — | ✅ |
| 16 | RcvngShpmntReceiptHdrPEOEmployeeId | EMPLOYEE_ID | — | ✅ |
| 17 | RcvngShpmntReceiptHdrPEOExpectedReceiptDate | EXPECTED_RECEIPT_DATE | — | ✅ |
| 18 | RcvngShpmntReceiptHdrPEOFreightAmount | FREIGHT_AMOUNT | — | ✅ |
| 19 | RcvngShpmntReceiptHdrPEOFreightBillNumber | FREIGHT_BILL_NUMBER | — | ✅ |
| 20 | RcvngShpmntReceiptHdrPEOFreightCarrierId | FREIGHT_CARRIER_ID | — | ✅ |
| 21 | RcvngShpmntReceiptHdrPEOFreightTerms | FREIGHT_TERMS | — | ✅ |
| 22 | RcvngShpmntReceiptHdrPEOGovernmentContext | GOVERNMENT_CONTEXT | — | ✅ |
| 23 | RcvngShpmntReceiptHdrPEOGrossWeight | GROSS_WEIGHT | — | ✅ |
| 24 | RcvngShpmntReceiptHdrPEOGrossWeightUomCode | GROSS_WEIGHT_UOM_CODE | — | ✅ |
| 25 | RcvngShpmntReceiptHdrPEOHazardClass | HAZARD_CLASS | — | ✅ |
| 26 | RcvngShpmntReceiptHdrPEOHazardCode | HAZARD_CODE | — | ✅ |
| 27 | RcvngShpmntReceiptHdrPEOHazardDescription | HAZARD_DESCRIPTION | — | ✅ |
| 28 | RcvngShpmntReceiptHdrPEOInvoiceAmount | INVOICE_AMOUNT | — | ✅ |
| 29 | RcvngShpmntReceiptHdrPEOInvoiceDate | INVOICE_DATE | — | ✅ |
| 30 | RcvngShpmntReceiptHdrPEOInvoiceNum | INVOICE_NUM | — | ✅ |
| 31 | RcvngShpmntReceiptHdrPEOInvoiceStatusCode | INVOICE_STATUS_CODE | — | ✅ |
| 32 | RcvngShpmntReceiptHdrPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 33 | RcvngShpmntReceiptHdrPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 34 | RcvngShpmntReceiptHdrPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 35 | RcvngShpmntReceiptHdrPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 36 | RcvngShpmntReceiptHdrPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 37 | RcvngShpmntReceiptHdrPEOLspFlag | LSP_FLAG | — | ✅ |
| 38 | RcvngShpmntReceiptHdrPEONetWeight | NET_WEIGHT | — | ✅ |
| 39 | RcvngShpmntReceiptHdrPEONetWeightUomCode | NET_WEIGHT_UOM_CODE | — | ✅ |
| 40 | RcvngShpmntReceiptHdrPEONoticeCreationDate | NOTICE_CREATION_DATE | — | ✅ |
| 41 | RcvngShpmntReceiptHdrPEONumOfContainers | NUM_OF_CONTAINERS | — | ✅ |
| 42 | RcvngShpmntReceiptHdrPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 43 | RcvngShpmntReceiptHdrPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 44 | RcvngShpmntReceiptHdrPEOPackagingCode | PACKAGING_CODE | — | ✅ |
| 45 | RcvngShpmntReceiptHdrPEOPackingSlip | PACKING_SLIP | — | ✅ |
| 46 | RcvngShpmntReceiptHdrPEOPaymentTermsId | PAYMENT_TERMS_ID | — | ✅ |
| 47 | RcvngShpmntReceiptHdrPEORaDocCreationDate | RA_DOC_CREATION_DATE | — | ✅ |
| 48 | RcvngShpmntReceiptHdrPEORaDocLastUpdateDate | RA_DOC_LAST_UPDATE_DATE | — | ✅ |
| 49 | RcvngShpmntReceiptHdrPEORaDocRevisionDate | RA_DOC_REVISION_DATE | — | ✅ |
| 50 | RcvngShpmntReceiptHdrPEORaDocRevisionNumber | RA_DOC_REVISION_NUMBER | — | ✅ |
| 51 | RcvngShpmntReceiptHdrPEORaDocumentCode | RA_DOCUMENT_CODE | — | ✅ |
| 52 | RcvngShpmntReceiptHdrPEORaDocumentNumber | RA_DOCUMENT_NUMBER | — | ✅ |
| 53 | RcvngShpmntReceiptHdrPEORaDooSourceSystemId | RA_DOO_SOURCE_SYSTEM_ID | — | ✅ |
| 54 | RcvngShpmntReceiptHdrPEORaNoteToReceiver | RA_NOTE_TO_RECEIVER | — | ✅ |
| 55 | RcvngShpmntReceiptHdrPEORaOutsourcerContactId | RA_OUTSOURCER_CONTACT_ID | — | ✅ |
| 56 | RcvngShpmntReceiptHdrPEORaOutsourcerPartyId | RA_OUTSOURCER_PARTY_ID | — | ✅ |
| 57 | RcvngShpmntReceiptHdrPEOReceiptAdviceNumber | RECEIPT_ADVICE_NUMBER | — | ✅ |
| 58 | RcvngShpmntReceiptHdrPEOReceiptNum | RECEIPT_NUM | — | ✅ |
| 59 | RcvngShpmntReceiptHdrPEOReceiptSourceCode | RECEIPT_SOURCE_CODE | — | ✅ |
| 60 | RcvngShpmntReceiptHdrPEORemitToSiteId | REMIT_TO_SITE_ID | — | ✅ |
| 61 | RcvngShpmntReceiptHdrPEORequestId | REQUEST_ID | — | ✅ |
| 62 | RcvngShpmntReceiptHdrPEORmaBuId | RMA_BU_ID | — | ✅ |
| 63 | RcvngShpmntReceiptHdrPEOShipFromLocationId | SHIP_FROM_LOCATION_ID | — | ✅ |
| 64 | RcvngShpmntReceiptHdrPEOShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 65 | RcvngShpmntReceiptHdrPEOShipToOrgId | SHIP_TO_ORG_ID | — | ✅ |
| 66 | RcvngShpmntReceiptHdrPEOShipmentHeaderId | SHIPMENT_HEADER_ID | — | ✅ |
| 67 | RcvngShpmntReceiptHdrPEOShipmentNum | SHIPMENT_NUM | — | ✅ |
| 68 | RcvngShpmntReceiptHdrPEOShippedDate | SHIPPED_DATE | — | ✅ |
| 69 | RcvngShpmntReceiptHdrPEOSpecialHandlingCode | SPECIAL_HANDLING_CODE | — | ✅ |
| 70 | RcvngShpmntReceiptHdrPEOTarWeight | TAR_WEIGHT | — | ✅ |
| 71 | RcvngShpmntReceiptHdrPEOTarWeightUomCode | TAR_WEIGHT_UOM_CODE | — | ✅ |
| 72 | RcvngShpmntReceiptHdrPEOTaxAmount | TAX_AMOUNT | — | ✅ |
| 73 | RcvngShpmntReceiptHdrPEOTaxName | TAX_NAME | — | ✅ |
| 74 | RcvngShpmntReceiptHdrPEOVendorId | VENDOR_ID | — | ✅ |
| 75 | RcvngShpmntReceiptHdrPEOVendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 76 | RcvngShpmntReceiptHdrPEOWaybillAirbillNum | WAYBILL_AIRBILL_NUM | — | ✅ |

### [[rcv_shipment_lines|RCV_SHIPMENT_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RcvngShpmntReceiptLinePEOAmount | AMOUNT | — | ✅ |
| 2 | RcvngShpmntReceiptLinePEOAmountReceived | AMOUNT_RECEIVED | — | ✅ |
| 3 | RcvngShpmntReceiptLinePEOAsnLpnId | ASN_LPN_ID | — | ✅ |
| 4 | RcvngShpmntReceiptLinePEOAssessableValue | ASSESSABLE_VALUE | — | ✅ |
| 5 | RcvngShpmntReceiptLinePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 6 | RcvngShpmntReceiptLinePEOBarCodeLabel | BAR_CODE_LABEL | — | ✅ |
| 7 | RcvngShpmntReceiptLinePEOCategoryId | CATEGORY_ID | — | ✅ |
| 8 | RcvngShpmntReceiptLinePEOComments | COMMENTS | — | ✅ |
| 9 | RcvngShpmntReceiptLinePEOConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 10 | RcvngShpmntReceiptLinePEOConsumedQuantity | CONSUMED_QUANTITY | — | ✅ |
| 11 | RcvngShpmntReceiptLinePEOContainerNum | CONTAINER_NUM | — | ✅ |
| 12 | RcvngShpmntReceiptLinePEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 13 | RcvngShpmntReceiptLinePEOCreatedBy | CREATED_BY | — | ✅ |
| 14 | RcvngShpmntReceiptLinePEOCreationDate | CREATION_DATE | — | ✅ |
| 15 | RcvngShpmntReceiptLinePEOCustomerId | CUSTOMER_ID | — | ✅ |
| 16 | RcvngShpmntReceiptLinePEOCustomerItemNum | CUSTOMER_ITEM_NUM | — | ✅ |
| 17 | RcvngShpmntReceiptLinePEOCustomerSiteId | CUSTOMER_SITE_ID | — | ✅ |
| 18 | RcvngShpmntReceiptLinePEODefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | ✅ |
| 19 | RcvngShpmntReceiptLinePEODeliverToLocationId | DELIVER_TO_LOCATION_ID | — | ✅ |
| 20 | RcvngShpmntReceiptLinePEODeliverToPersonId | DELIVER_TO_PERSON_ID | — | ✅ |
| 21 | RcvngShpmntReceiptLinePEODestinationContext | DESTINATION_CONTEXT | — | ✅ |
| 22 | RcvngShpmntReceiptLinePEODestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 23 | RcvngShpmntReceiptLinePEODocumentFiscalClassification | DOCUMENT_FISCAL_CLASSIFICATION | — | ✅ |
| 24 | RcvngShpmntReceiptLinePEOEmployeeId | EMPLOYEE_ID | — | ✅ |
| 25 | RcvngShpmntReceiptLinePEOExcessTransportReason | EXCESS_TRANSPORT_REASON | — | ✅ |
| 26 | RcvngShpmntReceiptLinePEOFinalDischargeLocationId | FINAL_DISCHARGE_LOCATION_ID | — | ✅ |
| 27 | RcvngShpmntReceiptLinePEOFirstPtyRegId | FIRST_PTY_REG_ID | — | ✅ |
| 28 | RcvngShpmntReceiptLinePEOFromOrganizationId | FROM_ORGANIZATION_ID | — | ✅ |
| 29 | RcvngShpmntReceiptLinePEOGovernmentContext | GOVERNMENT_CONTEXT | — | ✅ |
| 30 | RcvngShpmntReceiptLinePEOInvoiceStatusCode | INVOICE_STATUS_CODE | — | ✅ |
| 31 | RcvngShpmntReceiptLinePEOItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 32 | RcvngShpmntReceiptLinePEOItemId | ITEM_ID | — | ✅ |
| 33 | RcvngShpmntReceiptLinePEOItemRevision | ITEM_REVISION | — | ✅ |
| 34 | RcvngShpmntReceiptLinePEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 35 | RcvngShpmntReceiptLinePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 36 | RcvngShpmntReceiptLinePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 37 | RcvngShpmntReceiptLinePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 38 | RcvngShpmntReceiptLinePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 39 | RcvngShpmntReceiptLinePEOLineNum | LINE_NUM | — | ✅ |
| 40 | RcvngShpmntReceiptLinePEOLocatorId | LOCATOR_ID | — | ✅ |
| 41 | RcvngShpmntReceiptLinePEOMmtTransactionId | MMT_TRANSACTION_ID | — | ✅ |
| 42 | RcvngShpmntReceiptLinePEONoticeUnitPrice | NOTICE_UNIT_PRICE | — | ✅ |
| 43 | RcvngShpmntReceiptLinePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 44 | RcvngShpmntReceiptLinePEOPackingSlip | PACKING_SLIP | — | ✅ |
| 45 | RcvngShpmntReceiptLinePEOPoDistributionId | PO_DISTRIBUTION_ID | — | ✅ |
| 46 | RcvngShpmntReceiptLinePEOPoHeaderId | PO_HEADER_ID | — | ✅ |
| 47 | RcvngShpmntReceiptLinePEOPoLineId | PO_LINE_ID | — | ✅ |
| 48 | RcvngShpmntReceiptLinePEOPoLineLocationId | PO_LINE_LOCATION_ID | — | ✅ |
| 49 | RcvngShpmntReceiptLinePEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 50 | RcvngShpmntReceiptLinePEOProductCategory | PRODUCT_CATEGORY | — | ✅ |
| 51 | RcvngShpmntReceiptLinePEOProductType | PRODUCT_TYPE | — | ✅ |
| 52 | RcvngShpmntReceiptLinePEOQuantityAccepted | QUANTITY_ACCEPTED | — | ✅ |
| 53 | RcvngShpmntReceiptLinePEOQuantityDelivered | QUANTITY_DELIVERED | — | ✅ |
| 54 | RcvngShpmntReceiptLinePEOQuantityReceived | QUANTITY_RECEIVED | — | ✅ |
| 55 | RcvngShpmntReceiptLinePEOQuantityRejected | QUANTITY_REJECTED | — | ✅ |
| 56 | RcvngShpmntReceiptLinePEOQuantityReturned | QUANTITY_RETURNED | — | ✅ |
| 57 | RcvngShpmntReceiptLinePEOQuantityShipped | QUANTITY_SHIPPED | — | ✅ |
| 58 | RcvngShpmntReceiptLinePEORaAllowSubstituteReceipt | RA_ALLOW_SUBSTITUTE_RECEIPT | — | ✅ |
| 59 | RcvngShpmntReceiptLinePEORaDaysEarlyReceiptAllowed | RA_DAYS_EARLY_RECEIPT_ALLOWED | — | ✅ |
| 60 | RcvngShpmntReceiptLinePEORaDaysLateReceiptAllowed | RA_DAYS_LATE_RECEIPT_ALLOWED | — | ✅ |
| 61 | RcvngShpmntReceiptLinePEORaDocLineCreationDate | RA_DOC_LINE_CREATION_DATE | — | ✅ |
| 62 | RcvngShpmntReceiptLinePEORaDocLineLastUpdateDate | RA_DOC_LINE_LAST_UPDATE_DATE | — | ✅ |
| 63 | RcvngShpmntReceiptLinePEORaDocScheduleNumber | RA_DOC_SCHEDULE_NUMBER | — | ✅ |
| 64 | RcvngShpmntReceiptLinePEORaDocumentLineNumber | RA_DOCUMENT_LINE_NUMBER | — | ✅ |
| 65 | RcvngShpmntReceiptLinePEORaDooFulfillmentLineNumber | RA_DOO_FULFILLMENT_LINE_NUMBER | — | ✅ |
| 66 | RcvngShpmntReceiptLinePEORaDooHeaderNumber | RA_DOO_HEADER_NUMBER | — | ✅ |
| 67 | RcvngShpmntReceiptLinePEORaDooLineNumber | RA_DOO_LINE_NUMBER | — | ✅ |
| 68 | RcvngShpmntReceiptLinePEORaEnforceShipToLocCode | RA_ENFORCE_SHIP_TO_LOC_CODE | — | ✅ |
| 69 | RcvngShpmntReceiptLinePEORaExpectedReceiptDate | RA_EXPECTED_RECEIPT_DATE | — | ✅ |
| 70 | RcvngShpmntReceiptLinePEORaLastActionCode | RA_LAST_ACTION_CODE | — | ✅ |
| 71 | RcvngShpmntReceiptLinePEORaNoteToReceiver1 | RA_NOTE_TO_RECEIVER | — | ✅ |
| 72 | RcvngShpmntReceiptLinePEORaOrigDooFulfilLineNum | RA_ORIG_DOO_FULFIL_LINE_NUM | — | ✅ |
| 73 | RcvngShpmntReceiptLinePEORaOrigDooHeaderNumber | RA_ORIG_DOO_HEADER_NUMBER | — | ✅ |
| 74 | RcvngShpmntReceiptLinePEORaOrigDooLineNumber | RA_ORIG_DOO_LINE_NUMBER | — | ✅ |
| 75 | RcvngShpmntReceiptLinePEORaOrigOcHeaderNumber | RA_ORIG_OC_HEADER_NUMBER | — | ✅ |
| 76 | RcvngShpmntReceiptLinePEORaOrigOcLineNumber | RA_ORIG_OC_LINE_NUMBER | — | ✅ |
| 77 | RcvngShpmntReceiptLinePEORaQtyRcvExceptionCode | RA_QTY_RCV_EXCEPTION_CODE | — | ✅ |
| 78 | RcvngShpmntReceiptLinePEORaQtyRcvTolerance | RA_QTY_RCV_TOLERANCE | — | ✅ |
| 79 | RcvngShpmntReceiptLinePEORaQuantityExpected | RA_QUANTITY_EXPECTED | — | ✅ |
| 80 | RcvngShpmntReceiptLinePEORaReceiptDaysExceptionCode | RA_RECEIPT_DAYS_EXCEPTION_CODE | — | ✅ |
| 81 | RcvngShpmntReceiptLinePEORaSecondaryQuantityExpected | RA_SECONDARY_QUANTITY_EXPECTED | — | ✅ |
| 82 | RcvngShpmntReceiptLinePEORaUnitPrice | RA_UNIT_PRICE | — | ✅ |
| 83 | RcvngShpmntReceiptLinePEOReasonId | REASON_ID | — | ✅ |
| 84 | RcvngShpmntReceiptLinePEOReceiptAdviceHeaderId | RECEIPT_ADVICE_HEADER_ID | — | ✅ |
| 85 | RcvngShpmntReceiptLinePEOReceiptAdviceLineId | RECEIPT_ADVICE_LINE_ID | — | ✅ |
| 86 | RcvngShpmntReceiptLinePEOReceiptAdviceLineNumber | RECEIPT_ADVICE_LINE_NUMBER | — | ✅ |
| 87 | RcvngShpmntReceiptLinePEOReqDistributionId | REQ_DISTRIBUTION_ID | — | ✅ |
| 88 | RcvngShpmntReceiptLinePEORequestId1 | REQUEST_ID | — | ✅ |
| 89 | RcvngShpmntReceiptLinePEORequisitionLineId | REQUISITION_LINE_ID | — | ✅ |
| 90 | RcvngShpmntReceiptLinePEORoutingHeaderId | ROUTING_HEADER_ID | — | ✅ |
| 91 | RcvngShpmntReceiptLinePEOSecondaryQuantityReceived | SECONDARY_QUANTITY_RECEIVED | — | ✅ |
| 92 | RcvngShpmntReceiptLinePEOSecondaryQuantityShipped | SECONDARY_QUANTITY_SHIPPED | — | ✅ |
| 93 | RcvngShpmntReceiptLinePEOSecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 94 | RcvngShpmntReceiptLinePEOShipFromLocationId | SHIP_FROM_LOCATION_ID | — | ✅ |
| 95 | RcvngShpmntReceiptLinePEOShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 96 | RcvngShpmntReceiptLinePEOShipmentHeaderId | SHIPMENT_HEADER_ID | — | ✅ |
| 97 | RcvngShpmntReceiptLinePEOShipmentLineId | SHIPMENT_LINE_ID | — | ✅ |
| 98 | RcvngShpmntReceiptLinePEOShipmentLineStatusCode | SHIPMENT_LINE_STATUS_CODE | — | ✅ |
| 99 | RcvngShpmntReceiptLinePEOShipmentUnitPrice | SHIPMENT_UNIT_PRICE | — | ✅ |
| 100 | RcvngShpmntReceiptLinePEOSourceDocumentCode | SOURCE_DOCUMENT_CODE | — | ✅ |
| 101 | RcvngShpmntReceiptLinePEOSpGroupId | SP_GROUP_ID | — | ✅ |
| 102 | RcvngShpmntReceiptLinePEOSpQuantity | SP_QUANTITY | — | ✅ |
| 103 | RcvngShpmntReceiptLinePEOSpUomCode | SP_UOM_CODE | — | ✅ |
| 104 | RcvngShpmntReceiptLinePEOTaxAmount | TAX_AMOUNT | — | ✅ |
| 105 | RcvngShpmntReceiptLinePEOTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | ✅ |
| 106 | RcvngShpmntReceiptLinePEOTaxName | TAX_NAME | — | ✅ |
| 107 | RcvngShpmntReceiptLinePEOThirdPtyRegId | THIRD_PTY_REG_ID | — | ✅ |
| 108 | RcvngShpmntReceiptLinePEOToOrganizationId | TO_ORGANIZATION_ID | — | ✅ |
| 109 | RcvngShpmntReceiptLinePEOToSubinventory | TO_SUBINVENTORY | — | ✅ |
| 110 | RcvngShpmntReceiptLinePEOTransferCost | TRANSFER_COST | — | ✅ |
| 111 | RcvngShpmntReceiptLinePEOTransferOrderLineId | TRANSFER_ORDER_LINE_ID | — | ✅ |
| 112 | RcvngShpmntReceiptLinePEOTransferPercentage | TRANSFER_PERCENTAGE | — | ✅ |
| 113 | RcvngShpmntReceiptLinePEOTransportationCost | TRANSPORTATION_COST | — | ✅ |
| 114 | RcvngShpmntReceiptLinePEOTruckNum | TRUCK_NUM | — | ✅ |
| 115 | RcvngShpmntReceiptLinePEOTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 116 | RcvngShpmntReceiptLinePEOUomCode | UOM_CODE | — | ✅ |
| 117 | RcvngShpmntReceiptLinePEOUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |
| 118 | RcvngShpmntReceiptLinePEOVendorCumShippedQuantity | VENDOR_CUM_SHIPPED_QUANTITY | — | ✅ |
| 119 | RcvngShpmntReceiptLinePEOVendorItemNum | VENDOR_ITEM_NUM | — | ✅ |
| 120 | RcvngShpmntReceiptLinePEOVendorLotNum | VENDOR_LOT_NUM | — | ✅ |

### [[rcv_transactions|RCV_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RcvngRcptTrnsctnExtrctPEOAmount | AMOUNT | — | ✅ |
| 2 | RcvngRcptTrnsctnExtrctPEOAmountBilled | AMOUNT_BILLED | — | ✅ |
| 3 | RcvngRcptTrnsctnExtrctPEOAssessableValue | ASSESSABLE_VALUE | — | ✅ |
| 4 | RcvngRcptTrnsctnExtrctPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 5 | RcvngRcptTrnsctnExtrctPEOBillingUomCode | BILLING_UOM_CODE | — | ✅ |
| 6 | RcvngRcptTrnsctnExtrctPEOComments | COMMENTS | — | ✅ |
| 7 | RcvngRcptTrnsctnExtrctPEOConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 8 | RcvngRcptTrnsctnExtrctPEOConsignedFlag1 | CONSIGNED_FLAG | — | ✅ |
| 9 | RcvngRcptTrnsctnExtrctPEOConsumedQuantity | CONSUMED_QUANTITY | — | ✅ |
| 10 | RcvngRcptTrnsctnExtrctPEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 11 | RcvngRcptTrnsctnExtrctPEOCreatedBy | CREATED_BY | — | ✅ |
| 12 | RcvngRcptTrnsctnExtrctPEOCreationDate | CREATION_DATE | — | ✅ |
| 13 | RcvngRcptTrnsctnExtrctPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 14 | RcvngRcptTrnsctnExtrctPEOCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 15 | RcvngRcptTrnsctnExtrctPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 16 | RcvngRcptTrnsctnExtrctPEOCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 17 | RcvngRcptTrnsctnExtrctPEOCustomerId | CUSTOMER_ID | — | ✅ |
| 18 | RcvngRcptTrnsctnExtrctPEOCustomerSiteId | CUSTOMER_SITE_ID | — | ✅ |
| 19 | RcvngRcptTrnsctnExtrctPEODefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | ✅ |
| 20 | RcvngRcptTrnsctnExtrctPEODeliverToLocationId | DELIVER_TO_LOCATION_ID | — | ✅ |
| 21 | RcvngRcptTrnsctnExtrctPEODestinationContext | DESTINATION_CONTEXT | — | ✅ |
| 22 | RcvngRcptTrnsctnExtrctPEODestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 23 | RcvngRcptTrnsctnExtrctPEODirectTransferOrderFlag | DIRECT_TRANSFER_ORDER_FLAG | — | ✅ |
| 24 | RcvngRcptTrnsctnExtrctPEODocumentFiscalClassification | DOCUMENT_FISCAL_CLASSIFICATION | — | ✅ |
| 25 | RcvngRcptTrnsctnExtrctPEOEmployeeId | EMPLOYEE_ID | — | ✅ |
| 26 | RcvngRcptTrnsctnExtrctPEOExternalSysTxnReference | EXTERNAL_SYS_TXN_REFERENCE | — | ✅ |
| 27 | RcvngRcptTrnsctnExtrctPEOExtractDeliverToPersonId | DELIVER_TO_PERSON_ID | — | ✅ |
| 28 | RcvngRcptTrnsctnExtrctPEOFinalDischargeLocationId | FINAL_DISCHARGE_LOCATION_ID | — | ✅ |
| 29 | RcvngRcptTrnsctnExtrctPEOFirstPtyRegId | FIRST_PTY_REG_ID | — | ✅ |
| 30 | RcvngRcptTrnsctnExtrctPEOFromLocatorId | FROM_LOCATOR_ID | — | ✅ |
| 31 | RcvngRcptTrnsctnExtrctPEOFromSubinventory | FROM_SUBINVENTORY | — | ✅ |
| 32 | RcvngRcptTrnsctnExtrctPEOGroupId | GROUP_ID | — | ✅ |
| 33 | RcvngRcptTrnsctnExtrctPEOInspectionQualityCode | INSPECTION_QUALITY_CODE | — | ✅ |
| 34 | RcvngRcptTrnsctnExtrctPEOInspectionStatusCode | INSPECTION_STATUS_CODE | — | ✅ |
| 35 | RcvngRcptTrnsctnExtrctPEOIntendedUseClassifId | INTENDED_USE_CLASSIF_ID | — | ✅ |
| 36 | RcvngRcptTrnsctnExtrctPEOInterfaceGroupId | INTERFACE_GROUP_ID | — | ✅ |
| 37 | RcvngRcptTrnsctnExtrctPEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | ✅ |
| 38 | RcvngRcptTrnsctnExtrctPEOInterfaceSourceLineId | INTERFACE_SOURCE_LINE_ID | — | ✅ |
| 39 | RcvngRcptTrnsctnExtrctPEOInterfaceTransactionId | INTERFACE_TRANSACTION_ID | — | ✅ |
| 40 | RcvngRcptTrnsctnExtrctPEOInvTransactionId | INV_TRANSACTION_ID | — | ✅ |
| 41 | RcvngRcptTrnsctnExtrctPEOInvoiceId | INVOICE_ID | — | ✅ |
| 42 | RcvngRcptTrnsctnExtrctPEOInvoiceStatusCode | INVOICE_STATUS_CODE | — | ✅ |
| 43 | RcvngRcptTrnsctnExtrctPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 44 | RcvngRcptTrnsctnExtrctPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 45 | RcvngRcptTrnsctnExtrctPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 46 | RcvngRcptTrnsctnExtrctPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 47 | RcvngRcptTrnsctnExtrctPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 48 | RcvngRcptTrnsctnExtrctPEOLocationId | LOCATION_ID | — | ✅ |
| 49 | RcvngRcptTrnsctnExtrctPEOLocatorId | LOCATOR_ID | — | ✅ |
| 50 | RcvngRcptTrnsctnExtrctPEOLpnGroupId | LPN_GROUP_ID | — | ✅ |
| 51 | RcvngRcptTrnsctnExtrctPEOLpnId | LPN_ID | — | ✅ |
| 52 | RcvngRcptTrnsctnExtrctPEOMatchFlag | MATCH_FLAG | — | ✅ |
| 53 | RcvngRcptTrnsctnExtrctPEOMatchOption | MATCH_OPTION | — | ✅ |
| 54 | RcvngRcptTrnsctnExtrctPEOMovementId | MOVEMENT_ID | — | ✅ |
| 55 | RcvngRcptTrnsctnExtrctPEOMvtStatStatus | MVT_STAT_STATUS | — | ✅ |
| 56 | RcvngRcptTrnsctnExtrctPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 57 | RcvngRcptTrnsctnExtrctPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 58 | RcvngRcptTrnsctnExtrctPEOPEOAccrualStatusCode | ACCRUAL_STATUS_CODE | — | ✅ |
| 59 | RcvngRcptTrnsctnExtrctPEOPaAdditionFlag | PA_ADDITION_FLAG | — | ✅ |
| 60 | RcvngRcptTrnsctnExtrctPEOParentSpGroupId | PARENT_SP_GROUP_ID | — | ✅ |
| 61 | RcvngRcptTrnsctnExtrctPEOParentTransactionId | PARENT_TRANSACTION_ID | — | ✅ |
| 62 | RcvngRcptTrnsctnExtrctPEOPoDistributionId | PO_DISTRIBUTION_ID | — | ✅ |
| 63 | RcvngRcptTrnsctnExtrctPEOPoHeaderId | PO_HEADER_ID | — | ✅ |
| 64 | RcvngRcptTrnsctnExtrctPEOPoLineId | PO_LINE_ID | — | ✅ |
| 65 | RcvngRcptTrnsctnExtrctPEOPoLineLocationId | PO_LINE_LOCATION_ID | — | ✅ |
| 66 | RcvngRcptTrnsctnExtrctPEOPoRevisionNum | PO_REVISION_NUM | — | ✅ |
| 67 | RcvngRcptTrnsctnExtrctPEOPoUnitPrice | PO_UNIT_PRICE | — | ✅ |
| 68 | RcvngRcptTrnsctnExtrctPEOPricingQuantity | PRICING_QUANTITY | — | ✅ |
| 69 | RcvngRcptTrnsctnExtrctPEOPricingUomCode | PRICING_UOM_CODE | — | ✅ |
| 70 | RcvngRcptTrnsctnExtrctPEOPrimaryQuantity | PRIMARY_QUANTITY | — | ✅ |
| 71 | RcvngRcptTrnsctnExtrctPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 72 | RcvngRcptTrnsctnExtrctPEOProductCategory | PRODUCT_CATEGORY | — | ✅ |
| 73 | RcvngRcptTrnsctnExtrctPEOProductFiscClassId | PRODUCT_FISC_CLASS_ID | — | ✅ |
| 74 | RcvngRcptTrnsctnExtrctPEOProductType | PRODUCT_TYPE | — | ✅ |
| 75 | RcvngRcptTrnsctnExtrctPEOProjectId | PROJECT_ID | — | ✅ |
| 76 | RcvngRcptTrnsctnExtrctPEOQuantity | QUANTITY | — | ✅ |
| 77 | RcvngRcptTrnsctnExtrctPEOQuantityBilled | QUANTITY_BILLED | — | ✅ |
| 78 | RcvngRcptTrnsctnExtrctPEORcptConfMessageNumber | RCPT_CONF_MESSAGE_NUMBER | — | ✅ |
| 79 | RcvngRcptTrnsctnExtrctPEORcptConfStatus | RCPT_CONF_STATUS | — | ✅ |
| 80 | RcvngRcptTrnsctnExtrctPEOReasonId | REASON_ID | — | ✅ |
| 81 | RcvngRcptTrnsctnExtrctPEOReceiptAdviceHeaderId | RECEIPT_ADVICE_HEADER_ID | — | ✅ |
| 82 | RcvngRcptTrnsctnExtrctPEOReceiptAdviceLineId | RECEIPT_ADVICE_LINE_ID | — | ✅ |
| 83 | RcvngRcptTrnsctnExtrctPEOReceiptExceptionFlag | RECEIPT_EXCEPTION_FLAG | — | ✅ |
| 84 | RcvngRcptTrnsctnExtrctPEOReplenishOrderLineId | REPLENISH_ORDER_LINE_ID | — | ✅ |
| 85 | RcvngRcptTrnsctnExtrctPEOReqDistributionId | REQ_DISTRIBUTION_ID | — | ✅ |
| 86 | RcvngRcptTrnsctnExtrctPEORequestId | REQUEST_ID | — | ✅ |
| 87 | RcvngRcptTrnsctnExtrctPEORequisitionLineId | REQUISITION_LINE_ID | — | ✅ |
| 88 | RcvngRcptTrnsctnExtrctPEOReturnForCreditFlag | RETURN_FOR_CREDIT_FLAG | — | — |
| 89 | RcvngRcptTrnsctnExtrctPEORmaReference | RMA_REFERENCE | — | ✅ |
| 90 | RcvngRcptTrnsctnExtrctPEORoutingHeaderId | ROUTING_HEADER_ID | — | ✅ |
| 91 | RcvngRcptTrnsctnExtrctPEORoutingStepId | ROUTING_STEP_ID | — | ✅ |
| 92 | RcvngRcptTrnsctnExtrctPEOSecondaryQuantity | SECONDARY_QUANTITY | — | ✅ |
| 93 | RcvngRcptTrnsctnExtrctPEOSecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 94 | RcvngRcptTrnsctnExtrctPEOShipFromLocationId | SHIP_FROM_LOCATION_ID | — | ✅ |
| 95 | RcvngRcptTrnsctnExtrctPEOShipmentHeaderId | SHIPMENT_HEADER_ID | — | ✅ |
| 96 | RcvngRcptTrnsctnExtrctPEOShipmentLineId | SHIPMENT_LINE_ID | — | ✅ |
| 97 | RcvngRcptTrnsctnExtrctPEOSourceDocQuantity | SOURCE_DOC_QUANTITY | — | ✅ |
| 98 | RcvngRcptTrnsctnExtrctPEOSourceDocUomCode | SOURCE_DOC_UOM_CODE | — | ✅ |
| 99 | RcvngRcptTrnsctnExtrctPEOSourceDocumentCode | SOURCE_DOCUMENT_CODE | — | ✅ |
| 100 | RcvngRcptTrnsctnExtrctPEOSourceTransactionNum | SOURCE_TRANSACTION_NUM | — | ✅ |
| 101 | RcvngRcptTrnsctnExtrctPEOSpGroupId | SP_GROUP_ID | — | ✅ |
| 102 | RcvngRcptTrnsctnExtrctPEOSpQuantity | SP_QUANTITY | — | ✅ |
| 103 | RcvngRcptTrnsctnExtrctPEOSpUomCode | SP_UOM_CODE | — | ✅ |
| 104 | RcvngRcptTrnsctnExtrctPEOSubinventory | SUBINVENTORY | — | ✅ |
| 105 | RcvngRcptTrnsctnExtrctPEOSubstituteUnorderedCode | SUBSTITUTE_UNORDERED_CODE | — | ✅ |
| 106 | RcvngRcptTrnsctnExtrctPEOTaskId | TASK_ID | — | ✅ |
| 107 | RcvngRcptTrnsctnExtrctPEOTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | ✅ |
| 108 | RcvngRcptTrnsctnExtrctPEOTaxInvoiceDate | TAX_INVOICE_DATE | — | ✅ |
| 109 | RcvngRcptTrnsctnExtrctPEOTaxInvoiceNumber | TAX_INVOICE_NUMBER | — | ✅ |
| 110 | RcvngRcptTrnsctnExtrctPEOThirdPtyRegId | THIRD_PTY_REG_ID | — | ✅ |
| 111 | RcvngRcptTrnsctnExtrctPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 112 | RcvngRcptTrnsctnExtrctPEOTransactionId | TRANSACTION_ID | 🔑 | ✅ |
| 113 | RcvngRcptTrnsctnExtrctPEOTransactionType | TRANSACTION_TYPE | — | ✅ |
| 114 | RcvngRcptTrnsctnExtrctPEOTransferLpnId | TRANSFER_LPN_ID | — | ✅ |
| 115 | RcvngRcptTrnsctnExtrctPEOTransferOrderLineId | TRANSFER_ORDER_LINE_ID | — | ✅ |
| 116 | RcvngRcptTrnsctnExtrctPEOTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 117 | RcvngRcptTrnsctnExtrctPEOUomCode | UOM_CODE | — | ✅ |
| 118 | RcvngRcptTrnsctnExtrctPEOUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |
| 119 | RcvngRcptTrnsctnExtrctPEOUserEnteredFlag | USER_ENTERED_FLAG | — | ✅ |
| 120 | RcvngRcptTrnsctnExtrctPEOVendorId | VENDOR_ID | — | ✅ |
| 121 | RcvngRcptTrnsctnExtrctPEOVendorLotNum | VENDOR_LOT_NUM | — | ✅ |
| 122 | RcvngRcptTrnsctnExtrctPEOVendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 123 | ReceivingTransactionPARPEOAccrualStatusCode | ACCRUAL_STATUS_CODE | — | ✅ |
| 124 | ReceivingTransactionPARPEOAmount | AMOUNT | — | ✅ |
| 125 | ReceivingTransactionPARPEOAmountBilled | AMOUNT_BILLED | — | ✅ |
| 126 | ReceivingTransactionPARPEOAssessableValue | ASSESSABLE_VALUE | — | ✅ |
| 127 | ReceivingTransactionPARPEOAttribute | ATTRIBUTE1 | — | — |
| 128 | ReceivingTransactionPARPEOAttribute10 | ATTRIBUTE10 | — | — |
| 129 | ReceivingTransactionPARPEOAttribute11 | ATTRIBUTE11 | — | — |
| 130 | ReceivingTransactionPARPEOAttribute12 | ATTRIBUTE12 | — | — |
| 131 | ReceivingTransactionPARPEOAttribute14 | ATTRIBUTE14 | — | — |
| 132 | ReceivingTransactionPARPEOAttribute15 | ATTRIBUTE15 | — | — |
| 133 | ReceivingTransactionPARPEOAttribute2 | ATTRIBUTE2 | — | — |
| 134 | ReceivingTransactionPARPEOAttribute3 | ATTRIBUTE3 | — | — |
| 135 | ReceivingTransactionPARPEOAttribute4 | ATTRIBUTE4 | — | — |
| 136 | ReceivingTransactionPARPEOAttribute5 | ATTRIBUTE5 | — | — |
| 137 | ReceivingTransactionPARPEOAttribute6 | ATTRIBUTE6 | — | — |
| 138 | ReceivingTransactionPARPEOAttribute7 | ATTRIBUTE7 | — | — |
| 139 | ReceivingTransactionPARPEOAttribute8 | ATTRIBUTE8 | — | — |
| 140 | ReceivingTransactionPARPEOAttribute9 | ATTRIBUTE9 | — | — |
| 141 | ReceivingTransactionPARPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 142 | ReceivingTransactionPARPEOBillingUomCode | BILLING_UOM_CODE | — | ✅ |
| 143 | ReceivingTransactionPARPEOComments | COMMENTS | — | ✅ |
| 144 | ReceivingTransactionPARPEOConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 145 | ReceivingTransactionPARPEOConsumedQuantity | CONSUMED_QUANTITY | — | ✅ |
| 146 | ReceivingTransactionPARPEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 147 | ReceivingTransactionPARPEOCreatedBy | CREATED_BY | — | ✅ |
| 148 | ReceivingTransactionPARPEOCreationDate | CREATION_DATE | — | ✅ |
| 149 | ReceivingTransactionPARPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 150 | ReceivingTransactionPARPEOCurrencyConversionDate | CURRENCY_CONVERSION_DATE | — | ✅ |
| 151 | ReceivingTransactionPARPEOCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 152 | ReceivingTransactionPARPEOCurrencyConversionType | CURRENCY_CONVERSION_TYPE | — | ✅ |
| 153 | ReceivingTransactionPARPEOCustomerId | CUSTOMER_ID | — | ✅ |
| 154 | ReceivingTransactionPARPEOCustomerSiteId | CUSTOMER_SITE_ID | — | ✅ |
| 155 | ReceivingTransactionPARPEODefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | ✅ |
| 156 | ReceivingTransactionPARPEODeliverToLocationId | DELIVER_TO_LOCATION_ID | — | ✅ |
| 157 | ReceivingTransactionPARPEODeliverToPersonId | DELIVER_TO_PERSON_ID | — | ✅ |
| 158 | ReceivingTransactionPARPEODestinationContext | DESTINATION_CONTEXT | — | ✅ |
| 159 | ReceivingTransactionPARPEODestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 160 | ReceivingTransactionPARPEODocumentFiscalClassification | DOCUMENT_FISCAL_CLASSIFICATION | — | ✅ |
| 161 | ReceivingTransactionPARPEOEmployeeId | EMPLOYEE_ID | — | ✅ |
| 162 | ReceivingTransactionPARPEOFinalDischargeLocationId | FINAL_DISCHARGE_LOCATION_ID | — | ✅ |
| 163 | ReceivingTransactionPARPEOFirstPtyRegId | FIRST_PTY_REG_ID | — | ✅ |
| 164 | ReceivingTransactionPARPEOFiscalDocAccessKnum | FISCAL_DOC_ACCESS_KNUM | — | ✅ |
| 165 | ReceivingTransactionPARPEOFiscalDocHeaderId | FISCAL_DOC_HEADER_ID | — | ✅ |
| 166 | ReceivingTransactionPARPEOFiscalDocLineId | FISCAL_DOC_LINE_ID | — | ✅ |
| 167 | ReceivingTransactionPARPEOFiscalDocScheduleId | FISCAL_DOC_SCHEDULE_ID | — | ✅ |
| 168 | ReceivingTransactionPARPEOFromLocatorId | FROM_LOCATOR_ID | — | ✅ |
| 169 | ReceivingTransactionPARPEOFromSubinventory | FROM_SUBINVENTORY | — | ✅ |
| 170 | ReceivingTransactionPARPEOGroupId | GROUP_ID | — | ✅ |
| 171 | ReceivingTransactionPARPEOInspectionQualityCode | INSPECTION_QUALITY_CODE | — | ✅ |
| 172 | ReceivingTransactionPARPEOInspectionStatusCode | INSPECTION_STATUS_CODE | — | ✅ |
| 173 | ReceivingTransactionPARPEOIntendedUseClassifId | INTENDED_USE_CLASSIF_ID | — | ✅ |
| 174 | ReceivingTransactionPARPEOInterfaceGroupId | INTERFACE_GROUP_ID | — | ✅ |
| 175 | ReceivingTransactionPARPEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | ✅ |
| 176 | ReceivingTransactionPARPEOInterfaceSourceLineId | INTERFACE_SOURCE_LINE_ID | — | ✅ |
| 177 | ReceivingTransactionPARPEOInterfaceTransactionId | INTERFACE_TRANSACTION_ID | — | ✅ |
| 178 | ReceivingTransactionPARPEOInvTransactionId | INV_TRANSACTION_ID | — | ✅ |
| 179 | ReceivingTransactionPARPEOInvoiceId | INVOICE_ID | — | ✅ |
| 180 | ReceivingTransactionPARPEOInvoiceStatusCode | INVOICE_STATUS_CODE | — | ✅ |
| 181 | ReceivingTransactionPARPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 182 | ReceivingTransactionPARPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 183 | ReceivingTransactionPARPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 184 | ReceivingTransactionPARPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 185 | ReceivingTransactionPARPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 186 | ReceivingTransactionPARPEOLocationId | LOCATION_ID | — | ✅ |
| 187 | ReceivingTransactionPARPEOLocatorId | LOCATOR_ID | — | ✅ |
| 188 | ReceivingTransactionPARPEOLpnGroupId | LPN_GROUP_ID | — | ✅ |
| 189 | ReceivingTransactionPARPEOLpnId | LPN_ID | — | ✅ |
| 190 | ReceivingTransactionPARPEOMatchFlag | MATCH_FLAG | — | ✅ |
| 191 | ReceivingTransactionPARPEOMatchOption | MATCH_OPTION | — | ✅ |
| 192 | ReceivingTransactionPARPEOMovementId | MOVEMENT_ID | — | ✅ |
| 193 | ReceivingTransactionPARPEOMvtStatStatus | MVT_STAT_STATUS | — | ✅ |
| 194 | ReceivingTransactionPARPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 195 | ReceivingTransactionPARPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 196 | ReceivingTransactionPARPEOPaAdditionFlag | PA_ADDITION_FLAG | — | ✅ |
| 197 | ReceivingTransactionPARPEOParentSpGroupId | PARENT_SP_GROUP_ID | — | ✅ |
| 198 | ReceivingTransactionPARPEOParentTransactionId | PARENT_TRANSACTION_ID | — | ✅ |
| 199 | ReceivingTransactionPARPEOPoDistributionId | PO_DISTRIBUTION_ID | — | ✅ |
| 200 | ReceivingTransactionPARPEOPoHeaderId | PO_HEADER_ID | — | ✅ |
| 201 | ReceivingTransactionPARPEOPoLineId | PO_LINE_ID | — | ✅ |
| 202 | ReceivingTransactionPARPEOPoLineLocationId | PO_LINE_LOCATION_ID | — | ✅ |
| 203 | ReceivingTransactionPARPEOPoRevisionNum | PO_REVISION_NUM | — | ✅ |
| 204 | ReceivingTransactionPARPEOPoUnitPrice | PO_UNIT_PRICE | — | ✅ |
| 205 | ReceivingTransactionPARPEOPricingQuantity | PRICING_QUANTITY | — | ✅ |
| 206 | ReceivingTransactionPARPEOPricingUomCode | PRICING_UOM_CODE | — | ✅ |
| 207 | ReceivingTransactionPARPEOPrimaryQuantity | PRIMARY_QUANTITY | — | ✅ |
| 208 | ReceivingTransactionPARPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 209 | ReceivingTransactionPARPEOProductCategory | PRODUCT_CATEGORY | — | ✅ |
| 210 | ReceivingTransactionPARPEOProductFiscClassId | PRODUCT_FISC_CLASS_ID | — | ✅ |
| 211 | ReceivingTransactionPARPEOProductType | PRODUCT_TYPE | — | ✅ |
| 212 | ReceivingTransactionPARPEOProjectId | PROJECT_ID | — | ✅ |
| 213 | ReceivingTransactionPARPEOQuantity | QUANTITY | — | ✅ |
| 214 | ReceivingTransactionPARPEOQuantityBilled | QUANTITY_BILLED | — | ✅ |
| 215 | ReceivingTransactionPARPEORcptConfMessageNumber | RCPT_CONF_MESSAGE_NUMBER | — | ✅ |
| 216 | ReceivingTransactionPARPEORcptConfStatus | RCPT_CONF_STATUS | — | ✅ |
| 217 | ReceivingTransactionPARPEOReasonId | REASON_ID | — | ✅ |
| 218 | ReceivingTransactionPARPEOReceiptAdviceHeaderId | RECEIPT_ADVICE_HEADER_ID | — | ✅ |
| 219 | ReceivingTransactionPARPEOReceiptAdviceLineId | RECEIPT_ADVICE_LINE_ID | — | ✅ |
| 220 | ReceivingTransactionPARPEOReceiptExceptionFlag | RECEIPT_EXCEPTION_FLAG | — | ✅ |
| 221 | ReceivingTransactionPARPEORefFiscalDocAccessKnum | REF_FISCAL_DOC_ACCESS_KNUM | — | ✅ |
| 222 | ReceivingTransactionPARPEORefFiscalDocHeaderId | REF_FISCAL_DOC_HEADER_ID | — | ✅ |
| 223 | ReceivingTransactionPARPEORefFiscalDocLineId | REF_FISCAL_DOC_LINE_ID | — | ✅ |
| 224 | ReceivingTransactionPARPEORefFiscalDocScheduleId | REF_FISCAL_DOC_SCHEDULE_ID | — | ✅ |
| 225 | ReceivingTransactionPARPEOReplenishOrderLineId | REPLENISH_ORDER_LINE_ID | — | ✅ |
| 226 | ReceivingTransactionPARPEOReqDistributionId | REQ_DISTRIBUTION_ID | — | ✅ |
| 227 | ReceivingTransactionPARPEORequestId | REQUEST_ID | — | ✅ |
| 228 | ReceivingTransactionPARPEORequisitionLineId | REQUISITION_LINE_ID | — | ✅ |
| 229 | ReceivingTransactionPARPEORmaReference | RMA_REFERENCE | — | ✅ |
| 230 | ReceivingTransactionPARPEORoutingHeaderId | ROUTING_HEADER_ID | — | ✅ |
| 231 | ReceivingTransactionPARPEORoutingStepId | ROUTING_STEP_ID | — | ✅ |
| 232 | ReceivingTransactionPARPEOSecondaryQuantity | SECONDARY_QUANTITY | — | ✅ |
| 233 | ReceivingTransactionPARPEOSecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 234 | ReceivingTransactionPARPEOShipFromLocationId | SHIP_FROM_LOCATION_ID | — | ✅ |
| 235 | ReceivingTransactionPARPEOShipmentHeaderId | SHIPMENT_HEADER_ID | — | ✅ |
| 236 | ReceivingTransactionPARPEOShipmentLineId | SHIPMENT_LINE_ID | — | ✅ |
| 237 | ReceivingTransactionPARPEOSourceDocQuantity | SOURCE_DOC_QUANTITY | — | ✅ |
| 238 | ReceivingTransactionPARPEOSourceDocUomCode | SOURCE_DOC_UOM_CODE | — | ✅ |
| 239 | ReceivingTransactionPARPEOSourceDocumentCode | SOURCE_DOCUMENT_CODE | — | ✅ |
| 240 | ReceivingTransactionPARPEOSourceTransactionNum | SOURCE_TRANSACTION_NUM | — | ✅ |
| 241 | ReceivingTransactionPARPEOSpGroupId | SP_GROUP_ID | — | ✅ |
| 242 | ReceivingTransactionPARPEOSpQuantity | SP_QUANTITY | — | ✅ |
| 243 | ReceivingTransactionPARPEOSpUomCode | SP_UOM_CODE | — | ✅ |
| 244 | ReceivingTransactionPARPEOSubinventory | SUBINVENTORY | — | ✅ |
| 245 | ReceivingTransactionPARPEOSubstituteUnorderedCode | SUBSTITUTE_UNORDERED_CODE | — | ✅ |
| 246 | ReceivingTransactionPARPEOTaskId | TASK_ID | — | ✅ |
| 247 | ReceivingTransactionPARPEOTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | ✅ |
| 248 | ReceivingTransactionPARPEOTaxInvoiceDate | TAX_INVOICE_DATE | — | ✅ |
| 249 | ReceivingTransactionPARPEOTaxInvoiceNumber | TAX_INVOICE_NUMBER | — | ✅ |
| 250 | ReceivingTransactionPARPEOThirdPtyRegId | THIRD_PTY_REG_ID | — | ✅ |
| 251 | ReceivingTransactionPARPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 252 | ReceivingTransactionPARPEOTransactionId | TRANSACTION_ID | — | ✅ |
| 253 | ReceivingTransactionPARPEOTransactionId1 | TRANSACTION_ID | — | ✅ |
| 254 | ReceivingTransactionPARPEOTransactionType | TRANSACTION_TYPE | — | ✅ |
| 255 | ReceivingTransactionPARPEOTransferLpnId | TRANSFER_LPN_ID | — | ✅ |
| 256 | ReceivingTransactionPARPEOTransferOrderHeaderId | TRANSFER_ORDER_HEADER_ID | — | ✅ |
| 257 | ReceivingTransactionPARPEOTrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 258 | ReceivingTransactionPARPEOUomCode | UOM_CODE | — | ✅ |
| 259 | ReceivingTransactionPARPEOUserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |
| 260 | ReceivingTransactionPARPEOUserEnteredFlag | USER_ENTERED_FLAG | — | ✅ |
| 261 | ReceivingTransactionPARPEOVendorId | VENDOR_ID | — | ✅ |
| 262 | ReceivingTransactionPARPEOVendorLotNum | VENDOR_LOT_NUM | — | ✅ |
| 263 | ReceivingTransactionPARPEOVendorSiteId | VENDOR_SITE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
