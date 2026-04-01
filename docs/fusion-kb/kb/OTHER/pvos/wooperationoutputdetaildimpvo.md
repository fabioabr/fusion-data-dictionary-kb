---
id: DOC-OTHER-PVO-WOOperationOutputDetailDimPVO
doc_type: system-doc
title: "WOOperationOutputDetailDimPVO — PVO Cross-Module"
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
  - WOOperationOutputDetailDimPVO
  - wooperationoutputdetaildimpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WOOperationOutputDetailDimPVO

## 📌 Visão Geral

View Object para extração BICC de dados de WOOperation Output Detail Dim. Acessa as tabelas: INV_ITEM_LOCATIONS, WIE_WO_OPERATIONS_B, WIE_WO_OPERATION_OUTPUTS.

**Caminho:** `FscmTopModelAM.WorkOrderAM.WOOperationOutputDetailDimPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 245 | 3 | 1 | 11 | 4% |

---

## 🔗 Tabelas Relacionadas

- [[inv_item_locations|INV_ITEM_LOCATIONS]] — 95 atributos (1 BICC)
- [[wie_wo_operations_b|WIE_WO_OPERATIONS_B]] — 84 atributos (1 BICC)
- [[wie_wo_operation_outputs|WIE_WO_OPERATION_OUTPUTS]] — 66 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[inv_item_locations|INV_ITEM_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InventoryLocatorPEOAlias | ALIAS | — | — |
| 2 | InventoryLocatorPEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | InventoryLocatorPEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | InventoryLocatorPEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | InventoryLocatorPEOAttribute12 | ATTRIBUTE12 | — | — |
| 6 | InventoryLocatorPEOAttribute13 | ATTRIBUTE13 | — | — |
| 7 | InventoryLocatorPEOAttribute14 | ATTRIBUTE14 | — | — |
| 8 | InventoryLocatorPEOAttribute15 | ATTRIBUTE15 | — | — |
| 9 | InventoryLocatorPEOAttribute2 | ATTRIBUTE2 | — | — |
| 10 | InventoryLocatorPEOAttribute3 | ATTRIBUTE3 | — | — |
| 11 | InventoryLocatorPEOAttribute4 | ATTRIBUTE4 | — | — |
| 12 | InventoryLocatorPEOAttribute5 | ATTRIBUTE5 | — | — |
| 13 | InventoryLocatorPEOAttribute6 | ATTRIBUTE6 | — | — |
| 14 | InventoryLocatorPEOAttribute7 | ATTRIBUTE7 | — | — |
| 15 | InventoryLocatorPEOAttribute8 | ATTRIBUTE8 | — | — |
| 16 | InventoryLocatorPEOAttribute9 | ATTRIBUTE9 | — | — |
| 17 | InventoryLocatorPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 18 | InventoryLocatorPEOAvailabilityType | AVAILABILITY_TYPE | — | — |
| 19 | InventoryLocatorPEOAvailableCubicArea | AVAILABLE_CUBIC_AREA | — | — |
| 20 | InventoryLocatorPEOAvailableWeight | AVAILABLE_WEIGHT | — | — |
| 21 | InventoryLocatorPEOCreatedBy | CREATED_BY | — | — |
| 22 | InventoryLocatorPEOCreationDate | CREATION_DATE | — | — |
| 23 | InventoryLocatorPEOCurrentCubicArea | CURRENT_CUBIC_AREA | — | — |
| 24 | InventoryLocatorPEOCurrentWeight | CURRENT_WEIGHT | — | — |
| 25 | InventoryLocatorPEODepreciableFlag | DEPRECIABLE_FLAG | — | — |
| 26 | InventoryLocatorPEODescription | DESCRIPTION | — | — |
| 27 | InventoryLocatorPEODimensionUomCode | DIMENSION_UOM_CODE | — | — |
| 28 | InventoryLocatorPEODisableDate | DISABLE_DATE | — | — |
| 29 | InventoryLocatorPEODroppingOrder | DROPPING_ORDER | — | — |
| 30 | InventoryLocatorPEOEmptyFlag | EMPTY_FLAG | — | — |
| 31 | InventoryLocatorPEOEnabledFlag | ENABLED_FLAG | — | — |
| 32 | InventoryLocatorPEOEndDateActive | END_DATE_ACTIVE | — | — |
| 33 | InventoryLocatorPEOInventoryAtpCode | INVENTORY_ATP_CODE | — | — |
| 34 | InventoryLocatorPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 35 | InventoryLocatorPEOInventoryLocationId | INVENTORY_LOCATION_ID | — | — |
| 36 | InventoryLocatorPEOInventoryLocationType | INVENTORY_LOCATION_TYPE | — | — |
| 37 | InventoryLocatorPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 38 | InventoryLocatorPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 39 | InventoryLocatorPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 40 | InventoryLocatorPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 41 | InventoryLocatorPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 42 | InventoryLocatorPEOLocationAvailableUnits | LOCATION_AVAILABLE_UNITS | — | — |
| 43 | InventoryLocatorPEOLocationCurrentUnits | LOCATION_CURRENT_UNITS | — | — |
| 44 | InventoryLocatorPEOLocationHeight | LOCATION_HEIGHT | — | — |
| 45 | InventoryLocatorPEOLocationLength | LOCATION_LENGTH | — | — |
| 46 | InventoryLocatorPEOLocationMaximumUnits | LOCATION_MAXIMUM_UNITS | — | — |
| 47 | InventoryLocatorPEOLocationSuggestedUnits | LOCATION_SUGGESTED_UNITS | — | — |
| 48 | InventoryLocatorPEOLocationWeightUomCode | LOCATION_WEIGHT_UOM_CODE | — | — |
| 49 | InventoryLocatorPEOLocationWidth | LOCATION_WIDTH | — | — |
| 50 | InventoryLocatorPEOLocatorStatus | LOCATOR_STATUS | — | — |
| 51 | InventoryLocatorPEOMaxCubicArea | MAX_CUBIC_AREA | — | — |
| 52 | InventoryLocatorPEOMaxWeight | MAX_WEIGHT | — | — |
| 53 | InventoryLocatorPEOMixedItemsFlag | MIXED_ITEMS_FLAG | — | — |
| 54 | InventoryLocatorPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 55 | InventoryLocatorPEOOrganizationId | ORGANIZATION_ID | — | — |
| 56 | InventoryLocatorPEOPhysicalLocationCode | PHYSICAL_LOCATION_CODE | — | — |
| 57 | InventoryLocatorPEOPhysicalLocationId | PHYSICAL_LOCATION_ID | — | — |
| 58 | InventoryLocatorPEOPickUomCode | PICK_UOM_CODE | — | — |
| 59 | InventoryLocatorPEOPickingOrder | PICKING_ORDER | — | — |
| 60 | InventoryLocatorPEOProjectId | PROJECT_ID | — | — |
| 61 | InventoryLocatorPEORequestId | REQUEST_ID | — | — |
| 62 | InventoryLocatorPEOReservableType | RESERVABLE_TYPE | — | — |
| 63 | InventoryLocatorPEOSegment1 | SEGMENT1 | — | — |
| 64 | InventoryLocatorPEOSegment10 | SEGMENT10 | — | — |
| 65 | InventoryLocatorPEOSegment11 | SEGMENT11 | — | — |
| 66 | InventoryLocatorPEOSegment12 | SEGMENT12 | — | — |
| 67 | InventoryLocatorPEOSegment13 | SEGMENT13 | — | — |
| 68 | InventoryLocatorPEOSegment14 | SEGMENT14 | — | — |
| 69 | InventoryLocatorPEOSegment15 | SEGMENT15 | — | — |
| 70 | InventoryLocatorPEOSegment16 | SEGMENT16 | — | — |
| 71 | InventoryLocatorPEOSegment17 | SEGMENT17 | — | — |
| 72 | InventoryLocatorPEOSegment18 | SEGMENT18 | — | — |
| 73 | InventoryLocatorPEOSegment19 | SEGMENT19 | — | — |
| 74 | InventoryLocatorPEOSegment2 | SEGMENT2 | — | — |
| 75 | InventoryLocatorPEOSegment20 | SEGMENT20 | — | — |
| 76 | InventoryLocatorPEOSegment3 | SEGMENT3 | — | — |
| 77 | InventoryLocatorPEOSegment4 | SEGMENT4 | — | — |
| 78 | InventoryLocatorPEOSegment5 | SEGMENT5 | — | — |
| 79 | InventoryLocatorPEOSegment6 | SEGMENT6 | — | — |
| 80 | InventoryLocatorPEOSegment7 | SEGMENT7 | — | — |
| 81 | InventoryLocatorPEOSegment8 | SEGMENT8 | — | — |
| 82 | InventoryLocatorPEOSegment9 | SEGMENT9 | — | — |
| 83 | InventoryLocatorPEOStartDateActive | START_DATE_ACTIVE | — | — |
| 84 | InventoryLocatorPEOStatusId | STATUS_ID | — | — |
| 85 | InventoryLocatorPEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 86 | InventoryLocatorPEOSubinventoryCode | SUBINVENTORY_CODE | — | — |
| 87 | InventoryLocatorPEOSubinventoryId | SUBINVENTORY_ID | — | — |
| 88 | InventoryLocatorPEOSuggestedCubicArea | SUGGESTED_CUBIC_AREA | — | — |
| 89 | InventoryLocatorPEOSuggestedWeight | SUGGESTED_WEIGHT | — | — |
| 90 | InventoryLocatorPEOSummaryFlag | SUMMARY_FLAG | — | — |
| 91 | InventoryLocatorPEOTaskId | TASK_ID | — | — |
| 92 | InventoryLocatorPEOVolumeUomCode | VOLUME_UOM_CODE | — | — |
| 93 | InventoryLocatorPEOXCoordinate | X_COORDINATE | — | — |
| 94 | InventoryLocatorPEOYCoordinate | Y_COORDINATE | — | — |
| 95 | InventoryLocatorPEOZCoordinate | Z_COORDINATE | — | — |

### [[wie_wo_operations_b|WIE_WO_OPERATIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WOOperationAnalyticsPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
| 2 | WOOperationAnalyticsPEOActualStartDate | ACTUAL_START_DATE | — | — |
| 3 | WOOperationAnalyticsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | WOOperationAnalyticsPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 5 | WOOperationAnalyticsPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 6 | WOOperationAnalyticsPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 7 | WOOperationAnalyticsPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 8 | WOOperationAnalyticsPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 9 | WOOperationAnalyticsPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 10 | WOOperationAnalyticsPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 11 | WOOperationAnalyticsPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 12 | WOOperationAnalyticsPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 13 | WOOperationAnalyticsPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 14 | WOOperationAnalyticsPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 15 | WOOperationAnalyticsPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 16 | WOOperationAnalyticsPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 17 | WOOperationAnalyticsPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 18 | WOOperationAnalyticsPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 19 | WOOperationAnalyticsPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 20 | WOOperationAnalyticsPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 21 | WOOperationAnalyticsPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 22 | WOOperationAnalyticsPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 23 | WOOperationAnalyticsPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 24 | WOOperationAnalyticsPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 25 | WOOperationAnalyticsPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 26 | WOOperationAnalyticsPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 27 | WOOperationAnalyticsPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 28 | WOOperationAnalyticsPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 29 | WOOperationAnalyticsPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 30 | WOOperationAnalyticsPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 31 | WOOperationAnalyticsPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 32 | WOOperationAnalyticsPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 33 | WOOperationAnalyticsPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 34 | WOOperationAnalyticsPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 35 | WOOperationAnalyticsPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 36 | WOOperationAnalyticsPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 37 | WOOperationAnalyticsPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 38 | WOOperationAnalyticsPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 39 | WOOperationAnalyticsPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 40 | WOOperationAnalyticsPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 41 | WOOperationAnalyticsPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 42 | WOOperationAnalyticsPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 43 | WOOperationAnalyticsPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 44 | WOOperationAnalyticsPEOAutoTransactFlag | AUTO_TRANSACT_FLAG | — | — |
| 45 | WOOperationAnalyticsPEOCompletedQuantity | COMPLETED_QUANTITY | — | — |
| 46 | WOOperationAnalyticsPEOCountPointOperationFlag | COUNT_POINT_OPERATION_FLAG | — | — |
| 47 | WOOperationAnalyticsPEOCreatedBy | CREATED_BY | — | — |
| 48 | WOOperationAnalyticsPEOCreationDate | CREATION_DATE | — | — |
| 49 | WOOperationAnalyticsPEOFixedLeadTime | FIXED_LEAD_TIME | — | — |
| 50 | WOOperationAnalyticsPEOInProcessQuantity | IN_PROCESS_QUANTITY | — | — |
| 51 | WOOperationAnalyticsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 52 | WOOperationAnalyticsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 53 | WOOperationAnalyticsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 54 | WOOperationAnalyticsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 55 | WOOperationAnalyticsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 56 | WOOperationAnalyticsPEOLeadTimeUom | LEAD_TIME_UOM | — | — |
| 57 | WOOperationAnalyticsPEONextCpOpSeqNum | NEXT_CP_OP_SEQ_NUM | — | — |
| 58 | WOOperationAnalyticsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 59 | WOOperationAnalyticsPEOOperationSeqNumber | OPERATION_SEQ_NUMBER | — | — |
| 60 | WOOperationAnalyticsPEOOperationType | OPERATION_TYPE | — | — |
| 61 | WOOperationAnalyticsPEOOrganizationId | ORGANIZATION_ID | — | — |
| 62 | WOOperationAnalyticsPEOOspItemId | OSP_ITEM_ID | — | — |
| 63 | WOOperationAnalyticsPEOOverReceiptQuantity | OVER_RECEIPT_QUANTITY | — | — |
| 64 | WOOperationAnalyticsPEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | — |
| 65 | WOOperationAnalyticsPEOPlannedStartDate | PLANNED_START_DATE | — | — |
| 66 | WOOperationAnalyticsPEOPoApprovedQuantity | PO_APPROVED_QUANTITY | — | — |
| 67 | WOOperationAnalyticsPEOPoRequestedQuantity | PO_REQUESTED_QUANTITY | — | — |
| 68 | WOOperationAnalyticsPEOPreviousCpOpSeqNum | PREVIOUS_CP_OP_SEQ_NUM | — | — |
| 69 | WOOperationAnalyticsPEOReadyQuantity | READY_QUANTITY | — | — |
| 70 | WOOperationAnalyticsPEOReceivedQuantity | RECEIVED_QUANTITY | — | — |
| 71 | WOOperationAnalyticsPEORejectedQuantity | REJECTED_QUANTITY | — | — |
| 72 | WOOperationAnalyticsPEORequestId | REQUEST_ID | — | — |
| 73 | WOOperationAnalyticsPEOScrappedQuantity | SCRAPPED_QUANTITY | — | — |
| 74 | WOOperationAnalyticsPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | — |
| 75 | WOOperationAnalyticsPEOShippedQuantity | SHIPPED_QUANTITY | — | — |
| 76 | WOOperationAnalyticsPEOShippingDocumentsFlag | SHIPPING_DOCUMENTS_FLAG | — | — |
| 77 | WOOperationAnalyticsPEOStandardOperationId | STANDARD_OPERATION_ID | — | — |
| 78 | WOOperationAnalyticsPEOSupplierId | SUPPLIER_ID | — | — |
| 79 | WOOperationAnalyticsPEOSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 80 | WOOperationAnalyticsPEOVariableLeadTime | VARIABLE_LEAD_TIME | — | — |
| 81 | WOOperationAnalyticsPEOWdOperationId | WD_OPERATION_ID | — | — |
| 82 | WOOperationAnalyticsPEOWoOperationId | WO_OPERATION_ID | — | — |
| 83 | WOOperationAnalyticsPEOWorkCenterId | WORK_CENTER_ID | — | — |
| 84 | WOOperationAnalyticsPEOWorkOrderId | WORK_ORDER_ID | — | — |

### [[wie_wo_operation_outputs|WIE_WO_OPERATION_OUTPUTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderOperationOutputPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | WorkOrderOperationOutputPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 3 | WorkOrderOperationOutputPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 4 | WorkOrderOperationOutputPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 5 | WorkOrderOperationOutputPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 6 | WorkOrderOperationOutputPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 7 | WorkOrderOperationOutputPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 8 | WorkOrderOperationOutputPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 9 | WorkOrderOperationOutputPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 10 | WorkOrderOperationOutputPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 11 | WorkOrderOperationOutputPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 12 | WorkOrderOperationOutputPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 13 | WorkOrderOperationOutputPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 14 | WorkOrderOperationOutputPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 15 | WorkOrderOperationOutputPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 16 | WorkOrderOperationOutputPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 17 | WorkOrderOperationOutputPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 18 | WorkOrderOperationOutputPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 19 | WorkOrderOperationOutputPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 20 | WorkOrderOperationOutputPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 21 | WorkOrderOperationOutputPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 22 | WorkOrderOperationOutputPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | WorkOrderOperationOutputPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 24 | WorkOrderOperationOutputPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 25 | WorkOrderOperationOutputPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 26 | WorkOrderOperationOutputPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 27 | WorkOrderOperationOutputPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 28 | WorkOrderOperationOutputPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 29 | WorkOrderOperationOutputPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 30 | WorkOrderOperationOutputPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 31 | WorkOrderOperationOutputPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 32 | WorkOrderOperationOutputPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 33 | WorkOrderOperationOutputPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 34 | WorkOrderOperationOutputPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 35 | WorkOrderOperationOutputPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 36 | WorkOrderOperationOutputPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 37 | WorkOrderOperationOutputPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 38 | WorkOrderOperationOutputPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 39 | WorkOrderOperationOutputPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 40 | WorkOrderOperationOutputPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 41 | WorkOrderOperationOutputPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 42 | WorkOrderOperationOutputPEOComplLocatorId | COMPL_LOCATOR_ID | — | — |
| 43 | WorkOrderOperationOutputPEOComplSubinventoryCode | COMPL_SUBINVENTORY_CODE | — | ✅ |
| 44 | WorkOrderOperationOutputPEOCompletedQuantity | COMPLETED_QUANTITY | — | — |
| 45 | WorkOrderOperationOutputPEOCompletionType | COMPLETION_TYPE | — | ✅ |
| 46 | WorkOrderOperationOutputPEOCostAllocationPercentage | COST_ALLOCATION_PERCENTAGE | — | ✅ |
| 47 | WorkOrderOperationOutputPEOCreatedBy | CREATED_BY | — | — |
| 48 | WorkOrderOperationOutputPEOCreationDate | CREATION_DATE | — | — |
| 49 | WorkOrderOperationOutputPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 50 | WorkOrderOperationOutputPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 51 | WorkOrderOperationOutputPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 52 | WorkOrderOperationOutputPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 53 | WorkOrderOperationOutputPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 54 | WorkOrderOperationOutputPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 55 | WorkOrderOperationOutputPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 56 | WorkOrderOperationOutputPEOOrganizationId | ORGANIZATION_ID | — | — |
| 57 | WorkOrderOperationOutputPEOOutputQuantity | OUTPUT_QUANTITY | — | — |
| 58 | WorkOrderOperationOutputPEOOutputSeqNumber | OUTPUT_SEQ_NUMBER | — | ✅ |
| 59 | WorkOrderOperationOutputPEOOutputType | OUTPUT_TYPE | — | ✅ |
| 60 | WorkOrderOperationOutputPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 61 | WorkOrderOperationOutputPEORequestId | REQUEST_ID | — | — |
| 62 | WorkOrderOperationOutputPEOUomCode | UOM_CODE | — | ✅ |
| 63 | WorkOrderOperationOutputPEOWdOperationOutputId | WD_OPERATION_OUTPUT_ID | — | — |
| 64 | WorkOrderOperationOutputPEOWoOperationId | WO_OPERATION_ID | — | — |
| 65 | WorkOrderOperationOutputPEOWoOperationOutputId | WO_OPERATION_OUTPUT_ID | 🔑 | ✅ |
| 66 | WorkOrderOperationOutputPEOWorkOrderId | WORK_ORDER_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
