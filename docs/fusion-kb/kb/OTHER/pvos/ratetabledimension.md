---
id: DOC-OTHER-PVO-RateTableDimension
doc_type: system-doc
title: "RateTableDimension — PVO Cross-Module"
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
  - RateTableDimension
  - ratetabledimension
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RateTableDimension

## 📌 Visão Geral

View Object para extração BICC de dados de Rate Table Dimension. Acessa as tabelas: CN_RATE_DIMENSIONS_ALL_B, CN_RATE_DIMENSIONS_ALL_TL, CN_RATE_TABLE_DIMS_ALL.

**Caminho:** `FscmTopModelAM.RateTableAM.RateTableDimension`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 3 | 1 | 13 | 68% |

---

## 🔗 Tabelas Relacionadas

- [[cn_rate_dimensions_all_b|CN_RATE_DIMENSIONS_ALL_B]] — 3 atributos (2 BICC)
- [[cn_rate_dimensions_all_tl|CN_RATE_DIMENSIONS_ALL_TL]] — 5 atributos (2 BICC)
- [[cn_rate_table_dims_all|CN_RATE_TABLE_DIMS_ALL]] — 11 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[cn_rate_dimensions_all_b|CN_RATE_DIMENSIONS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DimUnitCode | DIM_UNIT_CODE | — | ✅ |
| 2 | NumberTier | NUMBER_TIER | — | ✅ |
| 3 | RateDimPEORateDimensionId | RATE_DIMENSION_ID | — | — |

### [[cn_rate_dimensions_all_tl|CN_RATE_DIMENSIONS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | RateDimTLPEOLanguage | LANGUAGE | — | — |
| 3 | RateDimTLPEOObjVerNum | OBJECT_VERSION_NUMBER | — | — |
| 4 | RateDimTLPEORateDimensionId | RATE_DIMENSION_ID | — | — |
| 5 | RateDimensionName | RATE_DIMENSION_NAME | — | ✅ |

### [[cn_rate_table_dims_all|CN_RATE_TABLE_DIMS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | OrgId | ORG_ID | — | — |
| 8 | RateDimSequence | RATE_DIM_SEQUENCE | — | ✅ |
| 9 | RateDimensionId | RATE_DIMENSION_ID | — | ✅ |
| 10 | RateTableDimId | RATE_TABLE_DIM_ID | 🔑 | ✅ |
| 11 | RateTableId | RATE_TABLE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
