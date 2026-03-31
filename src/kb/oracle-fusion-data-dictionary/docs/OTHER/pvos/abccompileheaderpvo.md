---
id: DOC-OTHER-PVO-AbcCompileHeaderPVO
doc_type: system-doc
title: "AbcCompileHeaderPVO — PVO Cross-Module"
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
  - AbcCompileHeaderPVO
  - abccompileheaderpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AbcCompileHeaderPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Abc Compile Header. Acessa as tabelas: INV_ABC_COMPILE_HEADERS.

**Caminho:** `FscmTopModelAM.InventoryAM.AbcCompileHeaderPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 1 | 1 | 27 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[inv_abc_compile_headers|INV_ABC_COMPILE_HEADERS]] — 27 atributos (1 PKs, 27 BICC)

---

## ⚙️ Atributos

### [[inv_abc_compile_headers|INV_ABC_COMPILE_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CompileDate | COMPILE_DATE | — | ✅ |
| 2 | CompileId | COMPILE_ID | 🔑 | ✅ |
| 3 | CompileItems | COMPILE_ITEMS | — | ✅ |
| 4 | CompileName | COMPILE_NAME | — | ✅ |
| 5 | CompileStatus | COMPILE_STATUS | — | ✅ |
| 6 | CompileType | COMPILE_TYPE | — | ✅ |
| 7 | CostType | COST_TYPE | — | ✅ |
| 8 | CreatedBy | CREATED_BY | — | ✅ |
| 9 | CreationDate | CREATION_DATE | — | ✅ |
| 10 | CumulativeQuantity | CUMULATIVE_QUANTITY | — | ✅ |
| 11 | CumulativeValue | CUMULATIVE_VALUE | — | ✅ |
| 12 | CutoffDate | CUTOFF_DATE | — | ✅ |
| 13 | Description | DESCRIPTION | — | ✅ |
| 14 | ItemScopeCode | ITEM_SCOPE_CODE | — | ✅ |
| 15 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 16 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 17 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 19 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 20 | MrpForecastName | MRP_FORECAST_NAME | — | ✅ |
| 21 | MrpPlanName | MRP_PLAN_NAME | — | ✅ |
| 22 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 23 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 24 | RequestId | REQUEST_ID | — | ✅ |
| 25 | ScheduleDesignator | SCHEDULE_DESIGNATOR | — | ✅ |
| 26 | SecondaryInventory | SECONDARY_INVENTORY | — | ✅ |
| 27 | StartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
