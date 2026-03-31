---
id: DOC-OTHER-PVO-InvItemSubinventoryPVO
doc_type: system-doc
title: "InvItemSubinventoryPVO — PVO Cross-Module"
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
  - InvItemSubinventoryPVO
  - invitemsubinventorypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvItemSubinventoryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inv Item Subinventory. Acessa as tabelas: INV_ITEM_SUB_INVENTORIES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.InvBiccExtractAM.InvItemSubinventoryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 49 | 1 | 3 | 49 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[inv_item_sub_inventories|INV_ITEM_SUB_INVENTORIES]] — 49 atributos (3 PKs, 49 BICC)

---

## ⚙️ Atributos

### [[inv_item_sub_inventories|INV_ITEM_SUB_INVENTORIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute1 | ATTRIBUTE1 | — | ✅ |
| 2 | Attribute10 | ATTRIBUTE10 | — | ✅ |
| 3 | Attribute11 | ATTRIBUTE11 | — | ✅ |
| 4 | Attribute12 | ATTRIBUTE12 | — | ✅ |
| 5 | Attribute13 | ATTRIBUTE13 | — | ✅ |
| 6 | Attribute14 | ATTRIBUTE14 | — | ✅ |
| 7 | Attribute15 | ATTRIBUTE15 | — | ✅ |
| 8 | Attribute2 | ATTRIBUTE2 | — | ✅ |
| 9 | Attribute3 | ATTRIBUTE3 | — | ✅ |
| 10 | Attribute4 | ATTRIBUTE4 | — | ✅ |
| 11 | Attribute5 | ATTRIBUTE5 | — | ✅ |
| 12 | Attribute6 | ATTRIBUTE6 | — | ✅ |
| 13 | Attribute7 | ATTRIBUTE7 | — | ✅ |
| 14 | Attribute8 | ATTRIBUTE8 | — | ✅ |
| 15 | Attribute9 | ATTRIBUTE9 | — | ✅ |
| 16 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 17 | CountRequired | COUNT_REQUIRED | — | ✅ |
| 18 | CreatedBy | CREATED_BY | — | ✅ |
| 19 | CreationDate | CREATION_DATE | — | ✅ |
| 20 | DefaultCountTypeCode | DEFAULT_COUNT_TYPE_CODE | — | ✅ |
| 21 | FixedLotMultiple | FIXED_LOT_MULTIPLE | — | ✅ |
| 22 | InventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 23 | InventoryPlanningCode | INVENTORY_PLANNING_CODE | — | ✅ |
| 24 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 25 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 26 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 27 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 28 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 29 | MaxMinmaxQuantity | MAX_MINMAX_QUANTITY | — | ✅ |
| 30 | MaximumOrderQuantity | MAXIMUM_ORDER_QUANTITY | — | ✅ |
| 31 | MinMinmaxQuantity | MIN_MINMAX_QUANTITY | — | ✅ |
| 32 | MinimumOrderQuantity | MINIMUM_ORDER_QUANTITY | — | ✅ |
| 33 | MinmaxQuantityUom | MINMAX_QUANTITY_UOM | — | ✅ |
| 34 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 35 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 36 | ParLevel | PAR_LEVEL | — | ✅ |
| 37 | ParMaxQty | PAR_MAX_QTY | — | ✅ |
| 38 | ParUomCode | PAR_UOM_CODE | — | ✅ |
| 39 | PickingOrder | PICKING_ORDER | — | ✅ |
| 40 | PostprocessingLeadTime | POSTPROCESSING_LEAD_TIME | — | ✅ |
| 41 | PreprocessingLeadTime | PREPROCESSING_LEAD_TIME | — | ✅ |
| 42 | PrimarySubinventoryFlag | PRIMARY_SUBINVENTORY_FLAG | — | ✅ |
| 43 | ProcessingLeadTime | PROCESSING_LEAD_TIME | — | ✅ |
| 44 | QtyCountTolerance | QTY_COUNT_TOLERANCE | — | ✅ |
| 45 | RequestId | REQUEST_ID | — | ✅ |
| 46 | SecondaryInventory | SECONDARY_INVENTORY | 🔑 | ✅ |
| 47 | SourceOrganizationId | SOURCE_ORGANIZATION_ID | — | ✅ |
| 48 | SourceSubinventory | SOURCE_SUBINVENTORY | — | ✅ |
| 49 | SourceType | SOURCE_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
