---
id: DOC-OTHER-PVO-MaintenanceWOOperationMaterialsPVO
doc_type: system-doc
title: "MaintenanceWOOperationMaterialsPVO — PVO Cross-Module"
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
  - MaintenanceWOOperationMaterialsPVO
  - maintenancewooperationmaterialspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MaintenanceWOOperationMaterialsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Maintenance WOOperation Materials. Acessa as tabelas: INV_RESERVATIONS, WIE_WORK_ORDERS_B, WIE_WO_OPERATIONS_B (+2).

**Caminho:** `FscmTopModelAM.WorkOrderAM.MaintenanceWOOperationMaterialsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 269 | 5 | 1 | 42 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[inv_reservations|INV_RESERVATIONS]] — 55 atributos
- [[wie_work_orders_b|WIE_WORK_ORDERS_B]] — 94 atributos (28 BICC)
- [[wie_wo_operations_b|WIE_WO_OPERATIONS_B]] — 84 atributos
- [[wie_wo_operation_materials|WIE_WO_OPERATION_MATERIALS]] — 33 atributos (1 PKs, 14 BICC)
- [[wis_work_methods_vl|WIS_WORK_METHODS_VL]] — 3 atributos

---

## ⚙️ Atributos

### [[inv_reservations|INV_RESERVATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvReservationsPEOContainerLpnId | CONTAINER_LPN_ID | — | — |
| 2 | InvReservationsPEOCrossdockCriteriaId | CROSSDOCK_CRITERIA_ID | — | — |
| 3 | InvReservationsPEOCrossdockFlag | CROSSDOCK_FLAG | — | — |
| 4 | InvReservationsPEODemandShipDate | DEMAND_SHIP_DATE | — | — |
| 5 | InvReservationsPEODemandSourceDelivery | DEMAND_SOURCE_DELIVERY | — | — |
| 6 | InvReservationsPEODemandSourceHeaderId | DEMAND_SOURCE_HEADER_ID | — | — |
| 7 | InvReservationsPEODemandSourceLineDetail | DEMAND_SOURCE_LINE_DETAIL | — | — |
| 8 | InvReservationsPEODemandSourceLineId | DEMAND_SOURCE_LINE_ID | — | — |
| 9 | InvReservationsPEODemandSourceName | DEMAND_SOURCE_NAME | — | — |
| 10 | InvReservationsPEODemandSourceTypeId | DEMAND_SOURCE_TYPE_ID | — | — |
| 11 | InvReservationsPEODetailedQuantity | DETAILED_QUANTITY | — | — |
| 12 | InvReservationsPEOExceptionCode | EXCEPTION_CODE | — | — |
| 13 | InvReservationsPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 14 | InvReservationsPEOLocatorId | LOCATOR_ID | — | — |
| 15 | InvReservationsPEOLotNumber | LOT_NUMBER | — | — |
| 16 | InvReservationsPEOLpnId | LPN_ID | — | — |
| 17 | InvReservationsPEONColumn1 | N_COLUMN1 | — | — |
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
| 31 | InvReservationsPEORequirementDate | REQUIREMENT_DATE | — | — |
| 32 | InvReservationsPEOReservationId | RESERVATION_ID | — | — |
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

### [[wie_work_orders_b|WIE_WORK_ORDERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderAnalyticsPEOBackToBackFlag | BACK_TO_BACK_FLAG | — | — |
| 2 | WorkOrderAnalyticsPEOCanceledDate | CANCELED_DATE | — | ✅ |
| 3 | WorkOrderAnalyticsPEOCanceledReason | CANCELED_REASON | — | — |
| 4 | WorkOrderAnalyticsPEOClosedDate | CLOSED_DATE | — | ✅ |
| 5 | WorkOrderAnalyticsPEOCmPoHeaderId | CM_PO_HEADER_ID | — | ✅ |
| 6 | WorkOrderAnalyticsPEOCmPoLineId | CM_PO_LINE_ID | — | ✅ |
| 7 | WorkOrderAnalyticsPEOCmPoLineLocId | CM_PO_LINE_LOC_ID | — | ✅ |
| 8 | WorkOrderAnalyticsPEOComplLocatorId | COMPL_LOCATOR_ID | — | ✅ |
| 9 | WorkOrderAnalyticsPEOComplSubinventoryCode | COMPL_SUBINVENTORY_CODE | — | — |
| 10 | WorkOrderAnalyticsPEOCompletedQuantity | COMPLETED_QUANTITY | — | ✅ |
| 11 | WorkOrderAnalyticsPEOContractMfgFlag | CONTRACT_MFG_FLAG | — | — |
| 12 | WorkOrderAnalyticsPEOCreatedBy | CREATED_BY | — | — |
| 13 | WorkOrderAnalyticsPEOCreationDate | CREATION_DATE | — | ✅ |
| 14 | WorkOrderAnalyticsPEOFirmPlannedFlag | FIRM_PLANNED_FLAG | — | — |
| 15 | WorkOrderAnalyticsPEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 16 | WorkOrderAnalyticsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 17 | WorkOrderAnalyticsPEOItemRevision | ITEM_REVISION | — | — |
| 18 | WorkOrderAnalyticsPEOItemStructureName | ITEM_STRUCTURE_NAME | — | — |
| 19 | WorkOrderAnalyticsPEOItemVersion | ITEM_VERSION | — | — |
| 20 | WorkOrderAnalyticsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 21 | WorkOrderAnalyticsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 22 | WorkOrderAnalyticsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | WorkOrderAnalyticsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | WorkOrderAnalyticsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 25 | WorkOrderAnalyticsPEONettableSupplyQtyOverride | NETTABLE_SUPPLY_QTY_OVERRIDE | — | — |
| 26 | WorkOrderAnalyticsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 27 | WorkOrderAnalyticsPEOOrchestrationCode | ORCHESTRATION_CODE | — | — |
| 28 | WorkOrderAnalyticsPEOOrderLessFlag | ORDER_LESS_FLAG | — | — |
| 29 | WorkOrderAnalyticsPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 30 | WorkOrderAnalyticsPEOOvercomplToleranceType | OVERCOMPL_TOLERANCE_TYPE | — | — |
| 31 | WorkOrderAnalyticsPEOOvercomplToleranceValue | OVERCOMPL_TOLERANCE_VALUE | — | — |
| 32 | WorkOrderAnalyticsPEOPjcBillableFlag | PJC_BILLABLE_FLAG | — | — |
| 33 | WorkOrderAnalyticsPEOPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | — |
| 34 | WorkOrderAnalyticsPEOPjcContextCategory | PJC_CONTEXT_CATEGORY | — | — |
| 35 | WorkOrderAnalyticsPEOPjcContractId | PJC_CONTRACT_ID | — | — |
| 36 | WorkOrderAnalyticsPEOPjcContractLineId | PJC_CONTRACT_LINE_ID | — | — |
| 37 | WorkOrderAnalyticsPEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 38 | WorkOrderAnalyticsPEOPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | — |
| 39 | WorkOrderAnalyticsPEOPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | — |
| 40 | WorkOrderAnalyticsPEOPjcOrganizationId | PJC_ORGANIZATION_ID | — | — |
| 41 | WorkOrderAnalyticsPEOPjcProjectId | PJC_PROJECT_ID | — | — |
| 42 | WorkOrderAnalyticsPEOPjcProjectNumber | PJC_PROJECT_NUMBER | — | — |
| 43 | WorkOrderAnalyticsPEOPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 44 | WorkOrderAnalyticsPEOPjcReservedAttribute10 | PJC_RESERVED_ATTRIBUTE10 | — | — |
| 45 | WorkOrderAnalyticsPEOPjcReservedAttribute2 | PJC_RESERVED_ATTRIBUTE2 | — | — |
| 46 | WorkOrderAnalyticsPEOPjcReservedAttribute3 | PJC_RESERVED_ATTRIBUTE3 | — | — |
| 47 | WorkOrderAnalyticsPEOPjcReservedAttribute4 | PJC_RESERVED_ATTRIBUTE4 | — | — |
| 48 | WorkOrderAnalyticsPEOPjcReservedAttribute5 | PJC_RESERVED_ATTRIBUTE5 | — | — |
| 49 | WorkOrderAnalyticsPEOPjcReservedAttribute6 | PJC_RESERVED_ATTRIBUTE6 | — | — |
| 50 | WorkOrderAnalyticsPEOPjcReservedAttribute7 | PJC_RESERVED_ATTRIBUTE7 | — | — |
| 51 | WorkOrderAnalyticsPEOPjcReservedAttribute8 | PJC_RESERVED_ATTRIBUTE8 | — | — |
| 52 | WorkOrderAnalyticsPEOPjcReservedAttribute9 | PJC_RESERVED_ATTRIBUTE9 | — | — |
| 53 | WorkOrderAnalyticsPEOPjcTaskId | PJC_TASK_ID | — | — |
| 54 | WorkOrderAnalyticsPEOPjcTaskNumber | PJC_TASK_NUMBER | — | — |
| 55 | WorkOrderAnalyticsPEOPjcUserDefAttribute1 | PJC_USER_DEF_ATTRIBUTE1 | — | — |
| 56 | WorkOrderAnalyticsPEOPjcUserDefAttribute10 | PJC_USER_DEF_ATTRIBUTE10 | — | — |
| 57 | WorkOrderAnalyticsPEOPjcUserDefAttribute2 | PJC_USER_DEF_ATTRIBUTE2 | — | — |
| 58 | WorkOrderAnalyticsPEOPjcUserDefAttribute3 | PJC_USER_DEF_ATTRIBUTE3 | — | — |
| 59 | WorkOrderAnalyticsPEOPjcUserDefAttribute4 | PJC_USER_DEF_ATTRIBUTE4 | — | — |
| 60 | WorkOrderAnalyticsPEOPjcUserDefAttribute5 | PJC_USER_DEF_ATTRIBUTE5 | — | — |
| 61 | WorkOrderAnalyticsPEOPjcUserDefAttribute6 | PJC_USER_DEF_ATTRIBUTE6 | — | — |
| 62 | WorkOrderAnalyticsPEOPjcUserDefAttribute7 | PJC_USER_DEF_ATTRIBUTE7 | — | — |
| 63 | WorkOrderAnalyticsPEOPjcUserDefAttribute8 | PJC_USER_DEF_ATTRIBUTE8 | — | — |
| 64 | WorkOrderAnalyticsPEOPjcUserDefAttribute9 | PJC_USER_DEF_ATTRIBUTE9 | — | — |
| 65 | WorkOrderAnalyticsPEOPjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |
| 66 | WorkOrderAnalyticsPEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | ✅ |
| 67 | WorkOrderAnalyticsPEOPlannedStartDate | PLANNED_START_DATE | — | ✅ |
| 68 | WorkOrderAnalyticsPEOPlannedStartQuantity | PLANNED_START_QUANTITY | — | ✅ |
| 69 | WorkOrderAnalyticsPEORejectedQuantity | REJECTED_QUANTITY | — | ✅ |
| 70 | WorkOrderAnalyticsPEOReleasedDate | RELEASED_DATE | — | ✅ |
| 71 | WorkOrderAnalyticsPEORequestId | REQUEST_ID | — | ✅ |
| 72 | WorkOrderAnalyticsPEOSchedulingMethod | SCHEDULING_METHOD | — | — |
| 73 | WorkOrderAnalyticsPEOScoSupplyOrderId | SCO_SUPPLY_ORDER_ID | — | ✅ |
| 74 | WorkOrderAnalyticsPEOScrappedQuantity | SCRAPPED_QUANTITY | — | ✅ |
| 75 | WorkOrderAnalyticsPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | — |
| 76 | WorkOrderAnalyticsPEOSourceHeaderRef | SOURCE_HEADER_REF | — | — |
| 77 | WorkOrderAnalyticsPEOSourceHeaderRefId | SOURCE_HEADER_REF_ID | — | ✅ |
| 78 | WorkOrderAnalyticsPEOSourceLineRef | SOURCE_LINE_REF | — | — |
| 79 | WorkOrderAnalyticsPEOSourceLineRefId | SOURCE_LINE_REF_ID | — | ✅ |
| 80 | WorkOrderAnalyticsPEOSourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 81 | WorkOrderAnalyticsPEOSourceSystemType | SOURCE_SYSTEM_TYPE | — | — |
| 82 | WorkOrderAnalyticsPEOStatusChangeReason | STATUS_CHANGE_REASON | — | — |
| 83 | WorkOrderAnalyticsPEOSupplyType | SUPPLY_TYPE | — | — |
| 84 | WorkOrderAnalyticsPEOUomCode | UOM_CODE | — | — |
| 85 | WorkOrderAnalyticsPEOWorkDefinitionAsOfDate | WORK_DEFINITION_AS_OF_DATE | — | ✅ |
| 86 | WorkOrderAnalyticsPEOWorkDefinitionId | WORK_DEFINITION_ID | — | ✅ |
| 87 | WorkOrderAnalyticsPEOWorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | ✅ |
| 88 | WorkOrderAnalyticsPEOWorkMethodId | WORK_METHOD_ID | — | ✅ |
| 89 | WorkOrderAnalyticsPEOWorkOrderNumber | WORK_ORDER_NUMBER | — | — |
| 90 | WorkOrderAnalyticsPEOWorkOrderPriority | WORK_ORDER_PRIORITY | — | — |
| 91 | WorkOrderAnalyticsPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | ✅ |
| 92 | WorkOrderAnalyticsPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | — |
| 93 | WorkOrderAnalyticsPEOWorkOrderType | WORK_ORDER_TYPE | — | — |
| 94 | WorkOrderId | WORK_ORDER_ID | — | ✅ |

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
| 53 | WOOperationAnalyticsPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
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

### [[wie_wo_operation_materials|WIE_WO_OPERATION_MATERIALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WOOperationMaterialId | WO_OPERATION_MATERIAL_ID | 🔑 | ✅ |
| 2 | WOOperationMaterialsPEOAllocatedQuantity | ALLOCATED_QUANTITY | — | — |
| 3 | WOOperationMaterialsPEOBasisType | BASIS_TYPE | — | — |
| 4 | WOOperationMaterialsPEOCreatedBy | CREATED_BY | — | — |
| 5 | WOOperationMaterialsPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | WOOperationMaterialsPEOIncludeInPlanningFlag | INCLUDE_IN_PLANNING_FLAG | — | — |
| 7 | WOOperationMaterialsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 8 | WOOperationMaterialsPEOInverseQuantity | INVERSE_QUANTITY | — | ✅ |
| 9 | WOOperationMaterialsPEOIssuedQuantity | ISSUED_QUANTITY | — | ✅ |
| 10 | WOOperationMaterialsPEOItemRevision | ITEM_REVISION | — | — |
| 11 | WOOperationMaterialsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 12 | WOOperationMaterialsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 13 | WOOperationMaterialsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | WOOperationMaterialsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | WOOperationMaterialsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | WOOperationMaterialsPEOMaterialSeqNumber | MATERIAL_SEQ_NUMBER | — | — |
| 17 | WOOperationMaterialsPEOMaterialType | MATERIAL_TYPE | — | — |
| 18 | WOOperationMaterialsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | WOOperationMaterialsPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 20 | WOOperationMaterialsPEOPickedQuantity | PICKED_QUANTITY | — | — |
| 21 | WOOperationMaterialsPEOProducedQuantity | PRODUCED_QUANTITY | — | ✅ |
| 22 | WOOperationMaterialsPEOQuantity | QUANTITY | — | ✅ |
| 23 | WOOperationMaterialsPEOQuantityPerProduct | QUANTITY_PER_PRODUCT | — | — |
| 24 | WOOperationMaterialsPEORequestId | REQUEST_ID | — | ✅ |
| 25 | WOOperationMaterialsPEORequiredDate | REQUIRED_DATE | — | ✅ |
| 26 | WOOperationMaterialsPEOSubstituteFlag | SUBSTITUTE_FLAG | — | — |
| 27 | WOOperationMaterialsPEOSupplyLocatorId | SUPPLY_LOCATOR_ID | — | ✅ |
| 28 | WOOperationMaterialsPEOSupplySubinventory | SUPPLY_SUBINVENTORY | — | — |
| 29 | WOOperationMaterialsPEOSupplyType | SUPPLY_TYPE | — | — |
| 30 | WOOperationMaterialsPEOUomCode | UOM_CODE | — | — |
| 31 | WOOperationMaterialsPEOWoOperationId | WO_OPERATION_ID | — | ✅ |
| 32 | WOOperationMaterialsPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 33 | WOOperationMaterialsPEOYieldFactor | YIELD_FACTOR | — | — |

### [[wis_work_methods_vl|WIS_WORK_METHODS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkMethodPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | WorkMethodPEOWorkMethodCode | WORK_METHOD_CODE | — | — |
| 3 | WorkMethodPEOWorkMethodId | WORK_METHOD_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
