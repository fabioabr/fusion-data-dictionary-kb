---
id: DOC-OTHER-PVO-CustomerAssetPVO
doc_type: system-doc
title: "CustomerAssetPVO — PVO Cross-Module"
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
  - CustomerAssetPVO
  - customerassetpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CustomerAssetPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Customer Asset. Acessa as tabelas: CSE_ASSETS_B, CSE_ASSETS_TL, CSE_GENEALOGY_OBJECTS (+3).

**Caminho:** `FscmTopModelAM.CustomerAssetAM.CustomerAssetPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 163 | 6 | 1 | 152 | 93% |

---

## 🔗 Tabelas Relacionadas

- [[cse_assets_b|CSE_ASSETS_B]] — 122 atributos (1 PKs, 111 BICC)
- [[cse_assets_tl|CSE_ASSETS_TL]] — 4 atributos (4 BICC)
- [[cse_genealogy_objects|CSE_GENEALOGY_OBJECTS]] — 14 atributos (14 BICC)
- [[doo_headers_all|DOO_HEADERS_ALL]] — 4 atributos (4 BICC)
- [[doo_lines_all|DOO_LINES_ALL]] — 13 atributos (13 BICC)
- [[wie_work_orders_b|WIE_WORK_ORDERS_B]] — 6 atributos (6 BICC)

---

## ⚙️ Atributos

### [[cse_assets_b|CSE_ASSETS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | AssetId | ASSET_ID | 🔑 | ✅ |
| 3 | AssetNumber | ASSET_NUMBER | — | ✅ |
| 4 | AssetTag | ASSET_TAG | — | ✅ |
| 5 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 6 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 7 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 8 | AttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 9 | AttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 10 | AttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 11 | AttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 12 | AttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 13 | AttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 14 | AttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 15 | AttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 16 | AttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 17 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 18 | AttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 19 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 20 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 21 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 22 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 23 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 24 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 25 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 26 | AttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 27 | AttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 28 | AttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 29 | AttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 30 | AttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 31 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 32 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 33 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 34 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 35 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 36 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 37 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 38 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 39 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 40 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 41 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 42 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 43 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 44 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 45 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 46 | ContactId | CONTACT_ID | — | — |
| 47 | CorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 48 | CountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | — |
| 49 | CreatedBy | CREATED_BY | — | ✅ |
| 50 | CreationDate | CREATION_DATE | — | ✅ |
| 51 | CurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 52 | CurrencyCode | CURRENCY_CODE | — | — |
| 53 | CurrentLocationContext | CURRENT_LOCATION_CONTEXT | — | ✅ |
| 54 | CurrentLocationId | CURRENT_LOCATION_ID | — | ✅ |
| 55 | CustomerAccountId | CUSTOMER_ACCOUNT_ID | — | ✅ |
| 56 | CustomerAccountSiteId | CUSTOMER_ACCOUNT_SITE_ID | — | ✅ |
| 57 | CustomerAccountSiteUseId | CUSTOMER_ACCOUNT_SITE_USE_ID | — | ✅ |
| 58 | CustomerAssetEndDate | CUSTOMER_ASSET_END_DATE | — | ✅ |
| 59 | CustomerAssetStartDate | CUSTOMER_ASSET_START_DATE | — | ✅ |
| 60 | CustomerBillingPartyId | CUSTOMER_BILLING_PARTY_ID | — | ✅ |
| 61 | CustomerBillingPartySiteId | CUSTOMER_BILLING_PARTY_SITE_ID | — | ✅ |
| 62 | CustomerId | CUSTOMER_ID | — | ✅ |
| 63 | CustomerSiteId | CUSTOMER_SITE_ID | — | ✅ |
| 64 | CustomerSitePartyId | CUSTOMER_SITE_PARTY_ID | — | ✅ |
| 65 | DfltWoSubType | DFLT_WO_SUB_TYPE | — | ✅ |
| 66 | DfltWoType | DFLT_WO_TYPE | — | ✅ |
| 67 | ExternalLocation | EXTERNAL_LOCATION | — | — |
| 68 | FulfillLineId | FULFILL_LINE_ID | — | — |
| 69 | GenObjectId | GEN_OBJECT_ID | — | ✅ |
| 70 | InServiceDate | IN_SERVICE_DATE | — | ✅ |
| 71 | InstalledDate | INSTALLED_DATE | — | ✅ |
| 72 | InstalledLocationContext | INSTALLED_LOCATION_CONTEXT | — | ✅ |
| 73 | InstalledLocationId | INSTALLED_LOCATION_ID | — | ✅ |
| 74 | InventoryLocatorId | INVENTORY_LOCATOR_ID | — | ✅ |
| 75 | ItemId | ITEM_ID | — | ✅ |
| 76 | ItemOrganizationId | ITEM_ORGANIZATION_ID | — | ✅ |
| 77 | ItemRevision | ITEM_REVISION | — | ✅ |
| 78 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 79 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 80 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 81 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 82 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 83 | LocationOrganizationId | LOCATION_ORGANIZATION_ID | — | ✅ |
| 84 | LogicalFlag | LOGICAL_FLAG | — | ✅ |
| 85 | LotNumber | LOT_NUMBER | — | ✅ |
| 86 | MaintainableFlag | MAINTAINABLE_FLAG | — | ✅ |
| 87 | NewWoAllowedFlag | NEW_WO_ALLOWED_FLAG | — | ✅ |
| 88 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 89 | OriginationDate | ORIGINATION_DATE | — | ✅ |
| 90 | OwnedBy | OWNED_BY | — | ✅ |
| 91 | ParentOrderLineId | PARENT_ORDER_LINE_ID | — | ✅ |
| 92 | ParentOrderLineNumber | PARENT_ORDER_LINE_NUMBER | — | ✅ |
| 93 | PartiallyFinishedFlag | PARTIALLY_FINISHED_FLAG | — | ✅ |
| 94 | ProjectId | PROJECT_ID | — | — |
| 95 | PurchaseDate | PURCHASE_DATE | — | ✅ |
| 96 | Quantity | QUANTITY | — | ✅ |
| 97 | RegisteredFlag | REGISTERED_FLAG | — | ✅ |
| 98 | RegistrationDate | REGISTRATION_DATE | — | — |
| 99 | RequestId | REQUEST_ID | — | ✅ |
| 100 | SalesOrderId | SALES_ORDER_ID | — | ✅ |
| 101 | SalesOrderLineId | SALES_ORDER_LINE_ID | — | ✅ |
| 102 | SalesOrderLineNumber | SALES_ORDER_LINE_NUMBER | — | ✅ |
| 103 | SalesOrderNumber | SALES_ORDER_NUMBER | — | ✅ |
| 104 | SalesOrderSourceSystem | SALES_ORDER_SOURCE_SYSTEM | — | ✅ |
| 105 | SalesOrderSourceSystemType | SALES_ORDER_SOURCE_SYSTEM_TYPE | — | ✅ |
| 106 | SecondaryQuantity | SECONDARY_QUANTITY | — | ✅ |
| 107 | SecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 108 | SerialNumber | SERIAL_NUMBER | — | ✅ |
| 109 | ShipmentDate | SHIPMENT_DATE | — | ✅ |
| 110 | ShipmentNumber | SHIPMENT_NUMBER | — | — |
| 111 | SoldByBusinessUnitId | SOLD_BY_BUSINESS_UNIT_ID | — | ✅ |
| 112 | StatusCode | STATUS_CODE | — | ✅ |
| 113 | SubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 114 | SupplierId | SUPPLIER_ID | — | ✅ |
| 115 | SupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 116 | TaskId | TASK_ID | — | — |
| 117 | UnassignedFlag | UNASSIGNED_FLAG | — | ✅ |
| 118 | UomCode | UOM_CODE | — | ✅ |
| 119 | UsedBy | USED_BY | — | ✅ |
| 120 | WorkCenterId | WORK_CENTER_ID | — | ✅ |
| 121 | WorkOrderId | WORK_ORDER_ID | — | ✅ |
| 122 | WorkOrderOperationId | WORK_ORDER_OPERATION_ID | — | ✅ |

### [[cse_assets_tl|CSE_ASSETS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetId1 | ASSET_ID | — | ✅ |
| 2 | Description | DESCRIPTION | — | ✅ |
| 3 | Language | LANGUAGE | — | ✅ |
| 4 | SourceLang | SOURCE_LANG | — | ✅ |

### [[cse_genealogy_objects|CSE_GENEALOGY_OBJECTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GenealogyObjectPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | GenealogyObjectPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | GenealogyObjectPEOGenObjectId | GEN_OBJECT_ID | — | ✅ |
| 4 | GenealogyObjectPEOItemId | ITEM_ID | — | ✅ |
| 5 | GenealogyObjectPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | GenealogyObjectPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | GenealogyObjectPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | GenealogyObjectPEOLotNumber | LOT_NUMBER | — | ✅ |
| 9 | GenealogyObjectPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 10 | GenealogyObjectPEOOriginationDate | ORIGINATION_DATE | — | ✅ |
| 11 | GenealogyObjectPEOOriginationDocumentNumber | ORIGINATION_DOCUMENT_NUMBER | — | ✅ |
| 12 | GenealogyObjectPEOOriginationDocumentType | ORIGINATION_DOCUMENT_TYPE | — | ✅ |
| 13 | GenealogyObjectPEOOriginationQuantity | ORIGINATION_QUANTITY | — | ✅ |
| 14 | GenealogyObjectPEOSerialNumber | SERIAL_NUMBER | — | ✅ |

### [[doo_headers_all|DOO_HEADERS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HeaderPEOHeaderId | HEADER_ID | — | ✅ |
| 2 | HeaderPEOOrderNumber | ORDER_NUMBER | — | ✅ |
| 3 | HeaderPEOOrderedDate | ORDERED_DATE | — | ✅ |
| 4 | HeaderPEOTransactionalCurrencyCode | TRANSACTIONAL_CURRENCY_CODE | — | ✅ |

### [[doo_lines_all|DOO_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LinePEOActualShipDate | ACTUAL_SHIP_DATE | — | ✅ |
| 2 | LinePEOCanceledFlag | CANCELED_FLAG | — | ✅ |
| 3 | LinePEOFulfillmentDate | FULFILLMENT_DATE | — | ✅ |
| 4 | LinePEOLineId | LINE_ID | — | ✅ |
| 5 | LinePEOLineNumber | LINE_NUMBER | — | ✅ |
| 6 | LinePEOOnHold | ON_HOLD | — | ✅ |
| 7 | LinePEOOpenFlag | OPEN_FLAG | — | ✅ |
| 8 | LinePEOOrderedQty | ORDERED_QTY | — | ✅ |
| 9 | LinePEOOrderedUom | ORDERED_UOM | — | ✅ |
| 10 | LinePEOScheduleShipDate | SCHEDULE_SHIP_DATE | — | ✅ |
| 11 | LinePEOSourceLineNumber | SOURCE_LINE_NUMBER | — | ✅ |
| 12 | LinePEOSourceOrderNumber | SOURCE_ORDER_NUMBER | — | ✅ |
| 13 | LinePEOSourceScheduleNumber | SOURCE_SCHEDULE_NUMBER | — | ✅ |

### [[wie_work_orders_b|WIE_WORK_ORDERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderAnalyticsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 2 | WorkOrderAnalyticsPEOWorkDefinitionId | WORK_DEFINITION_ID | — | ✅ |
| 3 | WorkOrderAnalyticsPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 4 | WorkOrderAnalyticsPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | ✅ |
| 5 | WorkOrderAnalyticsPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | ✅ |
| 6 | WorkOrderAnalyticsPEOWorkOrderType | WORK_ORDER_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
