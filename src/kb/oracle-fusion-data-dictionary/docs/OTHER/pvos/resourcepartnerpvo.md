---
id: DOC-OTHER-PVO-ResourcePartnerPVO
doc_type: system-doc
title: "ResourcePartnerPVO — PVO Cross-Module"
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
  - ResourcePartnerPVO
  - resourcepartnerpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ResourcePartnerPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Resource Partner. Acessa as tabelas: FND_TREE_VERSION_VL, HZ_PARTIES, HZ_PARTY_USG_ASSIGNMENTS (+3).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ResourcesAnalyticsAM.ResourcePartnerPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 146 | 6 | 2 | 6 | 4% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_tree_version_vl|FND_TREE_VERSION_VL]] — 6 atributos
- [[hz_parties|HZ_PARTIES]] — 120 atributos (2 BICC)
- [[hz_party_usg_assignments|HZ_PARTY_USG_ASSIGNMENTS]] — 2 atributos (1 PKs, 1 BICC)
- [[jtf_rs_rep_managers|JTF_RS_REP_MANAGERS]] — 5 atributos (1 BICC)
- [[jtf_rs_resource_profiles|JTF_RS_RESOURCE_PROFILES]] — 11 atributos (1 PKs, 2 BICC)
- [[per_users|PER_USERS]] — 2 atributos

---

## ⚙️ Atributos

### [[fnd_tree_version_vl|FND_TREE_VERSION_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | FndTreeVerStatus | STATUS | — | — |
| 4 | TreeCode | TREE_CODE | — | — |
| 5 | TreeStructureCode | TREE_STRUCTURE_CODE | — | — |
| 6 | TreeVersionId | TREE_VERSION_ID | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Address1 | ADDRESS1 | — | — |
| 2 | Address2 | ADDRESS2 | — | — |
| 3 | Address3 | ADDRESS3 | — | — |
| 4 | Address4 | ADDRESS4 | — | — |
| 5 | AnalysisFy | ANALYSIS_FY | — | — |
| 6 | CeoName | CEO_NAME | — | — |
| 7 | CertReasonCode | CERT_REASON_CODE | — | — |
| 8 | CertificationLevel | CERTIFICATION_LEVEL | — | — |
| 9 | City | CITY | — | — |
| 10 | Comments | COMMENTS | — | — |
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
| 29 | ManagerAddress1 | ADDRESS1 | — | — |
| 30 | ManagerAddress2 | ADDRESS2 | — | — |
| 31 | ManagerAddress3 | ADDRESS3 | — | — |
| 32 | ManagerAddress4 | ADDRESS4 | — | — |
| 33 | ManagerCity | CITY | — | — |
| 34 | ManagerCountry | COUNTRY | — | — |
| 35 | ManagerCounty | COUNTY | — | — |
| 36 | ManagerCreatedBy | CREATED_BY | — | — |
| 37 | ManagerCreationDate | CREATION_DATE | — | — |
| 38 | ManagerEmailAddress | EMAIL_ADDRESS | — | — |
| 39 | ManagerHomeCountry | HOME_COUNTRY | — | — |
| 40 | ManagerLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 41 | ManagerLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 42 | ManagerLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 43 | ManagerOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 44 | ManagerPartyId | PARTY_ID | — | — |
| 45 | ManagerPartyName | PARTY_NAME | — | — |
| 46 | ManagerPartyNumber | PARTY_NUMBER | — | — |
| 47 | ManagerPartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 48 | ManagerPersonFirstName | PERSON_FIRST_NAME | — | — |
| 49 | ManagerPersonLastName | PERSON_LAST_NAME | — | — |
| 50 | ManagerPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 51 | ManagerPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 52 | ManagerPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 53 | ManagerPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 54 | ManagerPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 55 | ManagerPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 56 | ManagerPersonTitle | PERSON_TITLE | — | — |
| 57 | ManagerPostalCode | POSTAL_CODE | — | — |
| 58 | ManagerPreferredName | PREFERRED_NAME | — | — |
| 59 | ManagerPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 60 | ManagerPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 61 | ManagerPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 62 | ManagerPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 63 | ManagerPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | — |
| 64 | ManagerPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 65 | ManagerProvince | PROVINCE | — | — |
| 66 | ManagerSalutation | SALUTATION | — | — |
| 67 | ManagerState | STATE | — | — |
| 68 | ManagerStatus | STATUS | — | — |
| 69 | ManagerUserGuid | USER_GUID | — | — |
| 70 | MaritalStatus | MARITAL_STATUS | — | — |
| 71 | MissionStatement | MISSION_STATEMENT | — | — |
| 72 | NextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 73 | OrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 74 | PartyName | PARTY_NAME | — | — |
| 75 | PartyNumber | PARTY_NUMBER | — | — |
| 76 | PartyPEOCreatedBy | CREATED_BY | — | — |
| 77 | PartyPEOCreatedByModule | CREATED_BY_MODULE | — | — |
| 78 | PartyPEOCreationDate | CREATION_DATE | — | — |
| 79 | PartyPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 80 | PartyPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 81 | PartyPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 82 | PartyPEOPartyId | PARTY_ID | — | ✅ |
| 83 | PartyType | PARTY_TYPE | — | — |
| 84 | PersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 85 | PersonFirstName | PERSON_FIRST_NAME | — | — |
| 86 | PersonLastName | PERSON_LAST_NAME | — | — |
| 87 | PersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 88 | PersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 89 | PersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 90 | PersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 91 | PersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 92 | PersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 93 | PersonTitle | PERSON_TITLE | — | — |
| 94 | PostalCode | POSTAL_CODE | — | — |
| 95 | PrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 96 | PreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 97 | PreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 98 | PreferredName | PREFERRED_NAME | — | — |
| 99 | PreferredNameId | PREFERRED_NAME_ID | — | — |
| 100 | PrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 101 | PrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 102 | PrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 103 | PrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 104 | PrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 105 | PrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 106 | PrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | — |
| 107 | PrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 108 | PrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 109 | Province | PROVINCE | — | — |
| 110 | Salutation | SALUTATION | — | — |
| 111 | SicCode | SIC_CODE | — | — |
| 112 | SicCodeType | SIC_CODE_TYPE | — | — |
| 113 | State | STATE | — | — |
| 114 | Status | STATUS | — | — |
| 115 | ThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 116 | TradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 117 | Url | URL | — | — |
| 118 | UserGuid | USER_GUID | — | — |
| 119 | ValidatedFlag | VALIDATED_FLAG | — | — |
| 120 | YearEstablished | YEAR_ESTABLISHED | — | — |

### [[hz_party_usg_assignments|HZ_PARTY_USG_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyUsageCode | PARTY_USAGE_CODE | — | — |
| 2 | PartyUsgAssignmentId | PARTY_USG_ASSIGNMENT_ID | 🔑 | ✅ |

### [[jtf_rs_rep_managers|JTF_RS_REP_MANAGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DenormMgrId | DENORM_MGR_ID | — | — |
| 2 | ParentResourceId | PARENT_RESOURCE_ID | — | — |
| 3 | PrimaryOrg | GROUP_ID | — | ✅ |
| 4 | RptgMgrEndDateActive | END_DATE_ACTIVE | — | — |
| 5 | RptgMgrStartDateActive | START_DATE_ACTIVE | — | — |

### [[jtf_rs_resource_profiles|JTF_RS_RESOURCE_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EndDateActive | END_DATE_ACTIVE | — | — |
| 2 | ResourcePEOCreatedBy | CREATED_BY | — | — |
| 3 | ResourcePEOCreatedByModule | CREATED_BY_MODULE | — | — |
| 4 | ResourcePEOCreationDate | CREATION_DATE | — | — |
| 5 | ResourcePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ResourcePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ResourcePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ResourcePEOPartyId | PARTY_ID | — | — |
| 9 | ResourceProfileId | RESOURCE_PROFILE_ID | 🔑 | ✅ |
| 10 | StartDateActive | START_DATE_ACTIVE | — | — |
| 11 | TimezoneCode | TIMEZONE_CODE | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserId | USER_ID | — | — |
| 2 | Username | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
