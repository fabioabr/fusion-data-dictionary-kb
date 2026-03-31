---
id: DOC-OTHER-PVO-OrchestrationGroup
doc_type: system-doc
title: "OrchestrationGroup — PVO Cross-Module"
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
  - OrchestrationGroup
  - orchestrationgroup
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OrchestrationGroup

## 📌 Visão Geral

View Object para extração BICC de dados de Orchestration Group. Acessa as tabelas: DOO_CVRD_FLINE_UNREF_RETRN_V, DOO_FULFILL_LINES_ALL, DOO_HEADERS_ALL (+9).

**Caminho:** `FscmTopModelAM.DooTopAM.OrchestrationGroup`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 356 | 12 | 1 | 29 | 8% |

---

## 🔗 Tabelas Relacionadas

- [[doo_cvrd_fline_unref_retrn_v|DOO_CVRD_FLINE_UNREF_RETRN_V]] — 17 atributos
- [[doo_fulfill_lines_all|DOO_FULFILL_LINES_ALL]] — 134 atributos (11 BICC)
- [[doo_headers_all|DOO_HEADERS_ALL]] — 39 atributos (3 BICC)
- [[doo_jeopardy_priorities|DOO_JEOPARDY_PRIORITIES]] — 2 atributos
- [[doo_lines_all|DOO_LINES_ALL]] — 49 atributos (1 BICC)
- [[doo_orchestration_groups|DOO_ORCHESTRATION_GROUPS]] — 25 atributos (1 PKs, 2 BICC)
- [[doo_order_terms|DOO_ORDER_TERMS]] — 6 atributos
- [[doo_process_instances|DOO_PROCESS_INSTANCES]] — 23 atributos (12 BICC)
- [[doo_projects|DOO_PROJECTS]] — 23 atributos
- [[egp_trading_partner_items|EGP_TRADING_PARTNER_ITEMS]] — 6 atributos
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 1 atributos
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 31 atributos

---

## ⚙️ Atributos

### [[doo_cvrd_fline_unref_retrn_v|DOO_CVRD_FLINE_UNREF_RETRN_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CoveredFlineUnrefRetrnCategoryCode | CATEGORY_CODE | — | — |
| 2 | CoveredFlineUnrefRetrnDocAltUserKey | DOC_ALT_USER_KEY | — | — |
| 3 | CoveredFlineUnrefRetrnDocContextId | DOC_CONTEXT_ID | — | — |
| 4 | CoveredFlineUnrefRetrnDocId | DOC_ID | — | — |
| 5 | CoveredFlineUnrefRetrnDocRefType | DOC_REF_TYPE | — | — |
| 6 | CoveredFlineUnrefRetrnDocSystemRefId | DOC_SYSTEM_REF_ID | — | — |
| 7 | CoveredFlineUnrefRetrnDocUserKey | DOC_USER_KEY | — | — |
| 8 | CoveredFlineUnrefRetrnDocumentFulfillLineId | DOCUMENT_FULFILL_LINE_ID | — | — |
| 9 | CoveredFlineUnrefRetrnDocumentHeaderId | DOCUMENT_HEADER_ID | — | — |
| 10 | CoveredFlineUnrefRetrnDocumentLineId | DOCUMENT_LINE_ID | — | — |
| 11 | CoveredFlineUnrefRetrnFlineFulfillLineId | FLINE_FULFILL_LINE_ID | — | — |
| 12 | CoveredFlineUnrefRetrnFlineHeaderId | FLINE_HEADER_ID | — | — |
| 13 | CoveredFlineUnrefRetrnFlineLineId | FLINE_LINE_ID | — | — |
| 14 | CoveredFlineUnrefRetrnInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 15 | CoveredFlineUnrefRetrnInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 16 | CoveredFlineUnrefRetrnOwnerTableId | OWNER_TABLE_ID | — | — |
| 17 | CoveredFlineUnrefRetrnStatusCode | STATUS_CODE | — | — |

### [[doo_fulfill_lines_all|DOO_FULFILL_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CancelBackordersFlag | CANCEL_BACKORDERS_FLAG | — | — |
| 2 | EnforceSingleShipmentFlag | ENFORCE_SINGLE_SHIPMENT_FLAG | — | — |
| 3 | FulfillLineAccountingRuleId | ACCOUNTING_RULE_ID | — | — |
| 4 | FulfillLineActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
| 5 | FulfillLineActualShipDate | ACTUAL_SHIP_DATE | — | — |
| 6 | FulfillLineBillToContactId | BILL_TO_CONTACT_ID | — | — |
| 7 | FulfillLineBillToCustomerId | BILL_TO_CUSTOMER_ID | — | — |
| 8 | FulfillLineBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 9 | FulfillLineCancelReasonCode | CANCEL_REASON_CODE | — | ✅ |
| 10 | FulfillLineCanceledFlag | CANCELED_FLAG | — | — |
| 11 | FulfillLineCanceledQty | CANCELED_QTY | — | — |
| 12 | FulfillLineCarrierId | CARRIER_ID | — | — |
| 13 | FulfillLineCategoryCode | CATEGORY_CODE | — | — |
| 14 | FulfillLineCompSeqPath | COMP_SEQ_PATH | — | — |
| 15 | FulfillLineConfigItemVersion | CONFIG_ITEM_VERSION | — | — |
| 16 | FulfillLineCreatedBy | CREATED_BY | — | — |
| 17 | FulfillLineCreationDate | CREATION_DATE | — | ✅ |
| 18 | FulfillLineCustomerItemId | CUSTOMER_ITEM_ID | — | — |
| 19 | FulfillLineCustomerPoLineNumber | CUSTOMER_PO_LINE_NUMBER | — | — |
| 20 | FulfillLineCustomerPoNumber | CUSTOMER_PO_NUMBER | — | — |
| 21 | FulfillLineDeltaType | DELTA_TYPE | — | — |
| 22 | FulfillLineDemandClassCode | DEMAND_CLASS_CODE | — | — |
| 23 | FulfillLineDemandSourceLineReference | DEMAND_SOURCE_LINE_REFERENCE | — | — |
| 24 | FulfillLineEarliestAcceptableShipDate | EARLIEST_ACCEPTABLE_SHIP_DATE | — | — |
| 25 | FulfillLineEndCreditMethodCode | END_CREDIT_METHOD_CODE | — | — |
| 26 | FulfillLineEndDate | END_DATE | — | — |
| 27 | FulfillLineEndReasonCode | END_REASON_CODE | — | — |
| 28 | FulfillLineEstimateFulfillmentCost | ESTIMATE_FULFILLMENT_COST | — | — |
| 29 | FulfillLineEstimateMargin | ESTIMATE_MARGIN | — | — |
| 30 | FulfillLineExemptionCertificateNumber | EXEMPTION_CERTIFICATE_NUMBER | — | — |
| 31 | FulfillLineExtendedAmount | EXTENDED_AMOUNT | — | — |
| 32 | FulfillLineExternalPriceBookName | EXTERNAL_PRICE_BOOK_NAME | — | — |
| 33 | FulfillLineFobPointCode | FOB_POINT_CODE | — | — |
| 34 | FulfillLineFulfillInstanceId | FULFILL_INSTANCE_ID | — | — |
| 35 | FulfillLineFulfillLineId | FULFILL_LINE_ID | — | — |
| 36 | FulfillLineFulfillLineNumber | FULFILL_LINE_NUMBER | — | — |
| 37 | FulfillLineFulfillOrgId | FULFILL_ORG_ID | — | — |
| 38 | FulfillLineFulfillToleranceAbove | FULFILL_TOLERANCE_ABOVE | — | — |
| 39 | FulfillLineFulfillToleranceBelow | FULFILL_TOLERANCE_BELOW | — | — |
| 40 | FulfillLineFulfilledQty | FULFILLED_QTY | — | — |
| 41 | FulfillLineFulfillmentDate | FULFILLMENT_DATE | — | — |
| 42 | FulfillLineFulfillmentSplitRefId | FULFILLMENT_SPLIT_REF_ID | — | ✅ |
| 43 | FulfillLineGopReferenceId | GOP_REFERENCE_ID | — | — |
| 44 | FulfillLineHeaderId | HEADER_ID | — | — |
| 45 | FulfillLineInventoryInterfacedFlag | INVENTORY_INTERFACED_FLAG | — | ✅ |
| 46 | FulfillLineInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 47 | FulfillLineInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 48 | FulfillLineInventoryTransactionFlag | INVENTORY_TRANSACTION_FLAG | — | ✅ |
| 49 | FulfillLineInvoiceEnabledFlag | INVOICE_ENABLED_FLAG | — | — |
| 50 | FulfillLineInvoiceableItemFlag | INVOICEABLE_ITEM_FLAG | — | — |
| 51 | FulfillLineInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 52 | FulfillLineItemTypeCode | ITEM_TYPE_CODE | — | — |
| 53 | FulfillLineLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 54 | FulfillLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 55 | FulfillLineLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 56 | FulfillLineLatestAcceptableArrivalDate | LATEST_ACCEPTABLE_ARRIVAL_DATE | — | — |
| 57 | FulfillLineLatestAcceptableShipDate | LATEST_ACCEPTABLE_SHIP_DATE | — | — |
| 58 | FulfillLineLineId | LINE_ID | — | — |
| 59 | FulfillLineLineTypeCode | LINE_TYPE_CODE | — | — |
| 60 | FulfillLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 61 | FulfillLineOnHold | ON_HOLD | — | — |
| 62 | FulfillLineOneTimeConfigFlag | ONE_TIME_CONFIG_FLAG | — | — |
| 63 | FulfillLineOpenFlag | OPEN_FLAG | — | — |
| 64 | FulfillLineOrderedQty | ORDERED_QTY | — | — |
| 65 | FulfillLineOrderedUom | ORDERED_UOM | — | — |
| 66 | FulfillLineOrgId | ORG_ID | — | — |
| 67 | FulfillLineOrigSysDocumentLineRef | ORIG_SYS_DOCUMENT_LINE_REF | — | — |
| 68 | FulfillLineOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | — |
| 69 | FulfillLineOriginalInventoryItemId | ORIGINAL_INVENTORY_ITEM_ID | — | — |
| 70 | FulfillLineOverrideScheduleDateFlag | OVERRIDE_SCHEDULE_DATE_FLAG | — | — |
| 71 | FulfillLineOwnerId | OWNER_ID | — | — |
| 72 | FulfillLinePackingInstructions | PACKING_INSTRUCTIONS | — | — |
| 73 | FulfillLineParentFulfillLineId | PARENT_FULFILL_LINE_ID | — | — |
| 74 | FulfillLinePartialShipAllowedFlag | PARTIAL_SHIP_ALLOWED_FLAG | — | — |
| 75 | FulfillLinePaymentTermId | PAYMENT_TERM_ID | — | — |
| 76 | FulfillLinePriceUsingSecUomFlag | PRICE_USING_SEC_UOM_FLAG | — | ✅ |
| 77 | FulfillLinePrjRecIndicator | PRJ_REC_INDICATOR | — | — |
| 78 | FulfillLinePromiseArrivalDate | PROMISE_ARRIVAL_DATE | — | — |
| 79 | FulfillLinePromiseShipDate | PROMISE_SHIP_DATE | — | — |
| 80 | FulfillLineReferenceFlineId | REFERENCE_FLINE_ID | — | — |
| 81 | FulfillLineRemnantFlag | REMNANT_FLAG | — | — |
| 82 | FulfillLineRequestArrivalDate | REQUEST_ARRIVAL_DATE | — | — |
| 83 | FulfillLineRequestShipDate | REQUEST_SHIP_DATE | — | — |
| 84 | FulfillLineRequestType | REQUEST_TYPE | — | — |
| 85 | FulfillLineReservableFlag | RESERVABLE_FLAG | — | — |
| 86 | FulfillLineReservationId | RESERVATION_ID | — | — |
| 87 | FulfillLineReservedQty | RESERVED_QTY | — | — |
| 88 | FulfillLineReturnReasonCode | RETURN_REASON_CODE | — | — |
| 89 | FulfillLineReturnableFlag | RETURNABLE_FLAG | — | — |
| 90 | FulfillLineRmaDeliveredQty | RMA_DELIVERED_QTY | — | — |
| 91 | FulfillLineRootParentFulfillLineId | ROOT_PARENT_FULFILL_LINE_ID | — | — |
| 92 | FulfillLineScheduleArrivalDate | SCHEDULE_ARRIVAL_DATE | — | — |
| 93 | FulfillLineScheduleShipDate | SCHEDULE_SHIP_DATE | — | — |
| 94 | FulfillLineSecondaryFulfilledQty | SECONDARY_FULFILLED_QTY | — | ✅ |
| 95 | FulfillLineSecondaryOrderedQty | SECONDARY_ORDERED_QTY | — | ✅ |
| 96 | FulfillLineSecondaryRmaDeliveredQty | SECONDARY_RMA_DELIVERED_QTY | — | — |
| 97 | FulfillLineSecondaryShippedQty | SECONDARY_SHIPPED_QTY | — | ✅ |
| 98 | FulfillLineSecondaryUom | SECONDARY_UOM | — | ✅ |
| 99 | FulfillLineSellingProfitCenterBUId | SELLING_PROFIT_CENTER_BU_ID | — | — |
| 100 | FulfillLineServiceCancelDate | SERVICE_CANCEL_DATE | — | — |
| 101 | FulfillLineShipClassOfService | SHIP_CLASS_OF_SERVICE | — | — |
| 102 | FulfillLineShipModeOfTransport | SHIP_MODE_OF_TRANSPORT | — | — |
| 103 | FulfillLineShipSetName | SHIP_SET_NAME | — | — |
| 104 | FulfillLineShipToContactId | SHIP_TO_CONTACT_ID | — | — |
| 105 | FulfillLineShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | — |
| 106 | FulfillLineShipToPartyContactId | SHIP_TO_PARTY_CONTACT_ID | — | — |
| 107 | FulfillLineShipToPartyId | SHIP_TO_PARTY_ID | — | — |
| 108 | FulfillLineShipToPartySiteId | SHIP_TO_PARTY_SITE_ID | — | — |
| 109 | FulfillLineShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 110 | FulfillLineShipmentPriorityCode | SHIPMENT_PRIORITY_CODE | — | — |
| 111 | FulfillLineShippableFlag | SHIPPABLE_FLAG | — | — |
| 112 | FulfillLineShippedQty | SHIPPED_QTY | — | — |
| 113 | FulfillLineShippingInstructions | SHIPPING_INSTRUCTIONS | — | — |
| 114 | FulfillLineSourceLineId | SOURCE_LINE_ID | — | — |
| 115 | FulfillLineSourceLineNumber | SOURCE_LINE_NUMBER | — | — |
| 116 | FulfillLineSourceOrderId | SOURCE_ORDER_ID | — | — |
| 117 | FulfillLineSourceOrderNumber | SOURCE_ORDER_NUMBER | — | — |
| 118 | FulfillLineSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | — |
| 119 | FulfillLineSourceOrgId | SOURCE_ORG_ID | — | — |
| 120 | FulfillLineSourceScheduleId | SOURCE_SCHEDULE_ID | — | — |
| 121 | FulfillLineSourceScheduleNumber | SOURCE_SCHEDULE_NUMBER | — | — |
| 122 | FulfillLineSplitFromFlineId | SPLIT_FROM_FLINE_ID | — | — |
| 123 | FulfillLineStatusCode | STATUS_CODE | — | — |
| 124 | FulfillLineStatusRulesetId | STATUS_RULESET_ID | — | — |
| 125 | FulfillLineSubinventory | SUBINVENTORY | — | — |
| 126 | FulfillLineSubscriptionInterfacedFlag | SUBSCRIPTION_INTERFACED_FLAG | — | — |
| 127 | FulfillLineSubstituteAllowedFlag | SUBSTITUTE_ALLOWED_FLAG | — | — |
| 128 | FulfillLineSubstituteReasonCode | SUBSTITUTE_REASON_CODE | — | — |
| 129 | FulfillLineTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 130 | FulfillLineTaxExemptFlag | TAX_EXEMPT_FLAG | — | — |
| 131 | FulfillLineTaxExemptionReasonCode | TAX_EXEMPTION_REASON_CODE | — | — |
| 132 | FulfillLineUnitListPrice | UNIT_LIST_PRICE | — | — |
| 133 | FulfillLineUnitSellingPrice | UNIT_SELLING_PRICE | — | — |
| 134 | FulfillLineUnreferencedReturnFlag | UNREFERENCED_RETURN_FLAG | — | — |

### [[doo_headers_all|DOO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HeaderCancelReasonCode | CANCEL_REASON_CODE | — | ✅ |
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
| 17 | HeaderOnHold | ON_HOLD | — | ✅ |
| 18 | HeaderOpenFlag | OPEN_FLAG | — | — |
| 19 | HeaderOrderNumber | ORDER_NUMBER | — | — |
| 20 | HeaderOrderTypeCode | ORDER_TYPE_CODE | — | — |
| 21 | HeaderOrderedDate | ORDERED_DATE | — | — |
| 22 | HeaderOrgId | ORG_ID | — | — |
| 23 | HeaderOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | — |
| 24 | HeaderOwnerId | OWNER_ID | — | — |
| 25 | HeaderPartialShipAllowedFlag | PARTIAL_SHIP_ALLOWED_FLAG | — | — |
| 26 | HeaderPricingDate | PRICING_DATE | — | — |
| 27 | HeaderRequestShipDate | REQUEST_SHIP_DATE | — | ✅ |
| 28 | HeaderSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 29 | HeaderSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 30 | HeaderSoldToPartyContactId | SOLD_TO_PARTY_CONTACT_ID | — | — |
| 31 | HeaderSoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 32 | HeaderSourceDocumentTypeCode | SOURCE_DOCUMENT_TYPE_CODE | — | — |
| 33 | HeaderSourceOrderId | SOURCE_ORDER_ID | — | — |
| 34 | HeaderSourceOrderNumber | SOURCE_ORDER_NUMBER | — | — |
| 35 | HeaderSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | — |
| 36 | HeaderSourceOrgId | SOURCE_ORG_ID | — | — |
| 37 | HeaderStatusCode | STATUS_CODE | — | — |
| 38 | HeaderSubmittedFlag | SUBMITTED_FLAG | — | — |
| 39 | HeaderTransactionalCurrencyCode | TRANSACTIONAL_CURRENCY_CODE | — | — |

### [[doo_jeopardy_priorities|DOO_JEOPARDY_PRIORITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JeopardyPriorityJeopardyPriorityCode | JEOPARDY_PRIORITY_CODE | — | — |
| 2 | JeopardyPriorityJeopardyPriorityId | JEOPARDY_PRIORITY_ID | — | — |

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
| 9 | LineDisplayLineNumber | DISPLAY_LINE_NUMBER | — | — |
| 10 | LineExtendedAmount | EXTENDED_AMOUNT | — | — |
| 11 | LineFulfilledQty | FULFILLED_QTY | — | — |
| 12 | LineFulfillmentDate | FULFILLMENT_DATE | — | — |
| 13 | LineHeaderId | HEADER_ID | — | — |
| 14 | LineInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 15 | LineInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 16 | LineItemTypeCode | ITEM_TYPE_CODE | — | — |
| 17 | LineLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 18 | LineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | LineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | LineLineId | LINE_ID | — | — |
| 21 | LineLineNumber | LINE_NUMBER | — | — |
| 22 | LineLineTypeCode | LINE_TYPE_CODE | — | — |
| 23 | LineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | LineOnHold | ON_HOLD | — | ✅ |
| 25 | LineOpenFlag | OPEN_FLAG | — | — |
| 26 | LineOrderedQty | ORDERED_QTY | — | — |
| 27 | LineOrderedUom | ORDERED_UOM | — | — |
| 28 | LineOrgId | ORG_ID | — | — |
| 29 | LineOrigSysDocumentLineRef | ORIG_SYS_DOCUMENT_LINE_REF | — | — |
| 30 | LineOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | — |
| 31 | LineOwnerId | OWNER_ID | — | — |
| 32 | LineParentLineId | PARENT_LINE_ID | — | — |
| 33 | LineReferenceLineId | REFERENCE_LINE_ID | — | — |
| 34 | LineRmaDeliveredQty | RMA_DELIVERED_QTY | — | — |
| 35 | LineRootParentLineId | ROOT_PARENT_LINE_ID | — | — |
| 36 | LineScheduleShipDate | SCHEDULE_SHIP_DATE | — | — |
| 37 | LineShippedQty | SHIPPED_QTY | — | — |
| 38 | LineSourceLineId | SOURCE_LINE_ID | — | — |
| 39 | LineSourceLineNumber | SOURCE_LINE_NUMBER | — | — |
| 40 | LineSourceOrderId | SOURCE_ORDER_ID | — | — |
| 41 | LineSourceOrderNumber | SOURCE_ORDER_NUMBER | — | — |
| 42 | LineSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | — |
| 43 | LineSourceOrgId | SOURCE_ORG_ID | — | — |
| 44 | LineSourceScheduleId | SOURCE_SCHEDULE_ID | — | — |
| 45 | LineSourceScheduleNumber | SOURCE_SCHEDULE_NUMBER | — | — |
| 46 | LineStatusCode | STATUS_CODE | — | — |
| 47 | LineTransformFromLineId | TRANSFORM_FROM_LINE_ID | — | — |
| 48 | LineUnitListPrice | UNIT_LIST_PRICE | — | — |
| 49 | LineUnitSellingPrice | UNIT_SELLING_PRICE | — | — |

### [[doo_orchestration_groups|DOO_ORCHESTRATION_GROUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GroupSeqId | GROUP_SEQ_ID | 🔑 | ✅ |
| 2 | OrchestrationGroupCreatedBy | CREATED_BY | — | — |
| 3 | OrchestrationGroupCreationDate | CREATION_DATE | — | — |
| 4 | OrchestrationGroupDeltaType | DELTA_TYPE | — | — |
| 5 | OrchestrationGroupDooProcessId | DOO_PROCESS_ID | — | — |
| 6 | OrchestrationGroupDooProcessInstanceId | DOO_PROCESS_INSTANCE_ID | — | — |
| 7 | OrchestrationGroupDooProcessVersion | DOO_PROCESS_VERSION | — | — |
| 8 | OrchestrationGroupFulfillmentLineId | FULFILLMENT_LINE_ID | — | — |
| 9 | OrchestrationGroupGroupCreatedBy | GROUP_CREATED_BY | — | — |
| 10 | OrchestrationGroupGroupId | GROUP_ID | — | — |
| 11 | OrchestrationGroupGroupSetName | GROUP_SET_NAME | — | — |
| 12 | OrchestrationGroupGroupSetType | GROUP_SET_TYPE | — | — |
| 13 | OrchestrationGroupHeaderId | HEADER_ID | — | — |
| 14 | OrchestrationGroupIsGroupEditable | IS_GROUP_EDITABLE | — | — |
| 15 | OrchestrationGroupLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | OrchestrationGroupLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | OrchestrationGroupLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | OrchestrationGroupLineId | LINE_ID | — | — |
| 19 | OrchestrationGroupObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | OrchestrationGroupOrgId | ORG_ID | — | — |
| 21 | OrchestrationGroupParentGroupId | PARENT_GROUP_ID | — | — |
| 22 | OrchestrationGroupReferenceGroupId | REFERENCE_GROUP_ID | — | — |
| 23 | OrchestrationGroupRootParentGroupId | ROOT_PARENT_GROUP_ID | — | — |
| 24 | OrchestrationGroupSplitGroupFromId | SPLIT_GROUP_FROM_ID | — | — |
| 25 | OrchestrationGroupStatus | STATUS | — | — |

### [[doo_order_terms|DOO_ORDER_TERMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrderTermOrderTermId | ORDER_TERM_ID | — | — |
| 2 | OrderTermTermApplicationMethod | TERM_APPLICATION_METHOD | — | — |
| 3 | OrderTermTermApplicationValuePct | TERM_APPLICATION_VALUE_PCT | — | — |
| 4 | OrderTermTermDuration | TERM_DURATION | — | — |
| 5 | OrderTermTermPeriod | TERM_PERIOD | — | — |
| 6 | OrderTermTermStartDate | TERM_START_DATE | — | — |

### [[doo_process_instances|DOO_PROCESS_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessInstanceActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 2 | ProcessInstanceActualFulfillDate | ACTUAL_FULFILL_DATE | — | — |
| 3 | ProcessInstanceActualStartDate | ACTUAL_START_DATE | — | ✅ |
| 4 | ProcessInstanceBpelInstanceId | BPEL_INSTANCE_ID | — | — |
| 5 | ProcessInstanceCreatedBy | CREATED_BY | — | — |
| 6 | ProcessInstanceCreationDate | CREATION_DATE | — | ✅ |
| 7 | ProcessInstanceDooProcessId | DOO_PROCESS_ID | — | ✅ |
| 8 | ProcessInstanceDooProcessInstanceId | DOO_PROCESS_INSTANCE_ID | — | ✅ |
| 9 | ProcessInstanceDooProcessVersion | DOO_PROCESS_VERSION | — | — |
| 10 | ProcessInstanceJeopardyReason | JEOPARDY_REASON | — | ✅ |
| 11 | ProcessInstanceJeopardyReasonTaskInstId | JEOPARDY_REASON_TASK_INST_ID | — | — |
| 12 | ProcessInstanceJeopardyScore | JEOPARDY_SCORE | — | ✅ |
| 13 | ProcessInstanceLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 14 | ProcessInstanceLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | ProcessInstanceLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | ProcessInstanceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | ProcessInstancePlannedCompletionDate | PLANNED_COMPLETION_DATE | — | ✅ |
| 18 | ProcessInstancePlannedFulfillDate | PLANNED_FULFILL_DATE | — | — |
| 19 | ProcessInstanceProcessActive | PROCESS_ACTIVE | — | ✅ |
| 20 | ProcessInstanceProcessNumber | PROCESS_NUMBER | — | ✅ |
| 21 | ProcessInstanceReferenceProcessInstanceId | REFERENCE_PROCESS_INSTANCE_ID | — | — |
| 22 | ProcessInstanceRequiredFulfillDate | REQUIRED_FULFILL_DATE | — | ✅ |
| 23 | ProcessInstanceStatusCode | STATUS_CODE | — | ✅ |

### [[doo_projects|DOO_PROJECTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectCreatedBy | CREATED_BY | — | — |
| 2 | ProjectCreationDate | CREATION_DATE | — | — |
| 3 | ProjectDooOrderPrjId | DOO_ORDER_PRJ_ID | — | — |
| 4 | ProjectLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 5 | ProjectLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ProjectLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ProjectModifiedFlag | MODIFIED_FLAG | — | — |
| 8 | ProjectObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ProjectParentEntityCode | PARENT_ENTITY_CODE | — | — |
| 10 | ProjectParentEntityId | PARENT_ENTITY_ID | — | — |
| 11 | ProjectPjcBillableFlag | PJC_BILLABLE_FLAG | — | — |
| 12 | ProjectPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | — |
| 13 | ProjectPjcContextCategory | PJC_CONTEXT_CATEGORY | — | — |
| 14 | ProjectPjcContractId | PJC_CONTRACT_ID | — | — |
| 15 | ProjectPjcContractLineId | PJC_CONTRACT_LINE_ID | — | — |
| 16 | ProjectPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 17 | ProjectPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | — |
| 18 | ProjectPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | — |
| 19 | ProjectPjcOrganizationId | PJC_ORGANIZATION_ID | — | — |
| 20 | ProjectPjcProjectId | PJC_PROJECT_ID | — | — |
| 21 | ProjectPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 22 | ProjectPjcTaskId | PJC_TASK_ID | — | — |
| 23 | ProjectPjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |

### [[egp_trading_partner_items|EGP_TRADING_PARTNER_ITEMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TradingPartnerItemEndDate | END_DATE | — | — |
| 2 | TradingPartnerItemStartDate | START_DATE | — | — |
| 3 | TradingPartnerItemTpItemDesc | TP_ITEM_DESC | — | — |
| 4 | TradingPartnerItemTpItemId | TP_ITEM_ID | — | — |
| 5 | TradingPartnerItemTpItemNumber | TP_ITEM_NUMBER | — | — |
| 6 | TradingPartnerItemTpType | TP_TYPE | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUBusinessUnitId | BU_ID | — | — |

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
