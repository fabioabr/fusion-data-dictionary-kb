---
id: DOC-OTHER-PVO-HoldInstance
doc_type: system-doc
title: "HoldInstance — PVO Cross-Module"
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
  - HoldInstance
  - holdinstance
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HoldInstance

## 📌 Visão Geral

View Object para extração BICC de dados de Hold Instance. Acessa as tabelas: DOO_FULFILL_LINES_ALL, DOO_HEADERS_ALL, DOO_HOLD_INSTANCES (+3).

**Caminho:** `FscmTopModelAM.DooTopAM.HoldInstance`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 215 | 6 | 2 | 27 | 13% |

---

## 🔗 Tabelas Relacionadas

- [[doo_fulfill_lines_all|DOO_FULFILL_LINES_ALL]] — 110 atributos (1 PKs, 9 BICC)
- [[doo_headers_all|DOO_HEADERS_ALL]] — 3 atributos (2 BICC)
- [[doo_hold_instances|DOO_HOLD_INSTANCES]] — 27 atributos (1 PKs, 12 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 21 atributos
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 30 atributos (1 BICC)
- [[per_users|PER_USERS]] — 24 atributos (3 BICC)

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
| 26 | FulfillLineFulfillLineId | FULFILL_LINE_ID | 🔑 | ✅ |
| 27 | FulfillLineFulfillLineNumber | FULFILL_LINE_NUMBER | — | — |
| 28 | FulfillLineFulfillOrgId | FULFILL_ORG_ID | — | — |
| 29 | FulfillLineFulfillToleranceAbove | FULFILL_TOLERANCE_ABOVE | — | — |
| 30 | FulfillLineFulfillToleranceBelow | FULFILL_TOLERANCE_BELOW | — | — |
| 31 | FulfillLineFulfilledQty | FULFILLED_QTY | — | — |
| 32 | FulfillLineFulfillmentDate | FULFILLMENT_DATE | — | — |
| 33 | FulfillLineFulfillmentSplitRefId | FULFILLMENT_SPLIT_REF_ID | — | — |
| 34 | FulfillLineGopReferenceId | GOP_REFERENCE_ID | — | — |
| 35 | FulfillLineHeaderId | HEADER_ID | — | ✅ |
| 36 | FulfillLineInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 37 | FulfillLineInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 38 | FulfillLineInvoiceEnabledFlag | INVOICE_ENABLED_FLAG | — | — |
| 39 | FulfillLineInvoiceableItemFlag | INVOICEABLE_ITEM_FLAG | — | — |
| 40 | FulfillLineInvoicingRuleId | INVOICING_RULE_ID | — | — |
| 41 | FulfillLineItemTypeCode | ITEM_TYPE_CODE | — | — |
| 42 | FulfillLineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 43 | FulfillLineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 44 | FulfillLineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 45 | FulfillLineLatestAcceptableArrivalDate | LATEST_ACCEPTABLE_ARRIVAL_DATE | — | — |
| 46 | FulfillLineLatestAcceptableShipDate | LATEST_ACCEPTABLE_SHIP_DATE | — | — |
| 47 | FulfillLineLineId | LINE_ID | — | ✅ |
| 48 | FulfillLineLineTypeCode | LINE_TYPE_CODE | — | — |
| 49 | FulfillLineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 50 | FulfillLineOnHold | ON_HOLD | — | — |
| 51 | FulfillLineOpenFlag | OPEN_FLAG | — | ✅ |
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
| 77 | FulfillLineRootParentFulfillLineId | ROOT_PARENT_FULFILL_LINE_ID | — | ✅ |
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
| 94 | FulfillLineSourceLineNumber | SOURCE_LINE_NUMBER | — | ✅ |
| 95 | FulfillLineSourceOrderId | SOURCE_ORDER_ID | — | — |
| 96 | FulfillLineSourceOrderNumber | SOURCE_ORDER_NUMBER | — | ✅ |
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
| 1 | HeaderHeaderId | HEADER_ID | — | — |
| 2 | HeaderOrderNumber | ORDER_NUMBER | — | ✅ |
| 3 | HeaderSoldToPartyId | SOLD_TO_PARTY_ID | — | ✅ |

### [[doo_hold_instances|DOO_HOLD_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HoldInstanceActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | HoldInstanceApplyDate | APPLY_DATE | — | ✅ |
| 3 | HoldInstanceApplySystem | APPLY_SYSTEM | — | ✅ |
| 4 | HoldInstanceApplyUserId | APPLY_USER_ID | — | — |
| 5 | HoldInstanceCreatedBy | CREATED_BY | — | — |
| 6 | HoldInstanceCreationDate | CREATION_DATE | — | — |
| 7 | HoldInstanceDeletedFlag | DELETED_FLAG | — | — |
| 8 | HoldInstanceHoldCodeId | HOLD_CODE_ID | — | — |
| 9 | HoldInstanceHoldComments | HOLD_COMMENTS | — | ✅ |
| 10 | HoldInstanceHoldReleaseComments | HOLD_RELEASE_COMMENTS | — | ✅ |
| 11 | HoldInstanceHoldReleaseReasonCode | HOLD_RELEASE_REASON_CODE | — | ✅ |
| 12 | HoldInstanceHoldRunningTaskFlag | HOLD_RUNNING_TASK_FLAG | — | — |
| 13 | HoldInstanceId | HOLD_INSTANCE_ID | 🔑 | ✅ |
| 14 | HoldInstanceLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | HoldInstanceLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | HoldInstanceLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | HoldInstanceObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | HoldInstancePendingFlag | PENDING_FLAG | — | ✅ |
| 19 | HoldInstanceReleaseDate | RELEASE_DATE | — | ✅ |
| 20 | HoldInstanceReleaseUserId | RELEASE_USER_ID | — | — |
| 21 | HoldInstanceSourceLineId | SOURCE_LINE_ID | — | — |
| 22 | HoldInstanceSourceOrderId | SOURCE_ORDER_ID | — | — |
| 23 | HoldInstanceSourceOrderRevision | SOURCE_ORDER_REVISION | — | — |
| 24 | HoldInstanceSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | — |
| 25 | HoldInstanceSourceRequestId | SOURCE_REQUEST_ID | — | — |
| 26 | HoldInstanceTransactionEntityId1 | TRANSACTION_ENTITY_ID1 | — | ✅ |
| 27 | HoldInstanceTransactionEntityName1 | TRANSACTION_ENTITY_NAME1 | — | ✅ |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUBusinessUnitId | BU_ID | — | — |
| 2 | BUCreatedBy | CREATED_BY | — | — |
| 3 | BUCreationDate | CREATION_DATE | — | — |
| 4 | BUDateFrom | DATE_FROM | — | — |
| 5 | BUDateTo | DATE_TO | — | — |
| 6 | BUDefaultCurrencyCode | DEFAULT_CURRENCY_CODE | — | — |
| 7 | BUDefaultSetId | DEFAULT_SET_ID | — | — |
| 8 | BUEnabledForHrFlag | ENABLED_FOR_HR_FLAG | — | — |
| 9 | BUEnterpriseId | BUSINESS_GROUP_ID | — | — |
| 10 | BUFinancialsBusinessUnitId | FIN_BUSINESS_UNIT_ID | — | — |
| 11 | BULastUpdateDate | LAST_UPDATE_DATE | — | — |
| 12 | BULastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | BULastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | BULegalEntityId | LEGAL_ENTITY_ID | — | — |
| 15 | BULocationId | LOCATION_ID | — | — |
| 16 | BUManagerId | MANAGER_ID | — | — |
| 17 | BUName | BU_NAME | — | — |
| 18 | BUPrimaryLedgerId | PRIMARY_LEDGER_ID | — | — |
| 19 | BUProfitCenterFlag | PROFIT_CENTER_FLAG | — | — |
| 20 | BUShortCode | SHORT_CODE | — | — |
| 21 | BUStatus | STATUS | — | — |

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
| 16 | BillToCustomerAccountHoldBillFlag | HOLD_BILL_FLAG | — | — |
| 17 | BillToCustomerAccountLastBatchId | LAST_BATCH_ID | — | — |
| 18 | BillToCustomerAccountLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | BillToCustomerAccountLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | BillToCustomerAccountLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 21 | BillToCustomerAccountNpaNumber | NPA_NUMBER | — | — |
| 22 | BillToCustomerAccountOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 23 | BillToCustomerAccountPartyId | PARTY_ID | — | — |
| 24 | BillToCustomerAccountSellingPartyId | SELLING_PARTY_ID | — | — |
| 25 | BillToCustomerAccountSourceCode | SOURCE_CODE | — | — |
| 26 | BillToCustomerAccountStatus | STATUS | — | — |
| 27 | BillToCustomerAccountStatusUpdateDate | STATUS_UPDATE_DATE | — | — |
| 28 | BillToCustomerAccountTaxCode | TAX_CODE | — | — |
| 29 | BillToCustomerAccountTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | — |
| 30 | BillToCustomerAccountTaxRoundingRule | TAX_ROUNDING_RULE | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplyUserActiveFlag | ACTIVE_FLAG | — | — |
| 2 | ApplyUserBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | ApplyUserEndDate | END_DATE | — | ✅ |
| 4 | ApplyUserHrTerminated | HR_TERMINATED | — | — |
| 5 | ApplyUserObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | ApplyUserPartyId | PARTY_ID | — | — |
| 7 | ApplyUserPersonId | PERSON_ID | — | — |
| 8 | ApplyUserStartDate | START_DATE | — | — |
| 9 | ApplyUserSuspended | SUSPENDED | — | — |
| 10 | ApplyUserUserGuid | USER_GUID | — | — |
| 11 | ApplyUserUserId | USER_ID | — | — |
| 12 | ApplyUserUsername | USERNAME | — | ✅ |
| 13 | ReleaseUserActiveFlag | ACTIVE_FLAG | — | — |
| 14 | ReleaseUserBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 15 | ReleaseUserEndDate | END_DATE | — | — |
| 16 | ReleaseUserHrTerminated | HR_TERMINATED | — | — |
| 17 | ReleaseUserObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | ReleaseUserPartyId | PARTY_ID | — | — |
| 19 | ReleaseUserPersonId | PERSON_ID | — | — |
| 20 | ReleaseUserStartDate | START_DATE | — | — |
| 21 | ReleaseUserSuspended | SUSPENDED | — | — |
| 22 | ReleaseUserUserGuid | USER_GUID | — | — |
| 23 | ReleaseUserUserId | USER_ID | — | — |
| 24 | ReleaseUserUsername | USERNAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
