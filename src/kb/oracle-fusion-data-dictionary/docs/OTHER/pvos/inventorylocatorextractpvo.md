---
id: DOC-OTHER-PVO-InventoryLocatorExtractPVO
doc_type: system-doc
title: "InventoryLocatorExtractPVO — PVO Cross-Module"
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
  - InventoryLocatorExtractPVO
  - inventorylocatorextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InventoryLocatorExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inventory Locator Extract. Acessa as tabelas: INV_ITEM_LOCATIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.InvBiccExtractAM.InventoryLocatorExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 59 | 1 | 1 | 59 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[inv_item_locations|INV_ITEM_LOCATIONS]] — 59 atributos (1 PKs, 59 BICC)

---

## ⚙️ Atributos

### [[inv_item_locations|INV_ITEM_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvLocatorPEOAlias | ALIAS | — | ✅ |
| 2 | InvLocatorPEOAvailabilityType | AVAILABILITY_TYPE | — | ✅ |
| 3 | InvLocatorPEOAvailableCubicArea | AVAILABLE_CUBIC_AREA | — | ✅ |
| 4 | InvLocatorPEOAvailableWeight | AVAILABLE_WEIGHT | — | ✅ |
| 5 | InvLocatorPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | InvLocatorPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | InvLocatorPEOCurrentCubicArea | CURRENT_CUBIC_AREA | — | ✅ |
| 8 | InvLocatorPEOCurrentWeight | CURRENT_WEIGHT | — | ✅ |
| 9 | InvLocatorPEODepreciableFlag | DEPRECIABLE_FLAG | — | ✅ |
| 10 | InvLocatorPEODescription | DESCRIPTION | — | ✅ |
| 11 | InvLocatorPEODimensionUomCode | DIMENSION_UOM_CODE | — | ✅ |
| 12 | InvLocatorPEODisableDate | DISABLE_DATE | — | ✅ |
| 13 | InvLocatorPEODroppingOrder | DROPPING_ORDER | — | ✅ |
| 14 | InvLocatorPEOEmptyFlag | EMPTY_FLAG | — | ✅ |
| 15 | InvLocatorPEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 16 | InvLocatorPEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 17 | InvLocatorPEOInventoryAtpCode | INVENTORY_ATP_CODE | — | ✅ |
| 18 | InvLocatorPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 19 | InvLocatorPEOInventoryLocationId | INVENTORY_LOCATION_ID | 🔑 | ✅ |
| 20 | InvLocatorPEOInventoryLocationType | INVENTORY_LOCATION_TYPE | — | ✅ |
| 21 | InvLocatorPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 22 | InvLocatorPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 23 | InvLocatorPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | InvLocatorPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 25 | InvLocatorPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 26 | InvLocatorPEOLocationAvailableUnits | LOCATION_AVAILABLE_UNITS | — | ✅ |
| 27 | InvLocatorPEOLocationCurrentUnits | LOCATION_CURRENT_UNITS | — | ✅ |
| 28 | InvLocatorPEOLocationHeight | LOCATION_HEIGHT | — | ✅ |
| 29 | InvLocatorPEOLocationLength | LOCATION_LENGTH | — | ✅ |
| 30 | InvLocatorPEOLocationMaximumUnits | LOCATION_MAXIMUM_UNITS | — | ✅ |
| 31 | InvLocatorPEOLocationSuggestedUnits | LOCATION_SUGGESTED_UNITS | — | ✅ |
| 32 | InvLocatorPEOLocationWeightUomCode | LOCATION_WEIGHT_UOM_CODE | — | ✅ |
| 33 | InvLocatorPEOLocationWidth | LOCATION_WIDTH | — | ✅ |
| 34 | InvLocatorPEOLocatorStatus | LOCATOR_STATUS | — | ✅ |
| 35 | InvLocatorPEOMaxCubicArea | MAX_CUBIC_AREA | — | ✅ |
| 36 | InvLocatorPEOMaxWeight | MAX_WEIGHT | — | ✅ |
| 37 | InvLocatorPEOMixedItemsFlag | MIXED_ITEMS_FLAG | — | ✅ |
| 38 | InvLocatorPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 39 | InvLocatorPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 40 | InvLocatorPEOPhysicalLocationCode | PHYSICAL_LOCATION_CODE | — | ✅ |
| 41 | InvLocatorPEOPhysicalLocationId | PHYSICAL_LOCATION_ID | — | ✅ |
| 42 | InvLocatorPEOPickUomCode | PICK_UOM_CODE | — | ✅ |
| 43 | InvLocatorPEOPickingOrder | PICKING_ORDER | — | ✅ |
| 44 | InvLocatorPEOProjectId | PROJECT_ID | — | ✅ |
| 45 | InvLocatorPEORequestId | REQUEST_ID | — | ✅ |
| 46 | InvLocatorPEOReservableType | RESERVABLE_TYPE | — | ✅ |
| 47 | InvLocatorPEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 48 | InvLocatorPEOStatusId | STATUS_ID | — | ✅ |
| 49 | InvLocatorPEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | ✅ |
| 50 | InvLocatorPEOSubinventoryCode | SUBINVENTORY_CODE | — | ✅ |
| 51 | InvLocatorPEOSubinventoryId | SUBINVENTORY_ID | — | ✅ |
| 52 | InvLocatorPEOSuggestedCubicArea | SUGGESTED_CUBIC_AREA | — | ✅ |
| 53 | InvLocatorPEOSuggestedWeight | SUGGESTED_WEIGHT | — | ✅ |
| 54 | InvLocatorPEOSummaryFlag | SUMMARY_FLAG | — | ✅ |
| 55 | InvLocatorPEOTaskId | TASK_ID | — | ✅ |
| 56 | InvLocatorPEOVolumeUomCode | VOLUME_UOM_CODE | — | ✅ |
| 57 | InvLocatorPEOXCoordinate | X_COORDINATE | — | ✅ |
| 58 | InvLocatorPEOYCoordinate | Y_COORDINATE | — | ✅ |
| 59 | InvLocatorPEOZCoordinate | Z_COORDINATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
