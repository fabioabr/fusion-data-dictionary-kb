---
id: DOC-HCM-PVO-AddressesPVO
doc_type: system-doc
title: "AddressesPVO — PVO Human Capital Management"
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
  - AddressesPVO
  - addressespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AddressesPVO

## 📌 Visão Geral

Disponibiliza enderecos de pessoas com vigencia temporal e atributos adicionais configuraveis. Fundamental para correspondencia e localizacao de colaboradores.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.LocationAM.AddressesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 32 | 1 | 3 | 31 | 97% |

---

## 🔗 Tabelas Relacionadas

- [[per_addresses_f|PER_ADDRESSES_F]] — 32 atributos (3 PKs, 31 BICC)

---

## ⚙️ Atributos

### [[per_addresses_f|PER_ADDRESSES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddressId | ADDRESS_ID | 🔑 | ✅ |
| 2 | AddressesPEOAddlAddressAttribute1 | ADDL_ADDRESS_ATTRIBUTE1 | — | ✅ |
| 3 | AddressesPEOAddlAddressAttribute2 | ADDL_ADDRESS_ATTRIBUTE2 | — | ✅ |
| 4 | AddressesPEOAddlAddressAttribute3 | ADDL_ADDRESS_ATTRIBUTE3 | — | ✅ |
| 5 | AddressesPEOAddlAddressAttribute4 | ADDL_ADDRESS_ATTRIBUTE4 | — | ✅ |
| 6 | AddressesPEOAddlAddressAttribute5 | ADDL_ADDRESS_ATTRIBUTE5 | — | ✅ |
| 7 | AddressesPEOAddressLine1 | ADDRESS_LINE_1 | — | ✅ |
| 8 | AddressesPEOAddressLine2 | ADDRESS_LINE_2 | — | ✅ |
| 9 | AddressesPEOAddressLine3 | ADDRESS_LINE_3 | — | ✅ |
| 10 | AddressesPEOAddressLine4 | ADDRESS_LINE_4 | — | ✅ |
| 11 | AddressesPEOBuilding | BUILDING | — | ✅ |
| 12 | AddressesPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 13 | AddressesPEOCountry | COUNTRY | — | ✅ |
| 14 | AddressesPEOCreatedBy | CREATED_BY | — | ✅ |
| 15 | AddressesPEOCreationDate | CREATION_DATE | — | ✅ |
| 16 | AddressesPEODerivedLocale | DERIVED_LOCALE | — | ✅ |
| 17 | AddressesPEODqValidationLevel | DQ_VALIDATION_LEVEL | — | ✅ |
| 18 | AddressesPEOFloorNumber | FLOOR_NUMBER | — | ✅ |
| 19 | AddressesPEOGeometry | GEOMETRY | — | — |
| 20 | AddressesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | AddressesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 22 | AddressesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 23 | AddressesPEOLongPostalCode | LONG_POSTAL_CODE | — | ✅ |
| 24 | AddressesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 25 | AddressesPEOPostalCode | POSTAL_CODE | — | ✅ |
| 26 | AddressesPEORegion1 | REGION_1 | — | ✅ |
| 27 | AddressesPEORegion2 | REGION_2 | — | ✅ |
| 28 | AddressesPEORegion3 | REGION_3 | — | ✅ |
| 29 | AddressesPEOTimezoneCode | TIMEZONE_CODE | — | ✅ |
| 30 | AddressesPEOTownOrCity | TOWN_OR_CITY | — | ✅ |
| 31 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 32 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
