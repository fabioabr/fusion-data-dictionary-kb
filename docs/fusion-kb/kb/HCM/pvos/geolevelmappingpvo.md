---
id: DOC-HCM-PVO-GeoLevelMappingPVO
doc_type: system-doc
title: "GeoLevelMappingPVO — PVO Human Capital Management"
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
  - GeoLevelMappingPVO
  - geolevelmappingpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GeoLevelMappingPVO

## 📌 Visão Geral

Disponibiliza mapeamentos de níveis geográficos por país para recrutamento. Define a correspondência entre tipos geográficos e hierarquias de contratação.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecruitingSetupAM.GeoLevelMappingPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 3 | 23% |

---

## 🔗 Tabelas Relacionadas

- [[irc_geo_level_mappings|IRC_GEO_LEVEL_MAPPINGS]] — 13 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[irc_geo_level_mappings|IRC_GEO_LEVEL_MAPPINGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GeoLevelMappingPEOCountryCode | COUNTRY_CODE | — | ✅ |
| 2 | GeoLevelMappingPEOCreatedBy | CREATED_BY | — | — |
| 3 | GeoLevelMappingPEOCreationDate | CREATION_DATE | — | — |
| 4 | GeoLevelMappingPEOGeoLevel2ColumnName | GEO_LEVEL2_COLUMN_NAME | — | — |
| 5 | GeoLevelMappingPEOGeoLevel3ColumnName | GEO_LEVEL3_COLUMN_NAME | — | — |
| 6 | GeoLevelMappingPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | GeoLevelMappingPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | GeoLevelMappingPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | GeoLevelMappingPEOModuleId | MODULE_ID | — | — |
| 10 | GeoLevelMappingPEOObjectStatus | OBJECT_STATUS | — | — |
| 11 | GeoLevelMappingPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | GeoLevelMappingPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 13 | GeoMappingId | GEO_MAPPING_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
