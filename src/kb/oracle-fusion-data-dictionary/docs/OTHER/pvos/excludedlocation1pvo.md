---
id: DOC-OTHER-PVO-ExcludedLocation1PVO
doc_type: system-doc
title: "ExcludedLocation1PVO — PVO Cross-Module"
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
  - ExcludedLocation1PVO
  - excludedlocation1pvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExcludedLocation1PVO

## 📌 Visão Geral

View Object para extração BICC de dados de Excluded Location1. Acessa as tabelas: PER_LOCATIONS, PER_LOCATION_DETAILS_F_TL, PER_LOCATION_DETAILS_F_VL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.ExcludedLocation1PVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 56 | 3 | 4 | 9 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[per_locations|PER_LOCATIONS]] — 12 atributos (1 PKs, 2 BICC)
- [[per_location_details_f_tl|PER_LOCATION_DETAILS_F_TL]] — 10 atributos (1 PKs, 4 BICC)
- [[per_location_details_f_vl|PER_LOCATION_DETAILS_F_VL]] — 34 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[per_locations|PER_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | LocationPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 7 | LocationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 8 | LocationPEOInternalLocationCode | INTERNAL_LOCATION_CODE | — | — |
| 9 | LocationPEOLocationId | LOCATION_ID | 🔑 | ✅ |
| 10 | LocationPEOLocationImageUrl | LOCATION_IMAGE_URL | — | — |
| 11 | LocationPEOSetId | SET_ID | — | — |
| 12 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[per_location_details_f_tl|PER_LOCATION_DETAILS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocationDetailsTranslationPEOAcLocationCode | AC_LOCATION_CODE | — | — |
| 2 | LocationDetailsTranslationPEODescription | DESCRIPTION | — | — |
| 3 | LocationDetailsTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | LocationDetailsTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | LocationDetailsTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | LocationDetailsTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LocationDetailsTranslationPEOLocationCode | LOCATION_CODE | — | — |
| 8 | LocationDetailsTranslationPEOLocationDetailsId | LOCATION_DETAILS_ID | — | — |
| 9 | LocationDetailsTranslationPEOLocationName | LOCATION_NAME | — | ✅ |
| 10 | LocationDetailsTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[per_location_details_f_vl|PER_LOCATION_DETAILS_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocationDetailsPEOActiveStatus | ACTIVE_STATUS | — | — |
| 2 | LocationDetailsPEOBillToSiteFlag | BILL_TO_SITE_FLAG | — | — |
| 3 | LocationDetailsPEOBusinessGroupId | business_group_id | — | — |
| 4 | LocationDetailsPEODesignatedReceiverId | DESIGNATED_RECEIVER_ID | — | — |
| 5 | LocationDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 6 | LocationDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 7 | LocationDetailsPEOEmailAddress | EMAIL_ADDRESS | — | — |
| 8 | LocationDetailsPEOFaxAreaCode2 | FAX_AREA_CODE2 | — | — |
| 9 | LocationDetailsPEOFaxCountryCode2 | FAX_COUNTRY_CODE2 | — | — |
| 10 | LocationDetailsPEOFaxExtension2 | FAX_EXTENSION2 | — | — |
| 11 | LocationDetailsPEOFaxSubscriberNum2 | FAX_SUBSCRIBER_NUM2 | — | — |
| 12 | LocationDetailsPEOGeoHierarchyNodeId | GEO_HIERARCHY_NODE_ID | — | — |
| 13 | LocationDetailsPEOGeoHierarchyNodeValue | GEO_HIERARCHY_NODE_VALUE | — | — |
| 14 | LocationDetailsPEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 15 | LocationDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | LocationDetailsPEOLocationDetailsId | LOCATION_DETAILS_ID | — | — |
| 17 | LocationDetailsPEOLocationId | LOCATION_ID | — | — |
| 18 | LocationDetailsPEOMainAddressId | MAIN_ADDRESS_ID | — | — |
| 19 | LocationDetailsPEOMainphoneAreaCode1 | MAINPHONE_AREA_CODE1 | — | — |
| 20 | LocationDetailsPEOMainphoneCountryCode1 | MAINPHONE_COUNTRY_CODE1 | — | — |
| 21 | LocationDetailsPEOMainphoneExtension1 | MAINPHONE_EXTENSION1 | — | — |
| 22 | LocationDetailsPEOMainphoneSubscriberNum1 | MAINPHONE_SUBSCRIBER_NUM1 | — | — |
| 23 | LocationDetailsPEOOfficeSiteFlag | OFFICE_SITE_FLAG | — | — |
| 24 | LocationDetailsPEOOfficialLanguageCode | OFFICIAL_LANGUAGE_CODE | — | — |
| 25 | LocationDetailsPEOOtherphoneAreaCode3 | OTHERPHONE_AREA_CODE3 | — | — |
| 26 | LocationDetailsPEOOtherphoneCountryCode3 | OTHERPHONE_COUNTRY_CODE3 | — | — |
| 27 | LocationDetailsPEOOtherphoneExtension3 | OTHERPHONE_EXTENSION3 | — | — |
| 28 | LocationDetailsPEOOtherphoneSubscriberNum3 | OTHERPHONE_SUBSCRIBER_NUM3 | — | — |
| 29 | LocationDetailsPEOReceivingSiteFlag | RECEIVING_SITE_FLAG | — | — |
| 30 | LocationDetailsPEOShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 31 | LocationDetailsPEOShipToSiteFlag | SHIP_TO_SITE_FLAG | — | — |
| 32 | LocationDetailsPEOTelephoneNumber1 | TELEPHONE_NUMBER_1 | — | — |
| 33 | LocationDetailsPEOTelephoneNumber2 | TELEPHONE_NUMBER_2 | — | — |
| 34 | LocationDetailsPEOTelephoneNumber3 | TELEPHONE_NUMBER_3 | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
