---
id: DOC-OTHER-PVO-WOOperationStartStopPVO
doc_type: system-doc
title: "WOOperationStartStopPVO — PVO Cross-Module"
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
  - WOOperationStartStopPVO
  - wooperationstartstoppvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WOOperationStartStopPVO

## 📌 Visão Geral

View Object para extração BICC de dados de WOOperation Start Stop. Acessa as tabelas: WIE_WORK_ORDERS_B, WIE_WO_OPERATIONS_B, WIE_WO_OPERATION_START_STOP (+1).

**Caminho:** `FscmTopModelAM.WorkOrderAM.WOOperationStartStopPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 247 | 4 | 3 | 70 | 28% |

---

## 🔗 Tabelas Relacionadas

- [[wie_work_orders_b|WIE_WORK_ORDERS_B]] — 103 atributos (30 BICC)
- [[wie_wo_operations_b|WIE_WO_OPERATIONS_B]] — 70 atributos (17 BICC)
- [[wie_wo_operation_start_stop|WIE_WO_OPERATION_START_STOP]] — 15 atributos (3 PKs, 13 BICC)
- [[wie_wo_product_serials|WIE_WO_PRODUCT_SERIALS]] — 59 atributos (10 BICC)

---

## ⚙️ Atributos

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
| 68 | WorkOrderAnalyticsPEONettableSupplyQtyOverride | NETTABLE_SUPPLY_QTY_OVERRIDE | — | — |
| 69 | WorkOrderAnalyticsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 70 | WorkOrderAnalyticsPEOOrchestrationCode | ORCHESTRATION_CODE | — | — |
| 71 | WorkOrderAnalyticsPEOOrderLessFlag | ORDER_LESS_FLAG | — | — |
| 72 | WorkOrderAnalyticsPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 73 | WorkOrderAnalyticsPEOOvercomplToleranceType | OVERCOMPL_TOLERANCE_TYPE | — | — |
| 74 | WorkOrderAnalyticsPEOOvercomplToleranceValue | OVERCOMPL_TOLERANCE_VALUE | — | — |
| 75 | WorkOrderAnalyticsPEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | ✅ |
| 76 | WorkOrderAnalyticsPEOPlannedStartDate | PLANNED_START_DATE | — | ✅ |
| 77 | WorkOrderAnalyticsPEOPlannedStartQuantity | PLANNED_START_QUANTITY | — | ✅ |
| 78 | WorkOrderAnalyticsPEORejectedQuantity | REJECTED_QUANTITY | — | ✅ |
| 79 | WorkOrderAnalyticsPEOReleasedDate | RELEASED_DATE | — | ✅ |
| 80 | WorkOrderAnalyticsPEORequestId | REQUEST_ID | — | ✅ |
| 81 | WorkOrderAnalyticsPEOSchedulingMethod | SCHEDULING_METHOD | — | — |
| 82 | WorkOrderAnalyticsPEOScoSupplyOrderId | SCO_SUPPLY_ORDER_ID | — | ✅ |
| 83 | WorkOrderAnalyticsPEOScrappedQuantity | SCRAPPED_QUANTITY | — | ✅ |
| 84 | WorkOrderAnalyticsPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | — |
| 85 | WorkOrderAnalyticsPEOSourceHeaderRef | SOURCE_HEADER_REF | — | — |
| 86 | WorkOrderAnalyticsPEOSourceHeaderRefId | SOURCE_HEADER_REF_ID | — | ✅ |
| 87 | WorkOrderAnalyticsPEOSourceLineRef | SOURCE_LINE_REF | — | — |
| 88 | WorkOrderAnalyticsPEOSourceLineRefId | SOURCE_LINE_REF_ID | — | ✅ |
| 89 | WorkOrderAnalyticsPEOSourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 90 | WorkOrderAnalyticsPEOSourceSystemType | SOURCE_SYSTEM_TYPE | — | — |
| 91 | WorkOrderAnalyticsPEOStatusChangeReason | STATUS_CHANGE_REASON | — | — |
| 92 | WorkOrderAnalyticsPEOSupplyType | SUPPLY_TYPE | — | — |
| 93 | WorkOrderAnalyticsPEOUomCode | UOM_CODE | — | — |
| 94 | WorkOrderAnalyticsPEOWorkDefinitionAsOfDate | WORK_DEFINITION_AS_OF_DATE | — | ✅ |
| 95 | WorkOrderAnalyticsPEOWorkDefinitionId | WORK_DEFINITION_ID | — | ✅ |
| 96 | WorkOrderAnalyticsPEOWorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | ✅ |
| 97 | WorkOrderAnalyticsPEOWorkMethodId | WORK_METHOD_ID | — | ✅ |
| 98 | WorkOrderAnalyticsPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 99 | WorkOrderAnalyticsPEOWorkOrderNumber | WORK_ORDER_NUMBER | — | — |
| 100 | WorkOrderAnalyticsPEOWorkOrderPriority | WORK_ORDER_PRIORITY | — | — |
| 101 | WorkOrderAnalyticsPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | ✅ |
| 102 | WorkOrderAnalyticsPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | — |
| 103 | WorkOrderAnalyticsPEOWorkOrderType | WORK_ORDER_TYPE | — | — |

### [[wie_wo_operations_b|WIE_WO_OPERATIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WOOperationAnalyticsPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 2 | WOOperationAnalyticsPEOActualStartDate | ACTUAL_START_DATE | — | ✅ |
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
| 45 | WOOperationAnalyticsPEOCompletedQuantity | COMPLETED_QUANTITY | — | ✅ |
| 46 | WOOperationAnalyticsPEOCountPointOperationFlag | COUNT_POINT_OPERATION_FLAG | — | — |
| 47 | WOOperationAnalyticsPEOCreatedBy | CREATED_BY | — | — |
| 48 | WOOperationAnalyticsPEOCreationDate | CREATION_DATE | — | ✅ |
| 49 | WOOperationAnalyticsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 50 | WOOperationAnalyticsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 51 | WOOperationAnalyticsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 52 | WOOperationAnalyticsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 53 | WOOperationAnalyticsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 54 | WOOperationAnalyticsPEONextCpOpSeqNum | NEXT_CP_OP_SEQ_NUM | — | — |
| 55 | WOOperationAnalyticsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 56 | WOOperationAnalyticsPEOOperationSeqNumber | OPERATION_SEQ_NUMBER | — | — |
| 57 | WOOperationAnalyticsPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 58 | WOOperationAnalyticsPEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | ✅ |
| 59 | WOOperationAnalyticsPEOPlannedStartDate | PLANNED_START_DATE | — | ✅ |
| 60 | WOOperationAnalyticsPEOPreviousCpOpSeqNum | PREVIOUS_CP_OP_SEQ_NUM | — | — |
| 61 | WOOperationAnalyticsPEOReadyQuantity | READY_QUANTITY | — | ✅ |
| 62 | WOOperationAnalyticsPEORejectedQuantity | REJECTED_QUANTITY | — | ✅ |
| 63 | WOOperationAnalyticsPEORequestId | REQUEST_ID | — | ✅ |
| 64 | WOOperationAnalyticsPEOScrappedQuantity | SCRAPPED_QUANTITY | — | ✅ |
| 65 | WOOperationAnalyticsPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | — |
| 66 | WOOperationAnalyticsPEOStandardOperationId | STANDARD_OPERATION_ID | — | ✅ |
| 67 | WOOperationAnalyticsPEOWdOperationId | WD_OPERATION_ID | — | ✅ |
| 68 | WOOperationAnalyticsPEOWoOperationId1 | WO_OPERATION_ID | — | ✅ |
| 69 | WOOperationAnalyticsPEOWorkCenterId | WORK_CENTER_ID | — | ✅ |
| 70 | WOOperationAnalyticsPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |

### [[wie_wo_operation_start_stop|WIE_WO_OPERATION_START_STOP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OperationStartTime | OPERATION_START_TIME | 🔑 | ✅ |
| 2 | WOOperationStartStopPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | WOOperationStartStopPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | WOOperationStartStopPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 5 | WOOperationStartStopPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 6 | WOOperationStartStopPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | WOOperationStartStopPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | WOOperationStartStopPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | WOOperationStartStopPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | WOOperationStartStopPEOOperationStopTime | OPERATION_STOP_TIME | — | ✅ |
| 11 | WOOperationStartStopPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 12 | WOOperationStartStopPEORequestId | REQUEST_ID | — | ✅ |
| 13 | WOOperationStartStopPEOWoOpStartStopId | WO_OP_START_STOP_ID | — | ✅ |
| 14 | WoOperationId | WO_OPERATION_ID | 🔑 | ✅ |
| 15 | WoProductSerialId | WO_PRODUCT_SERIAL_ID | 🔑 | ✅ |

### [[wie_wo_product_serials|WIE_WO_PRODUCT_SERIALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderProductSerialPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 2 | WorkOrderProductSerialPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 3 | WorkOrderProductSerialPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 4 | WorkOrderProductSerialPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 5 | WorkOrderProductSerialPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 6 | WorkOrderProductSerialPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 7 | WorkOrderProductSerialPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 8 | WorkOrderProductSerialPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 9 | WorkOrderProductSerialPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 10 | WorkOrderProductSerialPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 11 | WorkOrderProductSerialPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 12 | WorkOrderProductSerialPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 13 | WorkOrderProductSerialPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 14 | WorkOrderProductSerialPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 15 | WorkOrderProductSerialPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 16 | WorkOrderProductSerialPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 17 | WorkOrderProductSerialPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 18 | WorkOrderProductSerialPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 19 | WorkOrderProductSerialPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 20 | WorkOrderProductSerialPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 21 | WorkOrderProductSerialPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 22 | WorkOrderProductSerialPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | WorkOrderProductSerialPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 24 | WorkOrderProductSerialPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 25 | WorkOrderProductSerialPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 26 | WorkOrderProductSerialPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 27 | WorkOrderProductSerialPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 28 | WorkOrderProductSerialPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 29 | WorkOrderProductSerialPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 30 | WorkOrderProductSerialPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 31 | WorkOrderProductSerialPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 32 | WorkOrderProductSerialPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 33 | WorkOrderProductSerialPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 34 | WorkOrderProductSerialPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 35 | WorkOrderProductSerialPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 36 | WorkOrderProductSerialPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 37 | WorkOrderProductSerialPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 38 | WorkOrderProductSerialPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 39 | WorkOrderProductSerialPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 40 | WorkOrderProductSerialPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 41 | WorkOrderProductSerialPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 42 | WorkOrderProductSerialPEOCreatedBy | CREATED_BY | — | — |
| 43 | WorkOrderProductSerialPEOCreationDate | CREATION_DATE | — | ✅ |
| 44 | WorkOrderProductSerialPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 45 | WorkOrderProductSerialPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 46 | WorkOrderProductSerialPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 47 | WorkOrderProductSerialPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 48 | WorkOrderProductSerialPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 49 | WorkOrderProductSerialPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 50 | WorkOrderProductSerialPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 51 | WorkOrderProductSerialPEOOperationSeqNumber | OPERATION_SEQ_NUMBER | — | — |
| 52 | WorkOrderProductSerialPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 53 | WorkOrderProductSerialPEORequestId | REQUEST_ID | — | ✅ |
| 54 | WorkOrderProductSerialPEOSerialNumber | SERIAL_NUMBER | — | ✅ |
| 55 | WorkOrderProductSerialPEOSerialStatus | SERIAL_STATUS | — | — |
| 56 | WorkOrderProductSerialPEOWoOperationId | WO_OPERATION_ID | — | ✅ |
| 57 | WorkOrderProductSerialPEOWoOperationMaterialId | WO_OPERATION_MATERIAL_ID | — | ✅ |
| 58 | WorkOrderProductSerialPEOWoProductSerialId | WO_PRODUCT_SERIAL_ID | — | ✅ |
| 59 | WorkOrderProductSerialPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
