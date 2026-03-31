---
id: DOC-OTHER-PVO-PriceAdjustment
doc_type: system-doc
title: "PriceAdjustment — PVO Cross-Module"
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
  - PriceAdjustment
  - priceadjustment
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PriceAdjustment

## 📌 Visão Geral

View Object para extração BICC de dados de Price Adjustment. Acessa as tabelas: DOO_FULFILL_LINES_ALL, DOO_HEADERS_ALL, DOO_LINES_ALL (+3).

**Caminho:** `FscmTopModelAM.DooTopAM.PriceAdjustment`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 241 | 6 | 1 | 7 | 3% |

---

## 🔗 Tabelas Relacionadas

- [[doo_fulfill_lines_all|DOO_FULFILL_LINES_ALL]] — 110 atributos
- [[doo_headers_all|DOO_HEADERS_ALL]] — 35 atributos
- [[doo_lines_all|DOO_LINES_ALL]] — 48 atributos
- [[doo_price_adjustments|DOO_PRICE_ADJUSTMENTS]] — 16 atributos (1 PKs, 7 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 1 atributos
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 31 atributos

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
| 12 | FulfillLineCreatedBy | CREATED_BY | — | — |
| 13 | FulfillLineCreationDate | CREATION_DATE | — | — |
| 14 | FulfillLineCustomerItemId | CUSTOMER_ITEM_ID | — | — |
| 15 | FulfillLineCustomerPoLineNumber | CUSTOMER_PO_LINE_NUMBER | — | — |
| 16 | FulfillLineCustomerPoNumber | CUSTOMER_PO_NUMBER | — | — |
| 17 | FulfillLineDeltaType | DELTA_TYPE | — | — |
| 18 | FulfillLineDemandClassCode | DEMAND_CLASS_CODE | — | — |
| 19 | FulfillLineEarliestAcceptableShipDate | EARLIEST_ACCEPTABLE_SHIP_DATE | — | — |
| 20 | FulfillLineEstimateFulfillmentCost | ESTIMATE_FULFILLMENT_COST | — | — |
| 21 | FulfillLineEstimateMargin | ESTIMATE_MARGIN | — | — |
| 22 | FulfillLineExemptionCertificateNumber | EXEMPTION_CERTIFICATE_NUMBER | — | — |
| 23 | FulfillLineExtendedAmount | EXTENDED_AMOUNT | — | — |
| 24 | FulfillLineFobPointCode | FOB_POINT_CODE | — | — |
| 25 | FulfillLineFulfillInstanceId | FULFILL_INSTANCE_ID | — | — |
| 26 | FulfillLineFulfillLineId | FULFILL_LINE_ID | — | — |
| 27 | FulfillLineFulfillLineNumber | FULFILL_LINE_NUMBER | — | — |
| 28 | FulfillLineFulfillOrgId | FULFILL_ORG_ID | — | — |
| 29 | FulfillLineFulfillToleranceAbove | FULFILL_TOLERANCE_ABOVE | — | — |
| 30 | FulfillLineFulfillToleranceBelow | FULFILL_TOLERANCE_BELOW | — | — |
| 31 | FulfillLineFulfilledQty | FULFILLED_QTY | — | — |
| 32 | FulfillLineFulfillmentDate | FULFILLMENT_DATE | — | — |
| 33 | FulfillLineFulfillmentSplitRefId | FULFILLMENT_SPLIT_REF_ID | — | — |
| 34 | FulfillLineGopReferenceId | GOP_REFERENCE_ID | — | — |
| 35 | FulfillLineHeaderId | HEADER_ID | — | — |
| 36 | FulfillLineInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 37 | FulfillLineInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 38 | FulfillLineInvoiceEnabledFlag | INVOICE_ENABLED_FLAG | — | — |
| 39 | FulfillLineInvoiceableItemFlag | INVOICEABLE_ITEM_FLAG | — | — |
| 40 | FulfillLineInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 41 | FulfillLineItemTypeCode | ITEM_TYPE_CODE | — | — |
| 42 | FulfillLineLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 43 | FulfillLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 44 | FulfillLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 45 | FulfillLineLatestAcceptableArrivalDate | LATEST_ACCEPTABLE_ARRIVAL_DATE | — | — |
| 46 | FulfillLineLatestAcceptableShipDate | LATEST_ACCEPTABLE_SHIP_DATE | — | — |
| 47 | FulfillLineLineId | LINE_ID | — | — |
| 48 | FulfillLineLineTypeCode | LINE_TYPE_CODE | — | — |
| 49 | FulfillLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 50 | FulfillLineOnHold | ON_HOLD | — | — |
| 51 | FulfillLineOpenFlag | OPEN_FLAG | — | — |
| 52 | FulfillLineOrderedQty | ORDERED_QTY | — | — |
| 53 | FulfillLineOrderedUom | ORDERED_UOM | — | — |
| 54 | FulfillLineOrgId | ORG_ID | — | — |
| 55 | FulfillLineOrigSysDocumentLineRef | ORIG_SYS_DOCUMENT_LINE_REF | — | — |
| 56 | FulfillLineOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | — |
| 57 | FulfillLineOriginalInventoryItemId | ORIGINAL_INVENTORY_ITEM_ID | — | — |
| 58 | FulfillLineOverrideScheduleDateFlag | OVERRIDE_SCHEDULE_DATE_FLAG | — | — |
| 59 | FulfillLineOwnerId | OWNER_ID | — | — |
| 60 | FulfillLinePackingInstructions | PACKING_INSTRUCTIONS | — | — |
| 61 | FulfillLineParentFulfillLineId | PARENT_FULFILL_LINE_ID | — | — |
| 62 | FulfillLinePartialShipAllowedFlag | PARTIAL_SHIP_ALLOWED_FLAG | — | — |
| 63 | FulfillLinePaymentTermId | PAYMENT_TERM_ID | — | — |
| 64 | FulfillLinePromiseArrivalDate | PROMISE_ARRIVAL_DATE | — | — |
| 65 | FulfillLinePromiseShipDate | PROMISE_SHIP_DATE | — | — |
| 66 | FulfillLineReferenceFlineId | REFERENCE_FLINE_ID | — | — |
| 67 | FulfillLineRemnantFlag | REMNANT_FLAG | — | — |
| 68 | FulfillLineRequestArrivalDate | REQUEST_ARRIVAL_DATE | — | — |
| 69 | FulfillLineRequestShipDate | REQUEST_SHIP_DATE | — | — |
| 70 | FulfillLineRequestType | REQUEST_TYPE | — | — |
| 71 | FulfillLineReservableFlag | RESERVABLE_FLAG | — | — |
| 72 | FulfillLineReservationId | RESERVATION_ID | — | — |
| 73 | FulfillLineReservedQty | RESERVED_QTY | — | — |
| 74 | FulfillLineReturnReasonCode | RETURN_REASON_CODE | — | — |
| 75 | FulfillLineReturnableFlag | RETURNABLE_FLAG | — | — |
| 76 | FulfillLineRmaDeliveredQty | RMA_DELIVERED_QTY | — | — |
| 77 | FulfillLineRootParentFulfillLineId | ROOT_PARENT_FULFILL_LINE_ID | — | — |
| 78 | FulfillLineScheduleArrivalDate | SCHEDULE_ARRIVAL_DATE | — | — |
| 79 | FulfillLineScheduleShipDate | SCHEDULE_SHIP_DATE | — | — |
| 80 | FulfillLineShipClassOfService | SHIP_CLASS_OF_SERVICE | — | — |
| 81 | FulfillLineShipModeOfTransport | SHIP_MODE_OF_TRANSPORT | — | — |
| 82 | FulfillLineShipSetName | SHIP_SET_NAME | — | — |
| 83 | FulfillLineShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 84 | FulfillLineShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 85 | FulfillLineShipToPartyContactId | SHIP_TO_PARTY_CONTACT_ID | — | — |
| 86 | FulfillLineShipToPartyId | SHIP_TO_PARTY_ID | — | — |
| 87 | FulfillLineShipToPartySiteId | SHIP_TO_PARTY_SITE_ID | — | — |
| 88 | FulfillLineShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 89 | FulfillLineShipmentPriorityCode | SHIPMENT_PRIORITY_CODE | — | — |
| 90 | FulfillLineShippableFlag | SHIPPABLE_FLAG | — | — |
| 91 | FulfillLineShippedQty | SHIPPED_QTY | — | — |
| 92 | FulfillLineShippingInstructions | SHIPPING_INSTRUCTIONS | — | — |
| 93 | FulfillLineSourceLineId | SOURCE_LINE_ID | — | — |
| 94 | FulfillLineSourceLineNumber | SOURCE_LINE_NUMBER | — | — |
| 95 | FulfillLineSourceOrderId | SOURCE_ORDER_ID | — | — |
| 96 | FulfillLineSourceOrderNumber | SOURCE_ORDER_NUMBER | — | — |
| 97 | FulfillLineSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | — |
| 98 | FulfillLineSourceOrgId | SOURCE_ORG_ID | — | — |
| 99 | FulfillLineSourceScheduleId | SOURCE_SCHEDULE_ID | — | — |
| 100 | FulfillLineSourceScheduleNumber | SOURCE_SCHEDULE_NUMBER | — | — |
| 101 | FulfillLineSplitFromFlineId | SPLIT_FROM_FLINE_ID | — | — |
| 102 | FulfillLineStatusCode | STATUS_CODE | — | — |
| 103 | FulfillLineStatusRulesetId | STATUS_RULESET_ID | — | — |
| 104 | FulfillLineSubstituteAllowedFlag | SUBSTITUTE_ALLOWED_FLAG | — | — |
| 105 | FulfillLineSubstituteReasonCode | SUBSTITUTE_REASON_CODE | — | — |
| 106 | FulfillLineTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 107 | FulfillLineTaxExemptFlag | TAX_EXEMPT_FLAG | — | — |
| 108 | FulfillLineTaxExemptionReasonCode | TAX_EXEMPTION_REASON_CODE | — | — |
| 109 | FulfillLineUnitListPrice | UNIT_LIST_PRICE | — | — |
| 110 | FulfillLineUnitSellingPrice | UNIT_SELLING_PRICE | — | — |

### [[doo_headers_all|DOO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HeaderCanceledFlag | CANCELED_FLAG | — | — |
| 2 | HeaderChangeVersionNumber | CHANGE_VERSION_NUMBER | — | — |
| 3 | HeaderConversionDate | CONVERSION_DATE | — | — |
| 4 | HeaderConversionRate | CONVERSION_RATE | — | — |
| 5 | HeaderConversionTypeCode | CONVERSION_TYPE_CODE | — | — |
| 6 | HeaderCreatedBy | CREATED_BY | — | — |
| 7 | HeaderCreationDate | CREATION_DATE | — | — |
| 8 | HeaderCustomerPoNumber | CUSTOMER_PO_NUMBER | — | — |
| 9 | HeaderHeaderId | HEADER_ID | — | — |
| 10 | HeaderIsEditable | IS_EDITABLE | — | — |
| 11 | HeaderLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 12 | HeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | HeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | HeaderLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 15 | HeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | HeaderOnHold | ON_HOLD | — | — |
| 17 | HeaderOpenFlag | OPEN_FLAG | — | — |
| 18 | HeaderOrderNumber | ORDER_NUMBER | — | — |
| 19 | HeaderOrderTypeCode | ORDER_TYPE_CODE | — | — |
| 20 | HeaderOrderedDate | ORDERED_DATE | — | — |
| 21 | HeaderOrgId | ORG_ID | — | — |
| 22 | HeaderOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | — |
| 23 | HeaderOwnerId | OWNER_ID | — | — |
| 24 | HeaderPartialShipAllowedFlag | PARTIAL_SHIP_ALLOWED_FLAG | — | — |
| 25 | HeaderSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 26 | HeaderSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 27 | HeaderSoldToPartyContactId | SOLD_TO_PARTY_CONTACT_ID | — | — |
| 28 | HeaderSoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 29 | HeaderSourceDocumentTypeCode | SOURCE_DOCUMENT_TYPE_CODE | — | — |
| 30 | HeaderSourceOrderId | SOURCE_ORDER_ID | — | — |
| 31 | HeaderSourceOrderNumber | SOURCE_ORDER_NUMBER | — | — |
| 32 | HeaderSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | — |
| 33 | HeaderSourceOrgId | SOURCE_ORG_ID | — | — |
| 34 | HeaderStatusCode | STATUS_CODE | — | — |
| 35 | HeaderTransactionalCurrencyCode | TRANSACTIONAL_CURRENCY_CODE | — | — |

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

### [[doo_price_adjustments|DOO_PRICE_ADJUSTMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PriceAdjustmentAdjustmentName | ADJUSTMENT_NAME | — | ✅ |
| 2 | PriceAdjustmentAdjustmentTypeCode | ADJUSTMENT_TYPE_CODE | — | ✅ |
| 3 | PriceAdjustmentAmount | AMOUNT | — | ✅ |
| 4 | PriceAdjustmentCreatedBy | CREATED_BY | — | — |
| 5 | PriceAdjustmentCreationDate | CREATION_DATE | — | — |
| 6 | PriceAdjustmentCreditOrChargeFlag | CREDIT_OR_CHARGE_FLAG | — | ✅ |
| 7 | PriceAdjustmentFulfillLineId | FULFILL_LINE_ID | — | — |
| 8 | PriceAdjustmentHeaderId | HEADER_ID | — | — |
| 9 | PriceAdjustmentId | PRICE_ADJUSTMENT_ID | 🔑 | ✅ |
| 10 | PriceAdjustmentInvoicedFlag | INVOICED_FLAG | — | ✅ |
| 11 | PriceAdjustmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | PriceAdjustmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | PriceAdjustmentLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | PriceAdjustmentLineId | LINE_ID | — | — |
| 15 | PriceAdjustmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | PriceAdjustmentOrigSysAdjustmentRef | ORIG_SYS_ADJUSTMENT_REF | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitId | BU_ID | — | — |

### [[hz_cust_accounts|HZ_CUST_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillToCustomerAccountAccountEstablishedDate | ACCOUNT_ESTABLISHED_DATE | — | — |
| 2 | BillToCustomerAccountAccountName | ACCOUNT_NAME | — | — |
| 3 | BillToCustomerAccountAccountNumber | ACCOUNT_NUMBER | — | — |
| 4 | BillToCustomerAccountArrivalsetsIncludeLinesFlag | ARRIVALSETS_INCLUDE_LINES_FLAG | — | — |
| 5 | BillToCustomerAccountAutopayFlag | AUTOPAY_FLAG | — | — |
| 6 | BillToCustomerAccountComments | COMMENTS | — | — |
| 7 | BillToCustomerAccountCoterminateDayMonth | COTERMINATE_DAY_MONTH | — | — |
| 8 | BillToCustomerAccountCreatedBy | CREATED_BY | — | — |
| 9 | BillToCustomerAccountCreatedByModule | CREATED_BY_MODULE | — | — |
| 10 | BillToCustomerAccountCreationDate | CREATION_DATE | — | — |
| 11 | BillToCustomerAccountCustAccountId | CUST_ACCOUNT_ID | — | — |
| 12 | BillToCustomerAccountCustomerClassCode | CUSTOMER_CLASS_CODE | — | — |
| 13 | BillToCustomerAccountCustomerType | CUSTOMER_TYPE | — | — |
| 14 | BillToCustomerAccountDateTypePreference | DATE_TYPE_PREFERENCE | — | — |
| 15 | BillToCustomerAccountDepositRefundMethod | DEPOSIT_REFUND_METHOD | — | — |
| 16 | BillToCustomerAccountHeldBillExpirationDate | HELD_BILL_EXPIRATION_DATE | — | — |
| 17 | BillToCustomerAccountHoldBillFlag | HOLD_BILL_FLAG | — | — |
| 18 | BillToCustomerAccountLastBatchId | LAST_BATCH_ID | — | — |
| 19 | BillToCustomerAccountLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 20 | BillToCustomerAccountLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | BillToCustomerAccountLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 22 | BillToCustomerAccountNpaNumber | NPA_NUMBER | — | — |
| 23 | BillToCustomerAccountOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 24 | BillToCustomerAccountPartyId | PARTY_ID | — | — |
| 25 | BillToCustomerAccountSellingPartyId | SELLING_PARTY_ID | — | — |
| 26 | BillToCustomerAccountSourceCode | SOURCE_CODE | — | — |
| 27 | BillToCustomerAccountStatus | STATUS | — | — |
| 28 | BillToCustomerAccountStatusUpdateDate | STATUS_UPDATE_DATE | — | — |
| 29 | BillToCustomerAccountTaxCode | TAX_CODE | — | — |
| 30 | BillToCustomerAccountTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | — |
| 31 | BillToCustomerAccountTaxRoundingRule | TAX_ROUNDING_RULE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
