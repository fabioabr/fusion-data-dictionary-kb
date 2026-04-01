---
id: DOC-OTHER-PVO-AssetExtract
doc_type: system-doc
title: "AssetExtract — PVO Cross-Module"
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
  - AssetExtract
  - assetextract
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssetExtract

## 📌 Visão Geral

View Object para extração BICC de dados de Asset Extract. Acessa as tabelas: MNT_ASSETS_EXT.

**Caminho:** `FscmTopModelAM.MaintProgramAM.AssetExtract`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 70 | 1 | 1 | 3 | 4% |

---

## 🔗 Tabelas Relacionadas

- [[mnt_assets_ext|MNT_ASSETS_EXT]] — 70 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[mnt_assets_ext|MNT_ASSETS_EXT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveEndDate | ACTIVE_END_DATE | — | — |
| 2 | AssetId | ASSET_ID | — | ✅ |
| 3 | AssetNumber | ASSET_NUMBER | — | — |
| 4 | AssetOvn | ASSET_OVN | — | — |
| 5 | AssetTag | ASSET_TAG | — | — |
| 6 | CreatedBy | CREATED_BY | — | — |
| 7 | CreationDate | CREATION_DATE | — | — |
| 8 | CurrentLocationContext | CURRENT_LOCATION_CONTEXT | — | — |
| 9 | CurrentLocationId | CURRENT_LOCATION_ID | — | — |
| 10 | CustomerAccountId | CUSTOMER_ACCOUNT_ID | — | — |
| 11 | CustomerAccountSiteId | CUSTOMER_ACCOUNT_SITE_ID | — | — |
| 12 | CustomerAccountSiteUseId | CUSTOMER_ACCOUNT_SITE_USE_ID | — | — |
| 13 | CustomerAssetEndDate | CUSTOMER_ASSET_END_DATE | — | — |
| 14 | CustomerAssetStartDate | CUSTOMER_ASSET_START_DATE | — | — |
| 15 | CustomerBillingPartyId | CUSTOMER_BILLING_PARTY_ID | — | — |
| 16 | CustomerBillingPartySiteId | CUSTOMER_BILLING_PARTY_SITE_ID | — | — |
| 17 | CustomerId | CUSTOMER_ID | — | — |
| 18 | CustomerSiteId | CUSTOMER_SITE_ID | — | — |
| 19 | CustomerSitePartyId | CUSTOMER_SITE_PARTY_ID | — | — |
| 20 | DataRowId | DATA_ROW_ID | 🔑 | ✅ |
| 21 | DfltWoSubType | DFLT_WO_SUB_TYPE | — | — |
| 22 | DfltWoType | DFLT_WO_TYPE | — | — |
| 23 | ExternalLocation | EXTERNAL_LOCATION | — | — |
| 24 | InServiceDate | IN_SERVICE_DATE | — | — |
| 25 | InstalledDate | INSTALLED_DATE | — | — |
| 26 | InstalledLocationContext | INSTALLED_LOCATION_CONTEXT | — | — |
| 27 | InstalledLocationId | INSTALLED_LOCATION_ID | — | — |
| 28 | InventoryLocatorId | INVENTORY_LOCATOR_ID | — | — |
| 29 | IotEnabledFlag | IOT_ENABLED_FLAG | — | — |
| 30 | ItemId | ITEM_ID | — | — |
| 31 | ItemNumber | ITEM_NUMBER | — | — |
| 32 | ItemOrganizationCode | ITEM_ORGANIZATION_CODE | — | — |
| 33 | ItemOrganizationId | ITEM_ORGANIZATION_ID | — | — |
| 34 | ItemRevision | ITEM_REVISION | — | — |
| 35 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 36 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 37 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 38 | LocationOrganizationId | LOCATION_ORGANIZATION_ID | — | — |
| 39 | LogicalFlag | LOGICAL_FLAG | — | — |
| 40 | LotNumber | LOT_NUMBER | — | — |
| 41 | MaintainableFlag | MAINTAINABLE_FLAG | — | — |
| 42 | NewWoAllowedFlag | NEW_WO_ALLOWED_FLAG | — | — |
| 43 | OriginationDate | ORIGINATION_DATE | — | — |
| 44 | PurchaseDate | PURCHASE_DATE | — | — |
| 45 | Quantity | QUANTITY | — | — |
| 46 | RegisteredFlag | REGISTERED_FLAG | — | — |
| 47 | RegistrationDate | REGISTRATION_DATE | — | — |
| 48 | RunId | RUN_ID | — | — |
| 49 | SalesOrderId | SALES_ORDER_ID | — | — |
| 50 | SalesOrderLineId | SALES_ORDER_LINE_ID | — | — |
| 51 | SalesOrderLineNumber | SALES_ORDER_LINE_NUMBER | — | — |
| 52 | SalesOrderNumber | SALES_ORDER_NUMBER | — | — |
| 53 | SalesOrderSourceSystem | SALES_ORDER_SOURCE_SYSTEM | — | — |
| 54 | SalesOrderSourceSystemType | SALES_ORDER_SOURCE_SYSTEM_TYPE | — | — |
| 55 | SerialNumber | SERIAL_NUMBER | — | — |
| 56 | ShipmentDate | SHIPMENT_DATE | — | — |
| 57 | SoldByBusinessUnitId | SOLD_BY_BUSINESS_UNIT_ID | — | — |
| 58 | StatusCode | STATUS_CODE | — | — |
| 59 | SubinventoryCode | SUBINVENTORY_CODE | — | — |
| 60 | SupplierId | SUPPLIER_ID | — | — |
| 61 | SupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 62 | UomCode | UOM_CODE | — | — |
| 63 | WoOperationName | WO_OPERATION_NAME | — | — |
| 64 | WoOperationSeqNumber | WO_OPERATION_SEQ_NUMBER | — | — |
| 65 | WorkCenterCode | WORK_CENTER_CODE | — | — |
| 66 | WorkCenterId | WORK_CENTER_ID | — | — |
| 67 | WorkCenterName | WORK_CENTER_NAME | — | — |
| 68 | WorkOrderId | WORK_ORDER_ID | — | — |
| 69 | WorkOrderNumber | WORK_ORDER_NUMBER | — | — |
| 70 | WorkOrderOperationId | WORK_ORDER_OPERATION_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
