---
id: DOC-PO-PVO-DraftPurchasingDocumentLineLocationExtractPVO
doc_type: system-doc
title: "DraftPurchasingDocumentLineLocationExtractPVO — PVO Purchasing"
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
  - DraftPurchasingDocumentLineLocationExtractPVO
  - draftpurchasingdocumentlinelocationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DraftPurchasingDocumentLineLocationExtractPVO

## 📌 Visão Geral

Extrai as localizações de entrega de rascunhos de documentos de compra para carga BICC. Permite planejamento logístico antecipado mesmo para pedidos ainda não aprovados.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoBiccExtractAM.DraftPurchasingDocumentLineLocationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 142 | 1 | 1 | 140 | 99% |

---

## 🔗 Tabelas Relacionadas

- [[po_line_locations_draft_all|PO_LINE_LOCATIONS_DRAFT_ALL]] — 142 atributos (1 PKs, 140 BICC)

---

## ⚙️ Atributos

### [[po_line_locations_draft_all|PO_LINE_LOCATIONS_DRAFT_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccrueOnReceiptFlag | ACCRUE_ON_RECEIPT_FLAG | — | ✅ |
| 2 | AllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | ✅ |
| 3 | Amount | AMOUNT | — | ✅ |
| 4 | AssessableValue | ASSESSABLE_VALUE | — | ✅ |
| 5 | BackToBackFlag | BACK_TO_BACK_FLAG | — | ✅ |
| 6 | BidPaymentId | BID_PAYMENT_ID | — | ✅ |
| 7 | CalculateTaxFlag | CALCULATE_TAX_FLAG | — | ✅ |
| 8 | CancelBackingReqFlag | CANCEL_BACKING_REQ_FLAG | — | ✅ |
| 9 | CancelBudgetDate | CANCEL_BUDGET_DATE | — | ✅ |
| 10 | CancelDate | CANCEL_DATE | — | ✅ |
| 11 | CancelFlag | CANCEL_FLAG | — | ✅ |
| 12 | CancelReason | CANCEL_REASON | — | ✅ |
| 13 | CancelledBy | CANCELLED_BY | — | ✅ |
| 14 | CarrierId | CARRIER_ID | — | ✅ |
| 15 | ChangeAcceptedFlag | CHANGE_ACCEPTED_FLAG | — | ✅ |
| 16 | ChangePromisedDateReason | CHANGE_PROMISED_DATE_REASON | — | ✅ |
| 17 | CoAmountCancelled | CO_AMOUNT_CANCELLED | — | ✅ |
| 18 | CoQuantityCancelled | CO_QUANTITY_CANCELLED | — | ✅ |
| 19 | ConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 20 | CountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 21 | CreatedBy | CREATED_BY | — | ✅ |
| 22 | CreationDate | CREATION_DATE | — | ✅ |
| 23 | CustomerItem | CUSTOMER_ITEM | — | ✅ |
| 24 | CustomerItemDesc | CUSTOMER_ITEM_DESC | — | ✅ |
| 25 | CustomerPoLineNumber | CUSTOMER_PO_LINE_NUMBER | — | ✅ |
| 26 | CustomerPoNumber | CUSTOMER_PO_NUMBER | — | ✅ |
| 27 | CustomerPoScheduleNumber | CUSTOMER_PO_SCHEDULE_NUMBER | — | ✅ |
| 28 | DaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | ✅ |
| 29 | DaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | ✅ |
| 30 | Description | DESCRIPTION | — | ✅ |
| 31 | DestinationTypeCode | DESTINATION_TYPE_CODE | — | ✅ |
| 32 | DropShipFlag | DROP_SHIP_FLAG | — | ✅ |
| 33 | EncumberedDate | ENCUMBERED_DATE | — | ✅ |
| 34 | EncumberedFlag | ENCUMBERED_FLAG | — | ✅ |
| 35 | EndDate | END_DATE | — | ✅ |
| 36 | EnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | ✅ |
| 37 | EntityChangeTypeCode | ENTITY_CHANGE_TYPE_CODE | — | ✅ |
| 38 | ExternalChangeFlag | EXTERNAL_CHANGE_FLAG | — | ✅ |
| 39 | FinalDischargeLocationId | FINAL_DISCHARGE_LOCATION_ID | — | — |
| 40 | FirmDate | FIRM_DATE | — | ✅ |
| 41 | FirmStatusLookupCode | FIRM_STATUS_LOOKUP_CODE | — | ✅ |
| 42 | FobLookupCode | FOB_LOOKUP_CODE | — | ✅ |
| 43 | FreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | ✅ |
| 44 | FromHeaderId | FROM_HEADER_ID | — | ✅ |
| 45 | FromLineId | FROM_LINE_ID | — | ✅ |
| 46 | FromLineLocationId | FROM_LINE_LOCATION_ID | — | ✅ |
| 47 | FundsStatus | FUNDS_STATUS | — | ✅ |
| 48 | InputTaxClassificationCode | INPUT_TAX_CLASSIFICATION_CODE | — | ✅ |
| 49 | InspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | ✅ |
| 50 | InvoiceCloseTolerance | INVOICE_CLOSE_TOLERANCE | — | ✅ |
| 51 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 52 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 53 | LastAcceptDate | LAST_ACCEPT_DATE | — | ✅ |
| 54 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 55 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 56 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 57 | LeadTime | LEAD_TIME | — | ✅ |
| 58 | LeadTimeUnit | LEAD_TIME_UNIT | — | ✅ |
| 59 | LineIntendedUse | LINE_INTENDED_USE | — | ✅ |
| 60 | LineIntendedUseId | LINE_INTENDED_USE_ID | — | ✅ |
| 61 | LineLocationId | LINE_LOCATION_ID | 🔑 | ✅ |
| 62 | ManualPriceChangeFlag | MANUAL_PRICE_CHANGE_FLAG | — | ✅ |
| 63 | MatchOption | MATCH_OPTION | — | ✅ |
| 64 | MatchingBasis | MATCHING_BASIS | — | ✅ |
| 65 | ModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 66 | NeedByDate | NEED_BY_DATE | — | ✅ |
| 67 | NoteToReceiver | NOTE_TO_RECEIVER | — | ✅ |
| 68 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 69 | OriginalShipmentId | ORIGINAL_SHIPMENT_ID | — | ✅ |
| 70 | OutsourcedAssembly | OUTSOURCED_ASSEMBLY | — | ✅ |
| 71 | PaymentType | PAYMENT_TYPE | — | ✅ |
| 72 | PjcContextCategory | PJC_CONTEXT_CATEGORY | — | ✅ |
| 73 | PoHeaderId | PO_HEADER_ID | — | ✅ |
| 74 | PoLineId | PO_LINE_ID | — | ✅ |
| 75 | PoTradingOrganizationId | PO_TRADING_ORGANIZATION_ID | — | ✅ |
| 76 | PrcBuId | PRC_BU_ID | — | ✅ |
| 77 | PreferredGrade | PREFERRED_GRADE | — | ✅ |
| 78 | PriceDiscount | PRICE_DISCOUNT | — | ✅ |
| 79 | PriceOverride | PRICE_OVERRIDE | — | ✅ |
| 80 | ProductCategory | PRODUCT_CATEGORY | — | ✅ |
| 81 | ProductFiscClassId | PRODUCT_FISC_CLASS_ID | — | ✅ |
| 82 | ProductFiscClassification | PRODUCT_FISC_CLASSIFICATION | — | ✅ |
| 83 | ProductType | PRODUCT_TYPE | — | ✅ |
| 84 | ProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 85 | ProgramName | PROGRAM_NAME | — | ✅ |
| 86 | PromisedDate | PROMISED_DATE | — | ✅ |
| 87 | PromisedShipDate | PROMISED_SHIP_DATE | — | ✅ |
| 88 | QtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | ✅ |
| 89 | QtyRcvTolerance | QTY_RCV_TOLERANCE | — | ✅ |
| 90 | Quantity | QUANTITY | — | ✅ |
| 91 | ReasonForChange | REASON_FOR_CHANGE | — | ✅ |
| 92 | ReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | ✅ |
| 93 | ReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | ✅ |
| 94 | ReceiveCloseTolerance | RECEIVE_CLOSE_TOLERANCE | — | ✅ |
| 95 | ReceivingRoutingId | RECEIVING_ROUTING_ID | — | ✅ |
| 96 | RejectedBy | REJECTED_BY | — | ✅ |
| 97 | RejectedByRole | REJECTED_BY_ROLE | — | ✅ |
| 98 | RejectedReason | REJECTED_REASON | — | ✅ |
| 99 | ReqBuId | REQ_BU_ID | — | ✅ |
| 100 | RequestId | REQUEST_ID | — | ✅ |
| 101 | RequestedShipDate | REQUESTED_SHIP_DATE | — | ✅ |
| 102 | RetainageRate | RETAINAGE_RATE | — | ✅ |
| 103 | RetroactiveDate | RETROACTIVE_DATE | — | ✅ |
| 104 | SalesOrderLineNumber | SALES_ORDER_LINE_NUMBER | — | ✅ |
| 105 | SalesOrderNumber | SALES_ORDER_NUMBER | — | ✅ |
| 106 | SalesOrderScheduleNumber | SALES_ORDER_SCHEDULE_NUMBER | — | ✅ |
| 107 | SalesOrderUpdateDate | SALES_ORDER_UPDATE_DATE | — | ✅ |
| 108 | SecondaryQuantity | SECONDARY_QUANTITY | — | ✅ |
| 109 | SecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 110 | ServiceLevel | SERVICE_LEVEL | — | ✅ |
| 111 | SfoAgreementLineNumber | SFO_AGREEMENT_LINE_NUMBER | — | ✅ |
| 112 | SfoAgreementNumber | SFO_AGREEMENT_NUMBER | — | ✅ |
| 113 | SfoPtrId | SFO_PTR_ID | — | ✅ |
| 114 | ShipToCustContactId | SHIP_TO_CUST_CONTACT_ID | — | ✅ |
| 115 | ShipToCustId | SHIP_TO_CUST_ID | — | ✅ |
| 116 | ShipToCustLocationId | SHIP_TO_CUST_LOCATION_ID | — | ✅ |
| 117 | ShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 118 | ShipToOrganizationId | SHIP_TO_ORGANIZATION_ID | — | ✅ |
| 119 | ShipmentNum | SHIPMENT_NUM | — | ✅ |
| 120 | ShipmentType | SHIPMENT_TYPE | — | ✅ |
| 121 | ShippingUomCode | SHIPPING_UOM_CODE | — | ✅ |
| 122 | ShippingUomQuantity | SHIPPING_UOM_QUANTITY | — | ✅ |
| 123 | SourceShipmentId | SOURCE_SHIPMENT_ID | — | ✅ |
| 124 | StartDate | START_DATE | — | ✅ |
| 125 | SupplierOrderLineNumber | SUPPLIER_ORDER_LINE_NUMBER | — | ✅ |
| 126 | TaxAttributeUpdateCode | TAX_ATTRIBUTE_UPDATE_CODE | — | ✅ |
| 127 | TaxCodeId | TAX_CODE_ID | — | ✅ |
| 128 | TaxName | TAX_NAME | — | ✅ |
| 129 | TaxUserOverrideFlag | TAX_USER_OVERRIDE_FLAG | — | ✅ |
| 130 | TaxableFlag | TAXABLE_FLAG | — | ✅ |
| 131 | TermsId | TERMS_ID | — | ✅ |
| 132 | TransactionFlowHeaderId | TRANSACTION_FLOW_HEADER_ID | — | — |
| 133 | TrxBusinessCategory | TRX_BUSINESS_CATEGORY | — | ✅ |
| 134 | UnencumberedQuantity | UNENCUMBERED_QUANTITY | — | ✅ |
| 135 | UnitOfMeasureClass | UNIT_OF_MEASURE_CLASS | — | ✅ |
| 136 | UomCode | UOM_CODE | — | ✅ |
| 137 | UserDefinedFiscClass | USER_DEFINED_FISC_CLASS | — | ✅ |
| 138 | ValueBasis | VALUE_BASIS | — | ✅ |
| 139 | VmiFlag | VMI_FLAG | — | ✅ |
| 140 | WorkOrderId | WORK_ORDER_ID | — | ✅ |
| 141 | WorkOrderNumber | WORK_ORDER_NUMBER | — | ✅ |
| 142 | WorkOrderOperationSeq | WORK_ORDER_OPERATION_SEQ | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
