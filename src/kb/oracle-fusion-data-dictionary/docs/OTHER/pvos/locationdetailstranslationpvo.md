---
id: DOC-OTHER-PVO-LocationDetailsTranslationPVO
doc_type: system-doc
title: "LocationDetailsTranslationPVO — PVO Cross-Module"
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
  - LocationDetailsTranslationPVO
  - locationdetailstranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LocationDetailsTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Location Details Translation. Acessa as tabelas: PER_LOCATION_DETAILS_F_TL, PER_LOCATION_DETAILS_F_VL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.LocationAM.LocationDetailsTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 54 | 2 | 2 | 16 | 30% |

---

## 🔗 Tabelas Relacionadas

- [[per_location_details_f_tl|PER_LOCATION_DETAILS_F_TL]] — 15 atributos (2 PKs, 12 BICC)
- [[per_location_details_f_vl|PER_LOCATION_DETAILS_F_VL]] — 39 atributos (4 BICC)

---

## ⚙️ Atributos

### [[per_location_details_f_tl|PER_LOCATION_DETAILS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | Language | LANGUAGE | 🔑 | ✅ |
| 4 | LocationDetailsId | LOCATION_DETAILS_ID | 🔑 | ✅ |
| 5 | LocationDetailsTranslationPEOAcLocationCode | AC_LOCATION_CODE | — | — |
| 6 | LocationDetailsTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | LocationDetailsTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | LocationDetailsTranslationPEODescription | DESCRIPTION | — | ✅ |
| 9 | LocationDetailsTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LocationDetailsTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | LocationDetailsTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | LocationDetailsTranslationPEOLocationCode | LOCATION_CODE | — | ✅ |
| 13 | LocationDetailsTranslationPEOLocationName | LOCATION_NAME | — | ✅ |
| 14 | LocationDetailsTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | LocationDetailsTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

### [[per_location_details_f_vl|PER_LOCATION_DETAILS_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocationDetailsPEOActiveStatus | ACTIVE_STATUS | — | — |
| 2 | LocationDetailsPEOBillToSiteFlag | BILL_TO_SITE_FLAG | — | — |
| 3 | LocationDetailsPEOBusinessGroupId | business_group_id | — | — |
| 4 | LocationDetailsPEOCreatedBy | CREATED_BY | — | — |
| 5 | LocationDetailsPEOCreationDate | CREATION_DATE | — | — |
| 6 | LocationDetailsPEODesignatedReceiverId | DESIGNATED_RECEIVER_ID | — | — |
| 7 | LocationDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | LocationDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 9 | LocationDetailsPEOEmailAddress | EMAIL_ADDRESS | — | — |
| 10 | LocationDetailsPEOFaxAreaCode2 | FAX_AREA_CODE2 | — | — |
| 11 | LocationDetailsPEOFaxCountryCode2 | FAX_COUNTRY_CODE2 | — | — |
| 12 | LocationDetailsPEOFaxExtension2 | FAX_EXTENSION2 | — | — |
| 13 | LocationDetailsPEOFaxSubscriberNum2 | FAX_SUBSCRIBER_NUM2 | — | — |
| 14 | LocationDetailsPEOGeoHierarchyNodeId | GEO_HIERARCHY_NODE_ID | — | — |
| 15 | LocationDetailsPEOGeoHierarchyNodeValue | GEO_HIERARCHY_NODE_VALUE | — | — |
| 16 | LocationDetailsPEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 17 | LocationDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | LocationDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | LocationDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | LocationDetailsPEOLocationDetailsId | LOCATION_DETAILS_ID | — | — |
| 21 | LocationDetailsPEOLocationId | LOCATION_ID | — | ✅ |
| 22 | LocationDetailsPEOMainAddressId | MAIN_ADDRESS_ID | — | — |
| 23 | LocationDetailsPEOMainphoneAreaCode1 | MAINPHONE_AREA_CODE1 | — | — |
| 24 | LocationDetailsPEOMainphoneCountryCode1 | MAINPHONE_COUNTRY_CODE1 | — | — |
| 25 | LocationDetailsPEOMainphoneExtension1 | MAINPHONE_EXTENSION1 | — | — |
| 26 | LocationDetailsPEOMainphoneSubscriberNum1 | MAINPHONE_SUBSCRIBER_NUM1 | — | — |
| 27 | LocationDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 28 | LocationDetailsPEOOfficeSiteFlag | OFFICE_SITE_FLAG | — | — |
| 29 | LocationDetailsPEOOfficialLanguageCode | OFFICIAL_LANGUAGE_CODE | — | — |
| 30 | LocationDetailsPEOOtherphoneAreaCode3 | OTHERPHONE_AREA_CODE3 | — | — |
| 31 | LocationDetailsPEOOtherphoneCountryCode3 | OTHERPHONE_COUNTRY_CODE3 | — | — |
| 32 | LocationDetailsPEOOtherphoneExtension3 | OTHERPHONE_EXTENSION3 | — | — |
| 33 | LocationDetailsPEOOtherphoneSubscriberNum3 | OTHERPHONE_SUBSCRIBER_NUM3 | — | — |
| 34 | LocationDetailsPEOReceivingSiteFlag | RECEIVING_SITE_FLAG | — | — |
| 35 | LocationDetailsPEOShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 36 | LocationDetailsPEOShipToSiteFlag | SHIP_TO_SITE_FLAG | — | ✅ |
| 37 | LocationDetailsPEOTelephoneNumber1 | TELEPHONE_NUMBER_1 | — | — |
| 38 | LocationDetailsPEOTelephoneNumber2 | TELEPHONE_NUMBER_2 | — | — |
| 39 | LocationDetailsPEOTelephoneNumber3 | TELEPHONE_NUMBER_3 | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
