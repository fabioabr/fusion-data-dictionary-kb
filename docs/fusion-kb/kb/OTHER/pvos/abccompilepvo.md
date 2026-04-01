---
id: DOC-OTHER-PVO-AbcCompilePVO
doc_type: system-doc
title: "AbcCompilePVO — PVO Cross-Module"
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
  - AbcCompilePVO
  - abccompilepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AbcCompilePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Abc Compile. Acessa as tabelas: INV_ABC_COMPILES, INV_ABC_COMPILE_HEADERS.

**Caminho:** `FscmTopModelAM.InventoryAM.AbcCompilePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 46 | 2 | 2 | 46 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[inv_abc_compiles|INV_ABC_COMPILES]] — 19 atributos (2 PKs, 19 BICC)
- [[inv_abc_compile_headers|INV_ABC_COMPILE_HEADERS]] — 27 atributos (27 BICC)

---

## ⚙️ Atributos

### [[inv_abc_compiles|INV_ABC_COMPILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbcCompilePEOCompileId | COMPILE_ID | 🔑 | ✅ |
| 2 | AbcCompilePEOCompileQuantity | COMPILE_QUANTITY | — | ✅ |
| 3 | AbcCompilePEOCompileValue | COMPILE_VALUE | — | ✅ |
| 4 | AbcCompilePEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | AbcCompilePEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | AbcCompilePEOCumulativeQuantity | CUMULATIVE_QUANTITY | — | ✅ |
| 7 | AbcCompilePEOCumulativeValue | CUMULATIVE_VALUE | — | ✅ |
| 8 | AbcCompilePEOInventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 9 | AbcCompilePEOItemUnitCost | ITEM_UNIT_COST | — | ✅ |
| 10 | AbcCompilePEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 11 | AbcCompilePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 12 | AbcCompilePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | AbcCompilePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | AbcCompilePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | AbcCompilePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | AbcCompilePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 17 | AbcCompilePEORequestId | REQUEST_ID | — | ✅ |
| 18 | AbcCompilePEOSecondaryInventory | SECONDARY_INVENTORY | — | ✅ |
| 19 | AbcCompilePEOSequenceNumber | SEQUENCE_NUMBER | — | ✅ |

### [[inv_abc_compile_headers|INV_ABC_COMPILE_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbcCompileHeaderPEOCompileDate | COMPILE_DATE | — | ✅ |
| 2 | AbcCompileHeaderPEOCompileId | COMPILE_ID | — | ✅ |
| 3 | AbcCompileHeaderPEOCompileItems | COMPILE_ITEMS | — | ✅ |
| 4 | AbcCompileHeaderPEOCompileName | COMPILE_NAME | — | ✅ |
| 5 | AbcCompileHeaderPEOCompileStatus | COMPILE_STATUS | — | ✅ |
| 6 | AbcCompileHeaderPEOCompileType | COMPILE_TYPE | — | ✅ |
| 7 | AbcCompileHeaderPEOCostType | COST_TYPE | — | ✅ |
| 8 | AbcCompileHeaderPEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | AbcCompileHeaderPEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | AbcCompileHeaderPEOCumulativeQuantity | CUMULATIVE_QUANTITY | — | ✅ |
| 11 | AbcCompileHeaderPEOCumulativeValue | CUMULATIVE_VALUE | — | ✅ |
| 12 | AbcCompileHeaderPEOCutoffDate | CUTOFF_DATE | — | ✅ |
| 13 | AbcCompileHeaderPEODescription | DESCRIPTION | — | ✅ |
| 14 | AbcCompileHeaderPEOItemScopeCode | ITEM_SCOPE_CODE | — | ✅ |
| 15 | AbcCompileHeaderPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 16 | AbcCompileHeaderPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 17 | AbcCompileHeaderPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | AbcCompileHeaderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 19 | AbcCompileHeaderPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 20 | AbcCompileHeaderPEOMrpForecastName | MRP_FORECAST_NAME | — | ✅ |
| 21 | AbcCompileHeaderPEOMrpPlanName | MRP_PLAN_NAME | — | ✅ |
| 22 | AbcCompileHeaderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 23 | AbcCompileHeaderPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 24 | AbcCompileHeaderPEORequestId | REQUEST_ID | — | ✅ |
| 25 | AbcCompileHeaderPEOScheduleDesignator | SCHEDULE_DESIGNATOR | — | ✅ |
| 26 | AbcCompileHeaderPEOSecondaryInventory | SECONDARY_INVENTORY | — | ✅ |
| 27 | AbcCompileHeaderPEOStartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
