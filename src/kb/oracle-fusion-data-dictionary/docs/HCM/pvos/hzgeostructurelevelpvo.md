---
id: DOC-HCM-PVO-HZGeoStructureLevelPVO
doc_type: system-doc
title: "HZGeoStructureLevelPVO — PVO Human Capital Management"
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
  - HZGeoStructureLevelPVO
  - hzgeostructurelevelpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HZGeoStructureLevelPVO

## 📌 Visão Geral

Disponibiliza níveis de estrutura geográfica (país, estado, cidade) para recrutamento. Suporta configuração de hierarquias de localidade.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecruitingSetupAM.HZGeoStructureLevelPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 1 | 1 | 3 | 15% |

---

## 🔗 Tabelas Relacionadas

- [[hz_geo_structure_levels|HZ_GEO_STRUCTURE_LEVELS]] — 20 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[hz_geo_structure_levels|HZ_GEO_STRUCTURE_LEVELS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GeoStructureLevelId | GEO_STRUCTURE_LEVEL_ID | 🔑 | ✅ |
| 2 | HZGeoStructureLevelPEOAddrValLevel | ADDR_VAL_LEVEL | — | — |
| 3 | HZGeoStructureLevelPEOCountryCode | COUNTRY_CODE | — | — |
| 4 | HZGeoStructureLevelPEOCreatedBy | CREATED_BY | — | — |
| 5 | HZGeoStructureLevelPEOCreatedByModule | CREATED_BY_MODULE | — | — |
| 6 | HZGeoStructureLevelPEOCreationDate | CREATION_DATE | — | — |
| 7 | HZGeoStructureLevelPEOGeographyElementColumn | GEOGRAPHY_ELEMENT_COLUMN | — | — |
| 8 | HZGeoStructureLevelPEOGeographyId | GEOGRAPHY_ID | — | — |
| 9 | HZGeoStructureLevelPEOGeographyType | GEOGRAPHY_TYPE | — | ✅ |
| 10 | HZGeoStructureLevelPEOGroupingFlag | GROUPING_FLAG | — | — |
| 11 | HZGeoStructureLevelPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 12 | HZGeoStructureLevelPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 13 | HZGeoStructureLevelPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | HZGeoStructureLevelPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | HZGeoStructureLevelPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | HZGeoStructureLevelPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | HZGeoStructureLevelPEORelationshipTypeId | RELATIONSHIP_TYPE_ID | — | — |
| 18 | HZGeoStructureLevelPEORequestId | REQUEST_ID | — | — |
| 19 | HZGeoStructureLevelPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 20 | ParentGeographyType | PARENT_GEOGRAPHY_TYPE | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
