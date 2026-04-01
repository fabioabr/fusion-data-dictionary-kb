---
id: DOC-OTHER-PVO-CycleCountExtractPVO
doc_type: system-doc
title: "CycleCountExtractPVO — PVO Cross-Module"
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
  - CycleCountExtractPVO
  - cyclecountextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CycleCountExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cycle Count Extract. Acessa as tabelas: INV_CYCLE_COUNT_CLASSES, INV_CYCLE_COUNT_ENTRIES, INV_CYCLE_COUNT_ITEMS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.InvBiccExtractAM.CycleCountExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 92 | 3 | 5 | 92 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[inv_cycle_count_classes|INV_CYCLE_COUNT_CLASSES]] — 20 atributos (2 PKs, 20 BICC)
- [[inv_cycle_count_entries|INV_CYCLE_COUNT_ENTRIES]] — 53 atributos (1 PKs, 53 BICC)
- [[inv_cycle_count_items|INV_CYCLE_COUNT_ITEMS]] — 19 atributos (2 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[inv_cycle_count_classes|INV_CYCLE_COUNT_CLASSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvCycleCountClassPEOAbcAssignmentGroupId | ABC_ASSIGNMENT_GROUP_ID | — | ✅ |
| 2 | InvCycleCountClassPEOAbcClassId | ABC_CLASS_ID | 🔑 | ✅ |
| 3 | InvCycleCountClassPEOApprovalToleranceNegative | APPROVAL_TOLERANCE_NEGATIVE | — | ✅ |
| 4 | InvCycleCountClassPEOApprovalTolerancePositive | APPROVAL_TOLERANCE_POSITIVE | — | ✅ |
| 5 | InvCycleCountClassPEOCostToleranceNegative | COST_TOLERANCE_NEGATIVE | — | ✅ |
| 6 | InvCycleCountClassPEOCostTolerancePositive | COST_TOLERANCE_POSITIVE | — | ✅ |
| 7 | InvCycleCountClassPEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | InvCycleCountClassPEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | InvCycleCountClassPEOCycleCountHeaderId | CYCLE_COUNT_HEADER_ID | 🔑 | ✅ |
| 10 | InvCycleCountClassPEOHitMissToleranceNegative | HIT_MISS_TOLERANCE_NEGATIVE | — | ✅ |
| 11 | InvCycleCountClassPEOHitMissTolerancePositive | HIT_MISS_TOLERANCE_POSITIVE | — | ✅ |
| 12 | InvCycleCountClassPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 13 | InvCycleCountClassPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 14 | InvCycleCountClassPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | InvCycleCountClassPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | InvCycleCountClassPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | InvCycleCountClassPEONumCountsPerYear | NUM_COUNTS_PER_YEAR | — | ✅ |
| 18 | InvCycleCountClassPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 19 | InvCycleCountClassPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 20 | InvCycleCountClassPEORequestId | REQUEST_ID | — | ✅ |

### [[inv_cycle_count_entries|INV_CYCLE_COUNT_ENTRIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvCycleCountEntriesPEOAdjustmentAmount | ADJUSTMENT_AMOUNT | — | ✅ |
| 2 | InvCycleCountEntriesPEOAdjustmentDate | ADJUSTMENT_DATE | — | ✅ |
| 3 | InvCycleCountEntriesPEOAdjustmentQuantity | ADJUSTMENT_QUANTITY | — | ✅ |
| 4 | InvCycleCountEntriesPEOApprovalDate | APPROVAL_DATE | — | ✅ |
| 5 | InvCycleCountEntriesPEOApprovalType | APPROVAL_TYPE | — | ✅ |
| 6 | InvCycleCountEntriesPEOApproverEmployeeId | APPROVER_EMPLOYEE_ID | — | ✅ |
| 7 | InvCycleCountEntriesPEOComments | COMMENTS | — | ✅ |
| 8 | InvCycleCountEntriesPEOCountDate | COUNT_DATE | — | ✅ |
| 9 | InvCycleCountEntriesPEOCountDueDate | COUNT_DUE_DATE | — | ✅ |
| 10 | InvCycleCountEntriesPEOCountListSequence | COUNT_LIST_SEQUENCE | — | ✅ |
| 11 | InvCycleCountEntriesPEOCountQuantity | COUNT_QUANTITY | — | ✅ |
| 12 | InvCycleCountEntriesPEOCountSecondaryUom | COUNT_SECONDARY_UOM | — | ✅ |
| 13 | InvCycleCountEntriesPEOCountTypeCode | COUNT_TYPE_CODE | — | ✅ |
| 14 | InvCycleCountEntriesPEOCountUom | COUNT_UOM | — | ✅ |
| 15 | InvCycleCountEntriesPEOCountedByEmployeeId | COUNTED_BY_EMPLOYEE_ID | — | ✅ |
| 16 | InvCycleCountEntriesPEOCreatedBy | CREATED_BY | — | ✅ |
| 17 | InvCycleCountEntriesPEOCreationDate | CREATION_DATE | — | ✅ |
| 18 | InvCycleCountEntriesPEOCycleCountEntryId | CYCLE_COUNT_ENTRY_ID | 🔑 | ✅ |
| 19 | InvCycleCountEntriesPEOCycleCountHeaderId | CYCLE_COUNT_HEADER_ID | — | ✅ |
| 20 | InvCycleCountEntriesPEOEntryStatusCode | ENTRY_STATUS_CODE | — | ✅ |
| 21 | InvCycleCountEntriesPEOExportFlag | EXPORT_FLAG | — | ✅ |
| 22 | InvCycleCountEntriesPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 23 | InvCycleCountEntriesPEOItemLotControlCode | ITEM_LOT_CONTROL_CODE | — | ✅ |
| 24 | InvCycleCountEntriesPEOItemRevisionQtyControlCode | ITEM_REVISION_QTY_CONTROL_CODE | — | ✅ |
| 25 | InvCycleCountEntriesPEOItemSerialControlCode | ITEM_SERIAL_CONTROL_CODE | — | ✅ |
| 26 | InvCycleCountEntriesPEOItemUnitCost | ITEM_UNIT_COST | — | ✅ |
| 27 | InvCycleCountEntriesPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 28 | InvCycleCountEntriesPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 29 | InvCycleCountEntriesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | InvCycleCountEntriesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 31 | InvCycleCountEntriesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 32 | InvCycleCountEntriesPEOLocatorId | LOCATOR_ID | — | ✅ |
| 33 | InvCycleCountEntriesPEOLotNumber | LOT_NUMBER | — | ✅ |
| 34 | InvCycleCountEntriesPEONumberOfCounts | NUMBER_OF_COUNTS | — | ✅ |
| 35 | InvCycleCountEntriesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 36 | InvCycleCountEntriesPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 37 | InvCycleCountEntriesPEOOutermostLpnId | OUTERMOST_LPN_ID | — | ✅ |
| 38 | InvCycleCountEntriesPEOOwningEntityId | OWNING_ENTITY_ID | — | ✅ |
| 39 | InvCycleCountEntriesPEOOwningType | OWNING_TYPE | — | ✅ |
| 40 | InvCycleCountEntriesPEOParentLpnId | PARENT_LPN_ID | — | ✅ |
| 41 | InvCycleCountEntriesPEOPrimaryUomQuantity | PRIMARY_UOM_QUANTITY | — | ✅ |
| 42 | InvCycleCountEntriesPEORequestId | REQUEST_ID | — | ✅ |
| 43 | InvCycleCountEntriesPEORevision | REVISION | — | ✅ |
| 44 | InvCycleCountEntriesPEOSecondaryAdjustmentQuantity | SECONDARY_ADJUSTMENT_QUANTITY | — | ✅ |
| 45 | InvCycleCountEntriesPEOSecondarySystemQty | SECONDARY_SYSTEM_QTY | — | ✅ |
| 46 | InvCycleCountEntriesPEOSecondaryUomQuantity | SECONDARY_UOM_QUANTITY | — | ✅ |
| 47 | InvCycleCountEntriesPEOSerialDetail | SERIAL_DETAIL | — | ✅ |
| 48 | InvCycleCountEntriesPEOSerialNumber | SERIAL_NUMBER | — | ✅ |
| 49 | InvCycleCountEntriesPEOStandardOperationId | STANDARD_OPERATION_ID | — | ✅ |
| 50 | InvCycleCountEntriesPEOSubinventory | SUBINVENTORY | — | ✅ |
| 51 | InvCycleCountEntriesPEOSystemQuantity | SYSTEM_QUANTITY | — | ✅ |
| 52 | InvCycleCountEntriesPEOTaskPriority | TASK_PRIORITY | — | ✅ |
| 53 | InvCycleCountEntriesPEOTransactionReasonId | TRANSACTION_REASON_ID | — | ✅ |

### [[inv_cycle_count_items|INV_CYCLE_COUNT_ITEMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvCycleCountItemPEOAbcClassId | ABC_CLASS_ID | — | ✅ |
| 2 | InvCycleCountItemPEOApprovalToleranceNegative | APPROVAL_TOLERANCE_NEGATIVE | — | ✅ |
| 3 | InvCycleCountItemPEOApprovalTolerancePositive | APPROVAL_TOLERANCE_POSITIVE | — | ✅ |
| 4 | InvCycleCountItemPEOCostToleranceNegative | COST_TOLERANCE_NEGATIVE | — | ✅ |
| 5 | InvCycleCountItemPEOCostTolerancePositive | COST_TOLERANCE_POSITIVE | — | ✅ |
| 6 | InvCycleCountItemPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | InvCycleCountItemPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | InvCycleCountItemPEOCycleCountHeaderId | CYCLE_COUNT_HEADER_ID | 🔑 | ✅ |
| 9 | InvCycleCountItemPEOIncludeInSchedule | INCLUDE_IN_SCHEDULE | — | ✅ |
| 10 | InvCycleCountItemPEOInventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 11 | InvCycleCountItemPEOItemLastScheduleDate | ITEM_LAST_SCHEDULE_DATE | — | ✅ |
| 12 | InvCycleCountItemPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 13 | InvCycleCountItemPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 14 | InvCycleCountItemPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | InvCycleCountItemPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | InvCycleCountItemPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | InvCycleCountItemPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | InvCycleCountItemPEORequestId | REQUEST_ID | — | ✅ |
| 19 | InvCycleCountItemPEOScheduleOrder | SCHEDULE_ORDER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
