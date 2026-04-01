---
id: DOC-OTHER-PVO-WOOperationStartStopDistinctPVO
doc_type: system-doc
title: "WOOperationStartStopDistinctPVO — PVO Cross-Module"
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
  - WOOperationStartStopDistinctPVO
  - wooperationstartstopdistinctpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WOOperationStartStopDistinctPVO

## 📌 Visão Geral

View Object para extração BICC de dados de WOOperation Start Stop Distinct. Acessa as tabelas: WIE_WORK_ORDERS_B, WIE_WO_OPERATIONS_B, WIE_WO_OPERATION_START_STOP_V.

**Caminho:** `FscmTopModelAM.WorkOrderAM.WOOperationStartStopDistinctPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 177 | 3 | 3 | 50 | 28% |

---

## 🔗 Tabelas Relacionadas

- [[wie_work_orders_b|WIE_WORK_ORDERS_B]] — 104 atributos (30 BICC)
- [[wie_wo_operations_b|WIE_WO_OPERATIONS_B]] — 70 atributos (17 BICC)
- [[wie_wo_operation_start_stop_v|WIE_WO_OPERATION_START_STOP_V]] — 3 atributos (3 PKs, 3 BICC)

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
| 68 | WorkOrderAnalyticsPEONeedByDate | NEED_BY_DATE | — | — |
| 69 | WorkOrderAnalyticsPEONettableSupplyQtyOverride | NETTABLE_SUPPLY_QTY_OVERRIDE | — | — |
| 70 | WorkOrderAnalyticsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 71 | WorkOrderAnalyticsPEOOrchestrationCode | ORCHESTRATION_CODE | — | — |
| 72 | WorkOrderAnalyticsPEOOrderLessFlag | ORDER_LESS_FLAG | — | — |
| 73 | WorkOrderAnalyticsPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 74 | WorkOrderAnalyticsPEOOvercomplToleranceType | OVERCOMPL_TOLERANCE_TYPE | — | — |
| 75 | WorkOrderAnalyticsPEOOvercomplToleranceValue | OVERCOMPL_TOLERANCE_VALUE | — | — |
| 76 | WorkOrderAnalyticsPEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | ✅ |
| 77 | WorkOrderAnalyticsPEOPlannedStartDate | PLANNED_START_DATE | — | ✅ |
| 78 | WorkOrderAnalyticsPEOPlannedStartQuantity | PLANNED_START_QUANTITY | — | ✅ |
| 79 | WorkOrderAnalyticsPEORejectedQuantity | REJECTED_QUANTITY | — | ✅ |
| 80 | WorkOrderAnalyticsPEOReleasedDate | RELEASED_DATE | — | ✅ |
| 81 | WorkOrderAnalyticsPEORequestId | REQUEST_ID | — | ✅ |
| 82 | WorkOrderAnalyticsPEOSchedulingMethod | SCHEDULING_METHOD | — | — |
| 83 | WorkOrderAnalyticsPEOScoSupplyOrderId | SCO_SUPPLY_ORDER_ID | — | ✅ |
| 84 | WorkOrderAnalyticsPEOScrappedQuantity | SCRAPPED_QUANTITY | — | ✅ |
| 85 | WorkOrderAnalyticsPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | — |
| 86 | WorkOrderAnalyticsPEOSourceHeaderRef | SOURCE_HEADER_REF | — | — |
| 87 | WorkOrderAnalyticsPEOSourceHeaderRefId | SOURCE_HEADER_REF_ID | — | ✅ |
| 88 | WorkOrderAnalyticsPEOSourceLineRef | SOURCE_LINE_REF | — | — |
| 89 | WorkOrderAnalyticsPEOSourceLineRefId | SOURCE_LINE_REF_ID | — | ✅ |
| 90 | WorkOrderAnalyticsPEOSourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 91 | WorkOrderAnalyticsPEOSourceSystemType | SOURCE_SYSTEM_TYPE | — | — |
| 92 | WorkOrderAnalyticsPEOStatusChangeReason | STATUS_CHANGE_REASON | — | — |
| 93 | WorkOrderAnalyticsPEOSupplyType | SUPPLY_TYPE | — | — |
| 94 | WorkOrderAnalyticsPEOUomCode | UOM_CODE | — | — |
| 95 | WorkOrderAnalyticsPEOWorkDefinitionAsOfDate | WORK_DEFINITION_AS_OF_DATE | — | ✅ |
| 96 | WorkOrderAnalyticsPEOWorkDefinitionId | WORK_DEFINITION_ID | — | ✅ |
| 97 | WorkOrderAnalyticsPEOWorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | ✅ |
| 98 | WorkOrderAnalyticsPEOWorkMethodId | WORK_METHOD_ID | — | ✅ |
| 99 | WorkOrderAnalyticsPEOWorkOrderId1 | WORK_ORDER_ID | — | ✅ |
| 100 | WorkOrderAnalyticsPEOWorkOrderNumber | WORK_ORDER_NUMBER | — | — |
| 101 | WorkOrderAnalyticsPEOWorkOrderPriority | WORK_ORDER_PRIORITY | — | — |
| 102 | WorkOrderAnalyticsPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | ✅ |
| 103 | WorkOrderAnalyticsPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | — |
| 104 | WorkOrderAnalyticsPEOWorkOrderType | WORK_ORDER_TYPE | — | — |

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
| 70 | WOOperationAnalyticsPEOWorkOrderId1 | WORK_ORDER_ID | — | ✅ |

### [[wie_wo_operation_start_stop_v|WIE_WO_OPERATION_START_STOP_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WoOperationId | WO_OPERATION_ID | 🔑 | ✅ |
| 2 | WoProductSerialId | WO_PRODUCT_SERIAL_ID | 🔑 | ✅ |
| 3 | WorkOrderId | WORK_ORDER_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
