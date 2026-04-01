---
id: DOC-PO-PVO-BrowsingCategoryHierarchyExtractPVO
doc_type: system-doc
title: "BrowsingCategoryHierarchyExtractPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - BrowsingCategoryHierarchyExtractPVO
  - browsingcategoryhierarchyextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BrowsingCategoryHierarchyExtractPVO

## 📌 Visão Geral

Extrai a hierarquia de categorias de navegação do catálogo de compras, com níveis e relacionamentos pai-filho. Fundamental para organização do catálogo de procurement e análise de gastos por categoria.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PorBiccExtractAM.BrowsingCategoryHierarchyExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 2 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[por_item_cat_parent_levels|POR_ITEM_CAT_PARENT_LEVELS]] — 22 atributos (2 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[por_item_cat_parent_levels|POR_ITEM_CAT_PARENT_LEVELS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 4 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | Level10CatId | LEVEL10_CAT_ID | — | ✅ |
| 9 | Level1CatId | LEVEL1_CAT_ID | — | ✅ |
| 10 | Level2CatId | LEVEL2_CAT_ID | — | ✅ |
| 11 | Level3CatId | LEVEL3_CAT_ID | — | ✅ |
| 12 | Level4CatId | LEVEL4_CAT_ID | — | ✅ |
| 13 | Level5CatId | LEVEL5_CAT_ID | — | ✅ |
| 14 | Level6CatId | LEVEL6_CAT_ID | — | ✅ |
| 15 | Level7CatId | LEVEL7_CAT_ID | — | ✅ |
| 16 | Level8CatId | LEVEL8_CAT_ID | — | ✅ |
| 17 | Level9CatId | LEVEL9_CAT_ID | — | ✅ |
| 18 | NodeLevel | NODE_LEVEL | — | ✅ |
| 19 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 20 | PurchasingCatId | PURCHASING_CAT_ID | 🔑 | ✅ |
| 21 | RequestId | REQUEST_ID | — | ✅ |
| 22 | Type | TYPE | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
