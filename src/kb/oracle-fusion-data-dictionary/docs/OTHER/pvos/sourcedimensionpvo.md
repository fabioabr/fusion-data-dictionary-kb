---
id: DOC-OTHER-PVO-SourceDimensionPVO
doc_type: system-doc
title: "SourceDimensionPVO — PVO Cross-Module"
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
  - SourceDimensionPVO
  - sourcedimensionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SourceDimensionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Source Dimension. Acessa as tabelas: IRC_DIMENSION_DEF_B, IRC_DIMENSION_DEF_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecSrcTrackingAM.SourceDimensionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 2 | 1 | 8 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[irc_dimension_def_b|IRC_DIMENSION_DEF_B]] — 14 atributos (1 PKs, 7 BICC)
- [[irc_dimension_def_tl|IRC_DIMENSION_DEF_TL]] — 4 atributos (1 BICC)

---

## ⚙️ Atributos

### [[irc_dimension_def_b|IRC_DIMENSION_DEF_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | DimensionId | DIMENSION_ID | 🔑 | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ModuleId | MODULE_ID | — | — |
| 8 | Priority | PRIORITY | — | — |
| 9 | SeedDataSource | SEED_DATA_SOURCE | — | — |
| 10 | Sequence | SEQUENCE | — | — |
| 11 | SourceMedium | SOURCE_MEDIUM | — | ✅ |
| 12 | SourceMediumUrlValue | SOURCE_MEDIUM_URL_VALUE | — | — |
| 13 | SourceUrlValue | SOURCE_URL_VALUE | — | — |
| 14 | UrlHeaderRegex | URL_HEADER_REGEX | — | — |

### [[irc_dimension_def_tl|IRC_DIMENSION_DEF_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SourceDimensionTLPEODimensionId | DIMENSION_ID | — | — |
| 2 | SourceDimensionTLPEOLanguage | LANGUAGE | — | — |
| 3 | SourceDimensionTLPEOSourceName | SOURCE_NAME | — | ✅ |
| 4 | SourceDisplayName | SOURCE_DISPLAY_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
