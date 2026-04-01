---
id: DOC-HCM-PVO-HRLocationsPVOViewAll
doc_type: system-doc
title: "HRLocationsPVOViewAll — PVO Human Capital Management"
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
  - HRLocationsPVOViewAll
  - hrlocationspvoviewall
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HRLocationsPVOViewAll

## 📌 Visão Geral

Visão completa (sem filtro de segurança) de localizações do HCM com detalhes. Utilizado em relatórios analíticos de infraestrutura de locais.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.LocationAM.HRLocationsPVOViewAll`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 105 | 9 | 3 | 16 | 15% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_setid_sets_vl|FND_SETID_SETS_VL]] — 5 atributos (2 BICC)
- [[inv_organization_definitions_v|INV_ORGANIZATION_DEFINITIONS_V]] — 3 atributos
- [[per_action_occurrences|PER_ACTION_OCCURRENCES]] — 3 atributos (1 BICC)
- [[per_action_reasons_b|PER_ACTION_REASONS_B]] — 2 atributos (1 BICC)
- [[per_action_reasons_tl|PER_ACTION_REASONS_TL]] — 4 atributos (1 BICC)
- [[per_addresses_f|PER_ADDRESSES_F]] — 27 atributos (5 BICC)
- [[per_locations|PER_LOCATIONS]] — 12 atributos (1 BICC)
- [[per_location_details_f_vl|PER_LOCATION_DETAILS_F_VL]] — 45 atributos (3 PKs, 4 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 4 atributos (1 BICC)

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
| 3 | InventoryOrganizationPEOOrganizationName | ORGANIZATION_NAME | — | — |

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
| 1 | ActionReasonTranslationPEOActionReason | ACTION_REASON | — | — |
| 2 | ActionReasonTranslationPEOActionReasonId | ACTION_REASON_ID | — | — |
| 3 | ActionReasonTranslationPEOLanguage | LANGUAGE | — | — |
| 4 | ActionReasonsTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |

### [[per_addresses_f|PER_ADDRESSES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddressesPEOAddressId | ADDRESS_ID | — | — |
| 2 | AddressesPEOAddressLine1 | ADDRESS_LINE_1 | — | ✅ |
| 3 | AddressesPEOAddressLine2 | ADDRESS_LINE_2 | — | — |
| 4 | AddressesPEOAddressLine3 | ADDRESS_LINE_3 | — | — |
| 5 | AddressesPEOAddressLine4 | ADDRESS_LINE_4 | — | — |
| 6 | AddressesPEOBuilding | BUILDING | — | — |
| 7 | AddressesPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 8 | AddressesPEOCountry | COUNTRY | — | — |
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
| 20 | AddressesPEOLongPostalCode | LONG_POSTAL_CODE | — | — |
| 21 | AddressesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | AddressesPEOPostalCode | POSTAL_CODE | — | ✅ |
| 23 | AddressesPEORegion1 | REGION_1 | — | — |
| 24 | AddressesPEORegion2 | REGION_2 | — | — |
| 25 | AddressesPEORegion3 | REGION_3 | — | — |
| 26 | AddressesPEOTimezoneCode | TIMEZONE_CODE | — | — |
| 27 | AddressesPEOTownOrCity | TOWN_OR_CITY | — | ✅ |

### [[per_locations|PER_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocationPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | LocationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | LocationPEOCreatedBy | CREATED_BY | — | — |
| 4 | LocationPEOCreationDate | CREATION_DATE | — | — |
| 5 | LocationPEOInternalLocationCode | INTERNAL_LOCATION_CODE | — | — |
| 6 | LocationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LocationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LocationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | LocationPEOLocationId | LOCATION_ID | — | — |
| 10 | LocationPEOLocationImageUrl | LOCATION_IMAGE_URL | — | — |
| 11 | LocationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | LocationPEOSetId | SET_ID | — | — |

### [[per_location_details_f_vl|PER_LOCATION_DETAILS_F_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | LocationDetailsId | LOCATION_DETAILS_ID | 🔑 | ✅ |
| 4 | LocationDetailsPEOActiveStatus | ACTIVE_STATUS | — | — |
| 5 | LocationDetailsPEOAnnualWorkingDurationUnits | ANNUAL_WORKING_DURATION_UNITS | — | — |
| 6 | LocationDetailsPEOBillToSiteFlag | BILL_TO_SITE_FLAG | — | — |
| 7 | LocationDetailsPEOBusinessGroupId | business_group_id | — | — |
| 8 | LocationDetailsPEOCreatedBy | CREATED_BY | — | — |
| 9 | LocationDetailsPEOCreationDate | CREATION_DATE | — | — |
| 10 | LocationDetailsPEODescription | DESCRIPTION | — | — |
| 11 | LocationDetailsPEODesignatedReceiverId | DESIGNATED_RECEIVER_ID | — | — |
| 12 | LocationDetailsPEOEmailAddress | EMAIL_ADDRESS | — | — |
| 13 | LocationDetailsPEOFaxAreaCode2 | FAX_AREA_CODE2 | — | — |
| 14 | LocationDetailsPEOFaxCountryCode2 | FAX_COUNTRY_CODE2 | — | — |
| 15 | LocationDetailsPEOFaxExtension2 | FAX_EXTENSION2 | — | — |
| 16 | LocationDetailsPEOFaxSubscriberNum2 | FAX_SUBSCRIBER_NUM2 | — | — |
| 17 | LocationDetailsPEOGeoHierarchyNodeId | GEO_HIERARCHY_NODE_ID | — | — |
| 18 | LocationDetailsPEOGeoHierarchyNodeValue | GEO_HIERARCHY_NODE_VALUE | — | — |
| 19 | LocationDetailsPEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | — |
| 20 | LocationDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | LocationDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 22 | LocationDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 23 | LocationDetailsPEOLocationCode | LOCATION_CODE | — | — |
| 24 | LocationDetailsPEOLocationId | LOCATION_ID | — | — |
| 25 | LocationDetailsPEOMainAddressId | MAIN_ADDRESS_ID | — | — |
| 26 | LocationDetailsPEOMainphoneAreaCode1 | MAINPHONE_AREA_CODE1 | — | — |
| 27 | LocationDetailsPEOMainphoneCountryCode1 | MAINPHONE_COUNTRY_CODE1 | — | — |
| 28 | LocationDetailsPEOMainphoneExtension1 | MAINPHONE_EXTENSION1 | — | — |
| 29 | LocationDetailsPEOMainphoneSubscriberNum1 | MAINPHONE_SUBSCRIBER_NUM1 | — | — |
| 30 | LocationDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 31 | LocationDetailsPEOOfficeSiteFlag | OFFICE_SITE_FLAG | — | — |
| 32 | LocationDetailsPEOOfficialLanguageCode | OFFICIAL_LANGUAGE_CODE | — | — |
| 33 | LocationDetailsPEOOtherphoneAreaCode3 | OTHERPHONE_AREA_CODE3 | — | — |
| 34 | LocationDetailsPEOOtherphoneCountryCode3 | OTHERPHONE_COUNTRY_CODE3 | — | — |
| 35 | LocationDetailsPEOOtherphoneExtension3 | OTHERPHONE_EXTENSION3 | — | — |
| 36 | LocationDetailsPEOOtherphoneSubscriberNum3 | OTHERPHONE_SUBSCRIBER_NUM3 | — | — |
| 37 | LocationDetailsPEOReceivingSiteFlag | RECEIVING_SITE_FLAG | — | — |
| 38 | LocationDetailsPEOShipToLocationId | SHIP_TO_LOCATION_ID | — | — |
| 39 | LocationDetailsPEOShipToSiteFlag | SHIP_TO_SITE_FLAG | — | — |
| 40 | LocationDetailsPEOStandardWorkingFrequency | STANDARD_WORKING_FREQUENCY | — | — |
| 41 | LocationDetailsPEOStandardWorkingHours | STANDARD_WORKING_HOURS | — | — |
| 42 | LocationDetailsPEOStdAnnualWorkingDuration | STD_ANNUAL_WORKING_DURATION | — | — |
| 43 | LocationDetailsPEOTelephoneNumber1 | TELEPHONE_NUMBER_1 | — | — |
| 44 | LocationDetailsPEOTelephoneNumber2 | TELEPHONE_NUMBER_2 | — | — |
| 45 | LocationDetailsPEOTelephoneNumber3 | TELEPHONE_NUMBER_3 | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DesignatedReceiverPEODisplayName | DISPLAY_NAME | — | — |
| 2 | DesignatedReceiverPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | DesignatedReceiverPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | DesignatedReceiverPEOPersonNameId | PERSON_NAME_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
