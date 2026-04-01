---
id: DOC-AP-PVO-SupplierSiteAddressPVO
doc_type: system-doc
title: "SupplierSiteAddressPVO — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - SupplierSiteAddressPVO
  - suppliersiteaddresspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierSiteAddressPVO

## 📌 Visão Geral

Extrai os endereços dos sites de fornecedores, incluindo logradouro, cidade, estado, país, CEP e pontos de contato (telefone, e-mail, fax). Essencial para cadastro de fornecedores, emissão de documentos fiscais e comunicação com a cadeia de suprimentos.

**Caminho:** `FscmTopModelAM.FinApInvTransactionsAM.SupplierSiteAddressPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 54 | 3 | 3 | 19 | 35% |

---

## 🔗 Tabelas Relacionadas

- [[hz_contact_points|HZ_CONTACT_POINTS]] — 9 atributos (1 PKs, 4 BICC)
- [[hz_locations|HZ_LOCATIONS]] — 13 atributos (1 PKs, 13 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 32 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[hz_contact_points|HZ_CONTACT_POINTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContactPointContactPointId | CONTACT_POINT_ID | 🔑 | ✅ |
| 2 | ContactPointContactPointType | CONTACT_POINT_TYPE | — | — |
| 3 | ContactPointEmailAddress | EMAIL_ADDRESS | — | — |
| 4 | ContactPointPhoneAreaCode | PHONE_AREA_CODE | — | ✅ |
| 5 | ContactPointPhoneCountryCode | PHONE_COUNTRY_CODE | — | ✅ |
| 6 | ContactPointPhoneExtension | PHONE_EXTENSION | — | ✅ |
| 7 | ContactPointPhoneLineType | PHONE_LINE_TYPE | — | — |
| 8 | ContactPointPhoneNumber | PHONE_NUMBER | — | — |
| 9 | ContactPointPrimaryFlag | PRIMARY_FLAG | — | — |

### [[hz_locations|HZ_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocationAddress1 | ADDRESS1 | — | ✅ |
| 2 | LocationAddress2 | ADDRESS2 | — | ✅ |
| 3 | LocationAddress3 | ADDRESS3 | — | ✅ |
| 4 | LocationAddress4 | ADDRESS4 | — | ✅ |
| 5 | LocationAddressEffectiveDate | ADDRESS_EFFECTIVE_DATE | — | ✅ |
| 6 | LocationAddressExpirationDate | ADDRESS_EXPIRATION_DATE | — | ✅ |
| 7 | LocationCity | CITY | — | ✅ |
| 8 | LocationCountry | COUNTRY | — | ✅ |
| 9 | LocationCounty | COUNTY | — | ✅ |
| 10 | LocationLocationId | LOCATION_ID | 🔑 | ✅ |
| 11 | LocationPostalCode | POSTAL_CODE | — | ✅ |
| 12 | LocationProvince | PROVINCE | — | ✅ |
| 13 | LocationState | STATE | — | ✅ |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartySitePEOActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | PartySitePEOAddressee | ADDRESSEE | — | — |
| 3 | PartySitePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | PartySitePEOComments | COMMENTS | — | — |
| 5 | PartySitePEOCreatedBy | CREATED_BY | — | — |
| 6 | PartySitePEOCreatedByModule | CREATED_BY_MODULE | — | — |
| 7 | PartySitePEOCreationDate | CREATION_DATE | — | — |
| 8 | PartySitePEODunsNumberC | DUNS_NUMBER_C | — | — |
| 9 | PartySitePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 10 | PartySitePEOGlobalLocationNumber | GLOBAL_LOCATION_NUMBER | — | — |
| 11 | PartySitePEOIdentifyingAddressFlag | IDENTIFYING_ADDRESS_FLAG | — | — |
| 12 | PartySitePEOLanguage | PARTY_SITE_LANGUAGE | — | — |
| 13 | PartySitePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 14 | PartySitePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | PartySitePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | PartySitePEOLocationId | LOCATION_ID | — | — |
| 17 | PartySitePEOMailstop | MAILSTOP | — | — |
| 18 | PartySitePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | PartySitePEOOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 20 | PartySitePEOOverallPrimaryFlag | OVERALL_PRIMARY_FLAG | — | — |
| 21 | PartySitePEOPartyId | PARTY_ID | — | — |
| 22 | PartySitePEOPartyNameDba | PARTY_NAME_DBA | — | — |
| 23 | PartySitePEOPartyNameDivision | PARTY_NAME_DIVISION | — | — |
| 24 | PartySitePEOPartyNameLegal | PARTY_NAME_LEGAL | — | — |
| 25 | PartySitePEOPartySiteId | PARTY_SITE_ID | 🔑 | ✅ |
| 26 | PartySitePEOPartySiteName | PARTY_SITE_NAME | — | — |
| 27 | PartySitePEOPartySiteNumber | PARTY_SITE_NUMBER | — | — |
| 28 | PartySitePEOPartySiteType | PARTY_SITE_TYPE | — | — |
| 29 | PartySitePEOPartyUsageCode | PARTY_USAGE_CODE | — | — |
| 30 | PartySitePEORelationshipId | RELATIONSHIP_ID | — | — |
| 31 | PartySitePEOStartDateActive | START_DATE_ACTIVE | — | — |
| 32 | PartySitePEOStatus | STATUS | — | — |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
