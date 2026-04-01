---
id: DOC-HCM-PVO-HZGeoTypePVO
doc_type: system-doc
title: "HZGeoTypePVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - HZGeoTypePVO
  - hzgeotypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HZGeoTypePVO

## 📌 Visão Geral

Disponibiliza tipos geográficos com traduções (país, região, município). Tabela de referência para classificação de localidades em recrutamento.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecruitingSetupAM.HZGeoTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 2 | 1 | 4 | 15% |

---

## 🔗 Tabelas Relacionadas

- [[hz_geography_types_b|HZ_GEOGRAPHY_TYPES_B]] — 16 atributos (1 PKs, 2 BICC)
- [[hz_geography_types_tl|HZ_GEOGRAPHY_TYPES_TL]] — 11 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hz_geography_types_b|HZ_GEOGRAPHY_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GeographyTypeId | GEOGRAPHY_TYPE_ID | — | — |
| 2 | HZGeoTypePEOCreatedBy | CREATED_BY | — | — |
| 3 | HZGeoTypePEOCreatedByModule | CREATED_BY_MODULE | — | — |
| 4 | HZGeoTypePEOCreationDate | CREATION_DATE | — | — |
| 5 | HZGeoTypePEOGeographyType | GEOGRAPHY_TYPE | 🔑 | ✅ |
| 6 | HZGeoTypePEOGeographyUse | GEOGRAPHY_USE | — | — |
| 7 | HZGeoTypePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 8 | HZGeoTypePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 9 | HZGeoTypePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | HZGeoTypePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | HZGeoTypePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | HZGeoTypePEOLimitedByGeographyId | LIMITED_BY_GEOGRAPHY_ID | — | — |
| 13 | HZGeoTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | HZGeoTypePEOPostalCodeRangeFlag | POSTAL_CODE_RANGE_FLAG | — | — |
| 15 | HZGeoTypePEORequestId | REQUEST_ID | — | — |
| 16 | HZGeoTypePEOSeedDataSource | SEED_DATA_SOURCE | — | — |

### [[hz_geography_types_tl|HZ_GEOGRAPHY_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HZGeoTypeTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | HZGeoTypeTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | HZGeoTypeTranslationPEOGeographyType | GEOGRAPHY_TYPE | — | — |
| 4 | HZGeoTypeTranslationPEOGeographyTypeName | GEOGRAPHY_TYPE_NAME | — | ✅ |
| 5 | HZGeoTypeTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | HZGeoTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | HZGeoTypeTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | HZGeoTypeTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | HZGeoTypeTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | HZGeoTypeTranslationPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 11 | HZGeoTypeTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
