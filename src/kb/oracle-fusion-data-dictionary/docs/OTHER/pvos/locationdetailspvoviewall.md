---
id: DOC-OTHER-PVO-LocationDetailsPVOViewAll
doc_type: system-doc
title: "LocationDetailsPVOViewAll — PVO Cross-Module"
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
  - LocationDetailsPVOViewAll
  - locationdetailspvoviewall
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LocationDetailsPVOViewAll

## 📌 Visão Geral

View Object para extração BICC de dados de Location Details View All. Acessa as tabelas: PER_LOCATION_DETAILS_F_VL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.LocationAM.LocationDetailsPVOViewAll`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 47 | 1 | 3 | 5 | 11% |

---

## 🔗 Tabelas Relacionadas

- [[per_location_details_f_vl|PER_LOCATION_DETAILS_F_VL]] — 47 atributos (3 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[per_location_details_f_vl|PER_LOCATION_DETAILS_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcLocationCode | AC_LOCATION_CODE | — | — |
| 2 | Description | DESCRIPTION | — | — |
| 3 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 4 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 5 | LocationCode | LOCATION_CODE | — | — |
| 6 | LocationDetailsId | LOCATION_DETAILS_ID | 🔑 | ✅ |
| 7 | LocationDetailsPEOActiveStatus | ACTIVE_STATUS | — | — |
| 8 | LocationDetailsPEOAnnualWorkingDurationUnits | ANNUAL_WORKING_DURATION_UNITS | — | — |
| 9 | LocationDetailsPEOBillToSiteFlag | BILL_TO_SITE_FLAG | — | — |
| 10 | LocationDetailsPEOBusinessGroupId | business_group_id | — | — |
| 11 | LocationDetailsPEOCreatedBy | CREATED_BY | — | — |
| 12 | LocationDetailsPEOCreationDate | CREATION_DATE | — | — |
| 13 | LocationDetailsPEODesignatedReceiverId | DESIGNATED_RECEIVER_ID | — | — |
| 14 | LocationDetailsPEOEmailAddress | EMAIL_ADDRESS | — | — |
| 15 | LocationDetailsPEOFaxAreaCode2 | FAX_AREA_CODE2 | — | — |
| 16 | LocationDetailsPEOFaxCountryCode2 | FAX_COUNTRY_CODE2 | — | — |
| 17 | LocationDetailsPEOFaxExtension2 | FAX_EXTENSION2 | — | — |
| 18 | LocationDetailsPEOFaxSubscriberNum2 | FAX_SUBSCRIBER_NUM2 | — | — |
| 19 | LocationDetailsPEOGeoHierarchyNodeId | GEO_HIERARCHY_NODE_ID | — | — |
| 20 | LocationDetailsPEOGeoHierarchyNodeValue | GEO_HIERARCHY_NODE_VALUE | — | — |
| 21 | LocationDetailsPEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 22 | LocationDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | LocationDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 24 | LocationDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 25 | LocationDetailsPEOLocationId | LOCATION_ID | — | — |
| 26 | LocationDetailsPEOMainAddressId | MAIN_ADDRESS_ID | — | — |
| 27 | LocationDetailsPEOMainphoneAreaCode1 | MAINPHONE_AREA_CODE1 | — | — |
| 28 | LocationDetailsPEOMainphoneCountryCode1 | MAINPHONE_COUNTRY_CODE1 | — | — |
| 29 | LocationDetailsPEOMainphoneExtension1 | MAINPHONE_EXTENSION1 | — | — |
| 30 | LocationDetailsPEOMainphoneSubscriberNum1 | MAINPHONE_SUBSCRIBER_NUM1 | — | — |
| 31 | LocationDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 32 | LocationDetailsPEOOfficeSiteFlag | OFFICE_SITE_FLAG | — | — |
| 33 | LocationDetailsPEOOfficialLanguageCode | OFFICIAL_LANGUAGE_CODE | — | — |
| 34 | LocationDetailsPEOOtherphoneAreaCode3 | OTHERPHONE_AREA_CODE3 | — | — |
| 35 | LocationDetailsPEOOtherphoneCountryCode3 | OTHERPHONE_COUNTRY_CODE3 | — | — |
| 36 | LocationDetailsPEOOtherphoneExtension3 | OTHERPHONE_EXTENSION3 | — | — |
| 37 | LocationDetailsPEOOtherphoneSubscriberNum3 | OTHERPHONE_SUBSCRIBER_NUM3 | — | — |
| 38 | LocationDetailsPEOReceivingSiteFlag | RECEIVING_SITE_FLAG | — | — |
| 39 | LocationDetailsPEOShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 40 | LocationDetailsPEOShipToSiteFlag | SHIP_TO_SITE_FLAG | — | — |
| 41 | LocationDetailsPEOStandardWorkingFrequency | STANDARD_WORKING_FREQUENCY | — | — |
| 42 | LocationDetailsPEOStandardWorkingHours | STANDARD_WORKING_HOURS | — | — |
| 43 | LocationDetailsPEOStdAnnualWorkingDuration | STD_ANNUAL_WORKING_DURATION | — | — |
| 44 | LocationDetailsPEOTelephoneNumber1 | TELEPHONE_NUMBER_1 | — | — |
| 45 | LocationDetailsPEOTelephoneNumber2 | TELEPHONE_NUMBER_2 | — | — |
| 46 | LocationDetailsPEOTelephoneNumber3 | TELEPHONE_NUMBER_3 | — | — |
| 47 | LocationName | LOCATION_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
