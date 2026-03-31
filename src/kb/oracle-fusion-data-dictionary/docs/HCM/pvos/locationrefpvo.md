---
id: DOC-HCM-PVO-LocationRefPVO
doc_type: system-doc
title: "LocationRefPVO — PVO Human Capital Management"
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
  - LocationRefPVO
  - locationrefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LocationRefPVO

## 📌 Visão Geral

Consolida dados de referência de localidades incluindo endereços e detalhes traduzidos com vigência temporal. Utilizado como dimensão enriquecida para cruzamento com atribuições e posições.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.LocationAM.LocationRefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 66 | 4 | 4 | 10 | 15% |

---

## 🔗 Tabelas Relacionadas

- [[per_addresses_f|PER_ADDRESSES_F]] — 25 atributos
- [[per_locations|PER_LOCATIONS]] — 3 atributos (1 BICC)
- [[per_location_details_f_tl|PER_LOCATION_DETAILS_F_TL]] — 15 atributos (4 PKs, 6 BICC)
- [[per_location_details_f_vl|PER_LOCATION_DETAILS_F_VL]] — 23 atributos (3 BICC)

---

## ⚙️ Atributos

### [[per_addresses_f|PER_ADDRESSES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddressesPEOAddressId | ADDRESS_ID | — | — |
| 2 | AddressesPEOAddressLine1 | ADDRESS_LINE_1 | — | — |
| 3 | AddressesPEOAddressLine2 | ADDRESS_LINE_2 | — | — |
| 4 | AddressesPEOAddressLine3 | ADDRESS_LINE_3 | — | — |
| 5 | AddressesPEOAddressLine4 | ADDRESS_LINE_4 | — | — |
| 6 | AddressesPEOBuilding | BUILDING | — | — |
| 7 | AddressesPEOCountry | COUNTRY | — | — |
| 8 | AddressesPEOCreatedBy | CREATED_BY | — | — |
| 9 | AddressesPEOCreationDate | CREATION_DATE | — | — |
| 10 | AddressesPEODerivedLocale | DERIVED_LOCALE | — | — |
| 11 | AddressesPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 12 | AddressesPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 13 | AddressesPEOFloorNumber | FLOOR_NUMBER | — | — |
| 14 | AddressesPEOGeometry | GEOMETRY | — | — |
| 15 | AddressesPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 16 | AddressesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | AddressesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | AddressesPEOLongPostalCode | LONG_POSTAL_CODE | — | — |
| 19 | AddressesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | AddressesPEOPostalCode | POSTAL_CODE | — | — |
| 21 | AddressesPEORegion1 | REGION_1 | — | — |
| 22 | AddressesPEORegion2 | REGION_2 | — | — |
| 23 | AddressesPEORegion3 | REGION_3 | — | — |
| 24 | AddressesPEOTimezoneCode | TIMEZONE_CODE | — | — |
| 25 | AddressesPEOTownOrCity | TOWN_OR_CITY | — | — |

### [[per_locations|PER_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocationPEOInternalLocationCode | INTERNAL_LOCATION_CODE | — | — |
| 2 | LocationPEOLocationId | LOCATION_ID | — | — |
| 3 | LocationPEOSetId | SET_ID | — | ✅ |

### [[per_location_details_f_tl|PER_LOCATION_DETAILS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | Language | LANGUAGE | 🔑 | ✅ |
| 4 | LocationDetailsId | LOCATION_DETAILS_ID | 🔑 | ✅ |
| 5 | LocationDetailsTranslationPEOAcLocationCode | AC_LOCATION_CODE | — | — |
| 6 | LocationDetailsTranslationPEOCreatedBy | CREATED_BY | — | — |
| 7 | LocationDetailsTranslationPEOCreationDate | CREATION_DATE | — | — |
| 8 | LocationDetailsTranslationPEODescription | DESCRIPTION | — | — |
| 9 | LocationDetailsTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LocationDetailsTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | LocationDetailsTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | LocationDetailsTranslationPEOLocationCode | LOCATION_CODE | — | — |
| 13 | LocationDetailsTranslationPEOLocationName | LOCATION_NAME | — | ✅ |
| 14 | LocationDetailsTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | LocationDetailsTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[per_location_details_f_vl|PER_LOCATION_DETAILS_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocationDetailsPEOActiveStatus | ACTIVE_STATUS | — | — |
| 2 | LocationDetailsPEOBusinessGroupId | business_group_id | — | — |
| 3 | LocationDetailsPEOCreatedBy | CREATED_BY | — | — |
| 4 | LocationDetailsPEOCreationDate | CREATION_DATE | — | — |
| 5 | LocationDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | LocationDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | LocationDetailsPEOGeoHierarchyNodeId | GEO_HIERARCHY_NODE_ID | — | — |
| 8 | LocationDetailsPEOGeoHierarchyNodeValue | GEO_HIERARCHY_NODE_VALUE | — | — |
| 9 | LocationDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LocationDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | LocationDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | LocationDetailsPEOLocationDetailsId | LOCATION_DETAILS_ID | — | — |
| 13 | LocationDetailsPEOLocationId | LOCATION_ID | — | ✅ |
| 14 | LocationDetailsPEOMainAddressId | MAIN_ADDRESS_ID | — | — |
| 15 | LocationDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | LocationDetailsPEOOfficeSiteFlag | OFFICE_SITE_FLAG | — | — |
| 17 | LocationDetailsPEOOfficialLanguageCode | OFFICIAL_LANGUAGE_CODE | — | — |
| 18 | LocationDetailsPEOReceivingSiteFlag | RECEIVING_SITE_FLAG | — | — |
| 19 | LocationDetailsPEOShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 20 | LocationDetailsPEOShipToSiteFlag | SHIP_TO_SITE_FLAG | — | — |
| 21 | LocationDetailsPEOTelephoneNumber1 | TELEPHONE_NUMBER_1 | — | — |
| 22 | LocationDetailsPEOTelephoneNumber2 | TELEPHONE_NUMBER_2 | — | — |
| 23 | LocationDetailsPEOTelephoneNumber3 | TELEPHONE_NUMBER_3 | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
