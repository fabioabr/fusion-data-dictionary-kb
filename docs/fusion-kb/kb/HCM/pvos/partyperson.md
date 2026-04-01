---
id: DOC-HCM-PVO-PartyPerson
doc_type: system-doc
title: "PartyPerson — PVO Human Capital Management"
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
  - PartyPerson
  - partyperson
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PartyPerson

## 📌 Visão Geral

Disponibiliza perfis de pessoas do Trading Community Architecture com dados de localização e contas de vendas. Utilizado como referência cruzada de pessoas entre HCM e CRM.

**Caminho:** `FscmTopModelAM.PartiesAnalyticsAM.PartyPerson`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 159 | 4 | 1 | 6 | 4% |

---

## 🔗 Tabelas Relacionadas

- [[hz_locations|HZ_LOCATIONS]] — 11 atributos
- [[hz_parties|HZ_PARTIES]] — 82 atributos (1 PKs, 4 BICC)
- [[hz_person_profiles|HZ_PERSON_PROFILES]] — 65 atributos (2 BICC)
- [[zca_sales_accounts|ZCA_SALES_ACCOUNTS]] — 1 atributos

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
| 6 | Building | BUILDING | — | — |
| 7 | FloorNumber | FLOOR_NUMBER | — | — |
| 8 | Latitude | LATITUDE | — | — |
| 9 | LocationId | LOCATION_ID | — | — |
| 10 | Longitude | LONGITUDE | — | — |
| 11 | PostalCodeExtension | POSTAL_PLUS4_CODE | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Address1 | ADDRESS1 | — | — |
| 2 | Address2 | ADDRESS2 | — | — |
| 3 | Address3 | ADDRESS3 | — | — |
| 4 | Address4 | ADDRESS4 | — | — |
| 5 | AnalysisFy | ANALYSIS_FY | — | — |
| 6 | CategoryCode | CATEGORY_CODE | — | — |
| 7 | CeoName | CEO_NAME | — | — |
| 8 | CertReasonCode | CERT_REASON_CODE | — | — |
| 9 | CertificationLevel | CERTIFICATION_LEVEL | — | — |
| 10 | City | CITY | — | — |
| 11 | Country | COUNTRY | — | — |
| 12 | County | COUNTY | — | — |
| 13 | CurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 14 | DateOfBirth | DATE_OF_BIRTH | — | — |
| 15 | DunsNumberC | DUNS_NUMBER_C | — | — |
| 16 | EmailAddress | EMAIL_ADDRESS | — | — |
| 17 | EmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 18 | FiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 19 | Gender | GENDER | — | — |
| 20 | GroupType | GROUP_TYPE | — | — |
| 21 | GsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 22 | HomeCountry | HOME_COUNTRY | — | — |
| 23 | HqBranchInd | HQ_BRANCH_IND | — | — |
| 24 | IdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 25 | IdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 26 | InternalFlag | INTERNAL_FLAG | — | — |
| 27 | JgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 28 | LanguageName | LANGUAGE_NAME | — | — |
| 29 | MaritalStatus | MARITAL_STATUS | — | — |
| 30 | MissionStatement | MISSION_STATEMENT | — | — |
| 31 | NextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 32 | OrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 33 | PartyId | PARTY_ID | 🔑 | ✅ |
| 34 | PartyName | PARTY_NAME | — | ✅ |
| 35 | PartyNumber | PARTY_NUMBER | — | ✅ |
| 36 | PartyPEOCreatedBy | CREATED_BY | — | — |
| 37 | PartyPEOCreatedByModule | CREATED_BY_MODULE | — | — |
| 38 | PartyPEOCreationDate | CREATION_DATE | — | — |
| 39 | PartyPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 40 | PartyPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 41 | PartyPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 42 | PartyPEOPartyId | PARTY_ID | — | — |
| 43 | PartySalesAccountId | SALES_ACCOUNT_ID | — | — |
| 44 | PartyType | PARTY_TYPE | — | — |
| 45 | PartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 46 | PersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 47 | PersonFirstName | PERSON_FIRST_NAME | — | — |
| 48 | PersonLastName | PERSON_LAST_NAME | — | — |
| 49 | PersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 50 | PersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 51 | PersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 52 | PersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 53 | PersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 54 | PersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 55 | PersonTitle | PERSON_TITLE | — | — |
| 56 | PostalCode | POSTAL_CODE | — | — |
| 57 | PrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 58 | PreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 59 | PreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 60 | PreferredName | PREFERRED_NAME | — | — |
| 61 | PreferredNameId | PREFERRED_NAME_ID | — | — |
| 62 | PrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 63 | PrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 64 | PrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 65 | PrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 66 | PrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 67 | PrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 68 | PrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | — |
| 69 | PrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 70 | PrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 71 | Province | PROVINCE | — | — |
| 72 | Salutation | SALUTATION | — | — |
| 73 | SicCode | SIC_CODE | — | — |
| 74 | SicCodeType | SIC_CODE_TYPE | — | — |
| 75 | State | STATE | — | — |
| 76 | Status | STATUS | — | — |
| 77 | ThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 78 | TradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 79 | Url | URL | — | — |
| 80 | UserGuid | USER_GUID | — | — |
| 81 | ValidatedFlag | VALIDATED_FLAG | — | — |
| 82 | YearEstablished | YEAR_ESTABLISHED | — | — |

### [[hz_person_profiles|HZ_PERSON_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | CleanlinessScore | CLEANLINESS_SCORE | — | — |
| 3 | Comments | COMMENTS | — | — |
| 4 | CompletenessScore | COMPLETENESS_SCORE | — | — |
| 5 | ContactRole | CONTACT_ROLE | — | — |
| 6 | CorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 7 | CurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 8 | CurrencyCode | CURRENCY_CODE | — | — |
| 9 | DataConfidenceScore | DATA_CONFIDENCE_SCORE | — | — |
| 10 | DateOfDeath | DATE_OF_DEATH | — | — |
| 11 | DeceasedFlag | DECEASED_FLAG | — | — |
| 12 | DeclaredEthnicity | DECLARED_ETHNICITY | — | — |
| 13 | Department | DEPARTMENT | — | — |
| 14 | DepartmentCode | DEPARTMENT_CODE | — | — |
| 15 | DoNotCallFlag | DO_NOT_CALL_FLAG | — | — |
| 16 | DoNotContactFlag | DO_NOT_CONTACT_FLAG | — | — |
| 17 | DoNotEmailFlag | DO_NOT_EMAIL_FLAG | — | — |
| 18 | DoNotMailFlag | DO_NOT_MAIL_FLAG | — | — |
| 19 | DuplicateIndicator | DUPLICATE_INDICATOR | — | — |
| 20 | DuplicateScore | DUPLICATE_SCORE | — | — |
| 21 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 22 | EffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 23 | EffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 24 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 25 | EnrichmentScore | ENRICHMENT_SCORE | — | — |
| 26 | HeadOfHouseholdFlag | HEAD_OF_HOUSEHOLD_FLAG | — | — |
| 27 | HouseholdIncome | HOUSEHOLD_INCOME | — | — |
| 28 | HouseholdSize | HOUSEHOLD_SIZE | — | — |
| 29 | JobTitle | JOB_TITLE | — | — |
| 30 | JobTitleCode | JOB_TITLE_CODE | — | — |
| 31 | LastAssignedDate | LAST_ASSIGNED_DATE | — | — |
| 32 | LastContactDate | LAST_CONTACT_DATE | — | — |
| 33 | LastEnrichmentDate | LAST_ENRICHMENT_DATE | — | — |
| 34 | LastKnownGps | LAST_KNOWN_GPS | — | — |
| 35 | LastScoreUpdateDate | LAST_SCORE_UPDATE_DATE | — | — |
| 36 | LastSourceUpdateDate | LAST_SOURCE_UPDATE_DATE | — | — |
| 37 | LastUpdateSourceSystem | LAST_UPDATE_SOURCE_SYSTEM | — | — |
| 38 | MaritalStatusEffectiveDate | MARITAL_STATUS_EFFECTIVE_DATE | — | — |
| 39 | NamedFlag | NAMED_FLAG | — | — |
| 40 | PersonInitials | PERSON_INITIALS | — | — |
| 41 | PersonName | PERSON_NAME | — | — |
| 42 | PersonPEOOwnerPartyId | OWNER_PARTY_ID | — | — |
| 43 | PersonProfileId | PERSON_PROFILE_ID | — | — |
| 44 | PersonProfilePEOCreatedBy | CREATED_BY | — | — |
| 45 | PersonProfilePEOCreatedByModule | CREATED_BY_MODULE | — | — |
| 46 | PersonProfilePEOCreationDate | CREATION_DATE | — | — |
| 47 | PersonProfilePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 48 | PersonProfilePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 49 | PersonProfilePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 50 | PersonProfilesPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 51 | PersonProfilesPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 52 | PersonProfilesPersonTitle | PERSON_TITLE | — | — |
| 53 | PersonalIncome | PERSONAL_INCOME | — | — |
| 54 | PlaceOfBirth | PLACE_OF_BIRTH | — | — |
| 55 | PrimaryCustomerId | PRIMARY_CUSTOMER_ID | — | — |
| 56 | PrimaryCustomerRelationshipId | PRIMARY_CUST_RELATIONSHIP_ID | — | — |
| 57 | RecencyScore | RECENCY_SCORE | — | — |
| 58 | RegistrationStatus | REGISTRATION_STATUS | — | — |
| 59 | RentOwnInd | RENT_OWN_IND | — | — |
| 60 | SalesAffinityCode | SALES_AFFINITY_CODE | — | — |
| 61 | SalesBuyingRoleCode | SALES_BUYING_ROLE_CODE | — | — |
| 62 | SalesProfileStatus | SALES_PROFILE_STATUS | — | — |
| 63 | SalesProfileType | SALES_PROFILE_TYPE | — | — |
| 64 | SuffixOverriddenFlag | SUFFIX_OVERRIDDEN_FLAG | — | — |
| 65 | UniqueNameSuffix | UNIQUE_NAME_SUFFIX | — | — |

### [[zca_sales_accounts|ZCA_SALES_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SalesAccountPEOSalesAccountId | SALES_ACCOUNT_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
