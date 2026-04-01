---
id: DOC-OTHER-PVO-WorkOrderProductSerialPVO
doc_type: system-doc
title: "WorkOrderProductSerialPVO — PVO Cross-Module"
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
  - WorkOrderProductSerialPVO
  - workorderproductserialpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkOrderProductSerialPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Work Order Product Serial. Acessa as tabelas: WIE_WORK_ORDERS_B, WIE_WO_PRODUCT_SERIALS.

**Caminho:** `FscmTopModelAM.WorkOrderAM.WorkOrderProductSerialPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 81 | 2 | 1 | 41 | 51% |

---

## 🔗 Tabelas Relacionadas

- [[wie_work_orders_b|WIE_WORK_ORDERS_B]] — 63 atributos (31 BICC)
- [[wie_wo_product_serials|WIE_WO_PRODUCT_SERIALS]] — 18 atributos (1 PKs, 10 BICC)

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
| 34 | WorkOrderAnalyticsPEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | ✅ |
| 35 | WorkOrderAnalyticsPEOPlannedStartDate | PLANNED_START_DATE | — | ✅ |
| 36 | WorkOrderAnalyticsPEOPlannedStartQuantity | PLANNED_START_QUANTITY | — | ✅ |
| 37 | WorkOrderAnalyticsPEORejectedQuantity | REJECTED_QUANTITY | — | ✅ |
| 38 | WorkOrderAnalyticsPEOReleasedDate | RELEASED_DATE | — | ✅ |
| 39 | WorkOrderAnalyticsPEORequestId | REQUEST_ID | — | ✅ |
| 40 | WorkOrderAnalyticsPEOSchedulingMethod | SCHEDULING_METHOD | — | — |
| 41 | WorkOrderAnalyticsPEOScoSupplyOrderId | SCO_SUPPLY_ORDER_ID | — | ✅ |
| 42 | WorkOrderAnalyticsPEOScrappedQuantity | SCRAPPED_QUANTITY | — | ✅ |
| 43 | WorkOrderAnalyticsPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | — |
| 44 | WorkOrderAnalyticsPEOSourceHeaderRef | SOURCE_HEADER_REF | — | — |
| 45 | WorkOrderAnalyticsPEOSourceHeaderRefId | SOURCE_HEADER_REF_ID | — | ✅ |
| 46 | WorkOrderAnalyticsPEOSourceLineRef | SOURCE_LINE_REF | — | — |
| 47 | WorkOrderAnalyticsPEOSourceLineRefId | SOURCE_LINE_REF_ID | — | ✅ |
| 48 | WorkOrderAnalyticsPEOSourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 49 | WorkOrderAnalyticsPEOSourceSystemType | SOURCE_SYSTEM_TYPE | — | — |
| 50 | WorkOrderAnalyticsPEOStatusChangeReason | STATUS_CHANGE_REASON | — | — |
| 51 | WorkOrderAnalyticsPEOSupplyType | SUPPLY_TYPE | — | — |
| 52 | WorkOrderAnalyticsPEOUomCode | UOM_CODE | — | — |
| 53 | WorkOrderAnalyticsPEOWorkDefinitionAsOfDate | WORK_DEFINITION_AS_OF_DATE | — | ✅ |
| 54 | WorkOrderAnalyticsPEOWorkDefinitionId | WORK_DEFINITION_ID | — | ✅ |
| 55 | WorkOrderAnalyticsPEOWorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | ✅ |
| 56 | WorkOrderAnalyticsPEOWorkMethodId | WORK_METHOD_ID | — | ✅ |
| 57 | WorkOrderAnalyticsPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |
| 58 | WorkOrderAnalyticsPEOWorkOrderId1 | WORK_ORDER_ID | — | ✅ |
| 59 | WorkOrderAnalyticsPEOWorkOrderNumber | WORK_ORDER_NUMBER | — | — |
| 60 | WorkOrderAnalyticsPEOWorkOrderPriority | WORK_ORDER_PRIORITY | — | — |
| 61 | WorkOrderAnalyticsPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | ✅ |
| 62 | WorkOrderAnalyticsPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | — |
| 63 | WorkOrderAnalyticsPEOWorkOrderType | WORK_ORDER_TYPE | — | — |

### [[wie_wo_product_serials|WIE_WO_PRODUCT_SERIALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderProductSerialPEOCreatedBy | CREATED_BY | — | — |
| 2 | WorkOrderProductSerialPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | WorkOrderProductSerialPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 4 | WorkOrderProductSerialPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 5 | WorkOrderProductSerialPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 6 | WorkOrderProductSerialPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | WorkOrderProductSerialPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | WorkOrderProductSerialPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | WorkOrderProductSerialPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | WorkOrderProductSerialPEOOperationSeqNumber | OPERATION_SEQ_NUMBER | — | — |
| 11 | WorkOrderProductSerialPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 12 | WorkOrderProductSerialPEORequestId | REQUEST_ID | — | ✅ |
| 13 | WorkOrderProductSerialPEOSerialNumber | SERIAL_NUMBER | — | ✅ |
| 14 | WorkOrderProductSerialPEOSerialStatus | SERIAL_STATUS | — | — |
| 15 | WorkOrderProductSerialPEOWoOperationId | WO_OPERATION_ID | — | ✅ |
| 16 | WorkOrderProductSerialPEOWoOperationMaterialId | WO_OPERATION_MATERIAL_ID | — | ✅ |
| 17 | WorkOrderProductSerialPEOWoProductSerialId | WO_PRODUCT_SERIAL_ID | 🔑 | ✅ |
| 18 | WorkOrderProductSerialPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
