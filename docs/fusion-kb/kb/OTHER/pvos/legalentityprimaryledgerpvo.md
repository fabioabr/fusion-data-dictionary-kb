---
id: DOC-OTHER-PVO-LegalEntityPrimaryLedgerPVO
doc_type: system-doc
title: "LegalEntityPrimaryLedgerPVO — PVO Cross-Module"
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
  - LegalEntityPrimaryLedgerPVO
  - legalentityprimaryledgerpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LegalEntityPrimaryLedgerPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Legal Entity Primary Ledger. Acessa as tabelas: GL_LEDGERS, GL_LEDGER_CONFIGURATIONS, GL_LEDGER_CONFIG_DETAILS (+6).

**Caminho:** `FscmTopModelAM.FinLeLegalEntitiesAM.LegalEntityPrimaryLedgerPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 261 | 9 | 1 | 23 | 9% |

---

## 🔗 Tabelas Relacionadas

- [[gl_ledgers|GL_LEDGERS]] — 59 atributos
- [[gl_ledger_configurations|GL_LEDGER_CONFIGURATIONS]] — 7 atributos
- [[gl_ledger_config_details|GL_LEDGER_CONFIG_DETAILS]] — 9 atributos
- [[hz_geographies|HZ_GEOGRAPHIES]] — 35 atributos
- [[hz_locations|HZ_LOCATIONS]] — 48 atributos (9 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos
- [[per_users|PER_USERS]] — 10 atributos
- [[xle_entity_profiles|XLE_ENTITY_PROFILES]] — 42 atributos (1 PKs, 11 BICC)
- [[xle_registrations|XLE_REGISTRATIONS]] — 41 atributos (3 BICC)

---

## ⚙️ Atributos

### [[gl_ledgers|GL_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlLedgersAccountedPeriodType | ACCOUNTED_PERIOD_TYPE | — | — |
| 2 | GlLedgersAlcLedgerTypeCode | ALC_LEDGER_TYPE_CODE | — | — |
| 3 | GlLedgersAllowIntercompanyPostFlag | ALLOW_INTERCOMPANY_POST_FLAG | — | — |
| 4 | GlLedgersApDocSequencingOptionFlag | AP_DOC_SEQUENCING_OPTION_FLAG | — | — |
| 5 | GlLedgersArDocSequencingOptionFlag | AR_DOC_SEQUENCING_OPTION_FLAG | — | — |
| 6 | GlLedgersAutomateSecJrnlRevFlag | AUTOMATE_SEC_JRNL_REV_FLAG | — | — |
| 7 | GlLedgersAutomaticallyCreatedFlag | AUTOMATICALLY_CREATED_FLAG | — | — |
| 8 | GlLedgersAutorevAfterOpenPrdFlag | AUTOREV_AFTER_OPEN_PRD_FLAG | — | — |
| 9 | GlLedgersBalSegColumnName | BAL_SEG_COLUMN_NAME | — | — |
| 10 | GlLedgersBalSegValueOptionCode | BAL_SEG_VALUE_OPTION_CODE | — | — |
| 11 | GlLedgersBalSegValueSetId | BAL_SEG_VALUE_SET_ID | — | — |
| 12 | GlLedgersBudgetPeriodAvgRateType | BUDGET_PERIOD_AVG_RATE_TYPE | — | — |
| 13 | GlLedgersBudgetPeriodEndRateType | BUDGET_PERIOD_END_RATE_TYPE | — | — |
| 14 | GlLedgersChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 15 | GlLedgersCompleteFlag | COMPLETE_FLAG | — | — |
| 16 | GlLedgersCompletionStatusCode1 | COMPLETION_STATUS_CODE | — | — |
| 17 | GlLedgersConfigurationId2 | CONFIGURATION_ID | — | — |
| 18 | GlLedgersConsolidationLedgerFlag | CONSOLIDATION_LEDGER_FLAG | — | — |
| 19 | GlLedgersCreateJeFlag | CREATE_JE_FLAG | — | — |
| 20 | GlLedgersCriteriaSetId | CRITERIA_SET_ID | — | — |
| 21 | GlLedgersCumTransCodeCombinationId | CUM_TRANS_CODE_COMBINATION_ID | — | — |
| 22 | GlLedgersCurrencyCode | CURRENCY_CODE | — | — |
| 23 | GlLedgersDailyTranslationRateType | DAILY_TRANSLATION_RATE_TYPE | — | — |
| 24 | GlLedgersDescription1 | DESCRIPTION | — | — |
| 25 | GlLedgersEnableAutomaticTaxFlag | ENABLE_AUTOMATIC_TAX_FLAG | — | — |
| 26 | GlLedgersEnableAverageBalancesFlag | ENABLE_AVERAGE_BALANCES_FLAG | — | — |
| 27 | GlLedgersEnableBudgetaryControlFlag | ENABLE_BUDGETARY_CONTROL_FLAG | — | — |
| 28 | GlLedgersEnableJeApprovalFlag | ENABLE_JE_APPROVAL_FLAG | — | — |
| 29 | GlLedgersEnableReconciliationFlag | ENABLE_RECONCILIATION_FLAG | — | — |
| 30 | GlLedgersEnableRevalSsTrackFlag | ENABLE_REVAL_SS_TRACK_FLAG | — | — |
| 31 | GlLedgersEnableSecondaryTrackFlag | ENABLE_SECONDARY_TRACK_FLAG | — | — |
| 32 | GlLedgersEnfSeqDateCorrelationCode | ENF_SEQ_DATE_CORRELATION_CODE | — | — |
| 33 | GlLedgersFirstLedgerPeriodName | FIRST_LEDGER_PERIOD_NAME | — | — |
| 34 | GlLedgersFutureEnterablePeriodsLimit | FUTURE_ENTERABLE_PERIODS_LIMIT | — | — |
| 35 | GlLedgersImplicitAccessSetId | IMPLICIT_ACCESS_SET_ID | — | — |
| 36 | GlLedgersImplicitLedgerSetId | IMPLICIT_LEDGER_SET_ID | — | — |
| 37 | GlLedgersIntercoGainLossCcid | INTERCO_GAIN_LOSS_CCID | — | — |
| 38 | GlLedgersJrnlsGroupByDateFlag | JRNLS_GROUP_BY_DATE_FLAG | — | — |
| 39 | GlLedgersLatestEncumbranceYear | LATEST_ENCUMBRANCE_YEAR | — | — |
| 40 | GlLedgersLatestOpenedPeriodName | LATEST_OPENED_PERIOD_NAME | — | — |
| 41 | GlLedgersLeLedgerTypeCode | LE_LEDGER_TYPE_CODE | — | — |
| 42 | GlLedgersLedgerAttributes | LEDGER_ATTRIBUTES | — | — |
| 43 | GlLedgersLedgerCategoryCode | LEDGER_CATEGORY_CODE | — | — |
| 44 | GlLedgersName | NAME | — | — |
| 45 | GlLedgersNetClosingBalFlag | NET_CLOSING_BAL_FLAG | — | — |
| 46 | GlLedgersNetIncomeCodeCombinationId | NET_INCOME_CODE_COMBINATION_ID | — | — |
| 47 | GlLedgersObjectTypeCode1 | OBJECT_TYPE_CODE | — | — |
| 48 | GlLedgersPeriodAverageRateType | PERIOD_AVERAGE_RATE_TYPE | — | — |
| 49 | GlLedgersPeriodEndRateType | PERIOD_END_RATE_TYPE | — | — |
| 50 | GlLedgersPeriodSetName | PERIOD_SET_NAME | — | — |
| 51 | GlLedgersRequireBudgetJournalsFlag | REQUIRE_BUDGET_JOURNALS_FLAG | — | — |
| 52 | GlLedgersShortName | SHORT_NAME | — | — |
| 53 | GlLedgersSlaAccountingMethodCode | SLA_ACCOUNTING_METHOD_CODE | — | — |
| 54 | GlLedgersSlaAccountingMethodType | SLA_ACCOUNTING_METHOD_TYPE | — | — |
| 55 | GlLedgersSlaBalByLedgerCurrFlag | SLA_BAL_BY_LEDGER_CURR_FLAG | — | — |
| 56 | GlLedgersThresholdAmount | THRESHOLD_AMOUNT | — | — |
| 57 | GlLedgersTransactionCalendarId | TRANSACTION_CALENDAR_ID | — | — |
| 58 | LedgerId | LEDGER_ID | — | — |
| 59 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[gl_ledger_configurations|GL_LEDGER_CONFIGURATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlLedgerConfigurationsAcctgEnvironmentCode | ACCTG_ENVIRONMENT_CODE | — | — |
| 2 | GlLedgerConfigurationsAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 3 | GlLedgerConfigurationsCompletionStatusCode | COMPLETION_STATUS_CODE | — | — |
| 4 | GlLedgerConfigurationsConfigurationId1 | CONFIGURATION_ID | — | — |
| 5 | GlLedgerConfigurationsDescription | DESCRIPTION | — | — |
| 6 | GlLedgerConfigurationsName | NAME | — | — |
| 7 | GlLedgerConfigurationsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[gl_ledger_config_details|GL_LEDGER_CONFIG_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlLedConfDetConfigurationId | CONFIGURATION_ID | — | — |
| 2 | GlLedConfDetNextActionCode | NEXT_ACTION_CODE | — | — |
| 3 | GlLedConfDetObjectId | OBJECT_ID | — | — |
| 4 | GlLedConfDetObjectName | OBJECT_NAME | — | — |
| 5 | GlLedConfDetObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 6 | GlLedConfDetSetupStepCode | SETUP_STEP_CODE | — | — |
| 7 | GlLedConfDetStatusCode | STATUS_CODE | — | — |
| 8 | GlLedConfDetTaxDefaultLeFlag | TAX_DEFAULT_LE_FLAG | — | — |
| 9 | GlLedConfDetTimeZoneDefaultLeFlag | TIME_ZONE_DEFAULT_LE_FLAG | — | — |

### [[hz_geographies|HZ_GEOGRAPHIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GeographyCountryCode | COUNTRY_CODE | — | — |
| 2 | GeographyEndDate | END_DATE | — | — |
| 3 | GeographyGeographyCode | GEOGRAPHY_CODE | — | — |
| 4 | GeographyGeographyElement1 | GEOGRAPHY_ELEMENT1 | — | — |
| 5 | GeographyGeographyElement10 | GEOGRAPHY_ELEMENT10 | — | — |
| 6 | GeographyGeographyElement10Id | GEOGRAPHY_ELEMENT10_ID | — | — |
| 7 | GeographyGeographyElement1Code | GEOGRAPHY_ELEMENT1_CODE | — | — |
| 8 | GeographyGeographyElement1Id | GEOGRAPHY_ELEMENT1_ID | — | — |
| 9 | GeographyGeographyElement2 | GEOGRAPHY_ELEMENT2 | — | — |
| 10 | GeographyGeographyElement2Code | GEOGRAPHY_ELEMENT2_CODE | — | — |
| 11 | GeographyGeographyElement2Id | GEOGRAPHY_ELEMENT2_ID | — | — |
| 12 | GeographyGeographyElement3 | GEOGRAPHY_ELEMENT3 | — | — |
| 13 | GeographyGeographyElement3Code | GEOGRAPHY_ELEMENT3_CODE | — | — |
| 14 | GeographyGeographyElement3Id | GEOGRAPHY_ELEMENT3_ID | — | — |
| 15 | GeographyGeographyElement4 | GEOGRAPHY_ELEMENT4 | — | — |
| 16 | GeographyGeographyElement4Code | GEOGRAPHY_ELEMENT4_CODE | — | — |
| 17 | GeographyGeographyElement4Id | GEOGRAPHY_ELEMENT4_ID | — | — |
| 18 | GeographyGeographyElement5 | GEOGRAPHY_ELEMENT5 | — | — |
| 19 | GeographyGeographyElement5Code | GEOGRAPHY_ELEMENT5_CODE | — | — |
| 20 | GeographyGeographyElement5Id | GEOGRAPHY_ELEMENT5_ID | — | — |
| 21 | GeographyGeographyElement6 | GEOGRAPHY_ELEMENT6 | — | — |
| 22 | GeographyGeographyElement6Id | GEOGRAPHY_ELEMENT6_ID | — | — |
| 23 | GeographyGeographyElement7 | GEOGRAPHY_ELEMENT7 | — | — |
| 24 | GeographyGeographyElement7Id | GEOGRAPHY_ELEMENT7_ID | — | — |
| 25 | GeographyGeographyElement8 | GEOGRAPHY_ELEMENT8 | — | — |
| 26 | GeographyGeographyElement8Id | GEOGRAPHY_ELEMENT8_ID | — | — |
| 27 | GeographyGeographyElement9 | GEOGRAPHY_ELEMENT9 | — | — |
| 28 | GeographyGeographyElement9Id | GEOGRAPHY_ELEMENT9_ID | — | — |
| 29 | GeographyGeographyId | GEOGRAPHY_ID | — | — |
| 30 | GeographyGeographyName | GEOGRAPHY_NAME | — | — |
| 31 | GeographyGeographyType | GEOGRAPHY_TYPE | — | — |
| 32 | GeographyGeographyUse | GEOGRAPHY_USE | — | — |
| 33 | GeographyMultipleParentFlag | MULTIPLE_PARENT_FLAG | — | — |
| 34 | GeographyStartDate | START_DATE | — | — |
| 35 | GeographyTimezoneCode | TIMEZONE_CODE | — | — |

### [[hz_locations|HZ_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LocationActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | LocationAddrElementAttribute1 | ADDR_ELEMENT_ATTRIBUTE1 | — | ✅ |
| 3 | LocationAddrElementAttribute2 | ADDR_ELEMENT_ATTRIBUTE2 | — | ✅ |
| 4 | LocationAddrElementAttribute3 | ADDR_ELEMENT_ATTRIBUTE3 | — | — |
| 5 | LocationAddrElementAttribute4 | ADDR_ELEMENT_ATTRIBUTE4 | — | — |
| 6 | LocationAddrElementAttribute5 | ADDR_ELEMENT_ATTRIBUTE5 | — | — |
| 7 | LocationAddress1 | ADDRESS1 | — | — |
| 8 | LocationAddress2 | ADDRESS2 | — | — |
| 9 | LocationAddress3 | ADDRESS3 | — | — |
| 10 | LocationAddress4 | ADDRESS4 | — | — |
| 11 | LocationAddressEffectiveDate | ADDRESS_EFFECTIVE_DATE | — | — |
| 12 | LocationAddressExpirationDate | ADDRESS_EXPIRATION_DATE | — | — |
| 13 | LocationAddressLinesPhonetic | ADDRESS_LINES_PHONETIC | — | — |
| 14 | LocationAddressStyle | ADDRESS_STYLE | — | — |
| 15 | LocationBuilding | BUILDING | — | — |
| 16 | LocationCity | CITY | — | ✅ |
| 17 | LocationClliCode | CLLI_CODE | — | — |
| 18 | LocationComments | COMMENTS | — | — |
| 19 | LocationCountry | COUNTRY | — | ✅ |
| 20 | LocationCounty | COUNTY | — | ✅ |
| 21 | LocationCreatedByModule | CREATED_BY_MODULE | — | — |
| 22 | LocationDateValidated | DATE_VALIDATED | — | — |
| 23 | LocationDescription | DESCRIPTION | — | — |
| 24 | LocationDoNotValidateFlag | DO_NOT_VALIDATE_FLAG | — | — |
| 25 | LocationFaLocationId | FA_LOCATION_ID | — | — |
| 26 | LocationFloorNumber | FLOOR_NUMBER | — | — |
| 27 | LocationGeometryStatusCode | GEOMETRY_STATUS_CODE | — | — |
| 28 | LocationHouseType | HOUSE_TYPE | — | — |
| 29 | LocationInternalFlag | INTERNAL_FLAG | — | — |
| 30 | LocationJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 31 | LocationJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 32 | LocationLanguage | LOCATION_LANGUAGE | — | ✅ |
| 33 | LocationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | LocationLocationDirections | LOCATION_DIRECTIONS | — | — |
| 35 | LocationLocationId | LOCATION_ID | — | — |
| 36 | LocationOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 37 | LocationPosition | POSITION | — | — |
| 38 | LocationPostalCode | POSTAL_CODE | — | ✅ |
| 39 | LocationPostalPlus4Code | POSTAL_PLUS4_CODE | — | — |
| 40 | LocationProvince | PROVINCE | — | — |
| 41 | LocationSalesTaxGeocode | SALES_TAX_GEOCODE | — | — |
| 42 | LocationSalesTaxInsideCityLimits | SALES_TAX_INSIDE_CITY_LIMITS | — | — |
| 43 | LocationShortDescription | SHORT_DESCRIPTION | — | — |
| 44 | LocationState | STATE | — | ✅ |
| 45 | LocationStatusFlag | STATUS_FLAG | — | — |
| 46 | LocationTimezoneCode | TIMEZONE_CODE | — | — |
| 47 | LocationValidatedFlag | VALIDATED_FLAG | — | — |
| 48 | LocationValidationStatusCode | VALIDATION_STATUS_CODE | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | — |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | — |
| 7 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UserCreatedByPersonId | PERSON_ID | — | — |
| 3 | UserCreatedByUserGuid | USER_GUID | — | — |
| 4 | UserCreatedByUserId | USER_ID | — | — |
| 5 | UserCreatedByUsername | USERNAME | — | — |
| 6 | UserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 8 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 9 | UserUpdatedByUserId | USER_ID | — | — |
| 10 | UserUpdatedByUsername | USERNAME | — | — |

### [[xle_entity_profiles|XLE_ENTITY_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LegalEntityActivityCode | ACTIVITY_CODE | — | — |
| 2 | LegalEntityCreatedBy | CREATED_BY | — | ✅ |
| 3 | LegalEntityCreationDate | CREATION_DATE | — | ✅ |
| 4 | LegalEntityEffectiveFrom | EFFECTIVE_FROM | — | ✅ |
| 5 | LegalEntityEffectiveTo | EFFECTIVE_TO | — | ✅ |
| 6 | LegalEntityEnterpriseId | ENTERPRISE_ID | — | — |
| 7 | LegalEntityGeographyId | GEOGRAPHY_ID | — | — |
| 8 | LegalEntityId | LEGAL_ENTITY_ID | 🔑 | ✅ |
| 9 | LegalEntityLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LegalEntityLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | LegalEntityLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | LegalEntityLeInformation1 | LE_INFORMATION1 | — | — |
| 13 | LegalEntityLeInformation10 | LE_INFORMATION10 | — | — |
| 14 | LegalEntityLeInformation11 | LE_INFORMATION11 | — | — |
| 15 | LegalEntityLeInformation12 | LE_INFORMATION12 | — | — |
| 16 | LegalEntityLeInformation13 | LE_INFORMATION13 | — | — |
| 17 | LegalEntityLeInformation14 | LE_INFORMATION14 | — | — |
| 18 | LegalEntityLeInformation15 | LE_INFORMATION15 | — | — |
| 19 | LegalEntityLeInformation16 | LE_INFORMATION16 | — | — |
| 20 | LegalEntityLeInformation17 | LE_INFORMATION17 | — | — |
| 21 | LegalEntityLeInformation18 | LE_INFORMATION18 | — | — |
| 22 | LegalEntityLeInformation19 | LE_INFORMATION19 | — | — |
| 23 | LegalEntityLeInformation2 | LE_INFORMATION2 | — | — |
| 24 | LegalEntityLeInformation20 | LE_INFORMATION20 | — | — |
| 25 | LegalEntityLeInformation3 | LE_INFORMATION3 | — | — |
| 26 | LegalEntityLeInformation4 | LE_INFORMATION4 | — | — |
| 27 | LegalEntityLeInformation5 | LE_INFORMATION5 | — | — |
| 28 | LegalEntityLeInformation6 | LE_INFORMATION6 | — | — |
| 29 | LegalEntityLeInformation7 | LE_INFORMATION7 | — | — |
| 30 | LegalEntityLeInformation8 | LE_INFORMATION8 | — | — |
| 31 | LegalEntityLeInformation9 | LE_INFORMATION9 | — | — |
| 32 | LegalEntityLeInformationContext | LE_INFORMATION_CONTEXT | — | — |
| 33 | LegalEntityLegalEmployerFlag | LEGAL_EMPLOYER_FLAG | — | — |
| 34 | LegalEntityLegalEntityIdentifier | LEGAL_ENTITY_IDENTIFIER | — | ✅ |
| 35 | LegalEntityName | NAME | — | ✅ |
| 36 | LegalEntityObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 37 | LegalEntityParentPsuId | PARENT_PSU_ID | — | — |
| 38 | LegalEntityPartyId | PARTY_ID | — | — |
| 39 | LegalEntityPsuFlag | PSU_FLAG | — | ✅ |
| 40 | LegalEntitySubActivityCode | SUB_ACTIVITY_CODE | — | — |
| 41 | LegalEntityTransactingEntityFlag | TRANSACTING_ENTITY_FLAG | — | ✅ |
| 42 | LegalEntityTypeOfCompany | TYPE_OF_COMPANY | — | — |

### [[xle_registrations|XLE_REGISTRATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RegistrationAlternateRegisteredName | ALTERNATE_REGISTERED_NAME | — | — |
| 2 | RegistrationCreatedBy | CREATED_BY | — | — |
| 3 | RegistrationCreationDate | CREATION_DATE | — | — |
| 4 | RegistrationEffectiveFrom | EFFECTIVE_FROM | — | — |
| 5 | RegistrationEffectiveTo | EFFECTIVE_TO | — | — |
| 6 | RegistrationIdentifyingFlag | IDENTIFYING_FLAG | — | — |
| 7 | RegistrationIssuingAuthorityId | ISSUING_AUTHORITY_ID | — | — |
| 8 | RegistrationIssuingAuthoritySiteId | ISSUING_AUTHORITY_SITE_ID | — | — |
| 9 | RegistrationJurisdictionId | JURISDICTION_ID | — | — |
| 10 | RegistrationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | RegistrationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | RegistrationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | RegistrationLocationId | LOCATION_ID | — | — |
| 14 | RegistrationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | RegistrationPlaceOfRegistration | PLACE_OF_REGISTRATION | — | — |
| 16 | RegistrationRegInformation1 | REG_INFORMATION1 | — | — |
| 17 | RegistrationRegInformation10 | REG_INFORMATION10 | — | — |
| 18 | RegistrationRegInformation11 | REG_INFORMATION11 | — | — |
| 19 | RegistrationRegInformation12 | REG_INFORMATION12 | — | — |
| 20 | RegistrationRegInformation13 | REG_INFORMATION13 | — | — |
| 21 | RegistrationRegInformation14 | REG_INFORMATION14 | — | — |
| 22 | RegistrationRegInformation15 | REG_INFORMATION15 | — | — |
| 23 | RegistrationRegInformation16 | REG_INFORMATION16 | — | — |
| 24 | RegistrationRegInformation17 | REG_INFORMATION17 | — | — |
| 25 | RegistrationRegInformation18 | REG_INFORMATION18 | — | — |
| 26 | RegistrationRegInformation19 | REG_INFORMATION19 | — | — |
| 27 | RegistrationRegInformation2 | REG_INFORMATION2 | — | — |
| 28 | RegistrationRegInformation20 | REG_INFORMATION20 | — | — |
| 29 | RegistrationRegInformation3 | REG_INFORMATION3 | — | — |
| 30 | RegistrationRegInformation4 | REG_INFORMATION4 | — | — |
| 31 | RegistrationRegInformation5 | REG_INFORMATION5 | — | — |
| 32 | RegistrationRegInformation6 | REG_INFORMATION6 | — | — |
| 33 | RegistrationRegInformation7 | REG_INFORMATION7 | — | — |
| 34 | RegistrationRegInformation8 | REG_INFORMATION8 | — | — |
| 35 | RegistrationRegInformation9 | REG_INFORMATION9 | — | — |
| 36 | RegistrationRegInformationContext | REG_INFORMATION_CONTEXT | — | — |
| 37 | RegistrationRegisteredName | REGISTERED_NAME | — | ✅ |
| 38 | RegistrationRegistrationId | REGISTRATION_ID | — | — |
| 39 | RegistrationRegistrationNumber | REGISTRATION_NUMBER | — | ✅ |
| 40 | RegistrationSourceId | SOURCE_ID | — | — |
| 41 | RegistrationSourceTable | SOURCE_TABLE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
