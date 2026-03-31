---
id: DOC-PO-PVO-SupplierContactUserAcctDetailsPVO
doc_type: system-doc
title: "SupplierContactUserAcctDetailsPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - SupplierContactUserAcctDetailsPVO
  - suppliercontactuseracctdetailspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierContactUserAcctDetailsPVO

## 📌 Visão Geral

Extrai detalhes de conta de usuário dos contatos de fornecedores, incluindo roles, acessos e status da conta. Permite auditoria de segurança e gestão de credenciais do portal.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierContactUserAcctDetailsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 145 | 4 | 3 | 20 | 14% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 82 atributos (2 BICC)
- [[per_roles_dn_vl|PER_ROLES_DN_VL]] — 17 atributos (3 BICC)
- [[per_users|PER_USERS]] — 20 atributos (2 PKs, 9 BICC)
- [[poz_supp_role_assignments_v|POZ_SUPP_ROLE_ASSIGNMENTS_V]] — 26 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyAddress1 | ADDRESS1 | — | — |
| 2 | PartyAddress2 | ADDRESS2 | — | — |
| 3 | PartyAddress3 | ADDRESS3 | — | — |
| 4 | PartyAddress4 | ADDRESS4 | — | — |
| 5 | PartyAnalysisFy | ANALYSIS_FY | — | — |
| 6 | PartyCategoryCode | CATEGORY_CODE | — | — |
| 7 | PartyCeoName | CEO_NAME | — | — |
| 8 | PartyCertReasonCode | CERT_REASON_CODE | — | — |
| 9 | PartyCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 10 | PartyCity | CITY | — | — |
| 11 | PartyComments | COMMENTS | — | — |
| 12 | PartyCountry | COUNTRY | — | — |
| 13 | PartyCounty | COUNTY | — | — |
| 14 | PartyCreatedBy | CREATED_BY | — | — |
| 15 | PartyCreatedByModule | CREATED_BY_MODULE | — | — |
| 16 | PartyCreationDate | CREATION_DATE | — | — |
| 17 | PartyCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 18 | PartyDateOfBirth | DATE_OF_BIRTH | — | — |
| 19 | PartyDunsNumberC | DUNS_NUMBER_C | — | — |
| 20 | PartyEmailAddress | EMAIL_ADDRESS | — | — |
| 21 | PartyEmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 22 | PartyFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 23 | PartyGender | GENDER | — | — |
| 24 | PartyGroupType | GROUP_TYPE | — | — |
| 25 | PartyGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 26 | PartyHomeCountry | HOME_COUNTRY | — | — |
| 27 | PartyHqBranchInd | HQ_BRANCH_IND | — | — |
| 28 | PartyIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 29 | PartyIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 30 | PartyInternalFlag | INTERNAL_FLAG | — | — |
| 31 | PartyJgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 32 | PartyLanguageName | LANGUAGE_NAME | — | — |
| 33 | PartyLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | PartyLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 35 | PartyLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 36 | PartyMaritalStatus | MARITAL_STATUS | — | — |
| 37 | PartyMissionStatement | MISSION_STATEMENT | — | — |
| 38 | PartyNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 39 | PartyNumber | PARTY_NUMBER | — | — |
| 40 | PartyObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 41 | PartyOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 42 | PartyPartyId | PARTY_ID | — | — |
| 43 | PartyPartyName | PARTY_NAME | — | ✅ |
| 44 | PartyPartyType | PARTY_TYPE | — | — |
| 45 | PartyPartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 46 | PartyPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 47 | PartyPersonFirstName | PERSON_FIRST_NAME | — | — |
| 48 | PartyPersonLastName | PERSON_LAST_NAME | — | — |
| 49 | PartyPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 50 | PartyPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 51 | PartyPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 52 | PartyPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 53 | PartyPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 54 | PartyPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 55 | PartyPersonTitle | PERSON_TITLE | — | — |
| 56 | PartyPostalCode | POSTAL_CODE | — | — |
| 57 | PartyPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 58 | PartyPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 59 | PartyPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 60 | PartyPreferredName | PREFERRED_NAME | — | — |
| 61 | PartyPreferredNameId | PREFERRED_NAME_ID | — | — |
| 62 | PartyPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 63 | PartyPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 64 | PartyPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 65 | PartyPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 66 | PartyPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 67 | PartyPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 68 | PartyPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | — |
| 69 | PartyPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 70 | PartyPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 71 | PartyProvince | PROVINCE | — | — |
| 72 | PartySalutation | SALUTATION | — | — |
| 73 | PartySicCode | SIC_CODE | — | — |
| 74 | PartySicCodeType | SIC_CODE_TYPE | — | — |
| 75 | PartyState | STATE | — | — |
| 76 | PartyStatus | STATUS | — | — |
| 77 | PartyThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 78 | PartyTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 79 | PartyUrl | URL | — | — |
| 80 | PartyUserGuid | USER_GUID | — | — |
| 81 | PartyValidatedFlag | VALIDATED_FLAG | — | — |
| 82 | PartyYearEstablished | YEAR_ESTABLISHED | — | — |

### [[per_roles_dn_vl|PER_ROLES_DN_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RoleNameAbstractRole | ABSTRACT_ROLE | — | — |
| 2 | RoleNameActiveFlag | ACTIVE_FLAG | — | — |
| 3 | RoleNameCreatedBy | CREATED_BY | — | — |
| 4 | RoleNameCreationDate | CREATION_DATE | — | — |
| 5 | RoleNameDataRole | DATA_ROLE | — | — |
| 6 | RoleNameDescription | DESCRIPTION | — | ✅ |
| 7 | RoleNameJobRole | JOB_ROLE | — | — |
| 8 | RoleNameLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | RoleNameLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | RoleNameLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | RoleNameMultitenancyCommonName | MULTITENANCY_COMMON_NAME | — | — |
| 12 | RoleNameObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | RoleNameRoleCommonName | ROLE_COMMON_NAME | — | — |
| 14 | RoleNameRoleDistinguishedName | ROLE_DISTINGUISHED_NAME | — | — |
| 15 | RoleNameRoleGuid | ROLE_GUID | — | — |
| 16 | RoleNameRoleId | ROLE_ID | — | — |
| 17 | RoleNameRoleName | ROLE_NAME | — | ✅ |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyId | PARTY_ID | 🔑 | ✅ |
| 2 | UserId | USER_ID | 🔑 | ✅ |
| 3 | UsersActiveFlag | ACTIVE_FLAG | — | ✅ |
| 4 | UsersBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 5 | UsersCreatedBy | CREATED_BY | — | ✅ |
| 6 | UsersCreationDate | CREATION_DATE | — | ✅ |
| 7 | UsersEndDate | END_DATE | — | — |
| 8 | UsersHrTerminated | HR_TERMINATED | — | — |
| 9 | UsersLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | UsersLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | UsersLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | UsersMultitenancyUsername | MULTITENANCY_USERNAME | — | — |
| 13 | UsersObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | UsersPersonId | PERSON_ID | — | — |
| 15 | UsersStartDate | START_DATE | — | — |
| 16 | UsersSuspended | SUSPENDED | — | ✅ |
| 17 | UsersUserDataChecksum | USER_DATA_CHECKSUM | — | — |
| 18 | UsersUserDistinguishedName | USER_DISTINGUISHED_NAME | — | — |
| 19 | UsersUserGuid | USER_GUID | — | — |
| 20 | UsersUsername | USERNAME | — | ✅ |

### [[poz_supp_role_assignments_v|POZ_SUPP_ROLE_ASSIGNMENTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RoleGuid | PROVISIONAL_ROLE_GUID | 🔑 | ✅ |
| 2 | SupplierContactUserAccountAllowSupplierProvisionFlag | ALLOW_SUPP_PROV_FLAG | — | — |
| 3 | SupplierContactUserAccountCreatedBy | CREATED_BY | — | ✅ |
| 4 | SupplierContactUserAccountCreationDate | CREATION_DATE | — | ✅ |
| 5 | SupplierContactUserAccountDefaultForPonFlag | DEFAULT_FOR_PON_FLAG | — | — |
| 6 | SupplierContactUserAccountDefaultForPosFlag | DEFAULT_FOR_POS_FLAG | — | — |
| 7 | SupplierContactUserAccountLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | SupplierContactUserAccountLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | SupplierContactUserAccountLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | SupplierContactUserAccountObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | UserRolesActiveFlag | ACTIVE_FLAG | — | — |
| 12 | UserRolesBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 13 | UserRolesCreatedBy | CREATED_BY | — | — |
| 14 | UserRolesCreationDate | CREATION_DATE | — | — |
| 15 | UserRolesEndDate | END_DATE | — | — |
| 16 | UserRolesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | UserRolesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | UserRolesLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | UserRolesMethodCode | METHOD_CODE | — | — |
| 20 | UserRolesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | UserRolesRoleGuid | ROLE_GUID | — | — |
| 22 | UserRolesRoleId | ROLE_ID | — | — |
| 23 | UserRolesStartDate | START_DATE | — | — |
| 24 | UserRolesTerminatedFlag | TERMINATED_FLAG | — | — |
| 25 | UserRolesUserId | USER_ID | — | — |
| 26 | UserRolesUserRoleId | USER_ROLE_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
