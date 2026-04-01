---
id: DOC-HCM-PVO-PartyUsage
doc_type: system-doc
title: "PartyUsage — PVO Human Capital Management"
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
  - PartyUsage
  - partyusage
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PartyUsage

## 📌 Visão Geral

Extrai atribuições de uso (usage) de entidades party com vigência temporal. Define os papéis que uma pessoa ou organização desempenha (empregado, fornecedor, cliente) no ecossistema.

**Caminho:** `FscmTopModelAM.PartiesAnalyticsAM.PartyUsage`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 95 | 2 | 1 | 5 | 5% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 81 atributos (2 BICC)
- [[hz_party_usg_assignments|HZ_PARTY_USG_ASSIGNMENTS]] — 14 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

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
| 33 | PartyEOComments | COMMENTS | — | — |
| 34 | PartyEOCreatedBy | CREATED_BY | — | — |
| 35 | PartyEOCreatedByModule | CREATED_BY_MODULE | — | — |
| 36 | PartyEOCreationDate | CREATION_DATE | — | — |
| 37 | PartyEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 38 | PartyEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 39 | PartyEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 40 | PartyEOPartyId | PARTY_ID | — | — |
| 41 | PartyEOStatus | STATUS | — | — |
| 42 | PartyName | PARTY_NAME | — | ✅ |
| 43 | PartyNumber | PARTY_NUMBER | — | — |
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
| 76 | ThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 77 | TradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 78 | Url | URL | — | — |
| 79 | UserGuid | USER_GUID | — | — |
| 80 | ValidatedFlag | VALIDATED_FLAG | — | — |
| 81 | YearEstablished | YEAR_ESTABLISHED | — | — |

### [[hz_party_usg_assignments|HZ_PARTY_USG_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | OwnerTableId | OWNER_TABLE_ID | — | — |
| 4 | OwnerTableName | OWNER_TABLE_NAME | — | — |
| 5 | PartyAssignmentComments | COMMENTS | — | — |
| 6 | PartyAssignmentCreatedByModule | CREATED_BY_MODULE | — | — |
| 7 | PartyAssignmentCreationDate | CREATION_DATE | — | — |
| 8 | PartyAssignmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | PartyAssignmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | PartyAssignmentLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | PartyAssignmentPartyId | PARTY_ID | — | — |
| 12 | PartyEOStatusFlag | STATUS_FLAG | — | — |
| 13 | PartyUsageCode | PARTY_USAGE_CODE | — | — |
| 14 | PartyUsgAssignmentId | PARTY_USG_ASSIGNMENT_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
