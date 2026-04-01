---
id: DOC-HCM-PVO-PersonAddressPVOViewAll
doc_type: system-doc
title: "PersonAddressPVOViewAll — PVO Human Capital Management"
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
  - PersonAddressPVOViewAll
  - personaddresspvoviewall
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonAddressPVOViewAll

## 📌 Visão Geral

Versão ViewAll dos endereços de colaboradores, sem filtros de segurança. Permite extração completa de dados de endereço para relatórios administrativos e auditorias.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.PersonAddressPVOViewAll`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 47 | 3 | 3 | 34 | 72% |

---

## 🔗 Tabelas Relacionadas

- [[per_addresses_f|PER_ADDRESSES_F]] — 30 atributos (3 PKs, 28 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 4 atributos (2 BICC)
- [[per_person_addr_usages_f|PER_PERSON_ADDR_USAGES_F]] — 13 atributos (4 BICC)

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
| 16 | AddressesPEOFloorNumber | FLOOR_NUMBER | — | ✅ |
| 17 | AddressesPEOGeometry | GEOMETRY | — | — |
| 18 | AddressesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | AddressesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 20 | AddressesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 21 | AddressesPEOLongPostalCode | LONG_POSTAL_CODE | — | ✅ |
| 22 | AddressesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | AddressesPEOPostalCode | POSTAL_CODE | — | ✅ |
| 24 | AddressesPEORegion1 | REGION_1 | — | ✅ |
| 25 | AddressesPEORegion2 | REGION_2 | — | ✅ |
| 26 | AddressesPEORegion3 | REGION_3 | — | ✅ |
| 27 | AddressesPEOTimezoneCode | TIMEZONE_CODE | — | ✅ |
| 28 | AddressesPEOTownOrCity | TOWN_OR_CITY | — | ✅ |
| 29 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 30 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonDetailsPEOMailingAddressId | MAILING_ADDRESS_ID | — | ✅ |
| 4 | PersonDetailsPEOPersonId | PERSON_ID | — | — |

### [[per_person_addr_usages_f|PER_PERSON_ADDR_USAGES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonAddressUsagesPEOAddressId | ADDRESS_ID | — | — |
| 2 | PersonAddressUsagesPEOAddressType | ADDRESS_TYPE | — | ✅ |
| 3 | PersonAddressUsagesPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | PersonAddressUsagesPEOCreatedBy | CREATED_BY | — | — |
| 5 | PersonAddressUsagesPEOCreationDate | CREATION_DATE | — | — |
| 6 | PersonAddressUsagesPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 7 | PersonAddressUsagesPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 8 | PersonAddressUsagesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | PersonAddressUsagesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | PersonAddressUsagesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | PersonAddressUsagesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | PersonAddressUsagesPEOPersonAddrUsageId | PERSON_ADDR_USAGE_ID | — | — |
| 13 | PersonAddressUsagesPEOPersonId | PERSON_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
