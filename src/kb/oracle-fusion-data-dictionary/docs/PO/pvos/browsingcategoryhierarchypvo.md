---
id: DOC-PO-PVO-BrowsingCategoryHierarchyPVO
doc_type: system-doc
title: "BrowsingCategoryHierarchyPVO — PVO Purchasing"
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
  - BrowsingCategoryHierarchyPVO
  - browsingcategoryhierarchypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BrowsingCategoryHierarchyPVO

## 📌 Visão Geral

Disponibiliza a hierarquia de categorias de navegação para consulta operacional, incluindo traduções e mapeamento de categorias de item. Suporta a experiência do usuário na busca e classificação de compras.

**Caminho:** `FscmTopModelAM.PrcPorPublicViewAM.BrowsingCategoryHierarchyPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 146 | 3 | 2 | 47 | 32% |

---

## 🔗 Tabelas Relacionadas

- [[egp_categories_tl|EGP_CATEGORIES_TL]] — 14 atributos (3 BICC)
- [[por_browse_categories_tl|POR_BROWSE_CATEGORIES_TL]] — 110 atributos (30 BICC)
- [[por_item_cat_parent_levels|POR_ITEM_CAT_PARENT_LEVELS]] — 22 atributos (2 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[egp_categories_tl|EGP_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy11 | CREATED_BY | — | — |
| 2 | CreationDate11 | CREATION_DATE | — | — |
| 3 | JobDefinitionName11 | $none$ | — | — |
| 4 | JobDefinitionPackage11 | $none$ | — | — |
| 5 | Language | LANGUAGE | — | — |
| 6 | LastUpdateDate11 | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin11 | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy11 | LAST_UPDATED_BY | — | — |
| 9 | ObjectVersionNumber11 | OBJECT_VERSION_NUMBER | — | — |
| 10 | PurchasingCategoryId | CATEGORY_ID | — | — |
| 11 | PurchasingCategoryName | CATEGORY_NAME | — | ✅ |
| 12 | PurchasingDescription | DESCRIPTION | — | ✅ |
| 13 | RequestId11 | $none$ | — | — |
| 14 | SourceLang | SOURCE_LANG | — | — |

### [[por_browse_categories_tl|POR_BROWSE_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy1 | CREATED_BY | — | — |
| 2 | CreatedBy10 | CREATED_BY | — | — |
| 3 | CreatedBy2 | CREATED_BY | — | — |
| 4 | CreatedBy3 | CREATED_BY | — | — |
| 5 | CreatedBy4 | CREATED_BY | — | — |
| 6 | CreatedBy5 | CREATED_BY | — | — |
| 7 | CreatedBy6 | CREATED_BY | — | — |
| 8 | CreatedBy7 | CREATED_BY | — | — |
| 9 | CreatedBy8 | CREATED_BY | — | — |
| 10 | CreatedBy9 | CREATED_BY | — | — |
| 11 | CreationDate1 | CREATION_DATE | — | — |
| 12 | CreationDate10 | CREATION_DATE | — | — |
| 13 | CreationDate2 | CREATION_DATE | — | — |
| 14 | CreationDate3 | CREATION_DATE | — | — |
| 15 | CreationDate4 | CREATION_DATE | — | — |
| 16 | CreationDate5 | CREATION_DATE | — | — |
| 17 | CreationDate6 | CREATION_DATE | — | — |
| 18 | CreationDate7 | CREATION_DATE | — | — |
| 19 | CreationDate8 | CREATION_DATE | — | — |
| 20 | CreationDate9 | CREATION_DATE | — | — |
| 21 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 22 | LastUpdateDate10 | LAST_UPDATE_DATE | — | ✅ |
| 23 | LastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 24 | LastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 25 | LastUpdateDate4 | LAST_UPDATE_DATE | — | ✅ |
| 26 | LastUpdateDate5 | LAST_UPDATE_DATE | — | ✅ |
| 27 | LastUpdateDate6 | LAST_UPDATE_DATE | — | ✅ |
| 28 | LastUpdateDate7 | LAST_UPDATE_DATE | — | ✅ |
| 29 | LastUpdateDate8 | LAST_UPDATE_DATE | — | ✅ |
| 30 | LastUpdateDate9 | LAST_UPDATE_DATE | — | ✅ |
| 31 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 32 | LastUpdateLogin10 | LAST_UPDATE_LOGIN | — | — |
| 33 | LastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 34 | LastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 35 | LastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 36 | LastUpdateLogin5 | LAST_UPDATE_LOGIN | — | — |
| 37 | LastUpdateLogin6 | LAST_UPDATE_LOGIN | — | — |
| 38 | LastUpdateLogin7 | LAST_UPDATE_LOGIN | — | — |
| 39 | LastUpdateLogin8 | LAST_UPDATE_LOGIN | — | — |
| 40 | LastUpdateLogin9 | LAST_UPDATE_LOGIN | — | — |
| 41 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 42 | LastUpdatedBy10 | LAST_UPDATED_BY | — | — |
| 43 | LastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 44 | LastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 45 | LastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 46 | LastUpdatedBy5 | LAST_UPDATED_BY | — | — |
| 47 | LastUpdatedBy6 | LAST_UPDATED_BY | — | — |
| 48 | LastUpdatedBy7 | LAST_UPDATED_BY | — | — |
| 49 | LastUpdatedBy8 | LAST_UPDATED_BY | — | — |
| 50 | LastUpdatedBy9 | LAST_UPDATED_BY | — | — |
| 51 | Level10CategoryDescription | CATEGORY_DESCRIPTION | — | ✅ |
| 52 | Level10CategoryId | CATEGORY_ID | — | — |
| 53 | Level10CategoryName | CATEGORY_NAME | — | ✅ |
| 54 | Level10Language | LANGUAGE | — | — |
| 55 | Level10SourceLang | SOURCE_LANG | — | — |
| 56 | Level1CategoryDescription | CATEGORY_DESCRIPTION | — | ✅ |
| 57 | Level1CategoryId | CATEGORY_ID | — | — |
| 58 | Level1CategoryName | CATEGORY_NAME | — | ✅ |
| 59 | Level1Language | LANGUAGE | — | — |
| 60 | Level1SourceLang | SOURCE_LANG | — | — |
| 61 | Level2CategoryDescription | CATEGORY_DESCRIPTION | — | ✅ |
| 62 | Level2CategoryId | CATEGORY_ID | — | — |
| 63 | Level2CategoryName | CATEGORY_NAME | — | ✅ |
| 64 | Level2Language | LANGUAGE | — | — |
| 65 | Level2SourceLang | SOURCE_LANG | — | — |
| 66 | Level3CategoryDescription | CATEGORY_DESCRIPTION | — | ✅ |
| 67 | Level3CategoryId | CATEGORY_ID | — | — |
| 68 | Level3CategoryName | CATEGORY_NAME | — | ✅ |
| 69 | Level3Language | LANGUAGE | — | — |
| 70 | Level3SourceLang | SOURCE_LANG | — | — |
| 71 | Level4CategoryDescription | CATEGORY_DESCRIPTION | — | ✅ |
| 72 | Level4CategoryId | CATEGORY_ID | — | — |
| 73 | Level4CategoryName | CATEGORY_NAME | — | ✅ |
| 74 | Level4Language | LANGUAGE | — | — |
| 75 | Level4SourceLang | SOURCE_LANG | — | — |
| 76 | Level5CategoryDescription | CATEGORY_DESCRIPTION | — | ✅ |
| 77 | Level5CategoryId | CATEGORY_ID | — | — |
| 78 | Level5CategoryName | CATEGORY_NAME | — | ✅ |
| 79 | Level5Language | LANGUAGE | — | — |
| 80 | Level5SourceLang | SOURCE_LANG | — | — |
| 81 | Level6CategoryDescription | CATEGORY_DESCRIPTION | — | ✅ |
| 82 | Level6CategoryId | CATEGORY_ID | — | — |
| 83 | Level6CategoryName | CATEGORY_NAME | — | ✅ |
| 84 | Level6Language | LANGUAGE | — | — |
| 85 | Level6SourceLang | SOURCE_LANG | — | — |
| 86 | Level7CategoryDescription | CATEGORY_DESCRIPTION | — | ✅ |
| 87 | Level7CategoryId | CATEGORY_ID | — | — |
| 88 | Level7CategoryName | CATEGORY_NAME | — | ✅ |
| 89 | Level7Language | LANGUAGE | — | — |
| 90 | Level7SourceLang | SOURCE_LANG | — | — |
| 91 | Level8CategoryDescription | CATEGORY_DESCRIPTION | — | ✅ |
| 92 | Level8CategoryId | CATEGORY_ID | — | — |
| 93 | Level8CategoryName | CATEGORY_NAME | — | ✅ |
| 94 | Level8Language | LANGUAGE | — | — |
| 95 | Level8SourceLang | SOURCE_LANG | — | — |
| 96 | Level9CategoryDescription | CATEGORY_DESCRIPTION | — | ✅ |
| 97 | Level9CategoryId | CATEGORY_ID | — | — |
| 98 | Level9CategoryName | CATEGORY_NAME | — | ✅ |
| 99 | Level9Language | LANGUAGE | — | — |
| 100 | Level9SourceLang | SOURCE_LANG | — | — |
| 101 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 102 | ObjectVersionNumber10 | OBJECT_VERSION_NUMBER | — | — |
| 103 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 104 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 105 | ObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 106 | ObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 107 | ObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 108 | ObjectVersionNumber7 | OBJECT_VERSION_NUMBER | — | — |
| 109 | ObjectVersionNumber8 | OBJECT_VERSION_NUMBER | — | — |
| 110 | ObjectVersionNumber9 | OBJECT_VERSION_NUMBER | — | — |

### [[por_item_cat_parent_levels|POR_ITEM_CAT_PARENT_LEVELS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 4 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
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
| 19 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | PurchasingCatId | PURCHASING_CAT_ID | 🔑 | ✅ |
| 21 | RequestId | REQUEST_ID | — | — |
| 22 | Type | TYPE | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
