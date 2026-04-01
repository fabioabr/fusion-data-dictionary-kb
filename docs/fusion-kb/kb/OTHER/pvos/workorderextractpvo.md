---
id: DOC-OTHER-PVO-WorkOrderExtractPVO
doc_type: system-doc
title: "WorkOrderExtractPVO — PVO Cross-Module"
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
  - WorkOrderExtractPVO
  - workorderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkOrderExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Work Order Extract. Acessa as tabelas: WIE_WORK_ORDERS_B, WIE_WORK_ORDERS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WieBiccExtractAM.WorkOrderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 166 | 2 | 1 | 166 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wie_work_orders_b|WIE_WORK_ORDERS_B]] — 156 atributos (1 PKs, 156 BICC)
- [[wie_work_orders_tl|WIE_WORK_ORDERS_TL]] — 10 atributos (10 BICC)

---

## ⚙️ Atributos

### [[wie_work_orders_b|WIE_WORK_ORDERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BuildSequence | BUILD_SEQUENCE | — | ✅ |
| 2 | ExpeditedFlag | EXPEDITED_FLAG | — | ✅ |
| 3 | ProductionLineId | PRODUCTION_LINE_ID | — | ✅ |
| 4 | WorkOrderPEOActualCompletionDate | ACTUAL_COMPLETION_DATE | — | ✅ |
| 5 | WorkOrderPEOActualStartDate | ACTUAL_START_DATE | — | ✅ |
| 6 | WorkOrderPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 7 | WorkOrderPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 8 | WorkOrderPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 9 | WorkOrderPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 10 | WorkOrderPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 11 | WorkOrderPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 12 | WorkOrderPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 13 | WorkOrderPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 14 | WorkOrderPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 15 | WorkOrderPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 16 | WorkOrderPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 17 | WorkOrderPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 18 | WorkOrderPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 19 | WorkOrderPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 20 | WorkOrderPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 21 | WorkOrderPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 22 | WorkOrderPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 23 | WorkOrderPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 24 | WorkOrderPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 25 | WorkOrderPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 26 | WorkOrderPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 27 | WorkOrderPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 28 | WorkOrderPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 29 | WorkOrderPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 30 | WorkOrderPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 31 | WorkOrderPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 32 | WorkOrderPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 33 | WorkOrderPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 34 | WorkOrderPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 35 | WorkOrderPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 36 | WorkOrderPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 37 | WorkOrderPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 38 | WorkOrderPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 39 | WorkOrderPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 40 | WorkOrderPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 41 | WorkOrderPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 42 | WorkOrderPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 43 | WorkOrderPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 44 | WorkOrderPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 45 | WorkOrderPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 46 | WorkOrderPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 47 | WorkOrderPEOBackToBackFlag | BACK_TO_BACK_FLAG | — | ✅ |
| 48 | WorkOrderPEOCanceledDate | CANCELED_DATE | — | ✅ |
| 49 | WorkOrderPEOCanceledReason | CANCELED_REASON | — | ✅ |
| 50 | WorkOrderPEOClosedDate | CLOSED_DATE | — | ✅ |
| 51 | WorkOrderPEOCmPoHeaderId | CM_PO_HEADER_ID | — | ✅ |
| 52 | WorkOrderPEOCmPoLineId | CM_PO_LINE_ID | — | ✅ |
| 53 | WorkOrderPEOCmPoLineLocId | CM_PO_LINE_LOC_ID | — | ✅ |
| 54 | WorkOrderPEOComplLocatorId | COMPL_LOCATOR_ID | — | ✅ |
| 55 | WorkOrderPEOComplSubinventoryCode | COMPL_SUBINVENTORY_CODE | — | ✅ |
| 56 | WorkOrderPEOCompletedQuantity | COMPLETED_QUANTITY | — | ✅ |
| 57 | WorkOrderPEOConfigItemVersion | CONFIG_ITEM_VERSION | — | ✅ |
| 58 | WorkOrderPEOContractMfgFlag | CONTRACT_MFG_FLAG | — | ✅ |
| 59 | WorkOrderPEOCreatedBy | CREATED_BY | — | ✅ |
| 60 | WorkOrderPEOCreationDate | CREATION_DATE | — | ✅ |
| 61 | WorkOrderPEOFirmPlannedFlag | FIRM_PLANNED_FLAG | — | ✅ |
| 62 | WorkOrderPEOInterfaceSourceCode | INTERFACE_SOURCE_CODE | — | ✅ |
| 63 | WorkOrderPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 64 | WorkOrderPEOItemRevision | ITEM_REVISION | — | ✅ |
| 65 | WorkOrderPEOItemStructureName | ITEM_STRUCTURE_NAME | — | ✅ |
| 66 | WorkOrderPEOItemVersion | ITEM_VERSION | — | ✅ |
| 67 | WorkOrderPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 68 | WorkOrderPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 69 | WorkOrderPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 70 | WorkOrderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 71 | WorkOrderPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 72 | WorkOrderPEOMntAllowMultipleAssetsFlag | MNT_ALLOW_MULTIPLE_ASSETS_FLAG | — | ✅ |
| 73 | WorkOrderPEOMntCompleteToInvFlag | MNT_COMPLETE_TO_INV_FLAG | — | ✅ |
| 74 | WorkOrderPEOMntIncludeInPlanningFlag | MNT_INCLUDE_IN_PLANNING_FLAG | — | ✅ |
| 75 | WorkOrderPEOMntOutOfSequenceFlag | MNT_OUT_OF_SEQUENCE_FLAG | — | ✅ |
| 76 | WorkOrderPEOMntTransformToItemId | MNT_TRANSFORM_TO_ITEM_ID | — | ✅ |
| 77 | WorkOrderPEONeedByDate | NEED_BY_DATE | — | ✅ |
| 78 | WorkOrderPEONettableSupplyQtyOverride | NETTABLE_SUPPLY_QTY_OVERRIDE | — | ✅ |
| 79 | WorkOrderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 80 | WorkOrderPEOOneTimeConfigFlag | ONE_TIME_CONFIG_FLAG | — | ✅ |
| 81 | WorkOrderPEOOrchestrationCode | ORCHESTRATION_CODE | — | ✅ |
| 82 | WorkOrderPEOOrderLessFlag | ORDER_LESS_FLAG | — | ✅ |
| 83 | WorkOrderPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 84 | WorkOrderPEOOvercomplToleranceType | OVERCOMPL_TOLERANCE_TYPE | — | ✅ |
| 85 | WorkOrderPEOOvercomplToleranceValue | OVERCOMPL_TOLERANCE_VALUE | — | ✅ |
| 86 | WorkOrderPEOPjcBillableFlag | PJC_BILLABLE_FLAG | — | ✅ |
| 87 | WorkOrderPEOPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | ✅ |
| 88 | WorkOrderPEOPjcContextCategory | PJC_CONTEXT_CATEGORY | — | ✅ |
| 89 | WorkOrderPEOPjcContractId | PJC_CONTRACT_ID | — | ✅ |
| 90 | WorkOrderPEOPjcContractLineId | PJC_CONTRACT_LINE_ID | — | ✅ |
| 91 | WorkOrderPEOPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | ✅ |
| 92 | WorkOrderPEOPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | ✅ |
| 93 | WorkOrderPEOPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | ✅ |
| 94 | WorkOrderPEOPjcOrganizationId | PJC_ORGANIZATION_ID | — | ✅ |
| 95 | WorkOrderPEOPjcProjectId | PJC_PROJECT_ID | — | ✅ |
| 96 | WorkOrderPEOPjcProjectNumber | PJC_PROJECT_NUMBER | — | ✅ |
| 97 | WorkOrderPEOPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | ✅ |
| 98 | WorkOrderPEOPjcReservedAttribute10 | PJC_RESERVED_ATTRIBUTE10 | — | ✅ |
| 99 | WorkOrderPEOPjcReservedAttribute2 | PJC_RESERVED_ATTRIBUTE2 | — | ✅ |
| 100 | WorkOrderPEOPjcReservedAttribute3 | PJC_RESERVED_ATTRIBUTE3 | — | ✅ |
| 101 | WorkOrderPEOPjcReservedAttribute4 | PJC_RESERVED_ATTRIBUTE4 | — | ✅ |
| 102 | WorkOrderPEOPjcReservedAttribute5 | PJC_RESERVED_ATTRIBUTE5 | — | ✅ |
| 103 | WorkOrderPEOPjcReservedAttribute6 | PJC_RESERVED_ATTRIBUTE6 | — | ✅ |
| 104 | WorkOrderPEOPjcReservedAttribute7 | PJC_RESERVED_ATTRIBUTE7 | — | ✅ |
| 105 | WorkOrderPEOPjcReservedAttribute8 | PJC_RESERVED_ATTRIBUTE8 | — | ✅ |
| 106 | WorkOrderPEOPjcReservedAttribute9 | PJC_RESERVED_ATTRIBUTE9 | — | ✅ |
| 107 | WorkOrderPEOPjcTaskId | PJC_TASK_ID | — | ✅ |
| 108 | WorkOrderPEOPjcTaskNumber | PJC_TASK_NUMBER | — | ✅ |
| 109 | WorkOrderPEOPjcUserDefAttribute1 | PJC_USER_DEF_ATTRIBUTE1 | — | ✅ |
| 110 | WorkOrderPEOPjcUserDefAttribute10 | PJC_USER_DEF_ATTRIBUTE10 | — | ✅ |
| 111 | WorkOrderPEOPjcUserDefAttribute2 | PJC_USER_DEF_ATTRIBUTE2 | — | ✅ |
| 112 | WorkOrderPEOPjcUserDefAttribute3 | PJC_USER_DEF_ATTRIBUTE3 | — | ✅ |
| 113 | WorkOrderPEOPjcUserDefAttribute4 | PJC_USER_DEF_ATTRIBUTE4 | — | ✅ |
| 114 | WorkOrderPEOPjcUserDefAttribute5 | PJC_USER_DEF_ATTRIBUTE5 | — | ✅ |
| 115 | WorkOrderPEOPjcUserDefAttribute6 | PJC_USER_DEF_ATTRIBUTE6 | — | ✅ |
| 116 | WorkOrderPEOPjcUserDefAttribute7 | PJC_USER_DEF_ATTRIBUTE7 | — | ✅ |
| 117 | WorkOrderPEOPjcUserDefAttribute8 | PJC_USER_DEF_ATTRIBUTE8 | — | ✅ |
| 118 | WorkOrderPEOPjcUserDefAttribute9 | PJC_USER_DEF_ATTRIBUTE9 | — | ✅ |
| 119 | WorkOrderPEOPjcWorkTypeId | PJC_WORK_TYPE_ID | — | ✅ |
| 120 | WorkOrderPEOPlannedCompletionDate | PLANNED_COMPLETION_DATE | — | ✅ |
| 121 | WorkOrderPEOPlannedStartDate | PLANNED_START_DATE | — | ✅ |
| 122 | WorkOrderPEOPlannedStartQuantity | PLANNED_START_QUANTITY | — | ✅ |
| 123 | WorkOrderPEOPreassignLotFlag | PREASSIGN_LOT_FLAG | — | ✅ |
| 124 | WorkOrderPEOPrimaryProductQuantity | PRIMARY_PRODUCT_QUANTITY | — | ✅ |
| 125 | WorkOrderPEOPrimaryProductUomCode | PRIMARY_PRODUCT_UOM_CODE | — | ✅ |
| 126 | WorkOrderPEORejectedQuantity | REJECTED_QUANTITY | — | ✅ |
| 127 | WorkOrderPEOReleasedDate | RELEASED_DATE | — | ✅ |
| 128 | WorkOrderPEORequestId | REQUEST_ID | — | ✅ |
| 129 | WorkOrderPEOResequenceFlag | RESEQUENCE_FLAG | — | ✅ |
| 130 | WorkOrderPEOSchedulingMethod | SCHEDULING_METHOD | — | ✅ |
| 131 | WorkOrderPEOScoSupplyOrderId | SCO_SUPPLY_ORDER_ID | — | ✅ |
| 132 | WorkOrderPEOScrappedQuantity | SCRAPPED_QUANTITY | — | ✅ |
| 133 | WorkOrderPEOSerialTrackingFlag | SERIAL_TRACKING_FLAG | — | ✅ |
| 134 | WorkOrderPEOSourceHeaderRef | SOURCE_HEADER_REF | — | ✅ |
| 135 | WorkOrderPEOSourceHeaderRefId | SOURCE_HEADER_REF_ID | — | ✅ |
| 136 | WorkOrderPEOSourceLineRef | SOURCE_LINE_REF | — | ✅ |
| 137 | WorkOrderPEOSourceLineRefId | SOURCE_LINE_REF_ID | — | ✅ |
| 138 | WorkOrderPEOSourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |
| 139 | WorkOrderPEOSourceSystemType | SOURCE_SYSTEM_TYPE | — | ✅ |
| 140 | WorkOrderPEOStatusChangeReason | STATUS_CHANGE_REASON | — | ✅ |
| 141 | WorkOrderPEOSupplyType | SUPPLY_TYPE | — | ✅ |
| 142 | WorkOrderPEOTransformFromItemId | TRANSFORM_FROM_ITEM_ID | — | ✅ |
| 143 | WorkOrderPEOUnderCompletedFlag | UNDER_COMPLETED_FLAG | — | ✅ |
| 144 | WorkOrderPEOUndercomplToleranceType | UNDERCOMPL_TOLERANCE_TYPE | — | ✅ |
| 145 | WorkOrderPEOUndercomplToleranceValue | UNDERCOMPL_TOLERANCE_VALUE | — | ✅ |
| 146 | WorkOrderPEOUomCode | UOM_CODE | — | ✅ |
| 147 | WorkOrderPEOWorkDefinitionAsOfDate | WORK_DEFINITION_AS_OF_DATE | — | ✅ |
| 148 | WorkOrderPEOWorkDefinitionId | WORK_DEFINITION_ID | — | ✅ |
| 149 | WorkOrderPEOWorkDefinitionVersionId | WORK_DEFINITION_VERSION_ID | — | ✅ |
| 150 | WorkOrderPEOWorkMethodId | WORK_METHOD_ID | — | ✅ |
| 151 | WorkOrderPEOWorkOrderId | WORK_ORDER_ID | 🔑 | ✅ |
| 152 | WorkOrderPEOWorkOrderNumber | WORK_ORDER_NUMBER | — | ✅ |
| 153 | WorkOrderPEOWorkOrderPriority | WORK_ORDER_PRIORITY | — | ✅ |
| 154 | WorkOrderPEOWorkOrderStatusId | WORK_ORDER_STATUS_ID | — | ✅ |
| 155 | WorkOrderPEOWorkOrderSubType | WORK_ORDER_SUB_TYPE | — | ✅ |
| 156 | WorkOrderPEOWorkOrderType | WORK_ORDER_TYPE | — | ✅ |

### [[wie_work_orders_tl|WIE_WORK_ORDERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkOrderTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | WorkOrderTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | WorkOrderTLPEOLanguage | LANGUAGE | — | ✅ |
| 4 | WorkOrderTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | WorkOrderTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | WorkOrderTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | WorkOrderTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | WorkOrderTLPEOSourceLang | SOURCE_LANG | — | ✅ |
| 9 | WorkOrderTLPEOWorkOrderDescription | WORK_ORDER_DESCRIPTION | — | ✅ |
| 10 | WorkOrderTLPEOWorkOrderId | WORK_ORDER_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
