---
id: DOC-OTHER-PVO-InventorySubinventoryExtractPVO
doc_type: system-doc
title: "InventorySubinventoryExtractPVO — PVO Cross-Module"
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
  - InventorySubinventoryExtractPVO
  - inventorysubinventoryextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InventorySubinventoryExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inventory Subinventory Extract. Acessa as tabelas: INV_SECONDARY_INVENTORIES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.InvBiccExtractAM.InventorySubinventoryExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 51 | 1 | 2 | 51 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[inv_secondary_inventories|INV_SECONDARY_INVENTORIES]] — 51 atributos (2 PKs, 51 BICC)

---

## ⚙️ Atributos

### [[inv_secondary_inventories|INV_SECONDARY_INVENTORIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvSubinvPEOAssetInventory | ASSET_INVENTORY | — | ✅ |
| 2 | InvSubinvPEOAvailabilityType | AVAILABILITY_TYPE | — | ✅ |
| 3 | InvSubinvPEOCartonizationFlag | CARTONIZATION_FLAG | — | ✅ |
| 4 | InvSubinvPEOCountMethod | COUNT_METHOD | — | ✅ |
| 5 | InvSubinvPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | InvSubinvPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | InvSubinvPEODefaultCountTypeCode | DEFAULT_COUNT_TYPE_CODE | — | ✅ |
| 8 | InvSubinvPEODefaultLocStatusId | DEFAULT_LOC_STATUS_ID | — | ✅ |
| 9 | InvSubinvPEODemandClass | DEMAND_CLASS | — | ✅ |
| 10 | InvSubinvPEODepreciableFlag | DEPRECIABLE_FLAG | — | ✅ |
| 11 | InvSubinvPEODescription | DESCRIPTION | — | ✅ |
| 12 | InvSubinvPEODisableDate | DISABLE_DATE | — | ✅ |
| 13 | InvSubinvPEODroppingOrder | DROPPING_ORDER | — | ✅ |
| 14 | InvSubinvPEOEnableBulkPick | ENABLE_BULK_PICK | — | ✅ |
| 15 | InvSubinvPEOEnableLocatorAlias | ENABLE_LOCATOR_ALIAS | — | ✅ |
| 16 | InvSubinvPEOEnforceAliasUniqueness | ENFORCE_ALIAS_UNIQUENESS | — | ✅ |
| 17 | InvSubinvPEOInventoryAtpCode | INVENTORY_ATP_CODE | — | ✅ |
| 18 | InvSubinvPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 19 | InvSubinvPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 20 | InvSubinvPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | InvSubinvPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 22 | InvSubinvPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 23 | InvSubinvPEOLocationId | LOCATION_ID | — | ✅ |
| 24 | InvSubinvPEOLocatorType | LOCATOR_TYPE | — | ✅ |
| 25 | InvSubinvPEOLpnControlledFlag | LPN_CONTROLLED_FLAG | — | ✅ |
| 26 | InvSubinvPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 27 | InvSubinvPEOOrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 28 | InvSubinvPEOPickMethodology | PICK_METHODOLOGY | — | ✅ |
| 29 | InvSubinvPEOPickUomCode | PICK_UOM_CODE | — | ✅ |
| 30 | InvSubinvPEOPickingOrder | PICKING_ORDER | — | ✅ |
| 31 | InvSubinvPEOPlanningLevel | PLANNING_LEVEL | — | ✅ |
| 32 | InvSubinvPEOPostprocessingLeadTime | POSTPROCESSING_LEAD_TIME | — | ✅ |
| 33 | InvSubinvPEOPreprocessingLeadTime | PREPROCESSING_LEAD_TIME | — | ✅ |
| 34 | InvSubinvPEOProcessingLeadTime | PROCESSING_LEAD_TIME | — | ✅ |
| 35 | InvSubinvPEOProjectId | PROJECT_ID | — | ✅ |
| 36 | InvSubinvPEOQuantityTracked | QUANTITY_TRACKED | — | ✅ |
| 37 | InvSubinvPEORequestId | REQUEST_ID | — | ✅ |
| 38 | InvSubinvPEORequisitionApprovalType | REQUISITION_APPROVAL_TYPE | — | ✅ |
| 39 | InvSubinvPEOReservableType | RESERVABLE_TYPE | — | ✅ |
| 40 | InvSubinvPEOSecondaryInventoryName | SECONDARY_INVENTORY_NAME | 🔑 | ✅ |
| 41 | InvSubinvPEOSourceOrganizationId | SOURCE_ORGANIZATION_ID | — | ✅ |
| 42 | InvSubinvPEOSourceSubinventory | SOURCE_SUBINVENTORY | — | ✅ |
| 43 | InvSubinvPEOSourceType | SOURCE_TYPE | — | ✅ |
| 44 | InvSubinvPEOStandardPackType | STANDARD_PACK_TYPE | — | ✅ |
| 45 | InvSubinvPEOStatusId | STATUS_ID | — | ✅ |
| 46 | InvSubinvPEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | ✅ |
| 47 | InvSubinvPEOSubinventoryGroup | SUBINVENTORY_GROUP | — | ✅ |
| 48 | InvSubinvPEOSubinventoryId | SUBINVENTORY_ID | — | ✅ |
| 49 | InvSubinvPEOSubinventoryType | SUBINVENTORY_TYPE | — | ✅ |
| 50 | InvSubinvPEOSubinventoryUsage | SUBINVENTORY_USAGE | — | ✅ |
| 51 | InvSubinvPEOTaskId | TASK_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
