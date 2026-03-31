---
id: DOC-OTHER-PVO-TransitTimePVO
doc_type: system-doc
title: "TransitTimePVO — PVO Cross-Module"
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
  - TransitTimePVO
  - transittimepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransitTimePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transit Time. Acessa as tabelas: WSH_TRANSIT_TIMES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.TransitTimePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 1 | 1 | 19 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wsh_transit_times|WSH_TRANSIT_TIMES]] — 19 atributos (1 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[wsh_transit_times|WSH_TRANSIT_TIMES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | DestExtLocSource | DEST_EXT_LOC_SOURCE | — | ✅ |
| 4 | DestExtLocSourceId | DEST_EXT_LOC_SOURCE_ID | — | ✅ |
| 5 | DestinationType | DESTINATION_TYPE | — | ✅ |
| 6 | FromLocationId | FROM_LOCATION_ID | — | ✅ |
| 7 | FromRegionId | FROM_REGION_ID | — | ✅ |
| 8 | FromZoneId | FROM_ZONE_ID | — | ✅ |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | OriginExtLocSource | ORIGIN_EXT_LOC_SOURCE | — | ✅ |
| 14 | OriginExtLocSourceId | ORIGIN_EXT_LOC_SOURCE_ID | — | ✅ |
| 15 | OriginType | ORIGIN_TYPE | — | ✅ |
| 16 | ToLocationId | TO_LOCATION_ID | — | ✅ |
| 17 | ToRegionId | TO_REGION_ID | — | ✅ |
| 18 | ToZoneId | TO_ZONE_ID | — | ✅ |
| 19 | TransitTimeId | TRANSIT_TIME_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
