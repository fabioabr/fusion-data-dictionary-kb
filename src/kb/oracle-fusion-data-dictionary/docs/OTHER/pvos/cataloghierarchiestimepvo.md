---
id: DOC-OTHER-PVO-CatalogHierarchiesTimePVO
doc_type: system-doc
title: "CatalogHierarchiesTimePVO — PVO Cross-Module"
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
  - CatalogHierarchiesTimePVO
  - cataloghierarchiestimepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CatalogHierarchiesTimePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Catalog Hierarchies Time. Acessa as tabelas: MSC_CATALOG_HIERARCHIES.

**Caminho:** `FscmTopModelAM.MscAnalyticsTopAM.CatalogHierarchiesTimePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 3 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[msc_catalog_hierarchies|MSC_CATALOG_HIERARCHIES]] — 11 atributos (3 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[msc_catalog_hierarchies|MSC_CATALOG_HIERARCHIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CatalogHierarchyEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | CatalogHierarchyEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | CatalogHierarchyEODimensionId | DIMENSION_ID | — | ✅ |
| 4 | CatalogHierarchyEOIsDefault | IS_DEFAULT | — | ✅ |
| 5 | CatalogHierarchyEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | CatalogHierarchyEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | CatalogHierarchyEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | CatalogHierarchyEOPriority | PRIORITY | — | ✅ |
| 9 | CatalogId | CATALOG_ID | 🔑 | ✅ |
| 10 | HierarchyId | HIERARCHY_ID | 🔑 | ✅ |
| 11 | IsAttribute | IS_ATTRIBUTE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
