---
id: DOC-OTHER-PVO-QualityType
doc_type: system-doc
title: "QualityType — PVO Cross-Module"
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
  - QualityType
  - qualitytype
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QualityType

## 📌 Visão Geral

View Object para extração BICC de dados de Quality Type. Acessa as tabelas: ENQ_QUALITY_TYPES_VL.

**Caminho:** `FscmTopModelAM.QualityCommonAnalyticsAM.QualityType`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 1 | 18 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[enq_quality_types_vl|ENQ_QUALITY_TYPES_VL]] — 18 atributos (1 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[enq_quality_types_vl|ENQ_QUALITY_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualityTypePEOCode | CODE | — | ✅ |
| 2 | QualityTypePEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | QualityTypePEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | QualityTypePEODescription | DESCRIPTION | — | ✅ |
| 5 | QualityTypePEODisplayOrder | DISPLAY_ORDER | — | ✅ |
| 6 | QualityTypePEOInstantiationAllowed | INSTANTIATION_ALLOWED | — | ✅ |
| 7 | QualityTypePEOIsActive | IS_ACTIVE | — | ✅ |
| 8 | QualityTypePEOIsSeeded | IS_SEEDED | — | ✅ |
| 9 | QualityTypePEOLabel | LABEL | — | ✅ |
| 10 | QualityTypePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | QualityTypePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | QualityTypePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | QualityTypePEOName | NAME | — | ✅ |
| 14 | QualityTypePEOObjectType | OBJECT_TYPE | — | ✅ |
| 15 | QualityTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | QualityTypePEOParentQualityTypeId | PARENT_QUALITY_TYPE_ID | — | ✅ |
| 17 | QualityTypePEOQualityTypeId | QUALITY_TYPE_ID | 🔑 | ✅ |
| 18 | QualityTypePEOSource | SOURCE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
