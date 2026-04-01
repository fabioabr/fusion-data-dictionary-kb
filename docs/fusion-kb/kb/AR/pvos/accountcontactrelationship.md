---
id: DOC-AR-PVO-AccountContactRelationShip
doc_type: system-doc
title: "AccountContactRelationShip — PVO Accounts Receivable"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ar
  - data-dictionary
  - pvo
  - bicc
aliases:
  - AccountContactRelationShip
  - accountcontactrelationship
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AccountContactRelationShip

## 📌 Visão Geral

Extrai os relacionamentos entre contatos e contas de clientes, incluindo hierarquias organizacionais e papéis. Permite mapear a estrutura de responsáveis por pagamentos e aprovações em cada conta.

**Caminho:** `FscmTopModelAM.FinArCustomersPublicModelAM.AccountContactRelationShip`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 171 | 6 | 1 | 30 | 18% |

---

## 🔗 Tabelas Relacionadas

- [[hz_cust_account_roles|HZ_CUST_ACCOUNT_ROLES]] — 16 atributos (1 PKs, 11 BICC)
- [[hz_org_contacts|HZ_ORG_CONTACTS]] — 25 atributos (5 BICC)
- [[hz_parties|HZ_PARTIES]] — 77 atributos (12 BICC)
- [[hz_relationships|HZ_RELATIONSHIPS]] — 29 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (1 BICC)
- [[per_users|PER_USERS]] — 14 atributos

---

## ⚙️ Atributos

### [[hz_cust_account_roles|HZ_CUST_ACCOUNT_ROLES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CustAccountRoleId | CUST_ACCOUNT_ROLE_ID | 🔑 | ✅ |
| 2 | CustomerAccountContactContactPersonId | CONTACT_PERSON_ID | — | — |
| 3 | CustomerAccountContactCreatedBy | CREATED_BY | — | ✅ |
| 4 | CustomerAccountContactCreatedByModule | CREATED_BY_MODULE | — | ✅ |
| 5 | CustomerAccountContactCreationDate | CREATION_DATE | — | ✅ |
| 6 | CustomerAccountContactCustAccountId | CUST_ACCOUNT_ID | — | — |
| 7 | CustomerAccountContactCustAcctSiteId | CUST_ACCT_SITE_ID | — | — |
| 8 | CustomerAccountContactLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | CustomerAccountContactLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | CustomerAccountContactLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | CustomerAccountContactOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | ✅ |
| 12 | CustomerAccountContactPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 13 | CustomerAccountContactRelationshipId | RELATIONSHIP_ID | — | — |
| 14 | CustomerAccountContactRoleType | ROLE_TYPE | — | ✅ |
| 15 | CustomerAccountContactSourceCode | SOURCE_CODE | — | — |
| 16 | CustomerAccountContactStatus | STATUS | — | ✅ |

### [[hz_org_contacts|HZ_ORG_CONTACTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationContactComments | COMMENTS | — | — |
| 2 | OrganizationContactContactNumber | CONTACT_NUMBER | — | ✅ |
| 3 | OrganizationContactCreatedBy | CREATED_BY | — | — |
| 4 | OrganizationContactCreatedByModule | CREATED_BY_MODULE | — | — |
| 5 | OrganizationContactCreationDate | CREATION_DATE | — | — |
| 6 | OrganizationContactCurrencyCode | CURRENCY_CODE | — | — |
| 7 | OrganizationContactDecisionMakerFlag | DECISION_MAKER_FLAG | — | — |
| 8 | OrganizationContactDepartment | DEPARTMENT | — | — |
| 9 | OrganizationContactDepartmentCode | DEPARTMENT_CODE | — | ✅ |
| 10 | OrganizationContactJobTitle | JOB_TITLE | — | ✅ |
| 11 | OrganizationContactJobTitleCode | JOB_TITLE_CODE | — | ✅ |
| 12 | OrganizationContactLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | OrganizationContactLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | OrganizationContactLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | OrganizationContactObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | OrganizationContactOrgContactId | ORG_CONTACT_ID | — | — |
| 17 | OrganizationContactOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 18 | OrganizationContactPartyRelationshipId | PARTY_RELATIONSHIP_ID | — | — |
| 19 | OrganizationContactPartySiteId | PARTY_SITE_ID | — | — |
| 20 | OrganizationContactRank | RANK | — | — |
| 21 | OrganizationContactReferenceUseFlag | REFERENCE_USE_FLAG | — | — |
| 22 | OrganizationContactSalesAffinityCode | SALES_AFFINITY_CODE | — | — |
| 23 | OrganizationContactSalesAffinityComments | SALES_AFFINITY_COMMENTS | — | — |
| 24 | OrganizationContactSalesBuyingRoleCode | SALES_BUYING_ROLE_CODE | — | — |
| 25 | OrganizationContactSalesInfluenceLevelCode | SALES_INFLUENCE_LEVEL_CODE | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContactPersonPartyCategoryCode | CATEGORY_CODE | — | — |
| 2 | ContactPersonPartyCeoName | CEO_NAME | — | — |
| 3 | ContactPersonPartyCertReasonCode | CERT_REASON_CODE | — | — |
| 4 | ContactPersonPartyCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 5 | ContactPersonPartyCity | CITY | — | — |
| 6 | ContactPersonPartyComments | COMMENTS | — | — |
| 7 | ContactPersonPartyCountry | COUNTRY | — | — |
| 8 | ContactPersonPartyCounty | COUNTY | — | — |
| 9 | ContactPersonPartyCreatedBy | CREATED_BY | — | — |
| 10 | ContactPersonPartyCreatedByModule | CREATED_BY_MODULE | — | — |
| 11 | ContactPersonPartyCreationDate | CREATION_DATE | — | — |
| 12 | ContactPersonPartyCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 13 | ContactPersonPartyDateOfBirth | DATE_OF_BIRTH | — | — |
| 14 | ContactPersonPartyDunsNumberC | DUNS_NUMBER_C | — | — |
| 15 | ContactPersonPartyEmailAddress | EMAIL_ADDRESS | — | — |
| 16 | ContactPersonPartyEmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 17 | ContactPersonPartyFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 18 | ContactPersonPartyGender | GENDER | — | — |
| 19 | ContactPersonPartyGroupType | GROUP_TYPE | — | — |
| 20 | ContactPersonPartyGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 21 | ContactPersonPartyHomeCountry | HOME_COUNTRY | — | — |
| 22 | ContactPersonPartyHqBranchInd | HQ_BRANCH_IND | — | — |
| 23 | ContactPersonPartyIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 24 | ContactPersonPartyIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 25 | ContactPersonPartyInternalFlag | INTERNAL_FLAG | — | — |
| 26 | ContactPersonPartyJgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 27 | ContactPersonPartyLanguageName | LANGUAGE_NAME | — | — |
| 28 | ContactPersonPartyLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 29 | ContactPersonPartyLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 30 | ContactPersonPartyLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 31 | ContactPersonPartyMaritalStatus | MARITAL_STATUS | — | — |
| 32 | ContactPersonPartyMissionStatement | MISSION_STATEMENT | — | — |
| 33 | ContactPersonPartyNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 34 | ContactPersonPartyObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 35 | ContactPersonPartyOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 36 | ContactPersonPartyPartyId | PARTY_ID | — | — |
| 37 | ContactPersonPartyPartyName | PARTY_NAME | — | — |
| 38 | ContactPersonPartyPartyNumber | PARTY_NUMBER | — | — |
| 39 | ContactPersonPartyPartyType | PARTY_TYPE | — | — |
| 40 | ContactPersonPartyPartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 41 | ContactPersonPartyPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 42 | ContactPersonPartyPersonFirstName | PERSON_FIRST_NAME | — | ✅ |
| 43 | ContactPersonPartyPersonLastName | PERSON_LAST_NAME | — | ✅ |
| 44 | ContactPersonPartyPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | ✅ |
| 45 | ContactPersonPartyPersonMiddleName | PERSON_MIDDLE_NAME | — | ✅ |
| 46 | ContactPersonPartyPersonNameSuffix | PERSON_NAME_SUFFIX | — | ✅ |
| 47 | ContactPersonPartyPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | ✅ |
| 48 | ContactPersonPartyPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | ✅ |
| 49 | ContactPersonPartyPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 50 | ContactPersonPartyPersonTitle | PERSON_TITLE | — | — |
| 51 | ContactPersonPartyPostalCode | POSTAL_CODE | — | — |
| 52 | ContactPersonPartyPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 53 | ContactPersonPartyPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 54 | ContactPersonPartyPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 55 | ContactPersonPartyPreferredName | PREFERRED_NAME | — | — |
| 56 | ContactPersonPartyPreferredNameId | PREFERRED_NAME_ID | — | — |
| 57 | ContactPersonPartyPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 58 | ContactPersonPartyPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | ✅ |
| 59 | ContactPersonPartyPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 60 | ContactPersonPartyPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | ✅ |
| 61 | ContactPersonPartyPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | ✅ |
| 62 | ContactPersonPartyPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 63 | ContactPersonPartyPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | ✅ |
| 64 | ContactPersonPartyPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 65 | ContactPersonPartyPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 66 | ContactPersonPartyProvince | PROVINCE | — | — |
| 67 | ContactPersonPartySalutation | SALUTATION | — | — |
| 68 | ContactPersonPartySicCode | SIC_CODE | — | — |
| 69 | ContactPersonPartySicCodeType | SIC_CODE_TYPE | — | — |
| 70 | ContactPersonPartyState | STATE | — | — |
| 71 | ContactPersonPartyStatus | STATUS | — | — |
| 72 | ContactPersonPartyThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 73 | ContactPersonPartyTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 74 | ContactPersonPartyUrl | URL | — | — |
| 75 | ContactPersonPartyUserGuid | USER_GUID | — | — |
| 76 | ContactPersonPartyValidatedFlag | VALIDATED_FLAG | — | — |
| 77 | ContactPersonPartyYearEstablished | YEAR_ESTABLISHED | — | — |

### [[hz_relationships|HZ_RELATIONSHIPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelationshipActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | RelationshipComments | COMMENTS | — | — |
| 3 | RelationshipCreatedBy | CREATED_BY | — | — |
| 4 | RelationshipCreatedByModule | CREATED_BY_MODULE | — | — |
| 5 | RelationshipCreationDate | CREATION_DATE | — | — |
| 6 | RelationshipDependentFlag | DEPENDENT_FLAG | — | — |
| 7 | RelationshipDirectionCode | DIRECTION_CODE | — | — |
| 8 | RelationshipDirectionalFlag | DIRECTIONAL_FLAG | — | — |
| 9 | RelationshipEndDate | END_DATE | — | — |
| 10 | RelationshipHeadOfHouseholdFlag | HEAD_OF_HOUSEHOLD_FLAG | — | — |
| 11 | RelationshipLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | RelationshipLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | RelationshipLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | RelationshipObjectId | OBJECT_ID | — | — |
| 15 | RelationshipObjectTableName | OBJECT_TABLE_NAME | — | — |
| 16 | RelationshipObjectType | OBJECT_TYPE | — | — |
| 17 | RelationshipObjectUsageCode | OBJECT_USAGE_CODE | — | — |
| 18 | RelationshipObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | RelationshipPercentageOwnership | PERCENTAGE_OWNERSHIP | — | — |
| 20 | RelationshipRelationshipCode | RELATIONSHIP_CODE | — | — |
| 21 | RelationshipRelationshipId | RELATIONSHIP_ID | — | — |
| 22 | RelationshipRelationshipRecId | RELATIONSHIP_REC_ID | — | — |
| 23 | RelationshipRelationshipType | RELATIONSHIP_TYPE | — | — |
| 24 | RelationshipStartDate | START_DATE | — | — |
| 25 | RelationshipStatus | STATUS | — | — |
| 26 | RelationshipSubjectId | SUBJECT_ID | — | — |
| 27 | RelationshipSubjectTableName | SUBJECT_TABLE_NAME | — | — |
| 28 | RelationshipSubjectType | SUBJECT_TYPE | — | — |
| 29 | RelationshipSubjectUsageCode | SUBJECT_USAGE_CODE | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | — |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonCreatedByPersonId1 | PERSON_ID | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonLastUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | PersonLastUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonLastUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | PersonLastUpdatedByPersonId1 | PERSON_ID | — | — |
| 10 | PersonLastUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserCreatedByCreatedBy | CREATED_BY | — | — |
| 2 | UserCreatedByCreationDate | CREATION_DATE | — | — |
| 3 | UserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | UserCreatedByPersonId | PERSON_ID | — | — |
| 5 | UserCreatedByUserGuid | USER_GUID | — | — |
| 6 | UserCreatedByUserId | USER_ID | — | — |
| 7 | UserCreatedByUsername | USERNAME | — | — |
| 8 | UserLastUpdatedByLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 9 | UserLastUpdatedByLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | UserLastUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | UserLastUpdatedByPersonId | PERSON_ID | — | — |
| 12 | UserLastUpdatedByUserGuid | USER_GUID | — | — |
| 13 | UserLastUpdatedByUserId | USER_ID | — | — |
| 14 | UserLastUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
