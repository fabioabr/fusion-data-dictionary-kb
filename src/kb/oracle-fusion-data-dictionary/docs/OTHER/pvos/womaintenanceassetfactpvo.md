---
id: DOC-OTHER-PVO-WOMaintenanceAssetFactPVO
doc_type: system-doc
title: "WOMaintenanceAssetFactPVO — PVO Cross-Module"
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
  - WOMaintenanceAssetFactPVO
  - womaintenanceassetfactpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WOMaintenanceAssetFactPVO

## 📌 Visão Geral

View Object para extração BICC de dados de WOMaintenance Asset Fact. Acessa as tabelas: CSE_ASSETS_VL, HZ_PARTIES, INV_ITEM_LOCATIONS (+2).

**Caminho:** `FscmTopModelAM.WorkOrderAM.WOMaintenanceAssetFactPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 220 | 5 | 1 | 71 | 32% |

---

## 🔗 Tabelas Relacionadas

- [[cse_assets_vl|CSE_ASSETS_VL]] — 97 atributos (1 PKs, 34 BICC)
- [[hz_parties|HZ_PARTIES]] — 3 atributos
- [[inv_item_locations|INV_ITEM_LOCATIONS]] — 4 atributos
- [[wie_work_orders_vl|WIE_WORK_ORDERS_VL]] — 103 atributos (30 BICC)
- [[wie_wo_assets|WIE_WO_ASSETS]] — 13 atributos (7 BICC)

---

## ⚙️ Atributos

### [[cse_assets_vl|CSE_ASSETS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetPEOActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | AssetPEOAssetId | ASSET_ID | 🔑 | ✅ |
| 3 | AssetPEOAssetNumber | ASSET_NUMBER | — | ✅ |
| 4 | AssetPEOAssetTag | ASSET_TAG | — | — |
| 5 | AssetPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 6 | AssetPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 7 | AssetPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 8 | AssetPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 9 | AssetPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 10 | AssetPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 11 | AssetPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 12 | AssetPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 13 | AssetPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 14 | AssetPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 15 | AssetPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 16 | AssetPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 17 | AssetPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 18 | AssetPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 19 | AssetPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 20 | AssetPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 21 | AssetPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 22 | AssetPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 23 | AssetPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 24 | AssetPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 25 | AssetPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 26 | AssetPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 27 | AssetPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 28 | AssetPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 29 | AssetPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 30 | AssetPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 31 | AssetPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 32 | AssetPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 33 | AssetPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 34 | AssetPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 35 | AssetPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 36 | AssetPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 37 | AssetPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 38 | AssetPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 39 | AssetPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 40 | AssetPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 41 | AssetPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 42 | AssetPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 43 | AssetPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 44 | AssetPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 45 | AssetPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 46 | AssetPEOContactId | CONTACT_ID | — | — |
| 47 | AssetPEOCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | — |
| 48 | AssetPEOCreatedBy | CREATED_BY | — | — |
| 49 | AssetPEOCreationDate | CREATION_DATE | — | ✅ |
| 50 | AssetPEOCurrentLocationContext | CURRENT_LOCATION_CONTEXT | — | ✅ |
| 51 | AssetPEOCurrentLocationId | CURRENT_LOCATION_ID | — | ✅ |
| 52 | AssetPEOCustomerId | CUSTOMER_ID | — | ✅ |
| 53 | AssetPEOCustomerSiteId | CUSTOMER_SITE_ID | — | ✅ |
| 54 | AssetPEODescription | DESCRIPTION | — | ✅ |
| 55 | AssetPEODfltWoSubType | DFLT_WO_SUB_TYPE | — | — |
| 56 | AssetPEODfltWoType | DFLT_WO_TYPE | — | — |
| 57 | AssetPEOGenObjectId | GEN_OBJECT_ID | — | ✅ |
| 58 | AssetPEOInServiceDate | IN_SERVICE_DATE | — | ✅ |
| 59 | AssetPEOInstalledDate | INSTALLED_DATE | — | ✅ |
| 60 | AssetPEOInstalledLocationContext | INSTALLED_LOCATION_CONTEXT | — | — |
| 61 | AssetPEOInstalledLocationId | INSTALLED_LOCATION_ID | — | ✅ |
| 62 | AssetPEOInventoryLocatorId | INVENTORY_LOCATOR_ID | — | ✅ |
| 63 | AssetPEOItemId | ITEM_ID | — | ✅ |
| 64 | AssetPEOItemOrganizationId | ITEM_ORGANIZATION_ID | — | ✅ |
| 65 | AssetPEOItemRevision | ITEM_REVISION | — | — |
| 66 | AssetPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 67 | AssetPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 68 | AssetPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 69 | AssetPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 70 | AssetPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 71 | AssetPEOLotNumber | LOT_NUMBER | — | — |
| 72 | AssetPEONewWoAllowedFlag | NEW_WO_ALLOWED_FLAG | — | — |
| 73 | AssetPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 74 | AssetPEOOriginationDate | ORIGINATION_DATE | — | ✅ |
| 75 | AssetPEOOwnedBy | OWNED_BY | — | — |
| 76 | AssetPEOProjectId | PROJECT_ID | — | — |
| 77 | AssetPEOPurchaseDate | PURCHASE_DATE | — | ✅ |
| 78 | AssetPEOQuantity | QUANTITY | — | ✅ |
| 79 | AssetPEORegisteredFlag | REGISTERED_FLAG | — | — |
| 80 | AssetPEORequestId | REQUEST_ID | — | ✅ |
| 81 | AssetPEOSalesOrderId | SALES_ORDER_ID | — | ✅ |
| 82 | AssetPEOSalesOrderLineId | SALES_ORDER_LINE_ID | — | ✅ |
| 83 | AssetPEOSecondaryQuantity | SECONDARY_QUANTITY | — | ✅ |
| 84 | AssetPEOSecondaryUomCode | SECONDARY_UOM_CODE | — | ✅ |
| 85 | AssetPEOSerialNumber | SERIAL_NUMBER | — | ✅ |
| 86 | AssetPEOShipmentDate | SHIPMENT_DATE | — | ✅ |
| 87 | AssetPEOSoldByBusinessUnitId | SOLD_BY_BUSINESS_UNIT_ID | — | ✅ |
| 88 | AssetPEOStatusCode | STATUS_CODE | — | — |
| 89 | AssetPEOSubinventoryCode | SUBINVENTORY_CODE | — | — |
| 90 | AssetPEOSupplierId | SUPPLIER_ID | — | ✅ |
| 91 | AssetPEOSupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 92 | AssetPEOTaskId | TASK_ID | — | — |
| 93 | AssetPEOUomCode | UOM_CODE | — | ✅ |
| 94 | AssetPEOUsedBy | USED_BY | — | — |
| 95 | AssetPEOWorkCenterId | WORK_CENTER_ID | — | ✅ |
| 96 | AssetPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 97 | AssetPEOWorkOrderOperationId | WORK_ORDER_OPERATION_ID | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyPEOPartyId | PARTY_ID | — | — |
| 2 | PartyPEOPartyName | PARTY_NAME | — | — |
| 3 | PartyPEOPartyType | PARTY_TYPE | — | — |

### [[inv_item_locations|INV_ITEM_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InventoryLocatorPEOInventoryLocationId | INVENTORY_LOCATION_ID | — | — |
| 2 | InventoryLocatorPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | InventoryLocatorPEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 4 | InventoryLocatorPEOSubinventoryId | SUBINVENTORY_ID | — | — |

### [[wie_work_orders_vl|WIE_WORK_ORDERS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 2 | WorkOrderPEOActualStartDate | ACTUAL_START_DATE | — | ✅ |
| 3 | WorkOrderPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | WorkOrderPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 5 | WorkOrderPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 6 | WorkOrderPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 7 | WorkOrderPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 8 | WorkOrderPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 9 | WorkOrderPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 10 | WorkOrderPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 11 | WorkOrderPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 12 | WorkOrderPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 13 | WorkOrderPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 14 | WorkOrderPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 15 | WorkOrderPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 16 | WorkOrderPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 17 | WorkOrderPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 18 | WorkOrderPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 19 | WorkOrderPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 20 | WorkOrderPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 21 | WorkOrderPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 22 | WorkOrderPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 23 | WorkOrderPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 24 | WorkOrderPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 25 | WorkOrderPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 26 | WorkOrderPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 27 | WorkOrderPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 28 | WorkOrderPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 29 | WorkOrderPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 30 | WorkOrderPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 31 | WorkOrderPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 32 | WorkOrderPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 33 | WorkOrderPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 34 | WorkOrderPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 35 | WorkOrderPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 36 | WorkOrderPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 37 | WorkOrderPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 38 | WorkOrderPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 39 | WorkOrderPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 40 | WorkOrderPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 41 | WorkOrderPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 42 | WorkOrderPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 43 | WorkOrderPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 44 | WorkOrderPEOBackToBackFlag | BACK_TO_BACK_FLAG | — | — |
| 45 | WorkOrderPEOCanceledDate | CANCELED_DATE | — | ✅ |
| 46 | WorkOrderPEOCanceledReason | CANCELED_REASON | — | — |
| 47 | WorkOrderPEOClosedDate | CLOSED_DATE | — | ✅ |
| 48 | WorkOrderPEOCmPoHeaderId | CM_PO_HEADER_ID | — | ✅ |
| 49 | WorkOrderPEOCmPoLineId | CM_PO_LINE_ID | — | ✅ |
| 50 | WorkOrderPEOCmPoLineLocId | CM_PO_LINE_LOC_ID | — | ✅ |
| 51 | WorkOrderPEOComplLocatorId | COMPL_LOCATOR_ID | — | ✅ |
| 52 | WorkOrderPEOComplSubinventoryCode | COMPL_SUBINVENTORY_CODE | — | — |
| 53 | WorkOrderPEOCompletedQuantity | COMPLETED_QUANTITY | — | ✅ |
| 54 | WorkOrderPEOContractMfgFlag | CONTRACT_MFG_FLAG | — | — |
| 55 | WorkOrderPEOCreatedBy | CREATED_BY | — | — |
| 56 | WorkOrderPEOCreationDate | CREATION_DATE | — | ✅ |
| 57 | WorkOrderPEOFirmPlannedFlag | FIRM_PLANNED_FLAG | — | — |
| 58 | WorkOrderPEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 59 | WorkOrderPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 60 | WorkOrderPEOItemRevision | ITEM_REVISION | — | — |
| 61 | WorkOrderPEOItemStructureName | ITEM_STRUCTURE_NAME | — | — |
| 62 | WorkOrderPEOItemVersion | ITEM_VERSION | — | — |
| 63 | WorkOrderPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 64 | WorkOrderPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 65 | WorkOrderPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 66 | WorkOrderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 67 | WorkOrderPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 68 | WorkOrderPEONettableSupplyQtyOverride | NETTABLE_SUPPLY_QTY_OVERRIDE | — | — |
| 69 | WorkOrderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 70 | WorkOrderPEOOrchestrationCode | ORCHESTRATION_CODE | — | — |
| 71 | WorkOrderPEOOrderLessFlag | ORDER_LESS_FLAG | — | — |
| 72 | WorkOrderPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 73 | WorkOrderPEOOvercomplToleranceType | OVERCOMPL_TOLERANCE_TYPE | — | — |
| 74 | WorkOrderPEOOvercomplToleranceValue | OVERCOMPL_TOLERANCE_VALUE | — | — |
| 75 | WorkOrderPEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | ✅ |
| 76 | WorkOrderPEOPlannedStartDate | PLANNED_START_DATE | — | ✅ |
| 77 | WorkOrderPEOPlannedStartQuantity | PLANNED_START_QUANTITY | — | ✅ |
| 78 | WorkOrderPEORejectedQuantity | REJECTED_QUANTITY | — | ✅ |
| 79 | WorkOrderPEOReleasedDate | RELEASED_DATE | — | ✅ |
| 80 | WorkOrderPEORequestId | REQUEST_ID | — | ✅ |
| 81 | WorkOrderPEOSchedulingMethod | SCHEDULING_METHOD | — | — |
| 82 | WorkOrderPEOScoSupplyOrderId | SCO_SUPPLY_ORDER_ID | — | ✅ |
| 83 | WorkOrderPEOScrappedQuantity | SCRAPPED_QUANTITY | — | ✅ |
| 84 | WorkOrderPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | — |
| 85 | WorkOrderPEOSourceHeaderRef | SOURCE_HEADER_REF | — | — |
| 86 | WorkOrderPEOSourceHeaderRefId | SOURCE_HEADER_REF_ID | — | ✅ |
| 87 | WorkOrderPEOSourceLineRef | SOURCE_LINE_REF | — | — |
| 88 | WorkOrderPEOSourceLineRefId | SOURCE_LINE_REF_ID | — | ✅ |
| 89 | WorkOrderPEOSourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 90 | WorkOrderPEOSourceSystemType | SOURCE_SYSTEM_TYPE | — | — |
| 91 | WorkOrderPEOSupplyType | SUPPLY_TYPE | — | — |
| 92 | WorkOrderPEOUomCode | UOM_CODE | — | — |
| 93 | WorkOrderPEOWorkDefinitionAsOfDate | WORK_DEFINITION_AS_OF_DATE | — | ✅ |
| 94 | WorkOrderPEOWorkDefinitionId | WORK_DEFINITION_ID | — | ✅ |
| 95 | WorkOrderPEOWorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | ✅ |
| 96 | WorkOrderPEOWorkMethodId | WORK_METHOD_ID | — | ✅ |
| 97 | WorkOrderPEOWorkOrderDescription | WORK_ORDER_DESCRIPTION | — | — |
| 98 | WorkOrderPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 99 | WorkOrderPEOWorkOrderNumber | WORK_ORDER_NUMBER | — | — |
| 100 | WorkOrderPEOWorkOrderPriority | WORK_ORDER_PRIORITY | — | — |
| 101 | WorkOrderPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | ✅ |
| 102 | WorkOrderPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | — |
| 103 | WorkOrderPEOWorkOrderType | WORK_ORDER_TYPE | — | — |

### [[wie_wo_assets|WIE_WO_ASSETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderAssetPEOAssetId | ASSET_ID | — | ✅ |
| 2 | WorkOrderAssetPEOCreatedBy | CREATED_BY | — | — |
| 3 | WorkOrderAssetPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | WorkOrderAssetPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 5 | WorkOrderAssetPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 6 | WorkOrderAssetPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | WorkOrderAssetPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | WorkOrderAssetPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | WorkOrderAssetPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | WorkOrderAssetPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 11 | WorkOrderAssetPEORequestId | REQUEST_ID | — | ✅ |
| 12 | WorkOrderAssetPEOWoAssetId | WO_ASSET_ID | — | ✅ |
| 13 | WorkOrderAssetPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
