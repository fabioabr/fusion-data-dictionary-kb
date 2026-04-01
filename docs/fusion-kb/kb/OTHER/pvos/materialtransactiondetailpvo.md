---
id: DOC-OTHER-PVO-MaterialTransactionDetailPVO
doc_type: system-doc
title: "MaterialTransactionDetailPVO — PVO Cross-Module"
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
  - MaterialTransactionDetailPVO
  - materialtransactiondetailpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MaterialTransactionDetailPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Material Transaction Detail. Acessa as tabelas: INV_RESERVATIONS, INV_TRANSACTION_LOT_NUMBERS, INV_UNIT_TRANSACTIONS (+4).

**Caminho:** `FscmTopModelAM.WOMaterialTransactionsAM.MaterialTransactionDetailPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 284 | 7 | 0 | 72 | 25% |

---

## 🔗 Tabelas Relacionadas

- [[inv_reservations|INV_RESERVATIONS]] — 56 atributos
- [[inv_transaction_lot_numbers|INV_TRANSACTION_LOT_NUMBERS]] — 62 atributos (15 BICC)
- [[inv_unit_transactions|INV_UNIT_TRANSACTIONS]] — 88 atributos (22 BICC)
- [[wie_transaction_serials|WIE_TRANSACTION_SERIALS]] — 17 atributos (9 BICC)
- [[wie_wo_operation_materials|WIE_WO_OPERATION_MATERIALS]] — 33 atributos (23 BICC)
- [[wie_wo_operation_outputs|WIE_WO_OPERATION_OUTPUTS]] — 25 atributos (2 BICC)
- [[wis_work_methods_vl|WIS_WORK_METHODS_VL]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[inv_reservations|INV_RESERVATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EInvReservationsPEOxceptionCode | EXCEPTION_CODE | — | — |
| 2 | InvReservationsPEOContainerLpnId | CONTAINER_LPN_ID | — | — |
| 3 | InvReservationsPEOCrossdockCriteriaId | CROSSDOCK_CRITERIA_ID | — | — |
| 4 | InvReservationsPEOCrossdockFlag | CROSSDOCK_FLAG | — | — |
| 5 | InvReservationsPEODemandShipDate | DEMAND_SHIP_DATE | — | — |
| 6 | InvReservationsPEODemandSourceDelivery | DEMAND_SOURCE_DELIVERY | — | — |
| 7 | InvReservationsPEODemandSourceHeaderId | DEMAND_SOURCE_HEADER_ID | — | — |
| 8 | InvReservationsPEODemandSourceLineDetail | DEMAND_SOURCE_LINE_DETAIL | — | — |
| 9 | InvReservationsPEODemandSourceLineId | DEMAND_SOURCE_LINE_ID | — | — |
| 10 | InvReservationsPEODemandSourceName | DEMAND_SOURCE_NAME | — | — |
| 11 | InvReservationsPEODemandSourceTypeId | DEMAND_SOURCE_TYPE_ID | — | — |
| 12 | InvReservationsPEODetailedQuantity | DETAILED_QUANTITY | — | — |
| 13 | InvReservationsPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 14 | InvReservationsPEOLocatorId | LOCATOR_ID | — | — |
| 15 | InvReservationsPEOLotNumber | LOT_NUMBER | — | — |
| 16 | InvReservationsPEOLpnId | LPN_ID | — | — |
| 17 | InvReservationsPEONColumn | N_COLUMN1 | — | — |
| 18 | InvReservationsPEOOrganizationId | ORGANIZATION_ID | — | — |
| 19 | InvReservationsPEOOrigDemandSourceHeaderId | ORIG_DEMAND_SOURCE_HEADER_ID | — | — |
| 20 | InvReservationsPEOOrigDemandSourceLineDetail | ORIG_DEMAND_SOURCE_LINE_DETAIL | — | — |
| 21 | InvReservationsPEOOrigDemandSourceLineId | ORIG_DEMAND_SOURCE_LINE_ID | — | — |
| 22 | InvReservationsPEOOrigDemandSourceLineNumber | ORIG_DEMAND_SOURCE_LINE_NUMBER | — | — |
| 23 | InvReservationsPEOOrigDemandSourceTypeId | ORIG_DEMAND_SOURCE_TYPE_ID | — | — |
| 24 | InvReservationsPEOOrigSupplySourceHeaderId | ORIG_SUPPLY_SOURCE_HEADER_ID | — | — |
| 25 | InvReservationsPEOOrigSupplySourceLineDetail | ORIG_SUPPLY_SOURCE_LINE_DETAIL | — | — |
| 26 | InvReservationsPEOOrigSupplySourceLineId | ORIG_SUPPLY_SOURCE_LINE_ID | — | — |
| 27 | InvReservationsPEOOrigSupplySourceTypeId | ORIG_SUPPLY_SOURCE_TYPE_ID | — | — |
| 28 | InvReservationsPEOPrimaryReservationQuantity | PRIMARY_RESERVATION_QUANTITY | — | — |
| 29 | InvReservationsPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | — |
| 30 | InvReservationsPEOProjectId | PROJECT_ID | — | — |
| 31 | InvReservationsPEORequestId | REQUEST_ID | — | — |
| 32 | InvReservationsPEORequirementDate | REQUIREMENT_DATE | — | — |
| 33 | InvReservationsPEOReservationQuantity | RESERVATION_QUANTITY | — | — |
| 34 | InvReservationsPEOReservationUomCode | RESERVATION_UOM_CODE | — | — |
| 35 | InvReservationsPEORevision | REVISION | — | — |
| 36 | InvReservationsPEOSalesOrderLineNumber | SALES_ORDER_LINE_NUMBER | — | — |
| 37 | InvReservationsPEOSalesOrderShipmentNumber | SALES_ORDER_SHIPMENT_NUMBER | — | — |
| 38 | InvReservationsPEOSecondaryDetailedQuantity | SECONDARY_DETAILED_QUANTITY | — | — |
| 39 | InvReservationsPEOSecondaryReservationQuantity | SECONDARY_RESERVATION_QUANTITY | — | — |
| 40 | InvReservationsPEOSecondaryUomCode | SECONDARY_UOM_CODE | — | — |
| 41 | InvReservationsPEOSerialReservationQuantity | SERIAL_RESERVATION_QUANTITY | — | — |
| 42 | InvReservationsPEOShipReadyFlag | SHIP_READY_FLAG | — | — |
| 43 | InvReservationsPEOShipToPartyId | SHIP_TO_PARTY_ID | — | — |
| 44 | InvReservationsPEOSourceFulfillmentLineId | SOURCE_FULFILLMENT_LINE_ID | — | — |
| 45 | InvReservationsPEOSourceLineNumber | SOURCE_LINE_NUMBER | — | — |
| 46 | InvReservationsPEOSourceShipmentNumber | SOURCE_SHIPMENT_NUMBER | — | — |
| 47 | InvReservationsPEOStagedFlag | STAGED_FLAG | — | — |
| 48 | InvReservationsPEOSubinventoryCode | SUBINVENTORY_CODE | — | — |
| 49 | InvReservationsPEOSupplyReceiptDate | SUPPLY_RECEIPT_DATE | — | — |
| 50 | InvReservationsPEOSupplySourceHeaderId | SUPPLY_SOURCE_HEADER_ID | — | — |
| 51 | InvReservationsPEOSupplySourceLineDetail | SUPPLY_SOURCE_LINE_DETAIL | — | — |
| 52 | InvReservationsPEOSupplySourceLineId | SUPPLY_SOURCE_LINE_ID | — | — |
| 53 | InvReservationsPEOSupplySourceName | SUPPLY_SOURCE_NAME | — | — |
| 54 | InvReservationsPEOSupplySourceTypeId | SUPPLY_SOURCE_TYPE_ID | — | — |
| 55 | InvReservationsPEOTaskId | TASK_ID | — | — |
| 56 | ReservationId | RESERVATION_ID | — | — |

### [[inv_transaction_lot_numbers|INV_TRANSACTION_LOT_NUMBERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvTransactionLotDetailPEOAge | AGE | — | — |
| 2 | InvTransactionLotDetailPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 3 | InvTransactionLotDetailPEOBestByDate | BEST_BY_DATE | — | ✅ |
| 4 | InvTransactionLotDetailPEOChangeDate | CHANGE_DATE | — | ✅ |
| 5 | InvTransactionLotDetailPEOColor | COLOR | — | — |
| 6 | InvTransactionLotDetailPEOCreatedBy | CREATED_BY | — | — |
| 7 | InvTransactionLotDetailPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | InvTransactionLotDetailPEOCurlWrinkleFold | CURL_WRINKLE_FOLD | — | — |
| 9 | InvTransactionLotDetailPEODateCode | DATE_CODE | — | — |
| 10 | InvTransactionLotDetailPEODescription | DESCRIPTION | — | — |
| 11 | InvTransactionLotDetailPEOExpirationActionCode | EXPIRATION_ACTION_CODE | — | — |
| 12 | InvTransactionLotDetailPEOExpirationActionDate | EXPIRATION_ACTION_DATE | — | — |
| 13 | InvTransactionLotDetailPEOGradeCode | GRADE_CODE | — | — |
| 14 | InvTransactionLotDetailPEOHoldDate | HOLD_DATE | — | ✅ |
| 15 | InvTransactionLotDetailPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 16 | InvTransactionLotDetailPEOItemSize | ITEM_SIZE | — | — |
| 17 | InvTransactionLotDetailPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | InvTransactionLotDetailPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | InvTransactionLotDetailPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | InvTransactionLotDetailPEOLengthUom | LENGTH_UOM | — | — |
| 21 | InvTransactionLotDetailPEOLotAttributeCategory | LOT_ATTRIBUTE_CATEGORY | — | — |
| 22 | InvTransactionLotDetailPEOLotLength | LOT_LENGTH | — | — |
| 23 | InvTransactionLotDetailPEOLotNumber | LOT_NUMBER | — | — |
| 24 | InvTransactionLotDetailPEOLotThickness | LOT_THICKNESS | — | — |
| 25 | InvTransactionLotDetailPEOLotVolume | LOT_VOLUME | — | — |
| 26 | InvTransactionLotDetailPEOLotWidth | LOT_WIDTH | — | — |
| 27 | InvTransactionLotDetailPEOMaturityDate | MATURITY_DATE | — | ✅ |
| 28 | InvTransactionLotDetailPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 29 | InvTransactionLotDetailPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 30 | InvTransactionLotDetailPEOOriginationDate | ORIGINATION_DATE | — | — |
| 31 | InvTransactionLotDetailPEOOriginationType | ORIGINATION_TYPE | — | — |
| 32 | InvTransactionLotDetailPEOParentItemId | PARENT_ITEM_ID | — | — |
| 33 | InvTransactionLotDetailPEOParentLotNumber | PARENT_LOT_NUMBER | — | — |
| 34 | InvTransactionLotDetailPEOParentObjectId | PARENT_OBJECT_ID | — | ✅ |
| 35 | InvTransactionLotDetailPEOParentObjectId2 | PARENT_OBJECT_ID2 | — | ✅ |
| 36 | InvTransactionLotDetailPEOParentObjectNumber | PARENT_OBJECT_NUMBER | — | — |
| 37 | InvTransactionLotDetailPEOParentObjectNumber2 | PARENT_OBJECT_NUMBER2 | — | — |
| 38 | InvTransactionLotDetailPEOParentObjectType | PARENT_OBJECT_TYPE | — | — |
| 39 | InvTransactionLotDetailPEOParentObjectType2 | PARENT_OBJECT_TYPE2 | — | — |
| 40 | InvTransactionLotDetailPEOPlaceOfOrigin | PLACE_OF_ORIGIN | — | — |
| 41 | InvTransactionLotDetailPEOPrimaryQuantity | PRIMARY_QUANTITY | — | — |
| 42 | InvTransactionLotDetailPEOProductCode | PRODUCT_CODE | — | — |
| 43 | InvTransactionLotDetailPEOProductTransactionId | PRODUCT_TRANSACTION_ID | — | — |
| 44 | InvTransactionLotDetailPEOReasonId | REASON_ID | — | — |
| 45 | InvTransactionLotDetailPEORecycledContent | RECYCLED_CONTENT | — | — |
| 46 | InvTransactionLotDetailPEORetestDate | RETEST_DATE | — | ✅ |
| 47 | InvTransactionLotDetailPEOSecondaryTransactionQuantity | SECONDARY_TRANSACTION_QUANTITY | — | — |
| 48 | InvTransactionLotDetailPEOSerialTransactionId | SERIAL_TRANSACTION_ID | — | ✅ |
| 49 | InvTransactionLotDetailPEOStatusId | STATUS_ID | — | ✅ |
| 50 | InvTransactionLotDetailPEOSupplierLotNumber | SUPPLIER_LOT_NUMBER | — | — |
| 51 | InvTransactionLotDetailPEOTerritoryCode | TERRITORY_CODE | — | — |
| 52 | InvTransactionLotDetailPEOThicknessUom | THICKNESS_UOM | — | — |
| 53 | InvTransactionLotDetailPEOTransactionDate | TRANSACTION_DATE | — | — |
| 54 | InvTransactionLotDetailPEOTransactionId | TRANSACTION_ID | — | ✅ |
| 55 | InvTransactionLotDetailPEOTransactionQuantity | TRANSACTION_QUANTITY | — | — |
| 56 | InvTransactionLotDetailPEOTransactionSourceId | TRANSACTION_SOURCE_ID | — | — |
| 57 | InvTransactionLotDetailPEOTransactionSourceName | TRANSACTION_SOURCE_NAME | — | — |
| 58 | InvTransactionLotDetailPEOTransactionSourceTypeId | TRANSACTION_SOURCE_TYPE_ID | — | — |
| 59 | InvTransactionLotDetailPEOVendorId | VENDOR_ID | — | ✅ |
| 60 | InvTransactionLotDetailPEOVendorName | VENDOR_NAME | — | — |
| 61 | InvTransactionLotDetailPEOVolumeUom | VOLUME_UOM | — | — |
| 62 | InvTransactionLotDetailPEOWidthUom | WIDTH_UOM | — | — |

### [[inv_unit_transactions|INV_UNIT_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvLotTransactionSerialPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | InvLotTransactionSerialPEOCreatedBy | CREATED_BY | — | — |
| 3 | InvLotTransactionSerialPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | InvLotTransactionSerialPEOCustomerId | CUSTOMER_ID | — | — |
| 5 | InvLotTransactionSerialPEOCyclesSinceMark | CYCLES_SINCE_MARK | — | — |
| 6 | InvLotTransactionSerialPEOCyclesSinceNew | CYCLES_SINCE_NEW | — | — |
| 7 | InvLotTransactionSerialPEOCyclesSinceOverhaul | CYCLES_SINCE_OVERHAUL | — | — |
| 8 | InvLotTransactionSerialPEOCyclesSinceRepair | CYCLES_SINCE_REPAIR | — | — |
| 9 | InvLotTransactionSerialPEOCyclesSinceVisit | CYCLES_SINCE_VISIT | — | — |
| 10 | InvLotTransactionSerialPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 11 | InvLotTransactionSerialPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | InvLotTransactionSerialPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | InvLotTransactionSerialPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | InvLotTransactionSerialPEOLocatorId | LOCATOR_ID | — | — |
| 15 | InvLotTransactionSerialPEONumberOfRepairs | NUMBER_OF_REPAIRS | — | — |
| 16 | InvLotTransactionSerialPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | InvLotTransactionSerialPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 18 | InvLotTransactionSerialPEOOriginationDate | ORIGINATION_DATE | — | ✅ |
| 19 | InvLotTransactionSerialPEOParentItemId | PARENT_ITEM_ID | — | ✅ |
| 20 | InvLotTransactionSerialPEOParentObjectId | PARENT_OBJECT_ID | — | ✅ |
| 21 | InvLotTransactionSerialPEOParentObjectId2 | PARENT_OBJECT_ID2 | — | ✅ |
| 22 | InvLotTransactionSerialPEOParentObjectNumber | PARENT_OBJECT_NUMBER | — | — |
| 23 | InvLotTransactionSerialPEOParentObjectNumber2 | PARENT_OBJECT_NUMBER2 | — | — |
| 24 | InvLotTransactionSerialPEOParentObjectType | PARENT_OBJECT_TYPE | — | — |
| 25 | InvLotTransactionSerialPEOParentObjectType2 | PARENT_OBJECT_TYPE2 | — | — |
| 26 | InvLotTransactionSerialPEOProductCode | PRODUCT_CODE | — | — |
| 27 | InvLotTransactionSerialPEOProductTransactionId | PRODUCT_TRANSACTION_ID | — | — |
| 28 | InvLotTransactionSerialPEOReceiptIssueType | RECEIPT_ISSUE_TYPE | — | — |
| 29 | InvLotTransactionSerialPEOSerialAttributeCategory | SERIAL_ATTRIBUTE_CATEGORY | — | — |
| 30 | InvLotTransactionSerialPEOSerialNumber | SERIAL_NUMBER | — | — |
| 31 | InvLotTransactionSerialPEOShipId | SHIP_ID | — | — |
| 32 | InvLotTransactionSerialPEOStatusId | STATUS_ID | — | ✅ |
| 33 | InvLotTransactionSerialPEOSubinventoryCode | SUBINVENTORY_CODE | — | — |
| 34 | InvLotTransactionSerialPEOTerritoryCode | TERRITORY_CODE | — | — |
| 35 | InvLotTransactionSerialPEOTimeSinceMark | TIME_SINCE_MARK | — | — |
| 36 | InvLotTransactionSerialPEOTimeSinceNew | TIME_SINCE_NEW | — | — |
| 37 | InvLotTransactionSerialPEOTimeSinceOverhaul | TIME_SINCE_OVERHAUL | — | — |
| 38 | InvLotTransactionSerialPEOTimeSinceRepair | TIME_SINCE_REPAIR | — | — |
| 39 | InvLotTransactionSerialPEOTimeSinceVisit | TIME_SINCE_VISIT | — | — |
| 40 | InvLotTransactionSerialPEOTransactionDate | TRANSACTION_DATE | — | — |
| 41 | InvLotTransactionSerialPEOTransactionId | TRANSACTION_ID | — | ✅ |
| 42 | InvLotTransactionSerialPEOTransactionSourceId | TRANSACTION_SOURCE_ID | — | — |
| 43 | InvLotTransactionSerialPEOTransactionSourceName | TRANSACTION_SOURCE_NAME | — | — |
| 44 | InvLotTransactionSerialPEOTransactionSourceTypeId | TRANSACTION_SOURCE_TYPE_ID | — | — |
| 45 | InvTransactionSerialPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 46 | InvTransactionSerialPEOCreatedBy | CREATED_BY | — | — |
| 47 | InvTransactionSerialPEOCreationDate | CREATION_DATE | — | ✅ |
| 48 | InvTransactionSerialPEOCustomerId | CUSTOMER_ID | — | ✅ |
| 49 | InvTransactionSerialPEOCyclesSinceMark | CYCLES_SINCE_MARK | — | — |
| 50 | InvTransactionSerialPEOCyclesSinceNew | CYCLES_SINCE_NEW | — | — |
| 51 | InvTransactionSerialPEOCyclesSinceOverhaul | CYCLES_SINCE_OVERHAUL | — | — |
| 52 | InvTransactionSerialPEOCyclesSinceRepair | CYCLES_SINCE_REPAIR | — | — |
| 53 | InvTransactionSerialPEOCyclesSinceVisit | CYCLES_SINCE_VISIT | — | — |
| 54 | InvTransactionSerialPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 55 | InvTransactionSerialPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 56 | InvTransactionSerialPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 57 | InvTransactionSerialPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 58 | InvTransactionSerialPEOLocatorId | LOCATOR_ID | — | — |
| 59 | InvTransactionSerialPEONumberOfRepairs | NUMBER_OF_REPAIRS | — | — |
| 60 | InvTransactionSerialPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 61 | InvTransactionSerialPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 62 | InvTransactionSerialPEOOriginationDate | ORIGINATION_DATE | — | — |
| 63 | InvTransactionSerialPEOParentItemId | PARENT_ITEM_ID | — | ✅ |
| 64 | InvTransactionSerialPEOParentObjectId | PARENT_OBJECT_ID | — | ✅ |
| 65 | InvTransactionSerialPEOParentObjectId2 | PARENT_OBJECT_ID2 | — | ✅ |
| 66 | InvTransactionSerialPEOParentObjectNumber | PARENT_OBJECT_NUMBER | — | — |
| 67 | InvTransactionSerialPEOParentObjectNumber2 | PARENT_OBJECT_NUMBER2 | — | — |
| 68 | InvTransactionSerialPEOParentObjectType | PARENT_OBJECT_TYPE | — | — |
| 69 | InvTransactionSerialPEOParentObjectType2 | PARENT_OBJECT_TYPE2 | — | — |
| 70 | InvTransactionSerialPEOProductCode | PRODUCT_CODE | — | — |
| 71 | InvTransactionSerialPEOProductTransactionId | PRODUCT_TRANSACTION_ID | — | ✅ |
| 72 | InvTransactionSerialPEOReceiptIssueType | RECEIPT_ISSUE_TYPE | — | — |
| 73 | InvTransactionSerialPEOSerialAttributeCategory | SERIAL_ATTRIBUTE_CATEGORY | — | — |
| 74 | InvTransactionSerialPEOSerialNumber | SERIAL_NUMBER | — | — |
| 75 | InvTransactionSerialPEOShipId | SHIP_ID | — | ✅ |
| 76 | InvTransactionSerialPEOStatusId | STATUS_ID | — | ✅ |
| 77 | InvTransactionSerialPEOSubinventoryCode | SUBINVENTORY_CODE | — | — |
| 78 | InvTransactionSerialPEOTerritoryCode | TERRITORY_CODE | — | — |
| 79 | InvTransactionSerialPEOTimeSinceMark | TIME_SINCE_MARK | — | — |
| 80 | InvTransactionSerialPEOTimeSinceNew | TIME_SINCE_NEW | — | — |
| 81 | InvTransactionSerialPEOTimeSinceOverhaul | TIME_SINCE_OVERHAUL | — | — |
| 82 | InvTransactionSerialPEOTimeSinceRepair | TIME_SINCE_REPAIR | — | — |
| 83 | InvTransactionSerialPEOTimeSinceVisit | TIME_SINCE_VISIT | — | — |
| 84 | InvTransactionSerialPEOTransactionDate | TRANSACTION_DATE | — | — |
| 85 | InvTransactionSerialPEOTransactionId | TRANSACTION_ID | — | ✅ |
| 86 | InvTransactionSerialPEOTransactionSourceId | TRANSACTION_SOURCE_ID | — | — |
| 87 | InvTransactionSerialPEOTransactionSourceName | TRANSACTION_SOURCE_NAME | — | — |
| 88 | InvTransactionSerialPEOTransactionSourceTypeId | TRANSACTION_SOURCE_TYPE_ID | — | — |

### [[wie_transaction_serials|WIE_TRANSACTION_SERIALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WOTransactionSerialsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | WOTransactionSerialsPEOCreatedBy | CREATED_BY | — | — |
| 3 | WOTransactionSerialsPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | WOTransactionSerialsPEOInterfaceBatchId | INTERFACE_BATCH_ID | — | ✅ |
| 5 | WOTransactionSerialsPEOInterfaceRowId | INTERFACE_ROW_ID | — | ✅ |
| 6 | WOTransactionSerialsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 7 | WOTransactionSerialsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | WOTransactionSerialsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | WOTransactionSerialsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | WOTransactionSerialsPEOLotNumber | LOT_NUMBER | — | — |
| 11 | WOTransactionSerialsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | WOTransactionSerialsPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 13 | WOTransactionSerialsPEOParentSerialNumber | PARENT_SERIAL_NUMBER | — | — |
| 14 | WOTransactionSerialsPEOSerialNumber | SERIAL_NUMBER | — | — |
| 15 | WOTransactionSerialsPEOWoLotTransactionId | WO_LOT_TRANSACTION_ID | — | ✅ |
| 16 | WOTransactionSerialsPEOWoSerialTransactionId | WO_SERIAL_TRANSACTION_ID | — | ✅ |
| 17 | WOTransactionSerialsPEOWoTransactionId | WO_TRANSACTION_ID | — | ✅ |

### [[wie_wo_operation_materials|WIE_WO_OPERATION_MATERIALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WoOperationMaterialsPEOAllocatedQuantity | ALLOCATED_QUANTITY | — | ✅ |
| 2 | WoOperationMaterialsPEOBasisType | BASIS_TYPE | — | ✅ |
| 3 | WoOperationMaterialsPEOCreatedBy | CREATED_BY | — | — |
| 4 | WoOperationMaterialsPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | WoOperationMaterialsPEOIncludeInPlanningFlag | INCLUDE_IN_PLANNING_FLAG | — | ✅ |
| 6 | WoOperationMaterialsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 7 | WoOperationMaterialsPEOInverseQuantity | INVERSE_QUANTITY | — | ✅ |
| 8 | WoOperationMaterialsPEOIssuedQuantity | ISSUED_QUANTITY | — | ✅ |
| 9 | WoOperationMaterialsPEOItemRevision | ITEM_REVISION | — | — |
| 10 | WoOperationMaterialsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 11 | WoOperationMaterialsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 12 | WoOperationMaterialsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | WoOperationMaterialsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | WoOperationMaterialsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | WoOperationMaterialsPEOMaterialSeqNumber | MATERIAL_SEQ_NUMBER | — | ✅ |
| 16 | WoOperationMaterialsPEOMaterialType | MATERIAL_TYPE | — | — |
| 17 | WoOperationMaterialsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | WoOperationMaterialsPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 19 | WoOperationMaterialsPEOPickedQuantity | PICKED_QUANTITY | — | ✅ |
| 20 | WoOperationMaterialsPEOProducedQuantity | PRODUCED_QUANTITY | — | ✅ |
| 21 | WoOperationMaterialsPEOQuantity | QUANTITY | — | ✅ |
| 22 | WoOperationMaterialsPEOQuantityPerProduct | QUANTITY_PER_PRODUCT | — | ✅ |
| 23 | WoOperationMaterialsPEORequestId | REQUEST_ID | — | ✅ |
| 24 | WoOperationMaterialsPEORequiredDate | REQUIRED_DATE | — | ✅ |
| 25 | WoOperationMaterialsPEOSubstituteFlag | SUBSTITUTE_FLAG | — | — |
| 26 | WoOperationMaterialsPEOSupplyLocatorId | SUPPLY_LOCATOR_ID | — | ✅ |
| 27 | WoOperationMaterialsPEOSupplySubinventory | SUPPLY_SUBINVENTORY | — | ✅ |
| 28 | WoOperationMaterialsPEOSupplyType | SUPPLY_TYPE | — | ✅ |
| 29 | WoOperationMaterialsPEOUomCode | UOM_CODE | — | — |
| 30 | WoOperationMaterialsPEOWoOperationId | WO_OPERATION_ID | — | ✅ |
| 31 | WoOperationMaterialsPEOWoOperationMaterialId | WO_OPERATION_MATERIAL_ID | — | ✅ |
| 32 | WoOperationMaterialsPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 33 | WoOperationMaterialsPEOYieldFactor | YIELD_FACTOR | — | ✅ |

### [[wie_wo_operation_outputs|WIE_WO_OPERATION_OUTPUTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderOperationOutputPEOComplLocatorId | COMPL_LOCATOR_ID | — | — |
| 2 | WorkOrderOperationOutputPEOComplSubinventoryCode | COMPL_SUBINVENTORY_CODE | — | — |
| 3 | WorkOrderOperationOutputPEOCompletedQuantity | COMPLETED_QUANTITY | — | — |
| 4 | WorkOrderOperationOutputPEOCompletionType | COMPLETION_TYPE | — | — |
| 5 | WorkOrderOperationOutputPEOCostAllocationPercentage | COST_ALLOCATION_PERCENTAGE | — | — |
| 6 | WorkOrderOperationOutputPEOCreatedBy | CREATED_BY | — | — |
| 7 | WorkOrderOperationOutputPEOCreationDate | CREATION_DATE | — | — |
| 8 | WorkOrderOperationOutputPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 9 | WorkOrderOperationOutputPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 10 | WorkOrderOperationOutputPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 11 | WorkOrderOperationOutputPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | WorkOrderOperationOutputPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | WorkOrderOperationOutputPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | WorkOrderOperationOutputPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | WorkOrderOperationOutputPEOOrganizationId | ORGANIZATION_ID | — | — |
| 16 | WorkOrderOperationOutputPEOOutputQuantity | OUTPUT_QUANTITY | — | ✅ |
| 17 | WorkOrderOperationOutputPEOOutputSeqNumber | OUTPUT_SEQ_NUMBER | — | — |
| 18 | WorkOrderOperationOutputPEOOutputType | OUTPUT_TYPE | — | — |
| 19 | WorkOrderOperationOutputPEOPrimaryFlag | PRIMARY_FLAG | — | — |
| 20 | WorkOrderOperationOutputPEORequestId | REQUEST_ID | — | — |
| 21 | WorkOrderOperationOutputPEOUomCode | UOM_CODE | — | — |
| 22 | WorkOrderOperationOutputPEOWdOperationOutputId | WD_OPERATION_OUTPUT_ID | — | — |
| 23 | WorkOrderOperationOutputPEOWoOperationId | WO_OPERATION_ID | — | — |
| 24 | WorkOrderOperationOutputPEOWoOperationOutputId | WO_OPERATION_OUTPUT_ID | — | — |
| 25 | WorkOrderOperationOutputPEOWorkOrderId | WORK_ORDER_ID | — | — |

### [[wis_work_methods_vl|WIS_WORK_METHODS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkMethodPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | WorkMethodPEOWorkMethodCode | WORK_METHOD_CODE | — | — |
| 3 | WorkMethodPEOWorkMethodId | WORK_METHOD_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
