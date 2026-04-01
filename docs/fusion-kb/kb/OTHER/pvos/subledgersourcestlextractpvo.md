---
id: DOC-OTHER-PVO-SubledgerSourcesTLExtractPVO
doc_type: system-doc
title: "SubledgerSourcesTLExtractPVO — PVO Cross-Module"
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
  - SubledgerSourcesTLExtractPVO
  - subledgersourcestlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SubledgerSourcesTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Subledger Sources TLExtract. Acessa as tabelas: XLA_SOURCES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.SubledgerSourcesTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 4 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_sources_tl|XLA_SOURCES_TL]] — 14 atributos (4 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[xla_sources_tl|XLA_SOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SubledgerSourcesTranslationApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 2 | SubledgerSourcesTranslationCreatedBy | CREATED_BY | — | ✅ |
| 3 | SubledgerSourcesTranslationCreationDate | CREATION_DATE | — | ✅ |
| 4 | SubledgerSourcesTranslationDescription | DESCRIPTION | — | ✅ |
| 5 | SubledgerSourcesTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | SubledgerSourcesTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | SubledgerSourcesTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | SubledgerSourcesTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | SubledgerSourcesTranslationName | NAME | — | ✅ |
| 10 | SubledgerSourcesTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | SubledgerSourcesTranslationSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 12 | SubledgerSourcesTranslationSourceCode | SOURCE_CODE | 🔑 | ✅ |
| 13 | SubledgerSourcesTranslationSourceLang | SOURCE_LANG | — | ✅ |
| 14 | SubledgerSourcesTranslationSourceTypeCode | SOURCE_TYPE_CODE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
