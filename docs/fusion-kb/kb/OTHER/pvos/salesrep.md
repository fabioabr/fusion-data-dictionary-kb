---
id: DOC-OTHER-PVO-SalesRep
doc_type: system-doc
title: "SalesRep — PVO Cross-Module"
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
  - SalesRep
  - salesrep
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SalesRep

## 📌 Visão Geral

View Object para extração BICC de dados de Sales Rep. Acessa as tabelas: AR_SALES_CREDIT_TYPES, HZ_PARTIES, JTF_RS_SALESREPS.

**Caminho:** `FscmTopModelAM.ResourcesAnalyticsAM.SalesRep`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 123 | 3 | 2 | 14 | 11% |

---

## 🔗 Tabelas Relacionadas

- [[ar_sales_credit_types|AR_SALES_CREDIT_TYPES]] — 27 atributos (1 BICC)
- [[hz_parties|HZ_PARTIES]] — 80 atributos (1 PKs, 5 BICC)
- [[jtf_rs_salesreps|JTF_RS_SALESREPS]] — 16 atributos (1 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[ar_sales_credit_types|AR_SALES_CREDIT_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute1 | ATTRIBUTE1 | — | — |
| 2 | Attribute10 | ATTRIBUTE10 | — | — |
| 3 | Attribute11 | ATTRIBUTE11 | — | — |
| 4 | Attribute12 | ATTRIBUTE12 | — | — |
| 5 | Attribute13 | ATTRIBUTE13 | — | — |
| 6 | Attribute14 | ATTRIBUTE14 | — | — |
| 7 | Attribute15 | ATTRIBUTE15 | — | — |
| 8 | Attribute2 | ATTRIBUTE2 | — | — |
| 9 | Attribute3 | ATTRIBUTE3 | — | — |
| 10 | Attribute4 | ATTRIBUTE4 | — | — |
| 11 | Attribute5 | ATTRIBUTE5 | — | — |
| 12 | Attribute6 | ATTRIBUTE6 | — | — |
| 13 | Attribute7 | ATTRIBUTE7 | — | — |
| 14 | Attribute8 | ATTRIBUTE8 | — | — |
| 15 | Attribute9 | ATTRIBUTE9 | — | — |
| 16 | Context | CONTEXT | — | — |
| 17 | Description | DESCRIPTION | — | — |
| 18 | EnabledFlag | ENABLED_FLAG | — | — |
| 19 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | QuotaFlag | QUOTA_FLAG | — | — |
| 21 | SCTPEOCreatedBy | CREATED_BY | — | — |
| 22 | SCTPEOCreationDate | CREATION_DATE | — | — |
| 23 | SCTPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 24 | SCTPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 25 | SCTPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 26 | SCTPEOSalesCreditTypeId | SALES_CREDIT_TYPE_ID | — | — |
| 27 | SalesCreditTypeName | NAME | — | ✅ |

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
| 11 | Comments | COMMENTS | — | — |
| 12 | Country | COUNTRY | — | — |
| 13 | County | COUNTY | — | — |
| 14 | CurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 15 | DateOfBirth | DATE_OF_BIRTH | — | — |
| 16 | DunsNumberC | DUNS_NUMBER_C | — | — |
| 17 | EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 18 | EmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 19 | FiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 20 | Gender | GENDER | — | — |
| 21 | GroupType | GROUP_TYPE | — | — |
| 22 | GsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 23 | HomeCountry | HOME_COUNTRY | — | — |
| 24 | HqBranchInd | HQ_BRANCH_IND | — | — |
| 25 | IdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 26 | IdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 27 | InternalFlag | INTERNAL_FLAG | — | — |
| 28 | JgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 29 | LanguageName | LANGUAGE_NAME | — | — |
| 30 | MaritalStatus | MARITAL_STATUS | — | — |
| 31 | MissionStatement | MISSION_STATEMENT | — | — |
| 32 | NextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 33 | OrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 34 | PartyId | PARTY_ID | 🔑 | ✅ |
| 35 | PartyName | PARTY_NAME | — | ✅ |
| 36 | PartyNumber | PARTY_NUMBER | — | — |
| 37 | PartyPEOCreatedByModule | CREATED_BY_MODULE | — | — |
| 38 | PartyPEOCreationDate | CREATION_DATE | — | — |
| 39 | PartyPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 40 | PartyPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 41 | PartyPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 42 | PartyPEOPEOCreatedBy | CREATED_BY | — | — |
| 43 | PartyPEOStatus | STATUS | — | — |
| 44 | PartyType | PARTY_TYPE | — | — |
| 45 | PersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 46 | PersonFirstName | PERSON_FIRST_NAME | — | — |
| 47 | PersonLastName | PERSON_LAST_NAME | — | — |
| 48 | PersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 49 | PersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 50 | PersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 51 | PersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 52 | PersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 53 | PersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 54 | PersonTitle | PERSON_TITLE | — | — |
| 55 | PostalCode | POSTAL_CODE | — | — |
| 56 | PrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 57 | PreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 58 | PreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 59 | PreferredName | PREFERRED_NAME | — | — |
| 60 | PreferredNameId | PREFERRED_NAME_ID | — | — |
| 61 | PrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 62 | PrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 63 | PrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 64 | PrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 65 | PrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 66 | PrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 67 | PrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | ✅ |
| 68 | PrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 69 | PrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 70 | Province | PROVINCE | — | — |
| 71 | Salutation | SALUTATION | — | — |
| 72 | SicCode | SIC_CODE | — | — |
| 73 | SicCodeType | SIC_CODE_TYPE | — | — |
| 74 | State | STATE | — | — |
| 75 | ThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 76 | TradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 77 | Url | URL | — | — |
| 78 | UserGuid | USER_GUID | — | — |
| 79 | ValidatedFlag | VALIDATED_FLAG | — | — |
| 80 | YearEstablished | YEAR_ESTABLISHED | — | — |

### [[jtf_rs_salesreps|JTF_RS_SALESREPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EndDateActive | END_DATE_ACTIVE | — | ✅ |
| 2 | ResourceId | RESOURCE_ID | — | ✅ |
| 3 | ResourceSalesrepId | RESOURCE_SALESREP_ID | 🔑 | ✅ |
| 4 | ResourceSalesrepPEOCreatedBy | CREATED_BY | — | — |
| 5 | ResourceSalesrepPEOCreationDate | CREATION_DATE | — | — |
| 6 | ResourceSalesrepPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ResourceSalesrepPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ResourceSalesrepPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ResourceSalesrepPEOStatus | STATUS | — | ✅ |
| 10 | SalesCreditTypeId | SALES_CREDIT_TYPE_ID | — | ✅ |
| 11 | SalesTaxGeocode | SALES_TAX_GEOCODE | — | — |
| 12 | SalesTaxInsideCityLimits | SALES_TAX_INSIDE_CITY_LIMITS | — | — |
| 13 | SalesrepNumber | SALESREP_NUMBER | — | ✅ |
| 14 | SetId | SET_ID | — | — |
| 15 | StartDateActive | START_DATE_ACTIVE | — | ✅ |
| 16 | WhUpdateDate | WH_UPDATE_DATE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
