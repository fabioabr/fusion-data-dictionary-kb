---
id: DOC-OTHER-PVO-AbcAssignmentPVO
doc_type: system-doc
title: "AbcAssignmentPVO — PVO Cross-Module"
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
  - AbcAssignmentPVO
  - abcassignmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AbcAssignmentPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Abc Assignment. Acessa as tabelas: INV_ABC_ASSIGNMENT_V, INV_ABC_COMPILES, INV_ABC_COMPILE_HEADERS.

**Caminho:** `FscmTopModelAM.InventoryAM.AbcAssignmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 88 | 3 | 3 | 87 | 99% |

---

## 🔗 Tabelas Relacionadas

- [[inv_abc_assignment_v|INV_ABC_ASSIGNMENT_V]] — 42 atributos (3 PKs, 41 BICC)
- [[inv_abc_compiles|INV_ABC_COMPILES]] — 19 atributos (19 BICC)
- [[inv_abc_compile_headers|INV_ABC_COMPILE_HEADERS]] — 27 atributos (27 BICC)

---

## ⚙️ Atributos

### [[inv_abc_assignment_v|INV_ABC_ASSIGNMENT_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ViewPEOAgAssignmentGroupId | AG_ASSIGNMENT_GROUP_ID | 🔑 | ✅ |
| 2 | ViewPEOAgAssignmentGroupName | AG_ASSIGNMENT_GROUP_NAME | — | ✅ |
| 3 | ViewPEOAgCompileId | AG_COMPILE_ID | — | ✅ |
| 4 | ViewPEOAgCreatedBy | AG_CREATED_BY | — | ✅ |
| 5 | ViewPEOAgCreationDate | AG_CREATION_DATE | — | ✅ |
| 6 | ViewPEOAgItemScopeType | AG_ITEM_SCOPE_TYPE | — | ✅ |
| 7 | ViewPEOAgJobDefinitionName | AG_JOB_DEFINITION_NAME | — | ✅ |
| 8 | ViewPEOAgJobDefinitionPackage | AG_JOB_DEFINITION_PACKAGE | — | ✅ |
| 9 | ViewPEOAgLastUpdateDate | AG_LAST_UPDATE_DATE | — | ✅ |
| 10 | ViewPEOAgLastUpdateLogin | AG_LAST_UPDATE_LOGIN | — | ✅ |
| 11 | ViewPEOAgLastUpdatedBy | AG_LAST_UPDATED_BY | — | ✅ |
| 12 | ViewPEOAgObjectVersionNumber | AG_OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | ViewPEOAgOrganizationId | AG_ORGANIZATION_ID | — | ✅ |
| 14 | ViewPEOAgRequestId | AG_REQUEST_ID | — | ✅ |
| 15 | ViewPEOAgSecondaryInventory | AG_SECONDARY_INVENTORY | — | ✅ |
| 16 | ViewPEOAgcAbcClassId | AGC_ABC_CLASS_ID | 🔑 | ✅ |
| 17 | ViewPEOAgcAbcGroupClassId | AGC_ABC_GROUP_CLASS_ID | — | ✅ |
| 18 | ViewPEOAgcCreatedBy | AGC_CREATED_BY | — | ✅ |
| 19 | ViewPEOAgcCreationDate | AGC_CREATION_DATE | — | ✅ |
| 20 | ViewPEOAgcItemSeqNumber | AGC_ITEM_SEQ_NUMBER | — | ✅ |
| 21 | ViewPEOAgcJobDefinitionName | AGC_JOB_DEFINITION_NAME | — | ✅ |
| 22 | ViewPEOAgcJobDefinitionPackage | AGC_JOB_DEFINITION_PACKAGE | — | ✅ |
| 23 | ViewPEOAgcLastUpdateDate | AGC_LAST_UPDATE_DATE | — | ✅ |
| 24 | ViewPEOAgcLastUpdateLogin | AGC_LAST_UPDATE_LOGIN | — | ✅ |
| 25 | ViewPEOAgcLastUpdatedBy | AGC_LAST_UPDATED_BY | — | ✅ |
| 26 | ViewPEOAgcObjectVersionNumber | AGC_OBJECT_VERSION_NUMBER | — | ✅ |
| 27 | ViewPEOAgcPercentOfItems | AGC_PERCENT_OF_ITEMS | — | ✅ |
| 28 | ViewPEOAgcPercentOfValue | AGC_PERCENT_OF_VALUE | — | ✅ |
| 29 | ViewPEOAgcRequestId | AGC_REQUEST_ID | — | ✅ |
| 30 | ViewPEOAgcSequenceNumber | AGC_SEQUENCE_NUMBER | — | ✅ |
| 31 | ViewPEOAsgnAbcAssignmentId | ASGN_ABC_ASSIGNMENT_ID | — | ✅ |
| 32 | ViewPEOAsgnCreatedBy | ASGN_CREATED_BY | — | ✅ |
| 33 | ViewPEOAsgnCreationDate | ASGN_CREATION_DATE | — | ✅ |
| 34 | ViewPEOAsgnInventoryItemId | ASGN_INVENTORY_ITEM_ID | 🔑 | ✅ |
| 35 | ViewPEOAsgnJobDefinitionName | ASGN_JOB_DEFINITION_NAME | — | ✅ |
| 36 | ViewPEOAsgnJobDefinitionPackage | ASGN_JOB_DEFINITION_PACKAGE | — | ✅ |
| 37 | ViewPEOAsgnLastUpdateDate | ASGN_LAST_UPDATE_DATE | — | ✅ |
| 38 | ViewPEOAsgnLastUpdateLogin | ASGN_LAST_UPDATE_LOGIN | — | ✅ |
| 39 | ViewPEOAsgnLastUpdatedBy | ASGN_LAST_UPDATED_BY | — | ✅ |
| 40 | ViewPEOAsgnObjectVersionNumber | ASGN_OBJECT_VERSION_NUMBER | — | ✅ |
| 41 | ViewPEOAsgnOrganizationId | ORGANIZATION_ID | — | — |
| 42 | ViewPEOAsgnRequestId | ASGN_REQUEST_ID | — | ✅ |

### [[inv_abc_compiles|INV_ABC_COMPILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CompilePEOCompileId | COMPILE_ID | — | ✅ |
| 2 | CompilePEOCompileQuantity | COMPILE_QUANTITY | — | ✅ |
| 3 | CompilePEOCompileValue | COMPILE_VALUE | — | ✅ |
| 4 | CompilePEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | CompilePEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | CompilePEOCumulativeQuantity | CUMULATIVE_QUANTITY | — | ✅ |
| 7 | CompilePEOCumulativeValue | CUMULATIVE_VALUE | — | ✅ |
| 8 | CompilePEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 9 | CompilePEOItemUnitCost | ITEM_UNIT_COST | — | ✅ |
| 10 | CompilePEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 11 | CompilePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 12 | CompilePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | CompilePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | CompilePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | CompilePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | CompilePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 17 | CompilePEORequestId | REQUEST_ID | — | ✅ |
| 18 | CompilePEOSecondaryInventory | SECONDARY_INVENTORY | — | ✅ |
| 19 | CompilePEOSequenceNumber | SEQUENCE_NUMBER | — | ✅ |

### [[inv_abc_compile_headers|INV_ABC_COMPILE_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HeaderPEOCompileDate | COMPILE_DATE | — | ✅ |
| 2 | HeaderPEOCompileId | COMPILE_ID | — | ✅ |
| 3 | HeaderPEOCompileItems | COMPILE_ITEMS | — | ✅ |
| 4 | HeaderPEOCompileName | COMPILE_NAME | — | ✅ |
| 5 | HeaderPEOCompileStatus | COMPILE_STATUS | — | ✅ |
| 6 | HeaderPEOCompileType | COMPILE_TYPE | — | ✅ |
| 7 | HeaderPEOCostType | COST_TYPE | — | ✅ |
| 8 | HeaderPEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | HeaderPEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | HeaderPEOCumulativeQuantity | CUMULATIVE_QUANTITY | — | ✅ |
| 11 | HeaderPEOCumulativeValue | CUMULATIVE_VALUE | — | ✅ |
| 12 | HeaderPEOCutoffDate | CUTOFF_DATE | — | ✅ |
| 13 | HeaderPEODescription | DESCRIPTION | — | ✅ |
| 14 | HeaderPEOItemScopeCode | ITEM_SCOPE_CODE | — | ✅ |
| 15 | HeaderPEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 16 | HeaderPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 17 | HeaderPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | HeaderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 19 | HeaderPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 20 | HeaderPEOMrpForecastName | MRP_FORECAST_NAME | — | ✅ |
| 21 | HeaderPEOMrpPlanName | MRP_PLAN_NAME | — | ✅ |
| 22 | HeaderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 23 | HeaderPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 24 | HeaderPEORequestId | REQUEST_ID | — | ✅ |
| 25 | HeaderPEOScheduleDesignator | SCHEDULE_DESIGNATOR | — | ✅ |
| 26 | HeaderPEOSecondaryInventory | SECONDARY_INVENTORY | — | ✅ |
| 27 | HeaderPEOStartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
