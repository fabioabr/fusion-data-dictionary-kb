---
id: DOC-OTHER-PVO-PartySite
doc_type: system-doc
title: "PartySite — PVO Cross-Module"
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
  - PartySite
  - partysite
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PartySite

## 📌 Visão Geral

View Object para extração BICC de dados de Party Site. Acessa as tabelas: HZ_LOCATIONS, HZ_PARTIES, HZ_PARTY_SITES.

**Caminho:** `FscmTopModelAM.PartiesAnalyticsAM.PartySite`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 143 | 3 | 1 | 12 | 8% |

---

## 🔗 Tabelas Relacionadas

- [[hz_locations|HZ_LOCATIONS]] — 110 atributos
- [[hz_parties|HZ_PARTIES]] — 1 atributos
- [[hz_party_sites|HZ_PARTY_SITES]] — 32 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[hz_locations|HZ_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocationPEOActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | LocationPEOAddrElementAttribute1 | ADDR_ELEMENT_ATTRIBUTE1 | — | — |
| 3 | LocationPEOAddrElementAttribute2 | ADDR_ELEMENT_ATTRIBUTE2 | — | — |
| 4 | LocationPEOAddrElementAttribute3 | ADDR_ELEMENT_ATTRIBUTE3 | — | — |
| 5 | LocationPEOAddrElementAttribute4 | ADDR_ELEMENT_ATTRIBUTE4 | — | — |
| 6 | LocationPEOAddrElementAttribute5 | ADDR_ELEMENT_ATTRIBUTE5 | — | — |
| 7 | LocationPEOAddress1 | ADDRESS1 | — | — |
| 8 | LocationPEOAddress2 | ADDRESS2 | — | — |
| 9 | LocationPEOAddress3 | ADDRESS3 | — | — |
| 10 | LocationPEOAddress4 | ADDRESS4 | — | — |
| 11 | LocationPEOAddressEffectiveDate | ADDRESS_EFFECTIVE_DATE | — | — |
| 12 | LocationPEOAddressExpirationDate | ADDRESS_EXPIRATION_DATE | — | — |
| 13 | LocationPEOAddressLinesPhonetic | ADDRESS_LINES_PHONETIC | — | — |
| 14 | LocationPEOAddressStyle | ADDRESS_STYLE | — | — |
| 15 | LocationPEOAttribute1 | ATTRIBUTE1 | — | — |
| 16 | LocationPEOAttribute10 | ATTRIBUTE10 | — | — |
| 17 | LocationPEOAttribute11 | ATTRIBUTE11 | — | — |
| 18 | LocationPEOAttribute12 | ATTRIBUTE12 | — | — |
| 19 | LocationPEOAttribute13 | ATTRIBUTE13 | — | — |
| 20 | LocationPEOAttribute14 | ATTRIBUTE14 | — | — |
| 21 | LocationPEOAttribute15 | ATTRIBUTE15 | — | — |
| 22 | LocationPEOAttribute16 | ATTRIBUTE16 | — | — |
| 23 | LocationPEOAttribute17 | ATTRIBUTE17 | — | — |
| 24 | LocationPEOAttribute18 | ATTRIBUTE18 | — | — |
| 25 | LocationPEOAttribute19 | ATTRIBUTE19 | — | — |
| 26 | LocationPEOAttribute2 | ATTRIBUTE2 | — | — |
| 27 | LocationPEOAttribute20 | ATTRIBUTE20 | — | — |
| 28 | LocationPEOAttribute21 | ATTRIBUTE21 | — | — |
| 29 | LocationPEOAttribute22 | ATTRIBUTE22 | — | — |
| 30 | LocationPEOAttribute23 | ATTRIBUTE23 | — | — |
| 31 | LocationPEOAttribute24 | ATTRIBUTE24 | — | — |
| 32 | LocationPEOAttribute25 | ATTRIBUTE25 | — | — |
| 33 | LocationPEOAttribute26 | ATTRIBUTE26 | — | — |
| 34 | LocationPEOAttribute27 | ATTRIBUTE27 | — | — |
| 35 | LocationPEOAttribute28 | ATTRIBUTE28 | — | — |
| 36 | LocationPEOAttribute29 | ATTRIBUTE29 | — | — |
| 37 | LocationPEOAttribute3 | ATTRIBUTE3 | — | — |
| 38 | LocationPEOAttribute30 | ATTRIBUTE30 | — | — |
| 39 | LocationPEOAttribute4 | ATTRIBUTE4 | — | — |
| 40 | LocationPEOAttribute5 | ATTRIBUTE5 | — | — |
| 41 | LocationPEOAttribute6 | ATTRIBUTE6 | — | — |
| 42 | LocationPEOAttribute7 | ATTRIBUTE7 | — | — |
| 43 | LocationPEOAttribute8 | ATTRIBUTE8 | — | — |
| 44 | LocationPEOAttribute9 | ATTRIBUTE9 | — | — |
| 45 | LocationPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 46 | LocationPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 47 | LocationPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 48 | LocationPEOAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 49 | LocationPEOAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 50 | LocationPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 51 | LocationPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 52 | LocationPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 53 | LocationPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 54 | LocationPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 55 | LocationPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 56 | LocationPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 57 | LocationPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 58 | LocationPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 59 | LocationPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 60 | LocationPEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 61 | LocationPEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 62 | LocationPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 63 | LocationPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 64 | LocationPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 65 | LocationPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 66 | LocationPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 67 | LocationPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 68 | LocationPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 69 | LocationPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 70 | LocationPEOBuilding | BUILDING | — | — |
| 71 | LocationPEOCity | CITY | — | — |
| 72 | LocationPEOClliCode | CLLI_CODE | — | — |
| 73 | LocationPEOComments | COMMENTS | — | — |
| 74 | LocationPEOCountry | COUNTRY | — | — |
| 75 | LocationPEOCounty | COUNTY | — | — |
| 76 | LocationPEOCreatedBy | CREATED_BY | — | — |
| 77 | LocationPEOCreatedByModule | CREATED_BY_MODULE | — | — |
| 78 | LocationPEOCreationDate | CREATION_DATE | — | — |
| 79 | LocationPEODateValidated | DATE_VALIDATED | — | — |
| 80 | LocationPEODescription | DESCRIPTION | — | — |
| 81 | LocationPEODoNotValidateFlag | DO_NOT_VALIDATE_FLAG | — | — |
| 82 | LocationPEOFaLocationId | FA_LOCATION_ID | — | — |
| 83 | LocationPEOFloorNumber | FLOOR_NUMBER | — | — |
| 84 | LocationPEOGeometryStatusCode | GEOMETRY_STATUS_CODE | — | — |
| 85 | LocationPEOHouseType | HOUSE_TYPE | — | — |
| 86 | LocationPEOInternalFlag | INTERNAL_FLAG | — | — |
| 87 | LocationPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 88 | LocationPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 89 | LocationPEOLanguage | LOCATION_LANGUAGE | — | — |
| 90 | LocationPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 91 | LocationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 92 | LocationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 93 | LocationPEOLatitude | LATITUDE | — | — |
| 94 | LocationPEOLocationDirections | LOCATION_DIRECTIONS | — | — |
| 95 | LocationPEOLocationId | LOCATION_ID | — | — |
| 96 | LocationPEOLongitude | LONGITUDE | — | — |
| 97 | LocationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 98 | LocationPEOOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 99 | LocationPEOPosition | POSITION | — | — |
| 100 | LocationPEOPostalCode | POSTAL_CODE | — | — |
| 101 | LocationPEOPostalPlus4Code | POSTAL_PLUS4_CODE | — | — |
| 102 | LocationPEOProvince | PROVINCE | — | — |
| 103 | LocationPEOSalesTaxGeocode | SALES_TAX_GEOCODE | — | — |
| 104 | LocationPEOSalesTaxInsideCityLimits | SALES_TAX_INSIDE_CITY_LIMITS | — | — |
| 105 | LocationPEOShortDescription | SHORT_DESCRIPTION | — | — |
| 106 | LocationPEOState | STATE | — | — |
| 107 | LocationPEOStatusFlag | STATUS_FLAG | — | — |
| 108 | LocationPEOTimezoneCode | TIMEZONE_CODE | — | — |
| 109 | LocationPEOValidatedFlag | VALIDATED_FLAG | — | — |
| 110 | LocationPEOValidationStatusCode | VALIDATION_STATUS_CODE | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyPEOPartyId | PARTY_ID | — | — |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | Addressee | ADDRESSEE | — | — |
| 3 | Comments | COMMENTS | — | — |
| 4 | CorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 5 | CreatedBy | CREATED_BY | — | — |
| 6 | CreatedByModule | CREATED_BY_MODULE | — | — |
| 7 | CreationDate | CREATION_DATE | — | — |
| 8 | CurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 9 | CurrencyCode | CURRENCY_CODE | — | — |
| 10 | DunsNumberC | DUNS_NUMBER_C | — | — |
| 11 | EndDateActive | END_DATE_ACTIVE | — | ✅ |
| 12 | GlobalLocationNumber | GLOBAL_LOCATION_NUMBER | — | ✅ |
| 13 | IdentifyingAddressFlag | IDENTIFYING_ADDRESS_FLAG | — | ✅ |
| 14 | Language | PARTY_SITE_LANGUAGE | — | — |
| 15 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | LocationId | LOCATION_ID | — | ✅ |
| 19 | Mailstop | MAILSTOP | — | — |
| 20 | OrigSystemReference | ORIG_SYSTEM_REFERENCE | — | ✅ |
| 21 | PartyId | PARTY_ID | — | ✅ |
| 22 | PartyNameDba | PARTY_NAME_DBA | — | — |
| 23 | PartyNameDivision | PARTY_NAME_DIVISION | — | — |
| 24 | PartyNameLegal | PARTY_NAME_LEGAL | — | — |
| 25 | PartySiteId | PARTY_SITE_ID | 🔑 | ✅ |
| 26 | PartySiteName | PARTY_SITE_NAME | — | ✅ |
| 27 | PartySiteNumber | PARTY_SITE_NUMBER | — | ✅ |
| 28 | PartySiteType | PARTY_SITE_TYPE | — | — |
| 29 | PartyUsageCode | PARTY_USAGE_CODE | — | — |
| 30 | RelationshipId | RELATIONSHIP_ID | — | — |
| 31 | StartDateActive | START_DATE_ACTIVE | — | ✅ |
| 32 | Status | STATUS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
