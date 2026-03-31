---
id: DOC-OTHER-PVO-Person
doc_type: system-doc
title: "Person — PVO Cross-Module"
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
  - Person
  - person
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Person

## 📌 Visão Geral

View Object para extração BICC de dados de Person. Acessa as tabelas: HZ_PARTIES, HZ_PERSON_PROFILES.

**Caminho:** `FscmTopModelAM.PartiesAnalyticsAM.Person`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 117 | 2 | 1 | 29 | 25% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 29 atributos
- [[hz_person_profiles|HZ_PERSON_PROFILES]] — 88 atributos (1 PKs, 29 BICC)

---

## ⚙️ Atributos

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonOwnerPartyId | PARTY_ID | — | — |
| 2 | PersonOwnerPartyName | PARTY_NAME | — | — |
| 3 | PersonPartyAddress1 | ADDRESS1 | — | — |
| 4 | PersonPartyAddress2 | ADDRESS2 | — | — |
| 5 | PersonPartyAddress3 | ADDRESS3 | — | — |
| 6 | PersonPartyAddress4 | ADDRESS4 | — | — |
| 7 | PersonPartyCity | CITY | — | — |
| 8 | PersonPartyCountry | COUNTRY | — | — |
| 9 | PersonPartyCounty | COUNTY | — | — |
| 10 | PersonPartyEmailAddress | EMAIL_ADDRESS | — | — |
| 11 | PersonPartyLanguageName | LANGUAGE_NAME | — | — |
| 12 | PersonPartyPartyId | PARTY_ID | — | — |
| 13 | PersonPartyPartyName | PARTY_NAME | — | — |
| 14 | PersonPartyPartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 15 | PersonPartyPostalCode | POSTAL_CODE | — | — |
| 16 | PersonPartyPreferredName | PREFERRED_NAME | — | — |
| 17 | PersonPartyPreferredNameId | PREFERRED_NAME_ID | — | — |
| 18 | PersonPartyPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 19 | PersonPartyPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 20 | PersonPartyPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 21 | PersonPartyPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 22 | PersonPartyPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 23 | PersonPartyPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 24 | PersonPartyPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | — |
| 25 | PersonPartyPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 26 | PersonPartyPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 27 | PersonPartyProvince | PROVINCE | — | — |
| 28 | PersonPartyState | STATE | — | — |
| 29 | PersonPartyUrl | URL | — | — |

### [[hz_person_profiles|HZ_PERSON_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | CertReasonCode | CERT_REASON_CODE | — | — |
| 3 | CertificationLevel | CERTIFICATION_LEVEL | — | — |
| 4 | CleanlinessScore | CLEANLINESS_SCORE | — | — |
| 5 | Comments | COMMENTS | — | ✅ |
| 6 | CompletenessScore | COMPLETENESS_SCORE | — | — |
| 7 | ContactRole | CONTACT_ROLE | — | — |
| 8 | CorpCurrencyCode | CORP_CURRENCY_CODE | — | ✅ |
| 9 | CreatedBy | CREATED_BY | — | — |
| 10 | CreatedByModule | CREATED_BY_MODULE | — | — |
| 11 | CreationDate | CREATION_DATE | — | — |
| 12 | CurcyConvRateType | CURCY_CONV_RATE_TYPE | — | ✅ |
| 13 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 14 | DataCloudStatus | DATA_CLOUD_STATUS | — | — |
| 15 | DataConfidenceScore | DATA_CONFIDENCE_SCORE | — | — |
| 16 | DateOfBirth | DATE_OF_BIRTH | — | ✅ |
| 17 | DateOfDeath | DATE_OF_DEATH | — | ✅ |
| 18 | DeceasedFlag | DECEASED_FLAG | — | ✅ |
| 19 | DeclaredEthnicity | DECLARED_ETHNICITY | — | ✅ |
| 20 | Department | DEPARTMENT | — | — |
| 21 | DepartmentCode | DEPARTMENT_CODE | — | — |
| 22 | DoNotCallFlag | DO_NOT_CALL_FLAG | — | — |
| 23 | DoNotContactFlag | DO_NOT_CONTACT_FLAG | — | — |
| 24 | DoNotEmailFlag | DO_NOT_EMAIL_FLAG | — | — |
| 25 | DoNotMailFlag | DO_NOT_MAIL_FLAG | — | — |
| 26 | DuplicateIndicator | DUPLICATE_INDICATOR | — | — |
| 27 | DuplicateScore | DUPLICATE_SCORE | — | — |
| 28 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 29 | EffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 30 | EffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 31 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 32 | EnrichmentScore | ENRICHMENT_SCORE | — | — |
| 33 | Gender | GENDER | — | ✅ |
| 34 | HeadOfHouseholdFlag | HEAD_OF_HOUSEHOLD_FLAG | — | ✅ |
| 35 | HouseholdIncome | HOUSEHOLD_INCOME | — | ✅ |
| 36 | HouseholdSize | HOUSEHOLD_SIZE | — | ✅ |
| 37 | InternalFlag | INTERNAL_FLAG | — | — |
| 38 | JgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 39 | JobTitle | JOB_TITLE | — | — |
| 40 | JobTitleCode | JOB_TITLE_CODE | — | — |
| 41 | LastAssignedDate | LAST_ASSIGNED_DATE | — | — |
| 42 | LastContactDate | LAST_CONTACT_DATE | — | — |
| 43 | LastEnrichmentDate | LAST_ENRICHMENT_DATE | — | — |
| 44 | LastKnownGps | LAST_KNOWN_GPS | — | ✅ |
| 45 | LastScoreUpdateDate | LAST_SCORE_UPDATE_DATE | — | — |
| 46 | LastSourceUpdateDate | LAST_SOURCE_UPDATE_DATE | — | — |
| 47 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 48 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 49 | LastUpdateSourceSystem | LAST_UPDATE_SOURCE_SYSTEM | — | — |
| 50 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 51 | MaritalStatus | MARITAL_STATUS | — | ✅ |
| 52 | MaritalStatusEffectiveDate | MARITAL_STATUS_EFFECTIVE_DATE | — | — |
| 53 | NamedFlag | NAMED_FLAG | — | — |
| 54 | OwnerPartyId | OWNER_PARTY_ID | — | — |
| 55 | PartyId | PARTY_ID | — | — |
| 56 | PartyNumber | PARTY_NUMBER | — | — |
| 57 | PersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 58 | PersonFirstName | PERSON_FIRST_NAME | — | ✅ |
| 59 | PersonInitials | PERSON_INITIALS | — | ✅ |
| 60 | PersonLastName | PERSON_LAST_NAME | — | ✅ |
| 61 | PersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | ✅ |
| 62 | PersonMiddleName | PERSON_MIDDLE_NAME | — | ✅ |
| 63 | PersonName | PERSON_NAME | — | ✅ |
| 64 | PersonNameSuffix | PERSON_NAME_SUFFIX | — | ✅ |
| 65 | PersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 66 | PersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 67 | PersonProfileId | PERSON_PROFILE_ID | 🔑 | ✅ |
| 68 | PersonSecondLastName | PERSON_SECOND_LAST_NAME | — | ✅ |
| 69 | PersonTitle | PERSON_TITLE | — | ✅ |
| 70 | PersonalIncome | PERSONAL_INCOME | — | ✅ |
| 71 | PlaceOfBirth | PLACE_OF_BIRTH | — | ✅ |
| 72 | PrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 73 | PreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 74 | PreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 75 | PrimaryCustomerId | PRIMARY_CUSTOMER_ID | — | — |
| 76 | PrimaryCustomerRelationshipId | PRIMARY_CUST_RELATIONSHIP_ID | — | — |
| 77 | RecencyScore | RECENCY_SCORE | — | — |
| 78 | RegistrationStatus | REGISTRATION_STATUS | — | — |
| 79 | RentOwnInd | RENT_OWN_IND | — | ✅ |
| 80 | SalesAffinityCode | SALES_AFFINITY_CODE | — | — |
| 81 | SalesBuyingRoleCode | SALES_BUYING_ROLE_CODE | — | — |
| 82 | SalesProfileStatus | SALES_PROFILE_STATUS | — | — |
| 83 | SalesProfileType | SALES_PROFILE_TYPE | — | — |
| 84 | Salutation | SALUTATION | — | — |
| 85 | Status | STATUS | — | — |
| 86 | SuffixOverriddenFlag | SUFFIX_OVERRIDDEN_FLAG | — | — |
| 87 | UniqueNameSuffix | UNIQUE_NAME_SUFFIX | — | — |
| 88 | ValidityScore | VALIDITY_SCORE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
