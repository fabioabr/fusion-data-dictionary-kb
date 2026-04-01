---
id: DOC-HCM-497
doc_type: system-doc
title: "HZ_GEO_STRUCTURE_LEVELS — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - HZ_GEO_STRUCTURE_LEVELS
  - hz_geo_structure_levels
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# HZ_GEO_STRUCTURE_LEVELS

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ADDR_VAL_LEVEL | — | — | — | — | — | — |
| 2 | COUNTRY_CODE | — | — | — | — | — | — |
| 3 | CREATED_BY | — | — | — | — | — | — |
| 4 | CREATED_BY_MODULE | — | — | — | — | — | — |
| 5 | CREATION_DATE | — | — | — | — | — | — |
| 6 | GEOGRAPHY_ELEMENT_COLUMN | — | — | — | — | — | — |
| 7 | GEOGRAPHY_ID | — | — | — | — | — | — |
| 8 | GEOGRAPHY_TYPE | — | — | — | — | — | — |
| 9 | GEO_STRUCTURE_LEVEL_ID | — | — | — | — | — | — |
| 10 | GROUPING_FLAG | — | — | — | — | — | — |
| 11 | JOB_DEFINITION_NAME | — | — | — | — | — | — |
| 12 | JOB_DEFINITION_PACKAGE | — | — | — | — | — | — |
| 13 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 14 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 15 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 16 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 17 | PARENT_GEOGRAPHY_TYPE | — | — | — | — | — | — |
| 18 | RELATIONSHIP_TYPE_ID | — | — | — | — | — | — |
| 19 | REQUEST_ID | — | — | — | — | — | — |
| 20 | SEED_DATA_SOURCE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[hzgeostructurelevelpvo|HZGeoStructureLevelPVO]] (HCM · BICC: 3/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDR_VAL_LEVEL | HZGeoStructureLevelPEOAddrValLevel | — |
| COUNTRY_CODE | HZGeoStructureLevelPEOCountryCode | — |
| CREATED_BY | HZGeoStructureLevelPEOCreatedBy | — |
| CREATED_BY_MODULE | HZGeoStructureLevelPEOCreatedByModule | — |
| CREATION_DATE | HZGeoStructureLevelPEOCreationDate | — |
| GEO_STRUCTURE_LEVEL_ID | GeoStructureLevelId | ✅ |
| GEOGRAPHY_ELEMENT_COLUMN | HZGeoStructureLevelPEOGeographyElementColumn | — |
| GEOGRAPHY_ID | HZGeoStructureLevelPEOGeographyId | — |
| GEOGRAPHY_TYPE | HZGeoStructureLevelPEOGeographyType | ✅ |
| GROUPING_FLAG | HZGeoStructureLevelPEOGroupingFlag | — |
| JOB_DEFINITION_NAME | HZGeoStructureLevelPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | HZGeoStructureLevelPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | HZGeoStructureLevelPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | HZGeoStructureLevelPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | HZGeoStructureLevelPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | HZGeoStructureLevelPEOObjectVersionNumber | — |
| PARENT_GEOGRAPHY_TYPE | ParentGeographyType | — |
| RELATIONSHIP_TYPE_ID | HZGeoStructureLevelPEORelationshipTypeId | — |
| REQUEST_ID | HZGeoStructureLevelPEORequestId | — |
| SEED_DATA_SOURCE | HZGeoStructureLevelPEOSeedDataSource | — |
