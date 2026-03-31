---
id: DOC-OTHER-PVO-PSCParcelOwnerPVO
doc_type: system-doc
title: "PSCParcelOwnerPVO — PVO Cross-Module"
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
  - PSCParcelOwnerPVO
  - pscparcelownerpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PSCParcelOwnerPVO

## 📌 Visão Geral

View Object para extração BICC de dados de PSCParcel Owner. Acessa as tabelas: PSC_LNP_PARCEL_OWNER.

**Caminho:** `FscmTopModelAM.PscPermitsReportingAM.PSCParcelOwnerPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 50 | 1 | 1 | 40 | 80% |

---

## 🔗 Tabelas Relacionadas

- [[psc_lnp_parcel_owner|PSC_LNP_PARCEL_OWNER]] — 50 atributos (1 PKs, 40 BICC)

---

## ⚙️ Atributos

### [[psc_lnp_parcel_owner|PSC_LNP_PARCEL_OWNER]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ParcelOwnerPEOAddress1 | ADDRESS1 | — | ✅ |
| 2 | ParcelOwnerPEOAddress2 | ADDRESS2 | — | ✅ |
| 3 | ParcelOwnerPEOAddress3 | ADDRESS3 | — | ✅ |
| 4 | ParcelOwnerPEOAddress4 | ADDRESS4 | — | ✅ |
| 5 | ParcelOwnerPEOAddressField1 | ADDRESS_FIELD1 | — | ✅ |
| 6 | ParcelOwnerPEOAddressField2 | ADDRESS_FIELD2 | — | ✅ |
| 7 | ParcelOwnerPEOAddressField3 | ADDRESS_FIELD3 | — | ✅ |
| 8 | ParcelOwnerPEOAgencyId | AGENCY_ID | — | — |
| 9 | ParcelOwnerPEOBuildingType | BUILDING_TYPE | — | ✅ |
| 10 | ParcelOwnerPEOCellPhoneCountry | CELL_PHONE_COUNTRY | — | ✅ |
| 11 | ParcelOwnerPEOCellPhoneNum | CELL_PHONE_NUM | — | ✅ |
| 12 | ParcelOwnerPEOCity | CITY | — | ✅ |
| 13 | ParcelOwnerPEOCountry | COUNTRY | — | ✅ |
| 14 | ParcelOwnerPEOCounty | COUNTY | — | — |
| 15 | ParcelOwnerPEOCreatedBy | CREATED_BY | — | ✅ |
| 16 | ParcelOwnerPEOCreationDate | CREATION_DATE | — | ✅ |
| 17 | ParcelOwnerPEODocumentNum | DOCUMENT_NUM | — | ✅ |
| 18 | ParcelOwnerPEOEmailId | EMAIL_ID | — | ✅ |
| 19 | ParcelOwnerPEOFaxCountry | FAX_COUNTRY | — | ✅ |
| 20 | ParcelOwnerPEOFaxNum | FAX_NUM | — | ✅ |
| 21 | ParcelOwnerPEOFloor | FLOOR | — | ✅ |
| 22 | ParcelOwnerPEOHomePhoneCountry | HOME_PHONE_COUNTRY | — | ✅ |
| 23 | ParcelOwnerPEOHomePhoneNum | HOME_PHONE_NUM | — | ✅ |
| 24 | ParcelOwnerPEOLastTransferDate | LAST_TRANSFER_DATE | — | ✅ |
| 25 | ParcelOwnerPEOLastTransferType | LAST_TRANSFER_TYPE | — | ✅ |
| 26 | ParcelOwnerPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 27 | ParcelOwnerPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 28 | ParcelOwnerPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 29 | ParcelOwnerPEOLnpRecordId | LNP_RECORD_ID | — | — |
| 30 | ParcelOwnerPEOLnpRecordKey | LNP_RECORD_KEY | — | — |
| 31 | ParcelOwnerPEOName1 | NAME1 | — | ✅ |
| 32 | ParcelOwnerPEOName2 | NAME2 | — | ✅ |
| 33 | ParcelOwnerPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 34 | ParcelOwnerPEOOwnerId | OWNER_ID | — | ✅ |
| 35 | ParcelOwnerPEOOwnerKey | OWNER_KEY | 🔑 | ✅ |
| 36 | ParcelOwnerPEOOwnerType | OWNER_TYPE | — | ✅ |
| 37 | ParcelOwnerPEOParcelId | PARCEL_ID | — | — |
| 38 | ParcelOwnerPEOParcelKey | PARCEL_KEY | — | — |
| 39 | ParcelOwnerPEOPostalCode | POSTAL_CODE | — | ✅ |
| 40 | ParcelOwnerPEOPostalPlus4Code | POSTAL_PLUS4_CODE | — | — |
| 41 | ParcelOwnerPEOPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 42 | ParcelOwnerPEOProvince | PROVINCE | — | — |
| 43 | ParcelOwnerPEOState | STATE | — | ✅ |
| 44 | ParcelOwnerPEOStreetDirection | STREET_DIRECTION | — | ✅ |
| 45 | ParcelOwnerPEOStreetName | STREET_NAME | — | ✅ |
| 46 | ParcelOwnerPEOStreetNumber | STREET_NUMBER | — | ✅ |
| 47 | ParcelOwnerPEOStreetType | STREET_TYPE | — | ✅ |
| 48 | ParcelOwnerPEOUnitNumber | UNIT_NUMBER | — | ✅ |
| 49 | ParcelOwnerPEOWorkPhoneCountry | WORK_PHONE_COUNTRY | — | ✅ |
| 50 | ParcelOwnerPEOWorkPhoneNum | WORK_PHONE_NUM | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
