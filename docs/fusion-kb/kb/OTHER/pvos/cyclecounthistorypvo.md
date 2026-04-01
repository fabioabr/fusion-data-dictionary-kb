---
id: DOC-OTHER-PVO-CycleCountHistoryPVO
doc_type: system-doc
title: "CycleCountHistoryPVO — PVO Cross-Module"
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
  - CycleCountHistoryPVO
  - cyclecounthistorypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CycleCountHistoryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cycle Count History. Acessa as tabelas: EGP_SYSTEM_ITEMS_B_V, HZ_PARTIES, INV_ABC_ASSIGNMENT_GROUPS (+9).

**Caminho:** `FscmTopModelAM.InventoryAM.CycleCountHistoryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 200 | 12 | 1 | 7 | 4% |

---

## 🔗 Tabelas Relacionadas

- [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]] — 3 atributos
- [[hz_parties|HZ_PARTIES]] — 2 atributos
- [[inv_abc_assignment_groups|INV_ABC_ASSIGNMENT_GROUPS]] — 3 atributos
- [[inv_cc_entries_history|INV_CC_ENTRIES_HISTORY]] — 25 atributos (1 PKs, 7 BICC)
- [[inv_cc_subinventories|INV_CC_SUBINVENTORIES]] — 13 atributos
- [[inv_cycle_count_classes|INV_CYCLE_COUNT_CLASSES]] — 20 atributos
- [[inv_cycle_count_entries|INV_CYCLE_COUNT_ENTRIES]] — 53 atributos
- [[inv_cycle_count_headers|INV_CYCLE_COUNT_HEADERS]] — 47 atributos
- [[inv_cycle_count_items|INV_CYCLE_COUNT_ITEMS]] — 20 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 8 atributos
- [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]] — 3 atributos
- [[zmm_sr_schedules_vl|ZMM_SR_SCHEDULES_VL]] — 3 atributos

---

## ⚙️ Atributos

### [[egp_system_items_b_v|EGP_SYSTEM_ITEMS_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemBasePEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 2 | ItemBasePEOItemNumber | ITEM_NUMBER | — | — |
| 3 | ItemBasePEOOrganizationId | ORGANIZATION_ID | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyId | PARTY_ID | — | — |
| 2 | PartyPEOPartyName | PARTY_NAME | — | — |

### [[inv_abc_assignment_groups|INV_ABC_ASSIGNMENT_GROUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbcAssignmentGroupPEOAssignmentGroupId | ASSIGNMENT_GROUP_ID | — | — |
| 2 | AbcAssignmentGroupPEOAssignmentGroupName | ASSIGNMENT_GROUP_NAME | — | — |
| 3 | AbcAssignmentGroupPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[inv_cc_entries_history|INV_CC_ENTRIES_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ICCHIstoryPEOApprovalDate | APPROVAL_DATE | — | — |
| 2 | ICCHIstoryPEOApproverEmployeeId | APPROVER_EMPLOYEE_ID | — | — |
| 3 | ICCHIstoryPEOCcEntryHistoryId | CC_ENTRY_HISTORY_ID | 🔑 | ✅ |
| 4 | ICCHIstoryPEOComments | COMMENTS | — | — |
| 5 | ICCHIstoryPEOCountDate | COUNT_DATE | — | ✅ |
| 6 | ICCHIstoryPEOCountQuantity | COUNT_QUANTITY | — | ✅ |
| 7 | ICCHIstoryPEOCountSecondaryUom | COUNT_SECONDARY_UOM | — | — |
| 8 | ICCHIstoryPEOCountUom | COUNT_UOM | — | ✅ |
| 9 | ICCHIstoryPEOCountedByEmployeeId | COUNTED_BY_EMPLOYEE_ID | — | — |
| 10 | ICCHIstoryPEOCreatedBy | CREATED_BY | — | — |
| 11 | ICCHIstoryPEOCreationDate | CREATION_DATE | — | — |
| 12 | ICCHIstoryPEOCycleCountEntryId | CYCLE_COUNT_ENTRY_ID | — | ✅ |
| 13 | ICCHIstoryPEOItemUnitCost | ITEM_UNIT_COST | — | ✅ |
| 14 | ICCHIstoryPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 15 | ICCHIstoryPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 16 | ICCHIstoryPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 17 | ICCHIstoryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | ICCHIstoryPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | ICCHIstoryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | ICCHIstoryPEOPrimaryUomQuantity | PRIMARY_UOM_QUANTITY | — | — |
| 21 | ICCHIstoryPEORequestId | REQUEST_ID | — | — |
| 22 | ICCHIstoryPEOSecondarySystemQty | SECONDARY_SYSTEM_QTY | — | — |
| 23 | ICCHIstoryPEOSecondaryUomQuantity | SECONDARY_UOM_QUANTITY | — | — |
| 24 | ICCHIstoryPEOSystemQuantity | SYSTEM_QUANTITY | — | ✅ |
| 25 | ICCHIstoryPEOTransactionReasonId | TRANSACTION_REASON_ID | — | — |

### [[inv_cc_subinventories|INV_CC_SUBINVENTORIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ICCSubinventoriesPEOCreatedBy | CREATED_BY | — | — |
| 2 | ICCSubinventoriesPEOCreationDate | CREATION_DATE | — | — |
| 3 | ICCSubinventoriesPEOCycleCountHeaderId | CYCLE_COUNT_HEADER_ID | — | — |
| 4 | ICCSubinventoriesPEOIncludeInCount | INCLUDE_IN_COUNT | — | — |
| 5 | ICCSubinventoriesPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 6 | ICCSubinventoriesPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 7 | ICCSubinventoriesPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | ICCSubinventoriesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ICCSubinventoriesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ICCSubinventoriesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ICCSubinventoriesPEOOrganizationId | ORGANIZATION_ID | — | — |
| 12 | ICCSubinventoriesPEORequestId | REQUEST_ID | — | — |
| 13 | ICCSubinventoriesPEOSubinventory | SUBINVENTORY | — | — |

### [[inv_cycle_count_classes|INV_CYCLE_COUNT_CLASSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ICCClassPEOAbcAssignmentGroupId | ABC_ASSIGNMENT_GROUP_ID | — | — |
| 2 | ICCClassPEOAbcClassId | ABC_CLASS_ID | — | — |
| 3 | ICCClassPEOApprovalToleranceNegative | APPROVAL_TOLERANCE_NEGATIVE | — | — |
| 4 | ICCClassPEOApprovalTolerancePositive | APPROVAL_TOLERANCE_POSITIVE | — | — |
| 5 | ICCClassPEOCostToleranceNegative | COST_TOLERANCE_NEGATIVE | — | — |
| 6 | ICCClassPEOCostTolerancePositive | COST_TOLERANCE_POSITIVE | — | — |
| 7 | ICCClassPEOCreatedBy | CREATED_BY | — | — |
| 8 | ICCClassPEOCreationDate | CREATION_DATE | — | — |
| 9 | ICCClassPEOCycleCountHeaderId | CYCLE_COUNT_HEADER_ID | — | — |
| 10 | ICCClassPEOHitMissToleranceNegative | HIT_MISS_TOLERANCE_NEGATIVE | — | — |
| 11 | ICCClassPEOHitMissTolerancePositive | HIT_MISS_TOLERANCE_POSITIVE | — | — |
| 12 | ICCClassPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 13 | ICCClassPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 14 | ICCClassPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 15 | ICCClassPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | ICCClassPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | ICCClassPEONumCountsPerYear | NUM_COUNTS_PER_YEAR | — | — |
| 18 | ICCClassPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | ICCClassPEOOrganizationId | ORGANIZATION_ID | — | — |
| 20 | ICCClassPEORequestId | REQUEST_ID | — | — |

### [[inv_cycle_count_entries|INV_CYCLE_COUNT_ENTRIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ICCEntriesPEOAdjustmentAmount | ADJUSTMENT_AMOUNT | — | — |
| 2 | ICCEntriesPEOAdjustmentDate | ADJUSTMENT_DATE | — | — |
| 3 | ICCEntriesPEOAdjustmentQuantity | ADJUSTMENT_QUANTITY | — | — |
| 4 | ICCEntriesPEOApprovalDate | APPROVAL_DATE | — | — |
| 5 | ICCEntriesPEOApprovalType | APPROVAL_TYPE | — | — |
| 6 | ICCEntriesPEOApproverEmployeeId | APPROVER_EMPLOYEE_ID | — | — |
| 7 | ICCEntriesPEOComments | COMMENTS | — | — |
| 8 | ICCEntriesPEOCountDate | COUNT_DATE | — | — |
| 9 | ICCEntriesPEOCountDueDate | COUNT_DUE_DATE | — | — |
| 10 | ICCEntriesPEOCountListSequence | COUNT_LIST_SEQUENCE | — | — |
| 11 | ICCEntriesPEOCountQuantity | COUNT_QUANTITY | — | — |
| 12 | ICCEntriesPEOCountSecondaryUom | COUNT_SECONDARY_UOM | — | — |
| 13 | ICCEntriesPEOCountTypeCode | COUNT_TYPE_CODE | — | — |
| 14 | ICCEntriesPEOCountUom | COUNT_UOM | — | — |
| 15 | ICCEntriesPEOCountedByEmployeeId | COUNTED_BY_EMPLOYEE_ID | — | — |
| 16 | ICCEntriesPEOCreatedBy | CREATED_BY | — | — |
| 17 | ICCEntriesPEOCreationDate | CREATION_DATE | — | — |
| 18 | ICCEntriesPEOCycleCountEntryId | CYCLE_COUNT_ENTRY_ID | — | — |
| 19 | ICCEntriesPEOCycleCountHeaderId | CYCLE_COUNT_HEADER_ID | — | — |
| 20 | ICCEntriesPEOEntryStatusCode | ENTRY_STATUS_CODE | — | — |
| 21 | ICCEntriesPEOExportFlag | EXPORT_FLAG | — | — |
| 22 | ICCEntriesPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 23 | ICCEntriesPEOItemLotControlCode | ITEM_LOT_CONTROL_CODE | — | — |
| 24 | ICCEntriesPEOItemRevisionQtyControlCode | ITEM_REVISION_QTY_CONTROL_CODE | — | — |
| 25 | ICCEntriesPEOItemSerialControlCode | ITEM_SERIAL_CONTROL_CODE | — | — |
| 26 | ICCEntriesPEOItemUnitCost | ITEM_UNIT_COST | — | — |
| 27 | ICCEntriesPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 28 | ICCEntriesPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 29 | ICCEntriesPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 30 | ICCEntriesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 31 | ICCEntriesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 32 | ICCEntriesPEOLocatorId | LOCATOR_ID | — | — |
| 33 | ICCEntriesPEOLotNumber | LOT_NUMBER | — | — |
| 34 | ICCEntriesPEONumberOfCounts | NUMBER_OF_COUNTS | — | — |
| 35 | ICCEntriesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 36 | ICCEntriesPEOOrganizationId | ORGANIZATION_ID | — | — |
| 37 | ICCEntriesPEOOutermostLpnId | OUTERMOST_LPN_ID | — | — |
| 38 | ICCEntriesPEOOwningEntityId | OWNING_ENTITY_ID | — | — |
| 39 | ICCEntriesPEOOwningType | OWNING_TYPE | — | — |
| 40 | ICCEntriesPEOParentLpnId | PARENT_LPN_ID | — | — |
| 41 | ICCEntriesPEOPrimaryUomQuantity | PRIMARY_UOM_QUANTITY | — | — |
| 42 | ICCEntriesPEORequestId | REQUEST_ID | — | — |
| 43 | ICCEntriesPEORevision | REVISION | — | — |
| 44 | ICCEntriesPEOSecondaryAdjustmentQuantity | SECONDARY_ADJUSTMENT_QUANTITY | — | — |
| 45 | ICCEntriesPEOSecondarySystemQty | SECONDARY_SYSTEM_QTY | — | — |
| 46 | ICCEntriesPEOSecondaryUomQuantity | SECONDARY_UOM_QUANTITY | — | — |
| 47 | ICCEntriesPEOSerialDetail | SERIAL_DETAIL | — | — |
| 48 | ICCEntriesPEOSerialNumber | SERIAL_NUMBER | — | — |
| 49 | ICCEntriesPEOStandardOperationId | STANDARD_OPERATION_ID | — | — |
| 50 | ICCEntriesPEOSubinventory | SUBINVENTORY | — | — |
| 51 | ICCEntriesPEOSystemQuantity | SYSTEM_QUANTITY | — | — |
| 52 | ICCEntriesPEOTaskPriority | TASK_PRIORITY | — | — |
| 53 | ICCEntriesPEOTransactionReasonId | TRANSACTION_REASON_ID | — | — |

### [[inv_cycle_count_headers|INV_CYCLE_COUNT_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CICCHeaderPEOycleCountHeaderName | CYCLE_COUNT_HEADER_NAME | — | — |
| 2 | ICCHeaderPEOAbcAssignmentGroupId | ABC_ASSIGNMENT_GROUP_ID | — | — |
| 3 | ICCHeaderPEOAbcInitializationStatus | ABC_INITIALIZATION_STATUS | — | — |
| 4 | ICCHeaderPEOAllowSerialItems | ALLOW_SERIAL_ITEMS | — | — |
| 5 | ICCHeaderPEOApprovalOptionCode | APPROVAL_OPTION_CODE | — | — |
| 6 | ICCHeaderPEOApprovalRequired | APPROVAL_REQUIRED | — | — |
| 7 | ICCHeaderPEOApprovalToleranceNegative | APPROVAL_TOLERANCE_NEGATIVE | — | — |
| 8 | ICCHeaderPEOApprovalTolerancePositive | APPROVAL_TOLERANCE_POSITIVE | — | — |
| 9 | ICCHeaderPEOAutoscheduleEnabledFlag | AUTOSCHEDULE_ENABLED_FLAG | — | — |
| 10 | ICCHeaderPEOContainerAdjustmentOption | CONTAINER_ADJUSTMENT_OPTION | — | — |
| 11 | ICCHeaderPEOContainerDiscrepancyOption | CONTAINER_DISCREPANCY_OPTION | — | — |
| 12 | ICCHeaderPEOContainerEnabledFlag | CONTAINER_ENABLED_FLAG | — | — |
| 13 | ICCHeaderPEOCostToleranceNegative | COST_TOLERANCE_NEGATIVE | — | — |
| 14 | ICCHeaderPEOCostTolerancePositive | COST_TOLERANCE_POSITIVE | — | — |
| 15 | ICCHeaderPEOCreatedBy | CREATED_BY | — | — |
| 16 | ICCHeaderPEOCreationDate | CREATION_DATE | — | — |
| 17 | ICCHeaderPEOCycleCountHeaderId | CYCLE_COUNT_HEADER_ID | — | — |
| 18 | ICCHeaderPEODaysUntilLate | DAYS_UNTIL_LATE | — | — |
| 19 | ICCHeaderPEODefaultApprover | DEFAULT_APPROVER | — | — |
| 20 | ICCHeaderPEODescription | DESCRIPTION | — | — |
| 21 | ICCHeaderPEOEndDate | END_DATE | — | — |
| 22 | ICCHeaderPEOHeaderLastScheduleDate | HEADER_LAST_SCHEDULE_DATE | — | — |
| 23 | ICCHeaderPEOHeaderNextScheduleDate | HEADER_NEXT_SCHEDULE_DATE | — | — |
| 24 | ICCHeaderPEOHitMissToleranceNegative | HIT_MISS_TOLERANCE_NEGATIVE | — | — |
| 25 | ICCHeaderPEOHitMissTolerancePositive | HIT_MISS_TOLERANCE_POSITIVE | — | — |
| 26 | ICCHeaderPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 27 | ICCHeaderPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 28 | ICCHeaderPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 29 | ICCHeaderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 30 | ICCHeaderPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 31 | ICCHeaderPEOMaximumAutoRecounts | MAXIMUM_AUTO_RECOUNTS | — | — |
| 32 | ICCHeaderPEONextUserCountSequence | NEXT_USER_COUNT_SEQUENCE | — | — |
| 33 | ICCHeaderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 34 | ICCHeaderPEOOnhandVisibleFlag | ONHAND_VISIBLE_FLAG | — | — |
| 35 | ICCHeaderPEOOrganizationId | ORGANIZATION_ID | — | — |
| 36 | ICCHeaderPEOOverrideDefaultApprover | OVERRIDE_DEFAULT_APPROVER | — | — |
| 37 | ICCHeaderPEORequestId | REQUEST_ID | — | — |
| 38 | ICCHeaderPEOScheduleIntervalTime | SCHEDULE_INTERVAL_TIME | — | — |
| 39 | ICCHeaderPEOSerialAdjustmentOption | SERIAL_ADJUSTMENT_OPTION | — | — |
| 40 | ICCHeaderPEOSerialCountOption | SERIAL_COUNT_OPTION | — | — |
| 41 | ICCHeaderPEOSerialDetailOption | SERIAL_DETAIL_OPTION | — | — |
| 42 | ICCHeaderPEOSerialDiscrepancyOption | SERIAL_DISCREPANCY_OPTION | — | — |
| 43 | ICCHeaderPEOStartDate | START_DATE | — | — |
| 44 | ICCHeaderPEOStartManualCountsPrefix | START_MANUAL_COUNTS_PREFIX | — | — |
| 45 | ICCHeaderPEOUnscheduledCountEntry | UNSCHEDULED_COUNT_ENTRY | — | — |
| 46 | ICCHeaderPEOWorkdaySchedule | WORKDAY_SCHEDULE | — | — |
| 47 | ICCHeaderPEOZeroCountFlag | ZERO_COUNT_FLAG | — | — |

### [[inv_cycle_count_items|INV_CYCLE_COUNT_ITEMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ICCItemPEOAbcClassId | ABC_CLASS_ID | — | — |
| 2 | ICCItemPEOApprovalToleranceNegative | APPROVAL_TOLERANCE_NEGATIVE | — | — |
| 3 | ICCItemPEOApprovalTolerancePositive | APPROVAL_TOLERANCE_POSITIVE | — | — |
| 4 | ICCItemPEOCostToleranceNegative | COST_TOLERANCE_NEGATIVE | — | — |
| 5 | ICCItemPEOCostTolerancePositive | COST_TOLERANCE_POSITIVE | — | — |
| 6 | ICCItemPEOCreatedBy | CREATED_BY | — | — |
| 7 | ICCItemPEOCreationDate | CREATION_DATE | — | — |
| 8 | ICCItemPEOCycleCountHeaderId | CYCLE_COUNT_HEADER_ID | — | — |
| 9 | ICCItemPEOIncludeInSchedule | INCLUDE_IN_SCHEDULE | — | — |
| 10 | ICCItemPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 11 | ICCItemPEOItemLastScheduleDate | ITEM_LAST_SCHEDULE_DATE | — | — |
| 12 | ICCItemPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 13 | ICCItemPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 14 | ICCItemPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 15 | ICCItemPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | ICCItemPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | ICCItemPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | ICCItemPEOOrganizationId | ORGANIZATION_ID | — | — |
| 19 | ICCItemPEORequestId | REQUEST_ID | — | — |
| 20 | ICCItemPEOScheduleOrder | SCHEDULE_ORDER | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | PersonNameId | PERSON_NAME_ID | — | — |
| 4 | PersonNamePEO1ApproverEmployeeId | DISPLAY_NAME | — | — |
| 5 | PersonNamePEO1EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | PersonNamePEO1EffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 7 | PersonNamePEO1PersonNameId | PERSON_NAME_ID | — | — |
| 8 | PersonNamePEOCountedByEmployeeId | DISPLAY_NAME | — | — |

### [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SuplierSiteDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | SuplierSiteDPEOVendorSiteCode | VENDOR_SITE_CODE | — | — |
| 3 | SuplierSiteDPEOVendorSiteId | VENDOR_SITE_ID | — | — |

### [[zmm_sr_schedules_vl|ZMM_SR_SCHEDULES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | ScheduleEOScheduleName | SCHEDULE_NAME | — | — |
| 3 | ScheduleId | SCHEDULE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
