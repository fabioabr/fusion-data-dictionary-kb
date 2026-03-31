---
id: DOC-OTHER-PVO-InventorySerialRefPVO
doc_type: system-doc
title: "InventorySerialRefPVO — PVO Cross-Module"
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
  - InventorySerialRefPVO
  - inventoryserialrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InventorySerialRefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inventory Serial Ref. Acessa as tabelas: INV_SERIAL_NUMBERS.

**Caminho:** `FscmTopModelAM.InventoryAM.InventorySerialRefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 77 | 1 | 3 | 76 | 99% |

---

## 🔗 Tabelas Relacionadas

- [[inv_serial_numbers|INV_SERIAL_NUMBERS]] — 77 atributos (3 PKs, 76 BICC)

---

## ⚙️ Atributos

### [[inv_serial_numbers|INV_SERIAL_NUMBERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetCriticalityCode | ASSET_CRITICALITY_CODE | — | ✅ |
| 2 | AvailabilityType | AVAILABILITY_TYPE | — | ✅ |
| 3 | CategoryId | CATEGORY_ID | — | ✅ |
| 4 | CompletionDate | COMPLETION_DATE | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | CurrentLocatorId | CURRENT_LOCATOR_ID | — | ✅ |
| 8 | CurrentOrganizationId | CURRENT_ORGANIZATION_ID | 🔑 | ✅ |
| 9 | CurrentStatus | CURRENT_STATUS | — | ✅ |
| 10 | CurrentSubinventoryCode | CURRENT_SUBINVENTORY_CODE | — | ✅ |
| 11 | DependentAssetFlag | DEPENDENT_ASSET_FLAG | — | ✅ |
| 12 | DescriptiveText | DESCRIPTIVE_TEXT | — | ✅ |
| 13 | EamInstantiationFlag | EAM_INSTANTIATION_FLAG | — | ✅ |
| 14 | EamLinearLocationId | EAM_LINEAR_LOCATION_ID | — | ✅ |
| 15 | EamLocationId | EAM_LOCATION_ID | — | ✅ |
| 16 | EndItemUnitNumber | END_ITEM_UNIT_NUMBER | — | ✅ |
| 17 | EqpSerialNumber | EQP_SERIAL_NUMBER | — | ✅ |
| 18 | EquipmentItemId | EQUIPMENT_ITEM_ID | — | ✅ |
| 19 | FaAssetId | FA_ASSET_ID | — | ✅ |
| 20 | FixedAssetTag | FIXED_ASSET_TAG | — | ✅ |
| 21 | GenObjectId | GEN_OBJECT_ID | — | ✅ |
| 22 | GroupMarkId | GROUP_MARK_ID | — | ✅ |
| 23 | InitializationDate | INITIALIZATION_DATE | — | ✅ |
| 24 | InspectionStatus | INSPECTION_STATUS | — | ✅ |
| 25 | IntraoperationStepType | INTRAOPERATION_STEP_TYPE | — | ✅ |
| 26 | InventoryAtpCode | INVENTORY_ATP_CODE | — | ✅ |
| 27 | InventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 28 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 29 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 30 | LastReceiptIssueType | LAST_RECEIPT_ISSUE_TYPE | — | ✅ |
| 31 | LastTransactionId | LAST_TRANSACTION_ID | — | ✅ |
| 32 | LastTxnSourceId | LAST_TXN_SOURCE_ID | — | ✅ |
| 33 | LastTxnSourceName | LAST_TXN_SOURCE_NAME | — | ✅ |
| 34 | LastTxnSourceTypeId | LAST_TXN_SOURCE_TYPE_ID | — | ✅ |
| 35 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 36 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 37 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 38 | LineMarkId | LINE_MARK_ID | — | ✅ |
| 39 | LotLineMarkId | LOT_LINE_MARK_ID | — | ✅ |
| 40 | LotNumber | LOT_NUMBER | — | ✅ |
| 41 | LpnId | LPN_ID | — | ✅ |
| 42 | LpnTxnErrorFlag | LPN_TXN_ERROR_FLAG | — | ✅ |
| 43 | MaintainableFlag | MAINTAINABLE_FLAG | — | ✅ |
| 44 | NetworkAssetFlag | NETWORK_ASSET_FLAG | — | ✅ |
| 45 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 46 | OnhandQuantitiesId | ONHAND_QUANTITIES_ID | — | ✅ |
| 47 | OperationSeqNum | OPERATION_SEQ_NUM | — | ✅ |
| 48 | OperationalLogFlag | OPERATIONAL_LOG_FLAG | — | ✅ |
| 49 | OperationalStatusFlag | OPERATIONAL_STATUS_FLAG | — | ✅ |
| 50 | OrganizationType | ORGANIZATION_TYPE | — | ✅ |
| 51 | OriginalUnitVendorId | ORIGINAL_UNIT_VENDOR_ID | — | ✅ |
| 52 | OriginalWipEntityId | ORIGINAL_WIP_ENTITY_ID | — | ✅ |
| 53 | OriginationDate | ORIGINATION_DATE | — | ✅ |
| 54 | OwningDepartmentId | OWNING_DEPARTMENT_ID | — | ✅ |
| 55 | OwningOrganizationId | OWNING_ORGANIZATION_ID | — | ✅ |
| 56 | OwningTpType | OWNING_TP_TYPE | — | ✅ |
| 57 | ParentItemId | PARENT_ITEM_ID | — | ✅ |
| 58 | ParentLotNumber | PARENT_LOT_NUMBER | — | ✅ |
| 59 | ParentSerialNumber | PARENT_SERIAL_NUMBER | — | ✅ |
| 60 | PlanningOrganizationId | PLANNING_ORGANIZATION_ID | — | ✅ |
| 61 | PlanningTpType | PLANNING_TP_TYPE | — | ✅ |
| 62 | PnLocationId | PN_LOCATION_ID | — | ✅ |
| 63 | PreviousStatus | PREVIOUS_STATUS | — | ✅ |
| 64 | ProdOrganizationId | PROD_ORGANIZATION_ID | — | ✅ |
| 65 | RequestId | REQUEST_ID | — | ✅ |
| 66 | ReservableType | RESERVABLE_TYPE | — | ✅ |
| 67 | ReservationId | RESERVATION_ID | — | ✅ |
| 68 | ReservedOrderId | RESERVED_ORDER_ID | — | ✅ |
| 69 | Revision | REVISION | — | ✅ |
| 70 | SerialNumber | SERIAL_NUMBER | 🔑 | ✅ |
| 71 | ShipDate | SHIP_DATE | — | ✅ |
| 72 | StatusId | STATUS_ID | — | ✅ |
| 73 | UniqueDeviceIdentifier | UNIQUE_DEVICE_IDENTIFIER | — | — |
| 74 | VendorLotNumber | VENDOR_LOT_NUMBER | — | ✅ |
| 75 | VendorSerialNumber | VENDOR_SERIAL_NUMBER | — | ✅ |
| 76 | WipAccountingClassCode | WIP_ACCOUNTING_CLASS_CODE | — | ✅ |
| 77 | WipEntityId | WIP_ENTITY_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
