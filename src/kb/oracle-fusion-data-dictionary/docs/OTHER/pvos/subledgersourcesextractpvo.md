---
id: DOC-OTHER-PVO-SubledgerSourcesExtractPVO
doc_type: system-doc
title: "SubledgerSourcesExtractPVO — PVO Cross-Module"
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
  - SubledgerSourcesExtractPVO
  - subledgersourcesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SubledgerSourcesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Subledger Sources Extract. Acessa as tabelas: XLA_SOURCES_B, XLA_SOURCES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.SubledgerSourcesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 42 | 2 | 3 | 40 | 95% |

---

## 🔗 Tabelas Relacionadas

- [[xla_sources_b|XLA_SOURCES_B]] — 28 atributos (3 PKs, 26 BICC)
- [[xla_sources_tl|XLA_SOURCES_TL]] — 14 atributos (14 BICC)

---

## ⚙️ Atributos

### [[xla_sources_b|XLA_SOURCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SubledgerSourcesApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 2 | SubledgerSourcesCreatedBy | CREATED_BY | — | ✅ |
| 3 | SubledgerSourcesCreationDate | CREATION_DATE | — | ✅ |
| 4 | SubledgerSourcesDatatypeCode | DATATYPE_CODE | — | ✅ |
| 5 | SubledgerSourcesEnabledFlag | ENABLED_FLAG | — | ✅ |
| 6 | SubledgerSourcesFlexValueSetId | FLEX_VALUE_SET_ID | — | ✅ |
| 7 | SubledgerSourcesFlexfieldApplicationId | FLEXFIELD_APPLICATION_ID | — | ✅ |
| 8 | SubledgerSourcesIdFlexCode | ID_FLEX_CODE | — | ✅ |
| 9 | SubledgerSourcesKeyFlexfieldFlag | KEY_FLEXFIELD_FLAG | — | ✅ |
| 10 | SubledgerSourcesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | SubledgerSourcesLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | SubledgerSourcesLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | SubledgerSourcesLookupType | LOOKUP_TYPE | — | ✅ |
| 14 | SubledgerSourcesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | SubledgerSourcesPlsqlFunctionName | PLSQL_FUNCTION_NAME | — | ✅ |
| 16 | SubledgerSourcesSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 17 | SubledgerSourcesSegmentCode | SEGMENT_CODE | — | ✅ |
| 18 | SubledgerSourcesSourceCode | SOURCE_CODE | 🔑 | ✅ |
| 19 | SubledgerSourcesSourceColumnName | SOURCE_COLUMN_NAME | — | ✅ |
| 20 | SubledgerSourcesSourceId | SOURCE_ID | — | ✅ |
| 21 | SubledgerSourcesSourceTableName | SOURCE_TABLE_NAME | — | ✅ |
| 22 | SubledgerSourcesSourceTypeCode | SOURCE_TYPE_CODE | 🔑 | ✅ |
| 23 | SubledgerSourcesSplitTransactionFlag | SPLIT_TRANSACTION_FLAG | — | — |
| 24 | SubledgerSourcesSumFlag | SUM_FLAG | — | ✅ |
| 25 | SubledgerSourcesSummarizationFlag | SUMMARIZATION_FLAG | — | — |
| 26 | SubledgerSourcesTranslatedFlag | TRANSLATED_FLAG | — | ✅ |
| 27 | SubledgerSourcesViewApplicationId | VIEW_APPLICATION_ID | — | ✅ |
| 28 | SubledgerSourcesVisibleFlag | VISIBLE_FLAG | — | ✅ |

### [[xla_sources_tl|XLA_SOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SubledgerSourcesTranslationApplicationId | APPLICATION_ID | — | ✅ |
| 2 | SubledgerSourcesTranslationCreatedBy | CREATED_BY | — | ✅ |
| 3 | SubledgerSourcesTranslationCreationDate | CREATION_DATE | — | ✅ |
| 4 | SubledgerSourcesTranslationDescription | DESCRIPTION | — | ✅ |
| 5 | SubledgerSourcesTranslationLanguage | LANGUAGE | — | ✅ |
| 6 | SubledgerSourcesTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | SubledgerSourcesTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | SubledgerSourcesTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | SubledgerSourcesTranslationName | NAME | — | ✅ |
| 10 | SubledgerSourcesTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | SubledgerSourcesTranslationSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 12 | SubledgerSourcesTranslationSourceCode | SOURCE_CODE | — | ✅ |
| 13 | SubledgerSourcesTranslationSourceLang | SOURCE_LANG | — | ✅ |
| 14 | SubledgerSourcesTranslationSourceTypeCode | SOURCE_TYPE_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
