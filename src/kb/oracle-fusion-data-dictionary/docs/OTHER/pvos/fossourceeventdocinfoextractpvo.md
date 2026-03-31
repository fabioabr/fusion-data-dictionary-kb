---
id: DOC-OTHER-PVO-FosSourceEventDocInfoExtractPVO
doc_type: system-doc
title: "FosSourceEventDocInfoExtractPVO — PVO Cross-Module"
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
  - FosSourceEventDocInfoExtractPVO
  - fossourceeventdocinfoextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosSourceEventDocInfoExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos Source Event Doc Info Extract. Acessa as tabelas: FOS_SOURCE_EVENT_DOC_INFO.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosSourceEventDocInfoExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 74 | 1 | 1 | 74 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fos_source_event_doc_info|FOS_SOURCE_EVENT_DOC_INFO]] — 74 atributos (1 PKs, 74 BICC)

---

## ⚙️ Atributos

### [[fos_source_event_doc_info|FOS_SOURCE_EVENT_DOC_INFO]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SourceEventDocInfoPEOAgreementPtrId | AGREEMENT_PTR_ID | — | ✅ |
| 2 | SourceEventDocInfoPEOAutoCreatedConfigFlag | AUTO_CREATED_CONFIG_FLAG | — | ✅ |
| 3 | SourceEventDocInfoPEOBaseInventoryItemId | BASE_INVENTORY_ITEM_ID | — | ✅ |
| 4 | SourceEventDocInfoPEOBillToCustomerAccntNumber | BILL_TO_CUSTOMER_ACCNT_NUMBER | — | ✅ |
| 5 | SourceEventDocInfoPEOBillToLocationCode | BILL_TO_LOCATION_CODE | — | ✅ |
| 6 | SourceEventDocInfoPEOCategoryCode | CATEGORY_CODE | — | ✅ |
| 7 | SourceEventDocInfoPEOConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 8 | SourceEventDocInfoPEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | SourceEventDocInfoPEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | SourceEventDocInfoPEOCustomerDeliverToLocation | CUSTOMER_DELIVER_TO_LOCATION | — | ✅ |
| 11 | SourceEventDocInfoPEOCustomerShipToLocation | CUSTOMER_SHIP_TO_LOCATION | — | ✅ |
| 12 | SourceEventDocInfoPEODeliverToPartyNumber | DELIVER_TO_PARTY_NUMBER | — | ✅ |
| 13 | SourceEventDocInfoPEODeliverToPartySiteNumber | DELIVER_TO_PARTY_SITE_NUMBER | — | ✅ |
| 14 | SourceEventDocInfoPEODestinationType | DESTINATION_TYPE | — | ✅ |
| 15 | SourceEventDocInfoPEODocInfoLogId | DOC_INFO_LOG_ID | 🔑 | ✅ |
| 16 | SourceEventDocInfoPEODocumentDate | DOCUMENT_DATE | — | ✅ |
| 17 | SourceEventDocInfoPEODocumentHeaderId | DOCUMENT_HEADER_ID | — | ✅ |
| 18 | SourceEventDocInfoPEODocumentLineDetailId | DOCUMENT_LINE_DETAIL_ID | — | ✅ |
| 19 | SourceEventDocInfoPEODocumentLineDetailNumber | DOCUMENT_LINE_DETAIL_NUMBER | — | ✅ |
| 20 | SourceEventDocInfoPEODocumentLineId | DOCUMENT_LINE_ID | — | ✅ |
| 21 | SourceEventDocInfoPEODocumentLineNumber | DOCUMENT_LINE_NUMBER | — | ✅ |
| 22 | SourceEventDocInfoPEODocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 23 | SourceEventDocInfoPEODocumentRevision | DOCUMENT_REVISION | — | ✅ |
| 24 | SourceEventDocInfoPEODocumentSourceSystemCode | DOCUMENT_SOURCE_SYSTEM_CODE | — | ✅ |
| 25 | SourceEventDocInfoPEODocumentType | DOCUMENT_TYPE | — | ✅ |
| 26 | SourceEventDocInfoPEODropshipFlag | DROPSHIP_FLAG | — | ✅ |
| 27 | SourceEventDocInfoPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 28 | SourceEventDocInfoPEOFromBu | FROM_BU | — | ✅ |
| 29 | SourceEventDocInfoPEOFromLe | FROM_LE | — | ✅ |
| 30 | SourceEventDocInfoPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 31 | SourceEventDocInfoPEOItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 32 | SourceEventDocInfoPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 33 | SourceEventDocInfoPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 34 | SourceEventDocInfoPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 35 | SourceEventDocInfoPEOLineType | LINE_TYPE | — | ✅ |
| 36 | SourceEventDocInfoPEOLinkToDocumentId | LINK_TO_DOCUMENT_ID | — | ✅ |
| 37 | SourceEventDocInfoPEOLinkToDocumentSystemCode | LINK_TO_DOCUMENT_SYSTEM_CODE | — | ✅ |
| 38 | SourceEventDocInfoPEOLinkToDocumentType | LINK_TO_DOCUMENT_TYPE | — | ✅ |
| 39 | SourceEventDocInfoPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 40 | SourceEventDocInfoPEOOrderTypeCode | ORDER_TYPE_CODE | — | ✅ |
| 41 | SourceEventDocInfoPEOOrderedAmount | ORDERED_AMOUNT | — | ✅ |
| 42 | SourceEventDocInfoPEOOrderedCurrencyCode | ORDERED_CURRENCY_CODE | — | ✅ |
| 43 | SourceEventDocInfoPEOOrderedQuantity | ORDERED_QUANTITY | — | ✅ |
| 44 | SourceEventDocInfoPEOOrderedUom | ORDERED_UOM | — | ✅ |
| 45 | SourceEventDocInfoPEOPriceCurrencyCode | PRICE_CURRENCY_CODE | — | ✅ |
| 46 | SourceEventDocInfoPEOPrjRefEnabledFlag | PRJ_REF_ENABLED_FLAG | — | ✅ |
| 47 | SourceEventDocInfoPEOProcurementBuId | PROCUREMENT_BU_ID | — | ✅ |
| 48 | SourceEventDocInfoPEOPurchasingCategory | PURCHASING_CATEGORY | — | ✅ |
| 49 | SourceEventDocInfoPEOReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | ✅ |
| 50 | SourceEventDocInfoPEORefDocumentId | REF_DOCUMENT_ID | — | ✅ |
| 51 | SourceEventDocInfoPEORefDocumentSystemCode | REF_DOCUMENT_SYSTEM_CODE | — | ✅ |
| 52 | SourceEventDocInfoPEORefDocumentType | REF_DOCUMENT_TYPE | — | ✅ |
| 53 | SourceEventDocInfoPEORefSalesOrderLineNumber | REF_SALES_ORDER_LINE_NUMBER | — | ✅ |
| 54 | SourceEventDocInfoPEORefSalesOrderNumber | REF_SALES_ORDER_NUMBER | — | ✅ |
| 55 | SourceEventDocInfoPEORefSalesOrderSystemCode | REF_SALES_ORDER_SYSTEM_CODE | — | ✅ |
| 56 | SourceEventDocInfoPEOReferencedRmaFlag | REFERENCED_RMA_FLAG | — | ✅ |
| 57 | SourceEventDocInfoPEOShipFromOrganizationCode | SHIP_FROM_ORGANIZATION_CODE | — | ✅ |
| 58 | SourceEventDocInfoPEOShipToCustomerAccntNumber | SHIP_TO_CUSTOMER_ACCNT_NUMBER | — | ✅ |
| 59 | SourceEventDocInfoPEOShipToCustomerNumber | SHIP_TO_CUSTOMER_NUMBER | — | ✅ |
| 60 | SourceEventDocInfoPEOShipToLocationCode | SHIP_TO_LOCATION_CODE | — | ✅ |
| 61 | SourceEventDocInfoPEOShipToOrganizationCode | SHIP_TO_ORGANIZATION_CODE | — | ✅ |
| 62 | SourceEventDocInfoPEOShipToPartyNumber | SHIP_TO_PARTY_NUMBER | — | ✅ |
| 63 | SourceEventDocInfoPEOShipToPartySiteNumber | SHIP_TO_PARTY_SITE_NUMBER | — | ✅ |
| 64 | SourceEventDocInfoPEOSoldToCustomerAccntNumber | SOLD_TO_CUSTOMER_ACCNT_NUMBER | — | ✅ |
| 65 | SourceEventDocInfoPEOSoldToCustomerNumber | SOLD_TO_CUSTOMER_NUMBER | — | ✅ |
| 66 | SourceEventDocInfoPEOSoldToPartyNumber | SOLD_TO_PARTY_NUMBER | — | ✅ |
| 67 | SourceEventDocInfoPEOSourceDocumentId | SOURCE_DOCUMENT_ID | — | ✅ |
| 68 | SourceEventDocInfoPEOStatus | STATUS | — | ✅ |
| 69 | SourceEventDocInfoPEOSupplierNumber | SUPPLIER_NUMBER | — | ✅ |
| 70 | SourceEventDocInfoPEOSupplierSiteCode | SUPPLIER_SITE_CODE | — | ✅ |
| 71 | SourceEventDocInfoPEOToBu | TO_BU | — | ✅ |
| 72 | SourceEventDocInfoPEOToLe | TO_LE | — | ✅ |
| 73 | SourceEventDocInfoPEOTransferOrderFlag | TRANSFER_ORDER_FLAG | — | ✅ |
| 74 | SourceEventDocInfoPEOUnitPrice | UNIT_PRICE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
