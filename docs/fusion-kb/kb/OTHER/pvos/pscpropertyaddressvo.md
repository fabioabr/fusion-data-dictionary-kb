---
id: DOC-OTHER-PVO-PSCPropertyAddressVO
doc_type: system-doc
title: "PSCPropertyAddressVO — PVO Cross-Module"
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
  - PSCPropertyAddressVO
  - pscpropertyaddressvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PSCPropertyAddressVO

## 📌 Visão Geral

View Object para extração BICC de dados de PSCProperty Address VO. Acessa as tabelas: PSC_COM_PARCEL_ADDRESS.

**Caminho:** `FscmTopModelAM.PscPermitsReportingAM.PSCPropertyAddressVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 51 | 1 | 2 | 42 | 82% |

---

## 🔗 Tabelas Relacionadas

- [[psc_com_parcel_address|PSC_COM_PARCEL_ADDRESS]] — 51 atributos (2 PKs, 42 BICC)

---

## ⚙️ Atributos

### [[psc_com_parcel_address|PSC_COM_PARCEL_ADDRESS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PropertyParcelAddressPEOAddress1 | ADDRESS1 | — | ✅ |
| 2 | PropertyParcelAddressPEOAddress2 | ADDRESS2 | — | ✅ |
| 3 | PropertyParcelAddressPEOAddress3 | ADDRESS3 | — | ✅ |
| 4 | PropertyParcelAddressPEOAddress4 | ADDRESS4 | — | ✅ |
| 5 | PropertyParcelAddressPEOAddressCode | ADDRESS_CODE | — | ✅ |
| 6 | PropertyParcelAddressPEOAddressField1 | ADDRESS_FIELD1 | — | ✅ |
| 7 | PropertyParcelAddressPEOAddressField2 | ADDRESS_FIELD2 | — | ✅ |
| 8 | PropertyParcelAddressPEOAddressField3 | ADDRESS_FIELD3 | — | ✅ |
| 9 | PropertyParcelAddressPEOAddressId | ADDRESS_ID | 🔑 | ✅ |
| 10 | PropertyParcelAddressPEOAddressType | ADDRESS_TYPE | — | ✅ |
| 11 | PropertyParcelAddressPEOBuildingType | BUILDING_TYPE | — | ✅ |
| 12 | PropertyParcelAddressPEOCellPhoneCountry | CELL_PHONE_COUNTRY | — | ✅ |
| 13 | PropertyParcelAddressPEOCellPhoneNum | CELL_PHONE_NUM | — | ✅ |
| 14 | PropertyParcelAddressPEOCity | CITY | — | ✅ |
| 15 | PropertyParcelAddressPEOCoordinateX | COORDINATE_X | — | — |
| 16 | PropertyParcelAddressPEOCoordinateY | COORDINATE_Y | — | — |
| 17 | PropertyParcelAddressPEOCountry | COUNTRY | — | ✅ |
| 18 | PropertyParcelAddressPEOCounty | COUNTY | — | ✅ |
| 19 | PropertyParcelAddressPEOCreatedBy | CREATED_BY | — | — |
| 20 | PropertyParcelAddressPEOCreationDate | CREATION_DATE | — | — |
| 21 | PropertyParcelAddressPEOEmailId | EMAIL_ID | — | ✅ |
| 22 | PropertyParcelAddressPEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 23 | PropertyParcelAddressPEOFaxCountry | FAX_COUNTRY | — | ✅ |
| 24 | PropertyParcelAddressPEOFaxNum | FAX_NUM | — | ✅ |
| 25 | PropertyParcelAddressPEOFloor | FLOOR | — | ✅ |
| 26 | PropertyParcelAddressPEOHomePhoneCountry | HOME_PHONE_COUNTRY | — | ✅ |
| 27 | PropertyParcelAddressPEOHomePhoneNum | HOME_PHONE_NUM | — | ✅ |
| 28 | PropertyParcelAddressPEOInputSource | INPUT_SOURCE | — | — |
| 29 | PropertyParcelAddressPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | PropertyParcelAddressPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 31 | PropertyParcelAddressPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 32 | PropertyParcelAddressPEOLatitude | LATITUDE | — | ✅ |
| 33 | PropertyParcelAddressPEOLongitude | LONGITUDE | — | ✅ |
| 34 | PropertyParcelAddressPEOMunicipalityId | MUNICIPALITY_ID | — | ✅ |
| 35 | PropertyParcelAddressPEOName1 | NAME1 | — | ✅ |
| 36 | PropertyParcelAddressPEOName2 | NAME2 | — | ✅ |
| 37 | PropertyParcelAddressPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 38 | PropertyParcelAddressPEOParcelId | PARCEL_ID | 🔑 | ✅ |
| 39 | PropertyParcelAddressPEOPostalCode | POSTAL_CODE | — | ✅ |
| 40 | PropertyParcelAddressPEOPostalPlus4Code | POSTAL_PLUS4_CODE | — | ✅ |
| 41 | PropertyParcelAddressPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 42 | PropertyParcelAddressPEOProvince | PROVINCE | — | ✅ |
| 43 | PropertyParcelAddressPEOSrid | SRID | — | — |
| 44 | PropertyParcelAddressPEOState | STATE | — | ✅ |
| 45 | PropertyParcelAddressPEOStreeName | STREE_NAME | — | ✅ |
| 46 | PropertyParcelAddressPEOStreetDirection | STREET_DIRECTION | — | ✅ |
| 47 | PropertyParcelAddressPEOStreetNumber | STREET_NUMBER | — | ✅ |
| 48 | PropertyParcelAddressPEOStreetType | STREET_TYPE | — | ✅ |
| 49 | PropertyParcelAddressPEOUnitNumber | UNIT_NUMBER | — | ✅ |
| 50 | PropertyParcelAddressPEOWorkPhoneCountry | WORK_PHONE_COUNTRY | — | ✅ |
| 51 | PropertyParcelAddressPEOWorkPhoneNum | WORK_PHONE_NUM | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
