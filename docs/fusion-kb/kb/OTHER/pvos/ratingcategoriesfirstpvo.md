---
id: DOC-OTHER-PVO-RatingCategoriesFirstPVO
doc_type: system-doc
title: "RatingCategoriesFirstPVO — PVO Cross-Module"
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
  - RatingCategoriesFirstPVO
  - ratingcategoriesfirstpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RatingCategoriesFirstPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Rating Categories First. Acessa as tabelas: HRT_RATING_CATEGORIES_B, HRT_RATING_CATEGORIES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileContentLibraryAM.RatingCategoriesFirstPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 2 | 2 | 8 | 42% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_rating_categories_b|HRT_RATING_CATEGORIES_B]] — 12 atributos (2 PKs, 5 BICC)
- [[hrt_rating_categories_tl|HRT_RATING_CATEGORIES_TL]] — 7 atributos (3 BICC)

---

## ⚙️ Atributos

### [[hrt_rating_categories_b|HRT_RATING_CATEGORIES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | RatingCategoriesBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 8 | RatingCategoriesBPEOCategoryId | CATEGORY_ID | 🔑 | ✅ |
| 9 | RatingCategoriesBPEOLowerBoundary | LOWER_BOUNDARY | — | ✅ |
| 10 | RatingCategoriesBPEOModuleId | MODULE_ID | — | — |
| 11 | RatingCategoriesBPEORatingModelId | RATING_MODEL_ID | — | — |
| 12 | RatingCategoriesBPEOUpperBoundary | UPPER_BOUNDARY | — | ✅ |

### [[hrt_rating_categories_tl|HRT_RATING_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RatingCategoriesTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | RatingCategoriesTranslationPEOCategoryDescription | CATEGORY_DESCRIPTION | — | ✅ |
| 3 | RatingCategoriesTranslationPEOCategoryId | CATEGORY_ID | — | — |
| 4 | RatingCategoriesTranslationPEOCategoryName | CATEGORY_NAME | — | ✅ |
| 5 | RatingCategoriesTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | RatingCategoriesTranslationPLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | SourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
