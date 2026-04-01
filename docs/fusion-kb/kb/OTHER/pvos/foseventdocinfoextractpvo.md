---
id: DOC-OTHER-PVO-FosEventDocInfoExtractPVO
doc_type: system-doc
title: "FosEventDocInfoExtractPVO — PVO Cross-Module"
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
  - FosEventDocInfoExtractPVO
  - foseventdocinfoextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosEventDocInfoExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos Event Doc Info Extract. Acessa as tabelas: FOS_EVENT_DOC_INFO.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosEventDocInfoExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 81 | 1 | 1 | 81 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fos_event_doc_info|FOS_EVENT_DOC_INFO]] — 81 atributos (1 PKs, 81 BICC)

---

## ⚙️ Atributos

### [[fos_event_doc_info|FOS_EVENT_DOC_INFO]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FosEventDocInfoPEOAgreementPtrId | AGREEMENT_PTR_ID | — | ✅ |
| 2 | FosEventDocInfoPEOAgreementType | AGREEMENT_TYPE | — | ✅ |
| 3 | FosEventDocInfoPEOAutoCreatedConfigFlag | AUTO_CREATED_CONFIG_FLAG | — | ✅ |
| 4 | FosEventDocInfoPEOBaseInventoryItemId | BASE_INVENTORY_ITEM_ID | — | ✅ |
| 5 | FosEventDocInfoPEOBillToCustomerAccntNumber | BILL_TO_CUSTOMER_ACCNT_NUMBER | — | ✅ |
| 6 | FosEventDocInfoPEOBillToLocationCode | BILL_TO_LOCATION_CODE | — | ✅ |
| 7 | FosEventDocInfoPEOCategoryCode | CATEGORY_CODE | — | ✅ |
| 8 | FosEventDocInfoPEOConsignedFlag | CONSIGNED_FLAG | — | ✅ |
| 9 | FosEventDocInfoPEOCreatedBy | CREATED_BY | — | ✅ |
| 10 | FosEventDocInfoPEOCreationDate | CREATION_DATE | — | ✅ |
| 11 | FosEventDocInfoPEOCustomerDeliverToLocation | CUSTOMER_DELIVER_TO_LOCATION | — | ✅ |
| 12 | FosEventDocInfoPEOCustomerShipToLocation | CUSTOMER_SHIP_TO_LOCATION | — | ✅ |
| 13 | FosEventDocInfoPEODeliverToPartyNumber | DELIVER_TO_PARTY_NUMBER | — | ✅ |
| 14 | FosEventDocInfoPEODeliverToPartySiteNumber | DELIVER_TO_PARTY_SITE_NUMBER | — | ✅ |
| 15 | FosEventDocInfoPEODeliveryTransactionId | DELIVERY_TRANSACTION_ID | — | ✅ |
| 16 | FosEventDocInfoPEODestinationType | DESTINATION_TYPE | — | ✅ |
| 17 | FosEventDocInfoPEODocumentDate | DOCUMENT_DATE | — | ✅ |
| 18 | FosEventDocInfoPEODocumentHeaderId | DOCUMENT_HEADER_ID | — | ✅ |
| 19 | FosEventDocInfoPEODocumentLineDetailId | DOCUMENT_LINE_DETAIL_ID | — | ✅ |
| 20 | FosEventDocInfoPEODocumentLineDetailNumber | DOCUMENT_LINE_DETAIL_NUMBER | — | ✅ |
| 21 | FosEventDocInfoPEODocumentLineId | DOCUMENT_LINE_ID | — | ✅ |
| 22 | FosEventDocInfoPEODocumentLineNumber | DOCUMENT_LINE_NUMBER | — | ✅ |
| 23 | FosEventDocInfoPEODocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 24 | FosEventDocInfoPEODocumentRevision | DOCUMENT_REVISION | — | ✅ |
| 25 | FosEventDocInfoPEODocumentSourceSystemId | DOCUMENT_SOURCE_SYSTEM_ID | — | ✅ |
| 26 | FosEventDocInfoPEODocumentType | DOCUMENT_TYPE | — | ✅ |
| 27 | FosEventDocInfoPEODropshipFlag | DROPSHIP_FLAG | — | ✅ |
| 28 | FosEventDocInfoPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 29 | FosEventDocInfoPEOEventDocInfoId | EVENT_DOC_INFO_ID | 🔑 | ✅ |
| 30 | FosEventDocInfoPEOFromBuId | FROM_BU_ID | — | ✅ |
| 31 | FosEventDocInfoPEOFromLeCode | FROM_LE_CODE | — | ✅ |
| 32 | FosEventDocInfoPEOFromLeId | FROM_LE_ID | — | ✅ |
| 33 | FosEventDocInfoPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 34 | FosEventDocInfoPEOItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 35 | FosEventDocInfoPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 36 | FosEventDocInfoPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 37 | FosEventDocInfoPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 38 | FosEventDocInfoPEOLineType | LINE_TYPE | — | ✅ |
| 39 | FosEventDocInfoPEOLinkToDocumentId | LINK_TO_DOCUMENT_ID | — | ✅ |
| 40 | FosEventDocInfoPEOLinkToDocumentSystemId | LINK_TO_DOCUMENT_SYSTEM_ID | — | ✅ |
| 41 | FosEventDocInfoPEOLinkToDocumentType | LINK_TO_DOCUMENT_TYPE | — | ✅ |
| 42 | FosEventDocInfoPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 43 | FosEventDocInfoPEOOrderTypeCode | ORDER_TYPE_CODE | — | ✅ |
| 44 | FosEventDocInfoPEOOrderedAmount | ORDERED_AMOUNT | — | ✅ |
| 45 | FosEventDocInfoPEOOrderedCurrencyCode | ORDERED_CURRENCY_CODE | — | ✅ |
| 46 | FosEventDocInfoPEOOrderedQuantity | ORDERED_QUANTITY | — | ✅ |
| 47 | FosEventDocInfoPEOOrderedUom | ORDERED_UOM | — | ✅ |
| 48 | FosEventDocInfoPEOPriceCurrencyCode | PRICE_CURRENCY_CODE | — | ✅ |
| 49 | FosEventDocInfoPEOPricingUomType | PRICING_UOM_TYPE | — | ✅ |
| 50 | FosEventDocInfoPEOPricingUomValue | PRICING_UOM_VALUE | — | ✅ |
| 51 | FosEventDocInfoPEOPrjRefEnabledFlag | PRJ_REF_ENABLED_FLAG | — | ✅ |
| 52 | FosEventDocInfoPEOProcurementBuId | PROCUREMENT_BU_ID | — | ✅ |
| 53 | FosEventDocInfoPEOPurchasingCategory | PURCHASING_CATEGORY | — | ✅ |
| 54 | FosEventDocInfoPEOReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | ✅ |
| 55 | FosEventDocInfoPEORefDocumentId | REF_DOCUMENT_ID | — | ✅ |
| 56 | FosEventDocInfoPEORefDocumentSystemId | REF_DOCUMENT_SYSTEM_ID | — | ✅ |
| 57 | FosEventDocInfoPEORefDocumentType | REF_DOCUMENT_TYPE | — | ✅ |
| 58 | FosEventDocInfoPEORefSalesOrderLineNumber | REF_SALES_ORDER_LINE_NUMBER | — | ✅ |
| 59 | FosEventDocInfoPEORefSalesOrderNumber | REF_SALES_ORDER_NUMBER | — | ✅ |
| 60 | FosEventDocInfoPEORefSalesOrderSystemCode | REF_SALES_ORDER_SYSTEM_CODE | — | ✅ |
| 61 | FosEventDocInfoPEOReferencedRmaFlag | REFERENCED_RMA_FLAG | — | ✅ |
| 62 | FosEventDocInfoPEOShipFromOrganizationCode | SHIP_FROM_ORGANIZATION_CODE | — | ✅ |
| 63 | FosEventDocInfoPEOShipToCustomerAccntNumber | SHIP_TO_CUSTOMER_ACCNT_NUMBER | — | ✅ |
| 64 | FosEventDocInfoPEOShipToCustomerNumber | SHIP_TO_CUSTOMER_NUMBER | — | ✅ |
| 65 | FosEventDocInfoPEOShipToLocationCode | SHIP_TO_LOCATION_CODE | — | ✅ |
| 66 | FosEventDocInfoPEOShipToOrganizationCode | SHIP_TO_ORGANIZATION_CODE | — | ✅ |
| 67 | FosEventDocInfoPEOShipToPartyNumber | SHIP_TO_PARTY_NUMBER | — | ✅ |
| 68 | FosEventDocInfoPEOShipToPartySiteNumber | SHIP_TO_PARTY_SITE_NUMBER | — | ✅ |
| 69 | FosEventDocInfoPEOSoldToCustomerAccntNumber | SOLD_TO_CUSTOMER_ACCNT_NUMBER | — | ✅ |
| 70 | FosEventDocInfoPEOSoldToCustomerNumber | SOLD_TO_CUSTOMER_NUMBER | — | ✅ |
| 71 | FosEventDocInfoPEOSoldToPartyNumber | SOLD_TO_PARTY_NUMBER | — | ✅ |
| 72 | FosEventDocInfoPEOSourceDocumentId | SOURCE_DOCUMENT_ID | — | ✅ |
| 73 | FosEventDocInfoPEOStatus | STATUS | — | ✅ |
| 74 | FosEventDocInfoPEOSupplierNumber | SUPPLIER_NUMBER | — | ✅ |
| 75 | FosEventDocInfoPEOSupplierSiteCode | SUPPLIER_SITE_CODE | — | ✅ |
| 76 | FosEventDocInfoPEOToBuId | TO_BU_ID | — | ✅ |
| 77 | FosEventDocInfoPEOToLeCode | TO_LE_CODE | — | ✅ |
| 78 | FosEventDocInfoPEOToLeId | TO_LE_ID | — | ✅ |
| 79 | FosEventDocInfoPEOTransactionOrgId | TRANSACTION_ORG_ID | — | ✅ |
| 80 | FosEventDocInfoPEOTransferOrderFlag | TRANSFER_ORDER_FLAG | — | ✅ |
| 81 | FosEventDocInfoPEOUnitPrice | UNIT_PRICE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
