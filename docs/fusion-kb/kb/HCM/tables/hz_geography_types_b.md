---
id: DOC-HCM-495
doc_type: system-doc
title: "HZ_GEOGRAPHY_TYPES_B — (título a preencher)"
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
  - HZ_GEOGRAPHY_TYPES_B
  - hz_geography_types_b
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# HZ_GEOGRAPHY_TYPES_B

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CREATED_BY | — | — | — | — | — | — |
| 2 | CREATED_BY_MODULE | — | — | — | — | — | — |
| 3 | CREATION_DATE | — | — | — | — | — | — |
| 4 | GEOGRAPHY_TYPE | — | — | — | — | — | — |
| 5 | GEOGRAPHY_TYPE_ID | — | — | — | — | — | — |
| 6 | GEOGRAPHY_USE | — | — | — | — | — | — |
| 7 | JOB_DEFINITION_NAME | — | — | — | — | — | — |
| 8 | JOB_DEFINITION_PACKAGE | — | — | — | — | — | — |
| 9 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 10 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 11 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 12 | LIMITED_BY_GEOGRAPHY_ID | — | — | — | — | — | — |
| 13 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 14 | POSTAL_CODE_RANGE_FLAG | — | — | — | — | — | — |
| 15 | REQUEST_ID | — | — | — | — | — | — |
| 16 | SEED_DATA_SOURCE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[hzgeotypepvo|HZGeoTypePVO]] (HCM · BICC: 2/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | HZGeoTypePEOCreatedBy | — |
| CREATED_BY_MODULE | HZGeoTypePEOCreatedByModule | — |
| CREATION_DATE | HZGeoTypePEOCreationDate | — |
| GEOGRAPHY_TYPE | HZGeoTypePEOGeographyType | ✅ |
| GEOGRAPHY_TYPE_ID | GeographyTypeId | — |
| GEOGRAPHY_USE | HZGeoTypePEOGeographyUse | — |
| JOB_DEFINITION_NAME | HZGeoTypePEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | HZGeoTypePEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | HZGeoTypePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | HZGeoTypePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | HZGeoTypePEOLastUpdatedBy | — |
| LIMITED_BY_GEOGRAPHY_ID | HZGeoTypePEOLimitedByGeographyId | — |
| OBJECT_VERSION_NUMBER | HZGeoTypePEOObjectVersionNumber | — |
| POSTAL_CODE_RANGE_FLAG | HZGeoTypePEOPostalCodeRangeFlag | — |
| REQUEST_ID | HZGeoTypePEORequestId | — |
| SEED_DATA_SOURCE | HZGeoTypePEOSeedDataSource | — |
