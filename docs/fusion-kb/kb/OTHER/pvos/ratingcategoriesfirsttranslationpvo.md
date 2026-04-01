---
id: DOC-OTHER-PVO-RatingCategoriesFirstTranslationPVO
doc_type: system-doc
title: "RatingCategoriesFirstTranslationPVO — PVO Cross-Module"
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
  - RatingCategoriesFirstTranslationPVO
  - ratingcategoriesfirsttranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RatingCategoriesFirstTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Rating Categories First Translation. Acessa as tabelas: HRT_RATING_CATEGORIES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.HcmProfileContentLibraryAM.RatingCategoriesFirstTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 3 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_rating_categories_tl|HRT_RATING_CATEGORIES_TL]] — 12 atributos (3 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[hrt_rating_categories_tl|HRT_RATING_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | CategoryDescription | CATEGORY_DESCRIPTION | — | ✅ |
| 3 | CategoryId | CATEGORY_ID | 🔑 | ✅ |
| 4 | CategoryName | CATEGORY_NAME | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | Language | LANGUAGE | 🔑 | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
