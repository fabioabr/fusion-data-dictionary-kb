---
id: DOC-OTHER-PVO-FunctionalAreaCatalogsExtractPVO
doc_type: system-doc
title: "FunctionalAreaCatalogsExtractPVO — PVO Cross-Module"
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
  - FunctionalAreaCatalogsExtractPVO
  - functionalareacatalogsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FunctionalAreaCatalogsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Functional Area Catalogs Extract. Acessa as tabelas: EGP_DEFAULT_CATEGORY_SETS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgpBiccExtractAM.FunctionalAreaCatalogsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 7 | 1 | 1 | 7 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[egp_default_category_sets|EGP_DEFAULT_CATEGORY_SETS]] — 7 atributos (1 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[egp_default_category_sets|EGP_DEFAULT_CATEGORY_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FunctionalAreaCatalogPEOCategorySetId | CATEGORY_SET_ID | — | ✅ |
| 2 | FunctionalAreaCatalogPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | FunctionalAreaCatalogPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | FunctionalAreaCatalogPEOFunctionalAreaId | FUNCTIONAL_AREA_ID | 🔑 | ✅ |
| 5 | FunctionalAreaCatalogPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | FunctionalAreaCatalogPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | FunctionalAreaCatalogPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
