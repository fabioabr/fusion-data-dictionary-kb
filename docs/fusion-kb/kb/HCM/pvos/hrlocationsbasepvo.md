---
id: DOC-HCM-PVO-HRLocationsBasePVO
doc_type: system-doc
title: "HRLocationsBasePVO — PVO Human Capital Management"
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
  - HRLocationsBasePVO
  - hrlocationsbasepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HRLocationsBasePVO

## 📌 Visão Geral

Consolida localizações base do HCM com sets, organizações de inventário e ações. Fundamental para cadastro e administração de locais de trabalho.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.LocationAM.HRLocationsBasePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 142 | 10 | 3 | 56 | 39% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_setid_sets_vl|FND_SETID_SETS_VL]] — 5 atributos (2 BICC)
- [[inv_organization_definitions_v|INV_ORGANIZATION_DEFINITIONS_V]] — 3 atributos (1 BICC)
- [[per_action_occurrences|PER_ACTION_OCCURRENCES]] — 3 atributos (1 BICC)
- [[per_action_reasons_b|PER_ACTION_REASONS_B]] — 2 atributos (1 BICC)
- [[per_action_reasons_tl|PER_ACTION_REASONS_TL]] — 4 atributos (2 BICC)
- [[per_addresses_f|PER_ADDRESSES_F]] — 27 atributos (15 BICC)
- [[per_locations|PER_LOCATIONS]] — 13 atributos (6 BICC)
- [[per_location_details_f|PER_LOCATION_DETAILS_F]] — 43 atributos (3 PKs, 20 BICC)
- [[per_location_details_f_tl|PER_LOCATION_DETAILS_F_TL]] — 15 atributos (5 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 27 atributos (3 BICC)

---

## ⚙️ Atributos

### [[fnd_setid_sets_vl|FND_SETID_SETS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SetIdSetPEODescription | DESCRIPTION | — | — |
| 2 | SetIdSetPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | SetIdSetPEOSetCode | SET_CODE | — | — |
| 4 | SetIdSetPEOSetId | SET_ID | — | — |
| 5 | SetIdSetPEOSetName | SET_NAME | — | ✅ |

### [[inv_organization_definitions_v|INV_ORGANIZATION_DEFINITIONS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InventoryOrganizationPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 2 | InventoryOrganizationPEOOrganizationId | ORGANIZATION_ID | — | — |
| 3 | InventoryOrganizationPEOOrganizationName | ORGANIZATION_NAME | — | ✅ |

### [[per_action_occurrences|PER_ACTION_OCCURRENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionOccurrencesPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | ActionOccurrencesPEOActionReasonId | ACTION_REASON_ID | — | — |
| 3 | ActionOccurrencesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[per_action_reasons_b|PER_ACTION_REASONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionReasonPEOActionReasonId | ACTION_REASON_ID | — | — |
| 2 | ActionReasonsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[per_action_reasons_tl|PER_ACTION_REASONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionReasonTranslationPEOActionReason | ACTION_REASON | — | ✅ |
| 2 | ActionReasonTranslationPEOActionReasonId | ACTION_REASON_ID | — | — |
| 3 | ActionReasonTranslationPEOLanguage | LANGUAGE | — | — |
| 4 | ActionReasonsTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[per_addresses_f|PER_ADDRESSES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddressesPEOAddressId | ADDRESS_ID | — | ✅ |
| 2 | AddressesPEOAddressLine1 | ADDRESS_LINE_1 | — | ✅ |
| 3 | AddressesPEOAddressLine2 | ADDRESS_LINE_2 | — | ✅ |
| 4 | AddressesPEOAddressLine3 | ADDRESS_LINE_3 | — | ✅ |
| 5 | AddressesPEOAddressLine4 | ADDRESS_LINE_4 | — | ✅ |
| 6 | AddressesPEOBuilding | BUILDING | — | — |
| 7 | AddressesPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 8 | AddressesPEOCountry | COUNTRY | — | ✅ |
| 9 | AddressesPEOCreatedBy | CREATED_BY | — | — |
| 10 | AddressesPEOCreationDate | CREATION_DATE | — | — |
| 11 | AddressesPEODerivedLocale | DERIVED_LOCALE | — | — |
| 12 | AddressesPEODqValidationLevel | DQ_VALIDATION_LEVEL | — | — |
| 13 | AddressesPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 14 | AddressesPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 15 | AddressesPEOFloorNumber | FLOOR_NUMBER | — | — |
| 16 | AddressesPEOGeometry | GEOMETRY | — | — |
| 17 | AddressesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | AddressesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | AddressesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | AddressesPEOLongPostalCode | LONG_POSTAL_CODE | — | ✅ |
| 21 | AddressesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | AddressesPEOPostalCode | POSTAL_CODE | — | ✅ |
| 23 | AddressesPEORegion1 | REGION_1 | — | ✅ |
| 24 | AddressesPEORegion2 | REGION_2 | — | ✅ |
| 25 | AddressesPEORegion3 | REGION_3 | — | ✅ |
| 26 | AddressesPEOTimezoneCode | TIMEZONE_CODE | — | ✅ |
| 27 | AddressesPEOTownOrCity | TOWN_OR_CITY | — | ✅ |

### [[per_locations|PER_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocationPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | LocationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | LocationPEOCreatedBy | CREATED_BY | — | — |
| 4 | LocationPEOCreationDate | CREATION_DATE | — | — |
| 5 | LocationPEOEmployeeLocationFlag | EMPLOYEE_LOCATION_FLAG | — | ✅ |
| 6 | LocationPEOInternalLocationCode | INTERNAL_LOCATION_CODE | — | ✅ |
| 7 | LocationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LocationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LocationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | LocationPEOLocationId | LOCATION_ID | — | ✅ |
| 11 | LocationPEOLocationImageUrl | LOCATION_IMAGE_URL | — | ✅ |
| 12 | LocationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | LocationPEOSetId | SET_ID | — | ✅ |

### [[per_location_details_f|PER_LOCATION_DETAILS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | LocationDetailsId | LOCATION_DETAILS_ID | 🔑 | ✅ |
| 4 | LocationDetailsPEOActiveStatus | ACTIVE_STATUS | — | ✅ |
| 5 | LocationDetailsPEOAnnualWorkingDurationUnits | ANNUAL_WORKING_DURATION_UNITS | — | — |
| 6 | LocationDetailsPEOBillToSiteFlag | BILL_TO_SITE_FLAG | — | ✅ |
| 7 | LocationDetailsPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 8 | LocationDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 9 | LocationDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 10 | LocationDetailsPEODesignatedReceiverId | DESIGNATED_RECEIVER_ID | — | — |
| 11 | LocationDetailsPEOEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 12 | LocationDetailsPEOFaxAreaCode2 | FAX_AREA_CODE2 | — | — |
| 13 | LocationDetailsPEOFaxCountryCode2 | FAX_COUNTRY_CODE2 | — | — |
| 14 | LocationDetailsPEOFaxExtension2 | FAX_EXTENSION2 | — | — |
| 15 | LocationDetailsPEOFaxSubscriberNum2 | FAX_SUBSCRIBER_NUM2 | — | — |
| 16 | LocationDetailsPEOGeoHierarchyNodeId | GEO_HIERARCHY_NODE_ID | — | — |
| 17 | LocationDetailsPEOGeoHierarchyNodeValue | GEO_HIERARCHY_NODE_VALUE | — | ✅ |
| 18 | LocationDetailsPEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 19 | LocationDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | LocationDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | LocationDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 22 | LocationDetailsPEOLocationId | LOCATION_ID | — | — |
| 23 | LocationDetailsPEOMainAddressId | MAIN_ADDRESS_ID | — | ✅ |
| 24 | LocationDetailsPEOMainphoneAreaCode1 | MAINPHONE_AREA_CODE1 | — | — |
| 25 | LocationDetailsPEOMainphoneCountryCode1 | MAINPHONE_COUNTRY_CODE1 | — | — |
| 26 | LocationDetailsPEOMainphoneExtension1 | MAINPHONE_EXTENSION1 | — | — |
| 27 | LocationDetailsPEOMainphoneSubscriberNum1 | MAINPHONE_SUBSCRIBER_NUM1 | — | — |
| 28 | LocationDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 29 | LocationDetailsPEOOfficeSiteFlag | OFFICE_SITE_FLAG | — | ✅ |
| 30 | LocationDetailsPEOOfficialLanguageCode | OFFICIAL_LANGUAGE_CODE | — | ✅ |
| 31 | LocationDetailsPEOOtherphoneAreaCode3 | OTHERPHONE_AREA_CODE3 | — | — |
| 32 | LocationDetailsPEOOtherphoneCountryCode3 | OTHERPHONE_COUNTRY_CODE3 | — | — |
| 33 | LocationDetailsPEOOtherphoneExtension3 | OTHERPHONE_EXTENSION3 | — | — |
| 34 | LocationDetailsPEOOtherphoneSubscriberNum3 | OTHERPHONE_SUBSCRIBER_NUM3 | — | — |
| 35 | LocationDetailsPEOReceivingSiteFlag | RECEIVING_SITE_FLAG | — | ✅ |
| 36 | LocationDetailsPEOShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 37 | LocationDetailsPEOShipToSiteFlag | SHIP_TO_SITE_FLAG | — | ✅ |
| 38 | LocationDetailsPEOStandardWorkingFrequency | STANDARD_WORKING_FREQUENCY | — | — |
| 39 | LocationDetailsPEOStandardWorkingHours | STANDARD_WORKING_HOURS | — | — |
| 40 | LocationDetailsPEOStdAnnualWorkingDuration | STD_ANNUAL_WORKING_DURATION | — | — |
| 41 | LocationDetailsPEOTelephoneNumber1 | TELEPHONE_NUMBER_1 | — | ✅ |
| 42 | LocationDetailsPEOTelephoneNumber2 | TELEPHONE_NUMBER_2 | — | ✅ |
| 43 | LocationDetailsPEOTelephoneNumber3 | TELEPHONE_NUMBER_3 | — | ✅ |

### [[per_location_details_f_tl|PER_LOCATION_DETAILS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocationDetailsTranslationPEOAcLocationCode | AC_LOCATION_CODE | — | — |
| 2 | LocationDetailsTranslationPEOCreatedBy | CREATED_BY | — | — |
| 3 | LocationDetailsTranslationPEOCreationDate | CREATION_DATE | — | — |
| 4 | LocationDetailsTranslationPEODescription | DESCRIPTION | — | ✅ |
| 5 | LocationDetailsTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | LocationDetailsTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | LocationDetailsTranslationPEOLanguage | LANGUAGE | — | — |
| 8 | LocationDetailsTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LocationDetailsTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | LocationDetailsTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | LocationDetailsTranslationPEOLocationCode | LOCATION_CODE | — | ✅ |
| 12 | LocationDetailsTranslationPEOLocationDetailsId | LOCATION_DETAILS_ID | — | — |
| 13 | LocationDetailsTranslationPEOLocationName | LOCATION_NAME | — | ✅ |
| 14 | LocationDetailsTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | LocationDetailsTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DesignatedReceiverPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | DesignatedReceiverPEOCreatedBy | CREATED_BY | — | — |
| 3 | DesignatedReceiverPEOCreationDate | CREATION_DATE | — | — |
| 4 | DesignatedReceiverPEODisplayName | DISPLAY_NAME | — | ✅ |
| 5 | DesignatedReceiverPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | DesignatedReceiverPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | DesignatedReceiverPEOFirstName | FIRST_NAME | — | — |
| 8 | DesignatedReceiverPEOFullName | FULL_NAME | — | — |
| 9 | DesignatedReceiverPEOHonors | HONORS | — | — |
| 10 | DesignatedReceiverPEOKnownAs | KNOWN_AS | — | — |
| 11 | DesignatedReceiverPEOLastName | LAST_NAME | — | — |
| 12 | DesignatedReceiverPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | DesignatedReceiverPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | DesignatedReceiverPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | DesignatedReceiverPEOLegislationCode | LEGISLATION_CODE | — | — |
| 16 | DesignatedReceiverPEOListName | LIST_NAME | — | — |
| 17 | DesignatedReceiverPEOMiddleNames | MIDDLE_NAMES | — | — |
| 18 | DesignatedReceiverPEOMilitaryRank | MILITARY_RANK | — | — |
| 19 | DesignatedReceiverPEONameType | NAME_TYPE | — | — |
| 20 | DesignatedReceiverPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | DesignatedReceiverPEOOrderName | ORDER_NAME | — | — |
| 22 | DesignatedReceiverPEOPersonId | PERSON_ID | — | — |
| 23 | DesignatedReceiverPEOPersonNameId | PERSON_NAME_ID | — | — |
| 24 | DesignatedReceiverPEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 25 | DesignatedReceiverPEOPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 26 | DesignatedReceiverPEOSuffix | SUFFIX | — | — |
| 27 | DesignatedReceiverPEOTitle | TITLE | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
