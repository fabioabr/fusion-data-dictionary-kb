---
id: DOC-HCM-PVO-ContactPersonAddressPVO
doc_type: system-doc
title: "ContactPersonAddressPVO — PVO Human Capital Management"
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
  - ContactPersonAddressPVO
  - contactpersonaddresspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContactPersonAddressPVO

## 📌 Visão Geral

Extrai enderecos de contatos/dependentes com vigencia temporal e vinculo de relacionamento. Essencial para correspondencia com beneficiarios e dependentes.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.ContactPersonAddressPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 50 | 4 | 3 | 29 | 58% |

---

## 🔗 Tabelas Relacionadas

- [[per_addresses_f|PER_ADDRESSES_F]] — 25 atributos (3 PKs, 22 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 8 atributos (2 BICC)
- [[per_contact_relships_f|PER_CONTACT_RELSHIPS_F]] — 4 atributos (1 BICC)
- [[per_person_addr_usages_f|PER_PERSON_ADDR_USAGES_F]] — 13 atributos (4 BICC)

---

## ⚙️ Atributos

### [[per_addresses_f|PER_ADDRESSES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddressId | ADDRESS_ID | 🔑 | ✅ |
| 2 | AddressesPEOAddressLine1 | ADDRESS_LINE_1 | — | ✅ |
| 3 | AddressesPEOAddressLine2 | ADDRESS_LINE_2 | — | ✅ |
| 4 | AddressesPEOAddressLine3 | ADDRESS_LINE_3 | — | ✅ |
| 5 | AddressesPEOAddressLine4 | ADDRESS_LINE_4 | — | ✅ |
| 6 | AddressesPEOBuilding | BUILDING | — | ✅ |
| 7 | AddressesPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 8 | AddressesPEOCountry | COUNTRY | — | ✅ |
| 9 | AddressesPEOCreatedBy | CREATED_BY | — | ✅ |
| 10 | AddressesPEOCreationDate | CREATION_DATE | — | ✅ |
| 11 | AddressesPEOFloorNumber | FLOOR_NUMBER | — | ✅ |
| 12 | AddressesPEOGeometry | GEOMETRY | — | — |
| 13 | AddressesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | AddressesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | AddressesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | AddressesPEOLongPostalCode | LONG_POSTAL_CODE | — | ✅ |
| 17 | AddressesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | AddressesPEOPostalCode | POSTAL_CODE | — | ✅ |
| 19 | AddressesPEORegion1 | REGION_1 | — | ✅ |
| 20 | AddressesPEORegion2 | REGION_2 | — | ✅ |
| 21 | AddressesPEORegion3 | REGION_3 | — | ✅ |
| 22 | AddressesPEOTimezoneCode | TIMEZONE_CODE | — | ✅ |
| 23 | AddressesPEOTownOrCity | TOWN_OR_CITY | — | ✅ |
| 24 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 25 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContactPersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | ContactPersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | ContactPersonDetailsPEOMailingAddressId | MAILING_ADDRESS_ID | — | — |
| 4 | ContactPersonDetailsPEOPersonId | PERSON_ID | — | — |
| 5 | PersonDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | PersonDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | PersonDetailsPEOMailingAddressId | MAILING_ADDRESS_ID | — | — |
| 8 | PersonDetailsPEOPersonId | PERSON_ID | — | — |

### [[per_contact_relships_f|PER_CONTACT_RELSHIPS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContactRelshipsPEOContactRelationshipId | CONTACT_RELATIONSHIP_ID | — | — |
| 2 | ContactRelshipsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | ContactRelshipsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | ContactRelshipsPEOPersonId | PERSON_ID | — | — |

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
