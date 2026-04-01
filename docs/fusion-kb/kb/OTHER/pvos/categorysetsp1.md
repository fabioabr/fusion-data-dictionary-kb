---
id: DOC-OTHER-PVO-CategorySetsP1
doc_type: system-doc
title: "CategorySetsP1 — PVO Cross-Module"
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
  - CategorySetsP1
  - categorysetsp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CategorySetsP1

## 📌 Visão Geral

View Object para extração BICC de dados de Category Sets P1. Acessa as tabelas: EGP_CATEGORY_SETS_B, EGP_CATEGORY_SETS_TL.

**Caminho:** `FscmTopModelAM.CatalogAM.CategorySetsP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 45 | 2 | 1 | 19 | 42% |

---

## 🔗 Tabelas Relacionadas

- [[egp_category_sets_b|EGP_CATEGORY_SETS_B]] — 34 atributos (1 PKs, 16 BICC)
- [[egp_category_sets_tl|EGP_CATEGORY_SETS_TL]] — 11 atributos (3 BICC)

---

## ⚙️ Atributos

### [[egp_category_sets_b|EGP_CATEGORY_SETS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CatalogCode | CATALOG_CODE | — | ✅ |
| 2 | CatalogContentCode | CATALOG_CONTENT_CODE | — | ✅ |
| 3 | CategorySetId | CATEGORY_SET_ID | 🔑 | ✅ |
| 4 | ControlLevel | CONTROL_LEVEL | — | ✅ |
| 5 | ControlLevelUpdateableFlag | CONTROL_LEVEL_UPDATEABLE_FLAG | — | — |
| 6 | CreatedBy | CREATED_BY | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | DefaultCategoryId | DEFAULT_CATEGORY_ID | — | ✅ |
| 9 | EndDate | END_DATE | — | ✅ |
| 10 | HierarchyEnabled | HIERARCHY_ENABLED | — | ✅ |
| 11 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 12 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 13 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | MultItemCatAssignFlag | MULT_ITEM_CAT_ASSIGN_FLAG | — | — |
| 17 | MultItemCatUpdateableFlag | MULT_ITEM_CAT_UPDATEABLE_FLAG | — | ✅ |
| 18 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | ProgramAppName | PROGRAM_APP_NAME | — | — |
| 20 | ProgramName | PROGRAM_NAME | — | — |
| 21 | RaiseAltCatHierChgEvent | RAISE_ALT_CAT_HIER_CHG_EVENT | — | — |
| 22 | RaiseCatalogCatChgEvent | RAISE_CATALOG_CAT_CHG_EVENT | — | — |
| 23 | RaiseItemCatAssignEvent | RAISE_ITEM_CAT_ASSIGN_EVENT | — | — |
| 24 | RequestId | REQUEST_ID | — | — |
| 25 | SequenceNumber | SEQUENCE_NUMBER | — | — |
| 26 | SharingContentCode | SHARING_CONTENT_CODE | — | ✅ |
| 27 | SharingControlCode | SHARING_CONTROL_CODE | — | — |
| 28 | SourceCategorySetId | SOURCE_CATEGORY_SET_ID | — | ✅ |
| 29 | StartDate | START_DATE | — | ✅ |
| 30 | StatusFlag | STATUS_FLAG | — | — |
| 31 | StructureId | STRUCTURE_ID | — | — |
| 32 | StructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 33 | ValidateFlag | VALIDATE_FLAG | — | ✅ |
| 34 | ValidateFlagUpdateableFlag | VALIDATE_FLAG_UPDATEABLE_FLAG | — | — |

### [[egp_category_sets_tl|EGP_CATEGORY_SETS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CatalogTranslationPEOCategorySetId | CATEGORY_SET_ID | — | — |
| 2 | CatalogTranslationPEOCategorySetName | CATEGORY_SET_NAME | — | ✅ |
| 3 | CatalogTranslationPEOCreatedBy | CREATED_BY | — | — |
| 4 | CatalogTranslationPEOCreationDate | CREATION_DATE | — | — |
| 5 | CatalogTranslationPEODescription | DESCRIPTION | — | ✅ |
| 6 | CatalogTranslationPEOLanguage | LANGUAGE | — | — |
| 7 | CatalogTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CatalogTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | CatalogTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | CatalogTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | CatalogTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
