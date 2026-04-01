---
id: DOC-OTHER-PVO-FulfillLineDetailReceiving
doc_type: system-doc
title: "FulfillLineDetailReceiving — PVO Cross-Module"
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
  - FulfillLineDetailReceiving
  - fulfilllinedetailreceiving
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FulfillLineDetailReceiving

## 📌 Visão Geral

View Object para extração BICC de dados de Fulfill Line Detail Receiving. Acessa as tabelas: DOO_FULFILL_LINES_ALL, DOO_FULFILL_LINE_DETAILS, DOO_HEADERS_ALL (+2).

**Caminho:** `FscmTopModelAM.DooTopAM.FulfillLineDetailReceiving`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 229 | 5 | 1 | 4 | 2% |

---

## 🔗 Tabelas Relacionadas

- [[doo_fulfill_lines_all|DOO_FULFILL_LINES_ALL]] — 117 atributos (1 BICC)
- [[doo_fulfill_line_details|DOO_FULFILL_LINE_DETAILS]] — 26 atributos (1 PKs, 3 BICC)
- [[doo_headers_all|DOO_HEADERS_ALL]] — 37 atributos
- [[doo_lines_all|DOO_LINES_ALL]] — 48 atributos
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 1 atributos

---

## ⚙️ Atributos

### [[doo_fulfill_lines_all|DOO_FULFILL_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FulfillLineAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 2 | FulfillLineActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
| 3 | FulfillLineActualShipDate | ACTUAL_SHIP_DATE | — | — |
| 4 | FulfillLineBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 5 | FulfillLineBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 6 | FulfillLineBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 7 | FulfillLineCancelReasonCode | CANCEL_REASON_CODE | — | — |
| 8 | FulfillLineCanceledFlag | CANCELED_FLAG | — | — |
| 9 | FulfillLineCanceledQty | CANCELED_QTY | — | — |
| 10 | FulfillLineCarrierId | CARRIER_ID | — | — |
| 11 | FulfillLineCategoryCode | CATEGORY_CODE | — | — |
| 12 | FulfillLineCompSeqPath | COMP_SEQ_PATH | — | — |
| 13 | FulfillLineCreatedBy | CREATED_BY | — | — |
| 14 | FulfillLineCreationDate | CREATION_DATE | — | — |
| 15 | FulfillLineCustomerItemId | CUSTOMER_ITEM_ID | — | — |
| 16 | FulfillLineCustomerPoLineNumber | CUSTOMER_PO_LINE_NUMBER | — | — |
| 17 | FulfillLineCustomerPoNumber | CUSTOMER_PO_NUMBER | — | — |
| 18 | FulfillLineDeltaType | DELTA_TYPE | — | — |
| 19 | FulfillLineDemandClassCode | DEMAND_CLASS_CODE | — | — |
| 20 | FulfillLineEarliestAcceptableShipDate | EARLIEST_ACCEPTABLE_SHIP_DATE | — | — |
| 21 | FulfillLineEstimateFulfillmentCost | ESTIMATE_FULFILLMENT_COST | — | — |
| 22 | FulfillLineEstimateMargin | ESTIMATE_MARGIN | — | — |
| 23 | FulfillLineExemptionCertificateNumber | EXEMPTION_CERTIFICATE_NUMBER | — | — |
| 24 | FulfillLineExtendedAmount | EXTENDED_AMOUNT | — | — |
| 25 | FulfillLineFobPointCode | FOB_POINT_CODE | — | — |
| 26 | FulfillLineFulfillInstanceId | FULFILL_INSTANCE_ID | — | — |
| 27 | FulfillLineFulfillLineId | FULFILL_LINE_ID | — | — |
| 28 | FulfillLineFulfillLineNumber | FULFILL_LINE_NUMBER | — | — |
| 29 | FulfillLineFulfillOrgId | FULFILL_ORG_ID | — | — |
| 30 | FulfillLineFulfillToleranceAbove | FULFILL_TOLERANCE_ABOVE | — | — |
| 31 | FulfillLineFulfillToleranceBelow | FULFILL_TOLERANCE_BELOW | — | — |
| 32 | FulfillLineFulfilledQty | FULFILLED_QTY | — | — |
| 33 | FulfillLineFulfillmentDate | FULFILLMENT_DATE | — | — |
| 34 | FulfillLineFulfillmentSplitRefId | FULFILLMENT_SPLIT_REF_ID | — | — |
| 35 | FulfillLineGopReferenceId | GOP_REFERENCE_ID | — | — |
| 36 | FulfillLineHeaderId | HEADER_ID | — | — |
| 37 | FulfillLineInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 38 | FulfillLineInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 39 | FulfillLineInvoiceEnabledFlag | INVOICE_ENABLED_FLAG | — | — |
| 40 | FulfillLineInvoiceableItemFlag | INVOICEABLE_ITEM_FLAG | — | — |
| 41 | FulfillLineInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 42 | FulfillLineItemTypeCode | ITEM_TYPE_CODE | — | — |
| 43 | FulfillLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 44 | FulfillLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 45 | FulfillLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 46 | FulfillLineLatestAcceptableArrivalDate | LATEST_ACCEPTABLE_ARRIVAL_DATE | — | — |
| 47 | FulfillLineLatestAcceptableShipDate | LATEST_ACCEPTABLE_SHIP_DATE | — | — |
| 48 | FulfillLineLineId | LINE_ID | — | — |
| 49 | FulfillLineLineTypeCode | LINE_TYPE_CODE | — | — |
| 50 | FulfillLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 51 | FulfillLineOnHold | ON_HOLD | — | — |
| 52 | FulfillLineOpenFlag | OPEN_FLAG | — | — |
| 53 | FulfillLineOrderedQty | ORDERED_QTY | — | — |
| 54 | FulfillLineOrderedUom | ORDERED_UOM | — | — |
| 55 | FulfillLineOrgId | ORG_ID | — | — |
| 56 | FulfillLineOrigSysDocumentLineRef | ORIG_SYS_DOCUMENT_LINE_REF | — | — |
| 57 | FulfillLineOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | — |
| 58 | FulfillLineOriginalInventoryItemId | ORIGINAL_INVENTORY_ITEM_ID | — | — |
| 59 | FulfillLineOverrideScheduleDateFlag | OVERRIDE_SCHEDULE_DATE_FLAG | — | — |
| 60 | FulfillLineOwnerId | OWNER_ID | — | — |
| 61 | FulfillLinePackingInstructions | PACKING_INSTRUCTIONS | — | — |
| 62 | FulfillLineParentFulfillLineId | PARENT_FULFILL_LINE_ID | — | — |
| 63 | FulfillLinePartialShipAllowedFlag | PARTIAL_SHIP_ALLOWED_FLAG | — | — |
| 64 | FulfillLinePaymentTermId | PAYMENT_TERM_ID | — | — |
| 65 | FulfillLinePriceUsingSecUomFlag | PRICE_USING_SEC_UOM_FLAG | — | — |
| 66 | FulfillLinePromiseArrivalDate | PROMISE_ARRIVAL_DATE | — | — |
| 67 | FulfillLinePromiseShipDate | PROMISE_SHIP_DATE | — | — |
| 68 | FulfillLineReferenceFlineId | REFERENCE_FLINE_ID | — | — |
| 69 | FulfillLineRemnantFlag | REMNANT_FLAG | — | — |
| 70 | FulfillLineRequestArrivalDate | REQUEST_ARRIVAL_DATE | — | — |
| 71 | FulfillLineRequestShipDate | REQUEST_SHIP_DATE | — | — |
| 72 | FulfillLineRequestType | REQUEST_TYPE | — | — |
| 73 | FulfillLineReservableFlag | RESERVABLE_FLAG | — | — |
| 74 | FulfillLineReservationId | RESERVATION_ID | — | — |
| 75 | FulfillLineReservedQty | RESERVED_QTY | — | — |
| 76 | FulfillLineReturnReasonCode | RETURN_REASON_CODE | — | — |
| 77 | FulfillLineReturnableFlag | RETURNABLE_FLAG | — | — |
| 78 | FulfillLineRmaDeliveredQty | RMA_DELIVERED_QTY | — | — |
| 79 | FulfillLineRootParentFulfillLineId | ROOT_PARENT_FULFILL_LINE_ID | — | — |
| 80 | FulfillLineScheduleArrivalDate | SCHEDULE_ARRIVAL_DATE | — | — |
| 81 | FulfillLineScheduleShipDate | SCHEDULE_SHIP_DATE | — | — |
| 82 | FulfillLineSecondaryFulfilledQty | SECONDARY_FULFILLED_QTY | — | — |
| 83 | FulfillLineSecondaryOrderedQty | SECONDARY_ORDERED_QTY | — | — |
| 84 | FulfillLineSecondaryRmaDeliveredQty | SECONDARY_RMA_DELIVERED_QTY | — | — |
| 85 | FulfillLineSecondaryShippedQty | SECONDARY_SHIPPED_QTY | — | — |
| 86 | FulfillLineSecondaryUom | SECONDARY_UOM | — | — |
| 87 | FulfillLineShipClassOfService | SHIP_CLASS_OF_SERVICE | — | — |
| 88 | FulfillLineShipModeOfTransport | SHIP_MODE_OF_TRANSPORT | — | — |
| 89 | FulfillLineShipSetName | SHIP_SET_NAME | — | — |
| 90 | FulfillLineShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 91 | FulfillLineShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 92 | FulfillLineShipToPartyContactId | SHIP_TO_PARTY_CONTACT_ID | — | — |
| 93 | FulfillLineShipToPartyId | SHIP_TO_PARTY_ID | — | — |
| 94 | FulfillLineShipToPartySiteId | SHIP_TO_PARTY_SITE_ID | — | — |
| 95 | FulfillLineShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 96 | FulfillLineShipmentPriorityCode | SHIPMENT_PRIORITY_CODE | — | — |
| 97 | FulfillLineShippableFlag | SHIPPABLE_FLAG | — | — |
| 98 | FulfillLineShippedQty | SHIPPED_QTY | — | — |
| 99 | FulfillLineShippingInstructions | SHIPPING_INSTRUCTIONS | — | — |
| 100 | FulfillLineSourceLineId | SOURCE_LINE_ID | — | — |
| 101 | FulfillLineSourceLineNumber | SOURCE_LINE_NUMBER | — | — |
| 102 | FulfillLineSourceOrderId | SOURCE_ORDER_ID | — | — |
| 103 | FulfillLineSourceOrderNumber | SOURCE_ORDER_NUMBER | — | — |
| 104 | FulfillLineSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | — |
| 105 | FulfillLineSourceOrgId | SOURCE_ORG_ID | — | — |
| 106 | FulfillLineSourceScheduleId | SOURCE_SCHEDULE_ID | — | — |
| 107 | FulfillLineSourceScheduleNumber | SOURCE_SCHEDULE_NUMBER | — | — |
| 108 | FulfillLineSplitFromFlineId | SPLIT_FROM_FLINE_ID | — | — |
| 109 | FulfillLineStatusCode | STATUS_CODE | — | — |
| 110 | FulfillLineStatusRulesetId | STATUS_RULESET_ID | — | — |
| 111 | FulfillLineSubstituteAllowedFlag | SUBSTITUTE_ALLOWED_FLAG | — | — |
| 112 | FulfillLineSubstituteReasonCode | SUBSTITUTE_REASON_CODE | — | — |
| 113 | FulfillLineTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 114 | FulfillLineTaxExemptFlag | TAX_EXEMPT_FLAG | — | — |
| 115 | FulfillLineTaxExemptionReasonCode | TAX_EXEMPTION_REASON_CODE | — | — |
| 116 | FulfillLineUnitListPrice | UNIT_LIST_PRICE | — | — |
| 117 | FulfillLineUnitSellingPrice | UNIT_SELLING_PRICE | — | — |

### [[doo_fulfill_line_details|DOO_FULFILL_LINE_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FulfillLineDetailActualDeliveryDate | ACTUAL_DELIVERY_DATE | — | — |
| 2 | FulfillLineDetailBillOfLadingNumber | BILL_OF_LADING_NUMBER | — | — |
| 3 | FulfillLineDetailBillingTransactionAmount | BILLING_TRANSACTION_AMOUNT | — | — |
| 4 | FulfillLineDetailBillingTransactionDate | BILLING_TRANSACTION_DATE | — | — |
| 5 | FulfillLineDetailBillingTransactionNumber | BILLING_TRANSACTION_NUMBER | — | — |
| 6 | FulfillLineDetailCreatedBy | CREATED_BY | — | — |
| 7 | FulfillLineDetailCreationDate | CREATION_DATE | — | — |
| 8 | FulfillLineDetailCustomerTrxLineId | CUSTOMER_TRX_LINE_ID | — | — |
| 9 | FulfillLineDetailDeliveryName | DELIVERY_NAME | — | — |
| 10 | FulfillLineDetailFulfillLineId | FULFILL_LINE_ID | — | — |
| 11 | FulfillLineDetailId | FULFILL_LINE_DETAIL_ID | 🔑 | ✅ |
| 12 | FulfillLineDetailLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | FulfillLineDetailLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | FulfillLineDetailLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | FulfillLineDetailObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | FulfillLineDetailQuantity | QUANTITY | — | — |
| 17 | FulfillLineDetailRmaReceiptDate | RMA_RECEIPT_DATE | — | ✅ |
| 18 | FulfillLineDetailRmaReceiptLineNumber | RMA_RECEIPT_LINE_NUMBER | — | — |
| 19 | FulfillLineDetailRmaReceiptNumber | RMA_RECEIPT_NUMBER | — | — |
| 20 | FulfillLineDetailRmaReceiptTransactionId | RMA_RECEIPT_TRANSACTION_ID | — | — |
| 21 | FulfillLineDetailSecondaryQuantity | SECONDARY_QUANTITY | — | — |
| 22 | FulfillLineDetailStatus | STATUS | — | — |
| 23 | FulfillLineDetailStatusAsofDate | STATUS_ASOF_DATE | — | — |
| 24 | FulfillLineDetailTaskType | TASK_TYPE | — | — |
| 25 | FulfillLineDetailTrackingNumber | TRACKING_NUMBER | — | — |
| 26 | FulfillLineDetailWaybillNumber | WAYBILL_NUMBER | — | — |

### [[doo_headers_all|DOO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HeaderCancelReasonCode | CANCEL_REASON_CODE | — | — |
| 2 | HeaderCanceledFlag | CANCELED_FLAG | — | — |
| 3 | HeaderChangeVersionNumber | CHANGE_VERSION_NUMBER | — | — |
| 4 | HeaderConversionDate | CONVERSION_DATE | — | — |
| 5 | HeaderConversionRate | CONVERSION_RATE | — | — |
| 6 | HeaderConversionTypeCode | CONVERSION_TYPE_CODE | — | — |
| 7 | HeaderCreatedBy | CREATED_BY | — | — |
| 8 | HeaderCreationDate | CREATION_DATE | — | — |
| 9 | HeaderCustomerPoNumber | CUSTOMER_PO_NUMBER | — | — |
| 10 | HeaderHeaderId | HEADER_ID | — | — |
| 11 | HeaderIsEditable | IS_EDITABLE | — | — |
| 12 | HeaderLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 13 | HeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | HeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | HeaderLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 16 | HeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | HeaderOnHold | ON_HOLD | — | — |
| 18 | HeaderOpenFlag | OPEN_FLAG | — | — |
| 19 | HeaderOrderNumber | ORDER_NUMBER | — | — |
| 20 | HeaderOrderTypeCode | ORDER_TYPE_CODE | — | — |
| 21 | HeaderOrderedDate | ORDERED_DATE | — | — |
| 22 | HeaderOrgId | ORG_ID | — | — |
| 23 | HeaderOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | — |
| 24 | HeaderOwnerId | OWNER_ID | — | — |
| 25 | HeaderPartialShipAllowedFlag | PARTIAL_SHIP_ALLOWED_FLAG | — | — |
| 26 | HeaderRequestShipDate | REQUEST_SHIP_DATE | — | — |
| 27 | HeaderSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 28 | HeaderSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 29 | HeaderSoldToPartyContactId | SOLD_TO_PARTY_CONTACT_ID | — | — |
| 30 | HeaderSoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 31 | HeaderSourceDocumentTypeCode | SOURCE_DOCUMENT_TYPE_CODE | — | — |
| 32 | HeaderSourceOrderId | SOURCE_ORDER_ID | — | — |
| 33 | HeaderSourceOrderNumber | SOURCE_ORDER_NUMBER | — | — |
| 34 | HeaderSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | — |
| 35 | HeaderSourceOrgId | SOURCE_ORG_ID | — | — |
| 36 | HeaderStatusCode | STATUS_CODE | — | — |
| 37 | HeaderTransactionalCurrencyCode | TRANSACTIONAL_CURRENCY_CODE | — | — |

### [[doo_lines_all|DOO_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LineActualShipDate | ACTUAL_SHIP_DATE | — | — |
| 2 | LineCanceledFlag | CANCELED_FLAG | — | — |
| 3 | LineCanceledQty | CANCELED_QTY | — | — |
| 4 | LineCategoryCode | CATEGORY_CODE | — | — |
| 5 | LineCompSeqPath | COMP_SEQ_PATH | — | — |
| 6 | LineCreatedBy | CREATED_BY | — | — |
| 7 | LineCreationDate | CREATION_DATE | — | — |
| 8 | LineDeltaType | DELTA_TYPE | — | — |
| 9 | LineExtendedAmount | EXTENDED_AMOUNT | — | — |
| 10 | LineFulfilledQty | FULFILLED_QTY | — | — |
| 11 | LineFulfillmentDate | FULFILLMENT_DATE | — | — |
| 12 | LineHeaderId | HEADER_ID | — | — |
| 13 | LineInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 14 | LineInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 15 | LineItemTypeCode | ITEM_TYPE_CODE | — | — |
| 16 | LineLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 17 | LineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | LineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | LineLineId | LINE_ID | — | — |
| 20 | LineLineNumber | LINE_NUMBER | — | — |
| 21 | LineLineTypeCode | LINE_TYPE_CODE | — | — |
| 22 | LineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | LineOnHold | ON_HOLD | — | — |
| 24 | LineOpenFlag | OPEN_FLAG | — | — |
| 25 | LineOrderedQty | ORDERED_QTY | — | — |
| 26 | LineOrderedUom | ORDERED_UOM | — | — |
| 27 | LineOrgId | ORG_ID | — | — |
| 28 | LineOrigSysDocumentLineRef | ORIG_SYS_DOCUMENT_LINE_REF | — | — |
| 29 | LineOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | — |
| 30 | LineOwnerId | OWNER_ID | — | — |
| 31 | LineParentLineId | PARENT_LINE_ID | — | — |
| 32 | LineReferenceLineId | REFERENCE_LINE_ID | — | — |
| 33 | LineRmaDeliveredQty | RMA_DELIVERED_QTY | — | — |
| 34 | LineRootParentLineId | ROOT_PARENT_LINE_ID | — | — |
| 35 | LineScheduleShipDate | SCHEDULE_SHIP_DATE | — | — |
| 36 | LineShippedQty | SHIPPED_QTY | — | — |
| 37 | LineSourceLineId | SOURCE_LINE_ID | — | — |
| 38 | LineSourceLineNumber | SOURCE_LINE_NUMBER | — | — |
| 39 | LineSourceOrderId | SOURCE_ORDER_ID | — | — |
| 40 | LineSourceOrderNumber | SOURCE_ORDER_NUMBER | — | — |
| 41 | LineSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | — |
| 42 | LineSourceOrgId | SOURCE_ORG_ID | — | — |
| 43 | LineSourceScheduleId | SOURCE_SCHEDULE_ID | — | — |
| 44 | LineSourceScheduleNumber | SOURCE_SCHEDULE_NUMBER | — | — |
| 45 | LineStatusCode | STATUS_CODE | — | — |
| 46 | LineTransformFromLineId | TRANSFORM_FROM_LINE_ID | — | — |
| 47 | LineUnitListPrice | UNIT_LIST_PRICE | — | — |
| 48 | LineUnitSellingPrice | UNIT_SELLING_PRICE | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUBusinessUnitId | BU_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
