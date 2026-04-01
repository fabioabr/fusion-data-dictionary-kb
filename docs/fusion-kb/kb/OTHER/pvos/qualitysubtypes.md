---
id: DOC-OTHER-PVO-QualitySubTypes
doc_type: system-doc
title: "QualitySubTypes — PVO Cross-Module"
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
  - QualitySubTypes
  - qualitysubtypes
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QualitySubTypes

## 📌 Visão Geral

View Object para extração BICC de dados de Quality Sub Types. Acessa as tabelas: ENQ_QUALITY_TYPES_SUBTYPES_V.

**Caminho:** `FscmTopModelAM.QualityCommonAnalyticsAM.QualitySubTypes`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 31 | 1 | 1 | 31 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[enq_quality_types_subtypes_v|ENQ_QUALITY_TYPES_SUBTYPES_V]] — 31 atributos (1 PKs, 31 BICC)

---

## ⚙️ Atributos

### [[enq_quality_types_subtypes_v|ENQ_QUALITY_TYPES_SUBTYPES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ParentQualityTypeId1 | PARENT_QUALITY_TYPE_ID1 | — | ✅ |
| 2 | ParentQualityTypeId10 | PARENT_QUALITY_TYPE_ID10 | — | ✅ |
| 3 | ParentQualityTypeId11 | PARENT_QUALITY_TYPE_ID11 | — | ✅ |
| 4 | ParentQualityTypeId12 | PARENT_QUALITY_TYPE_ID12 | — | ✅ |
| 5 | ParentQualityTypeId13 | PARENT_QUALITY_TYPE_ID13 | — | ✅ |
| 6 | ParentQualityTypeId14 | PARENT_QUALITY_TYPE_ID14 | — | ✅ |
| 7 | ParentQualityTypeId15 | PARENT_QUALITY_TYPE_ID15 | — | ✅ |
| 8 | ParentQualityTypeId2 | PARENT_QUALITY_TYPE_ID2 | — | ✅ |
| 9 | ParentQualityTypeId3 | PARENT_QUALITY_TYPE_ID3 | — | ✅ |
| 10 | ParentQualityTypeId4 | PARENT_QUALITY_TYPE_ID4 | — | ✅ |
| 11 | ParentQualityTypeId5 | PARENT_QUALITY_TYPE_ID5 | — | ✅ |
| 12 | ParentQualityTypeId6 | PARENT_QUALITY_TYPE_ID6 | — | ✅ |
| 13 | ParentQualityTypeId7 | PARENT_QUALITY_TYPE_ID7 | — | ✅ |
| 14 | ParentQualityTypeId8 | PARENT_QUALITY_TYPE_ID8 | — | ✅ |
| 15 | ParentQualityTypeId9 | PARENT_QUALITY_TYPE_ID9 | — | ✅ |
| 16 | QualityTypeSubTypesPEOCode | CODE | — | ✅ |
| 17 | QualityTypeSubTypesPEOCreatedBy | CREATED_BY | — | ✅ |
| 18 | QualityTypeSubTypesPEOCreationDate | CREATION_DATE | — | ✅ |
| 19 | QualityTypeSubTypesPEODescription | DESCRIPTION | — | ✅ |
| 20 | QualityTypeSubTypesPEODisplayOrder | DISPLAY_ORDER | — | ✅ |
| 21 | QualityTypeSubTypesPEOInstantiationAllowed | INSTANTIATION_ALLOWED | — | ✅ |
| 22 | QualityTypeSubTypesPEOIsSeeded | IS_SEEDED | — | ✅ |
| 23 | QualityTypeSubTypesPEOLabel | LABEL | — | ✅ |
| 24 | QualityTypeSubTypesPEOLanguage | LANGUAGE | — | ✅ |
| 25 | QualityTypeSubTypesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | QualityTypeSubTypesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 27 | QualityTypeSubTypesPEOName | NAME | — | ✅ |
| 28 | QualityTypeSubTypesPEOObjectType | OBJECT_TYPE | — | ✅ |
| 29 | QualityTypeSubTypesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 30 | QualityTypeSubTypesPEOQualityTypeId | QUALITY_TYPE_ID | 🔑 | ✅ |
| 31 | QualityTypeSubTypesPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
