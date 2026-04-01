---
id: DOC-OTHER-PVO-MaintenanceWOOperationsResourceInstancesPVO
doc_type: system-doc
title: "MaintenanceWOOperationsResourceInstancesPVO — PVO Cross-Module"
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
  - MaintenanceWOOperationsResourceInstancesPVO
  - maintenancewooperationsresourceinstancespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MaintenanceWOOperationsResourceInstancesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Maintenance WOOperations Resource Instances. Acessa as tabelas: WIE_WORK_ORDERS_B, WIE_WO_OPERATIONS_B, WIE_WO_OPERATION_RESOURCES (+4).

**Caminho:** `FscmTopModelAM.WorkOrderAM.MaintenanceWOOperationsResourceInstancesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 192 | 7 | 1 | 9 | 5% |

---

## 🔗 Tabelas Relacionadas

- [[wie_work_orders_b|WIE_WORK_ORDERS_B]] — 70 atributos (1 BICC)
- [[wie_wo_operations_b|WIE_WO_OPERATIONS_B]] — 43 atributos (1 BICC)
- [[wie_wo_operation_resources|WIE_WO_OPERATION_RESOURCES]] — 32 atributos (2 BICC)
- [[wie_wo_op_resource_instances|WIE_WO_OP_RESOURCE_INSTANCES]] — 16 atributos (1 PKs, 3 BICC)
- [[wis_equipment_instances|WIS_EQUIPMENT_INSTANCES]] — 14 atributos (1 BICC)
- [[wis_labor_instances|WIS_LABOR_INSTANCES]] — 14 atributos (1 BICC)
- [[wis_work_methods_vl|WIS_WORK_METHODS_VL]] — 3 atributos

---

## ⚙️ Atributos

### [[wie_work_orders_b|WIE_WORK_ORDERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderAnalyticsPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
| 2 | WorkOrderAnalyticsPEOActualStartDate | ACTUAL_START_DATE | — | — |
| 3 | WorkOrderAnalyticsPEOBackToBackFlag | BACK_TO_BACK_FLAG | — | — |
| 4 | WorkOrderAnalyticsPEOCanceledDate | CANCELED_DATE | — | — |
| 5 | WorkOrderAnalyticsPEOCanceledReason | CANCELED_REASON | — | — |
| 6 | WorkOrderAnalyticsPEOClosedDate | CLOSED_DATE | — | — |
| 7 | WorkOrderAnalyticsPEOCmPoHeaderId | CM_PO_HEADER_ID | — | — |
| 8 | WorkOrderAnalyticsPEOCmPoLineId | CM_PO_LINE_ID | — | — |
| 9 | WorkOrderAnalyticsPEOCmPoLineLocId | CM_PO_LINE_LOC_ID | — | — |
| 10 | WorkOrderAnalyticsPEOComplLocatorId | COMPL_LOCATOR_ID | — | — |
| 11 | WorkOrderAnalyticsPEOComplSubinventoryCode | COMPL_SUBINVENTORY_CODE | — | — |
| 12 | WorkOrderAnalyticsPEOCompletedQuantity | COMPLETED_QUANTITY | — | — |
| 13 | WorkOrderAnalyticsPEOContractMfgFlag | CONTRACT_MFG_FLAG | — | — |
| 14 | WorkOrderAnalyticsPEOCreatedBy | CREATED_BY | — | — |
| 15 | WorkOrderAnalyticsPEOCreationDate | CREATION_DATE | — | — |
| 16 | WorkOrderAnalyticsPEOFirmPlannedFlag | FIRM_PLANNED_FLAG | — | — |
| 17 | WorkOrderAnalyticsPEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 18 | WorkOrderAnalyticsPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
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
| 31 | WorkOrderAnalyticsPEOOrganizationId | ORGANIZATION_ID | — | — |
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
| 42 | WorkOrderAnalyticsPEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | — |
| 43 | WorkOrderAnalyticsPEOPlannedStartDate | PLANNED_START_DATE | — | — |
| 44 | WorkOrderAnalyticsPEOPlannedStartQuantity | PLANNED_START_QUANTITY | — | — |
| 45 | WorkOrderAnalyticsPEORejectedQuantity | REJECTED_QUANTITY | — | — |
| 46 | WorkOrderAnalyticsPEOReleasedDate | RELEASED_DATE | — | — |
| 47 | WorkOrderAnalyticsPEORequestId | REQUEST_ID | — | — |
| 48 | WorkOrderAnalyticsPEOSchedulingMethod | SCHEDULING_METHOD | — | — |
| 49 | WorkOrderAnalyticsPEOScoSupplyOrderId | SCO_SUPPLY_ORDER_ID | — | — |
| 50 | WorkOrderAnalyticsPEOScrappedQuantity | SCRAPPED_QUANTITY | — | — |
| 51 | WorkOrderAnalyticsPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | — |
| 52 | WorkOrderAnalyticsPEOSourceHeaderRef | SOURCE_HEADER_REF | — | — |
| 53 | WorkOrderAnalyticsPEOSourceHeaderRefId | SOURCE_HEADER_REF_ID | — | — |
| 54 | WorkOrderAnalyticsPEOSourceLineRef | SOURCE_LINE_REF | — | — |
| 55 | WorkOrderAnalyticsPEOSourceLineRefId | SOURCE_LINE_REF_ID | — | — |
| 56 | WorkOrderAnalyticsPEOSourceSystemId | SOURCE_SYSTEM_ID | — | — |
| 57 | WorkOrderAnalyticsPEOSourceSystemType | SOURCE_SYSTEM_TYPE | — | — |
| 58 | WorkOrderAnalyticsPEOStatusChangeReason | STATUS_CHANGE_REASON | — | — |
| 59 | WorkOrderAnalyticsPEOSupplyType | SUPPLY_TYPE | — | — |
| 60 | WorkOrderAnalyticsPEOUomCode | UOM_CODE | — | — |
| 61 | WorkOrderAnalyticsPEOWorkDefinitionAsOfDate | WORK_DEFINITION_AS_OF_DATE | — | — |
| 62 | WorkOrderAnalyticsPEOWorkDefinitionId | WORK_DEFINITION_ID | — | — |
| 63 | WorkOrderAnalyticsPEOWorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | — |
| 64 | WorkOrderAnalyticsPEOWorkMethodId | WORK_METHOD_ID | — | — |
| 65 | WorkOrderAnalyticsPEOWorkOrderId | WORK_ORDER_ID | — | — |
| 66 | WorkOrderAnalyticsPEOWorkOrderNumber | WORK_ORDER_NUMBER | — | — |
| 67 | WorkOrderAnalyticsPEOWorkOrderPriority | WORK_ORDER_PRIORITY | — | — |
| 68 | WorkOrderAnalyticsPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | — |
| 69 | WorkOrderAnalyticsPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | — |
| 70 | WorkOrderAnalyticsPEOWorkOrderType | WORK_ORDER_TYPE | — | — |

### [[wie_wo_operations_b|WIE_WO_OPERATIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WOOperationAnalyticsPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | — |
| 2 | WOOperationAnalyticsPEOActualStartDate | ACTUAL_START_DATE | — | — |
| 3 | WOOperationAnalyticsPEOAutoTransactFlag | AUTO_TRANSACT_FLAG | — | — |
| 4 | WOOperationAnalyticsPEOCompletedQuantity | COMPLETED_QUANTITY | — | — |
| 5 | WOOperationAnalyticsPEOCountPointOperationFlag | COUNT_POINT_OPERATION_FLAG | — | — |
| 6 | WOOperationAnalyticsPEOCreatedBy | CREATED_BY | — | — |
| 7 | WOOperationAnalyticsPEOCreationDate | CREATION_DATE | — | — |
| 8 | WOOperationAnalyticsPEOFixedLeadTime | FIXED_LEAD_TIME | — | — |
| 9 | WOOperationAnalyticsPEOInProcessQuantity | IN_PROCESS_QUANTITY | — | — |
| 10 | WOOperationAnalyticsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 11 | WOOperationAnalyticsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 12 | WOOperationAnalyticsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | WOOperationAnalyticsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | WOOperationAnalyticsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | WOOperationAnalyticsPEOLeadTimeUom | LEAD_TIME_UOM | — | — |
| 16 | WOOperationAnalyticsPEONextCpOpSeqNum | NEXT_CP_OP_SEQ_NUM | — | — |
| 17 | WOOperationAnalyticsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | WOOperationAnalyticsPEOOperationSeqNumber | OPERATION_SEQ_NUMBER | — | — |
| 19 | WOOperationAnalyticsPEOOperationType | OPERATION_TYPE | — | — |
| 20 | WOOperationAnalyticsPEOOrganizationId | ORGANIZATION_ID | — | — |
| 21 | WOOperationAnalyticsPEOOspItemId | OSP_ITEM_ID | — | — |
| 22 | WOOperationAnalyticsPEOOverReceiptQuantity | OVER_RECEIPT_QUANTITY | — | — |
| 23 | WOOperationAnalyticsPEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | — |
| 24 | WOOperationAnalyticsPEOPlannedStartDate | PLANNED_START_DATE | — | — |
| 25 | WOOperationAnalyticsPEOPoApprovedQuantity | PO_APPROVED_QUANTITY | — | — |
| 26 | WOOperationAnalyticsPEOPoRequestedQuantity | PO_REQUESTED_QUANTITY | — | — |
| 27 | WOOperationAnalyticsPEOPreviousCpOpSeqNum | PREVIOUS_CP_OP_SEQ_NUM | — | — |
| 28 | WOOperationAnalyticsPEOReadyQuantity | READY_QUANTITY | — | — |
| 29 | WOOperationAnalyticsPEOReceivedQuantity | RECEIVED_QUANTITY | — | — |
| 30 | WOOperationAnalyticsPEORejectedQuantity | REJECTED_QUANTITY | — | — |
| 31 | WOOperationAnalyticsPEORequestId | REQUEST_ID | — | — |
| 32 | WOOperationAnalyticsPEOScrappedQuantity | SCRAPPED_QUANTITY | — | — |
| 33 | WOOperationAnalyticsPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | — |
| 34 | WOOperationAnalyticsPEOShippedQuantity | SHIPPED_QUANTITY | — | — |
| 35 | WOOperationAnalyticsPEOShippingDocumentsFlag | SHIPPING_DOCUMENTS_FLAG | — | — |
| 36 | WOOperationAnalyticsPEOStandardOperationId | STANDARD_OPERATION_ID | — | — |
| 37 | WOOperationAnalyticsPEOSupplierId | SUPPLIER_ID | — | — |
| 38 | WOOperationAnalyticsPEOSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 39 | WOOperationAnalyticsPEOVariableLeadTime | VARIABLE_LEAD_TIME | — | — |
| 40 | WOOperationAnalyticsPEOWdOperationId | WD_OPERATION_ID | — | — |
| 41 | WOOperationAnalyticsPEOWoOperationId | WO_OPERATION_ID | — | — |
| 42 | WOOperationAnalyticsPEOWorkCenterId | WORK_CENTER_ID | — | — |
| 43 | WOOperationAnalyticsPEOWorkOrderId | WORK_ORDER_ID | — | — |

### [[wie_wo_operation_resources|WIE_WO_OPERATION_RESOURCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderOperationResourcePEOActualResourceUsage | ACTUAL_RESOURCE_USAGE | — | — |
| 2 | WorkOrderOperationResourcePEOAssignedUnits | ASSIGNED_UNITS | — | — |
| 3 | WorkOrderOperationResourcePEOBasisType | BASIS_TYPE | — | — |
| 4 | WorkOrderOperationResourcePEOChargeType | CHARGE_TYPE | — | — |
| 5 | WorkOrderOperationResourcePEOCreatedBy | CREATED_BY | — | — |
| 6 | WorkOrderOperationResourcePEOCreationDate | CREATION_DATE | — | — |
| 7 | WorkOrderOperationResourcePEOEqpQualProfileId | EQP_QUAL_PROFILE_ID | — | — |
| 8 | WorkOrderOperationResourcePEOInverseRequiredUsage | INVERSE_REQUIRED_USAGE | — | — |
| 9 | WorkOrderOperationResourcePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 10 | WorkOrderOperationResourcePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 11 | WorkOrderOperationResourcePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | WorkOrderOperationResourcePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | WorkOrderOperationResourcePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | WorkOrderOperationResourcePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | WorkOrderOperationResourcePEOOrganizationId | ORGANIZATION_ID | — | — |
| 16 | WorkOrderOperationResourcePEOPhantomFlag | PHANTOM_FLAG | — | — |
| 17 | WorkOrderOperationResourcePEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | — |
| 18 | WorkOrderOperationResourcePEOPlannedStartDate | PLANNED_START_DATE | — | — |
| 19 | WorkOrderOperationResourcePEOPrincipalFlag | PRINCIPAL_FLAG | — | — |
| 20 | WorkOrderOperationResourcePEOProfileId | PROFILE_ID | — | — |
| 21 | WorkOrderOperationResourcePEORequestId | REQUEST_ID | — | — |
| 22 | WorkOrderOperationResourcePEORequiredUsage | REQUIRED_USAGE | — | ✅ |
| 23 | WorkOrderOperationResourcePEOResourceActivityCode | RESOURCE_ACTIVITY_CODE | — | — |
| 24 | WorkOrderOperationResourcePEOResourceId | RESOURCE_ID | — | — |
| 25 | WorkOrderOperationResourcePEOResourceSeqNumber | RESOURCE_SEQ_NUMBER | — | — |
| 26 | WorkOrderOperationResourcePEOScheduledFlag | SCHEDULED_FLAG | — | — |
| 27 | WorkOrderOperationResourcePEOUomCode | UOM_CODE | — | — |
| 28 | WorkOrderOperationResourcePEOUsageRate | USAGE_RATE | — | — |
| 29 | WorkOrderOperationResourcePEOWdOperationResourceId | WD_OPERATION_RESOURCE_ID | — | — |
| 30 | WorkOrderOperationResourcePEOWoOperationId | WO_OPERATION_ID | — | — |
| 31 | WorkOrderOperationResourcePEOWoOperationResourceId | WO_OPERATION_RESOURCE_ID | — | — |
| 32 | WorkOrderOperationResourcePEOWorkCenterId | WORK_CENTER_ID | — | — |

### [[wie_wo_op_resource_instances|WIE_WO_OP_RESOURCE_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WOOprResourceInstancesPEOChargedQuantity | CHARGED_QUANTITY | — | ✅ |
| 2 | WOOprResourceInstancesPEOCreatedBy | CREATED_BY | — | — |
| 3 | WOOprResourceInstancesPEOCreationDate | CREATION_DATE | — | — |
| 4 | WOOprResourceInstancesPEODocumentItemId | DOCUMENT_ITEM_ID | — | — |
| 5 | WOOprResourceInstancesPEOEquipmentInstanceId | EQUIPMENT_INSTANCE_ID | — | — |
| 6 | WOOprResourceInstancesPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 7 | WOOprResourceInstancesPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 8 | WOOprResourceInstancesPEOLaborInstanceId | LABOR_INSTANCE_ID | — | — |
| 9 | WOOprResourceInstancesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | WOOprResourceInstancesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | WOOprResourceInstancesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | WOOprResourceInstancesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | WOOprResourceInstancesPEOOrganizationId | ORGANIZATION_ID | — | — |
| 14 | WOOprResourceInstancesPEORequestId | REQUEST_ID | — | — |
| 15 | WOOprResourceInstancesPEOWoOpResourceInstanceId | WO_OP_RESOURCE_INSTANCE_ID | 🔑 | ✅ |
| 16 | WOOprResourceInstancesPEOWoOperationResourceId | WO_OPERATION_RESOURCE_ID | — | — |

### [[wis_equipment_instances|WIS_EQUIPMENT_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EquipmentInstancePEOAssetId | ASSET_ID | — | — |
| 2 | EquipmentInstancePEOCreatedBy | CREATED_BY | — | — |
| 3 | EquipmentInstancePEOCreationDate | CREATION_DATE | — | — |
| 4 | EquipmentInstancePEOEquipmentInstanceCode | EQUIPMENT_INSTANCE_CODE | — | — |
| 5 | EquipmentInstancePEOEquipmentInstanceId | EQUIPMENT_INSTANCE_ID | — | — |
| 6 | EquipmentInstancePEOEquipmentInstanceName | EQUIPMENT_INSTANCE_NAME | — | — |
| 7 | EquipmentInstancePEOInactiveDate | INACTIVE_DATE | — | — |
| 8 | EquipmentInstancePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | EquipmentInstancePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | EquipmentInstancePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | EquipmentInstancePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | EquipmentInstancePEOOrganizationId | ORGANIZATION_ID | — | — |
| 13 | EquipmentInstancePEOResourceId | RESOURCE_ID | — | — |
| 14 | EquipmentInstancePEOWorkCenterId | WORK_CENTER_ID | — | — |

### [[wis_labor_instances|WIS_LABOR_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LaborInstancePEOCreatedBy | CREATED_BY | — | — |
| 2 | LaborInstancePEOCreationDate | CREATION_DATE | — | — |
| 3 | LaborInstancePEOInactiveDate | INACTIVE_DATE | — | — |
| 4 | LaborInstancePEOLaborInstanceCode | LABOR_INSTANCE_CODE | — | — |
| 5 | LaborInstancePEOLaborInstanceId | LABOR_INSTANCE_ID | — | — |
| 6 | LaborInstancePEOLaborInstanceName | LABOR_INSTANCE_NAME | — | — |
| 7 | LaborInstancePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LaborInstancePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LaborInstancePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | LaborInstancePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | LaborInstancePEOOrganizationId | ORGANIZATION_ID | — | — |
| 12 | LaborInstancePEOPartyId | PARTY_ID | — | — |
| 13 | LaborInstancePEOResourceId | RESOURCE_ID | — | — |
| 14 | LaborInstancePEOWorkCenterId | WORK_CENTER_ID | — | — |

### [[wis_work_methods_vl|WIS_WORK_METHODS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkMethodCode | WORK_METHOD_CODE | — | — |
| 2 | WorkMethodId | WORK_METHOD_ID | — | — |
| 3 | WorkMethodPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
