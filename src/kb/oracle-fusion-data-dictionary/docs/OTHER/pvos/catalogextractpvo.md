---
id: DOC-OTHER-PVO-CatalogExtractPVO
doc_type: system-doc
title: "CatalogExtractPVO — PVO Cross-Module"
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
  - CatalogExtractPVO
  - catalogextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CatalogExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Catalog Extract. Acessa as tabelas: EGP_CATEGORY_SETS_B, EGP_CATEGORY_SETS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgpBiccExtractAM.CatalogExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 58 | 2 | 1 | 54 | 93% |

---

## 🔗 Tabelas Relacionadas

- [[egp_category_sets_b|EGP_CATEGORY_SETS_B]] — 54 atributos (1 PKs, 54 BICC)
- [[egp_category_sets_tl|EGP_CATEGORY_SETS_TL]] — 4 atributos

---

## ⚙️ Atributos

### [[egp_category_sets_b|EGP_CATEGORY_SETS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CatalogBasePEOAttribute1 | ATTRIBUTE1 | — | ✅ |
| 2 | CatalogBasePEOAttribute10 | ATTRIBUTE10 | — | ✅ |
| 3 | CatalogBasePEOAttribute11 | ATTRIBUTE11 | — | ✅ |
| 4 | CatalogBasePEOAttribute12 | ATTRIBUTE12 | — | ✅ |
| 5 | CatalogBasePEOAttribute13 | ATTRIBUTE13 | — | ✅ |
| 6 | CatalogBasePEOAttribute14 | ATTRIBUTE14 | — | ✅ |
| 7 | CatalogBasePEOAttribute15 | ATTRIBUTE15 | — | ✅ |
| 8 | CatalogBasePEOAttribute2 | ATTRIBUTE2 | — | ✅ |
| 9 | CatalogBasePEOAttribute3 | ATTRIBUTE3 | — | ✅ |
| 10 | CatalogBasePEOAttribute4 | ATTRIBUTE4 | — | ✅ |
| 11 | CatalogBasePEOAttribute5 | ATTRIBUTE5 | — | ✅ |
| 12 | CatalogBasePEOAttribute6 | ATTRIBUTE6 | — | ✅ |
| 13 | CatalogBasePEOAttribute7 | ATTRIBUTE7 | — | ✅ |
| 14 | CatalogBasePEOAttribute8 | ATTRIBUTE8 | — | ✅ |
| 15 | CatalogBasePEOAttribute9 | ATTRIBUTE9 | — | ✅ |
| 16 | CatalogBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 17 | CatalogBasePEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 18 | CatalogBasePEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 19 | CatalogBasePEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 20 | CatalogBasePEOAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 21 | CatalogBasePEOAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 22 | CatalogBasePEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 23 | CatalogBasePEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 24 | CatalogBasePEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 25 | CatalogBasePEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 26 | CatalogBasePEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 27 | CatalogBasePEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 28 | CatalogBasePEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 29 | CatalogBasePEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 30 | CatalogBasePEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 31 | CatalogBasePEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 32 | CatalogBasePEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 33 | CatalogBasePEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 34 | CatalogBasePEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 35 | CatalogBasePEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 36 | CatalogBasePEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 37 | CatalogBasePEOCatalogCode | CATALOG_CODE | — | ✅ |
| 38 | CatalogBasePEOCatalogContentCode | CATALOG_CONTENT_CODE | — | ✅ |
| 39 | CatalogBasePEOCategorySetId | CATEGORY_SET_ID | 🔑 | ✅ |
| 40 | CatalogBasePEOControlLevel | CONTROL_LEVEL | — | ✅ |
| 41 | CatalogBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 42 | CatalogBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 43 | CatalogBasePEODefaultCategoryId | DEFAULT_CATEGORY_ID | — | ✅ |
| 44 | CatalogBasePEOEndDate | END_DATE | — | ✅ |
| 45 | CatalogBasePEOHierarchyEnabled | HIERARCHY_ENABLED | — | ✅ |
| 46 | CatalogBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 47 | CatalogBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 48 | CatalogBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 49 | CatalogBasePEOMultItemCatAssignFlag | MULT_ITEM_CAT_ASSIGN_FLAG | — | ✅ |
| 50 | CatalogBasePEOPublicCatalogFlag | PUBLIC_CATALOG | — | ✅ |
| 51 | CatalogBasePEORaiseAltCatHierChgEvent | RAISE_ALT_CAT_HIER_CHG_EVENT | — | ✅ |
| 52 | CatalogBasePEORaiseCatalogCatChgEvent | RAISE_CATALOG_CAT_CHG_EVENT | — | ✅ |
| 53 | CatalogBasePEORaiseItemCatAssignEvent | RAISE_ITEM_CAT_ASSIGN_EVENT | — | ✅ |
| 54 | CatalogBasePEOStartDate | START_DATE | — | ✅ |

### [[egp_category_sets_tl|EGP_CATEGORY_SETS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CatalogTranslationPEOCategorySetId | CATEGORY_SET_ID | — | — |
| 2 | CatalogTranslationPEOCategorySetName | CATEGORY_SET_NAME | — | — |
| 3 | CatalogTranslationPEODescription | DESCRIPTION | — | — |
| 4 | CatalogTranslationPEOLanguage | LANGUAGE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
