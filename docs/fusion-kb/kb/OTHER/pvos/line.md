---
id: DOC-OTHER-PVO-Line
doc_type: system-doc
title: "Line — PVO Cross-Module"
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
  - Line
  - line
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Line

## 📌 Visão Geral

View Object para extração BICC de dados de Line. Acessa as tabelas: DOO_HEADERS_ALL, DOO_LINES_ALL, FUN_ALL_BUSINESS_UNITS_V.

**Caminho:** `FscmTopModelAM.DooTopAM.Line`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 95 | 3 | 1 | 42 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[doo_headers_all|DOO_HEADERS_ALL]] — 45 atributos (21 BICC)
- [[doo_lines_all|DOO_LINES_ALL]] — 49 atributos (1 PKs, 21 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 1 atributos

---

## ⚙️ Atributos

### [[doo_headers_all|DOO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HeaderAgreementHeaderId | AGREEMENT_HEADER_ID | — | — |
| 2 | HeaderAgreementVersionNumber | AGREEMENT_VERSION_NUMBER | — | — |
| 3 | HeaderCancelReasonCode | CANCEL_REASON_CODE | — | ✅ |
| 4 | HeaderCanceledFlag | CANCELED_FLAG | — | — |
| 5 | HeaderChangeVersionNumber | CHANGE_VERSION_NUMBER | — | ✅ |
| 6 | HeaderConversionDate | CONVERSION_DATE | — | — |
| 7 | HeaderConversionRate | CONVERSION_RATE | — | — |
| 8 | HeaderConversionTypeCode | CONVERSION_TYPE_CODE | — | — |
| 9 | HeaderCreatedBy | CREATED_BY | — | ✅ |
| 10 | HeaderCreationDate | CREATION_DATE | — | ✅ |
| 11 | HeaderCustomerPoNumber | CUSTOMER_PO_NUMBER | — | ✅ |
| 12 | HeaderHeaderId | HEADER_ID | — | ✅ |
| 13 | HeaderIsEditable | IS_EDITABLE | — | — |
| 14 | HeaderLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | HeaderLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | HeaderLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | HeaderLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 18 | HeaderObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | HeaderOnHold | ON_HOLD | — | ✅ |
| 20 | HeaderOpenFlag | OPEN_FLAG | — | ✅ |
| 21 | HeaderOrderNumber | ORDER_NUMBER | — | ✅ |
| 22 | HeaderOrderTypeCode | ORDER_TYPE_CODE | — | ✅ |
| 23 | HeaderOrderedDate | ORDERED_DATE | — | ✅ |
| 24 | HeaderOrgId | ORG_ID | — | — |
| 25 | HeaderOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | ✅ |
| 26 | HeaderOwnerId | OWNER_ID | — | — |
| 27 | HeaderPartialShipAllowedFlag | PARTIAL_SHIP_ALLOWED_FLAG | — | — |
| 28 | HeaderPricingDate | PRICING_DATE | — | — |
| 29 | HeaderRequestShipDate | REQUEST_SHIP_DATE | — | ✅ |
| 30 | HeaderSalesChannelCode | SALES_CHANNEL_CODE | — | ✅ |
| 31 | HeaderSalespersonId | SALESPERSON_ID | — | — |
| 32 | HeaderSoldToContactId | SOLD_TO_CONTACT_ID | — | — |
| 33 | HeaderSoldToCustomerId | SOLD_TO_CUSTOMER_ID | — | — |
| 34 | HeaderSoldToPartyContactId | SOLD_TO_PARTY_CONTACT_ID | — | — |
| 35 | HeaderSoldToPartyId | SOLD_TO_PARTY_ID | — | — |
| 36 | HeaderSourceDocumentTypeCode | SOURCE_DOCUMENT_TYPE_CODE | — | ✅ |
| 37 | HeaderSourceOrderId | SOURCE_ORDER_ID | — | — |
| 38 | HeaderSourceOrderNumber | SOURCE_ORDER_NUMBER | — | — |
| 39 | HeaderSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | ✅ |
| 40 | HeaderSourceOrgId | SOURCE_ORG_ID | — | — |
| 41 | HeaderStatusCode | STATUS_CODE | — | — |
| 42 | HeaderSubmittedBy | SUBMITTED_BY | — | ✅ |
| 43 | HeaderSubmittedDate | SUBMITTED_DATE | — | ✅ |
| 44 | HeaderSubmittedFlag | SUBMITTED_FLAG | — | ✅ |
| 45 | HeaderTransactionalCurrencyCode | TRANSACTIONAL_CURRENCY_CODE | — | — |

### [[doo_lines_all|DOO_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LineActualShipDate | ACTUAL_SHIP_DATE | — | — |
| 2 | LineCanceledFlag | CANCELED_FLAG | — | ✅ |
| 3 | LineCanceledQty | CANCELED_QTY | — | ✅ |
| 4 | LineCategoryCode | CATEGORY_CODE | — | ✅ |
| 5 | LineCompSeqPath | COMP_SEQ_PATH | — | — |
| 6 | LineCreatedBy | CREATED_BY | — | — |
| 7 | LineCreationDate | CREATION_DATE | — | — |
| 8 | LineDeltaType | DELTA_TYPE | — | — |
| 9 | LineDisplayLineNumber | DISPLAY_LINE_NUMBER | — | ✅ |
| 10 | LineExtendedAmount | EXTENDED_AMOUNT | — | — |
| 11 | LineFulfilledQty | FULFILLED_QTY | — | ✅ |
| 12 | LineFulfillmentDate | FULFILLMENT_DATE | — | — |
| 13 | LineHeaderId | HEADER_ID | — | ✅ |
| 14 | LineId | LINE_ID | 🔑 | ✅ |
| 15 | LineInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 16 | LineInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 17 | LineItemTypeCode | ITEM_TYPE_CODE | — | — |
| 18 | LineLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | LineLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | LineLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 21 | LineLineNumber | LINE_NUMBER | — | ✅ |
| 22 | LineLineTypeCode | LINE_TYPE_CODE | — | — |
| 23 | LineObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | LineOnHold | ON_HOLD | — | ✅ |
| 25 | LineOpenFlag | OPEN_FLAG | — | ✅ |
| 26 | LineOrderedQty | ORDERED_QTY | — | ✅ |
| 27 | LineOrderedUom | ORDERED_UOM | — | ✅ |
| 28 | LineOrgId | ORG_ID | — | — |
| 29 | LineOrigSysDocumentLineRef | ORIG_SYS_DOCUMENT_LINE_REF | — | — |
| 30 | LineOrigSysDocumentRef | ORIG_SYS_DOCUMENT_REF | — | — |
| 31 | LineOwnerId | OWNER_ID | — | — |
| 32 | LineParentLineId | PARENT_LINE_ID | — | — |
| 33 | LineReferenceLineId | REFERENCE_LINE_ID | — | — |
| 34 | LineRmaDeliveredQty | RMA_DELIVERED_QTY | — | ✅ |
| 35 | LineRootParentLineId | ROOT_PARENT_LINE_ID | — | — |
| 36 | LineScheduleShipDate | SCHEDULE_SHIP_DATE | — | ✅ |
| 37 | LineShippedQty | SHIPPED_QTY | — | ✅ |
| 38 | LineSourceLineId | SOURCE_LINE_ID | — | — |
| 39 | LineSourceLineNumber | SOURCE_LINE_NUMBER | — | ✅ |
| 40 | LineSourceOrderId | SOURCE_ORDER_ID | — | — |
| 41 | LineSourceOrderNumber | SOURCE_ORDER_NUMBER | — | ✅ |
| 42 | LineSourceOrderSystem | SOURCE_ORDER_SYSTEM | — | — |
| 43 | LineSourceOrgId | SOURCE_ORG_ID | — | — |
| 44 | LineSourceScheduleId | SOURCE_SCHEDULE_ID | — | — |
| 45 | LineSourceScheduleNumber | SOURCE_SCHEDULE_NUMBER | — | ✅ |
| 46 | LineStatusCode | STATUS_CODE | — | — |
| 47 | LineTransformFromLineId | TRANSFORM_FROM_LINE_ID | — | — |
| 48 | LineUnitListPrice | UNIT_LIST_PRICE | — | ✅ |
| 49 | LineUnitSellingPrice | UNIT_SELLING_PRICE | — | ✅ |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUBusinessUnitId | BU_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
