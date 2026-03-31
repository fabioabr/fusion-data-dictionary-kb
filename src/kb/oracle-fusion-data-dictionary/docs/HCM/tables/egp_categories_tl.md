---
id: DOC-HCM-097
doc_type: system-doc
title: "EGP_CATEGORIES_TL — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - EGP_CATEGORIES_TL
  - egp_categories_tl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# EGP_CATEGORIES_TL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | $none$ | — | — | — | — | — | — |
| 2 | CATEGORY_ID | — | — | — | — | — | — |
| 3 | CATEGORY_NAME | — | — | — | — | — | — |
| 4 | CREATED_BY | — | — | — | — | — | — |
| 5 | CREATION_DATE | — | — | — | — | — | — |
| 6 | DESCRIPTION | — | — | — | — | — | — |
| 7 | LANGUAGE | — | — | — | — | — | — |
| 8 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 9 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 10 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 11 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 12 | SOURCE_LANG | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[browsingcategoryhierarchypvo|BrowsingCategoryHierarchyPVO]] (PO · BICC: 3/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| $none$ | JobDefinitionName11 | — |
| $none$ | JobDefinitionPackage11 | — |
| $none$ | RequestId11 | — |
| CATEGORY_ID | PurchasingCategoryId | — |
| CATEGORY_NAME | PurchasingCategoryName | ✅ |
| CREATED_BY | CreatedBy11 | — |
| CREATION_DATE | CreationDate11 | — |
| DESCRIPTION | PurchasingDescription | ✅ |
| LANGUAGE | Language | — |
| LAST_UPDATE_DATE | LastUpdateDate11 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin11 | — |
| LAST_UPDATED_BY | LastUpdatedBy11 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber11 | — |
| SOURCE_LANG | SourceLang | — |

### [[catalogcategoryassignp1|CatalogCategoryAssignP1]] (OTHER · BICC: 9/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | CategoryTranslationPEOCategoryId | ✅ |
| CATEGORY_NAME | CategoryTranslationPEOCategoryName | ✅ |
| CREATED_BY | CategoryTranslationPEOCreatedBy | ✅ |
| CREATION_DATE | CategoryTranslationPEOCreationDate | ✅ |
| DESCRIPTION | CategoryTranslationPEODescription | ✅ |
| LANGUAGE | CategoryTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | CategoryTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CategoryTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CategoryTranslationPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | CategoryTranslationPEOObjectVersionNumber | — |
| SOURCE_LANG | CategoryTranslationPEOSourceLang | ✅ |

### [[categoryassignmentp1|CategoryAssignmentP1]] (OTHER · BICC: 4/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | CategoryTranslationPEOCategoryId | — |
| CATEGORY_NAME | CategoryTranslationPEOCategoryName | ✅ |
| CREATED_BY | CategoryTranslationPEOCreatedBy | — |
| CREATION_DATE | CategoryTranslationPEOCreationDate | — |
| DESCRIPTION | CategoryTranslationPEODescription | ✅ |
| LANGUAGE | CategoryTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | CategoryTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CategoryTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CategoryTranslationPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | CategoryTranslationPEOObjectVersionNumber | — |
| SOURCE_LANG | CategoryTranslationPEOSourceLang | — |

### [[categoryextractpvo|CategoryExtractPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | CategoryTranslationPEOCategoryId | — |
| CATEGORY_NAME | CategoryTranslationPEOCategoryName | — |
| DESCRIPTION | CategoryTranslationPEODescription | — |
| LANGUAGE | CategoryTranslationPEOLanguage | — |

### [[categoryp1|CategoryP1]] (OTHER · BICC: 3/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | CategoryTranslationPEOCategoryId | — |
| CATEGORY_NAME | CategoryTranslationPEOCategoryName | ✅ |
| CREATED_BY | CategoryTranslationPEOCreatedBy | — |
| CREATION_DATE | CategoryTranslationPEOCreationDate | — |
| DESCRIPTION | CategoryTranslationPEODescription | ✅ |
| LANGUAGE | CategoryTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | CategoryTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CategoryTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CategoryTranslationPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | CategoryTranslationPEOObjectVersionNumber | — |
| SOURCE_LANG | CategoryTranslationPEOSourceLang | — |

### [[categorytlpvo|CategoryTLPVO]] (OTHER · BICC: 5/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | CategoryId | ✅ |
| CATEGORY_NAME | CategoryName | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DESCRIPTION | Description | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| SOURCE_LANG | SourceLang | — |

### [[categorytranslationextractpvo|CategoryTranslationExtractPVO]] (OTHER · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | CategoryTranslationPEOCategoryId | ✅ |
| CATEGORY_NAME | CategoryTranslationPEOCategoryName | ✅ |
| CREATED_BY | CategoryTranslationPEOCreatedBy | ✅ |
| CREATION_DATE | CategoryTranslationPEOCreationDate | ✅ |
| DESCRIPTION | CategoryTranslationPEODescription | ✅ |
| LANGUAGE | CategoryTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | CategoryTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CategoryTranslationPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | CategoryTranslationPEOLastUpdatedBy | ✅ |
| SOURCE_LANG | CategoryTranslationPEOSourceLang | ✅ |

### [[contractfulfillment|ContractFulfillment]] (OTHER · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | ContractLineCategoryTLPEOCategoryId | — |
| CATEGORY_NAME | ContractLineCategoryTLPEOCategoryName | ✅ |
| CREATED_BY | ContractLineCategoryTLPEOCreatedBy | — |
| CREATION_DATE | ContractLineCategoryTLPEOCreationDate | — |
| DESCRIPTION | ContractLineCategoryTLPEODescription | — |
| LANGUAGE | ContractLineCategoryTLPEOLanguage | — |
| LAST_UPDATE_DATE | ContractLineCategoryTLPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ContractLineCategoryTLPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ContractLineCategoryTLPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ContractLineCategoryTLPEOObjectVersionNumber | — |
| SOURCE_LANG | ContractLineCategoryTLPEOSourceLang | — |

### [[contractheaderlinesall|ContractHeaderLinesAll]] (OTHER · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | ContractLineCategoryTLPEOCategoryId | — |
| CATEGORY_NAME | ContractLineCategoryTLPEOCategoryName | ✅ |
| CREATED_BY | ContractLineCategoryTLPEOCreatedBy | — |
| CREATION_DATE | ContractLineCategoryTLPEOCreationDate | — |
| DESCRIPTION | ContractLineCategoryTLPEODescription | — |
| LANGUAGE | ContractLineCategoryTLPEOLanguage | — |
| LAST_UPDATE_DATE | ContractLineCategoryTLPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ContractLineCategoryTLPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ContractLineCategoryTLPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ContractLineCategoryTLPEOObjectVersionNumber | — |
| SOURCE_LANG | ContractLineCategoryTLPEOSourceLang | — |

### [[contractheaderlinesallunsec|ContractHeaderLinesAllUnsec]] (OTHER · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | ContractLineCategoryTLPEOCategoryId | — |
| CATEGORY_NAME | ContractLineCategoryTLPEOCategoryName | — |
| CREATED_BY | ContractLineCategoryTLPEOCreatedBy | — |
| CREATION_DATE | ContractLineCategoryTLPEOCreationDate | — |
| DESCRIPTION | ContractLineCategoryTLPEODescription | — |
| LANGUAGE | ContractLineCategoryTLPEOLanguage | — |
| LAST_UPDATE_DATE | ContractLineCategoryTLPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ContractLineCategoryTLPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ContractLineCategoryTLPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ContractLineCategoryTLPEOObjectVersionNumber | — |
| SOURCE_LANG | ContractLineCategoryTLPEOSourceLang | — |

### [[contractheaderlinesp|ContractHeaderLinesP]] (OTHER · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | ContractLineCategoryTLPEOCategoryId | — |
| CATEGORY_NAME | ContractLineCategoryTLPEOCategoryName | — |
| CREATED_BY | ContractLineCategoryTLPEOCreatedBy | — |
| CREATION_DATE | ContractLineCategoryTLPEOCreationDate | — |
| DESCRIPTION | ContractLineCategoryTLPEODescription | — |
| LANGUAGE | ContractLineCategoryTLPEOLanguage | — |
| LAST_UPDATE_DATE | ContractLineCategoryTLPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ContractLineCategoryTLPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ContractLineCategoryTLPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ContractLineCategoryTLPEOObjectVersionNumber | — |
| SOURCE_LANG | ContractLineCategoryTLPEOSourceLang | — |

### [[contractheaderlinesrefp|ContractHeaderLinesRefP]] (OTHER · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | ContractLineCategoryTLPEOCategoryId | — |
| CATEGORY_NAME | ContractLineCategoryTLPEOCategoryName | — |
| CREATED_BY | ContractLineCategoryTLPEOCreatedBy | — |
| CREATION_DATE | ContractLineCategoryTLPEOCreationDate | — |
| DESCRIPTION | ContractLineCategoryTLPEODescription | — |
| LANGUAGE | ContractLineCategoryTLPEOLanguage | — |
| LAST_UPDATE_DATE | ContractLineCategoryTLPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ContractLineCategoryTLPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ContractLineCategoryTLPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ContractLineCategoryTLPEOObjectVersionNumber | — |
| SOURCE_LANG | ContractLineCategoryTLPEOSourceLang | — |

### [[itemcategory|ItemCategory]] (OTHER · BICC: 4/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | CategoryTranslationPEOCategoryId | — |
| CATEGORY_NAME | CategoryTranslationPEOCategoryName | ✅ |
| CREATED_BY | CategoryTranslationPEOCreatedBy | — |
| CREATION_DATE | CategoryTranslationPEOCreationDate | — |
| DESCRIPTION | CategoryTranslationPEODescription | ✅ |
| LANGUAGE | CategoryTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | CategoryTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CategoryTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CategoryTranslationPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | CategoryTranslationPEOObjectVersionNumber | — |
| SOURCE_LANG | CategoryTranslationPEOSourceLang | — |
