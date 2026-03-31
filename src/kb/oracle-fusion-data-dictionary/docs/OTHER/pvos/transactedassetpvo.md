---
id: DOC-OTHER-PVO-TransactedAssetPVO
doc_type: system-doc
title: "TransactedAssetPVO — PVO Cross-Module"
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
  - TransactedAssetPVO
  - transactedassetpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactedAssetPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transacted Asset. Acessa as tabelas: CSE_ASSETS_B, CSE_TRANSACTED_ASSETS, CSE_TRANSACTIONS (+1).

**Caminho:** `FscmTopModelAM.ProductGenealogyAM.TransactedAssetPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 214 | 4 | 3 | 211 | 99% |

---

## 🔗 Tabelas Relacionadas

- [[cse_assets_b|CSE_ASSETS_B]] — 118 atributos (1 PKs, 115 BICC)
- [[cse_transacted_assets|CSE_TRANSACTED_ASSETS]] — 28 atributos (1 PKs, 28 BICC)
- [[cse_transactions|CSE_TRANSACTIONS]] — 62 atributos (1 PKs, 62 BICC)
- [[wie_work_orders_b|WIE_WORK_ORDERS_B]] — 6 atributos (6 BICC)

---

## ⚙️ Atributos

### [[cse_assets_b|CSE_ASSETS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetPEOActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | AssetPEOAssetId | ASSET_ID | 🔑 | ✅ |
| 3 | AssetPEOAssetNumber | ASSET_NUMBER | — | ✅ |
| 4 | AssetPEOAssetTag | ASSET_TAG | — | ✅ |
| 5 | AssetPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 6 | AssetPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 7 | AssetPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 8 | AssetPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 9 | AssetPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 10 | AssetPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 11 | AssetPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 12 | AssetPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 13 | AssetPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 14 | AssetPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 15 | AssetPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 16 | AssetPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 17 | AssetPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 18 | AssetPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 19 | AssetPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 20 | AssetPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 21 | AssetPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 22 | AssetPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 23 | AssetPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 24 | AssetPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 25 | AssetPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 26 | AssetPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 27 | AssetPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 28 | AssetPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 29 | AssetPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 30 | AssetPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 31 | AssetPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 32 | AssetPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 33 | AssetPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 34 | AssetPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 35 | AssetPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 36 | AssetPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 37 | AssetPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 38 | AssetPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 39 | AssetPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 40 | AssetPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 41 | AssetPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 42 | AssetPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 43 | AssetPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 44 | AssetPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 45 | AssetPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 46 | AssetPEOCreatedBy | CREATED_BY | — | ✅ |
| 47 | AssetPEOCreationDate | CREATION_DATE | — | ✅ |
| 48 | AssetPEOCurrentLocationContext | CURRENT_LOCATION_CONTEXT | — | ✅ |
| 49 | AssetPEOCurrentLocationId | CURRENT_LOCATION_ID | — | ✅ |
| 50 | AssetPEOCustomerAccountId | CUSTOMER_ACCOUNT_ID | — | ✅ |
| 51 | AssetPEOCustomerAccountSiteId | CUSTOMER_ACCOUNT_SITE_ID | — | ✅ |
| 52 | AssetPEOCustomerAccountSiteUseId | CUSTOMER_ACCOUNT_SITE_USE_ID | — | ✅ |
| 53 | AssetPEOCustomerAssetEndDate | CUSTOMER_ASSET_END_DATE | — | ✅ |
| 54 | AssetPEOCustomerAssetStartDate | CUSTOMER_ASSET_START_DATE | — | ✅ |
| 55 | AssetPEOCustomerBillingPartyId | CUSTOMER_BILLING_PARTY_ID | — | ✅ |
| 56 | AssetPEOCustomerBillingPartySiteId | CUSTOMER_BILLING_PARTY_SITE_ID | — | ✅ |
| 57 | AssetPEOCustomerId | CUSTOMER_ID | — | ✅ |
| 58 | AssetPEOCustomerSiteId | CUSTOMER_SITE_ID | — | ✅ |
| 59 | AssetPEOCustomerSitePartyId | CUSTOMER_SITE_PARTY_ID | — | ✅ |
| 60 | AssetPEODfltWoSubType | DFLT_WO_SUB_TYPE | — | ✅ |
| 61 | AssetPEODfltWoType | DFLT_WO_TYPE | — | ✅ |
| 62 | AssetPEOExternalLocation | EXTERNAL_LOCATION | — | ✅ |
| 63 | AssetPEOFulfillLineId | FULFILL_LINE_ID | — | ✅ |
| 64 | AssetPEOGenObjectId | GEN_OBJECT_ID | — | ✅ |
| 65 | AssetPEOInServiceDate | IN_SERVICE_DATE | — | ✅ |
| 66 | AssetPEOInstalledDate | INSTALLED_DATE | — | ✅ |
| 67 | AssetPEOInstalledLocationContext | INSTALLED_LOCATION_CONTEXT | — | ✅ |
| 68 | AssetPEOInstalledLocationId | INSTALLED_LOCATION_ID | — | ✅ |
| 69 | AssetPEOInventoryLocatorId | INVENTORY_LOCATOR_ID | — | ✅ |
| 70 | AssetPEOItemId | ITEM_ID | — | ✅ |
| 71 | AssetPEOItemOrganizationId | ITEM_ORGANIZATION_ID | — | ✅ |
| 72 | AssetPEOItemRevision | ITEM_REVISION | — | ✅ |
| 73 | AssetPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 74 | AssetPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 75 | AssetPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 76 | AssetPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 77 | AssetPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 78 | AssetPEOLocationOrganizationId | LOCATION_ORGANIZATION_ID | — | ✅ |
| 79 | AssetPEOLogicalFlag | LOGICAL_FLAG | — | ✅ |
| 80 | AssetPEOLotNumber | LOT_NUMBER | — | ✅ |
| 81 | AssetPEOMaintainableFlag | MAINTAINABLE_FLAG | — | ✅ |
| 82 | AssetPEONewWoAllowedFlag | NEW_WO_ALLOWED_FLAG | — | ✅ |
| 83 | AssetPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 84 | AssetPEOOriginationDate | ORIGINATION_DATE | — | ✅ |
| 85 | AssetPEOOwnedBy | OWNED_BY | — | ✅ |
| 86 | AssetPEOParentFulfillLineId | PARENT_FULFILL_LINE_ID | — | ✅ |
| 87 | AssetPEOParentOrderLineId | PARENT_ORDER_LINE_ID | — | ✅ |
| 88 | AssetPEOParentOrderLineNumber | PARENT_ORDER_LINE_NUMBER | — | ✅ |
| 89 | AssetPEOPartiallyFinishedFlag | PARTIALLY_FINISHED_FLAG | — | ✅ |
| 90 | AssetPEOPurchaseDate | PURCHASE_DATE | — | ✅ |
| 91 | AssetPEOQuantity | QUANTITY | — | ✅ |
| 92 | AssetPEORegisteredFlag | REGISTERED_FLAG | — | ✅ |
| 93 | AssetPEORegistrationDate | REGISTRATION_DATE | — | ✅ |
| 94 | AssetPEORequestId | REQUEST_ID | — | ✅ |
| 95 | AssetPEOSalesOrderId | SALES_ORDER_ID | — | ✅ |
| 96 | AssetPEOSalesOrderLineId | SALES_ORDER_LINE_ID | — | ✅ |
| 97 | AssetPEOSalesOrderLineNumber | SALES_ORDER_LINE_NUMBER | — | ✅ |
| 98 | AssetPEOSalesOrderNumber | SALES_ORDER_NUMBER | — | ✅ |
| 99 | AssetPEOSalesOrderSourceSystem | SALES_ORDER_SOURCE_SYSTEM | — | ✅ |
| 100 | AssetPEOSalesOrderSourceSystemType | SALES_ORDER_SOURCE_SYSTEM_TYPE | — | ✅ |
| 101 | AssetPEOSerialNumber | SERIAL_NUMBER | — | ✅ |
| 102 | AssetPEOShipmentDate | SHIPMENT_DATE | — | ✅ |
| 103 | AssetPEOShipmentId | SHIPMENT_ID | — | ✅ |
| 104 | AssetPEOSoldByBusinessUnitId | SOLD_BY_BUSINESS_UNIT_ID | — | ✅ |
| 105 | AssetPEOSplitFromAssetId | SPLIT_FROM_ASSET_ID | — | ✅ |
| 106 | AssetPEOStatusCode | STATUS_CODE | — | ✅ |
| 107 | AssetPEOSubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 108 | AssetPEOSupplierId | SUPPLIER_ID | — | ✅ |
| 109 | AssetPEOSupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 110 | AssetPEOUnassignedFlag | UNASSIGNED_FLAG | — | ✅ |
| 111 | AssetPEOUomCode | UOM_CODE | — | ✅ |
| 112 | AssetPEOUsedBy | USED_BY | — | ✅ |
| 113 | AssetPEOWorkCenterId | WORK_CENTER_ID | — | ✅ |
| 114 | AssetPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 115 | AssetPEOWorkOrderOperationId | WORK_ORDER_OPERATION_ID | — | ✅ |
| 116 | CountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | — |
| 117 | ProjectId | PROJECT_ID | — | — |
| 118 | TaskId | TASK_ID | — | — |

### [[cse_transacted_assets|CSE_TRANSACTED_ASSETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetId | ASSET_ID | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | FullSnapshotFlag | FULL_SNAPSHOT_FLAG | — | ✅ |
| 5 | GenObjectId | GEN_OBJECT_ID | — | ✅ |
| 6 | InventoryLocatorId | INVENTORY_LOCATOR_ID | — | ✅ |
| 7 | ItemId | ITEM_ID | — | ✅ |
| 8 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 9 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | LocationContext | LOCATION_CONTEXT | — | ✅ |
| 14 | MergedToAssetId | MERGED_TO_ASSET_ID | — | ✅ |
| 15 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 16 | RequestId | REQUEST_ID | — | ✅ |
| 17 | SecondaryQuantity | SECONDARY_QUANTITY | — | ✅ |
| 18 | SecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 19 | SnapshotQualified | SNAPSHOT_QUALIFIED | — | ✅ |
| 20 | SplitFromAssetId | SPLIT_FROM_ASSET_ID | — | ✅ |
| 21 | SubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 22 | TransactedAssetId | TRANSACTED_ASSET_ID | 🔑 | ✅ |
| 23 | TransactedQuantity | TRANSACTED_QUANTITY | — | ✅ |
| 24 | TransactedUomCode | TRANSACTED_UOM_CODE | — | ✅ |
| 25 | TransactionId | TRANSACTION_ID | — | ✅ |
| 26 | WorkCenterId | WORK_CENTER_ID | — | ✅ |
| 27 | WorkOrderId | WORK_ORDER_ID | — | ✅ |
| 28 | WorkOrderOperationId | WORK_ORDER_OPERATION_ID | — | ✅ |

### [[cse_transactions|CSE_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetTransactionPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 2 | AssetTransactionPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 3 | AssetTransactionPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 4 | AssetTransactionPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 5 | AssetTransactionPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 6 | AssetTransactionPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 7 | AssetTransactionPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 8 | AssetTransactionPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 9 | AssetTransactionPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 10 | AssetTransactionPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 11 | AssetTransactionPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 12 | AssetTransactionPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 13 | AssetTransactionPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 14 | AssetTransactionPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 15 | AssetTransactionPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 16 | AssetTransactionPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 17 | AssetTransactionPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 18 | AssetTransactionPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 19 | AssetTransactionPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 20 | AssetTransactionPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 21 | AssetTransactionPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 22 | AssetTransactionPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 23 | AssetTransactionPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 24 | AssetTransactionPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 25 | AssetTransactionPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 26 | AssetTransactionPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 27 | AssetTransactionPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 28 | AssetTransactionPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 29 | AssetTransactionPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 30 | AssetTransactionPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 31 | AssetTransactionPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 32 | AssetTransactionPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 33 | AssetTransactionPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 34 | AssetTransactionPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 35 | AssetTransactionPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 36 | AssetTransactionPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 37 | AssetTransactionPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 38 | AssetTransactionPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 39 | AssetTransactionPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 40 | AssetTransactionPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 41 | AssetTransactionPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 42 | AssetTransactionPEOCreatedBy | CREATED_BY | — | ✅ |
| 43 | AssetTransactionPEOCreationDate | CREATION_DATE | — | ✅ |
| 44 | AssetTransactionPEOItemId | ITEM_ID | — | ✅ |
| 45 | AssetTransactionPEOItemOrganizationId | ITEM_ORGANIZATION_ID | — | ✅ |
| 46 | AssetTransactionPEOItemRevision | ITEM_REVISION | — | ✅ |
| 47 | AssetTransactionPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 48 | AssetTransactionPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 49 | AssetTransactionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 50 | AssetTransactionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 51 | AssetTransactionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 52 | AssetTransactionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 53 | AssetTransactionPEORequestId | REQUEST_ID | — | ✅ |
| 54 | AssetTransactionPEOSrcSystemId | SRC_SYSTEM_ID | — | ✅ |
| 55 | AssetTransactionPEOSrcSystemType | SRC_SYSTEM_TYPE | — | ✅ |
| 56 | AssetTransactionPEOSrcTransactionDate | SRC_TRANSACTION_DATE | — | ✅ |
| 57 | AssetTransactionPEOSrcTransactionId | SRC_TRANSACTION_ID | — | ✅ |
| 58 | AssetTransactionPEOSrcTransactionQty | SRC_TRANSACTION_QTY | — | ✅ |
| 59 | AssetTransactionPEOSrcTransactionType | SRC_TRANSACTION_TYPE | — | ✅ |
| 60 | AssetTransactionPEOSrcTransactionTypeId | SRC_TRANSACTION_TYPE_ID | — | ✅ |
| 61 | AssetTransactionPEOSrcTransactionUomCode | SRC_TRANSACTION_UOM_CODE | — | ✅ |
| 62 | AssetTransactionPEOTransactionId | TRANSACTION_ID | 🔑 | ✅ |

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
