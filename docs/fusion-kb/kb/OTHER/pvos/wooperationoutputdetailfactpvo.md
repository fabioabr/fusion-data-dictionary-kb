---
id: DOC-OTHER-PVO-WOOperationOutputDetailFactPVO
doc_type: system-doc
title: "WOOperationOutputDetailFactPVO — PVO Cross-Module"
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
  - WOOperationOutputDetailFactPVO
  - wooperationoutputdetailfactpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WOOperationOutputDetailFactPVO

## 📌 Visão Geral

View Object para extração BICC de dados de WOOperation Output Detail Fact. Acessa as tabelas: INV_ITEM_LOCATIONS, WIE_WORK_ORDERS_B, WIE_WO_OPERATIONS_B (+1).

**Caminho:** `FscmTopModelAM.WorkOrderAM.WOOperationOutputDetailFactPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 343 | 4 | 3 | 17 | 5% |

---

## 🔗 Tabelas Relacionadas

- [[inv_item_locations|INV_ITEM_LOCATIONS]] — 95 atributos (1 BICC)
- [[wie_work_orders_b|WIE_WORK_ORDERS_B]] — 139 atributos (1 BICC)
- [[wie_wo_operations_b|WIE_WO_OPERATIONS_B]] — 84 atributos (1 BICC)
- [[wie_wo_op_output_detail_v|WIE_WO_OP_OUTPUT_DETAIL_V]] — 25 atributos (3 PKs, 14 BICC)

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
| 55 | InventoryLocatorPEOOrganizationId3 | ORGANIZATION_ID | — | — |
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

### [[wie_work_orders_b|WIE_WORK_ORDERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderAnalyticsPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
| 2 | WorkOrderAnalyticsPEOActualStartDate | ACTUAL_START_DATE | — | — |
| 3 | WorkOrderAnalyticsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | WorkOrderAnalyticsPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 5 | WorkOrderAnalyticsPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 6 | WorkOrderAnalyticsPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 7 | WorkOrderAnalyticsPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 8 | WorkOrderAnalyticsPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 9 | WorkOrderAnalyticsPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 10 | WorkOrderAnalyticsPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 11 | WorkOrderAnalyticsPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 12 | WorkOrderAnalyticsPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 13 | WorkOrderAnalyticsPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 14 | WorkOrderAnalyticsPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 15 | WorkOrderAnalyticsPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 16 | WorkOrderAnalyticsPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 17 | WorkOrderAnalyticsPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 18 | WorkOrderAnalyticsPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 19 | WorkOrderAnalyticsPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 20 | WorkOrderAnalyticsPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 21 | WorkOrderAnalyticsPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 22 | WorkOrderAnalyticsPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 23 | WorkOrderAnalyticsPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 24 | WorkOrderAnalyticsPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 25 | WorkOrderAnalyticsPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 26 | WorkOrderAnalyticsPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 27 | WorkOrderAnalyticsPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 28 | WorkOrderAnalyticsPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 29 | WorkOrderAnalyticsPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 30 | WorkOrderAnalyticsPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 31 | WorkOrderAnalyticsPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 32 | WorkOrderAnalyticsPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 33 | WorkOrderAnalyticsPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 34 | WorkOrderAnalyticsPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 35 | WorkOrderAnalyticsPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 36 | WorkOrderAnalyticsPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 37 | WorkOrderAnalyticsPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 38 | WorkOrderAnalyticsPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 39 | WorkOrderAnalyticsPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 40 | WorkOrderAnalyticsPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 41 | WorkOrderAnalyticsPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 42 | WorkOrderAnalyticsPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 43 | WorkOrderAnalyticsPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 44 | WorkOrderAnalyticsPEOBackToBackFlag | BACK_TO_BACK_FLAG | — | — |
| 45 | WorkOrderAnalyticsPEOCanceledDate | CANCELED_DATE | — | — |
| 46 | WorkOrderAnalyticsPEOCanceledReason | CANCELED_REASON | — | — |
| 47 | WorkOrderAnalyticsPEOClosedDate | CLOSED_DATE | — | — |
| 48 | WorkOrderAnalyticsPEOCmPoHeaderId | CM_PO_HEADER_ID | — | — |
| 49 | WorkOrderAnalyticsPEOCmPoLineId | CM_PO_LINE_ID | — | — |
| 50 | WorkOrderAnalyticsPEOCmPoLineLocId | CM_PO_LINE_LOC_ID | — | — |
| 51 | WorkOrderAnalyticsPEOComplLocatorId | COMPL_LOCATOR_ID | — | — |
| 52 | WorkOrderAnalyticsPEOComplSubinventoryCode | COMPL_SUBINVENTORY_CODE | — | — |
| 53 | WorkOrderAnalyticsPEOCompletedQuantity | COMPLETED_QUANTITY | — | — |
| 54 | WorkOrderAnalyticsPEOContractMfgFlag | CONTRACT_MFG_FLAG | — | — |
| 55 | WorkOrderAnalyticsPEOCreatedBy | CREATED_BY | — | — |
| 56 | WorkOrderAnalyticsPEOCreationDate | CREATION_DATE | — | — |
| 57 | WorkOrderAnalyticsPEOFirmPlannedFlag | FIRM_PLANNED_FLAG | — | — |
| 58 | WorkOrderAnalyticsPEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 59 | WorkOrderAnalyticsPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 60 | WorkOrderAnalyticsPEOItemRevision | ITEM_REVISION | — | — |
| 61 | WorkOrderAnalyticsPEOItemStructureName | ITEM_STRUCTURE_NAME | — | — |
| 62 | WorkOrderAnalyticsPEOItemVersion | ITEM_VERSION | — | — |
| 63 | WorkOrderAnalyticsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 64 | WorkOrderAnalyticsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 65 | WorkOrderAnalyticsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 66 | WorkOrderAnalyticsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 67 | WorkOrderAnalyticsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 68 | WorkOrderAnalyticsPEONettableSupplyQtyOverride | NETTABLE_SUPPLY_QTY_OVERRIDE | — | — |
| 69 | WorkOrderAnalyticsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 70 | WorkOrderAnalyticsPEOOrchestrationCode | ORCHESTRATION_CODE | — | — |
| 71 | WorkOrderAnalyticsPEOOrderLessFlag | ORDER_LESS_FLAG | — | — |
| 72 | WorkOrderAnalyticsPEOOrganizationId | ORGANIZATION_ID | — | — |
| 73 | WorkOrderAnalyticsPEOOvercomplToleranceType | OVERCOMPL_TOLERANCE_TYPE | — | — |
| 74 | WorkOrderAnalyticsPEOOvercomplToleranceValue | OVERCOMPL_TOLERANCE_VALUE | — | — |
| 75 | WorkOrderAnalyticsPEOPjcBillableFlag | PJC_BILLABLE_FLAG | — | — |
| 76 | WorkOrderAnalyticsPEOPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | — |
| 77 | WorkOrderAnalyticsPEOPjcContextCategory | PJC_CONTEXT_CATEGORY | — | — |
| 78 | WorkOrderAnalyticsPEOPjcContractId | PJC_CONTRACT_ID | — | — |
| 79 | WorkOrderAnalyticsPEOPjcContractLineId | PJC_CONTRACT_LINE_ID | — | — |
| 80 | WorkOrderAnalyticsPEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 81 | WorkOrderAnalyticsPEOPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | — |
| 82 | WorkOrderAnalyticsPEOPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | — |
| 83 | WorkOrderAnalyticsPEOPjcOrganizationId | PJC_ORGANIZATION_ID | — | — |
| 84 | WorkOrderAnalyticsPEOPjcProjectId | PJC_PROJECT_ID | — | — |
| 85 | WorkOrderAnalyticsPEOPjcProjectNumber | PJC_PROJECT_NUMBER | — | — |
| 86 | WorkOrderAnalyticsPEOPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 87 | WorkOrderAnalyticsPEOPjcReservedAttribute10 | PJC_RESERVED_ATTRIBUTE10 | — | — |
| 88 | WorkOrderAnalyticsPEOPjcReservedAttribute2 | PJC_RESERVED_ATTRIBUTE2 | — | — |
| 89 | WorkOrderAnalyticsPEOPjcReservedAttribute3 | PJC_RESERVED_ATTRIBUTE3 | — | — |
| 90 | WorkOrderAnalyticsPEOPjcReservedAttribute4 | PJC_RESERVED_ATTRIBUTE4 | — | — |
| 91 | WorkOrderAnalyticsPEOPjcReservedAttribute5 | PJC_RESERVED_ATTRIBUTE5 | — | — |
| 92 | WorkOrderAnalyticsPEOPjcReservedAttribute6 | PJC_RESERVED_ATTRIBUTE6 | — | — |
| 93 | WorkOrderAnalyticsPEOPjcReservedAttribute7 | PJC_RESERVED_ATTRIBUTE7 | — | — |
| 94 | WorkOrderAnalyticsPEOPjcReservedAttribute8 | PJC_RESERVED_ATTRIBUTE8 | — | — |
| 95 | WorkOrderAnalyticsPEOPjcReservedAttribute9 | PJC_RESERVED_ATTRIBUTE9 | — | — |
| 96 | WorkOrderAnalyticsPEOPjcTaskId | PJC_TASK_ID | — | — |
| 97 | WorkOrderAnalyticsPEOPjcTaskNumber | PJC_TASK_NUMBER | — | — |
| 98 | WorkOrderAnalyticsPEOPjcUserDefAttribute1 | PJC_USER_DEF_ATTRIBUTE1 | — | — |
| 99 | WorkOrderAnalyticsPEOPjcUserDefAttribute10 | PJC_USER_DEF_ATTRIBUTE10 | — | — |
| 100 | WorkOrderAnalyticsPEOPjcUserDefAttribute2 | PJC_USER_DEF_ATTRIBUTE2 | — | — |
| 101 | WorkOrderAnalyticsPEOPjcUserDefAttribute3 | PJC_USER_DEF_ATTRIBUTE3 | — | — |
| 102 | WorkOrderAnalyticsPEOPjcUserDefAttribute4 | PJC_USER_DEF_ATTRIBUTE4 | — | — |
| 103 | WorkOrderAnalyticsPEOPjcUserDefAttribute5 | PJC_USER_DEF_ATTRIBUTE5 | — | — |
| 104 | WorkOrderAnalyticsPEOPjcUserDefAttribute6 | PJC_USER_DEF_ATTRIBUTE6 | — | — |
| 105 | WorkOrderAnalyticsPEOPjcUserDefAttribute7 | PJC_USER_DEF_ATTRIBUTE7 | — | — |
| 106 | WorkOrderAnalyticsPEOPjcUserDefAttribute8 | PJC_USER_DEF_ATTRIBUTE8 | — | — |
| 107 | WorkOrderAnalyticsPEOPjcUserDefAttribute9 | PJC_USER_DEF_ATTRIBUTE9 | — | — |
| 108 | WorkOrderAnalyticsPEOPjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |
| 109 | WorkOrderAnalyticsPEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | — |
| 110 | WorkOrderAnalyticsPEOPlannedStartDate | PLANNED_START_DATE | — | — |
| 111 | WorkOrderAnalyticsPEOPlannedStartQuantity | PLANNED_START_QUANTITY | — | — |
| 112 | WorkOrderAnalyticsPEOPrimaryProductQuantity | PRIMARY_PRODUCT_QUANTITY | — | — |
| 113 | WorkOrderAnalyticsPEOPrimaryProductUomCode | PRIMARY_PRODUCT_UOM_CODE | — | — |
| 114 | WorkOrderAnalyticsPEORejectedQuantity | REJECTED_QUANTITY | — | — |
| 115 | WorkOrderAnalyticsPEOReleasedDate | RELEASED_DATE | — | — |
| 116 | WorkOrderAnalyticsPEORequestId | REQUEST_ID | — | — |
| 117 | WorkOrderAnalyticsPEOSchedulingMethod | SCHEDULING_METHOD | — | — |
| 118 | WorkOrderAnalyticsPEOScoSupplyOrderId | SCO_SUPPLY_ORDER_ID | — | — |
| 119 | WorkOrderAnalyticsPEOScrappedQuantity | SCRAPPED_QUANTITY | — | — |
| 120 | WorkOrderAnalyticsPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | — |
| 121 | WorkOrderAnalyticsPEOSourceHeaderRef | SOURCE_HEADER_REF | — | — |
| 122 | WorkOrderAnalyticsPEOSourceHeaderRefId | SOURCE_HEADER_REF_ID | — | — |
| 123 | WorkOrderAnalyticsPEOSourceLineRef | SOURCE_LINE_REF | — | — |
| 124 | WorkOrderAnalyticsPEOSourceLineRefId | SOURCE_LINE_REF_ID | — | — |
| 125 | WorkOrderAnalyticsPEOSourceSystemId | SOURCE_SYSTEM_ID | — | — |
| 126 | WorkOrderAnalyticsPEOSourceSystemType | SOURCE_SYSTEM_TYPE | — | — |
| 127 | WorkOrderAnalyticsPEOStatusChangeReason | STATUS_CHANGE_REASON | — | — |
| 128 | WorkOrderAnalyticsPEOSupplyType | SUPPLY_TYPE | — | — |
| 129 | WorkOrderAnalyticsPEOUomCode | UOM_CODE | — | — |
| 130 | WorkOrderAnalyticsPEOWorkDefinitionAsOfDate | WORK_DEFINITION_AS_OF_DATE | — | — |
| 131 | WorkOrderAnalyticsPEOWorkDefinitionId | WORK_DEFINITION_ID | — | — |
| 132 | WorkOrderAnalyticsPEOWorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | — |
| 133 | WorkOrderAnalyticsPEOWorkMethodId | WORK_METHOD_ID | — | — |
| 134 | WorkOrderAnalyticsPEOWorkOrderId | WORK_ORDER_ID | — | — |
| 135 | WorkOrderAnalyticsPEOWorkOrderNumber | WORK_ORDER_NUMBER | — | — |
| 136 | WorkOrderAnalyticsPEOWorkOrderPriority | WORK_ORDER_PRIORITY | — | — |
| 137 | WorkOrderAnalyticsPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | — |
| 138 | WorkOrderAnalyticsPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | — |
| 139 | WorkOrderAnalyticsPEOWorkOrderType | WORK_ORDER_TYPE | — | — |

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
| 8 | WOOperationAnalyticsPEOAttributeChar131 | ATTRIBUTE_CHAR13 | — | — |
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
| 73 | WOOperationAnalyticsPEOScrappedQuantity1 | SCRAPPED_QUANTITY | — | — |
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

### [[wie_wo_op_output_detail_v|WIE_WO_OP_OUTPUT_DETAIL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WOOpOutputDetailExtendPEOComplLocatorId | COMPL_LOCATOR_ID | — | — |
| 2 | WOOpOutputDetailExtendPEOComplSubinventoryCode | COMPL_SUBINVENTORY_CODE | — | ✅ |
| 3 | WOOpOutputDetailExtendPEOCompletedQuantity | COMPLETED_QUANTITY | — | ✅ |
| 4 | WOOpOutputDetailExtendPEOCompletionType | COMPLETION_TYPE | — | ✅ |
| 5 | WOOpOutputDetailExtendPEOCostAllocationPercentage | COST_ALLOCATION_PERCENTAGE | — | ✅ |
| 6 | WOOpOutputDetailExtendPEOCreatedBy | CREATED_BY | — | — |
| 7 | WOOpOutputDetailExtendPEOCreationDate | CREATION_DATE | — | — |
| 8 | WOOpOutputDetailExtendPEOInventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 9 | WOOpOutputDetailExtendPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 10 | WOOpOutputDetailExtendPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 11 | WOOpOutputDetailExtendPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | WOOpOutputDetailExtendPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | WOOpOutputDetailExtendPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | WOOpOutputDetailExtendPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | WOOpOutputDetailExtendPEOOrganizationId | ORGANIZATION_ID | — | — |
| 16 | WOOpOutputDetailExtendPEOOutputQuantity | OUTPUT_QUANTITY | — | ✅ |
| 17 | WOOpOutputDetailExtendPEOOutputSeqNumber | OUTPUT_SEQ_NUMBER | — | ✅ |
| 18 | WOOpOutputDetailExtendPEOOutputType | OUTPUT_TYPE | — | ✅ |
| 19 | WOOpOutputDetailExtendPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 20 | WOOpOutputDetailExtendPEORequestId | REQUEST_ID | — | — |
| 21 | WOOpOutputDetailExtendPEOUomCode | UOM_CODE | — | ✅ |
| 22 | WOOpOutputDetailExtendPEOWdOperationOutputId | WD_OPERATION_OUTPUT_ID | — | — |
| 23 | WOOpOutputDetailExtendPEOWoOperationId | WO_OPERATION_ID | 🔑 | ✅ |
| 24 | WOOpOutputDetailExtendPEOWoOperationOutputId | WO_OPERATION_OUTPUT_ID | — | ✅ |
| 25 | WOOpOutputDetailExtendPEOWorkOrderId | WORK_ORDER_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
