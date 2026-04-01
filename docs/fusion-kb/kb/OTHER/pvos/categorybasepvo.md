---
id: DOC-OTHER-PVO-CategoryBasePVO
doc_type: system-doc
title: "CategoryBasePVO — PVO Cross-Module"
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
  - CategoryBasePVO
  - categorybasepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CategoryBasePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Category Base. Acessa as tabelas: FA_CATEGORIES_B, FA_CATEGORIES_TL.

**Caminho:** `FscmTopModelAM.FinFaDeprnSetupCategoriesAM.CategoryBasePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 46 | 2 | 2 | 19 | 41% |

---

## 🔗 Tabelas Relacionadas

- [[fa_categories_b|FA_CATEGORIES_B]] — 26 atributos (1 PKs, 11 BICC)
- [[fa_categories_tl|FA_CATEGORIES_TL]] — 20 atributos (1 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[fa_categories_b|FA_CATEGORIES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryCapitalizeFlag | CAPITALIZE_FLAG | — | ✅ |
| 2 | CategoryCategoryType | CATEGORY_TYPE | — | ✅ |
| 3 | CategoryCreatedBy | CREATED_BY | — | ✅ |
| 4 | CategoryCreationDate | CREATION_DATE | — | ✅ |
| 5 | CategoryDateIneffective | DATE_INEFFECTIVE | — | — |
| 6 | CategoryEnabledFlag | ENABLED_FLAG | — | ✅ |
| 7 | CategoryEndDateActive | END_DATE_ACTIVE | — | — |
| 8 | CategoryId | CATEGORY_ID | 🔑 | ✅ |
| 9 | CategoryInventorial | INVENTORIAL | — | — |
| 10 | CategoryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | CategoryLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | CategoryLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | CategoryObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | CategoryOwnedLeased | OWNED_LEASED | — | ✅ |
| 15 | CategoryProperty12451250Code | PROPERTY_1245_1250_CODE | — | ✅ |
| 16 | CategoryPropertyTypeCode | PROPERTY_TYPE_CODE | — | ✅ |
| 17 | CategoryStartDateActive | START_DATE_ACTIVE | — | — |
| 18 | CategoryStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 19 | CategorySummaryFlag | SUMMARY_FLAG | — | — |
| 20 | Segment1 | SEGMENT1 | — | — |
| 21 | Segment2 | SEGMENT2 | — | — |
| 22 | Segment3 | SEGMENT3 | — | — |
| 23 | Segment4 | SEGMENT4 | — | — |
| 24 | Segment5 | SEGMENT5 | — | — |
| 25 | Segment6 | SEGMENT6 | — | — |
| 26 | Segment7 | SEGMENT7 | — | — |

### [[fa_categories_tl|FA_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryLangTLCategoryId | CATEGORY_ID | — | — |
| 2 | CategoryLangTLCreatedBy | CREATED_BY | — | — |
| 3 | CategoryLangTLCreationDate | CREATION_DATE | — | — |
| 4 | CategoryLangTLDescription | DESCRIPTION | — | — |
| 5 | CategoryLangTLLanguage | LANGUAGE | — | — |
| 6 | CategoryLangTLLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | CategoryLangTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | CategoryLangTLLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | CategoryLangTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | CategoryLangTLSourceLang | SOURCE_LANG | — | — |
| 11 | CategoryTLCategoryId | CATEGORY_ID | — | ✅ |
| 12 | CategoryTLCreatedBy | CREATED_BY | — | ✅ |
| 13 | CategoryTLCreationDate | CREATION_DATE | — | ✅ |
| 14 | CategoryTLDescription | DESCRIPTION | — | ✅ |
| 15 | CategoryTLLanguage | LANGUAGE | 🔑 | ✅ |
| 16 | CategoryTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | CategoryTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | CategoryTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | CategoryTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | CategoryTLSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
