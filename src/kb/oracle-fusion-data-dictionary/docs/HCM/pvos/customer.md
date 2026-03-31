---
id: DOC-HCM-PVO-Customer
doc_type: system-doc
title: "Customer — PVO Human Capital Management"
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
  - Customer
  - customer
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Customer

## 📌 Visão Geral

Extrai dados de clientes (parties) com endereco e uso. Referencia para integracao HCM-financeiro em contextos de faturamento e relacionamento.

**Caminho:** `FscmTopModelAM.PartiesAnalyticsAM.Customer`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 107 | 3 | 1 | 57 | 53% |

---

## 🔗 Tabelas Relacionadas

- [[hz_locations|HZ_LOCATIONS]] — 11 atributos
- [[hz_parties|HZ_PARTIES]] — 82 atributos (1 PKs, 57 BICC)
- [[hz_party_usg_assignments|HZ_PARTY_USG_ASSIGNMENTS]] — 14 atributos

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
| 1 | Address1 | ADDRESS1 | — | ✅ |
| 2 | Address2 | ADDRESS2 | — | ✅ |
| 3 | Address3 | ADDRESS3 | — | ✅ |
| 4 | Address4 | ADDRESS4 | — | ✅ |
| 5 | AnalysisFy | ANALYSIS_FY | — | — |
| 6 | CategoryCode | CATEGORY_CODE | — | ✅ |
| 7 | CeoName | CEO_NAME | — | — |
| 8 | CertReasonCode | CERT_REASON_CODE | — | ✅ |
| 9 | CertificationLevel | CERTIFICATION_LEVEL | — | ✅ |
| 10 | City | CITY | — | ✅ |
| 11 | Comments | COMMENTS | — | ✅ |
| 12 | Country | COUNTRY | — | ✅ |
| 13 | County | COUNTY | — | ✅ |
| 14 | CreatedBy | CREATED_BY | — | ✅ |
| 15 | CreatedByModule | CREATED_BY_MODULE | — | — |
| 16 | CreationDate | CREATION_DATE | — | ✅ |
| 17 | CurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | ✅ |
| 18 | DateOfBirth | DATE_OF_BIRTH | — | ✅ |
| 19 | DunsNumberC | DUNS_NUMBER_C | — | ✅ |
| 20 | EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 21 | EmployeesTotal | EMPLOYEES_TOTAL | — | ✅ |
| 22 | FiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 23 | Gender | GENDER | — | ✅ |
| 24 | GroupType | GROUP_TYPE | — | — |
| 25 | GsaIndicatorFlag | GSA_INDICATOR_FLAG | — | ✅ |
| 26 | HomeCountry | HOME_COUNTRY | — | — |
| 27 | HqBranchInd | HQ_BRANCH_IND | — | — |
| 28 | IdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 29 | IdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 30 | InternalFlag | INTERNAL_FLAG | — | — |
| 31 | JgzzFiscalCode | JGZZ_FISCAL_CODE | — | ✅ |
| 32 | LanguageName | LANGUAGE_NAME | — | ✅ |
| 33 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 35 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 36 | MaritalStatus | MARITAL_STATUS | — | ✅ |
| 37 | MissionStatement | MISSION_STATEMENT | — | — |
| 38 | NextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | ✅ |
| 39 | OrigSystemReference | ORIG_SYSTEM_REFERENCE | — | ✅ |
| 40 | PartyId | PARTY_ID | 🔑 | ✅ |
| 41 | PartyName | PARTY_NAME | — | ✅ |
| 42 | PartyNumber | PARTY_NUMBER | — | ✅ |
| 43 | PartyType | PARTY_TYPE | — | ✅ |
| 44 | PartyUniqueName | PARTY_UNIQUE_NAME | — | ✅ |
| 45 | PersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | ✅ |
| 46 | PersonFirstName | PERSON_FIRST_NAME | — | — |
| 47 | PersonLastName | PERSON_LAST_NAME | — | ✅ |
| 48 | PersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 49 | PersonMiddleName | PERSON_MIDDLE_NAME | — | ✅ |
| 50 | PersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 51 | PersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | ✅ |
| 52 | PersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | ✅ |
| 53 | PersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 54 | PersonTitle | PERSON_TITLE | — | ✅ |
| 55 | PostalCode | POSTAL_CODE | — | ✅ |
| 56 | PrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | ✅ |
| 57 | PreferredContactMethod | PREFERRED_CONTACT_METHOD | — | ✅ |
| 58 | PreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | ✅ |
| 59 | PreferredName | PREFERRED_NAME | — | ✅ |
| 60 | PreferredNameId | PREFERRED_NAME_ID | — | — |
| 61 | PrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 62 | PrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | ✅ |
| 63 | PrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 64 | PrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | ✅ |
| 65 | PrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | ✅ |
| 66 | PrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 67 | PrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | ✅ |
| 68 | PrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 69 | PrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 70 | Province | PROVINCE | — | ✅ |
| 71 | RequestId | REQUEST_ID | — | — |
| 72 | Salutation | SALUTATION | — | ✅ |
| 73 | SicCode | SIC_CODE | — | ✅ |
| 74 | SicCodeType | SIC_CODE_TYPE | — | ✅ |
| 75 | State | STATE | — | ✅ |
| 76 | Status | STATUS | — | ✅ |
| 77 | ThirdPartyFlag | THIRD_PARTY_FLAG | — | ✅ |
| 78 | TradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 79 | Url | URL | — | ✅ |
| 80 | UserGuid | USER_GUID | — | — |
| 81 | ValidatedFlag | VALIDATED_FLAG | — | ✅ |
| 82 | YearEstablished | YEAR_ESTABLISHED | — | ✅ |

### [[hz_party_usg_assignments|HZ_PARTY_USG_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Comments1 | COMMENTS | — | — |
| 2 | CreatedBy1 | CREATED_BY | — | — |
| 3 | CreatedByModule1 | CREATED_BY_MODULE | — | — |
| 4 | CreationDate1 | CREATION_DATE | — | — |
| 5 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | EffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 7 | LastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 8 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 9 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 10 | OwnerTableId | OWNER_TABLE_ID | — | — |
| 11 | OwnerTableName | OWNER_TABLE_NAME | — | — |
| 12 | PartyUsageCode | PARTY_USAGE_CODE | — | — |
| 13 | PartyUsgAssignmentId | PARTY_USG_ASSIGNMENT_ID | — | — |
| 14 | StatusFlag | STATUS_FLAG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
