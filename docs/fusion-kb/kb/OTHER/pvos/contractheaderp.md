---
id: DOC-OTHER-PVO-ContractHeaderP
doc_type: system-doc
title: "ContractHeaderP — PVO Cross-Module"
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
  - ContractHeaderP
  - contractheaderp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContractHeaderP

## 📌 Visão Geral

View Object para extração BICC de dados de Contract Header P. Acessa as tabelas: FND_SETID_ASSIGNMENTS, FUN_ALL_BUSINESS_UNITS_V, GL_DAILY_CONVERSION_TYPES (+14).

**Caminho:** `FscmTopModelAM.ContractsCoreAM.ContractHeaderP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 463 | 17 | 2 | 80 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_setid_assignments|FND_SETID_ASSIGNMENTS]] — 16 atributos (4 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 2 atributos
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 8 atributos
- [[hr_organization_v|HR_ORGANIZATION_V]] — 6 atributos (1 BICC)
- [[hz_cust_accounts|HZ_CUST_ACCOUNTS]] — 9 atributos (3 BICC)
- [[hz_cust_site_uses_all|HZ_CUST_SITE_USES_ALL]] — 4 atributos (1 BICC)
- [[hz_locations|HZ_LOCATIONS]] — 15 atributos
- [[hz_parties|HZ_PARTIES]] — 137 atributos (14 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 86 atributos (6 BICC)
- [[inv_organization_definitions_v|INV_ORGANIZATION_DEFINITIONS_V]] — 2 atributos (1 BICC)
- [[okc_contract_types_tl|OKC_CONTRACT_TYPES_TL]] — 11 atributos (1 BICC)
- [[okc_contract_types_vl|OKC_CONTRACT_TYPES_VL]] — 38 atributos (5 BICC)
- [[okc_k_headers_all_b|OKC_K_HEADERS_ALL_B]] — 104 atributos (2 PKs, 35 BICC)
- [[okc_k_headers_tl|OKC_K_HEADERS_TL]] — 15 atributos (4 BICC)
- [[okc_k_inv_rev_summary_v|OKC_K_INV_REV_SUMMARY_V]] — 4 atributos (2 BICC)
- [[qsc_pricebook_headers_vl|QSC_PRICEBOOK_HEADERS_VL]] — 3 atributos (2 BICC)
- [[xle_entity_profiles|XLE_ENTITY_PROFILES]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[fnd_setid_assignments|FND_SETID_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CancelReasonSetIdAssignmentDeterminantType | DETERMINANT_TYPE | — | — |
| 2 | CancelReasonSetIdAssignmentDeterminantValue | DETERMINANT_VALUE | — | — |
| 3 | CancelReasonSetIdAssignmentReferenceGroupName | REFERENCE_GROUP_NAME | — | — |
| 4 | CancelReasonSetIdAssignmentSetId | SET_ID | — | ✅ |
| 5 | CloseReasonSetIdAssignmentDeterminantType | DETERMINANT_TYPE | — | — |
| 6 | CloseReasonSetIdAssignmentDeterminantValue | DETERMINANT_VALUE | — | — |
| 7 | CloseReasonSetIdAssignmentReferenceGroupName | REFERENCE_GROUP_NAME | — | — |
| 8 | CloseReasonSetIdAssignmentSetId | SET_ID | — | ✅ |
| 9 | HdrTaxClassPEODetType | DETERMINANT_TYPE | — | — |
| 10 | HdrTaxClassPEODetValue | DETERMINANT_VALUE | — | — |
| 11 | HdrTaxClassPEORefGpName | REFERENCE_GROUP_NAME | — | — |
| 12 | HdrTaxClassPEOSetId | SET_ID | — | ✅ |
| 13 | HoldReasonSetIdAssignmentDeterminantType | DETERMINANT_TYPE | — | — |
| 14 | HoldReasonSetIdAssignmentDeterminantValue | DETERMINANT_VALUE | — | — |
| 15 | HoldReasonSetIdAssignmentReferenceGroupName | REFERENCE_GROUP_NAME | — | — |
| 16 | HoldReasonSetIdAssignmentSetId | SET_ID | — | ✅ |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOId | BU_ID | — | — |
| 2 | HdrBUPEOBUName | BU_NAME | — | — |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHeaderInvConvRatePEOConversionType | CONVERSION_TYPE | — | — |
| 2 | ContractHeaderInvConvRatePEODescription | DESCRIPTION | — | — |
| 3 | ContractHeaderInvConvRatePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | ContractHeaderInvConvRatePEOUserConversionType | USER_CONVERSION_TYPE | — | — |
| 5 | ContractHeaderRevConvRatePEOConversionType | CONVERSION_TYPE | — | — |
| 6 | ContractHeaderRevConvRatePEODescription | DESCRIPTION | — | — |
| 7 | ContractHeaderRevConvRatePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | ContractHeaderRevConvRatePEOUserConversionType | USER_CONVERSION_TYPE | — | — |

### [[hr_organization_v|HR_ORGANIZATION_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHeaderOwingOrgPEOClassCode | CLASSIFICATION_CODE | — | — |
| 2 | ContractHeaderOwingOrgPEOEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | ContractHeaderOwingOrgPEOEffStrtDate | EFFECTIVE_START_DATE | — | — |
| 4 | ContractHeaderOwingOrgPEOName | NAME | — | ✅ |
| 5 | ContractHeaderOwingOrgPEOObjVerNum | OBJECT_VERSION_NUMBER | — | — |
| 6 | ContractHeaderOwingOrgPEOOrgId | ORGANIZATION_ID | — | — |

### [[hz_cust_accounts|HZ_CUST_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHeaderBillToPEOAccountName | ACCOUNT_NAME | — | ✅ |
| 2 | ContractHeaderBillToPEOAccountNumber | ACCOUNT_NUMBER | — | — |
| 3 | ContractHeaderBillToPEOCustAccountId | CUST_ACCOUNT_ID | — | — |
| 4 | ContractHeaderShipToPEOAccountName | ACCOUNT_NAME | — | ✅ |
| 5 | ContractHeaderShipToPEOAccountNumber | ACCOUNT_NUMBER | — | — |
| 6 | ContractHeaderShipToPEOCustAccountId | CUST_ACCOUNT_ID | — | — |
| 7 | ContractHeaderSoldToPEOAccountName | ACCOUNT_NAME | — | ✅ |
| 8 | ContractHeaderSoldToPEOAccountNumber | ACCOUNT_NUMBER | — | — |
| 9 | ContractHeaderSoldToPEOCustAccountId | CUST_ACCOUNT_ID | — | — |

### [[hz_cust_site_uses_all|HZ_CUST_SITE_USES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHeaderShipToSitePEOLocation | LOCATION | — | ✅ |
| 2 | HdrShipToSUPEOSiteUseId | SITE_USE_ID | — | — |
| 3 | HdrSoldToSUPEOSiteUseId | SITE_USE_ID | — | — |
| 4 | HdrSoldToSitePEOLocation | LOCATION | — | — |

### [[hz_locations|HZ_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HdrBillToAddress1 | ADDRESS1 | — | — |
| 2 | HdrBillToAddress2 | ADDRESS2 | — | — |
| 3 | HdrBillToAddress3 | ADDRESS3 | — | — |
| 4 | HdrBillToAddress4 | ADDRESS4 | — | — |
| 5 | HdrBillToLocationId | LOCATION_ID | — | — |
| 6 | HdrShipToAddress1 | ADDRESS1 | — | — |
| 7 | HdrShipToAddress2 | ADDRESS2 | — | — |
| 8 | HdrShipToAddress3 | ADDRESS3 | — | — |
| 9 | HdrShipToAddress4 | ADDRESS4 | — | — |
| 10 | HdrShipToLocationId | LOCATION_ID | — | — |
| 11 | HdrSoldToAddress1 | ADDRESS1 | — | — |
| 12 | HdrSoldToAddress2 | ADDRESS2 | — | — |
| 13 | HdrSoldToAddress3 | ADDRESS3 | — | — |
| 14 | HdrSoldToAddress4 | ADDRESS4 | — | — |
| 15 | HdrSoldToLocationId | LOCATION_ID | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HdrSupplierAddress1 | ADDRESS1 | — | ✅ |
| 2 | HdrSupplierAddress2 | ADDRESS2 | — | ✅ |
| 3 | HdrSupplierAddress3 | ADDRESS3 | — | ✅ |
| 4 | HdrSupplierAddress4 | ADDRESS4 | — | ✅ |
| 5 | HdrSupplierAnalysisFy | ANALYSIS_FY | — | — |
| 6 | HdrSupplierAttribute1 | ATTRIBUTE1 | — | — |
| 7 | HdrSupplierAttribute10 | ATTRIBUTE10 | — | — |
| 8 | HdrSupplierAttribute11 | ATTRIBUTE11 | — | — |
| 9 | HdrSupplierAttribute12 | ATTRIBUTE12 | — | — |
| 10 | HdrSupplierAttribute13 | ATTRIBUTE13 | — | — |
| 11 | HdrSupplierAttribute14 | ATTRIBUTE14 | — | — |
| 12 | HdrSupplierAttribute15 | ATTRIBUTE15 | — | — |
| 13 | HdrSupplierAttribute16 | ATTRIBUTE16 | — | — |
| 14 | HdrSupplierAttribute17 | ATTRIBUTE17 | — | — |
| 15 | HdrSupplierAttribute18 | ATTRIBUTE18 | — | — |
| 16 | HdrSupplierAttribute19 | ATTRIBUTE19 | — | — |
| 17 | HdrSupplierAttribute2 | ATTRIBUTE2 | — | — |
| 18 | HdrSupplierAttribute20 | ATTRIBUTE20 | — | — |
| 19 | HdrSupplierAttribute21 | ATTRIBUTE21 | — | — |
| 20 | HdrSupplierAttribute22 | ATTRIBUTE22 | — | — |
| 21 | HdrSupplierAttribute23 | ATTRIBUTE23 | — | — |
| 22 | HdrSupplierAttribute24 | ATTRIBUTE24 | — | — |
| 23 | HdrSupplierAttribute25 | ATTRIBUTE25 | — | — |
| 24 | HdrSupplierAttribute26 | ATTRIBUTE26 | — | — |
| 25 | HdrSupplierAttribute27 | ATTRIBUTE27 | — | — |
| 26 | HdrSupplierAttribute28 | ATTRIBUTE28 | — | — |
| 27 | HdrSupplierAttribute29 | ATTRIBUTE29 | — | — |
| 28 | HdrSupplierAttribute3 | ATTRIBUTE3 | — | — |
| 29 | HdrSupplierAttribute30 | ATTRIBUTE30 | — | — |
| 30 | HdrSupplierAttribute4 | ATTRIBUTE4 | — | — |
| 31 | HdrSupplierAttribute5 | ATTRIBUTE5 | — | — |
| 32 | HdrSupplierAttribute6 | ATTRIBUTE6 | — | — |
| 33 | HdrSupplierAttribute7 | ATTRIBUTE7 | — | — |
| 34 | HdrSupplierAttribute8 | ATTRIBUTE8 | — | — |
| 35 | HdrSupplierAttribute9 | ATTRIBUTE9 | — | — |
| 36 | HdrSupplierAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 37 | HdrSupplierAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 38 | HdrSupplierAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 39 | HdrSupplierAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 40 | HdrSupplierAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 41 | HdrSupplierAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 42 | HdrSupplierAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 43 | HdrSupplierAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 44 | HdrSupplierAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 45 | HdrSupplierAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 46 | HdrSupplierAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 47 | HdrSupplierAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 48 | HdrSupplierAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 49 | HdrSupplierAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 50 | HdrSupplierAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 51 | HdrSupplierAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 52 | HdrSupplierAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 53 | HdrSupplierAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 54 | HdrSupplierAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 55 | HdrSupplierAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 56 | HdrSupplierAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 57 | HdrSupplierAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 58 | HdrSupplierAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 59 | HdrSupplierAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 60 | HdrSupplierAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 61 | HdrSupplierCategoryCode | CATEGORY_CODE | — | — |
| 62 | HdrSupplierCeoName | CEO_NAME | — | — |
| 63 | HdrSupplierCertReasonCode | CERT_REASON_CODE | — | — |
| 64 | HdrSupplierCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 65 | HdrSupplierCity | CITY | — | ✅ |
| 66 | HdrSupplierComments | COMMENTS | — | — |
| 67 | HdrSupplierCountry | COUNTRY | — | ✅ |
| 68 | HdrSupplierCounty | COUNTY | — | — |
| 69 | HdrSupplierCreatedBy | CREATED_BY | — | — |
| 70 | HdrSupplierCreatedByModule | CREATED_BY_MODULE | — | — |
| 71 | HdrSupplierCreationDate | CREATION_DATE | — | — |
| 72 | HdrSupplierCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 73 | HdrSupplierDateOfBirth | DATE_OF_BIRTH | — | — |
| 74 | HdrSupplierDunsNumberC | DUNS_NUMBER_C | — | — |
| 75 | HdrSupplierEmailAddress | EMAIL_ADDRESS | — | — |
| 76 | HdrSupplierEmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 77 | HdrSupplierFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 78 | HdrSupplierGender | GENDER | — | — |
| 79 | HdrSupplierGroupType | GROUP_TYPE | — | — |
| 80 | HdrSupplierGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 81 | HdrSupplierHomeCountry | HOME_COUNTRY | — | — |
| 82 | HdrSupplierHqBranchInd | HQ_BRANCH_IND | — | — |
| 83 | HdrSupplierIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 84 | HdrSupplierIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 85 | HdrSupplierInternalFlag | INTERNAL_FLAG | — | — |
| 86 | HdrSupplierJgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 87 | HdrSupplierLanguageName | LANGUAGE_NAME | — | — |
| 88 | HdrSupplierLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 89 | HdrSupplierLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 90 | HdrSupplierLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 91 | HdrSupplierMaritalStatus | MARITAL_STATUS | — | — |
| 92 | HdrSupplierMissionStatement | MISSION_STATEMENT | — | — |
| 93 | HdrSupplierNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 94 | HdrSupplierObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 95 | HdrSupplierOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 96 | HdrSupplierPartyId | PARTY_ID | — | — |
| 97 | HdrSupplierPartyName | PARTY_NAME | — | ✅ |
| 98 | HdrSupplierPartyNumber | PARTY_NUMBER | — | ✅ |
| 99 | HdrSupplierPartyType | PARTY_TYPE | — | — |
| 100 | HdrSupplierPartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 101 | HdrSupplierPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 102 | HdrSupplierPersonFirstName | PERSON_FIRST_NAME | — | ✅ |
| 103 | HdrSupplierPersonLastName | PERSON_LAST_NAME | — | ✅ |
| 104 | HdrSupplierPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 105 | HdrSupplierPersonMiddleName | PERSON_MIDDLE_NAME | — | ✅ |
| 106 | HdrSupplierPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 107 | HdrSupplierPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 108 | HdrSupplierPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 109 | HdrSupplierPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 110 | HdrSupplierPersonTitle | PERSON_TITLE | — | — |
| 111 | HdrSupplierPostalCode | POSTAL_CODE | — | ✅ |
| 112 | HdrSupplierPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 113 | HdrSupplierPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 114 | HdrSupplierPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 115 | HdrSupplierPreferredName | PREFERRED_NAME | — | — |
| 116 | HdrSupplierPreferredNameId | PREFERRED_NAME_ID | — | — |
| 117 | HdrSupplierPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 118 | HdrSupplierPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 119 | HdrSupplierPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 120 | HdrSupplierPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 121 | HdrSupplierPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 122 | HdrSupplierPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 123 | HdrSupplierPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | — |
| 124 | HdrSupplierPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 125 | HdrSupplierPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 126 | HdrSupplierProvince | PROVINCE | — | — |
| 127 | HdrSupplierSalutation | SALUTATION | — | — |
| 128 | HdrSupplierSicCode | SIC_CODE | — | — |
| 129 | HdrSupplierSicCodeType | SIC_CODE_TYPE | — | — |
| 130 | HdrSupplierState | STATE | — | ✅ |
| 131 | HdrSupplierStatus | STATUS | — | — |
| 132 | HdrSupplierThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 133 | HdrSupplierTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 134 | HdrSupplierUrl | URL | — | — |
| 135 | HdrSupplierUserGuid | USER_GUID | — | — |
| 136 | HdrSupplierValidatedFlag | VALIDATED_FLAG | — | — |
| 137 | HdrSupplierYearEstablished | YEAR_ESTABLISHED | — | — |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HdrSupplierSiteActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | HdrSupplierSiteAddressee | ADDRESSEE | — | — |
| 3 | HdrSupplierSiteAttribute1 | ATTRIBUTE1 | — | — |
| 4 | HdrSupplierSiteAttribute10 | ATTRIBUTE10 | — | — |
| 5 | HdrSupplierSiteAttribute11 | ATTRIBUTE11 | — | — |
| 6 | HdrSupplierSiteAttribute12 | ATTRIBUTE12 | — | — |
| 7 | HdrSupplierSiteAttribute13 | ATTRIBUTE13 | — | — |
| 8 | HdrSupplierSiteAttribute14 | ATTRIBUTE14 | — | — |
| 9 | HdrSupplierSiteAttribute15 | ATTRIBUTE15 | — | — |
| 10 | HdrSupplierSiteAttribute16 | ATTRIBUTE16 | — | — |
| 11 | HdrSupplierSiteAttribute17 | ATTRIBUTE17 | — | — |
| 12 | HdrSupplierSiteAttribute18 | ATTRIBUTE18 | — | — |
| 13 | HdrSupplierSiteAttribute19 | ATTRIBUTE19 | — | — |
| 14 | HdrSupplierSiteAttribute2 | ATTRIBUTE2 | — | — |
| 15 | HdrSupplierSiteAttribute20 | ATTRIBUTE20 | — | — |
| 16 | HdrSupplierSiteAttribute21 | ATTRIBUTE21 | — | — |
| 17 | HdrSupplierSiteAttribute22 | ATTRIBUTE22 | — | — |
| 18 | HdrSupplierSiteAttribute23 | ATTRIBUTE23 | — | — |
| 19 | HdrSupplierSiteAttribute24 | ATTRIBUTE24 | — | — |
| 20 | HdrSupplierSiteAttribute25 | ATTRIBUTE25 | — | — |
| 21 | HdrSupplierSiteAttribute26 | ATTRIBUTE26 | — | — |
| 22 | HdrSupplierSiteAttribute27 | ATTRIBUTE27 | — | — |
| 23 | HdrSupplierSiteAttribute28 | ATTRIBUTE28 | — | — |
| 24 | HdrSupplierSiteAttribute29 | ATTRIBUTE29 | — | — |
| 25 | HdrSupplierSiteAttribute3 | ATTRIBUTE3 | — | — |
| 26 | HdrSupplierSiteAttribute30 | ATTRIBUTE30 | — | — |
| 27 | HdrSupplierSiteAttribute4 | ATTRIBUTE4 | — | — |
| 28 | HdrSupplierSiteAttribute5 | ATTRIBUTE5 | — | — |
| 29 | HdrSupplierSiteAttribute6 | ATTRIBUTE6 | — | — |
| 30 | HdrSupplierSiteAttribute7 | ATTRIBUTE7 | — | — |
| 31 | HdrSupplierSiteAttribute8 | ATTRIBUTE8 | — | — |
| 32 | HdrSupplierSiteAttribute9 | ATTRIBUTE9 | — | — |
| 33 | HdrSupplierSiteAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 34 | HdrSupplierSiteAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 35 | HdrSupplierSiteAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 36 | HdrSupplierSiteAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 37 | HdrSupplierSiteAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 38 | HdrSupplierSiteAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 39 | HdrSupplierSiteAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 40 | HdrSupplierSiteAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 41 | HdrSupplierSiteAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 42 | HdrSupplierSiteAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 43 | HdrSupplierSiteAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 44 | HdrSupplierSiteAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 45 | HdrSupplierSiteAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 46 | HdrSupplierSiteAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 47 | HdrSupplierSiteAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 48 | HdrSupplierSiteAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 49 | HdrSupplierSiteAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 50 | HdrSupplierSiteAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 51 | HdrSupplierSiteAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 52 | HdrSupplierSiteAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 53 | HdrSupplierSiteAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 54 | HdrSupplierSiteAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 55 | HdrSupplierSiteAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 56 | HdrSupplierSiteAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 57 | HdrSupplierSiteAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 58 | HdrSupplierSiteComments | COMMENTS | — | — |
| 59 | HdrSupplierSiteCreatedBy | CREATED_BY | — | — |
| 60 | HdrSupplierSiteCreatedByModule | CREATED_BY_MODULE | — | — |
| 61 | HdrSupplierSiteCreationDate | CREATION_DATE | — | — |
| 62 | HdrSupplierSiteDunsNumberC | DUNS_NUMBER_C | — | — |
| 63 | HdrSupplierSiteEndDateActive | END_DATE_ACTIVE | — | — |
| 64 | HdrSupplierSiteGlobalLocationNumber | GLOBAL_LOCATION_NUMBER | — | — |
| 65 | HdrSupplierSiteIdentifyingAddressFlag | IDENTIFYING_ADDRESS_FLAG | — | — |
| 66 | HdrSupplierSiteLanguage | PARTY_SITE_LANGUAGE | — | — |
| 67 | HdrSupplierSiteLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 68 | HdrSupplierSiteLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 69 | HdrSupplierSiteLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 70 | HdrSupplierSiteLocationId | LOCATION_ID | — | — |
| 71 | HdrSupplierSiteMailstop | MAILSTOP | — | — |
| 72 | HdrSupplierSiteObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 73 | HdrSupplierSiteOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 74 | HdrSupplierSiteOverallPrimaryFlag | OVERALL_PRIMARY_FLAG | — | — |
| 75 | HdrSupplierSitePartyId | PARTY_ID | — | — |
| 76 | HdrSupplierSitePartyNameDba | PARTY_NAME_DBA | — | — |
| 77 | HdrSupplierSitePartyNameDivision | PARTY_NAME_DIVISION | — | — |
| 78 | HdrSupplierSitePartyNameLegal | PARTY_NAME_LEGAL | — | — |
| 79 | HdrSupplierSitePartySiteId | PARTY_SITE_ID | — | — |
| 80 | HdrSupplierSitePartySiteName | PARTY_SITE_NAME | — | ✅ |
| 81 | HdrSupplierSitePartySiteNumber | PARTY_SITE_NUMBER | — | ✅ |
| 82 | HdrSupplierSitePartySiteType | PARTY_SITE_TYPE | — | ✅ |
| 83 | HdrSupplierSitePartyUsageCode | PARTY_USAGE_CODE | — | — |
| 84 | HdrSupplierSiteRelationshipId | RELATIONSHIP_ID | — | — |
| 85 | HdrSupplierSiteStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 86 | HdrSupplierSiteStatus | STATUS | — | ✅ |

### [[inv_organization_definitions_v|INV_ORGANIZATION_DEFINITIONS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHeaderInvOrgPEOOrganizationId | ORGANIZATION_ID | — | — |
| 2 | ContractHeaderInvOrgPEOOrganizationName | ORGANIZATION_NAME | — | ✅ |

### [[okc_contract_types_tl|OKC_CONTRACT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OKCTypeTPEOCreatedBy | CREATED_BY | — | — |
| 2 | OKCTypeTPEOCreationDate | CREATION_DATE | — | — |
| 3 | OKCTypeTPEODescription | DESCRIPTION | — | — |
| 4 | OKCTypeTPEOId | CONTRACT_TYPE_ID | — | — |
| 5 | OKCTypeTPEOLanguage | LANGUAGE | — | — |
| 6 | OKCTypeTPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | OKCTypeTPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | OKCTypeTPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | OKCTypeTPEOName | NAME | — | — |
| 10 | OKCTypeTPEOObjVerNum | OBJECT_VERSION_NUMBER | — | — |
| 11 | OKCTypeTPEOSourceLang | SOURCE_LANG | — | — |

### [[okc_contract_types_vl|OKC_CONTRACT_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractTypePEOAgreementEnabledFlag | AGREEMENT_ENABLED_FLAG | — | — |
| 2 | ContractTypePEOAllowLinesFlag | ALLOW_LINES_FLAG | — | — |
| 3 | ContractTypePEOBillingLimitType | BILLING_LIMIT_TYPE | — | — |
| 4 | ContractTypePEOContractClass | CONTRACT_CLASS | — | — |
| 5 | ContractTypePEOContractGroupId | CONTRACT_GROUP_ID | — | — |
| 6 | ContractTypePEOContractLayoutTemplate | CONTRACT_LAYOUT_TEMPLATE | — | — |
| 7 | ContractTypePEOContractTypeCode | CONTRACT_TYPE_CODE | — | — |
| 8 | ContractTypePEOContractTypeId | CONTRACT_TYPE_ID | — | — |
| 9 | ContractTypePEOCreatedBy | CREATED_BY | — | — |
| 10 | ContractTypePEOCreationDate | CREATION_DATE | — | — |
| 11 | ContractTypePEODaysToExpiration | DAYS_TO_EXPIRATION | — | — |
| 12 | ContractTypePEODescription | DESCRIPTION | — | ✅ |
| 13 | ContractTypePEOEnableBillingCtrlFlag | ENABLE_BILLING_CTRL_FLAG | — | — |
| 14 | ContractTypePEOEndDate | END_DATE | — | — |
| 15 | ContractTypePEOIntent | INTENT | — | — |
| 16 | ContractTypePEOInterCompanyFlag | INTER_COMPANY_FLAG | — | ✅ |
| 17 | ContractTypePEOInterProjectFlag | INTER_PROJECT_FLAG | — | ✅ |
| 18 | ContractTypePEOInteractionsEnabledFlag | INTERACTIONS_ENABLED_FLAG | — | — |
| 19 | ContractTypePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 20 | ContractTypePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | ContractTypePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 22 | ContractTypePEOLayoutTemplateId | LAYOUT_TEMPLATE_ID | — | — |
| 23 | ContractTypePEOLineAutonumberEnabledFlag | LINE_AUTONUMBER_ENABLED_FLAG | — | — |
| 24 | ContractTypePEOLineClass | LINE_CLASS | — | — |
| 25 | ContractTypePEOName | NAME | — | ✅ |
| 26 | ContractTypePEONotifyBeforeExpFlag | NOTIFY_BEFORE_EXP_FLAG | — | — |
| 27 | ContractTypePEONotifyContactRole | NOTIFY_CONTACT_ROLE | — | — |
| 28 | ContractTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 29 | ContractTypePEOPrimaryBuyerRole | PRIMARY_BUYER_ROLE | — | — |
| 30 | ContractTypePEOQclId | QCL_ID | — | — |
| 31 | ContractTypePEORelatedKEnabledFlag | RELATED_K_ENABLED_FLAG | — | — |
| 32 | ContractTypePEORequesterContactRole | REQUESTER_CONTACT_ROLE | — | — |
| 33 | ContractTypePEORisksEnabledFlag | RISKS_ENABLED_FLAG | — | — |
| 34 | ContractTypePEOSetId | SET_ID | — | — |
| 35 | ContractTypePEOSignatureRequiredFlag | SIGNATURE_REQUIRED_FLAG | — | — |
| 36 | ContractTypePEOStartDate | START_DATE | — | — |
| 37 | ContractTypePEOTermsEnabledFlag | TERMS_ENABLED_FLAG | — | — |
| 38 | ContractTypePEOTermsLayoutTemplate | TERMS_LAYOUT_TEMPLATE | — | — |

### [[okc_k_headers_all_b|OKC_K_HEADERS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHdrCommitmentAmount | COMMITMENT_AMOUNT | — | — |
| 2 | ContractHeaderBasePEOAcctRuleId | ACCT_RULE_ID | — | — |
| 3 | ContractHeaderBasePEOAgreedAmount | AGREED_AMOUNT | — | ✅ |
| 4 | ContractHeaderBasePEOAmendmentEffectiveDate | AMENDMENT_EFFECTIVE_DATE | — | ✅ |
| 5 | ContractHeaderBasePEOApTermsId | AP_TERMS_ID | — | — |
| 6 | ContractHeaderBasePEOArInterfaceYn | AR_INTERFACE_YN | — | — |
| 7 | ContractHeaderBasePEOAssigneeId | ASSIGNEE_ID | — | ✅ |
| 8 | ContractHeaderBasePEOAssigneeType | ASSIGNEE_TYPE | — | ✅ |
| 9 | ContractHeaderBasePEOAutoReleaseInvoice | AUTO_RELEASE_INVOICE | — | — |
| 10 | ContractHeaderBasePEOBaseContractYn | BASE_CONTRACT_YN | — | — |
| 11 | ContractHeaderBasePEOBillSequence | BILL_SEQUENCE | — | — |
| 12 | ContractHeaderBasePEOBillToAcctId | BILL_TO_ACCT_ID | — | — |
| 13 | ContractHeaderBasePEOBillToSiteUseId | BILL_TO_SITE_USE_ID | — | — |
| 14 | ContractHeaderBasePEOBilledAtSource | BILLED_AT_SOURCE | — | — |
| 15 | ContractHeaderBasePEOBilltoLocationId | BILLTO_LOCATION_ID | — | — |
| 16 | ContractHeaderBasePEOBuyOrSell | BUY_OR_SELL | — | — |
| 17 | ContractHeaderBasePEOCancelledAmount | CANCELLED_AMOUNT | — | — |
| 18 | ContractHeaderBasePEOCarrierId | CARRIER_ID | — | — |
| 19 | ContractHeaderBasePEOCommitmentId | COMMITMENT_ID | — | — |
| 20 | ContractHeaderBasePEOContractNumber | CONTRACT_NUMBER | — | ✅ |
| 21 | ContractHeaderBasePEOContractNumberModifier | CONTRACT_NUMBER_MODIFIER | — | — |
| 22 | ContractHeaderBasePEOContractTypeId | CONTRACT_TYPE_ID | — | ✅ |
| 23 | ContractHeaderBasePEOContributionPercent | CONTRIBUTION_PERCENT | — | — |
| 24 | ContractHeaderBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 25 | ContractHeaderBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 26 | ContractHeaderBasePEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 27 | ContractHeaderBasePEOCustPoNumber | CUST_PO_NUMBER | — | ✅ |
| 28 | ContractHeaderBasePEOCustPoNumberReqYn | CUST_PO_NUMBER_REQ_YN | — | — |
| 29 | ContractHeaderBasePEODateApproved | DATE_APPROVED | — | ✅ |
| 30 | ContractHeaderBasePEODateSigned | DATE_SIGNED | — | ✅ |
| 31 | ContractHeaderBasePEODateTerminated | DATE_TERMINATED | — | ✅ |
| 32 | ContractHeaderBasePEODatetimeCancelled | DATETIME_CANCELLED | — | ✅ |
| 33 | ContractHeaderBasePEOEndDate | END_DATE | — | ✅ |
| 34 | ContractHeaderBasePEOEstimatedAmount | ESTIMATED_AMOUNT | — | ✅ |
| 35 | ContractHeaderBasePEOExemptCertificateNumber | EXEMPT_CERTIFICATE_NUMBER | — | ✅ |
| 36 | ContractHeaderBasePEOExemptReasonCode | EXEMPT_REASON_CODE | — | ✅ |
| 37 | ContractHeaderBasePEOFob | FOB | — | — |
| 38 | ContractHeaderBasePEOFreightTerms | FREIGHT_TERMS | — | — |
| 39 | ContractHeaderBasePEOHoldBilling | HOLD_BILLING | — | — |
| 40 | ContractHeaderBasePEOHoldReasonCode | HOLD_REASON_CODE | — | ✅ |
| 41 | ContractHeaderBasePEOHoldReasonCodeSetId | HOLD_REASON_CODE_SET_ID | — | ✅ |
| 42 | ContractHeaderBasePEOHoldUntilDate | HOLD_UNTIL_DATE | — | ✅ |
| 43 | ContractHeaderBasePEOInvConvRateDate | INV_CONV_RATE_DATE | — | — |
| 44 | ContractHeaderBasePEOInvConvRateDateType | INV_CONV_RATE_DATE_TYPE | — | — |
| 45 | ContractHeaderBasePEOInvConvRateType | INV_CONV_RATE_TYPE | — | — |
| 46 | ContractHeaderBasePEOInvOrganizationId | INV_ORGANIZATION_ID | — | — |
| 47 | ContractHeaderBasePEOInvPrepayTrxTypeId | INV_PREPAY_TRX_TYPE_ID | — | — |
| 48 | ContractHeaderBasePEOInvPrintProfile | INV_PRINT_PROFILE | — | — |
| 49 | ContractHeaderBasePEOInvRuleId | INV_RULE_ID | — | — |
| 50 | ContractHeaderBasePEOInvTrxTypeId | INV_TRX_TYPE_ID | — | — |
| 51 | ContractHeaderBasePEOLastRevRecogDate | LAST_REV_RECOG_DATE | — | ✅ |
| 52 | ContractHeaderBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 53 | ContractHeaderBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 54 | ContractHeaderBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 55 | ContractHeaderBasePEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 56 | ContractHeaderBasePEOLineAutonumberEnabledFlag | LINE_AUTONUMBER_ENABLED_FLAG | — | — |
| 57 | ContractHeaderBasePEONetInvoiceFlag | NET_INVOICE_FLAG | — | ✅ |
| 58 | ContractHeaderBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 59 | ContractHeaderBasePEOOrderId | ORDER_ID | — | — |
| 60 | ContractHeaderBasePEOOrderNumber | ORDER_NUMBER | — | — |
| 61 | ContractHeaderBasePEOOrgId | ORG_ID | — | — |
| 62 | ContractHeaderBasePEOOrigSystemId1 | ORIG_SYSTEM_ID1 | — | — |
| 63 | ContractHeaderBasePEOOrigSystemReference1 | ORIG_SYSTEM_REFERENCE1 | — | — |
| 64 | ContractHeaderBasePEOOrigSystemSourceCode | ORIG_SYSTEM_SOURCE_CODE | — | — |
| 65 | ContractHeaderBasePEOOutputTaxClassificationCode | OUTPUT_TAX_CLASSIFICATION_CODE | — | ✅ |
| 66 | ContractHeaderBasePEOOverallRiskCode | OVERALL_RISK_CODE | — | ✅ |
| 67 | ContractHeaderBasePEOOwningOrgId | OWNING_ORG_ID | — | — |
| 68 | ContractHeaderBasePEOPaymentInstructionType | PAYMENT_INSTRUCTION_TYPE | — | — |
| 69 | ContractHeaderBasePEOPaymentTermId | PAYMENT_TERM_ID | — | — |
| 70 | ContractHeaderBasePEOPaymentType | PAYMENT_TYPE | — | — |
| 71 | ContractHeaderBasePEOPriceListId | PRICE_LIST_ID | — | — |
| 72 | ContractHeaderBasePEOPrimaryEntPartyId | PRIMARY_ENT_PARTY_ID | — | — |
| 73 | ContractHeaderBasePEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 74 | ContractHeaderBasePEOProgramName | PROGRAM_NAME | — | — |
| 75 | ContractHeaderBasePEOQclId | QCL_ID | — | — |
| 76 | ContractHeaderBasePEORecvInvOrgId | RECV_INV_ORG_ID | — | — |
| 77 | ContractHeaderBasePEORequestId | REQUEST_ID | — | — |
| 78 | ContractHeaderBasePEORevConvRateType | REV_CONV_RATE_TYPE | — | — |
| 79 | ContractHeaderBasePEOShareWithExternalPartyYn | SHARE_WITH_EXTERNAL_PARTY_YN | — | ✅ |
| 80 | ContractHeaderBasePEOShipInvOrgId | SHIP_INV_ORG_ID | — | — |
| 81 | ContractHeaderBasePEOShipToAcctId | SHIP_TO_ACCT_ID | — | — |
| 82 | ContractHeaderBasePEOShipToSiteUseId | SHIP_TO_SITE_USE_ID | — | — |
| 83 | ContractHeaderBasePEOShiptoLocationId | SHIPTO_LOCATION_ID | — | — |
| 84 | ContractHeaderBasePEOSoldToAcctId | SOLD_TO_ACCT_ID | — | — |
| 85 | ContractHeaderBasePEOSoldToSiteId | SOLD_TO_SITE_ID | — | — |
| 86 | ContractHeaderBasePEOStartDate | START_DATE | — | ✅ |
| 87 | ContractHeaderBasePEOStsCode | STS_CODE | — | ✅ |
| 88 | ContractHeaderBasePEOSummaryTrxYn | SUMMARY_TRX_YN | — | — |
| 89 | ContractHeaderBasePEOSupplierId | SUPPLIER_ID | — | — |
| 90 | ContractHeaderBasePEOSupplierSiteId | SUPPLIER_SITE_ID | — | — |
| 91 | ContractHeaderBasePEOTaskId | TASK_ID | — | — |
| 92 | ContractHeaderBasePEOTaxAmount | TAX_AMOUNT | — | — |
| 93 | ContractHeaderBasePEOTaxExemptionControl | TAX_EXEMPTION_CONTROL | — | ✅ |
| 94 | ContractHeaderBasePEOTemplateUsed | TEMPLATE_USED | — | — |
| 95 | ContractHeaderBasePEOTemplateYn | TEMPLATE_YN | — | — |
| 96 | ContractHeaderBasePEOTermCancelSource | TERM_CANCEL_SOURCE | — | — |
| 97 | ContractHeaderBasePEOTrnCode | TRN_CODE | — | — |
| 98 | ContractHeaderBasePEOTrnCodeSetId | TRN_CODE_SET_ID | — | — |
| 99 | ContractHeaderBasePEOUnderAmendVersionFlag | UNDER_AMEND_VERSION_FLAG | — | — |
| 100 | ContractHeaderBasePEOVersionType | VERSION_TYPE | — | ✅ |
| 101 | ContractId | CONTRACT_ID | — | — |
| 102 | Id | ID | 🔑 | ✅ |
| 103 | MajorVersion | MAJOR_VERSION | 🔑 | ✅ |
| 104 | UserStatusCode | USER_STATUS_CODE | — | — |

### [[okc_k_headers_tl|OKC_K_HEADERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHeaderTranslationPEOCognomen | COGNOMEN | — | ✅ |
| 2 | ContractHeaderTranslationPEOCreatedBy | CREATED_BY | — | — |
| 3 | ContractHeaderTranslationPEOCreationDate | CREATION_DATE | — | — |
| 4 | ContractHeaderTranslationPEODescription | DESCRIPTION | — | ✅ |
| 5 | ContractHeaderTranslationPEOId | ID | — | — |
| 6 | ContractHeaderTranslationPEOLanguage | LANGUAGE | — | — |
| 7 | ContractHeaderTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ContractHeaderTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ContractHeaderTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ContractHeaderTranslationPEOMajorVersion | MAJOR_VERSION | — | — |
| 11 | ContractHeaderTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ContractHeaderTranslationPEOShortDescription | SHORT_DESCRIPTION | — | — |
| 13 | ContractHeaderTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 14 | ContractHeaderTranslationPEOVersionDescription | VERSION_DESCRIPTION | — | ✅ |
| 15 | ContractHeaderTranslationPEOVersionType | VERSION_TYPE | — | — |

### [[okc_k_inv_rev_summary_v|OKC_K_INV_REV_SUMMARY_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OKCInvRevSmryContractId | CONTRACT_ID | — | — |
| 2 | OKCInvRevSmryContractLineId | CONTRACT_LINE_ID | — | — |
| 3 | OKCInvRevSmryInvoiced | INVOICED | — | ✅ |
| 4 | OKCInvRevSmryRevenue | REVENUE | — | ✅ |

### [[qsc_pricebook_headers_vl|QSC_PRICEBOOK_HEADERS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | PriceBookHeaderEOName | NAME | — | ✅ |
| 3 | PricebookId | PRICEBOOK_ID | — | ✅ |

### [[xle_entity_profiles|XLE_ENTITY_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHeaderLegalEntityPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 2 | ContractHeaderLegalEntityPEOName | NAME | — | ✅ |
| 3 | ContractHeaderLegalEntityPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
