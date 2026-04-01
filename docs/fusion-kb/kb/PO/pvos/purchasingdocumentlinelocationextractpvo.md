---
id: DOC-PO-PVO-PurchasingDocumentLineLocationExtractPVO
doc_type: system-doc
title: "PurchasingDocumentLineLocationExtractPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PurchasingDocumentLineLocationExtractPVO
  - purchasingdocumentlinelocationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingDocumentLineLocationExtractPVO

## 📌 Visão Geral

Extrai as localizações de entrega de cada linha de ordem de compra para carga BICC, incluindo endereço, quantidade e cronograma. Fundamental para logística de recebimento e planejamento de estoques.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoBiccExtractAM.PurchasingDocumentLineLocationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 159 | 1 | 1 | 156 | 98% |

---

## 🔗 Tabelas Relacionadas

- [[po_line_locations_all|PO_LINE_LOCATIONS_ALL]] — 159 atributos (1 PKs, 156 BICC)

---

## ⚙️ Atributos

### [[po_line_locations_all|PO_LINE_LOCATIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccrueOnReceiptFlag | ACCRUE_ON_RECEIPT_FLAG | — | ✅ |
| 2 | AllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | ✅ |
| 3 | Amount | AMOUNT | — | ✅ |
| 4 | AmountAccepted | AMOUNT_ACCEPTED | — | ✅ |
| 5 | AmountBilled | AMOUNT_BILLED | — | ✅ |
| 6 | AmountCancelled | AMOUNT_CANCELLED | — | ✅ |
| 7 | AmountReceived | AMOUNT_RECEIVED | — | ✅ |
| 8 | AmountShipped | AMOUNT_SHIPPED | — | ✅ |
| 9 | AnticipatedArrivalDate | ANTICIPATED_ARRIVAL_DATE | — | ✅ |
| 10 | AssessableValue | ASSESSABLE_VALUE | — | ✅ |
| 11 | BackToBackFlag | BACK_TO_BACK_FLAG | — | ✅ |
| 12 | CalculateTaxFlag | CALCULATE_TAX_FLAG | — | ✅ |
| 13 | CancelBudgetDate | CANCEL_BUDGET_DATE | — | ✅ |
| 14 | CancelDate | CANCEL_DATE | — | ✅ |
| 15 | CancelFlag | CANCEL_FLAG | — | ✅ |
| 16 | CancelReason | CANCEL_REASON | — | ✅ |
| 17 | CancelledBy | CANCELLED_BY | — | ✅ |
| 18 | CarrierId | CARRIER_ID | — | ✅ |
| 19 | ChangePromisedDateReason | CHANGE_PROMISED_DATE_REASON | — | ✅ |
| 20 | ClosedBy | CLOSED_BY | — | ✅ |
| 21 | ClosedDate | CLOSED_DATE | — | ✅ |
| 22 | ClosedDateTime | CLOSED_DATE | — | ✅ |
| 23 | ClosedForInvoiceDate | CLOSED_FOR_INVOICE_DATE | — | ✅ |
| 24 | ClosedForReceivingDate | CLOSED_FOR_RECEIVING_DATE | — | ✅ |
| 25 | ClosedReason | CLOSED_REASON | — | ✅ |
| 26 | ConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 27 | CountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 28 | CreatedBy | CREATED_BY | — | ✅ |
| 29 | CreationDate | CREATION_DATE | — | ✅ |
| 30 | CustomerItem | CUSTOMER_ITEM | — | ✅ |
| 31 | CustomerItemDesc | CUSTOMER_ITEM_DESC | — | ✅ |
| 32 | CustomerPoLineNumber | CUSTOMER_PO_LINE_NUMBER | — | ✅ |
| 33 | CustomerPoNumber | CUSTOMER_PO_NUMBER | — | ✅ |
| 34 | CustomerPoScheduleNumber | CUSTOMER_PO_SCHEDULE_NUMBER | — | ✅ |
| 35 | DaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | ✅ |
| 36 | DaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | ✅ |
| 37 | Description | DESCRIPTION | — | ✅ |
| 38 | DestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 39 | DropShipFlag | DROP_SHIP_FLAG | — | ✅ |
| 40 | EncumberedDate | ENCUMBERED_DATE | — | ✅ |
| 41 | EncumberedFlag | ENCUMBERED_FLAG | — | ✅ |
| 42 | EndDate | END_DATE | — | ✅ |
| 43 | EnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | ✅ |
| 44 | FinalDischargeLocationId | FINAL_DISCHARGE_LOCATION_ID | — | — |
| 45 | FinalMatchFlag | FINAL_MATCH_FLAG | — | — |
| 46 | FirmDate | FIRM_DATE | — | ✅ |
| 47 | FirmFlag | FIRM_FLAG | — | ✅ |
| 48 | FirmReason | FIRM_REASON | — | ✅ |
| 49 | FirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | ✅ |
| 50 | FirmedBy | FIRMED_BY | — | ✅ |
| 51 | FobLookupCode | FOB_LOOKUP_CODE | — | ✅ |
| 52 | FreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | ✅ |
| 53 | FromHeaderId | FROM_HEADER_ID | — | ✅ |
| 54 | FromLineId | FROM_LINE_ID | — | ✅ |
| 55 | FromLineLocationId | FROM_LINE_LOCATION_ID | — | ✅ |
| 56 | FundsStatus | FUNDS_STATUS | — | ✅ |
| 57 | InputTaxClassificationCode | INPUT_TAX_CLASSIFICATION_CODE | — | ✅ |
| 58 | InspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | ✅ |
| 59 | InvoiceCloseTolerance | INVOICE_CLOSE_TOLERANCE | — | ✅ |
| 60 | LastAcceptDate | LAST_ACCEPT_DATE | — | ✅ |
| 61 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 62 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 63 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 64 | LineLocationId | LINE_LOCATION_ID | 🔑 | ✅ |
| 65 | ManualPriceChangeFlag | MANUAL_PRICE_CHANGE_FLAG | — | ✅ |
| 66 | MatchOption | MATCH_OPTION | — | ✅ |
| 67 | MatchingBasis | MATCHING_BASIS | — | ✅ |
| 68 | ModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 69 | NeedByDate | NEED_BY_DATE | — | ✅ |
| 70 | NoteToReceiver | NOTE_TO_RECEIVER | — | ✅ |
| 71 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 72 | OrchestrationCode | ORCHESTRATION_CODE | — | ✅ |
| 73 | OriginalShipmentId | ORIGINAL_SHIPMENT_ID | — | ✅ |
| 74 | PaymentType | PAYMENT_TYPE | — | ✅ |
| 75 | PoHeaderId | PO_HEADER_ID | — | ✅ |
| 76 | PoLineId | PO_LINE_ID | — | ✅ |
| 77 | PoTradingOrganizationId | PO_TRADING_ORGANIZATION_ID | — | ✅ |
| 78 | PrcBuId | PRC_BU_ID | — | ✅ |
| 79 | PriceDiscount | PRICE_DISCOUNT | — | ✅ |
| 80 | PriceOverride | PRICE_OVERRIDE | — | ✅ |
| 81 | ProductCategory | PRODUCT_CATEGORY | — | ✅ |
| 82 | ProductFiscClassId | PRODUCT_FISC_CLASS_ID | — | ✅ |
| 83 | ProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | ✅ |
| 84 | ProductType | PRODUCT_TYPE | — | ✅ |
| 85 | PromisedDate | PROMISED_DATE | — | ✅ |
| 86 | PromisedShipDate | PROMISED_SHIP_DATE | — | ✅ |
| 87 | QtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | ✅ |
| 88 | QtyRcvTolerance | QTY_RCV_TOLERANCE | — | ✅ |
| 89 | Quantity | QUANTITY | — | ✅ |
| 90 | QuantityAccepted | QUANTITY_ACCEPTED | — | ✅ |
| 91 | QuantityBilled | QUANTITY_BILLED | — | ✅ |
| 92 | QuantityCancelled | QUANTITY_CANCELLED | — | ✅ |
| 93 | QuantityReceived | QUANTITY_RECEIVED | — | ✅ |
| 94 | QuantityRejected | QUANTITY_REJECTED | — | ✅ |
| 95 | QuantityShipped | QUANTITY_SHIPPED | — | ✅ |
| 96 | ReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | ✅ |
| 97 | ReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | ✅ |
| 98 | ReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | ✅ |
| 99 | ReceivingRoutingId | RECEIVING_ROUTING_ID | — | ✅ |
| 100 | ReopenFinalCloseDate | REOPEN_FINAL_CLOSE_DATE | — | ✅ |
| 101 | ReqBuId | REQ_BU_ID | — | ✅ |
| 102 | RequestId | REQUEST_ID | — | ✅ |
| 103 | RequestedShipDate | REQUESTED_SHIP_DATE | — | ✅ |
| 104 | RetainageRate | RETAINAGE_RATE | — | ✅ |
| 105 | RetainageReleasedAmount | RETAINAGE_RELEASED_AMOUNT | — | ✅ |
| 106 | RetainageWithheldAmount | RETAINAGE_WITHHELD_AMOUNT | — | ✅ |
| 107 | RetroactiveDate | RETROACTIVE_DATE | — | ✅ |
| 108 | SalesOrderLineNumber | SALES_ORDER_LINE_NUMBER | — | ✅ |
| 109 | SalesOrderNumber | SALES_ORDER_NUMBER | — | ✅ |
| 110 | SalesOrderScheduleNumber | SALES_ORDER_SCHEDULE_NUMBER | — | ✅ |
| 111 | SalesOrderUpdateDate | SALES_ORDER_UPDATE_DATE | — | ✅ |
| 112 | ScheduleStatus | SCHEDULE_STATUS | — | ✅ |
| 113 | SecondaryQuantity | SECONDARY_QUANTITY | — | ✅ |
| 114 | SecondaryQuantityAccepted | SECONDARY_QUANTITY_ACCEPTED | — | ✅ |
| 115 | SecondaryQuantityCancelled | SECONDARY_QUANTITY_CANCELLED | — | ✅ |
| 116 | SecondaryQuantityReceived | SECONDARY_QUANTITY_RECEIVED | — | ✅ |
| 117 | SecondaryQuantityRejected | SECONDARY_QUANTITY_REJECTED | — | ✅ |
| 118 | SecondaryQuantityShipped | SECONDARY_QUANTITY_SHIPPED | — | ✅ |
| 119 | SecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 120 | ServiceLevel | SERVICE_LEVEL | — | ✅ |
| 121 | SfoAgreementLineNumber | SFO_AGREEMENT_LINE_NUMBER | — | ✅ |
| 122 | SfoAgreementNumber | SFO_AGREEMENT_NUMBER | — | ✅ |
| 123 | SfoPtrId | SFO_PTR_ID | — | ✅ |
| 124 | ShipToCustContactId | SHIP_TO_CUST_CONTACT_ID | — | ✅ |
| 125 | ShipToCustId | SHIP_TO_CUST_ID | — | ✅ |
| 126 | ShipToCustLocationId | SHIP_TO_CUST_LOCATION_ID | — | ✅ |
| 127 | ShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 128 | ShipToOrganizationId | SHIP_TO_ORGANIZATION_ID | — | ✅ |
| 129 | ShipmentClosedDate | SHIPMENT_CLOSED_DATE | — | ✅ |
| 130 | ShipmentNum | SHIPMENT_NUM | — | ✅ |
| 131 | ShipmentType | SHIPMENT_TYPE | — | ✅ |
| 132 | ShippingUomCode | SHIPPING_UOM_CODE | — | ✅ |
| 133 | ShippingUomQuantity | SHIPPING_UOM_QUANTITY | — | ✅ |
| 134 | ShippingUomQuantityAccepted | SHIPPING_UOM_QUANTITY_ACCEPTED | — | ✅ |
| 135 | ShippingUomQuantityCanceled | SHIPPING_UOM_QUANTITY_CANCELED | — | ✅ |
| 136 | ShippingUomQuantityReceived | SHIPPING_UOM_QUANTITY_RECEIVED | — | ✅ |
| 137 | ShippingUomQuantityRejected | SHIPPING_UOM_QUANTITY_REJECTED | — | ✅ |
| 138 | ShippingUomQuantityShipped | SHIPPING_UOM_QUANTITY_SHIPPED | — | ✅ |
| 139 | SourceShipmentId | SOURCE_SHIPMENT_ID | — | ✅ |
| 140 | StartDate | START_DATE | — | ✅ |
| 141 | SupplierOrderLineNumber | SUPPLIER_ORDER_LINE_NUMBER | — | ✅ |
| 142 | TaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | ✅ |
| 143 | TaxCodeId | TAX_CODE_ID | — | ✅ |
| 144 | TaxUserOverrideFlag | TAX_USER_OVERRIDE_FLAG | — | ✅ |
| 145 | TaxableFlag | TAXABLE_FLAG | — | ✅ |
| 146 | TermsId | TERMS_ID | — | ✅ |
| 147 | TransactionFlowHeaderId | TRANSACTION_FLOW_HEADER_ID | — | — |
| 148 | TrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 149 | UnencumberedQuantity | UNENCUMBERED_QUANTITY | — | ✅ |
| 150 | UnitOfMeasureClass | UNIT_OF_MEASURE_CLASS | — | ✅ |
| 151 | UomCode | UOM_CODE | — | ✅ |
| 152 | UserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |
| 153 | ValueBasis | VALUE_BASIS | — | ✅ |
| 154 | WorkApproverId | WORK_APPROVER_ID | — | ✅ |
| 155 | WorkOrderId | WORK_ORDER_ID | — | ✅ |
| 156 | WorkOrderNumber | WORK_ORDER_NUMBER | — | ✅ |
| 157 | WorkOrderOperationId | WORK_ORDER_OPERATION_ID | — | ✅ |
| 158 | WorkOrderOperationSeq | WORK_ORDER_OPERATION_SEQ | — | ✅ |
| 159 | WorkOrderSubType | WORK_ORDER_SUB_TYPE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
