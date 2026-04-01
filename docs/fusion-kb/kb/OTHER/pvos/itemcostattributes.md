---
id: DOC-OTHER-PVO-ItemCostAttributes
doc_type: system-doc
title: "ItemCostAttributes — PVO Cross-Module"
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
  - ItemCostAttributes
  - itemcostattributes
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemCostAttributes

## 📌 Visão Geral

View Object para extração BICC de dados de Item Cost Attributes. Acessa as tabelas: ACA_PD_ITEM_COST.

**Caminho:** `FscmTopModelAM.EgpItemsPublicModelAM.ItemCostAttributes`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 1 | 1 | 4 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[aca_pd_item_cost|ACA_PD_ITEM_COST]] — 25 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[aca_pd_item_cost|ACA_PD_ITEM_COST]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemCostAttributesPEOCostSource | COST_SOURCE | — | — |
| 2 | ItemCostAttributesPEOCreatedBy | CREATED_BY | — | — |
| 3 | ItemCostAttributesPEOCreationDate | CREATION_DATE | — | — |
| 4 | ItemCostAttributesPEOCurrencyCode | CURRENCY_CODE | — | — |
| 5 | ItemCostAttributesPEOFromRevision | FROM_REVISION | — | — |
| 6 | ItemCostAttributesPEOIncompleteCostCnt | INCOMPLETE_COST_CNT | — | — |
| 7 | ItemCostAttributesPEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 8 | ItemCostAttributesPEOInventoryOrgId | INVENTORY_ORG_ID | — | — |
| 9 | ItemCostAttributesPEOIsLeaf | IS_LEAF | — | — |
| 10 | ItemCostAttributesPEOItemCostId | ITEM_COST_ID | 🔑 | ✅ |
| 11 | ItemCostAttributesPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 12 | ItemCostAttributesPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 13 | ItemCostAttributesPEOLastCostExtractDate | LAST_COST_EXTRACT_DATE | — | — |
| 14 | ItemCostAttributesPEOLastRollupDate | LAST_ROLLUP_DATE | — | — |
| 15 | ItemCostAttributesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | ItemCostAttributesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | ItemCostAttributesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | ItemCostAttributesPEOMaterialCost | MATERIAL_COST | — | ✅ |
| 19 | ItemCostAttributesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | ItemCostAttributesPEOOrganizationId | ORGANIZATION_ID | — | — |
| 21 | ItemCostAttributesPEOOverheadCost | OVERHEAD_COST | — | ✅ |
| 22 | ItemCostAttributesPEORequestId | REQUEST_ID | — | — |
| 23 | ItemCostAttributesPEORollupMaterialCost | ROLLUP_MATERIAL_COST | — | — |
| 24 | ItemCostAttributesPEORollupOverheadCost | ROLLUP_OVERHEAD_COST | — | — |
| 25 | ItemCostAttributesPEOToRevision | TO_REVISION | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
