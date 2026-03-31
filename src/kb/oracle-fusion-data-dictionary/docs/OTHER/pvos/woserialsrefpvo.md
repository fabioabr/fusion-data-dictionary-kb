---
id: DOC-OTHER-PVO-WOSerialsRefPVO
doc_type: system-doc
title: "WOSerialsRefPVO — PVO Cross-Module"
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
  - WOSerialsRefPVO
  - woserialsrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WOSerialsRefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de WOSerials Ref. Acessa as tabelas: INV_SERIAL_NUMBERS, WIE_WO_PRODUCT_SERIALS.

**Caminho:** `FscmTopModelAM.WorkOrderAM.WOSerialsRefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 108 | 2 | 3 | 20 | 19% |

---

## 🔗 Tabelas Relacionadas

- [[inv_serial_numbers|INV_SERIAL_NUMBERS]] — 90 atributos (17 BICC)
- [[wie_wo_product_serials|WIE_WO_PRODUCT_SERIALS]] — 18 atributos (3 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[inv_serial_numbers|INV_SERIAL_NUMBERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvSerialPEOAssetCriticalityCode | ASSET_CRITICALITY_CODE | — | — |
| 2 | InvSerialPEOAvailabilityType | AVAILABILITY_TYPE | — | — |
| 3 | InvSerialPEOCategoryId | CATEGORY_ID | — | — |
| 4 | InvSerialPEOCompletionDate | COMPLETION_DATE | — | ✅ |
| 5 | InvSerialPEOCreatedBy | CREATED_BY | — | — |
| 6 | InvSerialPEOCreationDate | CREATION_DATE | — | — |
| 7 | InvSerialPEOCurrentLocatorId | CURRENT_LOCATOR_ID | — | — |
| 8 | InvSerialPEOCurrentOrganizationId | CURRENT_ORGANIZATION_ID | — | ✅ |
| 9 | InvSerialPEOCurrentStatus | CURRENT_STATUS | — | ✅ |
| 10 | InvSerialPEOCurrentSubinventoryCode | CURRENT_SUBINVENTORY_CODE | — | ✅ |
| 11 | InvSerialPEOCyclesSinceMark | CYCLES_SINCE_MARK | — | — |
| 12 | InvSerialPEOCyclesSinceNew | CYCLES_SINCE_NEW | — | — |
| 13 | InvSerialPEOCyclesSinceOverhaul | CYCLES_SINCE_OVERHAUL | — | — |
| 14 | InvSerialPEOCyclesSinceRepair | CYCLES_SINCE_REPAIR | — | — |
| 15 | InvSerialPEOCyclesSinceVisit | CYCLES_SINCE_VISIT | — | — |
| 16 | InvSerialPEODependentAssetFlag | DEPENDENT_ASSET_FLAG | — | — |
| 17 | InvSerialPEODescriptiveText | DESCRIPTIVE_TEXT | — | — |
| 18 | InvSerialPEOEamInstantiationFlag | EAM_INSTANTIATION_FLAG | — | — |
| 19 | InvSerialPEOEamLinearLocationId | EAM_LINEAR_LOCATION_ID | — | — |
| 20 | InvSerialPEOEamLocationId | EAM_LOCATION_ID | — | — |
| 21 | InvSerialPEOEndItemUnitNumber | END_ITEM_UNIT_NUMBER | — | — |
| 22 | InvSerialPEOEqpSerialNumber | EQP_SERIAL_NUMBER | — | — |
| 23 | InvSerialPEOEquipmentItemId | EQUIPMENT_ITEM_ID | — | — |
| 24 | InvSerialPEOFaAssetId | FA_ASSET_ID | — | — |
| 25 | InvSerialPEOFixedAssetTag | FIXED_ASSET_TAG | — | — |
| 26 | InvSerialPEOGenObjectId | GEN_OBJECT_ID | — | — |
| 27 | InvSerialPEOGroupMarkId | GROUP_MARK_ID | — | — |
| 28 | InvSerialPEOInitializationDate | INITIALIZATION_DATE | — | ✅ |
| 29 | InvSerialPEOInspectionStatus | INSPECTION_STATUS | — | ✅ |
| 30 | InvSerialPEOIntraoperationStepType | INTRAOPERATION_STEP_TYPE | — | — |
| 31 | InvSerialPEOInventoryAtpCode | INVENTORY_ATP_CODE | — | — |
| 32 | InvSerialPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 33 | InvSerialPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 34 | InvSerialPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 35 | InvSerialPEOLastReceiptIssueType | LAST_RECEIPT_ISSUE_TYPE | — | — |
| 36 | InvSerialPEOLastTransactionId | LAST_TRANSACTION_ID | — | — |
| 37 | InvSerialPEOLastTxnSourceId | LAST_TXN_SOURCE_ID | — | — |
| 38 | InvSerialPEOLastTxnSourceName | LAST_TXN_SOURCE_NAME | — | — |
| 39 | InvSerialPEOLastTxnSourceTypeId | LAST_TXN_SOURCE_TYPE_ID | — | — |
| 40 | InvSerialPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 41 | InvSerialPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 42 | InvSerialPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 43 | InvSerialPEOLineMarkId | LINE_MARK_ID | — | — |
| 44 | InvSerialPEOLotLineMarkId | LOT_LINE_MARK_ID | — | — |
| 45 | InvSerialPEOLotNumber | LOT_NUMBER | — | ✅ |
| 46 | InvSerialPEOLpnId | LPN_ID | — | — |
| 47 | InvSerialPEOLpnTxnErrorFlag | LPN_TXN_ERROR_FLAG | — | — |
| 48 | InvSerialPEOMaintainableFlag | MAINTAINABLE_FLAG | — | — |
| 49 | InvSerialPEONetworkAssetFlag | NETWORK_ASSET_FLAG | — | — |
| 50 | InvSerialPEONumberOfRepairs | NUMBER_OF_REPAIRS | — | — |
| 51 | InvSerialPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 52 | InvSerialPEOOnhandQuantitiesId | ONHAND_QUANTITIES_ID | — | — |
| 53 | InvSerialPEOOperationSeqNum | OPERATION_SEQ_NUM | — | — |
| 54 | InvSerialPEOOperationalLogFlag | OPERATIONAL_LOG_FLAG | — | — |
| 55 | InvSerialPEOOperationalStatusFlag | OPERATIONAL_STATUS_FLAG | — | — |
| 56 | InvSerialPEOOrganizationType | ORGANIZATION_TYPE | — | — |
| 57 | InvSerialPEOOriginalUnitVendorId | ORIGINAL_UNIT_VENDOR_ID | — | — |
| 58 | InvSerialPEOOriginalWipEntityId | ORIGINAL_WIP_ENTITY_ID | — | — |
| 59 | InvSerialPEOOriginationDate | ORIGINATION_DATE | — | ✅ |
| 60 | InvSerialPEOOwningDepartmentId | OWNING_DEPARTMENT_ID | — | — |
| 61 | InvSerialPEOOwningOrganizationId | OWNING_ORGANIZATION_ID | — | — |
| 62 | InvSerialPEOOwningTpType | OWNING_TP_TYPE | — | — |
| 63 | InvSerialPEOParentItemId | PARENT_ITEM_ID | — | — |
| 64 | InvSerialPEOParentLotNumber | PARENT_LOT_NUMBER | — | ✅ |
| 65 | InvSerialPEOParentSerialNumber | PARENT_SERIAL_NUMBER | — | ✅ |
| 66 | InvSerialPEOPlanningOrganizationId | PLANNING_ORGANIZATION_ID | — | — |
| 67 | InvSerialPEOPlanningTpType | PLANNING_TP_TYPE | — | — |
| 68 | InvSerialPEOPnLocationId | PN_LOCATION_ID | — | — |
| 69 | InvSerialPEOPreviousStatus | PREVIOUS_STATUS | — | ✅ |
| 70 | InvSerialPEOProdOrganizationId | PROD_ORGANIZATION_ID | — | — |
| 71 | InvSerialPEORequestId | REQUEST_ID | — | — |
| 72 | InvSerialPEOReservableType | RESERVABLE_TYPE | — | — |
| 73 | InvSerialPEOReservationId | RESERVATION_ID | — | — |
| 74 | InvSerialPEOReservedOrderId | RESERVED_ORDER_ID | — | — |
| 75 | InvSerialPEORevision | REVISION | — | — |
| 76 | InvSerialPEOSerialAttributeCategory | SERIAL_ATTRIBUTE_CATEGORY | — | — |
| 77 | InvSerialPEOSerialNumber | SERIAL_NUMBER | — | ✅ |
| 78 | InvSerialPEOShipDate | SHIP_DATE | — | ✅ |
| 79 | InvSerialPEOStatusId | STATUS_ID | — | — |
| 80 | InvSerialPEOTerritoryCode | TERRITORY_CODE | — | — |
| 81 | InvSerialPEOTimeSinceMark | TIME_SINCE_MARK | — | — |
| 82 | InvSerialPEOTimeSinceNew | TIME_SINCE_NEW | — | — |
| 83 | InvSerialPEOTimeSinceOverhaul | TIME_SINCE_OVERHAUL | — | — |
| 84 | InvSerialPEOTimeSinceRepair | TIME_SINCE_REPAIR | — | — |
| 85 | InvSerialPEOTimeSinceVisit | TIME_SINCE_VISIT | — | — |
| 86 | InvSerialPEOUniqueDeviceIdentifier | UNIQUE_DEVICE_IDENTIFIER | — | — |
| 87 | InvSerialPEOVendorLotNumber | VENDOR_LOT_NUMBER | — | ✅ |
| 88 | InvSerialPEOVendorSerialNumber | VENDOR_SERIAL_NUMBER | — | ✅ |
| 89 | InvSerialPEOWipAccountingClassCode | WIP_ACCOUNTING_CLASS_CODE | — | — |
| 90 | InvSerialPEOWipEntityId | WIP_ENTITY_ID | — | — |

### [[wie_wo_product_serials|WIE_WO_PRODUCT_SERIALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProductSerialsPEOCreatedBy | CREATED_BY | — | — |
| 2 | ProductSerialsPEOCreationDate | CREATION_DATE | — | — |
| 3 | ProductSerialsPEOInventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 4 | ProductSerialsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 5 | ProductSerialsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 6 | ProductSerialsPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | ProductSerialsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ProductSerialsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ProductSerialsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ProductSerialsPEOOperationSeqNumber | OPERATION_SEQ_NUMBER | — | — |
| 11 | ProductSerialsPEOOrganizationId | ORGANIZATION_ID | — | — |
| 12 | ProductSerialsPEORequestId | REQUEST_ID | — | — |
| 13 | ProductSerialsPEOSerialNumber | SERIAL_NUMBER | 🔑 | ✅ |
| 14 | ProductSerialsPEOSerialStatus | SERIAL_STATUS | — | — |
| 15 | ProductSerialsPEOWoOperationId | WO_OPERATION_ID | — | — |
| 16 | ProductSerialsPEOWoOperationMaterialId | WO_OPERATION_MATERIAL_ID | — | — |
| 17 | ProductSerialsPEOWoProductSerialId | WO_PRODUCT_SERIAL_ID | 🔑 | ✅ |
| 18 | ProductSerialsPEOWorkOrderId | WORK_ORDER_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
