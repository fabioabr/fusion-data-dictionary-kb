---
id: DOC-OTHER-PVO-MaintenanceWOOperationsResourcesPVO
doc_type: system-doc
title: "MaintenanceWOOperationsResourcesPVO — PVO Cross-Module"
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
  - MaintenanceWOOperationsResourcesPVO
  - maintenancewooperationsresourcespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MaintenanceWOOperationsResourcesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Maintenance WOOperations Resources. Acessa as tabelas: WIE_WORK_ORDERS_B, WIE_WO_OPERATIONS_B, WIE_WO_OPERATION_RESOURCES (+1).

**Caminho:** `FscmTopModelAM.WorkOrderAM.MaintenanceWOOperationsResourcesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 148 | 4 | 1 | 76 | 51% |

---

## 🔗 Tabelas Relacionadas

- [[wie_work_orders_b|WIE_WORK_ORDERS_B]] — 70 atributos (30 BICC)
- [[wie_wo_operations_b|WIE_WO_OPERATIONS_B]] — 43 atributos (26 BICC)
- [[wie_wo_operation_resources|WIE_WO_OPERATION_RESOURCES]] — 32 atributos (1 PKs, 20 BICC)
- [[wis_work_methods_vl|WIS_WORK_METHODS_VL]] — 3 atributos

---

## ⚙️ Atributos

### [[wie_work_orders_b|WIE_WORK_ORDERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderAnalyticsPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 2 | WorkOrderAnalyticsPEOActualStartDate | ACTUAL_START_DATE | — | ✅ |
| 3 | WorkOrderAnalyticsPEOBackToBackFlag | BACK_TO_BACK_FLAG | — | — |
| 4 | WorkOrderAnalyticsPEOCanceledDate | CANCELED_DATE | — | ✅ |
| 5 | WorkOrderAnalyticsPEOCanceledReason | CANCELED_REASON | — | — |
| 6 | WorkOrderAnalyticsPEOClosedDate | CLOSED_DATE | — | ✅ |
| 7 | WorkOrderAnalyticsPEOCmPoHeaderId | CM_PO_HEADER_ID | — | ✅ |
| 8 | WorkOrderAnalyticsPEOCmPoLineId | CM_PO_LINE_ID | — | ✅ |
| 9 | WorkOrderAnalyticsPEOCmPoLineLocId | CM_PO_LINE_LOC_ID | — | ✅ |
| 10 | WorkOrderAnalyticsPEOComplLocatorId | COMPL_LOCATOR_ID | — | ✅ |
| 11 | WorkOrderAnalyticsPEOComplSubinventoryCode | COMPL_SUBINVENTORY_CODE | — | — |
| 12 | WorkOrderAnalyticsPEOCompletedQuantity | COMPLETED_QUANTITY | — | ✅ |
| 13 | WorkOrderAnalyticsPEOContractMfgFlag | CONTRACT_MFG_FLAG | — | — |
| 14 | WorkOrderAnalyticsPEOCreatedBy | CREATED_BY | — | — |
| 15 | WorkOrderAnalyticsPEOCreationDate | CREATION_DATE | — | ✅ |
| 16 | WorkOrderAnalyticsPEOFirmPlannedFlag | FIRM_PLANNED_FLAG | — | — |
| 17 | WorkOrderAnalyticsPEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 18 | WorkOrderAnalyticsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 19 | WorkOrderAnalyticsPEOItemRevision | ITEM_REVISION | — | — |
| 20 | WorkOrderAnalyticsPEOItemStructureName | ITEM_STRUCTURE_NAME | — | — |
| 21 | WorkOrderAnalyticsPEOItemVersion | ITEM_VERSION | — | — |
| 22 | WorkOrderAnalyticsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 23 | WorkOrderAnalyticsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 24 | WorkOrderAnalyticsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | WorkOrderAnalyticsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 26 | WorkOrderAnalyticsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 27 | WorkOrderAnalyticsPEONettableSupplyQtyOverride | NETTABLE_SUPPLY_QTY_OVERRIDE | — | — |
| 28 | WorkOrderAnalyticsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 29 | WorkOrderAnalyticsPEOOrchestrationCode | ORCHESTRATION_CODE | — | — |
| 30 | WorkOrderAnalyticsPEOOrderLessFlag | ORDER_LESS_FLAG | — | — |
| 31 | WorkOrderAnalyticsPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 32 | WorkOrderAnalyticsPEOOvercomplToleranceType | OVERCOMPL_TOLERANCE_TYPE | — | — |
| 33 | WorkOrderAnalyticsPEOOvercomplToleranceValue | OVERCOMPL_TOLERANCE_VALUE | — | — |
| 34 | WorkOrderAnalyticsPEOPjcContractId | PJC_CONTRACT_ID | — | — |
| 35 | WorkOrderAnalyticsPEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 36 | WorkOrderAnalyticsPEOPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | — |
| 37 | WorkOrderAnalyticsPEOPjcOrganizationId | PJC_ORGANIZATION_ID | — | — |
| 38 | WorkOrderAnalyticsPEOPjcProjectId | PJC_PROJECT_ID | — | — |
| 39 | WorkOrderAnalyticsPEOPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 40 | WorkOrderAnalyticsPEOPjcTaskId | PJC_TASK_ID | — | — |
| 41 | WorkOrderAnalyticsPEOPjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |
| 42 | WorkOrderAnalyticsPEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | ✅ |
| 43 | WorkOrderAnalyticsPEOPlannedStartDate | PLANNED_START_DATE | — | ✅ |
| 44 | WorkOrderAnalyticsPEOPlannedStartQuantity | PLANNED_START_QUANTITY | — | ✅ |
| 45 | WorkOrderAnalyticsPEORejectedQuantity | REJECTED_QUANTITY | — | ✅ |
| 46 | WorkOrderAnalyticsPEOReleasedDate | RELEASED_DATE | — | ✅ |
| 47 | WorkOrderAnalyticsPEORequestId | REQUEST_ID | — | ✅ |
| 48 | WorkOrderAnalyticsPEOSchedulingMethod | SCHEDULING_METHOD | — | — |
| 49 | WorkOrderAnalyticsPEOScoSupplyOrderId | SCO_SUPPLY_ORDER_ID | — | ✅ |
| 50 | WorkOrderAnalyticsPEOScrappedQuantity | SCRAPPED_QUANTITY | — | ✅ |
| 51 | WorkOrderAnalyticsPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | — |
| 52 | WorkOrderAnalyticsPEOSourceHeaderRef | SOURCE_HEADER_REF | — | — |
| 53 | WorkOrderAnalyticsPEOSourceHeaderRefId | SOURCE_HEADER_REF_ID | — | ✅ |
| 54 | WorkOrderAnalyticsPEOSourceLineRef | SOURCE_LINE_REF | — | — |
| 55 | WorkOrderAnalyticsPEOSourceLineRefId | SOURCE_LINE_REF_ID | — | ✅ |
| 56 | WorkOrderAnalyticsPEOSourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 57 | WorkOrderAnalyticsPEOSourceSystemType | SOURCE_SYSTEM_TYPE | — | — |
| 58 | WorkOrderAnalyticsPEOStatusChangeReason | STATUS_CHANGE_REASON | — | — |
| 59 | WorkOrderAnalyticsPEOSupplyType | SUPPLY_TYPE | — | — |
| 60 | WorkOrderAnalyticsPEOUomCode | UOM_CODE | — | — |
| 61 | WorkOrderAnalyticsPEOWorkDefinitionAsOfDate | WORK_DEFINITION_AS_OF_DATE | — | ✅ |
| 62 | WorkOrderAnalyticsPEOWorkDefinitionId | WORK_DEFINITION_ID | — | ✅ |
| 63 | WorkOrderAnalyticsPEOWorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | ✅ |
| 64 | WorkOrderAnalyticsPEOWorkMethodId | WORK_METHOD_ID | — | ✅ |
| 65 | WorkOrderAnalyticsPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 66 | WorkOrderAnalyticsPEOWorkOrderNumber | WORK_ORDER_NUMBER | — | — |
| 67 | WorkOrderAnalyticsPEOWorkOrderPriority | WORK_ORDER_PRIORITY | — | — |
| 68 | WorkOrderAnalyticsPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | ✅ |
| 69 | WorkOrderAnalyticsPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | — |
| 70 | WorkOrderAnalyticsPEOWorkOrderType | WORK_ORDER_TYPE | — | — |

### [[wie_wo_operations_b|WIE_WO_OPERATIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WOOperationPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 2 | WOOperationPEOActualStartDate | ACTUAL_START_DATE | — | ✅ |
| 3 | WOOperationPEOAutoTransactFlag | AUTO_TRANSACT_FLAG | — | — |
| 4 | WOOperationPEOCompletedQuantity | COMPLETED_QUANTITY | — | ✅ |
| 5 | WOOperationPEOCountPointOperationFlag | COUNT_POINT_OPERATION_FLAG | — | — |
| 6 | WOOperationPEOCreatedBy | CREATED_BY | — | — |
| 7 | WOOperationPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | WOOperationPEOFixedLeadTime | FIXED_LEAD_TIME | — | — |
| 9 | WOOperationPEOInProcessQuantity | IN_PROCESS_QUANTITY | — | ✅ |
| 10 | WOOperationPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 11 | WOOperationPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 12 | WOOperationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | WOOperationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | WOOperationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | WOOperationPEOLeadTimeUom | LEAD_TIME_UOM | — | — |
| 16 | WOOperationPEONextCpOpSeqNum | NEXT_CP_OP_SEQ_NUM | — | — |
| 17 | WOOperationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | WOOperationPEOOperationSeqNumber | OPERATION_SEQ_NUMBER | — | — |
| 19 | WOOperationPEOOperationType | OPERATION_TYPE | — | — |
| 20 | WOOperationPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 21 | WOOperationPEOOspItemId | OSP_ITEM_ID | — | ✅ |
| 22 | WOOperationPEOOverReceiptQuantity | OVER_RECEIPT_QUANTITY | — | ✅ |
| 23 | WOOperationPEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | ✅ |
| 24 | WOOperationPEOPlannedStartDate | PLANNED_START_DATE | — | ✅ |
| 25 | WOOperationPEOPoApprovedQuantity | PO_APPROVED_QUANTITY | — | ✅ |
| 26 | WOOperationPEOPoRequestedQuantity | PO_REQUESTED_QUANTITY | — | ✅ |
| 27 | WOOperationPEOPreviousCpOpSeqNum | PREVIOUS_CP_OP_SEQ_NUM | — | — |
| 28 | WOOperationPEOReadyQuantity | READY_QUANTITY | — | ✅ |
| 29 | WOOperationPEOReceivedQuantity | RECEIVED_QUANTITY | — | ✅ |
| 30 | WOOperationPEORejectedQuantity | REJECTED_QUANTITY | — | ✅ |
| 31 | WOOperationPEORequestId | REQUEST_ID | — | ✅ |
| 32 | WOOperationPEOScrappedQuantity | SCRAPPED_QUANTITY | — | ✅ |
| 33 | WOOperationPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | — |
| 34 | WOOperationPEOShippedQuantity | SHIPPED_QUANTITY | — | ✅ |
| 35 | WOOperationPEOShippingDocumentsFlag | SHIPPING_DOCUMENTS_FLAG | — | — |
| 36 | WOOperationPEOStandardOperationId | STANDARD_OPERATION_ID | — | ✅ |
| 37 | WOOperationPEOSupplierId | SUPPLIER_ID | — | ✅ |
| 38 | WOOperationPEOSupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 39 | WOOperationPEOVariableLeadTime | VARIABLE_LEAD_TIME | — | — |
| 40 | WOOperationPEOWdOperationId | WD_OPERATION_ID | — | ✅ |
| 41 | WOOperationPEOWoOperationId | WO_OPERATION_ID | — | ✅ |
| 42 | WOOperationPEOWorkCenterId | WORK_CENTER_ID | — | ✅ |
| 43 | WOOperationPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |

### [[wie_wo_operation_resources|WIE_WO_OPERATION_RESOURCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WoOperationResourceId | WO_OPERATION_RESOURCE_ID | 🔑 | ✅ |
| 2 | WorkOrderOperationResourcePEOActualResourceUsage | ACTUAL_RESOURCE_USAGE | — | ✅ |
| 3 | WorkOrderOperationResourcePEOAssignedUnits | ASSIGNED_UNITS | — | ✅ |
| 4 | WorkOrderOperationResourcePEOBasisType | BASIS_TYPE | — | ✅ |
| 5 | WorkOrderOperationResourcePEOChargeType | CHARGE_TYPE | — | ✅ |
| 6 | WorkOrderOperationResourcePEOCreatedBy | CREATED_BY | — | — |
| 7 | WorkOrderOperationResourcePEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | WorkOrderOperationResourcePEOEqpQualProfileId | EQP_QUAL_PROFILE_ID | — | — |
| 9 | WorkOrderOperationResourcePEOInverseRequiredUsage | INVERSE_REQUIRED_USAGE | — | — |
| 10 | WorkOrderOperationResourcePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 11 | WorkOrderOperationResourcePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 12 | WorkOrderOperationResourcePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | WorkOrderOperationResourcePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | WorkOrderOperationResourcePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | WorkOrderOperationResourcePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | WorkOrderOperationResourcePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 17 | WorkOrderOperationResourcePEOPhantomFlag | PHANTOM_FLAG | — | — |
| 18 | WorkOrderOperationResourcePEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | ✅ |
| 19 | WorkOrderOperationResourcePEOPlannedStartDate | PLANNED_START_DATE | — | ✅ |
| 20 | WorkOrderOperationResourcePEOPrincipalFlag | PRINCIPAL_FLAG | — | ✅ |
| 21 | WorkOrderOperationResourcePEOProfileId | PROFILE_ID | — | — |
| 22 | WorkOrderOperationResourcePEORequestId | REQUEST_ID | — | ✅ |
| 23 | WorkOrderOperationResourcePEORequiredUsage | REQUIRED_USAGE | — | ✅ |
| 24 | WorkOrderOperationResourcePEOResourceActivityCode | RESOURCE_ACTIVITY_CODE | — | ✅ |
| 25 | WorkOrderOperationResourcePEOResourceId | RESOURCE_ID | — | ✅ |
| 26 | WorkOrderOperationResourcePEOResourceSeqNumber | RESOURCE_SEQ_NUMBER | — | ✅ |
| 27 | WorkOrderOperationResourcePEOScheduledFlag | SCHEDULED_FLAG | — | ✅ |
| 28 | WorkOrderOperationResourcePEOUomCode | UOM_CODE | — | — |
| 29 | WorkOrderOperationResourcePEOUsageRate | USAGE_RATE | — | — |
| 30 | WorkOrderOperationResourcePEOWdOperationResourceId | WD_OPERATION_RESOURCE_ID | — | ✅ |
| 31 | WorkOrderOperationResourcePEOWoOperationId | WO_OPERATION_ID | — | ✅ |
| 32 | WorkOrderOperationResourcePEOWorkCenterId | WORK_CENTER_ID | — | ✅ |

### [[wis_work_methods_vl|WIS_WORK_METHODS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkMethodPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | WorkMethodPEOWorkMethodCode | WORK_METHOD_CODE | — | — |
| 3 | WorkMethodPEOWorkMethodId | WORK_METHOD_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
