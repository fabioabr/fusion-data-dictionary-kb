---
id: DOC-OTHER-PVO-InvItemLocatorPVO
doc_type: system-doc
title: "InvItemLocatorPVO — PVO Cross-Module"
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
  - InvItemLocatorPVO
  - invitemlocatorpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvItemLocatorPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inv Item Locator. Acessa as tabelas: INV_ITEM_LOCATIONS, INV_SECONDARY_LOCATORS.

**Caminho:** `FscmTopModelAM.InventoryAM.InvItemLocatorPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 2 | 3 | 10 | 37% |

---

## 🔗 Tabelas Relacionadas

- [[inv_item_locations|INV_ITEM_LOCATIONS]] — 4 atributos
- [[inv_secondary_locators|INV_SECONDARY_LOCATORS]] — 23 atributos (3 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[inv_item_locations|INV_ITEM_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | — |
| 2 | InventoryLocatorPEOInventoryLocationId | INVENTORY_LOCATION_ID | — | — |
| 3 | InventoryLocatorPEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 4 | InventoryLocatorPEOSubinventoryId | SUBINVENTORY_ID | — | — |

### [[inv_secondary_locators|INV_SECONDARY_LOCATORS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CountRequired | COUNT_REQUIRED | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | DefaultCountTypeCode | DEFAULT_COUNT_TYPE_CODE | — | ✅ |
| 5 | InventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 6 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 7 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | MaximumQuantity | MAXIMUM_QUANTITY | — | — |
| 12 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 14 | ParLevel | PAR_LEVEL | — | ✅ |
| 15 | ParMaxQty | PAR_MAX_QTY | — | ✅ |
| 16 | ParUomCode | PAR_UOM_CODE | — | ✅ |
| 17 | PickingOrder | PICKING_ORDER | — | — |
| 18 | PrimaryLocatorFlag | PRIMARY_LOCATOR_FLAG | — | — |
| 19 | QtyCountTolerance | QTY_COUNT_TOLERANCE | — | ✅ |
| 20 | RequestId | REQUEST_ID | — | — |
| 21 | SecondaryLocator | SECONDARY_LOCATOR | 🔑 | ✅ |
| 22 | StatusId | STATUS_ID | — | — |
| 23 | SubinventoryCode | SUBINVENTORY_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
