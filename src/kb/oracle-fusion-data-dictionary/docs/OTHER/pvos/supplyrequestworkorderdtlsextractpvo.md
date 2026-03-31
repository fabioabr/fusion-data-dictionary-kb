---
id: DOC-OTHER-PVO-SupplyRequestWorkOrderDtlsExtractPVO
doc_type: system-doc
title: "SupplyRequestWorkOrderDtlsExtractPVO — PVO Cross-Module"
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
  - SupplyRequestWorkOrderDtlsExtractPVO
  - supplyrequestworkorderdtlsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplyRequestWorkOrderDtlsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Supply Request Work Order Dtls Extract. Acessa as tabelas: DOS_WORKORDER_DETAILS_INT.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DosBiccExtractAM.SupplyRequestWorkOrderDtlsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 74 | 1 | 1 | 74 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[dos_workorder_details_int|DOS_WORKORDER_DETAILS_INT]] — 74 atributos (1 PKs, 74 BICC)

---

## ⚙️ Atributos

### [[dos_workorder_details_int|DOS_WORKORDER_DETAILS_INT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DosWorkOrderDetailsIntPEOActionCode | ACTION_CODE | — | ✅ |
| 2 | DosWorkOrderDetailsIntPEOAlternateNumber | ALTERNATE_NUMBER | — | ✅ |
| 3 | DosWorkOrderDetailsIntPEOAppliedResourceUnits | APPLIED_RESOURCE_UNITS | — | ✅ |
| 4 | DosWorkOrderDetailsIntPEOAppliedResourceValue | APPLIED_RESOURCE_VALUE | — | ✅ |
| 5 | DosWorkOrderDetailsIntPEOAssignedUnits | ASSIGNED_UNITS | — | ✅ |
| 6 | DosWorkOrderDetailsIntPEOBackflushFlag | BACKFLUSH_FLAG | — | ✅ |
| 7 | DosWorkOrderDetailsIntPEOCompChargeAccntId | COMP_CHARGE_ACCNT_ID | — | ✅ |
| 8 | DosWorkOrderDetailsIntPEOCompDateRequired | COMP_DATE_REQUIRED | — | ✅ |
| 9 | DosWorkOrderDetailsIntPEOCompItemIdNew | COMP_ITEM_ID_NEW | — | ✅ |
| 10 | DosWorkOrderDetailsIntPEOCompItemIdOld | COMP_ITEM_ID_OLD | — | ✅ |
| 11 | DosWorkOrderDetailsIntPEOCompItemNameNew | COMP_ITEM_NAME_NEW | — | ✅ |
| 12 | DosWorkOrderDetailsIntPEOCompItemNameOld | COMP_ITEM_NAME_OLD | — | ✅ |
| 13 | DosWorkOrderDetailsIntPEOCompItemRevision | COMP_ITEM_REVISION | — | ✅ |
| 14 | DosWorkOrderDetailsIntPEOCompMrpNetFlag | COMP_MRP_NET_FLAG | — | ✅ |
| 15 | DosWorkOrderDetailsIntPEOCompQuantityIssued | COMP_QUANTITY_ISSUED | — | ✅ |
| 16 | DosWorkOrderDetailsIntPEOCompQuantityPerAssembly | COMP_QUANTITY_PER_ASSEMBLY | — | ✅ |
| 17 | DosWorkOrderDetailsIntPEOCompRequiredQuantity | COMP_REQUIRED_QUANTITY | — | ✅ |
| 18 | DosWorkOrderDetailsIntPEOCompRequiredQuantityUom | COMP_REQUIRED_QUANTITY_UOM | — | ✅ |
| 19 | DosWorkOrderDetailsIntPEOCompSupplyLocatorId | COMP_SUPPLY_LOCATOR_ID | — | ✅ |
| 20 | DosWorkOrderDetailsIntPEOCompSupplyLocatorName | COMP_SUPPLY_LOCATOR_NAME | — | ✅ |
| 21 | DosWorkOrderDetailsIntPEOCompSupplySubInventory | COMP_SUPPLY_SUB_INVENTORY | — | ✅ |
| 22 | DosWorkOrderDetailsIntPEOCountPointType | COUNT_POINT_TYPE | — | ✅ |
| 23 | DosWorkOrderDetailsIntPEOCreatedBy | CREATED_BY | — | ✅ |
| 24 | DosWorkOrderDetailsIntPEOCreationDate | CREATION_DATE | — | ✅ |
| 25 | DosWorkOrderDetailsIntPEODetailType | DETAIL_TYPE | — | ✅ |
| 26 | DosWorkOrderDetailsIntPEOHeaderInterfaceId | HEADER_INTERFACE_ID | — | ✅ |
| 27 | DosWorkOrderDetailsIntPEOInterfaceBatchNumber | INTERFACE_BATCH_NUMBER | — | ✅ |
| 28 | DosWorkOrderDetailsIntPEOInterfaceStatusCode | INTERFACE_STATUS_CODE | — | ✅ |
| 29 | DosWorkOrderDetailsIntPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 30 | DosWorkOrderDetailsIntPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 31 | DosWorkOrderDetailsIntPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | DosWorkOrderDetailsIntPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 33 | DosWorkOrderDetailsIntPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 34 | DosWorkOrderDetailsIntPEOLineInterfaceId | LINE_INTERFACE_ID | — | ✅ |
| 35 | DosWorkOrderDetailsIntPEOLoadType | LOAD_TYPE | — | ✅ |
| 36 | DosWorkOrderDetailsIntPEOMaterialQtyPerProduct | MATERIAL_QTY_PER_PRODUCT | — | ✅ |
| 37 | DosWorkOrderDetailsIntPEOMaterialSeqNumber | MATERIAL_SEQ_NUMBER | — | ✅ |
| 38 | DosWorkOrderDetailsIntPEOMinTransferQuantity | MIN_TRANSFER_QUANTITY | — | ✅ |
| 39 | DosWorkOrderDetailsIntPEOMinTransferQuantityUom | MIN_TRANSFER_QUANTITY_UOM | — | ✅ |
| 40 | DosWorkOrderDetailsIntPEOMpsDateRequired | MPS_DATE_REQUIRED | — | ✅ |
| 41 | DosWorkOrderDetailsIntPEOMpsRequiredQuantity | MPS_REQUIRED_QUANTITY | — | ✅ |
| 42 | DosWorkOrderDetailsIntPEOMpsRequiredQuantityUom | MPS_REQUIRED_QUANTITY_UOM | — | ✅ |
| 43 | DosWorkOrderDetailsIntPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 44 | DosWorkOrderDetailsIntPEOOperationSequenceId | OPERATION_SEQUENCE_ID | — | ✅ |
| 45 | DosWorkOrderDetailsIntPEOOperationSequenceNumber | OPERATION_SEQUENCE_NUMBER | — | ✅ |
| 46 | DosWorkOrderDetailsIntPEORequestId | REQUEST_ID | — | ✅ |
| 47 | DosWorkOrderDetailsIntPEOResourceActivityId | RESOURCE_ACTIVITY_ID | — | ✅ |
| 48 | DosWorkOrderDetailsIntPEOResourceAutoChargeType | RESOURCE_AUTO_CHARGE_TYPE | — | ✅ |
| 49 | DosWorkOrderDetailsIntPEOResourceBasisType | RESOURCE_BASIS_TYPE | — | ✅ |
| 50 | DosWorkOrderDetailsIntPEOResourceCompletionDate | RESOURCE_COMPLETION_DATE | — | ✅ |
| 51 | DosWorkOrderDetailsIntPEOResourceDepartmentId | RESOURCE_DEPARTMENT_ID | — | ✅ |
| 52 | DosWorkOrderDetailsIntPEOResourceIdNew | RESOURCE_ID_NEW | — | ✅ |
| 53 | DosWorkOrderDetailsIntPEOResourceIdOld | RESOURCE_ID_OLD | — | ✅ |
| 54 | DosWorkOrderDetailsIntPEOResourceLoadType | RESOURCE_LOAD_TYPE | — | ✅ |
| 55 | DosWorkOrderDetailsIntPEOResourceNameNew | RESOURCE_NAME_NEW | — | ✅ |
| 56 | DosWorkOrderDetailsIntPEOResourceNameOld | RESOURCE_NAME_OLD | — | ✅ |
| 57 | DosWorkOrderDetailsIntPEOResourceSequenceNumber | RESOURCE_SEQUENCE_NUMBER | — | ✅ |
| 58 | DosWorkOrderDetailsIntPEOResourceStartDate | RESOURCE_START_DATE | — | ✅ |
| 59 | DosWorkOrderDetailsIntPEOResourceUomCode | RESOURCE_UOM_CODE | — | ✅ |
| 60 | DosWorkOrderDetailsIntPEOResourceUsageRateOrAmount | RESOURCE_USAGE_RATE_OR_AMOUNT | — | ✅ |
| 61 | DosWorkOrderDetailsIntPEOResoureDepartmentName | RESOURE_DEPARTMENT_NAME | — | ✅ |
| 62 | DosWorkOrderDetailsIntPEOScheduledFlag | SCHEDULED_FLAG | — | ✅ |
| 63 | DosWorkOrderDetailsIntPEOSourceCode | SOURCE_CODE | — | ✅ |
| 64 | DosWorkOrderDetailsIntPEOStandardOperationId | STANDARD_OPERATION_ID | — | ✅ |
| 65 | DosWorkOrderDetailsIntPEOStandardOperationName | STANDARD_OPERATION_NAME | — | ✅ |
| 66 | DosWorkOrderDetailsIntPEOStandardRateFlag | STANDARD_RATE_FLAG | — | ✅ |
| 67 | DosWorkOrderDetailsIntPEOSubstituteQtyPerProduct | SUBSTITUTE_QTY_PER_PRODUCT | — | ✅ |
| 68 | DosWorkOrderDetailsIntPEOSubstitutionType | SUBSTITUTION_TYPE | — | ✅ |
| 69 | DosWorkOrderDetailsIntPEOWdOpAltResourceId | WD_OP_ALT_RESOURCE_ID | — | ✅ |
| 70 | DosWorkOrderDetailsIntPEOWipEntityId | WIP_ENTITY_ID | — | ✅ |
| 71 | DosWorkOrderDetailsIntPEOWipSupplyType | WIP_SUPPLY_TYPE | — | ✅ |
| 72 | DosWorkOrderDetailsIntPEOWoProcessPhase | WO_PROCESS_PHASE | — | ✅ |
| 73 | DosWorkOrderDetailsIntPEOWoProcessStatus | WO_PROCESS_STATUS | — | ✅ |
| 74 | DosWorkOrderDetailsIntPEOWorkorderDetailsIntfId | WORKORDER_DETAILS_INTF_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
