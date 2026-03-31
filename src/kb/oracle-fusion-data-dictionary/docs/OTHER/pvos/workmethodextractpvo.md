---
id: DOC-OTHER-PVO-WorkMethodExtractPVO
doc_type: system-doc
title: "WorkMethodExtractPVO — PVO Cross-Module"
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
  - WorkMethodExtractPVO
  - workmethodextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkMethodExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Work Method Extract. Acessa as tabelas: WIS_WORK_METHODS_B, WIS_WORK_METHODS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WisBiccExtractAM.WorkMethodExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 62 | 2 | 3 | 62 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wis_work_methods_b|WIS_WORK_METHODS_B]] — 50 atributos (1 PKs, 50 BICC)
- [[wis_work_methods_tl|WIS_WORK_METHODS_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[wis_work_methods_b|WIS_WORK_METHODS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 2 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 3 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 4 | AttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 5 | AttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 6 | AttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 7 | AttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 8 | AttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 9 | AttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 10 | AttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 11 | AttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 12 | AttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 13 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 14 | AttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 15 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 16 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 17 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 18 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 19 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 20 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 21 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 22 | AttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 23 | AttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 24 | AttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 25 | AttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 26 | AttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 27 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 28 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 29 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 30 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 31 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 32 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 33 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 34 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 35 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 36 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 37 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 38 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 39 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 40 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 41 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 42 | CreatedBy | CREATED_BY | — | ✅ |
| 43 | CreationDate | CREATION_DATE | — | ✅ |
| 44 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 45 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 46 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 47 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 48 | SeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 49 | WorkMethodCode | WORK_METHOD_CODE | — | ✅ |
| 50 | WorkMethodId | WORK_METHOD_ID | 🔑 | ✅ |

### [[wis_work_methods_tl|WIS_WORK_METHODS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WorkMethodTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | WorkMethodTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | WorkMethodTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | WorkMethodTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | WorkMethodTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | WorkMethodTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | WorkMethodTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | WorkMethodTranslationPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 9 | WorkMethodTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |
| 10 | WorkMethodTranslationPEOWorkMethodDescription | WORK_METHOD_DESCRIPTION | — | ✅ |
| 11 | WorkMethodTranslationPEOWorkMethodId | WORK_METHOD_ID | 🔑 | ✅ |
| 12 | WorkMethodTranslationPEOWorkMethodName | WORK_METHOD_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
