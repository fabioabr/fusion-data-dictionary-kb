---
id: DOC-OTHER-PVO-MaintenanceWOOperationTransactionsPVO
doc_type: system-doc
title: "MaintenanceWOOperationTransactionsPVO — PVO Cross-Module"
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
  - MaintenanceWOOperationTransactionsPVO
  - maintenancewooperationtransactionspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MaintenanceWOOperationTransactionsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Maintenance WOOperation Transactions. Acessa as tabelas: WIE_OPERATION_TRANSACTIONS, WIE_TRANSACTION_SERIALS, WIE_WORK_ORDERS_B (+4).

**Caminho:** `FscmTopModelAM.WOOperationTransactionsAM.MaintenanceWOOperationTransactionsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 283 | 7 | 1 | 81 | 29% |

---

## 🔗 Tabelas Relacionadas

- [[wie_operation_transactions|WIE_OPERATION_TRANSACTIONS]] — 40 atributos (1 PKs, 24 BICC)
- [[wie_transaction_serials|WIE_TRANSACTION_SERIALS]] — 16 atributos (10 BICC)
- [[wie_work_orders_b|WIE_WORK_ORDERS_B]] — 142 atributos (30 BICC)
- [[wie_wo_operations_b|WIE_WO_OPERATIONS_B]] — 43 atributos (17 BICC)
- [[wie_wo_product_lots|WIE_WO_PRODUCT_LOTS]] — 15 atributos
- [[wie_wo_reservations_v|WIE_WO_RESERVATIONS_V]] — 24 atributos
- [[wis_work_methods_vl|WIS_WORK_METHODS_VL]] — 3 atributos

---

## ⚙️ Atributos

### [[wie_operation_transactions|WIE_OPERATION_TRANSACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OperationTransactionPEOComplLocatorId | COMPL_LOCATOR_ID | — | ✅ |
| 2 | OperationTransactionPEOComplSubinventoryCode | COMPL_SUBINVENTORY_CODE | — | — |
| 3 | OperationTransactionPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | OperationTransactionPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | OperationTransactionPEOCstInterfacedFlag | CST_INTERFACED_FLAG | — | — |
| 6 | OperationTransactionPEOFromDispatchState | FROM_DISPATCH_STATE | — | — |
| 7 | OperationTransactionPEOInterfaceBatchId | INTERFACE_BATCH_ID | — | ✅ |
| 8 | OperationTransactionPEOInterfaceRowId | INTERFACE_ROW_ID | — | ✅ |
| 9 | OperationTransactionPEOInvTransactionId | INV_TRANSACTION_ID | — | ✅ |
| 10 | OperationTransactionPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 11 | OperationTransactionPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 12 | OperationTransactionPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 13 | OperationTransactionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | OperationTransactionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | OperationTransactionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | OperationTransactionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | OperationTransactionPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 18 | OperationTransactionPEOPoHeaderId | PO_HEADER_ID | — | ✅ |
| 19 | OperationTransactionPEOPoLineId | PO_LINE_ID | — | ✅ |
| 20 | OperationTransactionPEOPrimaryQuantity | PRIMARY_QUANTITY | — | ✅ |
| 21 | OperationTransactionPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | — |
| 22 | OperationTransactionPEOReasonCode | REASON_CODE | — | — |
| 23 | OperationTransactionPEORequestId | REQUEST_ID | — | ✅ |
| 24 | OperationTransactionPEOSourceHeaderRef | SOURCE_HEADER_REF | — | — |
| 25 | OperationTransactionPEOSourceHeaderRefId | SOURCE_HEADER_REF_ID | — | ✅ |
| 26 | OperationTransactionPEOSourceLineRef | SOURCE_LINE_REF | — | — |
| 27 | OperationTransactionPEOSourceLineRefId | SOURCE_LINE_REF_ID | — | ✅ |
| 28 | OperationTransactionPEOSourceSystemCode | SOURCE_SYSTEM_CODE | — | — |
| 29 | OperationTransactionPEOSourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 30 | OperationTransactionPEOSourceSystemType | SOURCE_SYSTEM_TYPE | — | — |
| 31 | OperationTransactionPEOToDispatchState | TO_DISPATCH_STATE | — | — |
| 32 | OperationTransactionPEOTransactionDate | TRANSACTION_DATE | — | ✅ |
| 33 | OperationTransactionPEOTransactionNote | TRANSACTION_NOTE | — | ✅ |
| 34 | OperationTransactionPEOTransactionQuantity | TRANSACTION_QUANTITY | — | ✅ |
| 35 | OperationTransactionPEOTransactionTypeCode | TRANSACTION_TYPE_CODE | — | — |
| 36 | OperationTransactionPEOTransactionUomCode | TRANSACTION_UOM_CODE | — | ✅ |
| 37 | OperationTransactionPEOWoOperationId | WO_OPERATION_ID | — | ✅ |
| 38 | OperationTransactionPEOWoOperationTransactionId | WO_OPERATION_TRANSACTION_ID | 🔑 | ✅ |
| 39 | OperationTransactionPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 40 | OperationTransactionPEOWorkstationId | WORKSTATION_ID | — | — |

### [[wie_transaction_serials|WIE_TRANSACTION_SERIALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WOTransactionSerialsPEOCreatedBy | CREATED_BY | — | — |
| 2 | WOTransactionSerialsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | WOTransactionSerialsPEOInterfaceBatchId | INTERFACE_BATCH_ID | — | ✅ |
| 4 | WOTransactionSerialsPEOInterfaceRowId | INTERFACE_ROW_ID | — | ✅ |
| 5 | WOTransactionSerialsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 6 | WOTransactionSerialsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | WOTransactionSerialsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | WOTransactionSerialsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | WOTransactionSerialsPEOLotNumber | LOT_NUMBER | — | — |
| 10 | WOTransactionSerialsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | WOTransactionSerialsPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 12 | WOTransactionSerialsPEOParentSerialNumber | PARENT_SERIAL_NUMBER | — | — |
| 13 | WOTransactionSerialsPEOSerialNumber | SERIAL_NUMBER | — | ✅ |
| 14 | WOTransactionSerialsPEOWoLotTransactionId | WO_LOT_TRANSACTION_ID | — | ✅ |
| 15 | WOTransactionSerialsPEOWoSerialTransactionId | WO_SERIAL_TRANSACTION_ID | — | ✅ |
| 16 | WOTransactionSerialsPEOWoTransactionId | WO_TRANSACTION_ID | — | ✅ |

### [[wie_work_orders_b|WIE_WORK_ORDERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderAnalyticsPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 2 | WorkOrderAnalyticsPEOActualStartDate | ACTUAL_START_DATE | — | ✅ |
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
| 45 | WorkOrderAnalyticsPEOCanceledDate | CANCELED_DATE | — | ✅ |
| 46 | WorkOrderAnalyticsPEOCanceledReason | CANCELED_REASON | — | — |
| 47 | WorkOrderAnalyticsPEOClosedDate | CLOSED_DATE | — | ✅ |
| 48 | WorkOrderAnalyticsPEOCmPoHeaderId | CM_PO_HEADER_ID | — | ✅ |
| 49 | WorkOrderAnalyticsPEOCmPoLineId | CM_PO_LINE_ID | — | ✅ |
| 50 | WorkOrderAnalyticsPEOCmPoLineLocId | CM_PO_LINE_LOC_ID | — | ✅ |
| 51 | WorkOrderAnalyticsPEOComplLocatorId | COMPL_LOCATOR_ID | — | ✅ |
| 52 | WorkOrderAnalyticsPEOComplSubinventoryCode | COMPL_SUBINVENTORY_CODE | — | — |
| 53 | WorkOrderAnalyticsPEOCompletedQuantity | COMPLETED_QUANTITY | — | ✅ |
| 54 | WorkOrderAnalyticsPEOContractMfgFlag | CONTRACT_MFG_FLAG | — | — |
| 55 | WorkOrderAnalyticsPEOCreatedBy | CREATED_BY | — | — |
| 56 | WorkOrderAnalyticsPEOCreationDate | CREATION_DATE | — | ✅ |
| 57 | WorkOrderAnalyticsPEOFirmPlannedFlag | FIRM_PLANNED_FLAG | — | — |
| 58 | WorkOrderAnalyticsPEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | — |
| 59 | WorkOrderAnalyticsPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 60 | WorkOrderAnalyticsPEOItemRevision | ITEM_REVISION | — | — |
| 61 | WorkOrderAnalyticsPEOItemStructureName | ITEM_STRUCTURE_NAME | — | — |
| 62 | WorkOrderAnalyticsPEOItemVersion | ITEM_VERSION | — | — |
| 63 | WorkOrderAnalyticsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 64 | WorkOrderAnalyticsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 65 | WorkOrderAnalyticsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 66 | WorkOrderAnalyticsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 67 | WorkOrderAnalyticsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 68 | WorkOrderAnalyticsPEONeedByDate | NEED_BY_DATE | — | — |
| 69 | WorkOrderAnalyticsPEONettableSupplyQtyOverride | NETTABLE_SUPPLY_QTY_OVERRIDE | — | — |
| 70 | WorkOrderAnalyticsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 71 | WorkOrderAnalyticsPEOOrchestrationCode | ORCHESTRATION_CODE | — | — |
| 72 | WorkOrderAnalyticsPEOOrderLessFlag | ORDER_LESS_FLAG | — | — |
| 73 | WorkOrderAnalyticsPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 74 | WorkOrderAnalyticsPEOOvercomplToleranceType | OVERCOMPL_TOLERANCE_TYPE | — | — |
| 75 | WorkOrderAnalyticsPEOOvercomplToleranceValue | OVERCOMPL_TOLERANCE_VALUE | — | — |
| 76 | WorkOrderAnalyticsPEOPjcBillableFlag | PJC_BILLABLE_FLAG | — | — |
| 77 | WorkOrderAnalyticsPEOPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | — |
| 78 | WorkOrderAnalyticsPEOPjcContextCategory | PJC_CONTEXT_CATEGORY | — | — |
| 79 | WorkOrderAnalyticsPEOPjcContractId | PJC_CONTRACT_ID | — | — |
| 80 | WorkOrderAnalyticsPEOPjcContractLineId | PJC_CONTRACT_LINE_ID | — | — |
| 81 | WorkOrderAnalyticsPEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 82 | WorkOrderAnalyticsPEOPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | — |
| 83 | WorkOrderAnalyticsPEOPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | — |
| 84 | WorkOrderAnalyticsPEOPjcOrganizationId | PJC_ORGANIZATION_ID | — | — |
| 85 | WorkOrderAnalyticsPEOPjcProjectId | PJC_PROJECT_ID | — | — |
| 86 | WorkOrderAnalyticsPEOPjcProjectNumber | PJC_PROJECT_NUMBER | — | — |
| 87 | WorkOrderAnalyticsPEOPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 88 | WorkOrderAnalyticsPEOPjcReservedAttribute10 | PJC_RESERVED_ATTRIBUTE10 | — | — |
| 89 | WorkOrderAnalyticsPEOPjcReservedAttribute2 | PJC_RESERVED_ATTRIBUTE2 | — | — |
| 90 | WorkOrderAnalyticsPEOPjcReservedAttribute3 | PJC_RESERVED_ATTRIBUTE3 | — | — |
| 91 | WorkOrderAnalyticsPEOPjcReservedAttribute4 | PJC_RESERVED_ATTRIBUTE4 | — | — |
| 92 | WorkOrderAnalyticsPEOPjcReservedAttribute5 | PJC_RESERVED_ATTRIBUTE5 | — | — |
| 93 | WorkOrderAnalyticsPEOPjcReservedAttribute6 | PJC_RESERVED_ATTRIBUTE6 | — | — |
| 94 | WorkOrderAnalyticsPEOPjcReservedAttribute7 | PJC_RESERVED_ATTRIBUTE7 | — | — |
| 95 | WorkOrderAnalyticsPEOPjcReservedAttribute8 | PJC_RESERVED_ATTRIBUTE8 | — | — |
| 96 | WorkOrderAnalyticsPEOPjcReservedAttribute9 | PJC_RESERVED_ATTRIBUTE9 | — | — |
| 97 | WorkOrderAnalyticsPEOPjcTaskId | PJC_TASK_ID | — | — |
| 98 | WorkOrderAnalyticsPEOPjcTaskNumber | PJC_TASK_NUMBER | — | — |
| 99 | WorkOrderAnalyticsPEOPjcUserDefAttribute1 | PJC_USER_DEF_ATTRIBUTE1 | — | — |
| 100 | WorkOrderAnalyticsPEOPjcUserDefAttribute10 | PJC_USER_DEF_ATTRIBUTE10 | — | — |
| 101 | WorkOrderAnalyticsPEOPjcUserDefAttribute2 | PJC_USER_DEF_ATTRIBUTE2 | — | — |
| 102 | WorkOrderAnalyticsPEOPjcUserDefAttribute3 | PJC_USER_DEF_ATTRIBUTE3 | — | — |
| 103 | WorkOrderAnalyticsPEOPjcUserDefAttribute4 | PJC_USER_DEF_ATTRIBUTE4 | — | — |
| 104 | WorkOrderAnalyticsPEOPjcUserDefAttribute5 | PJC_USER_DEF_ATTRIBUTE5 | — | — |
| 105 | WorkOrderAnalyticsPEOPjcUserDefAttribute6 | PJC_USER_DEF_ATTRIBUTE6 | — | — |
| 106 | WorkOrderAnalyticsPEOPjcUserDefAttribute7 | PJC_USER_DEF_ATTRIBUTE7 | — | — |
| 107 | WorkOrderAnalyticsPEOPjcUserDefAttribute8 | PJC_USER_DEF_ATTRIBUTE8 | — | — |
| 108 | WorkOrderAnalyticsPEOPjcUserDefAttribute9 | PJC_USER_DEF_ATTRIBUTE9 | — | — |
| 109 | WorkOrderAnalyticsPEOPjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |
| 110 | WorkOrderAnalyticsPEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | ✅ |
| 111 | WorkOrderAnalyticsPEOPlannedStartDate | PLANNED_START_DATE | — | ✅ |
| 112 | WorkOrderAnalyticsPEOPlannedStartQuantity | PLANNED_START_QUANTITY | — | ✅ |
| 113 | WorkOrderAnalyticsPEOPreassignLotFlag | PREASSIGN_LOT_FLAG | — | — |
| 114 | WorkOrderAnalyticsPEOPrimaryProductQuantity | PRIMARY_PRODUCT_QUANTITY | — | — |
| 115 | WorkOrderAnalyticsPEOPrimaryProductUomCode | PRIMARY_PRODUCT_UOM_CODE | — | — |
| 116 | WorkOrderAnalyticsPEORejectedQuantity | REJECTED_QUANTITY | — | ✅ |
| 117 | WorkOrderAnalyticsPEOReleasedDate | RELEASED_DATE | — | ✅ |
| 118 | WorkOrderAnalyticsPEORequestId | REQUEST_ID | — | ✅ |
| 119 | WorkOrderAnalyticsPEOSchedulingMethod | SCHEDULING_METHOD | — | — |
| 120 | WorkOrderAnalyticsPEOScoSupplyOrderId | SCO_SUPPLY_ORDER_ID | — | ✅ |
| 121 | WorkOrderAnalyticsPEOScrappedQuantity | SCRAPPED_QUANTITY | — | ✅ |
| 122 | WorkOrderAnalyticsPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | ✅ |
| 123 | WorkOrderAnalyticsPEOSourceHeaderRef | SOURCE_HEADER_REF | — | — |
| 124 | WorkOrderAnalyticsPEOSourceHeaderRefId | SOURCE_HEADER_REF_ID | — | ✅ |
| 125 | WorkOrderAnalyticsPEOSourceLineRef | SOURCE_LINE_REF | — | — |
| 126 | WorkOrderAnalyticsPEOSourceLineRefId | SOURCE_LINE_REF_ID | — | ✅ |
| 127 | WorkOrderAnalyticsPEOSourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 128 | WorkOrderAnalyticsPEOSourceSystemType | SOURCE_SYSTEM_TYPE | — | — |
| 129 | WorkOrderAnalyticsPEOStatusChangeReason | STATUS_CHANGE_REASON | — | — |
| 130 | WorkOrderAnalyticsPEOSupplyType | SUPPLY_TYPE | — | — |
| 131 | WorkOrderAnalyticsPEOUnderCompletedFlag | UNDER_COMPLETED_FLAG | — | — |
| 132 | WorkOrderAnalyticsPEOUomCode | UOM_CODE | — | — |
| 133 | WorkOrderAnalyticsPEOWorkDefinitionAsOfDate | WORK_DEFINITION_AS_OF_DATE | — | — |
| 134 | WorkOrderAnalyticsPEOWorkDefinitionId | WORK_DEFINITION_ID | — | ✅ |
| 135 | WorkOrderAnalyticsPEOWorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | ✅ |
| 136 | WorkOrderAnalyticsPEOWorkMethodId | WORK_METHOD_ID | — | ✅ |
| 137 | WorkOrderAnalyticsPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 138 | WorkOrderAnalyticsPEOWorkOrderNumber | WORK_ORDER_NUMBER | — | — |
| 139 | WorkOrderAnalyticsPEOWorkOrderPriority | WORK_ORDER_PRIORITY | — | — |
| 140 | WorkOrderAnalyticsPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | ✅ |
| 141 | WorkOrderAnalyticsPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | — |
| 142 | WorkOrderAnalyticsPEOWorkOrderType | WORK_ORDER_TYPE | — | — |

### [[wie_wo_operations_b|WIE_WO_OPERATIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WOOperationAnalyticsPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 2 | WOOperationAnalyticsPEOActualStartDate | ACTUAL_START_DATE | — | ✅ |
| 3 | WOOperationAnalyticsPEOAutoTransactFlag | AUTO_TRANSACT_FLAG | — | — |
| 4 | WOOperationAnalyticsPEOCompletedQuantity | COMPLETED_QUANTITY | — | ✅ |
| 5 | WOOperationAnalyticsPEOCountPointOperationFlag | COUNT_POINT_OPERATION_FLAG | — | — |
| 6 | WOOperationAnalyticsPEOCreatedBy | CREATED_BY | — | — |
| 7 | WOOperationAnalyticsPEOCreationDate | CREATION_DATE | — | ✅ |
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
| 20 | WOOperationAnalyticsPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 21 | WOOperationAnalyticsPEOOspItemId | OSP_ITEM_ID | — | — |
| 22 | WOOperationAnalyticsPEOOverReceiptQuantity | OVER_RECEIPT_QUANTITY | — | — |
| 23 | WOOperationAnalyticsPEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | ✅ |
| 24 | WOOperationAnalyticsPEOPlannedStartDate | PLANNED_START_DATE | — | ✅ |
| 25 | WOOperationAnalyticsPEOPoApprovedQuantity | PO_APPROVED_QUANTITY | — | — |
| 26 | WOOperationAnalyticsPEOPoRequestedQuantity | PO_REQUESTED_QUANTITY | — | — |
| 27 | WOOperationAnalyticsPEOPreviousCpOpSeqNum | PREVIOUS_CP_OP_SEQ_NUM | — | — |
| 28 | WOOperationAnalyticsPEOReadyQuantity | READY_QUANTITY | — | ✅ |
| 29 | WOOperationAnalyticsPEOReceivedQuantity | RECEIVED_QUANTITY | — | — |
| 30 | WOOperationAnalyticsPEORejectedQuantity | REJECTED_QUANTITY | — | ✅ |
| 31 | WOOperationAnalyticsPEORequestId | REQUEST_ID | — | ✅ |
| 32 | WOOperationAnalyticsPEOScrappedQuantity | SCRAPPED_QUANTITY | — | ✅ |
| 33 | WOOperationAnalyticsPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | — |
| 34 | WOOperationAnalyticsPEOShippedQuantity | SHIPPED_QUANTITY | — | — |
| 35 | WOOperationAnalyticsPEOShippingDocumentsFlag | SHIPPING_DOCUMENTS_FLAG | — | — |
| 36 | WOOperationAnalyticsPEOStandardOperationId | STANDARD_OPERATION_ID | — | ✅ |
| 37 | WOOperationAnalyticsPEOSupplierId | SUPPLIER_ID | — | — |
| 38 | WOOperationAnalyticsPEOSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 39 | WOOperationAnalyticsPEOVariableLeadTime | VARIABLE_LEAD_TIME | — | — |
| 40 | WOOperationAnalyticsPEOWdOperationId | WD_OPERATION_ID | — | ✅ |
| 41 | WOOperationAnalyticsPEOWoOperationId | WO_OPERATION_ID | — | ✅ |
| 42 | WOOperationAnalyticsPEOWorkCenterId | WORK_CENTER_ID | — | ✅ |
| 43 | WOOperationAnalyticsPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |

### [[wie_wo_product_lots|WIE_WO_PRODUCT_LOTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderProductLotPEOCreatedBy | CREATED_BY | — | — |
| 2 | WorkOrderProductLotPEOCreationDate | CREATION_DATE | — | — |
| 3 | WorkOrderProductLotPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 4 | WorkOrderProductLotPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 5 | WorkOrderProductLotPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 6 | WorkOrderProductLotPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | WorkOrderProductLotPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | WorkOrderProductLotPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | WorkOrderProductLotPEOLotNumber | LOT_NUMBER | — | — |
| 10 | WorkOrderProductLotPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | WorkOrderProductLotPEOOrganizationId | ORGANIZATION_ID | — | — |
| 12 | WorkOrderProductLotPEORequestId | REQUEST_ID | — | — |
| 13 | WorkOrderProductLotPEOWoOperationOutputId | WO_OPERATION_OUTPUT_ID | — | — |
| 14 | WorkOrderProductLotPEOWoProductLotId | WO_PRODUCT_LOT_ID | — | — |
| 15 | WorkOrderProductLotPEOWorkOrderId | WORK_ORDER_ID | — | — |

### [[wie_wo_reservations_v|WIE_WO_RESERVATIONS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderReservationsPEOAttachmentEntityName | ATTACHMENT_ENTITY_NAME | — | — |
| 2 | WorkOrderReservationsPEOCustomerName | CUSTOMER_NAME | — | — |
| 3 | WorkOrderReservationsPEOCustomerNumber | CUSTOMER_NUMBER | — | — |
| 4 | WorkOrderReservationsPEOCustomerType | CUSTOMER_TYPE | — | — |
| 5 | WorkOrderReservationsPEODemandQuantity | DEMAND_QUANTITY | — | — |
| 6 | WorkOrderReservationsPEODemandSourceHeaderId | DEMAND_SOURCE_HEADER_ID | — | — |
| 7 | WorkOrderReservationsPEODemandSourceHeaderNumber | DEMAND_SOURCE_HEADER_NUMBER | — | — |
| 8 | WorkOrderReservationsPEODemandSourceLineId | DEMAND_SOURCE_LINE_ID | — | — |
| 9 | WorkOrderReservationsPEODemandSourceLineNumber | DEMAND_SOURCE_LINE_NUMBER | — | — |
| 10 | WorkOrderReservationsPEODemandSourceName | DEMAND_SOURCE_NAME | — | — |
| 11 | WorkOrderReservationsPEODemandSourceTypeId | DEMAND_SOURCE_TYPE_ID | — | — |
| 12 | WorkOrderReservationsPEODemandSourceTypeIdDerived | DEMAND_SOURCE_TYPE_ID_DERIVED | — | — |
| 13 | WorkOrderReservationsPEODemandUom | DEMAND_UOM | — | — |
| 14 | WorkOrderReservationsPEODueDate | DUE_DATE | — | — |
| 15 | WorkOrderReservationsPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 16 | WorkOrderReservationsPEOLineEntityName | LINE_ENTITY_NAME | — | — |
| 17 | WorkOrderReservationsPEOOrganizationId | ORGANIZATION_ID | — | — |
| 18 | WorkOrderReservationsPEOPrimaryReservationQuantity | PRIMARY_RESERVATION_QUANTITY | — | — |
| 19 | WorkOrderReservationsPEOPrimaryUomCode | PRIMARY_UOM_CODE | — | — |
| 20 | WorkOrderReservationsPEOReservationId | RESERVATION_ID | — | — |
| 21 | WorkOrderReservationsPEOReservationQuantity | RESERVATION_QUANTITY | — | — |
| 22 | WorkOrderReservationsPEOReservationUomCode | RESERVATION_UOM_CODE | — | — |
| 23 | WorkOrderReservationsPEOSrcFulfillLineId | SRC_FULFILL_LINE_ID | — | — |
| 24 | WorkOrderReservationsPEOSupplySourceHeaderId | SUPPLY_SOURCE_HEADER_ID | — | — |

### [[wis_work_methods_vl|WIS_WORK_METHODS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkMethodPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | WorkMethodPEOWorkMethodCode | WORK_METHOD_CODE | — | — |
| 3 | WorkMethodPEOWorkMethodId | WORK_METHOD_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
