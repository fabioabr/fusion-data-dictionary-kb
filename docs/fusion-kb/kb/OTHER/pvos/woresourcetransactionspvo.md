---
id: DOC-OTHER-PVO-WOResourceTransactionsPVO
doc_type: system-doc
title: "WOResourceTransactionsPVO — PVO Cross-Module"
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
  - WOResourceTransactionsPVO
  - woresourcetransactionspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WOResourceTransactionsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de WOResource Transactions. Acessa as tabelas: WIE_RESOURCE_TRANSACTIONS, WIE_WORK_ORDERS_B, WIE_WO_OPERATION_RESOURCES (+3).

**Caminho:** `FscmTopModelAM.WOResourceTransactionsAM.WOResourceTransactionsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 280 | 6 | 1 | 76 | 27% |

---

## 🔗 Tabelas Relacionadas

- [[wie_resource_transactions|WIE_RESOURCE_TRANSACTIONS]] — 80 atributos (1 PKs, 29 BICC)
- [[wie_work_orders_b|WIE_WORK_ORDERS_B]] — 96 atributos (31 BICC)
- [[wie_wo_operation_resources|WIE_WO_OPERATION_RESOURCES]] — 73 atributos (12 BICC)
- [[wis_equipment_instances|WIS_EQUIPMENT_INSTANCES]] — 14 atributos (2 BICC)
- [[wis_labor_instances|WIS_LABOR_INSTANCES]] — 14 atributos (2 BICC)
- [[wis_work_methods_vl|WIS_WORK_METHODS_VL]] — 3 atributos

---

## ⚙️ Atributos

### [[wie_resource_transactions|WIE_RESOURCE_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourceTransactionPEOAutoTransactFlag | AUTO_TRANSACT_FLAG | — | — |
| 2 | ResourceTransactionPEOBasisType | BASIS_TYPE | — | — |
| 3 | ResourceTransactionPEOChargeType | CHARGE_TYPE | — | — |
| 4 | ResourceTransactionPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | ResourceTransactionPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | ResourceTransactionPEOCstInterfacedFlag | CST_INTERFACED_FLAG | — | — |
| 7 | ResourceTransactionPEOEquipmentInstanceId | EQUIPMENT_INSTANCE_ID | — | — |
| 8 | ResourceTransactionPEOInterfaceBatchId | INTERFACE_BATCH_ID | — | ✅ |
| 9 | ResourceTransactionPEOInterfaceRowId | INTERFACE_ROW_ID | — | ✅ |
| 10 | ResourceTransactionPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 11 | ResourceTransactionPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 12 | ResourceTransactionPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 13 | ResourceTransactionPEOLaborInstanceId | LABOR_INSTANCE_ID | — | — |
| 14 | ResourceTransactionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | ResourceTransactionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | ResourceTransactionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | ResourceTransactionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | ResourceTransactionPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 19 | ResourceTransactionPEOPjcBillableFlag | PJC_BILLABLE_FLAG | — | — |
| 20 | ResourceTransactionPEOPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | — |
| 21 | ResourceTransactionPEOPjcContextCategory | PJC_CONTEXT_CATEGORY | — | — |
| 22 | ResourceTransactionPEOPjcContractId | PJC_CONTRACT_ID | — | — |
| 23 | ResourceTransactionPEOPjcContractLineId | PJC_CONTRACT_LINE_ID | — | — |
| 24 | ResourceTransactionPEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 25 | ResourceTransactionPEOPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | — |
| 26 | ResourceTransactionPEOPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | — |
| 27 | ResourceTransactionPEOPjcOrganizationId | PJC_ORGANIZATION_ID | — | — |
| 28 | ResourceTransactionPEOPjcProjectId | PJC_PROJECT_ID | — | — |
| 29 | ResourceTransactionPEOPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 30 | ResourceTransactionPEOPjcReservedAttribute10 | PJC_RESERVED_ATTRIBUTE10 | — | — |
| 31 | ResourceTransactionPEOPjcReservedAttribute2 | PJC_RESERVED_ATTRIBUTE2 | — | — |
| 32 | ResourceTransactionPEOPjcReservedAttribute3 | PJC_RESERVED_ATTRIBUTE3 | — | — |
| 33 | ResourceTransactionPEOPjcReservedAttribute4 | PJC_RESERVED_ATTRIBUTE4 | — | — |
| 34 | ResourceTransactionPEOPjcReservedAttribute5 | PJC_RESERVED_ATTRIBUTE5 | — | — |
| 35 | ResourceTransactionPEOPjcReservedAttribute6 | PJC_RESERVED_ATTRIBUTE6 | — | — |
| 36 | ResourceTransactionPEOPjcReservedAttribute7 | PJC_RESERVED_ATTRIBUTE7 | — | — |
| 37 | ResourceTransactionPEOPjcReservedAttribute8 | PJC_RESERVED_ATTRIBUTE8 | — | — |
| 38 | ResourceTransactionPEOPjcReservedAttribute9 | PJC_RESERVED_ATTRIBUTE9 | — | — |
| 39 | ResourceTransactionPEOPjcTaskId | PJC_TASK_ID | — | — |
| 40 | ResourceTransactionPEOPjcUserDefAttribute1 | PJC_USER_DEF_ATTRIBUTE1 | — | — |
| 41 | ResourceTransactionPEOPjcUserDefAttribute10 | PJC_USER_DEF_ATTRIBUTE10 | — | — |
| 42 | ResourceTransactionPEOPjcUserDefAttribute2 | PJC_USER_DEF_ATTRIBUTE2 | — | — |
| 43 | ResourceTransactionPEOPjcUserDefAttribute3 | PJC_USER_DEF_ATTRIBUTE3 | — | — |
| 44 | ResourceTransactionPEOPjcUserDefAttribute4 | PJC_USER_DEF_ATTRIBUTE4 | — | — |
| 45 | ResourceTransactionPEOPjcUserDefAttribute5 | PJC_USER_DEF_ATTRIBUTE5 | — | — |
| 46 | ResourceTransactionPEOPjcUserDefAttribute6 | PJC_USER_DEF_ATTRIBUTE6 | — | — |
| 47 | ResourceTransactionPEOPjcUserDefAttribute7 | PJC_USER_DEF_ATTRIBUTE7 | — | — |
| 48 | ResourceTransactionPEOPjcUserDefAttribute8 | PJC_USER_DEF_ATTRIBUTE8 | — | — |
| 49 | ResourceTransactionPEOPjcUserDefAttribute9 | PJC_USER_DEF_ATTRIBUTE9 | — | — |
| 50 | ResourceTransactionPEOPjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |
| 51 | ResourceTransactionPEOPrimaryQuantity | PRIMARY_QUANTITY | — | ✅ |
| 52 | ResourceTransactionPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | — |
| 53 | ResourceTransactionPEORequestId | REQUEST_ID | — | ✅ |
| 54 | ResourceTransactionPEORequiredUsage | REQUIRED_USAGE | — | ✅ |
| 55 | ResourceTransactionPEOResourceActivityCode | RESOURCE_ACTIVITY_CODE | — | — |
| 56 | ResourceTransactionPEOResourceCode | RESOURCE_CODE | — | — |
| 57 | ResourceTransactionPEOResourceId | RESOURCE_ID | — | ✅ |
| 58 | ResourceTransactionPEOResourceSeqNumber | RESOURCE_SEQ_NUMBER | — | — |
| 59 | ResourceTransactionPEOResourceType | RESOURCE_TYPE | — | — |
| 60 | ResourceTransactionPEOSourceHeaderRef | SOURCE_HEADER_REF | — | ✅ |
| 61 | ResourceTransactionPEOSourceHeaderRefId | SOURCE_HEADER_REF_ID | — | ✅ |
| 62 | ResourceTransactionPEOSourceLineRef | SOURCE_LINE_REF | — | ✅ |
| 63 | ResourceTransactionPEOSourceLineRefId | SOURCE_LINE_REF_ID | — | ✅ |
| 64 | ResourceTransactionPEOSourceSystemCode | SOURCE_SYSTEM_CODE | — | — |
| 65 | ResourceTransactionPEOSourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 66 | ResourceTransactionPEOSourceSystemType | SOURCE_SYSTEM_TYPE | — | ✅ |
| 67 | ResourceTransactionPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 68 | ResourceTransactionPEOTransactionQuantity | TRANSACTION_QUANTITY | — | ✅ |
| 69 | ResourceTransactionPEOTransactionTypeCode | TRANSACTION_TYPE_CODE | — | ✅ |
| 70 | ResourceTransactionPEOTransactionUomCode | TRANSACTION_UOM_CODE | — | ✅ |
| 71 | ResourceTransactionPEOTxnHeaderId | TXN_HEADER_ID | — | ✅ |
| 72 | ResourceTransactionPEOUsageRate | USAGE_RATE | — | — |
| 73 | ResourceTransactionPEOWoOperationId | WO_OPERATION_ID | — | ✅ |
| 74 | ResourceTransactionPEOWoOperationResourceId | WO_OPERATION_RESOURCE_ID | — | ✅ |
| 75 | ResourceTransactionPEOWoOperationTransactionId | WO_OPERATION_TRANSACTION_ID | — | ✅ |
| 76 | ResourceTransactionPEOWoResourceTransactionId | WO_RESOURCE_TRANSACTION_ID | — | — |
| 77 | ResourceTransactionPEOWorkCenterId | WORK_CENTER_ID | — | ✅ |
| 78 | ResourceTransactionPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 79 | ResourceTransactionPEOWorkstationId | WORKSTATION_ID | — | — |
| 80 | WoResourceTransactionId | WO_RESOURCE_TRANSACTION_ID | 🔑 | ✅ |

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
| 25 | WorkOrderAnalyticsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 26 | WorkOrderAnalyticsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 27 | WorkOrderAnalyticsPEONettableSupplyQtyOverride | NETTABLE_SUPPLY_QTY_OVERRIDE | — | — |
| 28 | WorkOrderAnalyticsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 29 | WorkOrderAnalyticsPEOOrchestrationCode | ORCHESTRATION_CODE | — | — |
| 30 | WorkOrderAnalyticsPEOOrderLessFlag | ORDER_LESS_FLAG | — | — |
| 31 | WorkOrderAnalyticsPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 32 | WorkOrderAnalyticsPEOOvercomplToleranceType | OVERCOMPL_TOLERANCE_TYPE | — | — |
| 33 | WorkOrderAnalyticsPEOOvercomplToleranceValue | OVERCOMPL_TOLERANCE_VALUE | — | — |
| 34 | WorkOrderAnalyticsPEOPjcBillableFlag | PJC_BILLABLE_FLAG | — | — |
| 35 | WorkOrderAnalyticsPEOPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | — |
| 36 | WorkOrderAnalyticsPEOPjcContextCategory | PJC_CONTEXT_CATEGORY | — | — |
| 37 | WorkOrderAnalyticsPEOPjcContractId | PJC_CONTRACT_ID | — | — |
| 38 | WorkOrderAnalyticsPEOPjcContractLineId | PJC_CONTRACT_LINE_ID | — | — |
| 39 | WorkOrderAnalyticsPEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 40 | WorkOrderAnalyticsPEOPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | — |
| 41 | WorkOrderAnalyticsPEOPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | — |
| 42 | WorkOrderAnalyticsPEOPjcOrganizationId | PJC_ORGANIZATION_ID | — | — |
| 43 | WorkOrderAnalyticsPEOPjcProjectId | PJC_PROJECT_ID | — | — |
| 44 | WorkOrderAnalyticsPEOPjcProjectNumber | PJC_PROJECT_NUMBER | — | — |
| 45 | WorkOrderAnalyticsPEOPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 46 | WorkOrderAnalyticsPEOPjcReservedAttribute10 | PJC_RESERVED_ATTRIBUTE10 | — | — |
| 47 | WorkOrderAnalyticsPEOPjcReservedAttribute2 | PJC_RESERVED_ATTRIBUTE2 | — | — |
| 48 | WorkOrderAnalyticsPEOPjcReservedAttribute3 | PJC_RESERVED_ATTRIBUTE3 | — | — |
| 49 | WorkOrderAnalyticsPEOPjcReservedAttribute4 | PJC_RESERVED_ATTRIBUTE4 | — | — |
| 50 | WorkOrderAnalyticsPEOPjcReservedAttribute5 | PJC_RESERVED_ATTRIBUTE5 | — | — |
| 51 | WorkOrderAnalyticsPEOPjcReservedAttribute6 | PJC_RESERVED_ATTRIBUTE6 | — | — |
| 52 | WorkOrderAnalyticsPEOPjcReservedAttribute7 | PJC_RESERVED_ATTRIBUTE7 | — | — |
| 53 | WorkOrderAnalyticsPEOPjcReservedAttribute8 | PJC_RESERVED_ATTRIBUTE8 | — | — |
| 54 | WorkOrderAnalyticsPEOPjcReservedAttribute9 | PJC_RESERVED_ATTRIBUTE9 | — | — |
| 55 | WorkOrderAnalyticsPEOPjcTaskId | PJC_TASK_ID | — | — |
| 56 | WorkOrderAnalyticsPEOPjcTaskNumber | PJC_TASK_NUMBER | — | — |
| 57 | WorkOrderAnalyticsPEOPjcUserDefAttribute1 | PJC_USER_DEF_ATTRIBUTE1 | — | — |
| 58 | WorkOrderAnalyticsPEOPjcUserDefAttribute10 | PJC_USER_DEF_ATTRIBUTE10 | — | — |
| 59 | WorkOrderAnalyticsPEOPjcUserDefAttribute2 | PJC_USER_DEF_ATTRIBUTE2 | — | — |
| 60 | WorkOrderAnalyticsPEOPjcUserDefAttribute3 | PJC_USER_DEF_ATTRIBUTE3 | — | — |
| 61 | WorkOrderAnalyticsPEOPjcUserDefAttribute4 | PJC_USER_DEF_ATTRIBUTE4 | — | — |
| 62 | WorkOrderAnalyticsPEOPjcUserDefAttribute5 | PJC_USER_DEF_ATTRIBUTE5 | — | — |
| 63 | WorkOrderAnalyticsPEOPjcUserDefAttribute6 | PJC_USER_DEF_ATTRIBUTE6 | — | — |
| 64 | WorkOrderAnalyticsPEOPjcUserDefAttribute7 | PJC_USER_DEF_ATTRIBUTE7 | — | — |
| 65 | WorkOrderAnalyticsPEOPjcUserDefAttribute8 | PJC_USER_DEF_ATTRIBUTE8 | — | — |
| 66 | WorkOrderAnalyticsPEOPjcUserDefAttribute9 | PJC_USER_DEF_ATTRIBUTE9 | — | — |
| 67 | WorkOrderAnalyticsPEOPjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |
| 68 | WorkOrderAnalyticsPEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | ✅ |
| 69 | WorkOrderAnalyticsPEOPlannedStartDate | PLANNED_START_DATE | — | ✅ |
| 70 | WorkOrderAnalyticsPEOPlannedStartQuantity | PLANNED_START_QUANTITY | — | ✅ |
| 71 | WorkOrderAnalyticsPEORejectedQuantity | REJECTED_QUANTITY | — | ✅ |
| 72 | WorkOrderAnalyticsPEOReleasedDate | RELEASED_DATE | — | ✅ |
| 73 | WorkOrderAnalyticsPEORequestId | REQUEST_ID | — | ✅ |
| 74 | WorkOrderAnalyticsPEOSchedulingMethod | SCHEDULING_METHOD | — | — |
| 75 | WorkOrderAnalyticsPEOScoSupplyOrderId | SCO_SUPPLY_ORDER_ID | — | ✅ |
| 76 | WorkOrderAnalyticsPEOScrappedQuantity | SCRAPPED_QUANTITY | — | ✅ |
| 77 | WorkOrderAnalyticsPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | — |
| 78 | WorkOrderAnalyticsPEOSourceHeaderRef | SOURCE_HEADER_REF | — | — |
| 79 | WorkOrderAnalyticsPEOSourceHeaderRefId | SOURCE_HEADER_REF_ID | — | ✅ |
| 80 | WorkOrderAnalyticsPEOSourceLineRef | SOURCE_LINE_REF | — | — |
| 81 | WorkOrderAnalyticsPEOSourceLineRefId | SOURCE_LINE_REF_ID | — | ✅ |
| 82 | WorkOrderAnalyticsPEOSourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 83 | WorkOrderAnalyticsPEOSourceSystemType | SOURCE_SYSTEM_TYPE | — | — |
| 84 | WorkOrderAnalyticsPEOStatusChangeReason | STATUS_CHANGE_REASON | — | — |
| 85 | WorkOrderAnalyticsPEOSupplyType | SUPPLY_TYPE | — | — |
| 86 | WorkOrderAnalyticsPEOUomCode | UOM_CODE | — | — |
| 87 | WorkOrderAnalyticsPEOWorkDefinitionAsOfDate | WORK_DEFINITION_AS_OF_DATE | — | ✅ |
| 88 | WorkOrderAnalyticsPEOWorkDefinitionId | WORK_DEFINITION_ID | — | ✅ |
| 89 | WorkOrderAnalyticsPEOWorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | ✅ |
| 90 | WorkOrderAnalyticsPEOWorkMethodId | WORK_METHOD_ID | — | ✅ |
| 91 | WorkOrderAnalyticsPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 92 | WorkOrderAnalyticsPEOWorkOrderNumber | WORK_ORDER_NUMBER | — | — |
| 93 | WorkOrderAnalyticsPEOWorkOrderPriority | WORK_ORDER_PRIORITY | — | — |
| 94 | WorkOrderAnalyticsPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | ✅ |
| 95 | WorkOrderAnalyticsPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | — |
| 96 | WorkOrderAnalyticsPEOWorkOrderType | WORK_ORDER_TYPE | — | — |

### [[wie_wo_operation_resources|WIE_WO_OPERATION_RESOURCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WOOperationResourcePEOActualResourceUsage | ACTUAL_RESOURCE_USAGE | — | — |
| 2 | WOOperationResourcePEOAssignedUnits | ASSIGNED_UNITS | — | ✅ |
| 3 | WOOperationResourcePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | WOOperationResourcePEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 5 | WOOperationResourcePEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 6 | WOOperationResourcePEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 7 | WOOperationResourcePEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 8 | WOOperationResourcePEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 9 | WOOperationResourcePEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 10 | WOOperationResourcePEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 11 | WOOperationResourcePEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 12 | WOOperationResourcePEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 13 | WOOperationResourcePEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 14 | WOOperationResourcePEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 15 | WOOperationResourcePEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 16 | WOOperationResourcePEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 17 | WOOperationResourcePEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 18 | WOOperationResourcePEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 19 | WOOperationResourcePEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 20 | WOOperationResourcePEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 21 | WOOperationResourcePEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 22 | WOOperationResourcePEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 23 | WOOperationResourcePEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 24 | WOOperationResourcePEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 25 | WOOperationResourcePEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 26 | WOOperationResourcePEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 27 | WOOperationResourcePEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 28 | WOOperationResourcePEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 29 | WOOperationResourcePEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 30 | WOOperationResourcePEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 31 | WOOperationResourcePEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 32 | WOOperationResourcePEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 33 | WOOperationResourcePEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 34 | WOOperationResourcePEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 35 | WOOperationResourcePEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 36 | WOOperationResourcePEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 37 | WOOperationResourcePEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 38 | WOOperationResourcePEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 39 | WOOperationResourcePEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 40 | WOOperationResourcePEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 41 | WOOperationResourcePEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 42 | WOOperationResourcePEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 43 | WOOperationResourcePEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 44 | WOOperationResourcePEOBasisType | BASIS_TYPE | — | ✅ |
| 45 | WOOperationResourcePEOChargeType | CHARGE_TYPE | — | ✅ |
| 46 | WOOperationResourcePEOCreatedBy | CREATED_BY | — | — |
| 47 | WOOperationResourcePEOCreationDate | CREATION_DATE | — | — |
| 48 | WOOperationResourcePEOEqpQualProfileId | EQP_QUAL_PROFILE_ID | — | — |
| 49 | WOOperationResourcePEOInverseRequiredUsage | INVERSE_REQUIRED_USAGE | — | — |
| 50 | WOOperationResourcePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 51 | WOOperationResourcePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 52 | WOOperationResourcePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 53 | WOOperationResourcePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 54 | WOOperationResourcePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 55 | WOOperationResourcePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 56 | WOOperationResourcePEOOrganizationId | ORGANIZATION_ID | — | — |
| 57 | WOOperationResourcePEOPhantomFlag | PHANTOM_FLAG | — | — |
| 58 | WOOperationResourcePEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | ✅ |
| 59 | WOOperationResourcePEOPlannedStartDate | PLANNED_START_DATE | — | ✅ |
| 60 | WOOperationResourcePEOPrincipalFlag | PRINCIPAL_FLAG | — | ✅ |
| 61 | WOOperationResourcePEOProfileId | PROFILE_ID | — | — |
| 62 | WOOperationResourcePEORequestId | REQUEST_ID | — | — |
| 63 | WOOperationResourcePEORequiredUsage | REQUIRED_USAGE | — | ✅ |
| 64 | WOOperationResourcePEOResourceActivityCode | RESOURCE_ACTIVITY_CODE | — | ✅ |
| 65 | WOOperationResourcePEOResourceId | RESOURCE_ID | — | — |
| 66 | WOOperationResourcePEOResourceSeqNumber | RESOURCE_SEQ_NUMBER | — | ✅ |
| 67 | WOOperationResourcePEOScheduledFlag | SCHEDULED_FLAG | — | ✅ |
| 68 | WOOperationResourcePEOUomCode | UOM_CODE | — | — |
| 69 | WOOperationResourcePEOUsageRate | USAGE_RATE | — | ✅ |
| 70 | WOOperationResourcePEOWdOperationResourceId | WD_OPERATION_RESOURCE_ID | — | — |
| 71 | WOOperationResourcePEOWoOperationId | WO_OPERATION_ID | — | — |
| 72 | WOOperationResourcePEOWoOperationResourceId | WO_OPERATION_RESOURCE_ID | — | — |
| 73 | WOOperationResourcePEOWorkCenterId | WORK_CENTER_ID | — | — |

### [[wis_equipment_instances|WIS_EQUIPMENT_INSTANCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EquipmentInstancePEOAssetId | ASSET_ID | — | ✅ |
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
| 12 | LaborInstancePEOPartyId | PARTY_ID | — | ✅ |
| 13 | LaborInstancePEOResourceId | RESOURCE_ID | — | — |
| 14 | LaborInstancePEOWorkCenterId | WORK_CENTER_ID | — | — |

### [[wis_work_methods_vl|WIS_WORK_METHODS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkMethodPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | WorkMethodPEOWorkMethodCode | WORK_METHOD_CODE | — | — |
| 3 | WorkMethodPEOWorkMethodId | WORK_METHOD_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
