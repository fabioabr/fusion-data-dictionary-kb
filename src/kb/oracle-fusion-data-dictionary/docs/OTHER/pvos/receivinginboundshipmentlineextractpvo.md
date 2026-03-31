---
id: DOC-OTHER-PVO-ReceivingInboundShipmentLineExtractPVO
doc_type: system-doc
title: "ReceivingInboundShipmentLineExtractPVO — PVO Cross-Module"
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
  - ReceivingInboundShipmentLineExtractPVO
  - receivinginboundshipmentlineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReceivingInboundShipmentLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Receiving Inbound Shipment Line Extract. Acessa as tabelas: RCV_SHIPMENT_LINES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.RcvBiccExtractAM.ReceivingInboundShipmentLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 197 | 1 | 1 | 150 | 76% |

---

## 🔗 Tabelas Relacionadas

- [[rcv_shipment_lines|RCV_SHIPMENT_LINES]] — 197 atributos (1 PKs, 150 BICC)

---

## ⚙️ Atributos

### [[rcv_shipment_lines|RCV_SHIPMENT_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Amount | AMOUNT | — | ✅ |
| 2 | AmountReceived | AMOUNT_RECEIVED | — | ✅ |
| 3 | AmountShipped | AMOUNT_SHIPPED | — | ✅ |
| 4 | AsnLineFlag | ASN_LINE_FLAG | — | ✅ |
| 5 | AsnLpnId | ASN_LPN_ID | — | ✅ |
| 6 | AssessableValue | ASSESSABLE_VALUE | — | ✅ |
| 7 | Attribute1 | ATTRIBUTE1 | — | — |
| 8 | Attribute10 | ATTRIBUTE10 | — | — |
| 9 | Attribute11 | ATTRIBUTE11 | — | — |
| 10 | Attribute12 | ATTRIBUTE12 | — | — |
| 11 | Attribute13 | ATTRIBUTE13 | — | — |
| 12 | Attribute14 | ATTRIBUTE14 | — | — |
| 13 | Attribute15 | ATTRIBUTE15 | — | — |
| 14 | Attribute16 | ATTRIBUTE16 | — | — |
| 15 | Attribute17 | ATTRIBUTE17 | — | — |
| 16 | Attribute18 | ATTRIBUTE18 | — | — |
| 17 | Attribute19 | ATTRIBUTE19 | — | — |
| 18 | Attribute2 | ATTRIBUTE2 | — | — |
| 19 | Attribute20 | ATTRIBUTE20 | — | — |
| 20 | Attribute3 | ATTRIBUTE3 | — | ✅ |
| 21 | Attribute4 | ATTRIBUTE4 | — | — |
| 22 | Attribute5 | ATTRIBUTE5 | — | ✅ |
| 23 | Attribute6 | ATTRIBUTE6 | — | — |
| 24 | Attribute7 | ATTRIBUTE7 | — | — |
| 25 | Attribute8 | ATTRIBUTE8 | — | — |
| 26 | Attribute9 | ATTRIBUTE9 | — | — |
| 27 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 28 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 29 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 30 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 31 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 32 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 33 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 34 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 35 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 36 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 37 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 38 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 39 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 40 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 41 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 42 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 43 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 44 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 45 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 46 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 47 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 48 | BackToBackFlag | BACK_TO_BACK_FLAG | — | ✅ |
| 49 | BarCodeLabel | BAR_CODE_LABEL | — | ✅ |
| 50 | CategoryId | CATEGORY_ID | — | ✅ |
| 51 | Comments | COMMENTS | — | ✅ |
| 52 | ConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 53 | ConsumedQuantity | CONSUMED_QUANTITY | — | ✅ |
| 54 | ContainerNum | CONTAINER_NUM | — | ✅ |
| 55 | CountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 56 | CreatedBy | CREATED_BY | — | ✅ |
| 57 | CreationDate | CREATION_DATE | — | ✅ |
| 58 | CustomerId | CUSTOMER_ID | — | ✅ |
| 59 | CustomerItemId | CUSTOMER_ITEM_ID | — | ✅ |
| 60 | CustomerItemNum | CUSTOMER_ITEM_NUM | — | ✅ |
| 61 | CustomerSiteId | CUSTOMER_SITE_ID | — | ✅ |
| 62 | DefaultTaxationCountry | DEFAULT_TAXATION_COUNTRY | — | ✅ |
| 63 | DeliverToLocationId | DELIVER_TO_LOCATION_ID | — | ✅ |
| 64 | DeliverToPersonId | DELIVER_TO_PERSON_ID | — | ✅ |
| 65 | DestinationContext | DESTINATION_CONTEXT | — | ✅ |
| 66 | DestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 67 | DocumentFiscalClassification | DOCUMENT_FISCAL_CLASSIFICATION | — | ✅ |
| 68 | EmployeeId | EMPLOYEE_ID | — | ✅ |
| 69 | EwayBillDate | EWAY_BILL_DATE | — | ✅ |
| 70 | EwayBillNumber | EWAY_BILL_NUMBER | — | ✅ |
| 71 | ExcessTransportReason | EXCESS_TRANSPORT_REASON | — | ✅ |
| 72 | ExternalSysIntfStatus | EXTERNAL_SYS_INTF_STATUS | — | ✅ |
| 73 | FinalDischargeLocationId | FINAL_DISCHARGE_LOCATION_ID | — | ✅ |
| 74 | FirstPtyRegId | FIRST_PTY_REG_ID | — | ✅ |
| 75 | FromOrganizationId | FROM_ORGANIZATION_ID | — | ✅ |
| 76 | GovernmentContext | GOVERNMENT_CONTEXT | — | ✅ |
| 77 | IntendedUse | INTENDED_USE | — | ✅ |
| 78 | IntendedUseClassifId | INTENDED_USE_CLASSIF_ID | — | ✅ |
| 79 | InterfaceTransactionId | INTERFACE_TRANSACTION_ID | — | ✅ |
| 80 | InvReservedAttribute1 | INV_RESERVED_ATTRIBUTE1 | — | — |
| 81 | InvReservedAttribute2 | INV_RESERVED_ATTRIBUTE2 | — | — |
| 82 | InvStripingCategory | INV_STRIPING_CATEGORY | — | ✅ |
| 83 | InvUserDefAttribute1 | INV_USER_DEF_ATTRIBUTE1 | — | — |
| 84 | InvUserDefAttribute10 | INV_USER_DEF_ATTRIBUTE10 | — | ✅ |
| 85 | InvUserDefAttribute2 | INV_USER_DEF_ATTRIBUTE2 | — | — |
| 86 | InvUserDefAttribute3 | INV_USER_DEF_ATTRIBUTE3 | — | — |
| 87 | InvUserDefAttribute4 | INV_USER_DEF_ATTRIBUTE4 | — | — |
| 88 | InvUserDefAttribute5 | INV_USER_DEF_ATTRIBUTE5 | — | — |
| 89 | InvUserDefAttribute6 | INV_USER_DEF_ATTRIBUTE6 | — | — |
| 90 | InvUserDefAttribute7 | INV_USER_DEF_ATTRIBUTE7 | — | — |
| 91 | InvUserDefAttribute8 | INV_USER_DEF_ATTRIBUTE8 | — | ✅ |
| 92 | InvUserDefAttribute9 | INV_USER_DEF_ATTRIBUTE9 | — | ✅ |
| 93 | InvoiceStatusCode | INVOICE_STATUS_CODE | — | ✅ |
| 94 | ItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 95 | ItemId | ITEM_ID | — | ✅ |
| 96 | ItemRevision | ITEM_REVISION | — | ✅ |
| 97 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 98 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 99 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 100 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 101 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 102 | LineNum | LINE_NUM | — | ✅ |
| 103 | LocatorId | LOCATOR_ID | — | ✅ |
| 104 | MmtTransactionId | MMT_TRANSACTION_ID | — | ✅ |
| 105 | NoticeUnitPrice | NOTICE_UNIT_PRICE | — | ✅ |
| 106 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 107 | OrigToInvShipTxnId | ORIG_TO_INV_SHIP_TXN_ID | — | ✅ |
| 108 | PackingSlip | PACKING_SLIP | — | ✅ |
| 109 | PoDistributionId | PO_DISTRIBUTION_ID | — | ✅ |
| 110 | PoHeaderId | PO_HEADER_ID | — | ✅ |
| 111 | PoLineId | PO_LINE_ID | — | ✅ |
| 112 | PoLineLocationId | PO_LINE_LOCATION_ID | — | ✅ |
| 113 | PrimaryUomCode | PRIMARY_UOM_CODE | — | ✅ |
| 114 | ProductCategory | PRODUCT_CATEGORY | — | ✅ |
| 115 | ProductFiscClassId | PRODUCT_FISC_CLASS_ID | — | ✅ |
| 116 | ProductType | PRODUCT_TYPE | — | ✅ |
| 117 | ProjectId | PROJECT_ID | — | ✅ |
| 118 | QuantityAccepted | QUANTITY_ACCEPTED | — | ✅ |
| 119 | QuantityDelivered | QUANTITY_DELIVERED | — | ✅ |
| 120 | QuantityReceived | QUANTITY_RECEIVED | — | ✅ |
| 121 | QuantityRejected | QUANTITY_REJECTED | — | ✅ |
| 122 | QuantityReturned | QUANTITY_RETURNED | — | ✅ |
| 123 | QuantityShipped | QUANTITY_SHIPPED | — | ✅ |
| 124 | RaAllowSubstituteReceipt | RA_ALLOW_SUBSTITUTE_RECEIPT | — | ✅ |
| 125 | RaDaysEarlyReceiptAllowed | RA_DAYS_EARLY_RECEIPT_ALLOWED | — | ✅ |
| 126 | RaDaysLateReceiptAllowed | RA_DAYS_LATE_RECEIPT_ALLOWED | — | ✅ |
| 127 | RaDocLineCreationDate | RA_DOC_LINE_CREATION_DATE | — | ✅ |
| 128 | RaDocLineLastUpdateDate | RA_DOC_LINE_LAST_UPDATE_DATE | — | ✅ |
| 129 | RaDocScheduleNumber | RA_DOC_SCHEDULE_NUMBER | — | ✅ |
| 130 | RaDocumentLineNumber | RA_DOCUMENT_LINE_NUMBER | — | ✅ |
| 131 | RaDooFulfillmentLineNumber | RA_DOO_FULFILLMENT_LINE_NUMBER | — | ✅ |
| 132 | RaDooHeaderNumber | RA_DOO_HEADER_NUMBER | — | ✅ |
| 133 | RaDooLineNumber | RA_DOO_LINE_NUMBER | — | ✅ |
| 134 | RaEnforceShipToLocCode | RA_ENFORCE_SHIP_TO_LOC_CODE | — | ✅ |
| 135 | RaExpectedReceiptDate | RA_EXPECTED_RECEIPT_DATE | — | ✅ |
| 136 | RaLastActionCode | RA_LAST_ACTION_CODE | — | ✅ |
| 137 | RaMessageNumber | RA_MESSAGE_NUMBER | — | ✅ |
| 138 | RaNoteToReceiver | RA_NOTE_TO_RECEIVER | — | ✅ |
| 139 | RaOrigDooFulfilLineNum | RA_ORIG_DOO_FULFIL_LINE_NUM | — | ✅ |
| 140 | RaOrigDooHeaderNumber | RA_ORIG_DOO_HEADER_NUMBER | — | ✅ |
| 141 | RaOrigDooLineNumber | RA_ORIG_DOO_LINE_NUMBER | — | ✅ |
| 142 | RaOrigOcHeaderNumber | RA_ORIG_OC_HEADER_NUMBER | — | ✅ |
| 143 | RaOrigOcLineNumber | RA_ORIG_OC_LINE_NUMBER | — | ✅ |
| 144 | RaQtyRcvExceptionCode | RA_QTY_RCV_EXCEPTION_CODE | — | ✅ |
| 145 | RaQtyRcvTolerance | RA_QTY_RCV_TOLERANCE | — | ✅ |
| 146 | RaQuantityExpected | RA_QUANTITY_EXPECTED | — | ✅ |
| 147 | RaReceiptDaysExceptionCode | RA_RECEIPT_DAYS_EXCEPTION_CODE | — | ✅ |
| 148 | RaSecondaryQuantityExpected | RA_SECONDARY_QUANTITY_EXPECTED | — | ✅ |
| 149 | RaUnitPrice | RA_UNIT_PRICE | — | ✅ |
| 150 | ReasonId | REASON_ID | — | ✅ |
| 151 | ReceiptAdviceHeaderId | RECEIPT_ADVICE_HEADER_ID | — | ✅ |
| 152 | ReceiptAdviceLineId | RECEIPT_ADVICE_LINE_ID | — | ✅ |
| 153 | ReceiptAdviceLineNumber | RECEIPT_ADVICE_LINE_NUMBER | — | ✅ |
| 154 | ReqDistributionId | REQ_DISTRIBUTION_ID | — | ✅ |
| 155 | RequestId | REQUEST_ID | — | ✅ |
| 156 | RequisitionLineId | REQUISITION_LINE_ID | — | ✅ |
| 157 | RoutingHeaderId | ROUTING_HEADER_ID | — | ✅ |
| 158 | SecondaryQtyAccepted | SECONDARY_QTY_ACCEPTED | — | ✅ |
| 159 | SecondaryQtyDelivered | SECONDARY_QTY_DELIVERED | — | ✅ |
| 160 | SecondaryQtyRejected | SECONDARY_QTY_REJECTED | — | ✅ |
| 161 | SecondaryQtyReturned | SECONDARY_QTY_RETURNED | — | ✅ |
| 162 | SecondaryQuantityReceived | SECONDARY_QUANTITY_RECEIVED | — | ✅ |
| 163 | SecondaryQuantityShipped | SECONDARY_QUANTITY_SHIPPED | — | ✅ |
| 164 | SecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 165 | ShipFromLocationId | SHIP_FROM_LOCATION_ID | — | ✅ |
| 166 | ShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 167 | ShipmentHeaderId | SHIPMENT_HEADER_ID | — | ✅ |
| 168 | ShipmentLineId | SHIPMENT_LINE_ID | 🔑 | ✅ |
| 169 | ShipmentLineStatusCode | SHIPMENT_LINE_STATUS_CODE | — | ✅ |
| 170 | ShipmentUnitPrice | SHIPMENT_UNIT_PRICE | — | ✅ |
| 171 | SourceDocumentCode | SOURCE_DOCUMENT_CODE | — | ✅ |
| 172 | SpGroupId | SP_GROUP_ID | — | ✅ |
| 173 | SpQuantity | SP_QUANTITY | — | ✅ |
| 174 | SpUomCode | SP_UOM_CODE | — | ✅ |
| 175 | TaskId | TASK_ID | — | ✅ |
| 176 | TaxAmount | TAX_AMOUNT | — | ✅ |
| 177 | TaxClassificationCode | TAX_CLASSIFICATION_CODE | — | ✅ |
| 178 | TaxInvoiceDate | TAX_INVOICE_DATE | — | ✅ |
| 179 | TaxInvoiceNumber | TAX_INVOICE_NUMBER | — | ✅ |
| 180 | TaxName | TAX_NAME | — | ✅ |
| 181 | ThirdPtyRegId | THIRD_PTY_REG_ID | — | ✅ |
| 182 | ToOrganizationId | TO_ORGANIZATION_ID | — | ✅ |
| 183 | ToSubinventory | TO_SUBINVENTORY | — | ✅ |
| 184 | TransferCost | TRANSFER_COST | — | ✅ |
| 185 | TransferOrderHeaderId | TRANSFER_ORDER_HEADER_ID | — | ✅ |
| 186 | TransferOrderLineId | TRANSFER_ORDER_LINE_ID | — | ✅ |
| 187 | TransferPercentage | TRANSFER_PERCENTAGE | — | ✅ |
| 188 | TransportationCost | TRANSPORTATION_COST | — | ✅ |
| 189 | TruckNum | TRUCK_NUM | — | ✅ |
| 190 | TrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 191 | UomCode | UOM_CODE | — | ✅ |
| 192 | UserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |
| 193 | VendorCumShippedQuantity | VENDOR_CUM_SHIPPED_QUANTITY | — | ✅ |
| 194 | VendorItemNum | VENDOR_ITEM_NUM | — | ✅ |
| 195 | VendorLotNum | VENDOR_LOT_NUM | — | ✅ |
| 196 | WorkConfirmationId | WORK_CONFIRMATION_ID | — | ✅ |
| 197 | WorkConfirmationLineId | WORK_CONFIRMATION_LINE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
