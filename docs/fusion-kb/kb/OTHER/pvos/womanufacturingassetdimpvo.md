---
id: DOC-OTHER-PVO-WOManufacturingAssetDimPVO
doc_type: system-doc
title: "WOManufacturingAssetDimPVO — PVO Cross-Module"
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
  - WOManufacturingAssetDimPVO
  - womanufacturingassetdimpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WOManufacturingAssetDimPVO

## 📌 Visão Geral

View Object para extração BICC de dados de WOManufacturing Asset Dim. Acessa as tabelas: CSE_ASSETS_VL, HR_ALL_ORGANIZATION_UNITS_F_VL, HZ_PARTIES (+4).

**Caminho:** `FscmTopModelAM.WorkOrderAM.WOManufacturingAssetDimPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 166 | 7 | 1 | 10 | 6% |

---

## 🔗 Tabelas Relacionadas

- [[cse_assets_vl|CSE_ASSETS_VL]] — 97 atributos (1 PKs, 6 BICC)
- [[hr_all_organization_units_f_vl|HR_ALL_ORGANIZATION_UNITS_F_VL]] — 21 atributos (3 BICC)
- [[hz_parties|HZ_PARTIES]] — 6 atributos
- [[inv_item_locations|INV_ITEM_LOCATIONS]] — 4 atributos
- [[wie_wo_assets|WIE_WO_ASSETS]] — 13 atributos (1 BICC)
- [[wis_work_areas_vl|WIS_WORK_AREAS_VL]] — 12 atributos
- [[wis_work_centers_vl|WIS_WORK_CENTERS_VL]] — 13 atributos

---

## ⚙️ Atributos

### [[cse_assets_vl|CSE_ASSETS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetPEOActiveEndDate | ACTIVE_END_DATE | — | — |
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
| 49 | AssetPEOCreationDate | CREATION_DATE | — | — |
| 50 | AssetPEOCurrentLocationContext | CURRENT_LOCATION_CONTEXT | — | ✅ |
| 51 | AssetPEOCurrentLocationId | CURRENT_LOCATION_ID | — | — |
| 52 | AssetPEOCustomerId | CUSTOMER_ID | — | — |
| 53 | AssetPEOCustomerSiteId | CUSTOMER_SITE_ID | — | — |
| 54 | AssetPEODescription | DESCRIPTION | — | ✅ |
| 55 | AssetPEODfltWoSubType | DFLT_WO_SUB_TYPE | — | — |
| 56 | AssetPEODfltWoType | DFLT_WO_TYPE | — | — |
| 57 | AssetPEOGenObjectId | GEN_OBJECT_ID | — | — |
| 58 | AssetPEOInServiceDate | IN_SERVICE_DATE | — | — |
| 59 | AssetPEOInstalledDate | INSTALLED_DATE | — | — |
| 60 | AssetPEOInstalledLocationContext | INSTALLED_LOCATION_CONTEXT | — | — |
| 61 | AssetPEOInstalledLocationId | INSTALLED_LOCATION_ID | — | — |
| 62 | AssetPEOInventoryLocatorId | INVENTORY_LOCATOR_ID | — | — |
| 63 | AssetPEOItemId | ITEM_ID | — | — |
| 64 | AssetPEOItemOrganizationId | ITEM_ORGANIZATION_ID | — | — |
| 65 | AssetPEOItemRevision | ITEM_REVISION | — | — |
| 66 | AssetPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 67 | AssetPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 68 | AssetPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 69 | AssetPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 70 | AssetPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 71 | AssetPEOLotNumber | LOT_NUMBER | — | — |
| 72 | AssetPEONewWoAllowedFlag | NEW_WO_ALLOWED_FLAG | — | — |
| 73 | AssetPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 74 | AssetPEOOriginationDate | ORIGINATION_DATE | — | — |
| 75 | AssetPEOOwnedBy | OWNED_BY | — | — |
| 76 | AssetPEOProjectId | PROJECT_ID | — | — |
| 77 | AssetPEOPurchaseDate | PURCHASE_DATE | — | — |
| 78 | AssetPEOQuantity | QUANTITY | — | — |
| 79 | AssetPEORegisteredFlag | REGISTERED_FLAG | — | — |
| 80 | AssetPEORequestId | REQUEST_ID | — | — |
| 81 | AssetPEOSalesOrderId | SALES_ORDER_ID | — | — |
| 82 | AssetPEOSalesOrderLineId | SALES_ORDER_LINE_ID | — | — |
| 83 | AssetPEOSecondaryQuantity | SECONDARY_QUANTITY | — | — |
| 84 | AssetPEOSecondaryUomCode | SECONDARY_UOM_CODE | — | — |
| 85 | AssetPEOSerialNumber | SERIAL_NUMBER | — | ✅ |
| 86 | AssetPEOShipmentDate | SHIPMENT_DATE | — | — |
| 87 | AssetPEOSoldByBusinessUnitId | SOLD_BY_BUSINESS_UNIT_ID | — | — |
| 88 | AssetPEOStatusCode | STATUS_CODE | — | — |
| 89 | AssetPEOSubinventoryCode | SUBINVENTORY_CODE | — | — |
| 90 | AssetPEOSupplierId | SUPPLIER_ID | — | — |
| 91 | AssetPEOSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 92 | AssetPEOTaskId | TASK_ID | — | — |
| 93 | AssetPEOUomCode | UOM_CODE | — | — |
| 94 | AssetPEOUsedBy | USED_BY | — | — |
| 95 | AssetPEOWorkCenterId | WORK_CENTER_ID | — | — |
| 96 | AssetPEOWorkOrderId | WORK_ORDER_ID | — | — |
| 97 | AssetPEOWorkOrderOperationId | WORK_ORDER_OPERATION_ID | — | — |

### [[hr_all_organization_units_f_vl|HR_ALL_ORGANIZATION_UNITS_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationUnitPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | OrganizationUnitPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 3 | OrganizationUnitPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | OrganizationUnitPEOCostAllocationKeyflexId | COST_ALLOCATION_KEYFLEX_ID | — | — |
| 5 | OrganizationUnitPEOCreatedBy | CREATED_BY | — | — |
| 6 | OrganizationUnitPEOCreationDate | CREATION_DATE | — | — |
| 7 | OrganizationUnitPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | OrganizationUnitPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 9 | OrganizationUnitPEOEstablishmentId | ESTABLISHMENT_ID | — | — |
| 10 | OrganizationUnitPEOInternalAddressLine | INTERNAL_ADDRESS_LINE | — | — |
| 11 | OrganizationUnitPEOInternalExternalFlag | INTERNAL_EXTERNAL_FLAG | — | — |
| 12 | OrganizationUnitPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | OrganizationUnitPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | OrganizationUnitPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | OrganizationUnitPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 16 | OrganizationUnitPEOLocationId | LOCATION_ID | — | — |
| 17 | OrganizationUnitPEOName | NAME | — | ✅ |
| 18 | OrganizationUnitPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | OrganizationUnitPEOOrganizationCode | ORGANIZATION_CODE | — | — |
| 20 | OrganizationUnitPEOOrganizationId | ORGANIZATION_ID | — | — |
| 21 | OrganizationUnitPEOType | TYPE | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustomerPartyPEOPartyId | PARTY_ID | — | — |
| 2 | CustomerPartyPEOPartyName | PARTY_NAME | — | — |
| 3 | CustomerPartyPEOPartyType | PARTY_TYPE | — | — |
| 4 | PartyPEOPartyId | PARTY_ID | — | — |
| 5 | PartyPEOPartyName | PARTY_NAME | — | — |
| 6 | PartyPEOPartyType | PARTY_TYPE | — | — |

### [[inv_item_locations|INV_ITEM_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InventoryLocatorPEOInventoryLocationId | INVENTORY_LOCATION_ID | — | — |
| 2 | InventoryLocatorPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | InventoryLocatorPEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 4 | InventoryLocatorPEOSubinventoryId | SUBINVENTORY_ID | — | — |

### [[wie_wo_assets|WIE_WO_ASSETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderAssetPEOAssetId | ASSET_ID | — | — |
| 2 | WorkOrderAssetPEOCreatedBy | CREATED_BY | — | — |
| 3 | WorkOrderAssetPEOCreationDate | CREATION_DATE | — | — |
| 4 | WorkOrderAssetPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 5 | WorkOrderAssetPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 6 | WorkOrderAssetPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | WorkOrderAssetPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | WorkOrderAssetPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | WorkOrderAssetPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | WorkOrderAssetPEOOrganizationId | ORGANIZATION_ID | — | — |
| 11 | WorkOrderAssetPEORequestId | REQUEST_ID | — | — |
| 12 | WorkOrderAssetPEOWoAssetId | WO_ASSET_ID | — | — |
| 13 | WorkOrderAssetPEOWorkOrderId | WORK_ORDER_ID | — | — |

### [[wis_work_areas_vl|WIS_WORK_AREAS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkAreaPEOCreatedBy | CREATED_BY | — | — |
| 2 | WorkAreaPEOCreationDate | CREATION_DATE | — | — |
| 3 | WorkAreaPEOInactiveDate | INACTIVE_DATE | — | — |
| 4 | WorkAreaPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 5 | WorkAreaPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | WorkAreaPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | WorkAreaPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | WorkAreaPEOOrganizationId | ORGANIZATION_ID | — | — |
| 9 | WorkAreaPEOWorkAreaCode | WORK_AREA_CODE | — | — |
| 10 | WorkAreaPEOWorkAreaDescription | WORK_AREA_DESCRIPTION | — | — |
| 11 | WorkAreaPEOWorkAreaId | WORK_AREA_ID | — | — |
| 12 | WorkAreaPEOWorkAreaName | WORK_AREA_NAME | — | — |

### [[wis_work_centers_vl|WIS_WORK_CENTERS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkCenterPEOCreatedBy | CREATED_BY | — | — |
| 2 | WorkCenterPEOCreationDate | CREATION_DATE | — | — |
| 3 | WorkCenterPEOInactiveDate | INACTIVE_DATE | — | — |
| 4 | WorkCenterPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 5 | WorkCenterPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | WorkCenterPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | WorkCenterPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | WorkCenterPEOOrganizationId | ORGANIZATION_ID | — | — |
| 9 | WorkCenterPEOWorkAreaId | WORK_AREA_ID | — | — |
| 10 | WorkCenterPEOWorkCenterCode | WORK_CENTER_CODE | — | — |
| 11 | WorkCenterPEOWorkCenterDescription | WORK_CENTER_DESCRIPTION | — | — |
| 12 | WorkCenterPEOWorkCenterId | WORK_CENTER_ID | — | — |
| 13 | WorkCenterPEOWorkCenterName | WORK_CENTER_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
