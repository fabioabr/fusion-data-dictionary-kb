---
id: DOC-OTHER-PVO-LotSerial
doc_type: system-doc
title: "LotSerial — PVO Cross-Module"
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
  - LotSerial
  - lotserial
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LotSerial

## 📌 Visão Geral

View Object para extração BICC de dados de Lot Serial. Acessa as tabelas: DOO_FULFILL_LINES_ALL, DOO_HEADERS_ALL, DOO_LINES_ALL (+2).

**Caminho:** `FscmTopModelAM.DooTopAM.LotSerial`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 191 | 5 | 1 | 6 | 3% |

---

## 🔗 Tabelas Relacionadas

- [[doo_fulfill_lines_all|DOO_FULFILL_LINES_ALL]] — 105 atributos
- [[doo_headers_all|DOO_HEADERS_ALL]] — 31 atributos
- [[doo_lines_all|DOO_LINES_ALL]] — 43 atributos
- [[doo_lot_serial_numbers|DOO_LOT_SERIAL_NUMBERS]] — 11 atributos (1 PKs, 6 BICC)
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
| 7 | FulfillLineCanceledFlag | CANCELED_FLAG | — | — |
| 8 | FulfillLineCanceledQty | CANCELED_QTY | — | — |
| 9 | FulfillLineCarrierId | CARRIER_ID | — | — |
| 10 | FulfillLineCategoryCode | CATEGORY_CODE | — | — |
| 11 | FulfillLineCompSeqPath | COMP_SEQ_PATH | — | — |
| 12 | FulfillLineCustomerItemId | CUSTOMER_ITEM_ID | — | — |
| 13 | FulfillLineCustomerPoLineNumber | CUSTOMER_PO_LINE_NUMBER | — | — |
| 14 | FulfillLineCustomerPoNumber | CUSTOMER_PO_NUMBER | — | — |
| 15 | FulfillLineDeltaType | DELTA_TYPE | — | — |
| 16 | FulfillLineDemandClassCode | DEMAND_CLASS_CODE | — | — |
| 17 | FulfillLineEarliestAcceptableShipDate | EARLIEST_ACCEPTABLE_SHIP_DATE | — | — |
| 18 | FulfillLineEstimateFulfillmentCost | ESTIMATE_FULFILLMENT_COST | — | — |
| 19 | FulfillLineEstimateMargin | ESTIMATE_MARGIN | — | — |
| 20 | FulfillLineExemptionCertificateNumber | EXEMPTION_CERTIFICATE_NUMBER | — | — |
| 21 | FulfillLineExtendedAmount | EXTENDED_AMOUNT | — | — |
| 22 | FulfillLineFobPointCode | FOB_POINT_CODE | — | — |
| 23 | FulfillLineFulfillInstanceId | FULFILL_INSTANCE_ID | — | — |
| 24 | FulfillLineFulfillLineId | FULFILL_LINE_ID | — | — |
| 25 | FulfillLineFulfillLineNumber | FULFILL_LINE_NUMBER | — | — |
| 26 | FulfillLineFulfillOrgId | FULFILL_ORG_ID | — | — |
| 27 | FulfillLineFulfillToleranceAbove | FULFILL_TOLERANCE_ABOVE | — | — |
| 28 | FulfillLineFulfillToleranceBelow | FULFILL_TOLERANCE_BELOW | — | — |
| 29 | FulfillLineFulfilledQty | FULFILLED_QTY | — | — |
| 30 | FulfillLineFulfillmentDate | FULFILLMENT_DATE | — | — |
| 31 | FulfillLineFulfillmentSplitRefId | FULFILLMENT_SPLIT_REF_ID | — | — |
| 32 | FulfillLineGopReferenceId | GOP_REFERENCE_ID | — | — |
| 33 | FulfillLineHeaderId | HEADER_ID | — | — |
| 34 | FulfillLineInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 35 | FulfillLineInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 36 | FulfillLineInvoiceEnabledFlag | INVOICE_ENABLED_FLAG | — | — |
| 37 | FulfillLineInvoiceableItemFlag | INVOICEABLE_ITEM_FLAG | — | — |
| 38 | FulfillLineInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 39 | FulfillLineItemTypeCode | ITEM_TYPE_CODE | — | — |
| 40 | FulfillLineLatestAcceptableArrivalDate | LATEST_ACCEPTABLE_ARRIVAL_DATE | — | — |
| 41 | FulfillLineLatestAcceptableShipDate | LATEST_ACCEPTABLE_SHIP_DATE | — | — |
| 42 | FulfillLineLineId | LINE_ID | — | — |
| 43 | FulfillLineLineTypeCode | LINE_TYPE_CODE | — | — |
| 44 | FulfillLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 45 | FulfillLineOnHold | ON_HOLD | — | — |
| 46 | FulfillLineOpenFlag | OPEN_FLAG | — | — |
| 47 | FulfillLineOrderedQty | ORDERED_QTY | — | — |
| 48 | FulfillLineOrderedUom | ORDERED_UOM | — | — |
| 49 | FulfillLineOrgId | ORG_ID | — | — |
| 50 | FulfillLineOrigSysDocumentLineRef | ORIG_SYS_DOCUMENT_LINE_REF | — | — |
| 51 | FulfillLineOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | — |
| 52 | FulfillLineOriginalInventoryItemId | ORIGINAL_INVENTORY_ITEM_ID | — | — |
| 53 | FulfillLineOverrideScheduleDateFlag | OVERRIDE_SCHEDULE_DATE_FLAG | — | — |
| 54 | FulfillLineOwnerId | OWNER_ID | — | — |
| 55 | FulfillLinePackingInstructions | PACKING_INSTRUCTIONS | — | — |
| 56 | FulfillLineParentFulfillLineId | PARENT_FULFILL_LINE_ID | — | — |
| 57 | FulfillLinePartialShipAllowedFlag | PARTIAL_SHIP_ALLOWED_FLAG | — | — |
| 58 | FulfillLinePaymentTermId | PAYMENT_TERM_ID | — | — |
| 59 | FulfillLinePromiseArrivalDate | PROMISE_ARRIVAL_DATE | — | — |
| 60 | FulfillLinePromiseShipDate | PROMISE_SHIP_DATE | — | — |
| 61 | FulfillLineReferenceFlineId | REFERENCE_FLINE_ID | — | — |
| 62 | FulfillLineRemnantFlag | REMNANT_FLAG | — | — |
| 63 | FulfillLineRequestArrivalDate | REQUEST_ARRIVAL_DATE | — | — |
| 64 | FulfillLineRequestShipDate | REQUEST_SHIP_DATE | — | — |
| 65 | FulfillLineRequestType | REQUEST_TYPE | — | — |
| 66 | FulfillLineReservableFlag | RESERVABLE_FLAG | — | — |
| 67 | FulfillLineReservationId | RESERVATION_ID | — | — |
| 68 | FulfillLineReservedQty | RESERVED_QTY | — | — |
| 69 | FulfillLineReturnReasonCode | RETURN_REASON_CODE | — | — |
| 70 | FulfillLineReturnableFlag | RETURNABLE_FLAG | — | — |
| 71 | FulfillLineRmaDeliveredQty | RMA_DELIVERED_QTY | — | — |
| 72 | FulfillLineRootParentFulfillLineId | ROOT_PARENT_FULFILL_LINE_ID | — | — |
| 73 | FulfillLineScheduleArrivalDate | SCHEDULE_ARRIVAL_DATE | — | — |
| 74 | FulfillLineScheduleShipDate | SCHEDULE_SHIP_DATE | — | — |
| 75 | FulfillLineShipClassOfService | SHIP_CLASS_OF_SERVICE | — | — |
| 76 | FulfillLineShipModeOfTransport | SHIP_MODE_OF_TRANSPORT | — | — |
| 77 | FulfillLineShipSetName | SHIP_SET_NAME | — | — |
| 78 | FulfillLineShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 79 | FulfillLineShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 80 | FulfillLineShipToPartyContactId | SHIP_TO_PARTY_CONTACT_ID | — | — |
| 81 | FulfillLineShipToPartyId | SHIP_TO_PARTY_ID | — | — |
| 82 | FulfillLineShipToPartySiteId | SHIP_TO_PARTY_SITE_ID | — | — |
| 83 | FulfillLineShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 84 | FulfillLineShipmentPriorityCode | SHIPMENT_PRIORITY_CODE | — | — |
| 85 | FulfillLineShippableFlag | SHIPPABLE_FLAG | — | — |
| 86 | FulfillLineShippedQty | SHIPPED_QTY | — | — |
| 87 | FulfillLineShippingInstructions | SHIPPING_INSTRUCTIONS | — | — |
| 88 | FulfillLineSourceLineId | SOURCE_LINE_ID | — | — |
| 89 | FulfillLineSourceLineNumber | SOURCE_LINE_NUMBER | — | — |
| 90 | FulfillLineSourceOrderId | SOURCE_ORDER_ID | — | — |
| 91 | FulfillLineSourceOrderNumber | SOURCE_ORDER_NUMBER | — | — |
| 92 | FulfillLineSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | — |
| 93 | FulfillLineSourceOrgId | SOURCE_ORG_ID | — | — |
| 94 | FulfillLineSourceScheduleId | SOURCE_SCHEDULE_ID | — | — |
| 95 | FulfillLineSourceScheduleNumber | SOURCE_SCHEDULE_NUMBER | — | — |
| 96 | FulfillLineSplitFromFlineId | SPLIT_FROM_FLINE_ID | — | — |
| 97 | FulfillLineStatusCode | STATUS_CODE | — | — |
| 98 | FulfillLineStatusRulesetId | STATUS_RULESET_ID | — | — |
| 99 | FulfillLineSubstituteAllowedFlag | SUBSTITUTE_ALLOWED_FLAG | — | — |
| 100 | FulfillLineSubstituteReasonCode | SUBSTITUTE_REASON_CODE | — | — |
| 101 | FulfillLineTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 102 | FulfillLineTaxExemptFlag | TAX_EXEMPT_FLAG | — | — |
| 103 | FulfillLineTaxExemptionReasonCode | TAX_EXEMPTION_REASON_CODE | — | — |
| 104 | FulfillLineUnitListPrice | UNIT_LIST_PRICE | — | — |
| 105 | FulfillLineUnitSellingPrice | UNIT_SELLING_PRICE | — | — |

### [[doo_headers_all|DOO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HeaderCanceledFlag | CANCELED_FLAG | — | — |
| 2 | HeaderChangeVersionNumber | CHANGE_VERSION_NUMBER | — | — |
| 3 | HeaderConversionDate | CONVERSION_DATE | — | — |
| 4 | HeaderConversionRate | CONVERSION_RATE | — | — |
| 5 | HeaderConversionTypeCode | CONVERSION_TYPE_CODE | — | — |
| 6 | HeaderCustomerPoNumber | CUSTOMER_PO_NUMBER | — | — |
| 7 | HeaderHeaderId | HEADER_ID | — | — |
| 8 | HeaderIsEditable | IS_EDITABLE | — | — |
| 9 | HeaderLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 10 | HeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | HeaderOnHold | ON_HOLD | — | — |
| 12 | HeaderOpenFlag | OPEN_FLAG | — | — |
| 13 | HeaderOrderNumber | ORDER_NUMBER | — | — |
| 14 | HeaderOrderTypeCode | ORDER_TYPE_CODE | — | — |
| 15 | HeaderOrderedDate | ORDERED_DATE | — | — |
| 16 | HeaderOrgId | ORG_ID | — | — |
| 17 | HeaderOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | — |
| 18 | HeaderOwnerId | OWNER_ID | — | — |
| 19 | HeaderPartialShipAllowedFlag | PARTIAL_SHIP_ALLOWED_FLAG | — | — |
| 20 | HeaderSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 21 | HeaderSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 22 | HeaderSoldToPartyContactId | SOLD_TO_PARTY_CONTACT_ID | — | — |
| 23 | HeaderSoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 24 | HeaderSourceDocumentTypeCode | SOURCE_DOCUMENT_TYPE_CODE | — | — |
| 25 | HeaderSourceOrderId | SOURCE_ORDER_ID | — | — |
| 26 | HeaderSourceOrderNumber | SOURCE_ORDER_NUMBER | — | — |
| 27 | HeaderSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | — |
| 28 | HeaderSourceOrgId | SOURCE_ORG_ID | — | — |
| 29 | HeaderStatusCode | STATUS_CODE | — | — |
| 30 | HeaderSubmittedFlag | SUBMITTED_FLAG | — | — |
| 31 | HeaderTransactionalCurrencyCode | TRANSACTIONAL_CURRENCY_CODE | — | — |

### [[doo_lines_all|DOO_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LineCanceledFlag | CANCELED_FLAG | — | — |
| 2 | LineCanceledQty | CANCELED_QTY | — | — |
| 3 | LineCategoryCode | CATEGORY_CODE | — | — |
| 4 | LineCompSeqPath | COMP_SEQ_PATH | — | — |
| 5 | LineDeltaType | DELTA_TYPE | — | — |
| 6 | LineExtendedAmount | EXTENDED_AMOUNT | — | — |
| 7 | LineFulfilledQty | FULFILLED_QTY | — | — |
| 8 | LineFulfillmentDate | FULFILLMENT_DATE | — | — |
| 9 | LineHeaderId | HEADER_ID | — | — |
| 10 | LineInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 11 | LineInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 12 | LineItemTypeCode | ITEM_TYPE_CODE | — | — |
| 13 | LineLineActualShipDate | ACTUAL_SHIP_DATE | — | — |
| 14 | LineLineId | LINE_ID | — | — |
| 15 | LineLineNumber | LINE_NUMBER | — | — |
| 16 | LineLineTypeCode | LINE_TYPE_CODE | — | — |
| 17 | LineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | LineOnHold | ON_HOLD | — | — |
| 19 | LineOpenFlag | OPEN_FLAG | — | — |
| 20 | LineOrderedQty | ORDERED_QTY | — | — |
| 21 | LineOrderedUom | ORDERED_UOM | — | — |
| 22 | LineOrgId | ORG_ID | — | — |
| 23 | LineOrigSysDocumentLineRef | ORIG_SYS_DOCUMENT_LINE_REF | — | — |
| 24 | LineOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | — |
| 25 | LineOwnerId | OWNER_ID | — | — |
| 26 | LineParentLineId | PARENT_LINE_ID | — | — |
| 27 | LineReferenceLineId | REFERENCE_LINE_ID | — | — |
| 28 | LineRmaDeliveredQty | RMA_DELIVERED_QTY | — | — |
| 29 | LineRootParentLineId | ROOT_PARENT_LINE_ID | — | — |
| 30 | LineScheduleShipDate | SCHEDULE_SHIP_DATE | — | — |
| 31 | LineShippedQty | SHIPPED_QTY | — | — |
| 32 | LineSourceLineId | SOURCE_LINE_ID | — | — |
| 33 | LineSourceLineNumber | SOURCE_LINE_NUMBER | — | — |
| 34 | LineSourceOrderId | SOURCE_ORDER_ID | — | — |
| 35 | LineSourceOrderNumber | SOURCE_ORDER_NUMBER | — | — |
| 36 | LineSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | — |
| 37 | LineSourceOrgId | SOURCE_ORG_ID | — | — |
| 38 | LineSourceScheduleId | SOURCE_SCHEDULE_ID | — | — |
| 39 | LineSourceScheduleNumber | SOURCE_SCHEDULE_NUMBER | — | — |
| 40 | LineStatusCode | STATUS_CODE | — | — |
| 41 | LineTransformFromLineId | TRANSFORM_FROM_LINE_ID | — | — |
| 42 | LineUnitListPrice | UNIT_LIST_PRICE | — | — |
| 43 | LineUnitSellingPrice | UNIT_SELLING_PRICE | — | — |

### [[doo_lot_serial_numbers|DOO_LOT_SERIAL_NUMBERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LotSerialFulfillLineId | FULFILL_LINE_ID | — | — |
| 2 | LotSerialId | LOT_SERIAL_ID | 🔑 | ✅ |
| 3 | LotSerialItemRevisionNumber | ITEM_REVISION_NUMBER | — | ✅ |
| 4 | LotSerialItemSerialNumberFrom | ITEM_SERIAL_NUMBER_FROM | — | ✅ |
| 5 | LotSerialItemSerialNumberTo | ITEM_SERIAL_NUMBER_TO | — | ✅ |
| 6 | LotSerialLineId | LINE_ID | — | — |
| 7 | LotSerialLocatorId | LOCATOR_ID | — | — |
| 8 | LotSerialLotNumber | LOT_NUMBER | — | ✅ |
| 9 | LotSerialObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | LotSerialOrigSysLotserialRef | ORIG_SYS_LOTSERIAL_REF | — | — |
| 11 | LotSerialQuantity | QUANTITY | — | ✅ |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitId | BU_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
