---
id: DOC-GL-PVO-IntervalType
doc_type: system-doc
title: "IntervalType — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - IntervalType
  - intervaltype
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# IntervalType

## 📌 Visão Geral

View Object para extração BICC de dados de Interval Type. Acessa as tabelas: CN_INTERVAL_TYPES_ALL_B, CN_INTERVAL_TYPES_ALL_TL.

**Caminho:** `FscmTopModelAM.CalendarAM.IntervalType`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 37 | 2 | 2 | 21 | 57% |

---

## 🔗 Tabelas Relacionadas

- [[cn_interval_types_all_b|CN_INTERVAL_TYPES_ALL_B]] — 24 atributos (2 PKs, 9 BICC)
- [[cn_interval_types_all_tl|CN_INTERVAL_TYPES_ALL_TL]] — 13 atributos (12 BICC)

---

## ⚙️ Atributos

### [[cn_interval_types_all_b|CN_INTERVAL_TYPES_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute1 | ATTRIBUTE1 | — | — |
| 2 | Attribute10 | ATTRIBUTE10 | — | — |
| 3 | Attribute11 | ATTRIBUTE11 | — | — |
| 4 | Attribute12 | ATTRIBUTE12 | — | — |
| 5 | Attribute13 | ATTRIBUTE13 | — | — |
| 6 | Attribute14 | ATTRIBUTE14 | — | — |
| 7 | Attribute15 | ATTRIBUTE15 | — | — |
| 8 | Attribute2 | ATTRIBUTE2 | — | — |
| 9 | Attribute3 | ATTRIBUTE3 | — | — |
| 10 | Attribute4 | ATTRIBUTE4 | — | — |
| 11 | Attribute5 | ATTRIBUTE5 | — | — |
| 12 | Attribute6 | ATTRIBUTE6 | — | — |
| 13 | Attribute7 | ATTRIBUTE7 | — | — |
| 14 | Attribute8 | ATTRIBUTE8 | — | — |
| 15 | Attribute9 | ATTRIBUTE9 | — | — |
| 16 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 17 | CreatedBy | CREATED_BY | — | ✅ |
| 18 | CreationDate | CREATION_DATE | — | ✅ |
| 19 | IntervalTypeId | INTERVAL_TYPE_ID | 🔑 | ✅ |
| 20 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 22 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 23 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 24 | OrgId | ORG_ID | 🔑 | ✅ |

### [[cn_interval_types_all_tl|CN_INTERVAL_TYPES_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IntTypeTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | IntTypeTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | IntTypeTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | IntTypeTLPEOIntervalDesc | DESCRIPTION | — | — |
| 5 | IntTypeTLPEOIntervalName | INTERVAL_NAME | — | ✅ |
| 6 | IntTypeTLPEOIntervalTypeId | INTERVAL_TYPE_ID | — | ✅ |
| 7 | IntTypeTLPEOLanguage | LANGUAGE | — | ✅ |
| 8 | IntTypeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | IntTypeTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | IntTypeTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | IntTypeTLPEOObjVerNum | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | IntTypeTLPEOOrgId | ORG_ID | — | ✅ |
| 13 | IntTypeTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
