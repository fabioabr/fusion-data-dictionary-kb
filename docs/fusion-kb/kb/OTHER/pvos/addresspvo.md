---
id: DOC-OTHER-PVO-AddressPVO
doc_type: system-doc
title: "AddressPVO — PVO Cross-Module"
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
  - AddressPVO
  - addresspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AddressPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Address. Acessa as tabelas: HZ_LOCATIONS, HZ_PARTY_SITES, HZ_PARTY_SITE_USES.

**Caminho:** `FscmTopModelAM.StudentEnrollmentAM.AddressPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 242 | 3 | 1 | 18 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[hz_locations|HZ_LOCATIONS]] — 110 atributos (11 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 86 atributos (1 PKs, 5 BICC)
- [[hz_party_site_uses|HZ_PARTY_SITE_USES]] — 46 atributos (2 BICC)

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
| 7 | LocationPEOAddress1 | ADDRESS1 | — | ✅ |
| 8 | LocationPEOAddress2 | ADDRESS2 | — | ✅ |
| 9 | LocationPEOAddress3 | ADDRESS3 | — | ✅ |
| 10 | LocationPEOAddress4 | ADDRESS4 | — | ✅ |
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
| 71 | LocationPEOCity | CITY | — | ✅ |
| 72 | LocationPEOClliCode | CLLI_CODE | — | — |
| 73 | LocationPEOComments | COMMENTS | — | — |
| 74 | LocationPEOCountry | COUNTRY | — | ✅ |
| 75 | LocationPEOCounty | COUNTY | — | ✅ |
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
| 95 | LocationPEOLocationId | LOCATION_ID | — | ✅ |
| 96 | LocationPEOLongitude | LONGITUDE | — | — |
| 97 | LocationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 98 | LocationPEOOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 99 | LocationPEOPosition | POSITION | — | — |
| 100 | LocationPEOPostalCode | POSTAL_CODE | — | ✅ |
| 101 | LocationPEOPostalPlus4Code | POSTAL_PLUS4_CODE | — | — |
| 102 | LocationPEOProvince | PROVINCE | — | ✅ |
| 103 | LocationPEOSalesTaxGeocode | SALES_TAX_GEOCODE | — | — |
| 104 | LocationPEOSalesTaxInsideCityLimits | SALES_TAX_INSIDE_CITY_LIMITS | — | — |
| 105 | LocationPEOShortDescription | SHORT_DESCRIPTION | — | — |
| 106 | LocationPEOState | STATE | — | ✅ |
| 107 | LocationPEOStatusFlag | STATUS_FLAG | — | — |
| 108 | LocationPEOTimezoneCode | TIMEZONE_CODE | — | — |
| 109 | LocationPEOValidatedFlag | VALIDATED_FLAG | — | — |
| 110 | LocationPEOValidationStatusCode | VALIDATION_STATUS_CODE | — | — |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartySitePEOActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | PartySitePEOAddressee | ADDRESSEE | — | — |
| 3 | PartySitePEOAttribute1 | ATTRIBUTE1 | — | — |
| 4 | PartySitePEOAttribute10 | ATTRIBUTE10 | — | — |
| 5 | PartySitePEOAttribute11 | ATTRIBUTE11 | — | — |
| 6 | PartySitePEOAttribute12 | ATTRIBUTE12 | — | — |
| 7 | PartySitePEOAttribute13 | ATTRIBUTE13 | — | — |
| 8 | PartySitePEOAttribute14 | ATTRIBUTE14 | — | — |
| 9 | PartySitePEOAttribute15 | ATTRIBUTE15 | — | — |
| 10 | PartySitePEOAttribute16 | ATTRIBUTE16 | — | — |
| 11 | PartySitePEOAttribute17 | ATTRIBUTE17 | — | — |
| 12 | PartySitePEOAttribute18 | ATTRIBUTE18 | — | — |
| 13 | PartySitePEOAttribute19 | ATTRIBUTE19 | — | — |
| 14 | PartySitePEOAttribute2 | ATTRIBUTE2 | — | — |
| 15 | PartySitePEOAttribute20 | ATTRIBUTE20 | — | — |
| 16 | PartySitePEOAttribute21 | ATTRIBUTE21 | — | — |
| 17 | PartySitePEOAttribute22 | ATTRIBUTE22 | — | — |
| 18 | PartySitePEOAttribute23 | ATTRIBUTE23 | — | — |
| 19 | PartySitePEOAttribute24 | ATTRIBUTE24 | — | — |
| 20 | PartySitePEOAttribute25 | ATTRIBUTE25 | — | — |
| 21 | PartySitePEOAttribute26 | ATTRIBUTE26 | — | — |
| 22 | PartySitePEOAttribute27 | ATTRIBUTE27 | — | — |
| 23 | PartySitePEOAttribute28 | ATTRIBUTE28 | — | — |
| 24 | PartySitePEOAttribute29 | ATTRIBUTE29 | — | — |
| 25 | PartySitePEOAttribute3 | ATTRIBUTE3 | — | — |
| 26 | PartySitePEOAttribute30 | ATTRIBUTE30 | — | — |
| 27 | PartySitePEOAttribute4 | ATTRIBUTE4 | — | — |
| 28 | PartySitePEOAttribute5 | ATTRIBUTE5 | — | — |
| 29 | PartySitePEOAttribute6 | ATTRIBUTE6 | — | — |
| 30 | PartySitePEOAttribute7 | ATTRIBUTE7 | — | — |
| 31 | PartySitePEOAttribute8 | ATTRIBUTE8 | — | — |
| 32 | PartySitePEOAttribute9 | ATTRIBUTE9 | — | — |
| 33 | PartySitePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 34 | PartySitePEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 35 | PartySitePEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 36 | PartySitePEOAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 37 | PartySitePEOAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 38 | PartySitePEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 39 | PartySitePEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 40 | PartySitePEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 41 | PartySitePEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 42 | PartySitePEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 43 | PartySitePEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 44 | PartySitePEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 45 | PartySitePEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 46 | PartySitePEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 47 | PartySitePEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 48 | PartySitePEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 49 | PartySitePEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 50 | PartySitePEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 51 | PartySitePEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 52 | PartySitePEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 53 | PartySitePEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 54 | PartySitePEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 55 | PartySitePEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 56 | PartySitePEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 57 | PartySitePEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 58 | PartySitePEOComments | COMMENTS | — | — |
| 59 | PartySitePEOCreatedBy | CREATED_BY | — | — |
| 60 | PartySitePEOCreatedByModule | CREATED_BY_MODULE | — | — |
| 61 | PartySitePEOCreationDate | CREATION_DATE | — | — |
| 62 | PartySitePEODunsNumberC | DUNS_NUMBER_C | — | — |
| 63 | PartySitePEOEndDateActive | END_DATE_ACTIVE | — | — |
| 64 | PartySitePEOGlobalLocationNumber | GLOBAL_LOCATION_NUMBER | — | — |
| 65 | PartySitePEOIdentifyingAddressFlag | IDENTIFYING_ADDRESS_FLAG | — | ✅ |
| 66 | PartySitePEOLanguage | PARTY_SITE_LANGUAGE | — | — |
| 67 | PartySitePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 68 | PartySitePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 69 | PartySitePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 70 | PartySitePEOLocationId | LOCATION_ID | — | — |
| 71 | PartySitePEOMailstop | MAILSTOP | — | — |
| 72 | PartySitePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 73 | PartySitePEOOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 74 | PartySitePEOOverallPrimaryFlag | OVERALL_PRIMARY_FLAG | — | ✅ |
| 75 | PartySitePEOPartyId | PARTY_ID | — | — |
| 76 | PartySitePEOPartyNameDba | PARTY_NAME_DBA | — | — |
| 77 | PartySitePEOPartyNameDivision | PARTY_NAME_DIVISION | — | — |
| 78 | PartySitePEOPartyNameLegal | PARTY_NAME_LEGAL | — | — |
| 79 | PartySitePEOPartySiteId | PARTY_SITE_ID | 🔑 | ✅ |
| 80 | PartySitePEOPartySiteName | PARTY_SITE_NAME | — | ✅ |
| 81 | PartySitePEOPartySiteNumber | PARTY_SITE_NUMBER | — | — |
| 82 | PartySitePEOPartySiteType | PARTY_SITE_TYPE | — | — |
| 83 | PartySitePEOPartyUsageCode | PARTY_USAGE_CODE | — | — |
| 84 | PartySitePEORelationshipId | RELATIONSHIP_ID | — | — |
| 85 | PartySitePEOStartDateActive | START_DATE_ACTIVE | — | — |
| 86 | PartySitePEOStatus | STATUS | — | — |

### [[hz_party_site_uses|HZ_PARTY_SITE_USES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartySiteUsePEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | PartySiteUsePEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | PartySiteUsePEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | PartySiteUsePEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | PartySiteUsePEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | PartySiteUsePEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | PartySiteUsePEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | PartySiteUsePEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | PartySiteUsePEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | PartySiteUsePEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | PartySiteUsePEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | PartySiteUsePEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | PartySiteUsePEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | PartySiteUsePEOAttribute21 | ATTRIBUTE21 | — | — |
| 15 | PartySiteUsePEOAttribute22 | ATTRIBUTE22 | — | — |
| 16 | PartySiteUsePEOAttribute23 | ATTRIBUTE23 | — | — |
| 17 | PartySiteUsePEOAttribute24 | ATTRIBUTE24 | — | — |
| 18 | PartySiteUsePEOAttribute25 | ATTRIBUTE25 | — | — |
| 19 | PartySiteUsePEOAttribute26 | ATTRIBUTE26 | — | — |
| 20 | PartySiteUsePEOAttribute27 | ATTRIBUTE27 | — | — |
| 21 | PartySiteUsePEOAttribute28 | ATTRIBUTE28 | — | — |
| 22 | PartySiteUsePEOAttribute29 | ATTRIBUTE29 | — | — |
| 23 | PartySiteUsePEOAttribute3 | ATTRIBUTE3 | — | — |
| 24 | PartySiteUsePEOAttribute30 | ATTRIBUTE30 | — | — |
| 25 | PartySiteUsePEOAttribute4 | ATTRIBUTE4 | — | — |
| 26 | PartySiteUsePEOAttribute5 | ATTRIBUTE5 | — | — |
| 27 | PartySiteUsePEOAttribute6 | ATTRIBUTE6 | — | — |
| 28 | PartySiteUsePEOAttribute7 | ATTRIBUTE7 | — | — |
| 29 | PartySiteUsePEOAttribute8 | ATTRIBUTE8 | — | — |
| 30 | PartySiteUsePEOAttribute9 | ATTRIBUTE9 | — | — |
| 31 | PartySiteUsePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 32 | PartySiteUsePEOBeginDate | BEGIN_DATE | — | — |
| 33 | PartySiteUsePEOComments | COMMENTS | — | — |
| 34 | PartySiteUsePEOCreatedBy | CREATED_BY | — | — |
| 35 | PartySiteUsePEOCreatedByModule | CREATED_BY_MODULE | — | — |
| 36 | PartySiteUsePEOCreationDate | CREATION_DATE | — | — |
| 37 | PartySiteUsePEOEndDate | END_DATE | — | — |
| 38 | PartySiteUsePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 39 | PartySiteUsePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 40 | PartySiteUsePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 41 | PartySiteUsePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 42 | PartySiteUsePEOPartySiteId | PARTY_SITE_ID | — | — |
| 43 | PartySiteUsePEOPartySiteUseId | PARTY_SITE_USE_ID | — | ✅ |
| 44 | PartySiteUsePEOPrimaryPerType | PRIMARY_PER_TYPE | — | — |
| 45 | PartySiteUsePEOSiteUseType | SITE_USE_TYPE | — | ✅ |
| 46 | PartySiteUsePEOStatus | STATUS | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
