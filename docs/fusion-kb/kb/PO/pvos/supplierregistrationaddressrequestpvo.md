---
id: DOC-PO-PVO-SupplierRegistrationAddressRequestPVO
doc_type: system-doc
title: "SupplierRegistrationAddressRequestPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - SupplierRegistrationAddressRequestPVO
  - supplierregistrationaddressrequestpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierRegistrationAddressRequestPVO

## 📌 Visão Geral

Extrai as solicitações de endereço no registro de novos fornecedores, com dados informados durante o onboarding. Suporta validação de dados iniciais e fluxo de cadastramento.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierRegistrationAddressRequestPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 43 | 2 | 1 | 22 | 51% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_territories_vl|FND_TERRITORIES_VL]] — 2 atributos (1 BICC)
- [[poz_address_requests|POZ_ADDRESS_REQUESTS]] — 41 atributos (1 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[fnd_territories_vl|FND_TERRITORIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TerritoryTerritoryCode | TERRITORY_CODE | — | — |
| 2 | TerritoryTerritoryShortName | TERRITORY_SHORT_NAME | — | ✅ |

### [[poz_address_requests|POZ_ADDRESS_REQUESTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddressRequestId | ADDRESS_REQUEST_ID | 🔑 | ✅ |
| 2 | SupplierRegAddressRequestAddressLine1 | ADDRESS_LINE1 | — | ✅ |
| 3 | SupplierRegAddressRequestAddressLine2 | ADDRESS_LINE2 | — | ✅ |
| 4 | SupplierRegAddressRequestAddressLine3 | ADDRESS_LINE3 | — | ✅ |
| 5 | SupplierRegAddressRequestAddressLine4 | ADDRESS_LINE4 | — | ✅ |
| 6 | SupplierRegAddressRequestAddressLinesPhonetic | ADDRESS_LINES_PHONETIC | — | — |
| 7 | SupplierRegAddressRequestBuilding | BUILDING | — | — |
| 8 | SupplierRegAddressRequestCity | CITY | — | ✅ |
| 9 | SupplierRegAddressRequestCountry | COUNTRY | — | — |
| 10 | SupplierRegAddressRequestCounty | COUNTY | — | ✅ |
| 11 | SupplierRegAddressRequestCreatedBy | CREATED_BY | — | — |
| 12 | SupplierRegAddressRequestCreationDate | CREATION_DATE | — | — |
| 13 | SupplierRegAddressRequestEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 14 | SupplierRegAddressRequestEndDateActive | END_DATE_ACTIVE | — | — |
| 15 | SupplierRegAddressRequestFaxAreaCode | FAX_AREA_CODE | — | ✅ |
| 16 | SupplierRegAddressRequestFaxCountryCode | FAX_COUNTRY_CODE | — | ✅ |
| 17 | SupplierRegAddressRequestFaxNumber | FAX_NUMBER | — | ✅ |
| 18 | SupplierRegAddressRequestFloorNumber | FLOOR_NUMBER | — | — |
| 19 | SupplierRegAddressRequestHasBackingDoc | HAS_BACKING_DOC | — | — |
| 20 | SupplierRegAddressRequestLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | SupplierRegAddressRequestLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 22 | SupplierRegAddressRequestLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 23 | SupplierRegAddressRequestMappingId | MAPPING_ID | — | — |
| 24 | SupplierRegAddressRequestObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 25 | SupplierRegAddressRequestPartySiteId | PARTY_SITE_ID | — | — |
| 26 | SupplierRegAddressRequestPartySiteName | PARTY_SITE_NAME | — | ✅ |
| 27 | SupplierRegAddressRequestPayFlag | PAY_FLAG | — | ✅ |
| 28 | SupplierRegAddressRequestPhoneAreaCode | PHONE_AREA_CODE | — | ✅ |
| 29 | SupplierRegAddressRequestPhoneCountryCode | PHONE_COUNTRY_CODE | — | ✅ |
| 30 | SupplierRegAddressRequestPhoneExtension | PHONE_EXTENSION | — | — |
| 31 | SupplierRegAddressRequestPhoneNumber | PHONE_NUMBER | — | ✅ |
| 32 | SupplierRegAddressRequestPostalCode | POSTAL_CODE | — | ✅ |
| 33 | SupplierRegAddressRequestPostalPlus4Code | POSTAL_PLUS4_CODE | — | — |
| 34 | SupplierRegAddressRequestPrimaryPayFlag | PRIMARY_PAY_FLAG | — | — |
| 35 | SupplierRegAddressRequestProvince | PROVINCE | — | — |
| 36 | SupplierRegAddressRequestPurFlag | PUR_FLAG | — | ✅ |
| 37 | SupplierRegAddressRequestRequestStatus | REQUEST_STATUS | — | — |
| 38 | SupplierRegAddressRequestRequestType | REQUEST_TYPE | — | — |
| 39 | SupplierRegAddressRequestRequestedStartDate | REQUESTED_START_DATE | — | — |
| 40 | SupplierRegAddressRequestRfqFlag | RFQ_FLAG | — | ✅ |
| 41 | SupplierRegAddressRequestState | STATE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
