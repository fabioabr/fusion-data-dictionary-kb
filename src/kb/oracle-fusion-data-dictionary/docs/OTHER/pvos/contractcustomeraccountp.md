---
id: DOC-OTHER-PVO-ContractCustomerAccountP
doc_type: system-doc
title: "ContractCustomerAccountP — PVO Cross-Module"
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
  - ContractCustomerAccountP
  - contractcustomeraccountp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContractCustomerAccountP

## 📌 Visão Geral

View Object para extração BICC de dados de Contract Customer Account P. Acessa as tabelas: HZ_CUST_ACCOUNTS, HZ_PARTIES.

**Caminho:** `FscmTopModelAM.ContractsCoreAM.ContractCustomerAccountP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 114 | 2 | 1 | 114 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 32 atributos (1 PKs, 32 BICC)
- [[hz_parties|HZ_PARTIES]] — 82 atributos (82 BICC)

---

## ⚙️ Atributos

### [[hz_cust_accounts|HZ_CUST_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustomerAccountAccountEstablishedDate | ACCOUNT_ESTABLISHED_DATE | — | ✅ |
| 2 | CustomerAccountAccountName | ACCOUNT_NAME | — | ✅ |
| 3 | CustomerAccountAccountNumber | ACCOUNT_NUMBER | — | ✅ |
| 4 | CustomerAccountAccountTerminationDate | ACCOUNT_TERMINATION_DATE | — | ✅ |
| 5 | CustomerAccountArrivalsetsIncludeLinesFlag | ARRIVALSETS_INCLUDE_LINES_FLAG | — | ✅ |
| 6 | CustomerAccountAutopayFlag | AUTOPAY_FLAG | — | ✅ |
| 7 | CustomerAccountComments | COMMENTS | — | ✅ |
| 8 | CustomerAccountCoterminateDayMonth | COTERMINATE_DAY_MONTH | — | ✅ |
| 9 | CustomerAccountCreatedBy | CREATED_BY | — | ✅ |
| 10 | CustomerAccountCreatedByModule | CREATED_BY_MODULE | — | ✅ |
| 11 | CustomerAccountCreationDate | CREATION_DATE | — | ✅ |
| 12 | CustomerAccountCustAccountId | CUST_ACCOUNT_ID | 🔑 | ✅ |
| 13 | CustomerAccountCustomerClassCode | CUSTOMER_CLASS_CODE | — | ✅ |
| 14 | CustomerAccountCustomerType | CUSTOMER_TYPE | — | ✅ |
| 15 | CustomerAccountDateTypePreference | DATE_TYPE_PREFERENCE | — | ✅ |
| 16 | CustomerAccountDepositRefundMethod | DEPOSIT_REFUND_METHOD | — | ✅ |
| 17 | CustomerAccountHeldBillExpirationDate | HELD_BILL_EXPIRATION_DATE | — | ✅ |
| 18 | CustomerAccountHoldBillFlag | HOLD_BILL_FLAG | — | ✅ |
| 19 | CustomerAccountLastBatchId | LAST_BATCH_ID | — | ✅ |
| 20 | CustomerAccountLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | CustomerAccountLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 22 | CustomerAccountLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 23 | CustomerAccountNpaNumber | NPA_NUMBER | — | ✅ |
| 24 | CustomerAccountOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | ✅ |
| 25 | CustomerAccountPartyId | PARTY_ID | — | ✅ |
| 26 | CustomerAccountSellingPartyId | SELLING_PARTY_ID | — | ✅ |
| 27 | CustomerAccountSourceCode | SOURCE_CODE | — | ✅ |
| 28 | CustomerAccountStatus | STATUS | — | ✅ |
| 29 | CustomerAccountStatusUpdateDate | STATUS_UPDATE_DATE | — | ✅ |
| 30 | CustomerAccountTaxCode | TAX_CODE | — | ✅ |
| 31 | CustomerAccountTaxHeaderLevelFlag | TAX_HEADER_LEVEL_FLAG | — | ✅ |
| 32 | CustomerAccountTaxRoundingRule | TAX_ROUNDING_RULE | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyAddress1 | ADDRESS1 | — | ✅ |
| 2 | PartyAddress2 | ADDRESS2 | — | ✅ |
| 3 | PartyAddress3 | ADDRESS3 | — | ✅ |
| 4 | PartyAddress4 | ADDRESS4 | — | ✅ |
| 5 | PartyAnalysisFy | ANALYSIS_FY | — | ✅ |
| 6 | PartyCategoryCode | CATEGORY_CODE | — | ✅ |
| 7 | PartyCeoName | CEO_NAME | — | ✅ |
| 8 | PartyCertReasonCode | CERT_REASON_CODE | — | ✅ |
| 9 | PartyCertificationLevel | CERTIFICATION_LEVEL | — | ✅ |
| 10 | PartyCity | CITY | — | ✅ |
| 11 | PartyComments | COMMENTS | — | ✅ |
| 12 | PartyCountry | COUNTRY | — | ✅ |
| 13 | PartyCounty | COUNTY | — | ✅ |
| 14 | PartyCreatedBy | CREATED_BY | — | ✅ |
| 15 | PartyCreatedByModule | CREATED_BY_MODULE | — | ✅ |
| 16 | PartyCreationDate | CREATION_DATE | — | ✅ |
| 17 | PartyCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | ✅ |
| 18 | PartyDateOfBirth | DATE_OF_BIRTH | — | ✅ |
| 19 | PartyDunsNumberC | DUNS_NUMBER_C | — | ✅ |
| 20 | PartyEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 21 | PartyEmployeesTotal | EMPLOYEES_TOTAL | — | ✅ |
| 22 | PartyFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | ✅ |
| 23 | PartyGender | GENDER | — | ✅ |
| 24 | PartyGroupType | GROUP_TYPE | — | ✅ |
| 25 | PartyGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | ✅ |
| 26 | PartyHomeCountry | HOME_COUNTRY | — | ✅ |
| 27 | PartyHqBranchInd | HQ_BRANCH_IND | — | ✅ |
| 28 | PartyIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | ✅ |
| 29 | PartyIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | ✅ |
| 30 | PartyInternalFlag | INTERNAL_FLAG | — | ✅ |
| 31 | PartyJgzzFiscalCode | JGZZ_FISCAL_CODE | — | ✅ |
| 32 | PartyLanguageName | LANGUAGE_NAME | — | ✅ |
| 33 | PartyLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | PartyLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 35 | PartyLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 36 | PartyMaritalStatus | MARITAL_STATUS | — | ✅ |
| 37 | PartyMissionStatement | MISSION_STATEMENT | — | ✅ |
| 38 | PartyNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | ✅ |
| 39 | PartyObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 40 | PartyOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | ✅ |
| 41 | PartyPartyId | PARTY_ID | — | ✅ |
| 42 | PartyPartyName | PARTY_NAME | — | ✅ |
| 43 | PartyPartyNumber | PARTY_NUMBER | — | ✅ |
| 44 | PartyPartyType | PARTY_TYPE | — | ✅ |
| 45 | PartyPartyUniqueName | PARTY_UNIQUE_NAME | — | ✅ |
| 46 | PartyPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | ✅ |
| 47 | PartyPersonFirstName | PERSON_FIRST_NAME | — | ✅ |
| 48 | PartyPersonLastName | PERSON_LAST_NAME | — | ✅ |
| 49 | PartyPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | ✅ |
| 50 | PartyPersonMiddleName | PERSON_MIDDLE_NAME | — | ✅ |
| 51 | PartyPersonNameSuffix | PERSON_NAME_SUFFIX | — | ✅ |
| 52 | PartyPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | ✅ |
| 53 | PartyPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | ✅ |
| 54 | PartyPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | ✅ |
| 55 | PartyPersonTitle | PERSON_TITLE | — | ✅ |
| 56 | PartyPostalCode | POSTAL_CODE | — | ✅ |
| 57 | PartyPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | ✅ |
| 58 | PartyPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | ✅ |
| 59 | PartyPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | ✅ |
| 60 | PartyPreferredName | PREFERRED_NAME | — | ✅ |
| 61 | PartyPreferredNameId | PREFERRED_NAME_ID | — | ✅ |
| 62 | PartyPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | ✅ |
| 63 | PartyPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | ✅ |
| 64 | PartyPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | ✅ |
| 65 | PartyPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | ✅ |
| 66 | PartyPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | ✅ |
| 67 | PartyPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | ✅ |
| 68 | PartyPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | ✅ |
| 69 | PartyPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | ✅ |
| 70 | PartyPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | ✅ |
| 71 | PartyProvince | PROVINCE | — | ✅ |
| 72 | PartySalutation | SALUTATION | — | ✅ |
| 73 | PartySicCode | SIC_CODE | — | ✅ |
| 74 | PartySicCodeType | SIC_CODE_TYPE | — | ✅ |
| 75 | PartyState | STATE | — | ✅ |
| 76 | PartyStatus | STATUS | — | ✅ |
| 77 | PartyThirdPartyFlag | THIRD_PARTY_FLAG | — | ✅ |
| 78 | PartyTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | ✅ |
| 79 | PartyUrl | URL | — | ✅ |
| 80 | PartyUserGuid | USER_GUID | — | ✅ |
| 81 | PartyValidatedFlag | VALIDATED_FLAG | — | ✅ |
| 82 | PartyYearEstablished | YEAR_ESTABLISHED | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
