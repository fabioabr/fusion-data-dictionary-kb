---
id: DOC-OTHER-PVO-GeoHierarchyCf
doc_type: system-doc
title: "GeoHierarchyCf — PVO Cross-Module"
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
  - GeoHierarchyCf
  - geohierarchycf
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GeoHierarchyCf

## 📌 Visão Geral

View Object para extração BICC de dados de Geo Hierarchy Cf. Acessa as tabelas: HZ_GEO_HIERARCHY_CF.

**Caminho:** `FscmTopModelAM.GeographiesAnalyticsAM.GeoHierarchyCf`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 52 | 1 | 1 | 43 | 83% |

---

## 🔗 Tabelas Relacionadas

- [[hz_geo_hierarchy_cf|HZ_GEO_HIERARCHY_CF]] — 52 atributos (1 PKs, 43 BICC)

---

## ⚙️ Atributos

### [[hz_geo_hierarchy_cf|HZ_GEO_HIERARCHY_CF]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BaseGeoCode | BASE_GEO_CODE | — | ✅ |
| 2 | BaseGeoId | BASE_GEO_ID | — | ✅ |
| 3 | BaseGeoName | BASE_GEO_NAME | — | — |
| 4 | BaseZoneName | BASE_ZONE_NAME | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | — |
| 6 | CreationDate | CREATION_DATE | — | — |
| 7 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 9 | FixedHierLevel | FIXED_HIER_LEVEL | — | ✅ |
| 10 | HierarchyNodeId | HIERARCHY_NODE_ID | 🔑 | ✅ |
| 11 | HierarchyType | HIERARCHY_TYPE | — | — |
| 12 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | LeafFlag | LEAF_FLAG | — | — |
| 16 | Level01GeoCode | LEVEL_01_GEO_CODE | — | ✅ |
| 17 | Level01GeoId | LEVEL_01_GEO_ID | — | ✅ |
| 18 | Level01GeoName | LEVEL_01_GEO_NAME | — | ✅ |
| 19 | Level01ZoneName | LEVEL_01_ZONE_NAME | — | ✅ |
| 20 | Level02GeoCode | LEVEL_02_GEO_CODE | — | ✅ |
| 21 | Level02GeoId | LEVEL_02_GEO_ID | — | ✅ |
| 22 | Level02GeoName | LEVEL_02_GEO_NAME | — | ✅ |
| 23 | Level02ZoneName | LEVEL_02_ZONE_NAME | — | ✅ |
| 24 | Level03GeoCode | LEVEL_03_GEO_CODE | — | ✅ |
| 25 | Level03GeoId | LEVEL_03_GEO_ID | — | ✅ |
| 26 | Level03GeoName | LEVEL_03_GEO_NAME | — | ✅ |
| 27 | Level03ZoneName | LEVEL_03_ZONE_NAME | — | ✅ |
| 28 | Level04GeoCode | LEVEL_04_GEO_CODE | — | ✅ |
| 29 | Level04GeoId | LEVEL_04_GEO_ID | — | ✅ |
| 30 | Level04GeoName | LEVEL_04_GEO_NAME | — | ✅ |
| 31 | Level04ZoneName | LEVEL_04_ZONE_NAME | — | ✅ |
| 32 | Level05GeoCode | LEVEL_05_GEO_CODE | — | ✅ |
| 33 | Level05GeoId | LEVEL_05_GEO_ID | — | ✅ |
| 34 | Level05GeoName | LEVEL_05_GEO_NAME | — | ✅ |
| 35 | Level05ZoneName | LEVEL_05_ZONE_NAME | — | ✅ |
| 36 | Level06GeoCode | LEVEL_06_GEO_CODE | — | ✅ |
| 37 | Level06GeoId | LEVEL_06_GEO_ID | — | ✅ |
| 38 | Level06GeoName | LEVEL_06_GEO_NAME | — | ✅ |
| 39 | Level06ZoneName | LEVEL_06_ZONE_NAME | — | ✅ |
| 40 | Level07GeoCode | LEVEL_07_GEO_CODE | — | ✅ |
| 41 | Level07GeoId | LEVEL_07_GEO_ID | — | ✅ |
| 42 | Level07GeoName | LEVEL_07_GEO_NAME | — | ✅ |
| 43 | Level07ZoneName | LEVEL_07_ZONE_NAME | — | ✅ |
| 44 | Level08GeoCode | LEVEL_08_GEO_CODE | — | ✅ |
| 45 | Level08GeoId | LEVEL_08_GEO_ID | — | ✅ |
| 46 | Level08GeoName | LEVEL_08_GEO_NAME | — | ✅ |
| 47 | Level08ZoneName | LEVEL_08_ZONE_NAME | — | ✅ |
| 48 | Status | STATUS | — | — |
| 49 | TopGeoCode | TOP_GEO_CODE | — | ✅ |
| 50 | TopGeoId | TOP_GEO_ID | — | ✅ |
| 51 | TopGeoName | TOP_GEO_NAME | — | ✅ |
| 52 | TopZoneName | TOP_ZONE_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
