---
id: DOC-OTHER-PVO-CategoryP1
doc_type: system-doc
title: "CategoryP1 — PVO Cross-Module"
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
  - CategoryP1
  - categoryp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CategoryP1

## 📌 Visão Geral

View Object para extração BICC de dados de Category P1. Acessa as tabelas: EGP_CATEGORIES_B, EGP_CATEGORIES_TL.

**Caminho:** `FscmTopModelAM.CatalogAM.CategoryP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 77 | 2 | 1 | 23 | 30% |

---

## 🔗 Tabelas Relacionadas

- [[egp_categories_b|EGP_CATEGORIES_B]] — 66 atributos (1 PKs, 20 BICC)
- [[egp_categories_tl|EGP_CATEGORIES_TL]] — 11 atributos (3 BICC)

---

## ⚙️ Atributos

### [[egp_categories_b|EGP_CATEGORIES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryCode | CATEGORY_CODE | — | ✅ |
| 2 | CategoryContentCode | CATEGORY_CONTENT_CODE | — | ✅ |
| 3 | CategoryId | CATEGORY_ID | 🔑 | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | Description | DESCRIPTION | — | — |
| 7 | DisableDate | DISABLE_DATE | — | — |
| 8 | EnabledFlag | ENABLED_FLAG | — | ✅ |
| 9 | EndDateActive | END_DATE_ACTIVE | — | ✅ |
| 10 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 11 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 12 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | ProgramAppName | PROGRAM_APP_NAME | — | — |
| 17 | ProgramName | PROGRAM_NAME | — | — |
| 18 | RequestId | REQUEST_ID | — | — |
| 19 | Segment1 | SEGMENT1 | — | ✅ |
| 20 | Segment10 | SEGMENT10 | — | ✅ |
| 21 | Segment11 | SEGMENT11 | — | — |
| 22 | Segment12 | SEGMENT12 | — | — |
| 23 | Segment13 | SEGMENT13 | — | — |
| 24 | Segment14 | SEGMENT14 | — | — |
| 25 | Segment15 | SEGMENT15 | — | — |
| 26 | Segment16 | SEGMENT16 | — | — |
| 27 | Segment17 | SEGMENT17 | — | — |
| 28 | Segment18 | SEGMENT18 | — | — |
| 29 | Segment19 | SEGMENT19 | — | — |
| 30 | Segment2 | SEGMENT2 | — | ✅ |
| 31 | Segment20 | SEGMENT20 | — | — |
| 32 | Segment3 | SEGMENT3 | — | ✅ |
| 33 | Segment4 | SEGMENT4 | — | ✅ |
| 34 | Segment5 | SEGMENT5 | — | ✅ |
| 35 | Segment6 | SEGMENT6 | — | ✅ |
| 36 | Segment7 | SEGMENT7 | — | ✅ |
| 37 | Segment8 | SEGMENT8 | — | ✅ |
| 38 | Segment9 | SEGMENT9 | — | ✅ |
| 39 | SegmentNumber1 | SEGMENT_NUMBER1 | — | — |
| 40 | SegmentNumber10 | SEGMENT_NUMBER10 | — | — |
| 41 | SegmentNumber11 | SEGMENT_NUMBER11 | — | — |
| 42 | SegmentNumber12 | SEGMENT_NUMBER12 | — | — |
| 43 | SegmentNumber13 | SEGMENT_NUMBER13 | — | — |
| 44 | SegmentNumber14 | SEGMENT_NUMBER14 | — | — |
| 45 | SegmentNumber15 | SEGMENT_NUMBER15 | — | — |
| 46 | SegmentNumber16 | SEGMENT_NUMBER16 | — | — |
| 47 | SegmentNumber17 | SEGMENT_NUMBER17 | — | — |
| 48 | SegmentNumber18 | SEGMENT_NUMBER18 | — | — |
| 49 | SegmentNumber19 | SEGMENT_NUMBER19 | — | — |
| 50 | SegmentNumber2 | SEGMENT_NUMBER2 | — | — |
| 51 | SegmentNumber20 | SEGMENT_NUMBER20 | — | — |
| 52 | SegmentNumber3 | SEGMENT_NUMBER3 | — | — |
| 53 | SegmentNumber4 | SEGMENT_NUMBER4 | — | — |
| 54 | SegmentNumber5 | SEGMENT_NUMBER5 | — | — |
| 55 | SegmentNumber6 | SEGMENT_NUMBER6 | — | — |
| 56 | SegmentNumber7 | SEGMENT_NUMBER7 | — | — |
| 57 | SegmentNumber8 | SEGMENT_NUMBER8 | — | — |
| 58 | SegmentNumber9 | SEGMENT_NUMBER9 | — | — |
| 59 | StartDateActive | START_DATE_ACTIVE | — | ✅ |
| 60 | StructureId | STRUCTURE_ID | — | — |
| 61 | StructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |
| 62 | SummaryFlag | SUMMARY_FLAG | — | — |
| 63 | SupplierEnabledFlag | SUPPLIER_ENABLED_FLAG | — | — |
| 64 | TotalProdId | TOTAL_PROD_ID | — | — |
| 65 | WebStatus | WEB_STATUS | — | — |
| 66 | WhUpdateDate | WH_UPDATE_DATE | — | — |

### [[egp_categories_tl|EGP_CATEGORIES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CategoryTranslationPEOCategoryId | CATEGORY_ID | — | — |
| 2 | CategoryTranslationPEOCategoryName | CATEGORY_NAME | — | ✅ |
| 3 | CategoryTranslationPEOCreatedBy | CREATED_BY | — | — |
| 4 | CategoryTranslationPEOCreationDate | CREATION_DATE | — | — |
| 5 | CategoryTranslationPEODescription | DESCRIPTION | — | ✅ |
| 6 | CategoryTranslationPEOLanguage | LANGUAGE | — | — |
| 7 | CategoryTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CategoryTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | CategoryTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | CategoryTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | CategoryTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
