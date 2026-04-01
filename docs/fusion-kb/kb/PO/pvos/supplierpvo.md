---
id: DOC-PO-PVO-SupplierPVO
doc_type: system-doc
title: "SupplierPVO — PVO Purchasing"
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
  - SupplierPVO
  - supplierpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierPVO

## 📌 Visão Geral

Extrai o cadastro completo de fornecedores, incluindo razão social, CNPJ/Tax ID, classificações fiscais, perfil tributário, dados organizacionais e indicadores de spend. Base fundamental para gestão de fornecedores, análise de risco e compliance regulatória.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 475 | 12 | 1 | 199 | 42% |

---

## 🔗 Tabelas Relacionadas

- [[ap_income_tax_types|AP_INCOME_TAX_TYPES]] — 2 atributos (1 BICC)
- [[hz_addtnl_party_names|HZ_ADDTNL_PARTY_NAMES]] — 8 atributos (2 BICC)
- [[hz_organization_profiles|HZ_ORGANIZATION_PROFILES]] — 7 atributos (5 BICC)
- [[hz_parties|HZ_PARTIES]] — 156 atributos (10 BICC)
- [[poz_bi_hierarchy_ap_inv_dist_v|POZ_BI_HIERARCHY_AP_INV_DIST_V]] — 2 atributos (2 BICC)
- [[poz_bi_supp_ap_inv_dist_v|POZ_BI_SUPP_AP_INV_DIST_V]] — 2 atributos (1 BICC)
- [[poz_bus_classifications|POZ_BUS_CLASSIFICATIONS]] — 108 atributos (26 BICC)
- [[poz_spend_auth_requests|POZ_SPEND_AUTH_REQUESTS]] — 2 atributos (1 BICC)
- [[poz_suppliers|POZ_SUPPLIERS]] — 167 atributos (1 PKs, 145 BICC)
- [[poz_suppliers_pii|POZ_SUPPLIERS_PII]] — 5 atributos (1 BICC)
- [[zx_party_tax_profile|ZX_PARTY_TAX_PROFILE]] — 6 atributos (3 BICC)
- [[zx_wht_tax_classification_v|ZX_WHT_TAX_CLASSIFICATION_V]] — 10 atributos (2 BICC)

---

## ⚙️ Atributos

### [[ap_income_tax_types|AP_INCOME_TAX_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IncomeTaxTypeDescription | DESCRIPTION | — | ✅ |
| 2 | IncomeTaxTypeIncomeTaxType1 | INCOME_TAX_TYPE | — | — |

### [[hz_addtnl_party_names|HZ_ADDTNL_PARTY_NAMES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AliasPartyId | PARTY_ID | — | — |
| 2 | AliasPartyName | PARTY_NAME | — | ✅ |
| 3 | AliasPartyNameId | PARTY_NAME_ID | — | — |
| 4 | AliasPartyNameType | PARTY_NAME_TYPE | — | — |
| 5 | AlternateNamePartyId | PARTY_ID | — | — |
| 6 | AlternateNamePartyName | PARTY_NAME | — | ✅ |
| 7 | AlternateNamePartyNameId | PARTY_NAME_ID | — | — |
| 8 | AlternateNamePartyNameType | PARTY_NAME_TYPE | — | — |

### [[hz_organization_profiles|HZ_ORGANIZATION_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | ✅ |
| 2 | OrganizationCeoName | CEO_NAME | — | ✅ |
| 3 | OrganizationCeoTitle | CEO_TITLE | — | ✅ |
| 4 | OrganizationEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 5 | OrganizationEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 6 | OrganizationOrganizationProfileId | ORGANIZATION_PROFILE_ID | — | — |
| 7 | YearEstablished | YEAR_ESTABLISHED | — | ✅ |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ParentAddress1 | ADDRESS1 | — | — |
| 2 | ParentAddress2 | ADDRESS2 | — | — |
| 3 | ParentAddress3 | ADDRESS3 | — | — |
| 4 | ParentAddress4 | ADDRESS4 | — | — |
| 5 | ParentAnalysisFy | ANALYSIS_FY | — | — |
| 6 | ParentCategoryCode | CATEGORY_CODE | — | — |
| 7 | ParentCeoName | CEO_NAME | — | — |
| 8 | ParentCertReasonCode | CERT_REASON_CODE | — | — |
| 9 | ParentCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 10 | ParentCity | CITY | — | — |
| 11 | ParentComments | COMMENTS | — | — |
| 12 | ParentCountry | COUNTRY | — | — |
| 13 | ParentCounty | COUNTY | — | — |
| 14 | ParentCreatedBy | CREATED_BY | — | — |
| 15 | ParentCreatedByModule | CREATED_BY_MODULE | — | — |
| 16 | ParentCreationDate | CREATION_DATE | — | — |
| 17 | ParentCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 18 | ParentDateOfBirth | DATE_OF_BIRTH | — | — |
| 19 | ParentDunsNumberC | DUNS_NUMBER_C | — | — |
| 20 | ParentEmailAddress | EMAIL_ADDRESS | — | — |
| 21 | ParentEmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 22 | ParentFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 23 | ParentGender | GENDER | — | — |
| 24 | ParentGroupType | GROUP_TYPE | — | — |
| 25 | ParentGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 26 | ParentHomeCountry | HOME_COUNTRY | — | — |
| 27 | ParentHqBranchInd | HQ_BRANCH_IND | — | — |
| 28 | ParentIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 29 | ParentIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 30 | ParentInternalFlag | INTERNAL_FLAG | — | — |
| 31 | ParentJgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 32 | ParentLanguageName | LANGUAGE_NAME | — | — |
| 33 | ParentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 34 | ParentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 35 | ParentLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 36 | ParentMaritalStatus | MARITAL_STATUS | — | — |
| 37 | ParentMissionStatement | MISSION_STATEMENT | — | — |
| 38 | ParentNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 39 | ParentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 40 | ParentOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 41 | ParentPartyId | PARTY_ID | — | — |
| 42 | ParentPartyName | PARTY_NAME | — | ✅ |
| 43 | ParentPartyNumber | PARTY_NUMBER | — | ✅ |
| 44 | ParentPartyType | PARTY_TYPE | — | — |
| 45 | ParentPartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 46 | ParentPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 47 | ParentPersonFirstName | PERSON_FIRST_NAME | — | — |
| 48 | ParentPersonLastName | PERSON_LAST_NAME | — | — |
| 49 | ParentPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 50 | ParentPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 51 | ParentPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 52 | ParentPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 53 | ParentPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 54 | ParentPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 55 | ParentPersonTitle | PERSON_TITLE | — | — |
| 56 | ParentPostalCode | POSTAL_CODE | — | — |
| 57 | ParentPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 58 | ParentPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 59 | ParentPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 60 | ParentPreferredName | PREFERRED_NAME | — | — |
| 61 | ParentPreferredNameId | PREFERRED_NAME_ID | — | — |
| 62 | ParentPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 63 | ParentPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 64 | ParentPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 65 | ParentPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 66 | ParentPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 67 | ParentPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 68 | ParentPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | ✅ |
| 69 | ParentPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 70 | ParentPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 71 | ParentProvince | PROVINCE | — | — |
| 72 | ParentSalutation | SALUTATION | — | — |
| 73 | ParentSicCode | SIC_CODE | — | — |
| 74 | ParentSicCodeType | SIC_CODE_TYPE | — | — |
| 75 | ParentState | STATE | — | — |
| 76 | ParentStatus | STATUS | — | — |
| 77 | ParentThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 78 | ParentTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 79 | ParentUrl | URL | — | ✅ |
| 80 | ParentUserGuid | USER_GUID | — | — |
| 81 | ParentValidatedFlag | VALIDATED_FLAG | — | — |
| 82 | ParentYearEstablished | YEAR_ESTABLISHED | — | — |
| 83 | PartyAddress1 | ADDRESS1 | — | — |
| 84 | PartyAddress2 | ADDRESS2 | — | — |
| 85 | PartyAddress3 | ADDRESS3 | — | — |
| 86 | PartyAddress4 | ADDRESS4 | — | — |
| 87 | PartyAnalysisFy | ANALYSIS_FY | — | — |
| 88 | PartyCategoryCode | CATEGORY_CODE | — | — |
| 89 | PartyCeoName | CEO_NAME | — | — |
| 90 | PartyCertReasonCode | CERT_REASON_CODE | — | — |
| 91 | PartyCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 92 | PartyCity | CITY | — | — |
| 93 | PartyComments | COMMENTS | — | — |
| 94 | PartyCountry | COUNTRY | — | — |
| 95 | PartyCounty | COUNTY | — | — |
| 96 | PartyCreatedByModule | CREATED_BY_MODULE | — | — |
| 97 | PartyCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 98 | PartyDateOfBirth | DATE_OF_BIRTH | — | — |
| 99 | PartyDunsNumberC | DUNS_NUMBER_C | — | ✅ |
| 100 | PartyEmailAddress | EMAIL_ADDRESS | — | — |
| 101 | PartyEmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 102 | PartyFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 103 | PartyGender | GENDER | — | — |
| 104 | PartyGroupType | GROUP_TYPE | — | — |
| 105 | PartyGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 106 | PartyHomeCountry | HOME_COUNTRY | — | — |
| 107 | PartyHqBranchInd | HQ_BRANCH_IND | — | — |
| 108 | PartyIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 109 | PartyIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 110 | PartyInternalFlag | INTERNAL_FLAG | — | — |
| 111 | PartyLanguageName | LANGUAGE_NAME | — | — |
| 112 | PartyMaritalStatus | MARITAL_STATUS | — | — |
| 113 | PartyMissionStatement | MISSION_STATEMENT | — | — |
| 114 | PartyNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 115 | PartyOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 116 | PartyPartyId | PARTY_ID | — | — |
| 117 | PartyPartyName | PARTY_NAME | — | ✅ |
| 118 | PartyPartyNumber | PARTY_NUMBER | — | ✅ |
| 119 | PartyPartyType | PARTY_TYPE | — | — |
| 120 | PartyPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 121 | PartyPersonFirstName | PERSON_FIRST_NAME | — | — |
| 122 | PartyPersonLastName | PERSON_LAST_NAME | — | — |
| 123 | PartyPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 124 | PartyPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 125 | PartyPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 126 | PartyPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 127 | PartyPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 128 | PartyPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 129 | PartyPersonTitle | PERSON_TITLE | — | — |
| 130 | PartyPostalCode | POSTAL_CODE | — | — |
| 131 | PartyPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 132 | PartyPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 133 | PartyPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 134 | PartyPreferredName | PREFERRED_NAME | — | — |
| 135 | PartyPreferredNameId | PREFERRED_NAME_ID | — | — |
| 136 | PartyPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 137 | PartyPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 138 | PartyPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 139 | PartyPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 140 | PartyPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 141 | PartyPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 142 | PartyPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | ✅ |
| 143 | PartyPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 144 | PartyPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 145 | PartyProvince | PROVINCE | — | — |
| 146 | PartySalutation | SALUTATION | — | — |
| 147 | PartySicCode | SIC_CODE | — | — |
| 148 | PartySicCodeType | SIC_CODE_TYPE | — | — |
| 149 | PartyState | STATE | — | — |
| 150 | PartyStatus | STATUS | — | — |
| 151 | PartyThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 152 | PartyTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | ✅ |
| 153 | PartyUrl | URL | — | — |
| 154 | PartyUserGuid | USER_GUID | — | — |
| 155 | PartyValidatedFlag | VALIDATED_FLAG | — | — |
| 156 | PartyYearEstablished | YEAR_ESTABLISHED | — | — |

### [[poz_bi_hierarchy_ap_inv_dist_v|POZ_BI_HIERARCHY_AP_INV_DIST_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupplierHierarchyInvDistHierarchyAmount | HIERARCHY_AMOUNT | — | ✅ |
| 2 | SupplierHierarchyInvDistVendorId | VENDOR_ID | — | ✅ |

### [[poz_bi_supp_ap_inv_dist_v|POZ_BI_SUPP_AP_INV_DIST_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SuppInvDistAmount | AMOUNT | — | ✅ |
| 2 | SuppInvDistVendorId | VENDOR_ID | — | — |

### [[poz_bus_classifications|POZ_BUS_CLASSIFICATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusClass1CertificateNumber | CERTIFICATE_NUMBER | — | — |
| 2 | BusClass1CertifyingAgency | CERTIFYING_AGENCY | — | — |
| 3 | BusClass1ClassStatus | CLASS_STATUS | — | — |
| 4 | BusClass1ClassificationId | CLASSIFICATION_ID | — | ✅ |
| 5 | BusClass1CreatedBy | CREATED_BY | — | — |
| 6 | BusClass1CreationDate | CREATION_DATE | — | — |
| 7 | BusClass1EndDateActive | END_DATE_ACTIVE | — | — |
| 8 | BusClass1ExpirationDate | EXPIRATION_DATE | — | — |
| 9 | BusClass1ExtAttr1 | EXT_ATTR_1 | — | ✅ |
| 10 | BusClass1LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | BusClass1LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | BusClass1LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | BusClass1LookupCode | LOOKUP_CODE | — | ✅ |
| 14 | BusClass1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | BusClass1PartyId | PARTY_ID | — | — |
| 16 | BusClass1StartDateActive | START_DATE_ACTIVE | — | — |
| 17 | BusClass1Status | STATUS | — | ✅ |
| 18 | BusClass1VendorId | VENDOR_ID | — | — |
| 19 | BusClass2CertificateNumber | CERTIFICATE_NUMBER | — | — |
| 20 | BusClass2CertifyingAgency | CERTIFYING_AGENCY | — | — |
| 21 | BusClass2ClassStatus | CLASS_STATUS | — | — |
| 22 | BusClass2ClassificationId | CLASSIFICATION_ID | — | ✅ |
| 23 | BusClass2CreatedBy | CREATED_BY | — | — |
| 24 | BusClass2CreationDate | CREATION_DATE | — | — |
| 25 | BusClass2EndDateActive | END_DATE_ACTIVE | — | — |
| 26 | BusClass2ExpirationDate | EXPIRATION_DATE | — | — |
| 27 | BusClass2ExtAttr1 | EXT_ATTR_1 | — | ✅ |
| 28 | BusClass2LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 29 | BusClass2LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 30 | BusClass2LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 31 | BusClass2LookupCode | LOOKUP_CODE | — | ✅ |
| 32 | BusClass2ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 33 | BusClass2PartyId | PARTY_ID | — | — |
| 34 | BusClass2StartDateActive | START_DATE_ACTIVE | — | — |
| 35 | BusClass2Status | STATUS | — | ✅ |
| 36 | BusClass2VendorId | VENDOR_ID | — | — |
| 37 | BusClass3CertificateNumber | CERTIFICATE_NUMBER | — | — |
| 38 | BusClass3CertifyingAgency | CERTIFYING_AGENCY | — | — |
| 39 | BusClass3ClassStatus | CLASS_STATUS | — | — |
| 40 | BusClass3ClassificationId | CLASSIFICATION_ID | — | ✅ |
| 41 | BusClass3CreatedBy | CREATED_BY | — | — |
| 42 | BusClass3CreationDate | CREATION_DATE | — | — |
| 43 | BusClass3EndDateActive | END_DATE_ACTIVE | — | — |
| 44 | BusClass3ExpirationDate | EXPIRATION_DATE | — | — |
| 45 | BusClass3ExtAttr1 | EXT_ATTR_1 | — | — |
| 46 | BusClass3LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 47 | BusClass3LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 48 | BusClass3LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 49 | BusClass3LookupCode | LOOKUP_CODE | — | ✅ |
| 50 | BusClass3ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 51 | BusClass3PartyId | PARTY_ID | — | — |
| 52 | BusClass3StartDateActive | START_DATE_ACTIVE | — | — |
| 53 | BusClass3Status | STATUS | — | ✅ |
| 54 | BusClass3VendorId | VENDOR_ID | — | — |
| 55 | BusClass4CertificateNumber | CERTIFICATE_NUMBER | — | — |
| 56 | BusClass4CertifyingAgency | CERTIFYING_AGENCY | — | — |
| 57 | BusClass4ClassStatus | CLASS_STATUS | — | — |
| 58 | BusClass4ClassificationId | CLASSIFICATION_ID | — | ✅ |
| 59 | BusClass4CreatedBy | CREATED_BY | — | — |
| 60 | BusClass4CreationDate | CREATION_DATE | — | — |
| 61 | BusClass4EndDateActive | END_DATE_ACTIVE | — | — |
| 62 | BusClass4ExpirationDate | EXPIRATION_DATE | — | — |
| 63 | BusClass4ExtAttr1 | EXT_ATTR_1 | — | — |
| 64 | BusClass4LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 65 | BusClass4LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 66 | BusClass4LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 67 | BusClass4LookupCode | LOOKUP_CODE | — | ✅ |
| 68 | BusClass4ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 69 | BusClass4PartyId | PARTY_ID | — | — |
| 70 | BusClass4StartDateActive | START_DATE_ACTIVE | — | — |
| 71 | BusClass4Status | STATUS | — | ✅ |
| 72 | BusClass4VendorId | VENDOR_ID | — | — |
| 73 | BusClass5CertificateNumber | CERTIFICATE_NUMBER | — | — |
| 74 | BusClass5CertifyingAgency | CERTIFYING_AGENCY | — | — |
| 75 | BusClass5ClassStatus | CLASS_STATUS | — | — |
| 76 | BusClass5ClassificationId | CLASSIFICATION_ID | — | ✅ |
| 77 | BusClass5CreatedBy | CREATED_BY | — | — |
| 78 | BusClass5CreationDate | CREATION_DATE | — | — |
| 79 | BusClass5EndDateActive | END_DATE_ACTIVE | — | — |
| 80 | BusClass5ExpirationDate | EXPIRATION_DATE | — | — |
| 81 | BusClass5ExtAttr1 | EXT_ATTR_1 | — | — |
| 82 | BusClass5LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 83 | BusClass5LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 84 | BusClass5LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 85 | BusClass5LookupCode | LOOKUP_CODE | — | ✅ |
| 86 | BusClass5ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 87 | BusClass5PartyId | PARTY_ID | — | — |
| 88 | BusClass5StartDateActive | START_DATE_ACTIVE | — | — |
| 89 | BusClass5Status | STATUS | — | ✅ |
| 90 | BusClass5VendorId | VENDOR_ID | — | — |
| 91 | BusClass6CertificateNumber | CERTIFICATE_NUMBER | — | — |
| 92 | BusClass6CertifyingAgency | CERTIFYING_AGENCY | — | — |
| 93 | BusClass6ClassStatus | CLASS_STATUS | — | — |
| 94 | BusClass6ClassificationId | CLASSIFICATION_ID | — | ✅ |
| 95 | BusClass6CreatedBy | CREATED_BY | — | — |
| 96 | BusClass6CreationDate | CREATION_DATE | — | — |
| 97 | BusClass6EndDateActive | END_DATE_ACTIVE | — | — |
| 98 | BusClass6ExpirationDate | EXPIRATION_DATE | — | — |
| 99 | BusClass6ExtAttr1 | EXT_ATTR_1 | — | — |
| 100 | BusClass6LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 101 | BusClass6LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 102 | BusClass6LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 103 | BusClass6LookupCode | LOOKUP_CODE | — | ✅ |
| 104 | BusClass6ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 105 | BusClass6PartyId | PARTY_ID | — | — |
| 106 | BusClass6StartDateActive | START_DATE_ACTIVE | — | — |
| 107 | BusClass6Status | STATUS | — | ✅ |
| 108 | BusClass6VendorId | VENDOR_ID | — | — |

### [[poz_spend_auth_requests|POZ_SPEND_AUTH_REQUESTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SpendAuthReqAuthorizationRequestId | AUTHORIZATION_REQUEST_ID | — | — |
| 2 | SpendAuthReqSpendAuthJustification | SPEND_AUTH_JUSTIFICATION | — | ✅ |

### [[poz_suppliers|POZ_SUPPLIERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DatafoxCompanyId | DATAFOX_COMPANY_ID | — | ✅ |
| 2 | DeniedPartyFlag | DENIED_PARTY_FLAG | — | — |
| 3 | DfCompanyName | DF_COMPANY_NAME | — | ✅ |
| 4 | DfCorporateWebsite | DF_CORPORATE_WEBSITE | — | ✅ |
| 5 | DfIndustryCategoryCode | DF_INDUSTRY_CATEGORY_CODE | — | ✅ |
| 6 | DfIndustrySubCategoryCode | DF_INDUSTRY_SUB_CATEGORY_CODE | — | ✅ |
| 7 | DfLastSyncDate | DF_LAST_SYNC_DATE | — | ✅ |
| 8 | DfLegalName | DF_LEGAL_NAME | — | ✅ |
| 9 | DfNaicsCode | DF_NAICS_CODE | — | ✅ |
| 10 | DfScore | DF_SCORE | — | ✅ |
| 11 | DfTaxpayerCountry | DF_TAXPAYER_COUNTRY | — | ✅ |
| 12 | ObnMatchedStatus | OBN_MATCHED_STATUS | — | ✅ |
| 13 | SuppParentPartyId | PARTY_ID | — | — |
| 14 | SuppParentSegment1 | SEGMENT1 | — | ✅ |
| 15 | SuppParentVendorId | VENDOR_ID | — | — |
| 16 | SupplierAllowAwtFlag | ALLOW_AWT_FLAG | — | ✅ |
| 17 | SupplierAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | — |
| 18 | SupplierApTaxRoundingRule | AP_TAX_ROUNDING_RULE | — | — |
| 19 | SupplierAttribute1 | ATTRIBUTE1 | — | ✅ |
| 20 | SupplierAttribute10 | ATTRIBUTE10 | — | ✅ |
| 21 | SupplierAttribute11 | ATTRIBUTE11 | — | ✅ |
| 22 | SupplierAttribute12 | ATTRIBUTE12 | — | ✅ |
| 23 | SupplierAttribute13 | ATTRIBUTE13 | — | ✅ |
| 24 | SupplierAttribute14 | ATTRIBUTE14 | — | ✅ |
| 25 | SupplierAttribute15 | ATTRIBUTE15 | — | ✅ |
| 26 | SupplierAttribute16 | ATTRIBUTE16 | — | ✅ |
| 27 | SupplierAttribute17 | ATTRIBUTE17 | — | ✅ |
| 28 | SupplierAttribute18 | ATTRIBUTE18 | — | ✅ |
| 29 | SupplierAttribute19 | ATTRIBUTE19 | — | ✅ |
| 30 | SupplierAttribute2 | ATTRIBUTE2 | — | ✅ |
| 31 | SupplierAttribute20 | ATTRIBUTE20 | — | ✅ |
| 32 | SupplierAttribute3 | ATTRIBUTE3 | — | ✅ |
| 33 | SupplierAttribute4 | ATTRIBUTE4 | — | ✅ |
| 34 | SupplierAttribute5 | ATTRIBUTE5 | — | ✅ |
| 35 | SupplierAttribute6 | ATTRIBUTE6 | — | ✅ |
| 36 | SupplierAttribute7 | ATTRIBUTE7 | — | ✅ |
| 37 | SupplierAttribute8 | ATTRIBUTE8 | — | ✅ |
| 38 | SupplierAttribute9 | ATTRIBUTE9 | — | ✅ |
| 39 | SupplierAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 40 | SupplierAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 41 | SupplierAttributeDate10 | ATTRIBUTE_DATE10 | — | ✅ |
| 42 | SupplierAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 43 | SupplierAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 44 | SupplierAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 45 | SupplierAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 46 | SupplierAttributeDate6 | ATTRIBUTE_DATE6 | — | ✅ |
| 47 | SupplierAttributeDate7 | ATTRIBUTE_DATE7 | — | ✅ |
| 48 | SupplierAttributeDate8 | ATTRIBUTE_DATE8 | — | ✅ |
| 49 | SupplierAttributeDate9 | ATTRIBUTE_DATE9 | — | ✅ |
| 50 | SupplierAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 51 | SupplierAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 52 | SupplierAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 53 | SupplierAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 54 | SupplierAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 55 | SupplierAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 56 | SupplierAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 57 | SupplierAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 58 | SupplierAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 59 | SupplierAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 60 | SupplierAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 61 | SupplierAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | ✅ |
| 62 | SupplierAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 63 | SupplierAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 64 | SupplierAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 65 | SupplierAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 66 | SupplierAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | ✅ |
| 67 | SupplierAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | ✅ |
| 68 | SupplierAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | ✅ |
| 69 | SupplierAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | ✅ |
| 70 | SupplierAutoTaxCalcFlag | AUTO_TAX_CALC_FLAG | — | — |
| 71 | SupplierAutoTaxCalcOverride | AUTO_TAX_CALC_OVERRIDE | — | ✅ |
| 72 | SupplierAwtGroupId | AWT_GROUP_ID | — | — |
| 73 | SupplierBcNotApplicableFlag | BC_NOT_APPLICABLE_FLAG | — | ✅ |
| 74 | SupplierBusinessRelationship | BUSINESS_RELATIONSHIP | — | ✅ |
| 75 | SupplierCorporateWebsite | CORPORATE_WEBSITE | — | ✅ |
| 76 | SupplierCreatedBy | CREATED_BY | — | ✅ |
| 77 | SupplierCreationDate | CREATION_DATE | — | ✅ |
| 78 | SupplierCreationSource | CREATION_SOURCE | — | ✅ |
| 79 | SupplierCustomerNum | CUSTOMER_NUM | — | ✅ |
| 80 | SupplierEmployeeId | EMPLOYEE_ID | — | — |
| 81 | SupplierEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 82 | SupplierFederalReportableFlag | FEDERAL_REPORTABLE_FLAG | — | ✅ |
| 83 | SupplierGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | ✅ |
| 84 | SupplierGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | ✅ |
| 85 | SupplierGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | ✅ |
| 86 | SupplierGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | ✅ |
| 87 | SupplierGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | ✅ |
| 88 | SupplierGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | ✅ |
| 89 | SupplierGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | ✅ |
| 90 | SupplierGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | ✅ |
| 91 | SupplierGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | ✅ |
| 92 | SupplierGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | ✅ |
| 93 | SupplierGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | ✅ |
| 94 | SupplierGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | ✅ |
| 95 | SupplierGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | ✅ |
| 96 | SupplierGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | ✅ |
| 97 | SupplierGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | ✅ |
| 98 | SupplierGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | ✅ |
| 99 | SupplierGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | ✅ |
| 100 | SupplierGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | ✅ |
| 101 | SupplierGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | ✅ |
| 102 | SupplierGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | ✅ |
| 103 | SupplierGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | ✅ |
| 104 | SupplierGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | ✅ |
| 105 | SupplierGlobalAttributeDate10 | GLOBAL_ATTRIBUTE_DATE10 | — | ✅ |
| 106 | SupplierGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | ✅ |
| 107 | SupplierGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | ✅ |
| 108 | SupplierGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | ✅ |
| 109 | SupplierGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | ✅ |
| 110 | SupplierGlobalAttributeDate6 | GLOBAL_ATTRIBUTE_DATE6 | — | ✅ |
| 111 | SupplierGlobalAttributeDate7 | GLOBAL_ATTRIBUTE_DATE7 | — | ✅ |
| 112 | SupplierGlobalAttributeDate8 | GLOBAL_ATTRIBUTE_DATE8 | — | ✅ |
| 113 | SupplierGlobalAttributeDate9 | GLOBAL_ATTRIBUTE_DATE9 | — | ✅ |
| 114 | SupplierGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | ✅ |
| 115 | SupplierGlobalAttributeNumber10 | GLOBAL_ATTRIBUTE_NUMBER10 | — | ✅ |
| 116 | SupplierGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | ✅ |
| 117 | SupplierGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | ✅ |
| 118 | SupplierGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | ✅ |
| 119 | SupplierGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | ✅ |
| 120 | SupplierGlobalAttributeNumber6 | GLOBAL_ATTRIBUTE_NUMBER6 | — | ✅ |
| 121 | SupplierGlobalAttributeNumber7 | GLOBAL_ATTRIBUTE_NUMBER7 | — | ✅ |
| 122 | SupplierGlobalAttributeNumber8 | GLOBAL_ATTRIBUTE_NUMBER8 | — | ✅ |
| 123 | SupplierGlobalAttributeNumber9 | GLOBAL_ATTRIBUTE_NUMBER9 | — | ✅ |
| 124 | SupplierGlobalAttributeTimestamp1 | GLOBAL_ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 125 | SupplierGlobalAttributeTimestamp10 | GLOBAL_ATTRIBUTE_TIMESTAMP10 | — | ✅ |
| 126 | SupplierGlobalAttributeTimestamp2 | GLOBAL_ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 127 | SupplierGlobalAttributeTimestamp3 | GLOBAL_ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 128 | SupplierGlobalAttributeTimestamp4 | GLOBAL_ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 129 | SupplierGlobalAttributeTimestamp5 | GLOBAL_ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 130 | SupplierGlobalAttributeTimestamp6 | GLOBAL_ATTRIBUTE_TIMESTAMP6 | — | ✅ |
| 131 | SupplierGlobalAttributeTimestamp7 | GLOBAL_ATTRIBUTE_TIMESTAMP7 | — | ✅ |
| 132 | SupplierGlobalAttributeTimestamp8 | GLOBAL_ATTRIBUTE_TIMESTAMP8 | — | ✅ |
| 133 | SupplierGlobalAttributeTimestamp9 | GLOBAL_ATTRIBUTE_TIMESTAMP9 | — | ✅ |
| 134 | SupplierIncomeTaxIdFlag | INCOME_TAX_ID_FLAG | — | — |
| 135 | SupplierLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 136 | SupplierLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 137 | SupplierLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 138 | SupplierMinOrderAmount | MIN_ORDER_AMOUNT | — | — |
| 139 | SupplierNameControl | NAME_CONTROL | — | ✅ |
| 140 | SupplierNiNumberFlag | NI_NUMBER_FLAG | — | — |
| 141 | SupplierObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 142 | SupplierOffsetTaxFlag | OFFSET_TAX_FLAG | — | — |
| 143 | SupplierOffsetVatCode | OFFSET_VAT_CODE | — | — |
| 144 | SupplierOneTimeFlag | ONE_TIME_FLAG | — | ✅ |
| 145 | SupplierOrganizationTypeLookupCode | ORGANIZATION_TYPE_LOOKUP_CODE | — | ✅ |
| 146 | SupplierParentPartyId | PARENT_PARTY_ID | — | — |
| 147 | SupplierParentVendorId | PARENT_VENDOR_ID | — | ✅ |
| 148 | SupplierPartyId | PARTY_ID | — | ✅ |
| 149 | SupplierProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 150 | SupplierProgramId | PROGRAM_ID | — | — |
| 151 | SupplierProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 152 | SupplierRequestId | REQUEST_ID | — | — |
| 153 | SupplierReviewType | REVIEW_TYPE | — | ✅ |
| 154 | SupplierSegment1 | SEGMENT1 | — | ✅ |
| 155 | SupplierSpendAuthReviewStatus | SPEND_AUTH_REVIEW_STATUS | — | ✅ |
| 156 | SupplierStandardIndustryClass | STANDARD_INDUSTRY_CLASS | — | ✅ |
| 157 | SupplierStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 158 | SupplierStateReportableFlag | STATE_REPORTABLE_FLAG | — | ✅ |
| 159 | SupplierTaxReportingName | TAX_REPORTING_NAME | — | ✅ |
| 160 | SupplierTaxVerificationDate | TAX_VERIFICATION_DATE | — | ✅ |
| 161 | SupplierTaxpayerCountry | TAXPAYER_COUNTRY | — | ✅ |
| 162 | SupplierType1099 | TYPE_1099 | — | ✅ |
| 163 | SupplierVatCode | VAT_CODE | — | ✅ |
| 164 | SupplierVendorTypeLookupCode | VENDOR_TYPE_LOOKUP_CODE | — | ✅ |
| 165 | SupplierWithholdingStartDate | WITHHOLDING_START_DATE | — | — |
| 166 | SupplierWithholdingStatusLookupCode | WITHHOLDING_STATUS_LOOKUP_CODE | — | — |
| 167 | VendorId | VENDOR_ID | 🔑 | ✅ |

### [[poz_suppliers_pii|POZ_SUPPLIERS_PII]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DfIncomeTaxId | DF_INCOME_TAX_ID | — | ✅ |
| 2 | SupplierPIIIncomeTaxId | INCOME_TAX_ID | — | — |
| 3 | SupplierPIINiNumber | NI_NUMBER | — | — |
| 4 | SupplierPIIVatRegistrationNum | VAT_REGISTRATION_NUM | — | — |
| 5 | SupplierPIIVendorId | VENDOR_ID | — | — |

### [[zx_party_tax_profile|ZX_PARTY_TAX_PROFILE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyTaxProfileGenericCountryCode | COUNTRY_CODE | — | ✅ |
| 2 | PartyTaxProfileGenericPartyId | PARTY_ID | — | — |
| 3 | PartyTaxProfileGenericPartyTaxProfileId | PARTY_TAX_PROFILE_ID | — | — |
| 4 | PartyTaxProfileGenericPartyTypeCode | PARTY_TYPE_CODE | — | — |
| 5 | PartyTaxProfileGenericRepRegistrationNumber | REP_REGISTRATION_NUMBER | — | ✅ |
| 6 | PartyTaxProfileGenericTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | ✅ |

### [[zx_wht_tax_classification_v|ZX_WHT_TAX_CLASSIFICATION_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WithholdingTaxGroupsCreatedBy | CREATED_BY | — | — |
| 2 | WithholdingTaxGroupsCreationDate | CREATION_DATE | — | — |
| 3 | WithholdingTaxGroupsDescription | DESCRIPTION | — | — |
| 4 | WithholdingTaxGroupsGroupId | GROUP_ID | — | — |
| 5 | WithholdingTaxGroupsInactiveDate | INACTIVE_DATE | — | — |
| 6 | WithholdingTaxGroupsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | WithholdingTaxGroupsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | WithholdingTaxGroupsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | WithholdingTaxGroupsName | NAME | — | ✅ |
| 10 | WithholdingTaxGroupsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
