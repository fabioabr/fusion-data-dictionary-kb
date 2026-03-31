---
id: DOC-OTHER-PVO-CatalogCategoryAssignP1
doc_type: system-doc
title: "CatalogCategoryAssignP1 — PVO Cross-Module"
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
  - CatalogCategoryAssignP1
  - catalogcategoryassignp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CatalogCategoryAssignP1

## 📌 Visão Geral

View Object para extração BICC de dados de Catalog Category Assign P1. Acessa as tabelas: EGP_CATEGORIES_B, EGP_CATEGORIES_TL, EGP_CATEGORY_SETS_B (+2).

**Caminho:** `FscmTopModelAM.CatalogAM.CatalogCategoryAssignP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 139 | 5 | 3 | 23 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[egp_categories_b|EGP_CATEGORIES_B]] — 66 atributos (1 PKs, 6 BICC)
- [[egp_categories_tl|EGP_CATEGORIES_TL]] — 11 atributos (1 PKs, 9 BICC)
- [[egp_category_sets_b|EGP_CATEGORY_SETS_B]] — 34 atributos (1 PKs, 2 BICC)
- [[egp_category_sets_tl|EGP_CATEGORY_SETS_TL]] — 11 atributos (2 BICC)
- [[egp_category_set_valid_cats|EGP_CATEGORY_SET_VALID_CATS]] — 17 atributos (4 BICC)

---

## ⚙️ Atributos

### [[egp_categories_b|EGP_CATEGORIES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryBasePEOCategoryCode | CATEGORY_CODE | — | ✅ |
| 2 | CategoryBasePEOCategoryContentCode | CATEGORY_CONTENT_CODE | — | — |
| 3 | CategoryBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | CategoryBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | CategoryBasePEODescription | DESCRIPTION | — | — |
| 6 | CategoryBasePEODisableDate | DISABLE_DATE | — | — |
| 7 | CategoryBasePEOEnabledFlag | ENABLED_FLAG | — | — |
| 8 | CategoryBasePEOEndDateActive | END_DATE_ACTIVE | — | — |
| 9 | CategoryBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 10 | CategoryBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 11 | CategoryBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | CategoryBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | CategoryBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | CategoryBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | CategoryBasePEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 16 | CategoryBasePEOProgramName | PROGRAM_NAME | — | — |
| 17 | CategoryBasePEORequestId | REQUEST_ID | — | — |
| 18 | CategoryBasePEOSegment1 | SEGMENT1 | — | — |
| 19 | CategoryBasePEOSegment10 | SEGMENT10 | — | — |
| 20 | CategoryBasePEOSegment11 | SEGMENT11 | — | — |
| 21 | CategoryBasePEOSegment12 | SEGMENT12 | — | — |
| 22 | CategoryBasePEOSegment13 | SEGMENT13 | — | — |
| 23 | CategoryBasePEOSegment14 | SEGMENT14 | — | — |
| 24 | CategoryBasePEOSegment15 | SEGMENT15 | — | — |
| 25 | CategoryBasePEOSegment16 | SEGMENT16 | — | — |
| 26 | CategoryBasePEOSegment17 | SEGMENT17 | — | — |
| 27 | CategoryBasePEOSegment18 | SEGMENT18 | — | — |
| 28 | CategoryBasePEOSegment19 | SEGMENT19 | — | — |
| 29 | CategoryBasePEOSegment2 | SEGMENT2 | — | — |
| 30 | CategoryBasePEOSegment20 | SEGMENT20 | — | — |
| 31 | CategoryBasePEOSegment3 | SEGMENT3 | — | — |
| 32 | CategoryBasePEOSegment4 | SEGMENT4 | — | — |
| 33 | CategoryBasePEOSegment5 | SEGMENT5 | — | — |
| 34 | CategoryBasePEOSegment6 | SEGMENT6 | — | — |
| 35 | CategoryBasePEOSegment7 | SEGMENT7 | — | — |
| 36 | CategoryBasePEOSegment8 | SEGMENT8 | — | — |
| 37 | CategoryBasePEOSegment9 | SEGMENT9 | — | — |
| 38 | CategoryBasePEOSegmentNumber1 | SEGMENT_NUMBER1 | — | — |
| 39 | CategoryBasePEOSegmentNumber10 | SEGMENT_NUMBER10 | — | — |
| 40 | CategoryBasePEOSegmentNumber11 | SEGMENT_NUMBER11 | — | — |
| 41 | CategoryBasePEOSegmentNumber12 | SEGMENT_NUMBER12 | — | — |
| 42 | CategoryBasePEOSegmentNumber13 | SEGMENT_NUMBER13 | — | — |
| 43 | CategoryBasePEOSegmentNumber14 | SEGMENT_NUMBER14 | — | — |
| 44 | CategoryBasePEOSegmentNumber15 | SEGMENT_NUMBER15 | — | — |
| 45 | CategoryBasePEOSegmentNumber16 | SEGMENT_NUMBER16 | — | — |
| 46 | CategoryBasePEOSegmentNumber17 | SEGMENT_NUMBER17 | — | — |
| 47 | CategoryBasePEOSegmentNumber18 | SEGMENT_NUMBER18 | — | — |
| 48 | CategoryBasePEOSegmentNumber19 | SEGMENT_NUMBER19 | — | — |
| 49 | CategoryBasePEOSegmentNumber2 | SEGMENT_NUMBER2 | — | — |
| 50 | CategoryBasePEOSegmentNumber20 | SEGMENT_NUMBER20 | — | — |
| 51 | CategoryBasePEOSegmentNumber3 | SEGMENT_NUMBER3 | — | — |
| 52 | CategoryBasePEOSegmentNumber4 | SEGMENT_NUMBER4 | — | — |
| 53 | CategoryBasePEOSegmentNumber5 | SEGMENT_NUMBER5 | — | — |
| 54 | CategoryBasePEOSegmentNumber6 | SEGMENT_NUMBER6 | — | — |
| 55 | CategoryBasePEOSegmentNumber7 | SEGMENT_NUMBER7 | — | — |
| 56 | CategoryBasePEOSegmentNumber8 | SEGMENT_NUMBER8 | — | — |
| 57 | CategoryBasePEOSegmentNumber9 | SEGMENT_NUMBER9 | — | — |
| 58 | CategoryBasePEOStartDateActive | START_DATE_ACTIVE | — | — |
| 59 | CategoryBasePEOStructureId | STRUCTURE_ID | — | — |
| 60 | CategoryBasePEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 61 | CategoryBasePEOSummaryFlag | SUMMARY_FLAG | — | — |
| 62 | CategoryBasePEOSupplierEnabledFlag | SUPPLIER_ENABLED_FLAG | — | — |
| 63 | CategoryBasePEOTotalProdId | TOTAL_PROD_ID | — | — |
| 64 | CategoryBasePEOWebStatus | WEB_STATUS | — | — |
| 65 | CategoryBasePEOWhUpdateDate | WH_UPDATE_DATE | — | — |
| 66 | CategoryId | CATEGORY_ID | 🔑 | ✅ |

### [[egp_categories_tl|EGP_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryTranslationPEOCategoryId | CATEGORY_ID | — | ✅ |
| 2 | CategoryTranslationPEOCategoryName | CATEGORY_NAME | — | ✅ |
| 3 | CategoryTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | CategoryTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | CategoryTranslationPEODescription | DESCRIPTION | — | ✅ |
| 6 | CategoryTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | CategoryTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CategoryTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | CategoryTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | CategoryTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | CategoryTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

### [[egp_category_sets_b|EGP_CATEGORY_SETS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CatalogBasePEOCatalogCode | CATALOG_CODE | — | — |
| 2 | CatalogBasePEOCatalogContentCode | CATALOG_CONTENT_CODE | — | — |
| 3 | CatalogBasePEOCategorySetId | CATEGORY_SET_ID | 🔑 | ✅ |
| 4 | CatalogBasePEOControlLevel | CONTROL_LEVEL | — | — |
| 5 | CatalogBasePEOControlLevelUpdateableFlag | CONTROL_LEVEL_UPDATEABLE_FLAG | — | — |
| 6 | CatalogBasePEOCreatedBy | CREATED_BY | — | — |
| 7 | CatalogBasePEOCreationDate | CREATION_DATE | — | — |
| 8 | CatalogBasePEODefaultCategoryId | DEFAULT_CATEGORY_ID | — | — |
| 9 | CatalogBasePEOEndDate | END_DATE | — | — |
| 10 | CatalogBasePEOHierarchyEnabled | HIERARCHY_ENABLED | — | — |
| 11 | CatalogBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 12 | CatalogBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 13 | CatalogBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | CatalogBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | CatalogBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | CatalogBasePEOMultItemCatAssignFlag | MULT_ITEM_CAT_ASSIGN_FLAG | — | — |
| 17 | CatalogBasePEOMultItemCatUpdateableFlag | MULT_ITEM_CAT_UPDATEABLE_FLAG | — | — |
| 18 | CatalogBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | CatalogBasePEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 20 | CatalogBasePEOProgramName | PROGRAM_NAME | — | — |
| 21 | CatalogBasePEORaiseAltCatHierChgEvent | RAISE_ALT_CAT_HIER_CHG_EVENT | — | — |
| 22 | CatalogBasePEORaiseCatalogCatChgEvent | RAISE_CATALOG_CAT_CHG_EVENT | — | — |
| 23 | CatalogBasePEORaiseItemCatAssignEvent | RAISE_ITEM_CAT_ASSIGN_EVENT | — | — |
| 24 | CatalogBasePEORequestId | REQUEST_ID | — | — |
| 25 | CatalogBasePEOSequenceNumber | SEQUENCE_NUMBER | — | — |
| 26 | CatalogBasePEOSharingContentCode | SHARING_CONTENT_CODE | — | — |
| 27 | CatalogBasePEOSharingControlCode | SHARING_CONTROL_CODE | — | — |
| 28 | CatalogBasePEOSourceCategorySetId | SOURCE_CATEGORY_SET_ID | — | — |
| 29 | CatalogBasePEOStartDate | START_DATE | — | — |
| 30 | CatalogBasePEOStatusFlag | STATUS_FLAG | — | — |
| 31 | CatalogBasePEOStructureId | STRUCTURE_ID | — | — |
| 32 | CatalogBasePEOStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 33 | CatalogBasePEOValidateFlag | VALIDATE_FLAG | — | — |
| 34 | CatalogBasePEOValidateFlagUpdateableFlag | VALIDATE_FLAG_UPDATEABLE_FLAG | — | — |

### [[egp_category_sets_tl|EGP_CATEGORY_SETS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CatalogTranslationPEOCategorySetId | CATEGORY_SET_ID | — | — |
| 2 | CatalogTranslationPEOCategorySetName | CATEGORY_SET_NAME | — | — |
| 3 | CatalogTranslationPEOCreatedBy | CREATED_BY | — | — |
| 4 | CatalogTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | CatalogTranslationPEODescription | DESCRIPTION | — | — |
| 6 | CatalogTranslationPEOLanguage | LANGUAGE | — | — |
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
| 3 | ValidCategoryPEOCategorySharedFlag | CATEGORY_SHARED_FLAG | — | ✅ |
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
| 17 | ValidCategoryPEOStartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
