---
id: DOC-OTHER-PVO-ManualPriceAdjustment
doc_type: system-doc
title: "ManualPriceAdjustment — PVO Cross-Module"
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
  - ManualPriceAdjustment
  - manualpriceadjustment
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ManualPriceAdjustment

## 📌 Visão Geral

View Object para extração BICC de dados de Manual Price Adjustment. Acessa as tabelas: DOO_COVERAGE_FLINES_DETAILS_V, DOO_COVERED_FLINES_DETAILS_V, DOO_CVRD_FLINE_UNREF_RETRN_V (+17).

**Caminho:** `FscmTopModelAM.DooTopAM.ManualPriceAdjustment`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 486 | 20 | 2 | 167 | 34% |

---

## 🔗 Tabelas Relacionadas

- [[doo_coverage_flines_details_v|DOO_COVERAGE_FLINES_DETAILS_V]] — 19 atributos
- [[doo_covered_flines_details_v|DOO_COVERED_FLINES_DETAILS_V]] — 20 atributos
- [[doo_cvrd_fline_unref_retrn_v|DOO_CVRD_FLINE_UNREF_RETRN_V]] — 17 atributos
- [[doo_document_references|DOO_DOCUMENT_REFERENCES]] — 14 atributos
- [[doo_doc_references_dropship_v|DOO_DOC_REFERENCES_DROPSHIP_V]] — 5 atributos
- [[doo_doc_references_supply_v|DOO_DOC_REFERENCES_SUPPLY_V]] — 4 atributos
- [[doo_fulfill_lines_all|DOO_FULFILL_LINES_ALL]] — 172 atributos (1 PKs, 141 BICC)
- [[doo_headers_all|DOO_HEADERS_ALL]] — 46 atributos (2 BICC)
- [[doo_lines_all|DOO_LINES_ALL]] — 49 atributos
- [[doo_manual_price_adjustments|DOO_MANUAL_PRICE_ADJUSTMENTS]] — 27 atributos (1 PKs, 23 BICC)
- [[doo_order_terms|DOO_ORDER_TERMS]] — 6 atributos
- [[doo_projects|DOO_PROJECTS]] — 23 atributos
- [[dos_supply_buy_order_dtls|DOS_SUPPLY_BUY_ORDER_DTLS]] — 8 atributos
- [[dos_supply_make_order_dtls|DOS_SUPPLY_MAKE_ORDER_DTLS]] — 6 atributos
- [[dos_supply_tracking_lines|DOS_SUPPLY_TRACKING_LINES]] — 3 atributos
- [[egp_trading_partner_items|EGP_TRADING_PARTNER_ITEMS]] — 28 atributos (1 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 3 atributos
- [[gl_ledgers|GL_LEDGERS]] — 3 atributos
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 31 atributos
- [[hz_cust_account_roles|HZ_CUST_ACCOUNT_ROLES]] — 2 atributos

---

## ⚙️ Atributos

### [[doo_coverage_flines_details_v|DOO_COVERAGE_FLINES_DETAILS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CoverageFlineDetailsConfigItemReference | CONFIG_ITEM_REFERENCE | — | — |
| 2 | CoverageFlineDetailsContractEndDate | CONTRACT_END_DATE | — | — |
| 3 | CoverageFlineDetailsContractStartDate | CONTRACT_START_DATE | — | — |
| 4 | CoverageFlineDetailsDocRefType | DOC_REF_TYPE | — | — |
| 5 | CoverageFlineDetailsDocSystemRefId | DOC_SYSTEM_REF_ID | — | — |
| 6 | CoverageFlineDetailsDocumentFulfillLineId | DOCUMENT_FULFILL_LINE_ID | — | — |
| 7 | CoverageFlineDetailsFlineFulfillLineId | FLINE_FULFILL_LINE_ID | — | — |
| 8 | CoverageFlineDetailsFlineHeaderId | FLINE_HEADER_ID | — | — |
| 9 | CoverageFlineDetailsFlineLineId | FLINE_LINE_ID | — | — |
| 10 | CoverageFlineDetailsFulfillLineNumber | FULFILL_LINE_NUMBER | — | — |
| 11 | CoverageFlineDetailsInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 12 | CoverageFlineDetailsInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 13 | CoverageFlineDetailsSalesProductTypeCode | SALES_PRODUCT_TYPE_CODE | — | — |
| 14 | CoverageFlineDetailsServiceDuration | SERVICE_DURATION | — | — |
| 15 | CoverageFlineDetailsServiceDurationPeriodCode | SERVICE_DURATION_PERIOD_CODE | — | — |
| 16 | CoverageFlineDetailsSourceLineNumber | SOURCE_LINE_NUMBER | — | — |
| 17 | CoverageFlineDetailsSourceOrderNumber | SOURCE_ORDER_NUMBER | — | — |
| 18 | CoverageFlineDetailsSourceRevisionNumber | SOURCE_REVISION_NUMBER | — | — |
| 19 | CoverageFlineDetailsSourceScheduleNumber | SOURCE_SCHEDULE_NUMBER | — | — |

### [[doo_covered_flines_details_v|DOO_COVERED_FLINES_DETAILS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CoveredFlineDetailsConfigItemReference | CONFIG_ITEM_REFERENCE | — | — |
| 2 | CoveredFlineDetailsContractEndDate | CONTRACT_END_DATE | — | — |
| 3 | CoveredFlineDetailsContractStartDate | CONTRACT_START_DATE | — | — |
| 4 | CoveredFlineDetailsDocRefType | DOC_REF_TYPE | — | — |
| 5 | CoveredFlineDetailsDocSublineId | DOC_SUBLINE_ID | — | — |
| 6 | CoveredFlineDetailsDocSystemRefId | DOC_SYSTEM_REF_ID | — | — |
| 7 | CoveredFlineDetailsDocumentFulfillLineId | DOCUMENT_FULFILL_LINE_ID | — | — |
| 8 | CoveredFlineDetailsFlineFulfillLineId | FLINE_FULFILL_LINE_ID | — | — |
| 9 | CoveredFlineDetailsFlineHeaderId | FLINE_HEADER_ID | — | — |
| 10 | CoveredFlineDetailsFlineLineId | FLINE_LINE_ID | — | — |
| 11 | CoveredFlineDetailsFulfillLineNumber | FULFILL_LINE_NUMBER | — | — |
| 12 | CoveredFlineDetailsInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 13 | CoveredFlineDetailsInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 14 | CoveredFlineDetailsSalesProductTypeCode | SALES_PRODUCT_TYPE_CODE | — | — |
| 15 | CoveredFlineDetailsServiceDuration | SERVICE_DURATION | — | — |
| 16 | CoveredFlineDetailsServiceDurationPeriodCode | SERVICE_DURATION_PERIOD_CODE | — | — |
| 17 | CoveredFlineDetailsSourceLineNumber | SOURCE_LINE_NUMBER | — | — |
| 18 | CoveredFlineDetailsSourceOrderNumber | SOURCE_ORDER_NUMBER | — | — |
| 19 | CoveredFlineDetailsSourceRevisionNumber | SOURCE_REVISION_NUMBER | — | — |
| 20 | CoveredFlineDetailsSourceScheduleNumber | SOURCE_SCHEDULE_NUMBER | — | — |

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

### [[doo_document_references|DOO_DOCUMENT_REFERENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocumentReferencesDocAltUserKey | DOC_ALT_USER_KEY | — | — |
| 2 | DocumentReferencesDocContextId | DOC_CONTEXT_ID | — | — |
| 3 | DocumentReferencesDocId | DOC_ID | — | — |
| 4 | DocumentReferencesDocLineAltUserKey | DOC_LINE_ALT_USER_KEY | — | — |
| 5 | DocumentReferencesDocLineContextId | DOC_LINE_CONTEXT_ID | — | — |
| 6 | DocumentReferencesDocLineId | DOC_LINE_ID | — | — |
| 7 | DocumentReferencesDocLineUserKey | DOC_LINE_USER_KEY | — | — |
| 8 | DocumentReferencesDocRefType | DOC_REF_TYPE | — | — |
| 9 | DocumentReferencesDocSublineAltUserKey | DOC_SUBLINE_ALT_USER_KEY | — | — |
| 10 | DocumentReferencesDocSublineContextId | DOC_SUBLINE_CONTEXT_ID | — | — |
| 11 | DocumentReferencesDocSublineId | DOC_SUBLINE_ID | — | — |
| 12 | DocumentReferencesDocSublineUserKey | DOC_SUBLINE_USER_KEY | — | — |
| 13 | DocumentReferencesDocSystemRefId | DOC_SYSTEM_REF_ID | — | — |
| 14 | DocumentReferencesDocUserKey | DOC_USER_KEY | — | — |

### [[doo_doc_references_dropship_v|DOO_DOC_REFERENCES_DROPSHIP_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocReferencesDropShipDocLineUserKey | DOC_LINE_USER_KEY | — | — |
| 2 | DocReferencesDropShipDocRefType | DOC_REF_TYPE | — | — |
| 3 | DocReferencesDropShipDocSublineUserKey | DOC_SUBLINE_USER_KEY | — | — |
| 4 | DocReferencesDropShipDocSystemRefId | DOC_SYSTEM_REF_ID | — | — |
| 5 | DocReferencesDropshipDocUserKey | DOC_USER_KEY | — | — |

### [[doo_doc_references_supply_v|DOO_DOC_REFERENCES_SUPPLY_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocReferencesSupplyDocAltUserKey | DOC_ALT_USER_KEY | — | — |
| 2 | DocReferencesSupplyDocRefType | DOC_REF_TYPE | — | — |
| 3 | DocReferencesSupplyDocSystemRefId | DOC_SYSTEM_REF_ID | — | — |
| 4 | DocReferencesSupplyDocUserKey | DOC_USER_KEY | — | — |

### [[doo_fulfill_lines_all|DOO_FULFILL_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CancelBackordersFlag | CANCEL_BACKORDERS_FLAG | — | — |
| 2 | EnforceSingleShipmentFlag | ENFORCE_SINGLE_SHIPMENT_FLAG | — | — |
| 3 | FulfillLineAccountingRuleId | ACCOUNTING_RULE_ID | — | ✅ |
| 4 | FulfillLineActionTypeCode | ACTION_TYPE_CODE | — | ✅ |
| 5 | FulfillLineActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 6 | FulfillLineActualShipDate | ACTUAL_SHIP_DATE | — | ✅ |
| 7 | FulfillLineAgreementHeaderId | AGREEMENT_HEADER_ID | — | — |
| 8 | FulfillLineAgreementLineId | AGREEMENT_LINE_ID | — | — |
| 9 | FulfillLineAgreementVersionNumber | AGREEMENT_VERSION_NUMBER | — | — |
| 10 | FulfillLineAssetGroupNumber | ASSET_GROUP_NUMBER | — | ✅ |
| 11 | FulfillLineAssetTrackedFlag | ASSET_TRACKED_FLAG | — | ✅ |
| 12 | FulfillLineBillToContactId | BILL_TO_CONTACT_ID | — | ✅ |
| 13 | FulfillLineBillToCustomerId | BILL_TO_CUSTOMER_ID | — | ✅ |
| 14 | FulfillLineBillToSiteUseId | BILL_TO_SITE_USE_ID | — | ✅ |
| 15 | FulfillLineBillingTrxTypeId | BILLING_TRX_TYPE_ID | — | ✅ |
| 16 | FulfillLineCancelReasonCode | CANCEL_REASON_CODE | — | ✅ |
| 17 | FulfillLineCanceledFlag | CANCELED_FLAG | — | ✅ |
| 18 | FulfillLineCanceledQty | CANCELED_QTY | — | ✅ |
| 19 | FulfillLineCarrierId | CARRIER_ID | — | ✅ |
| 20 | FulfillLineCategoryCode | CATEGORY_CODE | — | ✅ |
| 21 | FulfillLineCompSeqPath | COMP_SEQ_PATH | — | ✅ |
| 22 | FulfillLineConfigInventoryItemId | CONFIG_INVENTORY_ITEM_ID | — | ✅ |
| 23 | FulfillLineConfigItemReference | CONFIG_ITEM_REFERENCE | — | ✅ |
| 24 | FulfillLineConfigItemVersion | CONFIG_ITEM_VERSION | — | — |
| 25 | FulfillLineContractEndDate | CONTRACT_END_DATE | — | ✅ |
| 26 | FulfillLineContractStartDate | CONTRACT_START_DATE | — | ✅ |
| 27 | FulfillLineCreatedBy | CREATED_BY | — | ✅ |
| 28 | FulfillLineCreationDate | CREATION_DATE | — | ✅ |
| 29 | FulfillLineCustomerItemId | CUSTOMER_ITEM_ID | — | ✅ |
| 30 | FulfillLineCustomerPoLineNumber | CUSTOMER_PO_LINE_NUMBER | — | ✅ |
| 31 | FulfillLineCustomerPoNumber | CUSTOMER_PO_NUMBER | — | ✅ |
| 32 | FulfillLineDeltaType | DELTA_TYPE | — | ✅ |
| 33 | FulfillLineDemandClassCode | DEMAND_CLASS_CODE | — | ✅ |
| 34 | FulfillLineDemandSourceLineReference | DEMAND_SOURCE_LINE_REFERENCE | — | — |
| 35 | FulfillLineDestinationOrgId | DESTINATION_ORG_ID | — | ✅ |
| 36 | FulfillLineEarliestAcceptableShipDate | EARLIEST_ACCEPTABLE_SHIP_DATE | — | ✅ |
| 37 | FulfillLineEndCreditMethodCode | END_CREDIT_METHOD_CODE | — | — |
| 38 | FulfillLineEndDate | END_DATE | — | — |
| 39 | FulfillLineEndReasonCode | END_REASON_CODE | — | — |
| 40 | FulfillLineEstimateFulfillmentCost | ESTIMATE_FULFILLMENT_COST | — | ✅ |
| 41 | FulfillLineEstimateMargin | ESTIMATE_MARGIN | — | ✅ |
| 42 | FulfillLineExemptionCertificateNumber | EXEMPTION_CERTIFICATE_NUMBER | — | ✅ |
| 43 | FulfillLineExtendedAmount | EXTENDED_AMOUNT | — | ✅ |
| 44 | FulfillLineExternalPriceBookName | EXTERNAL_PRICE_BOOK_NAME | — | — |
| 45 | FulfillLineFobPointCode | FOB_POINT_CODE | — | ✅ |
| 46 | FulfillLineFreightTermsCode | FREIGHT_TERMS_CODE | — | ✅ |
| 47 | FulfillLineFulfillInstanceId | FULFILL_INSTANCE_ID | — | ✅ |
| 48 | FulfillLineFulfillLineNumber | FULFILL_LINE_NUMBER | — | ✅ |
| 49 | FulfillLineFulfillOrgId | FULFILL_ORG_ID | — | ✅ |
| 50 | FulfillLineFulfillToleranceAbove | FULFILL_TOLERANCE_ABOVE | — | ✅ |
| 51 | FulfillLineFulfillToleranceBelow | FULFILL_TOLERANCE_BELOW | — | ✅ |
| 52 | FulfillLineFulfilledQty | FULFILLED_QTY | — | ✅ |
| 53 | FulfillLineFulfillmentDate | FULFILLMENT_DATE | — | ✅ |
| 54 | FulfillLineFulfillmentSplitRefId | FULFILLMENT_SPLIT_REF_ID | — | ✅ |
| 55 | FulfillLineGopReferenceId | GOP_REFERENCE_ID | — | ✅ |
| 56 | FulfillLineHeaderId | HEADER_ID | — | ✅ |
| 57 | FulfillLineId | FULFILL_LINE_ID | 🔑 | ✅ |
| 58 | FulfillLineInventoryInterfacedFlag | INVENTORY_INTERFACED_FLAG | — | ✅ |
| 59 | FulfillLineInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 60 | FulfillLineInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | ✅ |
| 61 | FulfillLineInventoryTransactionFlag | INVENTORY_TRANSACTION_FLAG | — | ✅ |
| 62 | FulfillLineInvoiceEnabledFlag | INVOICE_ENABLED_FLAG | — | ✅ |
| 63 | FulfillLineInvoiceInterfacedFlag | INVOICE_INTERFACED_FLAG | — | ✅ |
| 64 | FulfillLineInvoiceableItemFlag | INVOICEABLE_ITEM_FLAG | — | ✅ |
| 65 | FulfillLineInvoicingRuleId | INVOICING_RULE_ID | — | ✅ |
| 66 | FulfillLineItemSubTypeCode | ITEM_SUB_TYPE_CODE | — | ✅ |
| 67 | FulfillLineItemTypeCode | ITEM_TYPE_CODE | — | ✅ |
| 68 | FulfillLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 69 | FulfillLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 70 | FulfillLineLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 71 | FulfillLineLatestAcceptableArrivalDate | LATEST_ACCEPTABLE_ARRIVAL_DATE | — | ✅ |
| 72 | FulfillLineLatestAcceptableShipDate | LATEST_ACCEPTABLE_SHIP_DATE | — | ✅ |
| 73 | FulfillLineLineId | LINE_ID | — | ✅ |
| 74 | FulfillLineLineTypeCode | LINE_TYPE_CODE | — | ✅ |
| 75 | FulfillLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 76 | FulfillLineOnHold | ON_HOLD | — | ✅ |
| 77 | FulfillLineOneTimeConfigFlag | ONE_TIME_CONFIG_FLAG | — | — |
| 78 | FulfillLineOpenFlag | OPEN_FLAG | — | ✅ |
| 79 | FulfillLineOrderedQty | ORDERED_QTY | — | ✅ |
| 80 | FulfillLineOrderedUom | ORDERED_UOM | — | ✅ |
| 81 | FulfillLineOrgId | ORG_ID | — | ✅ |
| 82 | FulfillLineOrigSysDocumentLineRef | ORIG_SYS_DOCUMENT_LINE_REF | — | ✅ |
| 83 | FulfillLineOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | ✅ |
| 84 | FulfillLineOriginalInventoryItemId | ORIGINAL_INVENTORY_ITEM_ID | — | ✅ |
| 85 | FulfillLineOverrideScheduleDateFlag | OVERRIDE_SCHEDULE_DATE_FLAG | — | ✅ |
| 86 | FulfillLineOwnerId | OWNER_ID | — | ✅ |
| 87 | FulfillLinePackingInstructions | PACKING_INSTRUCTIONS | — | ✅ |
| 88 | FulfillLineParentConfigInventoryItemId | CONFIG_INVENTORY_ITEM_ID | — | — |
| 89 | FulfillLineParentConfigItemReference | CONFIG_ITEM_REFERENCE | — | — |
| 90 | FulfillLineParentFulfillLineId | PARENT_FULFILL_LINE_ID | — | ✅ |
| 91 | FulfillLineParentFulfillLineIdPk | FULFILL_LINE_ID | — | — |
| 92 | FulfillLineParentFulfillLineNumber | FULFILL_LINE_NUMBER | — | — |
| 93 | FulfillLineParentFulfillOrgId | FULFILL_ORG_ID | — | — |
| 94 | FulfillLineParentInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 95 | FulfillLineParentStatusCode | STATUS_CODE | — | — |
| 96 | FulfillLinePartialShipAllowedFlag | PARTIAL_SHIP_ALLOWED_FLAG | — | ✅ |
| 97 | FulfillLinePaymentTermId | PAYMENT_TERM_ID | — | ✅ |
| 98 | FulfillLinePriceUsingSecUomFlag | PRICE_USING_SEC_UOM_FLAG | — | ✅ |
| 99 | FulfillLinePrjRecIndicator | PRJ_REC_INDICATOR | — | — |
| 100 | FulfillLinePromiseArrivalDate | PROMISE_ARRIVAL_DATE | — | ✅ |
| 101 | FulfillLinePromiseShipDate | PROMISE_SHIP_DATE | — | ✅ |
| 102 | FulfillLineReferenceFlineId | REFERENCE_FLINE_ID | — | ✅ |
| 103 | FulfillLineRemnantFlag | REMNANT_FLAG | — | ✅ |
| 104 | FulfillLineRequestArrivalDate | REQUEST_ARRIVAL_DATE | — | ✅ |
| 105 | FulfillLineRequestCancelDate | REQUEST_CANCEL_DATE | — | ✅ |
| 106 | FulfillLineRequestShipDate | REQUEST_SHIP_DATE | — | ✅ |
| 107 | FulfillLineRequestType | REQUEST_TYPE | — | ✅ |
| 108 | FulfillLineReservableFlag | RESERVABLE_FLAG | — | ✅ |
| 109 | FulfillLineReservationId | RESERVATION_ID | — | ✅ |
| 110 | FulfillLineReservedQty | RESERVED_QTY | — | ✅ |
| 111 | FulfillLineReturnReasonCode | RETURN_REASON_CODE | — | ✅ |
| 112 | FulfillLineReturnableFlag | RETURNABLE_FLAG | — | ✅ |
| 113 | FulfillLineRmaDeliveredQty | RMA_DELIVERED_QTY | — | ✅ |
| 114 | FulfillLineRootParentConfigInventoryItemId | CONFIG_INVENTORY_ITEM_ID | — | — |
| 115 | FulfillLineRootParentConfigItemReference | CONFIG_ITEM_REFERENCE | — | — |
| 116 | FulfillLineRootParentFulfillLineId | ROOT_PARENT_FULFILL_LINE_ID | — | ✅ |
| 117 | FulfillLineRootParentFulfillLineIdPk | FULFILL_LINE_ID | — | — |
| 118 | FulfillLineRootParentFulfillLineNumber | FULFILL_LINE_NUMBER | — | — |
| 119 | FulfillLineRootParentFulfillOrgId | FULFILL_ORG_ID | — | — |
| 120 | FulfillLineRootParentInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 121 | FulfillLineRootParentInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 122 | FulfillLineRootParentStatusCode | STATUS_CODE | — | — |
| 123 | FulfillLineSalesProductTypeCode | SALES_PRODUCT_TYPE_CODE | — | ✅ |
| 124 | FulfillLineScheduleArrivalDate | SCHEDULE_ARRIVAL_DATE | — | ✅ |
| 125 | FulfillLineScheduleShipDate | SCHEDULE_SHIP_DATE | — | ✅ |
| 126 | FulfillLineSchedulingReasonCode | SCHEDULING_REASON_CODE | — | ✅ |
| 127 | FulfillLineSecondaryFulfilledQty | SECONDARY_FULFILLED_QTY | — | ✅ |
| 128 | FulfillLineSecondaryOrderedQty | SECONDARY_ORDERED_QTY | — | ✅ |
| 129 | FulfillLineSecondaryRmaDeliveredQty | SECONDARY_RMA_DELIVERED_QTY | — | ✅ |
| 130 | FulfillLineSecondaryShippedQty | SECONDARY_SHIPPED_QTY | — | ✅ |
| 131 | FulfillLineSecondaryUom | SECONDARY_UOM | — | ✅ |
| 132 | FulfillLineSellingProfitCenterBUId | SELLING_PROFIT_CENTER_BU_ID | — | — |
| 133 | FulfillLineServiceCancelDate | SERVICE_CANCEL_DATE | — | ✅ |
| 134 | FulfillLineServiceDuration | SERVICE_DURATION | — | ✅ |
| 135 | FulfillLineServiceDurationPeriodCode | SERVICE_DURATION_PERIOD_CODE | — | ✅ |
| 136 | FulfillLineShipClassOfService | SHIP_CLASS_OF_SERVICE | — | ✅ |
| 137 | FulfillLineShipModeOfTransport | SHIP_MODE_OF_TRANSPORT | — | ✅ |
| 138 | FulfillLineShipSetName | SHIP_SET_NAME | — | ✅ |
| 139 | FulfillLineShipToContactId | SHIP_TO_CONTACT_ID | — | ✅ |
| 140 | FulfillLineShipToCustomerId | SHIP_TO_CUSTOMER_ID | — | ✅ |
| 141 | FulfillLineShipToPartyContactId | SHIP_TO_PARTY_CONTACT_ID | — | ✅ |
| 142 | FulfillLineShipToPartyId | SHIP_TO_PARTY_ID | — | ✅ |
| 143 | FulfillLineShipToPartySiteId | SHIP_TO_PARTY_SITE_ID | — | ✅ |
| 144 | FulfillLineShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | ✅ |
| 145 | FulfillLineShipmentPriorityCode | SHIPMENT_PRIORITY_CODE | — | ✅ |
| 146 | FulfillLineShippableFlag | SHIPPABLE_FLAG | — | ✅ |
| 147 | FulfillLineShippedQty | SHIPPED_QTY | — | ✅ |
| 148 | FulfillLineShippingInstructions | SHIPPING_INSTRUCTIONS | — | ✅ |
| 149 | FulfillLineSourceLineId | SOURCE_LINE_ID | — | ✅ |
| 150 | FulfillLineSourceLineNumber | SOURCE_LINE_NUMBER | — | ✅ |
| 151 | FulfillLineSourceOrderId | SOURCE_ORDER_ID | — | ✅ |
| 152 | FulfillLineSourceOrderNumber | SOURCE_ORDER_NUMBER | — | ✅ |
| 153 | FulfillLineSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | ✅ |
| 154 | FulfillLineSourceOrgId | SOURCE_ORG_ID | — | ✅ |
| 155 | FulfillLineSourceRevisionNumber | SOURCE_REVISION_NUMBER | — | ✅ |
| 156 | FulfillLineSourceScheduleId | SOURCE_SCHEDULE_ID | — | ✅ |
| 157 | FulfillLineSourceScheduleNumber | SOURCE_SCHEDULE_NUMBER | — | ✅ |
| 158 | FulfillLineSplitFromFlineId | SPLIT_FROM_FLINE_ID | — | ✅ |
| 159 | FulfillLineStatusCode | STATUS_CODE | — | ✅ |
| 160 | FulfillLineStatusRulesetId | STATUS_RULESET_ID | — | ✅ |
| 161 | FulfillLineSubinventory | SUBINVENTORY | — | — |
| 162 | FulfillLineSubscriptionInterfacedFlag | SUBSCRIPTION_INTERFACED_FLAG | — | — |
| 163 | FulfillLineSubstituteAllowedFlag | SUBSTITUTE_ALLOWED_FLAG | — | ✅ |
| 164 | FulfillLineSubstituteReasonCode | SUBSTITUTE_REASON_CODE | — | ✅ |
| 165 | FulfillLineSupplierId | SUPPLIER_ID | — | ✅ |
| 166 | FulfillLineSupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 167 | FulfillLineTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | ✅ |
| 168 | FulfillLineTaxExemptFlag | TAX_EXEMPT_FLAG | — | ✅ |
| 169 | FulfillLineTaxExemptionReasonCode | TAX_EXEMPTION_REASON_CODE | — | ✅ |
| 170 | FulfillLineUnitListPrice | UNIT_LIST_PRICE | — | ✅ |
| 171 | FulfillLineUnitSellingPrice | UNIT_SELLING_PRICE | — | ✅ |
| 172 | FulfillLineUnreferencedReturnFlag | UNREFERENCED_RETURN_FLAG | — | ✅ |

### [[doo_headers_all|DOO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HeaderAgreementHeaderId | AGREEMENT_HEADER_ID | — | — |
| 2 | HeaderAgreementVersionNumber | AGREEMENT_VERSION_NUMBER | — | — |
| 3 | HeaderCancelReasonCode | CANCEL_REASON_CODE | — | ✅ |
| 4 | HeaderCanceledFlag | CANCELED_FLAG | — | — |
| 5 | HeaderChangeVersionNumber | CHANGE_VERSION_NUMBER | — | — |
| 6 | HeaderConversionDate | CONVERSION_DATE | — | — |
| 7 | HeaderConversionRate | CONVERSION_RATE | — | — |
| 8 | HeaderConversionTypeCode | CONVERSION_TYPE_CODE | — | — |
| 9 | HeaderCreatedBy | CREATED_BY | — | — |
| 10 | HeaderCreationDate | CREATION_DATE | — | — |
| 11 | HeaderCustomerPoNumber | CUSTOMER_PO_NUMBER | — | — |
| 12 | HeaderHeaderId | HEADER_ID | — | — |
| 13 | HeaderIsEditable | IS_EDITABLE | — | — |
| 14 | HeaderLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 15 | HeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | HeaderLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | HeaderLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 18 | HeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | HeaderOnHold | ON_HOLD | — | — |
| 20 | HeaderOpenFlag | OPEN_FLAG | — | — |
| 21 | HeaderOrderNumber | ORDER_NUMBER | — | — |
| 22 | HeaderOrderTypeCode | ORDER_TYPE_CODE | — | — |
| 23 | HeaderOrderedDate | ORDERED_DATE | — | — |
| 24 | HeaderOrgId | ORG_ID | — | — |
| 25 | HeaderOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | — |
| 26 | HeaderOwnerId | OWNER_ID | — | — |
| 27 | HeaderPartialShipAllowedFlag | PARTIAL_SHIP_ALLOWED_FLAG | — | — |
| 28 | HeaderPaymentTermId | PAYMENT_TERM_ID | — | — |
| 29 | HeaderPricingDate | PRICING_DATE | — | — |
| 30 | HeaderRequestShipDate | REQUEST_SHIP_DATE | — | ✅ |
| 31 | HeaderSalesChannelCode | SALES_CHANNEL_CODE | — | — |
| 32 | HeaderSalespersonId | SALESPERSON_ID | — | — |
| 33 | HeaderSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 34 | HeaderSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 35 | HeaderSoldToPartyContactId | SOLD_TO_PARTY_CONTACT_ID | — | — |
| 36 | HeaderSoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 37 | HeaderSourceDocumentTypeCode | SOURCE_DOCUMENT_TYPE_CODE | — | — |
| 38 | HeaderSourceOrderId | SOURCE_ORDER_ID | — | — |
| 39 | HeaderSourceOrderNumber | SOURCE_ORDER_NUMBER | — | — |
| 40 | HeaderSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | — |
| 41 | HeaderSourceOrgId | SOURCE_ORG_ID | — | — |
| 42 | HeaderStatusCode | STATUS_CODE | — | — |
| 43 | HeaderSubmittedBy | SUBMITTED_BY | — | — |
| 44 | HeaderSubmittedDate | SUBMITTED_DATE | — | — |
| 45 | HeaderSubmittedFlag | SUBMITTED_FLAG | — | — |
| 46 | HeaderTransactionalCurrencyCode | TRANSACTIONAL_CURRENCY_CODE | — | — |

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
| 24 | LineOnHold | ON_HOLD | — | — |
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

### [[doo_manual_price_adjustments|DOO_MANUAL_PRICE_ADJUSTMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ManualPriceAdjustmentAdjustmentAmount | ADJUSTMENT_AMOUNT | — | ✅ |
| 2 | ManualPriceAdjustmentAdjustmentElementBasis | ADJUSTMENT_ELEMENT_BASIS | — | ✅ |
| 3 | ManualPriceAdjustmentAdjustmentTypeCode | ADJUSTMENT_TYPE_CODE | — | ✅ |
| 4 | ManualPriceAdjustmentChargeDefinitionCode | CHARGE_DEFINITION_CODE | — | ✅ |
| 5 | ManualPriceAdjustmentChargeRollupFlag | CHARGE_ROLLUP_FLAG | — | ✅ |
| 6 | ManualPriceAdjustmentComments | COMMENTS | — | ✅ |
| 7 | ManualPriceAdjustmentCreatedBy | CREATED_BY | — | ✅ |
| 8 | ManualPriceAdjustmentCreationDate | CREATION_DATE | — | ✅ |
| 9 | ManualPriceAdjustmentDeltaType | DELTA_TYPE | — | ✅ |
| 10 | ManualPriceAdjustmentEffectivityTypeCode | EFFECTIVITY_TYPE_CODE | — | — |
| 11 | ManualPriceAdjustmentId | MANUAL_PRICE_ADJUSTMENT_ID | 🔑 | ✅ |
| 12 | ManualPriceAdjustmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | ManualPriceAdjustmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | ManualPriceAdjustmentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | ManualPriceAdjustmentModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 16 | ManualPriceAdjustmentNumberOfPeriods | NUMBER_OF_PERIODS | — | — |
| 17 | ManualPriceAdjustmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | ManualPriceAdjustmentParentEntityCode | PARENT_ENTITY_CODE | — | ✅ |
| 19 | ManualPriceAdjustmentParentEntityId | PARENT_ENTITY_ID | — | ✅ |
| 20 | ManualPriceAdjustmentPeriodFrom | PERIOD_FROM | — | — |
| 21 | ManualPriceAdjustmentPeriodUntil | PERIOD_UNTIL | — | — |
| 22 | ManualPriceAdjustmentPricePeriodicityCode | PRICE_PERIODICITY_CODE | — | ✅ |
| 23 | ManualPriceAdjustmentReasonCode | REASON_CODE | — | ✅ |
| 24 | ManualPriceAdjustmentReferenceMpaId | REFERENCE_MPA_ID | — | ✅ |
| 25 | ManualPriceAdjustmentSequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 26 | ManualPriceAdjustmentSourceManualPriceAdjId | SOURCE_MANUAL_PRICE_ADJ_ID | — | ✅ |
| 27 | ManualPriceAdjustmentValidationStatusCode | VALIDATION_STATUS_CODE | — | ✅ |

### [[doo_order_terms|DOO_ORDER_TERMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrderTermOrderTermId | ORDER_TERM_ID | — | — |
| 2 | OrderTermTermApplicationMethod | TERM_APPLICATION_METHOD | — | — |
| 3 | OrderTermTermApplicationValuePct | TERM_APPLICATION_VALUE_PCT | — | — |
| 4 | OrderTermTermDuration | TERM_DURATION | — | — |
| 5 | OrderTermTermPeriod | TERM_PERIOD | — | — |
| 6 | OrderTermTermStartDate | TERM_START_DATE | — | — |

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
| 16 | ProjectPjcExpenditureAllocationId | PJC_FUNDING_ALLOCATION_ID | — | — |
| 17 | ProjectPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 18 | ProjectPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | — |
| 19 | ProjectPjcOrganizationId | PJC_ORGANIZATION_ID | — | — |
| 20 | ProjectPjcProjectId | PJC_PROJECT_ID | — | — |
| 21 | ProjectPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 22 | ProjectPjcTaskId | PJC_TASK_ID | — | — |
| 23 | ProjectPjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |

### [[dos_supply_buy_order_dtls|DOS_SUPPLY_BUY_ORDER_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DosSupplyBuyOrderDtlsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | DosSupplyBuyOrderDtlsPurchaseOrderHeaderId | PURCHASE_ORDER_HEADER_ID | — | — |
| 3 | DosSupplyBuyOrderDtlsPurchaseOrderLineId | PURCHASE_ORDER_LINE_ID | — | — |
| 4 | DosSupplyBuyOrderDtlsPurchaseOrderLineNumber | PURCHASE_ORDER_LINE_NUMBER | — | — |
| 5 | DosSupplyBuyOrderDtlsPurchaseOrderNumber | PURCHASE_ORDER_NUMBER | — | — |
| 6 | DosSupplyBuyOrderDtlsPurchaseOrderScheduleNumber | PURCHASE_ORDER_SCHEDULE_NUMBER | — | — |
| 7 | DosSupplyBuyOrderDtlsSupplyBuyOrdDtlsId | SUPPLY_BUY_ORD_DTLS_ID | — | — |
| 8 | DosSupplyBuyOrderDtlsTrackingLineId | TRACKING_LINE_ID | — | — |

### [[dos_supply_make_order_dtls|DOS_SUPPLY_MAKE_ORDER_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DosSupplyMakeOrderDtlsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | DosSupplyMakeOrderDtlsSupplyMakeDetailsId | SUPPLY_MAKE_DETAILS_ID | — | — |
| 3 | DosSupplyMakeOrderDtlsTrackingLineId | TRACKING_LINE_ID | — | — |
| 4 | DosSupplyMakeOrderDtlsWorkOrderId | WORK_ORDER_ID | — | — |
| 5 | DosSupplyMakeOrderDtlsWorkOrderNumber | WORK_ORDER_NUMBER | — | — |
| 6 | DosSupplyMakeOrderDtlsWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | — |

### [[dos_supply_tracking_lines|DOS_SUPPLY_TRACKING_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DosSupplyTrackingLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | DosSupplyTrackingLineSupplyType | SUPPLY_TYPE | — | — |
| 3 | DosSupplyTrackingLineTrackingLineId | TRACKING_LINE_ID | — | — |

### [[egp_trading_partner_items|EGP_TRADING_PARTNER_ITEMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CoverageTradingPartnerItemEndDate | END_DATE | — | — |
| 2 | CoverageTradingPartnerItemStartDate | START_DATE | — | — |
| 3 | CoverageTradingPartnerItemTpItemDesc | TP_ITEM_DESC | — | — |
| 4 | CoverageTradingPartnerItemTpItemId | TP_ITEM_ID | — | — |
| 5 | CoverageTradingPartnerItemTpItemNumber | TP_ITEM_NUMBER | — | — |
| 6 | CoverageTradingPartnerItemTpType | TP_TYPE | — | — |
| 7 | CoveredTradingPartnerItemEndDate | END_DATE | — | — |
| 8 | CoveredTradingPartnerItemStartDate | START_DATE | — | — |
| 9 | CoveredTradingPartnerItemTpItemDesc | TP_ITEM_DESC | — | — |
| 10 | CoveredTradingPartnerItemTpItemId | TP_ITEM_ID | — | — |
| 11 | CoveredTradingPartnerItemTpItemNumber | TP_ITEM_NUMBER | — | — |
| 12 | CoveredTradingPartnerItemTpType | TP_TYPE | — | — |
| 13 | CustomerItemEndDate | END_DATE | — | — |
| 14 | CustomerItemProgramAppName | PROGRAM_APP_NAME | — | — |
| 15 | CustomerItemProgramName | PROGRAM_NAME | — | — |
| 16 | CustomerItemRequestId | REQUEST_ID | — | — |
| 17 | CustomerItemStartDate | START_DATE | — | — |
| 18 | CustomerItemTpItemDesc | TP_ITEM_DESC | — | — |
| 19 | CustomerItemTpItemId | TP_ITEM_ID | — | — |
| 20 | CustomerItemTpItemNumber | TP_ITEM_NUMBER | — | ✅ |
| 21 | CustomerItemTpType | TP_TYPE | — | — |
| 22 | CustomerItemTradingPartnerId | TRADING_PARTNER_ID | — | — |
| 23 | TradingPartnerItemEndDate | END_DATE | — | — |
| 24 | TradingPartnerItemStartDate | START_DATE | — | — |
| 25 | TradingPartnerItemTpItemDesc | TP_ITEM_DESC | — | — |
| 26 | TradingPartnerItemTpItemId | TP_ITEM_ID | — | — |
| 27 | TradingPartnerItemTpItemNumber | TP_ITEM_NUMBER | — | — |
| 28 | TradingPartnerItemTpType | TP_TYPE | — | — |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUBusinessUnitId | BU_ID | — | — |
| 2 | BUDefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | — |
| 3 | BUPrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgerCurrencyCode | CURRENCY_CODE | — | — |
| 2 | LedgerLedgerId | LEDGER_ID | — | — |
| 3 | LedgerObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

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
| 12 | BillToCustomerAccountCustomerClassCode1 | CUSTOMER_CLASS_CODE | — | — |
| 13 | BillToCustomerAccountCustomerType1 | CUSTOMER_TYPE | — | — |
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

### [[hz_cust_account_roles|HZ_CUST_ACCOUNT_ROLES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillToContactAccountCustAccountRoleId | CUST_ACCOUNT_ROLE_ID | — | — |
| 2 | BillToContactAccountRelationshipId | RELATIONSHIP_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
