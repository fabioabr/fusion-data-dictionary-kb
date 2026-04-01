---
id: DOC-OTHER-PVO-ItemCategory
doc_type: system-doc
title: "ItemCategory — PVO Cross-Module"
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
  - ItemCategory
  - itemcategory
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemCategory

## 📌 Visão Geral

View Object para extração BICC de dados de Item Category. Acessa as tabelas: EGP_CATEGORIES_B, EGP_CATEGORIES_TL, EGP_CATEGORY_SETS_B (+3).

**Caminho:** `FscmTopModelAM.EgpItemsPublicModelAM.ItemCategory`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 134 | 6 | 4 | 58 | 43% |

---

## 🔗 Tabelas Relacionadas

- [[egp_categories_b|EGP_CATEGORIES_B]] — 46 atributos (25 BICC)
- [[egp_categories_tl|EGP_CATEGORIES_TL]] — 11 atributos (4 BICC)
- [[egp_category_sets_b|EGP_CATEGORY_SETS_B]] — 34 atributos (15 BICC)
- [[egp_category_sets_tl|EGP_CATEGORY_SETS_TL]] — 11 atributos (4 BICC)
- [[egp_category_set_valid_cats|EGP_CATEGORY_SET_VALID_CATS]] — 17 atributos (2 BICC)
- [[egp_item_categories|EGP_ITEM_CATEGORIES]] — 15 atributos (4 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[egp_categories_b|EGP_CATEGORIES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryBasePEOCategoryCode | CATEGORY_CODE | — | ✅ |
| 2 | CategoryBasePEOCategoryContentCode | CATEGORY_CONTENT_CODE | — | ✅ |
| 3 | CategoryBasePEOCategoryId | CATEGORY_ID | — | — |
| 4 | CategoryBasePEOCreatedBy | CREATED_BY | — | — |
| 5 | CategoryBasePEOCreationDate | CREATION_DATE | — | — |
| 6 | CategoryBasePEODescription | DESCRIPTION | — | — |
| 7 | CategoryBasePEODisableDate | DISABLE_DATE | — | — |
| 8 | CategoryBasePEOEnabledFlag | ENABLED_FLAG | — | — |
| 9 | CategoryBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 10 | CategoryBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 11 | CategoryBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 12 | CategoryBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | CategoryBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | CategoryBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | CategoryBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | CategoryBasePEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 17 | CategoryBasePEOProgramName | PROGRAM_NAME | — | — |
| 18 | CategoryBasePEORequestId | REQUEST_ID | — | — |
| 19 | CategoryBasePEOSegment1 | SEGMENT1 | — | ✅ |
| 20 | CategoryBasePEOSegment10 | SEGMENT10 | — | ✅ |
| 21 | CategoryBasePEOSegment11 | SEGMENT11 | — | ✅ |
| 22 | CategoryBasePEOSegment12 | SEGMENT12 | — | ✅ |
| 23 | CategoryBasePEOSegment13 | SEGMENT13 | — | ✅ |
| 24 | CategoryBasePEOSegment14 | SEGMENT14 | — | ✅ |
| 25 | CategoryBasePEOSegment15 | SEGMENT15 | — | ✅ |
| 26 | CategoryBasePEOSegment16 | SEGMENT16 | — | ✅ |
| 27 | CategoryBasePEOSegment17 | SEGMENT17 | — | ✅ |
| 28 | CategoryBasePEOSegment18 | SEGMENT18 | — | ✅ |
| 29 | CategoryBasePEOSegment19 | SEGMENT19 | — | ✅ |
| 30 | CategoryBasePEOSegment2 | SEGMENT2 | — | ✅ |
| 31 | CategoryBasePEOSegment20 | SEGMENT20 | — | ✅ |
| 32 | CategoryBasePEOSegment3 | SEGMENT3 | — | ✅ |
| 33 | CategoryBasePEOSegment4 | SEGMENT4 | — | ✅ |
| 34 | CategoryBasePEOSegment5 | SEGMENT5 | — | ✅ |
| 35 | CategoryBasePEOSegment6 | SEGMENT6 | — | ✅ |
| 36 | CategoryBasePEOSegment7 | SEGMENT7 | — | ✅ |
| 37 | CategoryBasePEOSegment8 | SEGMENT8 | — | ✅ |
| 38 | CategoryBasePEOSegment9 | SEGMENT9 | — | ✅ |
| 39 | CategoryBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 40 | CategoryBasePEOStructureId | STRUCTURE_ID | — | — |
| 41 | CategoryBasePEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 42 | CategoryBasePEOSummaryFlag | SUMMARY_FLAG | — | — |
| 43 | CategoryBasePEOSupplierEnabledFlag | SUPPLIER_ENABLED_FLAG | — | — |
| 44 | CategoryBasePEOTotalProdId | TOTAL_PROD_ID | — | — |
| 45 | CategoryBasePEOWebStatus | WEB_STATUS | — | — |
| 46 | CategoryBasePEOWhUpdateDate | WH_UPDATE_DATE | — | — |

### [[egp_categories_tl|EGP_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryTranslationPEOCategoryId | CATEGORY_ID | — | — |
| 2 | CategoryTranslationPEOCategoryName | CATEGORY_NAME | — | ✅ |
| 3 | CategoryTranslationPEOCreatedBy | CREATED_BY | — | — |
| 4 | CategoryTranslationPEOCreationDate | CREATION_DATE | — | — |
| 5 | CategoryTranslationPEODescription | DESCRIPTION | — | ✅ |
| 6 | CategoryTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 7 | CategoryTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CategoryTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | CategoryTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | CategoryTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | CategoryTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[egp_category_sets_b|EGP_CATEGORY_SETS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CatalogBasePEOCatalogCode | CATALOG_CODE | — | ✅ |
| 2 | CatalogBasePEOCatalogContentCode | CATALOG_CONTENT_CODE | — | ✅ |
| 3 | CatalogBasePEOCategorySetId | CATEGORY_SET_ID | — | ✅ |
| 4 | CatalogBasePEOControlLevel | CONTROL_LEVEL | — | ✅ |
| 5 | CatalogBasePEOControlLevelUpdateableFlag | CONTROL_LEVEL_UPDATEABLE_FLAG | — | — |
| 6 | CatalogBasePEOCreatedBy | CREATED_BY | — | — |
| 7 | CatalogBasePEOCreationDate | CREATION_DATE | — | — |
| 8 | CatalogBasePEODefaultCategoryId | DEFAULT_CATEGORY_ID | — | ✅ |
| 9 | CatalogBasePEOEndDate | END_DATE | — | ✅ |
| 10 | CatalogBasePEOHierarchyEnabled | HIERARCHY_ENABLED | — | ✅ |
| 11 | CatalogBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 12 | CatalogBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 13 | CatalogBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | CatalogBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | CatalogBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | CatalogBasePEOMultItemCatAssignFlag | MULT_ITEM_CAT_ASSIGN_FLAG | — | ✅ |
| 17 | CatalogBasePEOMultItemCatUpdateableFlag | MULT_ITEM_CAT_UPDATEABLE_FLAG | — | — |
| 18 | CatalogBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | CatalogBasePEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 20 | CatalogBasePEOProgramName | PROGRAM_NAME | — | — |
| 21 | CatalogBasePEORaiseAltCatHierChgEvent | RAISE_ALT_CAT_HIER_CHG_EVENT | — | — |
| 22 | CatalogBasePEORaiseCatalogCatChgEvent | RAISE_CATALOG_CAT_CHG_EVENT | — | — |
| 23 | CatalogBasePEORaiseItemCatAssignEvent | RAISE_ITEM_CAT_ASSIGN_EVENT | — | — |
| 24 | CatalogBasePEORequestId | REQUEST_ID | — | — |
| 25 | CatalogBasePEOSequenceNumber | SEQUENCE_NUMBER | — | — |
| 26 | CatalogBasePEOSharingContentCode | SHARING_CONTENT_CODE | — | ✅ |
| 27 | CatalogBasePEOSharingControlCode | SHARING_CONTROL_CODE | — | — |
| 28 | CatalogBasePEOSourceCategorySetId | SOURCE_CATEGORY_SET_ID | — | ✅ |
| 29 | CatalogBasePEOStartDate | START_DATE | — | ✅ |
| 30 | CatalogBasePEOStatusFlag | STATUS_FLAG | — | ✅ |
| 31 | CatalogBasePEOStructureId | STRUCTURE_ID | — | ✅ |
| 32 | CatalogBasePEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 33 | CatalogBasePEOValidateFlag | VALIDATE_FLAG | — | ✅ |
| 34 | CatalogBasePEOValidateFlagUpdateableFlag | VALIDATE_FLAG_UPDATEABLE_FLAG | — | — |

### [[egp_category_sets_tl|EGP_CATEGORY_SETS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CatalogTranslationPEOCategorySetId | CATEGORY_SET_ID | — | — |
| 2 | CatalogTranslationPEOCategorySetName | CATEGORY_SET_NAME | — | ✅ |
| 3 | CatalogTranslationPEOCreatedBy | CREATED_BY | — | — |
| 4 | CatalogTranslationPEOCreationDate | CREATION_DATE | — | — |
| 5 | CatalogTranslationPEODescription | DESCRIPTION | — | ✅ |
| 6 | CatalogTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 7 | CatalogTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CatalogTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | CatalogTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | CatalogTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | CatalogTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[egp_category_set_valid_cats|EGP_CATEGORY_SET_VALID_CATS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ValidCategoryPEOCategoryId | CATEGORY_ID | — | — |
| 2 | ValidCategoryPEOCategorySetId | CATEGORY_SET_ID | — | — |
| 3 | ValidCategoryPEOCategorySharedFlag | CATEGORY_SHARED_FLAG | — | — |
| 4 | ValidCategoryPEOCreatedBy | CREATED_BY | — | — |
| 5 | ValidCategoryPEOCreationDate | CREATION_DATE | — | — |
| 6 | ValidCategoryPEOEndDate | END_DATE | — | ✅ |
| 7 | ValidCategoryPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 8 | ValidCategoryPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 9 | ValidCategoryPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | ValidCategoryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | ValidCategoryPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | ValidCategoryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | ValidCategoryPEOParentCategoryId | PARENT_CATEGORY_ID | — | — |
| 14 | ValidCategoryPEOReferenceCategorySetId | REFERENCE_CATEGORY_SET_ID | — | — |
| 15 | ValidCategoryPEORequestId | REQUEST_ID | — | — |
| 16 | ValidCategoryPEOSequenceNumber | SEQUENCE_NUMBER | — | — |
| 17 | ValidCategoryPEOStartDate | START_DATE | — | — |

### [[egp_item_categories|EGP_ITEM_CATEGORIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryId | CATEGORY_ID | 🔑 | ✅ |
| 2 | CategorySetId | CATEGORY_SET_ID | 🔑 | ✅ |
| 3 | InventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 4 | ItemCategoryPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | ItemCategoryPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | ItemCategoryPEOItemCategoryAssignmentId | ITEM_CATEGORY_ASSIGNMENT_ID | — | — |
| 7 | ItemCategoryPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ItemCategoryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ItemCategoryPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ItemCategoryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ItemCategoryPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 12 | ItemCategoryPEOProgramName | PROGRAM_NAME | — | — |
| 13 | ItemCategoryPEORequestId | REQUEST_ID | — | — |
| 14 | ItemCategoryPEOSequenceNumber | SEQUENCE_NUMBER | — | — |
| 15 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
