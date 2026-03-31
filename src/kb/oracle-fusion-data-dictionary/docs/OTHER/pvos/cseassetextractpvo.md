---
id: DOC-OTHER-PVO-CseAssetExtractPVO
doc_type: system-doc
title: "CseAssetExtractPVO — PVO Cross-Module"
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
  - CseAssetExtractPVO
  - cseassetextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CseAssetExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cse Asset Extract. Acessa as tabelas: CSE_ASSETS_B, CSE_ASSETS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.CseAssetExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 145 | 2 | 3 | 145 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_assets_b|CSE_ASSETS_B]] — 135 atributos (1 PKs, 135 BICC)
- [[cse_assets_tl|CSE_ASSETS_TL]] — 10 atributos (2 PKs, 10 BICC)

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
| 19 | AttributeChar21 | ATTRIBUTE_CHAR21 | — | ✅ |
| 20 | AttributeChar22 | ATTRIBUTE_CHAR22 | — | ✅ |
| 21 | AttributeChar23 | ATTRIBUTE_CHAR23 | — | ✅ |
| 22 | AttributeChar24 | ATTRIBUTE_CHAR24 | — | ✅ |
| 23 | AttributeChar25 | ATTRIBUTE_CHAR25 | — | ✅ |
| 24 | AttributeChar26 | ATTRIBUTE_CHAR26 | — | ✅ |
| 25 | AttributeChar27 | ATTRIBUTE_CHAR27 | — | ✅ |
| 26 | AttributeChar28 | ATTRIBUTE_CHAR28 | — | ✅ |
| 27 | AttributeChar29 | ATTRIBUTE_CHAR29 | — | ✅ |
| 28 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 29 | AttributeChar30 | ATTRIBUTE_CHAR30 | — | ✅ |
| 30 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 31 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 32 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 33 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 34 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 35 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 36 | AttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 37 | AttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 38 | AttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 39 | AttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 40 | AttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 41 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 42 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 43 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 44 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 45 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 46 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 47 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 48 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 49 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 50 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 51 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 52 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 53 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 54 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 55 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 56 | BomExplosionFlag | BOM_EXPLOSION_FLAG | — | ✅ |
| 57 | CompetitorAssetFlag | COMPETITOR_ASSET_FLAG | — | ✅ |
| 58 | ComponentSequenceId | COMPONENT_SEQUENCE_ID | — | ✅ |
| 59 | CorpCurrencyCode | CORP_CURRENCY_CODE | — | ✅ |
| 60 | CreatedBy | CREATED_BY | — | ✅ |
| 61 | CreationDate | CREATION_DATE | — | ✅ |
| 62 | CurcyConvRateType | CURCY_CONV_RATE_TYPE | — | ✅ |
| 63 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 64 | CurrentLocationContext | CURRENT_LOCATION_CONTEXT | — | ✅ |
| 65 | CurrentLocationId | CURRENT_LOCATION_ID | — | ✅ |
| 66 | CustomerAccountId | CUSTOMER_ACCOUNT_ID | — | ✅ |
| 67 | CustomerAccountSiteId | CUSTOMER_ACCOUNT_SITE_ID | — | ✅ |
| 68 | CustomerAccountSiteUseId | CUSTOMER_ACCOUNT_SITE_USE_ID | — | ✅ |
| 69 | CustomerAssetEndDate | CUSTOMER_ASSET_END_DATE | — | ✅ |
| 70 | CustomerAssetStartDate | CUSTOMER_ASSET_START_DATE | — | ✅ |
| 71 | CustomerBillingPartyId | CUSTOMER_BILLING_PARTY_ID | — | ✅ |
| 72 | CustomerBillingPartySiteId | CUSTOMER_BILLING_PARTY_SITE_ID | — | ✅ |
| 73 | CustomerId | CUSTOMER_ID | — | ✅ |
| 74 | CustomerSiteId | CUSTOMER_SITE_ID | — | ✅ |
| 75 | CustomerSitePartyId | CUSTOMER_SITE_PARTY_ID | — | ✅ |
| 76 | DescriptionAssetFlag | DESCRIPTION_ASSET_FLAG | — | ✅ |
| 77 | DfltWoSubType | DFLT_WO_SUB_TYPE | — | ✅ |
| 78 | DfltWoType | DFLT_WO_TYPE | — | ✅ |
| 79 | ExternalLocation | EXTERNAL_LOCATION | — | ✅ |
| 80 | ExternalSystemPackingUnit | EXTERNAL_SYSTEM_PACKING_UNIT | — | ✅ |
| 81 | FulfillLineId | FULFILL_LINE_ID | — | ✅ |
| 82 | GenObjectId | GEN_OBJECT_ID | — | ✅ |
| 83 | InServiceDate | IN_SERVICE_DATE | — | ✅ |
| 84 | InstalledDate | INSTALLED_DATE | — | ✅ |
| 85 | InstalledLocationContext | INSTALLED_LOCATION_CONTEXT | — | ✅ |
| 86 | InstalledLocationId | INSTALLED_LOCATION_ID | — | ✅ |
| 87 | InventoryLocatorId | INVENTORY_LOCATOR_ID | — | ✅ |
| 88 | IotEnabledFlag | IOT_ENABLED_FLAG | — | ✅ |
| 89 | ItemId | ITEM_ID | — | ✅ |
| 90 | ItemOrganizationId | ITEM_ORGANIZATION_ID | — | ✅ |
| 91 | ItemRevision | ITEM_REVISION | — | ✅ |
| 92 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 93 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 94 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 95 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 96 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 97 | LocationOrganizationId | LOCATION_ORGANIZATION_ID | — | ✅ |
| 98 | LogicalFlag | LOGICAL_FLAG | — | ✅ |
| 99 | LotNumber | LOT_NUMBER | — | ✅ |
| 100 | MaintainableFlag | MAINTAINABLE_FLAG | — | ✅ |
| 101 | NewWoAllowedFlag | NEW_WO_ALLOWED_FLAG | — | ✅ |
| 102 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 103 | OriginationDate | ORIGINATION_DATE | — | ✅ |
| 104 | OwnedBy | OWNED_BY | — | ✅ |
| 105 | ParentFulfillLineId | PARENT_FULFILL_LINE_ID | — | ✅ |
| 106 | ParentOrderLineId | PARENT_ORDER_LINE_ID | — | ✅ |
| 107 | ParentOrderLineNumber | PARENT_ORDER_LINE_NUMBER | — | ✅ |
| 108 | PartiallyFinishedFlag | PARTIALLY_FINISHED_FLAG | — | ✅ |
| 109 | PurchaseDate | PURCHASE_DATE | — | ✅ |
| 110 | Quantity | QUANTITY | — | ✅ |
| 111 | QuantityPerAssembly | QUANTITY_PER_ASSEMBLY | — | ✅ |
| 112 | RegisteredFlag | REGISTERED_FLAG | — | ✅ |
| 113 | RegistrationDate | REGISTRATION_DATE | — | ✅ |
| 114 | RequestId | REQUEST_ID | — | ✅ |
| 115 | SalesOrderId | SALES_ORDER_ID | — | ✅ |
| 116 | SalesOrderLineId | SALES_ORDER_LINE_ID | — | ✅ |
| 117 | SalesOrderLineNumber | SALES_ORDER_LINE_NUMBER | — | ✅ |
| 118 | SalesOrderNumber | SALES_ORDER_NUMBER | — | ✅ |
| 119 | SalesOrderSourceSystem | SALES_ORDER_SOURCE_SYSTEM | — | ✅ |
| 120 | SalesOrderSourceSystemType | SALES_ORDER_SOURCE_SYSTEM_TYPE | — | ✅ |
| 121 | SerialNumber | SERIAL_NUMBER | — | ✅ |
| 122 | ShipmentDate | SHIPMENT_DATE | — | ✅ |
| 123 | ShipmentId | SHIPMENT_ID | — | ✅ |
| 124 | SoldByBusinessUnitId | SOLD_BY_BUSINESS_UNIT_ID | — | ✅ |
| 125 | SplitFromAssetId | SPLIT_FROM_ASSET_ID | — | ✅ |
| 126 | StatusCode | STATUS_CODE | — | ✅ |
| 127 | SubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 128 | SupplierId | SUPPLIER_ID | — | ✅ |
| 129 | SupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 130 | UnassignedFlag | UNASSIGNED_FLAG | — | ✅ |
| 131 | UomCode | UOM_CODE | — | ✅ |
| 132 | UsedBy | USED_BY | — | ✅ |
| 133 | WorkCenterId | WORK_CENTER_ID | — | ✅ |
| 134 | WorkOrderId | WORK_ORDER_ID | — | ✅ |
| 135 | WorkOrderOperationId | WORK_ORDER_OPERATION_ID | — | ✅ |

### [[cse_assets_tl|CSE_ASSETS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetTranslationAnalyticsPEOAssetId | ASSET_ID | 🔑 | ✅ |
| 2 | AssetTranslationAnalyticsPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | AssetTranslationAnalyticsPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | AssetTranslationAnalyticsPEODescription | DESCRIPTION | — | ✅ |
| 5 | AssetTranslationAnalyticsPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | AssetTranslationAnalyticsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | AssetTranslationAnalyticsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | AssetTranslationAnalyticsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | AssetTranslationAnalyticsPEOSourceLang | SOURCE_LANG | — | ✅ |
| 10 | AssetTranslationAnalyticsPEOTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
