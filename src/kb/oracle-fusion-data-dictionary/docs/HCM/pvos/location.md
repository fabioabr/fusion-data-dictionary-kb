---
id: DOC-HCM-PVO-Location
doc_type: system-doc
title: "Location — PVO Human Capital Management"
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
  - Location
  - location
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Location

## 📌 Visão Geral

Disponibiliza o cadastro de localizações com endereço completo (logradouro, cidade, CEP). Tabela de referência para endereçamento no HCM.

**Caminho:** `FscmTopModelAM.PartiesAnalyticsAM.Location`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 48 | 1 | 1 | 20 | 42% |

---

## 🔗 Tabelas Relacionadas

- [[hz_locations|HZ_LOCATIONS]] — 48 atributos (1 PKs, 20 BICC)

---

## ⚙️ Atributos

### [[hz_locations|HZ_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddrElementAttribute1 | ADDR_ELEMENT_ATTRIBUTE1 | — | — |
| 2 | AddrElementAttribute2 | ADDR_ELEMENT_ATTRIBUTE2 | — | — |
| 3 | AddrElementAttribute3 | ADDR_ELEMENT_ATTRIBUTE3 | — | — |
| 4 | AddrElementAttribute4 | ADDR_ELEMENT_ATTRIBUTE4 | — | — |
| 5 | AddrElementAttribute5 | ADDR_ELEMENT_ATTRIBUTE5 | — | — |
| 6 | Address1 | ADDRESS1 | — | ✅ |
| 7 | Address2 | ADDRESS2 | — | ✅ |
| 8 | Address3 | ADDRESS3 | — | ✅ |
| 9 | Address4 | ADDRESS4 | — | ✅ |
| 10 | AddressEffectiveDate | ADDRESS_EFFECTIVE_DATE | — | — |
| 11 | AddressExpirationDate | ADDRESS_EXPIRATION_DATE | — | — |
| 12 | AddressLinesPhonetic | ADDRESS_LINES_PHONETIC | — | — |
| 13 | AddressStyle | ADDRESS_STYLE | — | — |
| 14 | Building | BUILDING | — | — |
| 15 | City | CITY | — | ✅ |
| 16 | ClliCode | CLLI_CODE | — | — |
| 17 | Comments | COMMENTS | — | — |
| 18 | Country | COUNTRY | — | ✅ |
| 19 | County | COUNTY | — | ✅ |
| 20 | CreatedBy | CREATED_BY | — | — |
| 21 | CreatedByModule | CREATED_BY_MODULE | — | — |
| 22 | CreationDate | CREATION_DATE | — | — |
| 23 | DateValidated | DATE_VALIDATED | — | — |
| 24 | Description | DESCRIPTION | — | ✅ |
| 25 | DoNotValidateFlag | DO_NOT_VALIDATE_FLAG | — | — |
| 26 | FaLocationId | FA_LOCATION_ID | — | — |
| 27 | FloorNumber | FLOOR_NUMBER | — | — |
| 28 | HouseType | HOUSE_TYPE | — | — |
| 29 | InternalFlag | INTERNAL_FLAG | — | — |
| 30 | Language | LOCATION_LANGUAGE | — | ✅ |
| 31 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 32 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 33 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 34 | LocationDirections | LOCATION_DIRECTIONS | — | — |
| 35 | LocationId | LOCATION_ID | 🔑 | ✅ |
| 36 | OrigSystemReference | ORIG_SYSTEM_REFERENCE | — | ✅ |
| 37 | Position | POSITION | — | — |
| 38 | PostalCode | POSTAL_CODE | — | ✅ |
| 39 | PostalPlus4Code | POSTAL_PLUS4_CODE | — | — |
| 40 | Province | PROVINCE | — | ✅ |
| 41 | SalesTaxGeocode | SALES_TAX_GEOCODE | — | ✅ |
| 42 | SalesTaxInsideCityLimits | SALES_TAX_INSIDE_CITY_LIMITS | — | ✅ |
| 43 | ShortDescription | SHORT_DESCRIPTION | — | ✅ |
| 44 | State | STATE | — | ✅ |
| 45 | StatusFlag | STATUS_FLAG | — | ✅ |
| 46 | TimezoneCode | TIMEZONE_CODE | — | ✅ |
| 47 | ValidatedFlag | VALIDATED_FLAG | — | — |
| 48 | ValidationStatusCode | VALIDATION_STATUS_CODE | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
