---
id: DOC-OTHER-PVO-StudentPVO
doc_type: system-doc
title: "StudentPVO — PVO Cross-Module"
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
  - StudentPVO
  - studentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# StudentPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Student. Acessa as tabelas: HEY_ESTABLISHMENT_V, HEY_PERSONAL_DETAIL, HZ_ADDTNL_PARTY_NAMES (+2).

**Caminho:** `FscmTopModelAM.StudentEnrollmentAM.StudentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 417 | 5 | 1 | 42 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[hey_establishment_v|HEY_ESTABLISHMENT_V]] — 5 atributos (2 BICC)
- [[hey_personal_detail|HEY_PERSONAL_DETAIL]] — 73 atributos (15 BICC)
- [[hz_addtnl_party_names|HZ_ADDTNL_PARTY_NAMES]] — 57 atributos (8 BICC)
- [[hz_parties|HZ_PARTIES]] — 140 atributos (1 PKs, 5 BICC)
- [[hz_person_profiles|HZ_PERSON_PROFILES]] — 142 atributos (12 BICC)

---

## ⚙️ Atributos

### [[hey_establishment_v|HEY_ESTABLISHMENT_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EstablishmentPEOAffiliationType | AFFILIATION_TYPE_CODE | — | ✅ |
| 2 | EstablishmentPEOConstituentId | CONSTITUENT_IDENTIFIER | — | ✅ |
| 3 | EstablishmentPEOEndDate | END_DATE | — | — |
| 4 | EstablishmentPEOPartyId | PARTY_ID | — | — |
| 5 | EstablishmentPEOStartDate | START_DATE | — | — |

### [[hey_personal_detail|HEY_PERSONAL_DETAIL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonalDetailPEOAttachmentId | ATTACHMENT_ID | — | — |
| 2 | PersonalDetailPEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | PersonalDetailPEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | PersonalDetailPEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | PersonalDetailPEOAttribute12 | ATTRIBUTE12 | — | — |
| 6 | PersonalDetailPEOAttribute13 | ATTRIBUTE13 | — | — |
| 7 | PersonalDetailPEOAttribute14 | ATTRIBUTE14 | — | — |
| 8 | PersonalDetailPEOAttribute15 | ATTRIBUTE15 | — | — |
| 9 | PersonalDetailPEOAttribute16 | ATTRIBUTE16 | — | — |
| 10 | PersonalDetailPEOAttribute17 | ATTRIBUTE17 | — | — |
| 11 | PersonalDetailPEOAttribute18 | ATTRIBUTE18 | — | — |
| 12 | PersonalDetailPEOAttribute19 | ATTRIBUTE19 | — | — |
| 13 | PersonalDetailPEOAttribute2 | ATTRIBUTE2 | — | — |
| 14 | PersonalDetailPEOAttribute20 | ATTRIBUTE20 | — | — |
| 15 | PersonalDetailPEOAttribute3 | ATTRIBUTE3 | — | — |
| 16 | PersonalDetailPEOAttribute4 | ATTRIBUTE4 | — | — |
| 17 | PersonalDetailPEOAttribute5 | ATTRIBUTE5 | — | — |
| 18 | PersonalDetailPEOAttribute6 | ATTRIBUTE6 | — | — |
| 19 | PersonalDetailPEOAttribute7 | ATTRIBUTE7 | — | — |
| 20 | PersonalDetailPEOAttribute8 | ATTRIBUTE8 | — | — |
| 21 | PersonalDetailPEOAttribute9 | ATTRIBUTE9 | — | — |
| 22 | PersonalDetailPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | PersonalDetailPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | PersonalDetailPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 25 | PersonalDetailPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 26 | PersonalDetailPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 27 | PersonalDetailPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 28 | PersonalDetailPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 29 | PersonalDetailPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 30 | PersonalDetailPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 31 | PersonalDetailPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 32 | PersonalDetailPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 33 | PersonalDetailPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 34 | PersonalDetailPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 35 | PersonalDetailPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 36 | PersonalDetailPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 37 | PersonalDetailPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 38 | PersonalDetailPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 39 | PersonalDetailPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 40 | PersonalDetailPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 41 | PersonalDetailPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 42 | PersonalDetailPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 43 | PersonalDetailPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 44 | PersonalDetailPEOAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 45 | PersonalDetailPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 46 | PersonalDetailPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 47 | PersonalDetailPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 48 | PersonalDetailPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 49 | PersonalDetailPEOAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 50 | PersonalDetailPEOAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 51 | PersonalDetailPEOAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 52 | PersonalDetailPEOAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 53 | PersonalDetailPEOCitizenshipStatusCode | CITIZENSHIP_STATUS_CODE | — | ✅ |
| 54 | PersonalDetailPEOCountryOfBirthCode | COUNTRY_OF_BIRTH_CODE | — | ✅ |
| 55 | PersonalDetailPEOCountryOfResidenceCode | COUNTRY_OF_RESIDENCE_CODE | — | ✅ |
| 56 | PersonalDetailPEOCreatedBy | CREATED_BY | — | — |
| 57 | PersonalDetailPEOCreationDate | CREATION_DATE | — | — |
| 58 | PersonalDetailPEODeathCertificateNumber | DEATH_CERTIFICATE_NUMBER | — | ✅ |
| 59 | PersonalDetailPEOGenderIdentityCode | GENDER_IDENTITY_CODE | — | ✅ |
| 60 | PersonalDetailPEOGenderIdentityValue | GENDER_IDENTITY_VALUE | — | ✅ |
| 61 | PersonalDetailPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 62 | PersonalDetailPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 63 | PersonalDetailPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 64 | PersonalDetailPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 65 | PersonalDetailPEOPartyId | PARTY_ID | — | — |
| 66 | PersonalDetailPEOPlaceOfDeath | PLACE_OF_DEATH | — | ✅ |
| 67 | PersonalDetailPEOPreferredPronounsCode | PREFERRED_PRONOUNS_CODE | — | ✅ |
| 68 | PersonalDetailPEOPreferredPronounsValue | PREFERRED_PRONOUNS_VALUE | — | ✅ |
| 69 | PersonalDetailPEOPrimaryLanguageCode | PRIMARY_LANGUAGE_CODE | — | ✅ |
| 70 | PersonalDetailPEOPrimaryLanguageValue | PRIMARY_LANGUAGE_VALUE | — | ✅ |
| 71 | PersonalDetailPEOPrivacyFlag | PRIVACY_FLAG | — | ✅ |
| 72 | PersonalDetailPEORaceCode | RACE_CODE | — | ✅ |
| 73 | PersonalDetailPEOVisaTypeCode | VISA_TYPE_CODE | — | ✅ |

### [[hz_addtnl_party_names|HZ_ADDTNL_PARTY_NAMES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdditionalPartyNamePEOActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | AdditionalPartyNamePEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | AdditionalPartyNamePEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | AdditionalPartyNamePEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | AdditionalPartyNamePEOAttribute12 | ATTRIBUTE12 | — | — |
| 6 | AdditionalPartyNamePEOAttribute13 | ATTRIBUTE13 | — | — |
| 7 | AdditionalPartyNamePEOAttribute14 | ATTRIBUTE14 | — | — |
| 8 | AdditionalPartyNamePEOAttribute15 | ATTRIBUTE15 | — | — |
| 9 | AdditionalPartyNamePEOAttribute16 | ATTRIBUTE16 | — | — |
| 10 | AdditionalPartyNamePEOAttribute17 | ATTRIBUTE17 | — | — |
| 11 | AdditionalPartyNamePEOAttribute18 | ATTRIBUTE18 | — | — |
| 12 | AdditionalPartyNamePEOAttribute19 | ATTRIBUTE19 | — | — |
| 13 | AdditionalPartyNamePEOAttribute2 | ATTRIBUTE2 | — | — |
| 14 | AdditionalPartyNamePEOAttribute20 | ATTRIBUTE20 | — | — |
| 15 | AdditionalPartyNamePEOAttribute21 | ATTRIBUTE21 | — | — |
| 16 | AdditionalPartyNamePEOAttribute22 | ATTRIBUTE22 | — | — |
| 17 | AdditionalPartyNamePEOAttribute23 | ATTRIBUTE23 | — | — |
| 18 | AdditionalPartyNamePEOAttribute24 | ATTRIBUTE24 | — | — |
| 19 | AdditionalPartyNamePEOAttribute25 | ATTRIBUTE25 | — | — |
| 20 | AdditionalPartyNamePEOAttribute26 | ATTRIBUTE26 | — | — |
| 21 | AdditionalPartyNamePEOAttribute27 | ATTRIBUTE27 | — | — |
| 22 | AdditionalPartyNamePEOAttribute28 | ATTRIBUTE28 | — | — |
| 23 | AdditionalPartyNamePEOAttribute29 | ATTRIBUTE29 | — | — |
| 24 | AdditionalPartyNamePEOAttribute3 | ATTRIBUTE3 | — | — |
| 25 | AdditionalPartyNamePEOAttribute30 | ATTRIBUTE30 | — | — |
| 26 | AdditionalPartyNamePEOAttribute4 | ATTRIBUTE4 | — | — |
| 27 | AdditionalPartyNamePEOAttribute5 | ATTRIBUTE5 | — | — |
| 28 | AdditionalPartyNamePEOAttribute6 | ATTRIBUTE6 | — | — |
| 29 | AdditionalPartyNamePEOAttribute7 | ATTRIBUTE7 | — | — |
| 30 | AdditionalPartyNamePEOAttribute8 | ATTRIBUTE8 | — | — |
| 31 | AdditionalPartyNamePEOAttribute9 | ATTRIBUTE9 | — | — |
| 32 | AdditionalPartyNamePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 33 | AdditionalPartyNamePEOCreatedBy | CREATED_BY | — | — |
| 34 | AdditionalPartyNamePEOCreatedByModule | CREATED_BY_MODULE | — | — |
| 35 | AdditionalPartyNamePEOCreationDate | CREATION_DATE | — | — |
| 36 | AdditionalPartyNamePEODescription | DESCRIPTION | — | — |
| 37 | AdditionalPartyNamePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 38 | AdditionalPartyNamePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 39 | AdditionalPartyNamePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 40 | AdditionalPartyNamePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 41 | AdditionalPartyNamePEOPartyId | PARTY_ID | — | — |
| 42 | AdditionalPartyNamePEOPartyName | PARTY_NAME | — | ✅ |
| 43 | AdditionalPartyNamePEOPartyNameId | PARTY_NAME_ID | — | — |
| 44 | AdditionalPartyNamePEOPartyNameType | PARTY_NAME_TYPE | — | — |
| 45 | AdditionalPartyNamePEOPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 46 | AdditionalPartyNamePEOPersonFirstName | PERSON_FIRST_NAME | — | ✅ |
| 47 | AdditionalPartyNamePEOPersonLastName | PERSON_LAST_NAME | — | ✅ |
| 48 | AdditionalPartyNamePEOPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | ✅ |
| 49 | AdditionalPartyNamePEOPersonMiddleName | PERSON_MIDDLE_NAME | — | ✅ |
| 50 | AdditionalPartyNamePEOPersonNameSuffix | PERSON_NAME_SUFFIX | — | ✅ |
| 51 | AdditionalPartyNamePEOPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | ✅ |
| 52 | AdditionalPartyNamePEOPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 53 | AdditionalPartyNamePEOPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 54 | AdditionalPartyNamePEOPersonTitle | PERSON_TITLE | — | ✅ |
| 55 | AdditionalPartyNamePEOPreferredFlag | PREFERRED_FLAG | — | — |
| 56 | AdditionalPartyNamePEOStatusFlag | STATUS_FLAG | — | — |
| 57 | AdditionalPartyNamePEOTransliterationLang | TRANSLITERATION_LANG | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyPEOAddress1 | ADDRESS1 | — | — |
| 2 | PartyPEOAddress2 | ADDRESS2 | — | — |
| 3 | PartyPEOAddress3 | ADDRESS3 | — | — |
| 4 | PartyPEOAddress4 | ADDRESS4 | — | — |
| 5 | PartyPEOAnalysisFy | ANALYSIS_FY | — | — |
| 6 | PartyPEOAttribute1 | ATTRIBUTE1 | — | — |
| 7 | PartyPEOAttribute10 | ATTRIBUTE10 | — | — |
| 8 | PartyPEOAttribute11 | ATTRIBUTE11 | — | — |
| 9 | PartyPEOAttribute12 | ATTRIBUTE12 | — | — |
| 10 | PartyPEOAttribute13 | ATTRIBUTE13 | — | — |
| 11 | PartyPEOAttribute14 | ATTRIBUTE14 | — | — |
| 12 | PartyPEOAttribute15 | ATTRIBUTE15 | — | — |
| 13 | PartyPEOAttribute16 | ATTRIBUTE16 | — | — |
| 14 | PartyPEOAttribute17 | ATTRIBUTE17 | — | — |
| 15 | PartyPEOAttribute18 | ATTRIBUTE18 | — | — |
| 16 | PartyPEOAttribute19 | ATTRIBUTE19 | — | — |
| 17 | PartyPEOAttribute2 | ATTRIBUTE2 | — | — |
| 18 | PartyPEOAttribute20 | ATTRIBUTE20 | — | — |
| 19 | PartyPEOAttribute21 | ATTRIBUTE21 | — | — |
| 20 | PartyPEOAttribute22 | ATTRIBUTE22 | — | — |
| 21 | PartyPEOAttribute23 | ATTRIBUTE23 | — | — |
| 22 | PartyPEOAttribute24 | ATTRIBUTE24 | — | — |
| 23 | PartyPEOAttribute25 | ATTRIBUTE25 | — | — |
| 24 | PartyPEOAttribute26 | ATTRIBUTE26 | — | — |
| 25 | PartyPEOAttribute27 | ATTRIBUTE27 | — | — |
| 26 | PartyPEOAttribute28 | ATTRIBUTE28 | — | — |
| 27 | PartyPEOAttribute29 | ATTRIBUTE29 | — | — |
| 28 | PartyPEOAttribute3 | ATTRIBUTE3 | — | — |
| 29 | PartyPEOAttribute30 | ATTRIBUTE30 | — | — |
| 30 | PartyPEOAttribute4 | ATTRIBUTE4 | — | — |
| 31 | PartyPEOAttribute5 | ATTRIBUTE5 | — | — |
| 32 | PartyPEOAttribute6 | ATTRIBUTE6 | — | — |
| 33 | PartyPEOAttribute7 | ATTRIBUTE7 | — | — |
| 34 | PartyPEOAttribute8 | ATTRIBUTE8 | — | — |
| 35 | PartyPEOAttribute9 | ATTRIBUTE9 | — | — |
| 36 | PartyPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 37 | PartyPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 38 | PartyPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 39 | PartyPEOAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 40 | PartyPEOAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 41 | PartyPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 42 | PartyPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 43 | PartyPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 44 | PartyPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 45 | PartyPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 46 | PartyPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 47 | PartyPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 48 | PartyPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 49 | PartyPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 50 | PartyPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 51 | PartyPEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 52 | PartyPEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 53 | PartyPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 54 | PartyPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 55 | PartyPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 56 | PartyPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 57 | PartyPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 58 | PartyPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 59 | PartyPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 60 | PartyPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 61 | PartyPEOCategoryCode | CATEGORY_CODE | — | — |
| 62 | PartyPEOCeoName | CEO_NAME | — | — |
| 63 | PartyPEOCertReasonCode | CERT_REASON_CODE | — | — |
| 64 | PartyPEOCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 65 | PartyPEOCity | CITY | — | — |
| 66 | PartyPEOComments | COMMENTS | — | — |
| 67 | PartyPEOCountry | COUNTRY | — | — |
| 68 | PartyPEOCounty | COUNTY | — | — |
| 69 | PartyPEOCreatedBy | CREATED_BY | — | — |
| 70 | PartyPEOCreatedByModule | CREATED_BY_MODULE | — | — |
| 71 | PartyPEOCreationDate | CREATION_DATE | — | — |
| 72 | PartyPEOCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | — |
| 73 | PartyPEODateOfBirth | DATE_OF_BIRTH | — | ✅ |
| 74 | PartyPEODunsNumberC | DUNS_NUMBER_C | — | — |
| 75 | PartyPEOEmailAddress | EMAIL_ADDRESS | — | — |
| 76 | PartyPEOEmployeesTotal | EMPLOYEES_TOTAL | — | — |
| 77 | PartyPEOFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | — |
| 78 | PartyPEOGender | GENDER | — | ✅ |
| 79 | PartyPEOGroupType | GROUP_TYPE | — | — |
| 80 | PartyPEOGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | — |
| 81 | PartyPEOHomeCountry | HOME_COUNTRY | — | — |
| 82 | PartyPEOHqBranchInd | HQ_BRANCH_IND | — | — |
| 83 | PartyPEOIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 84 | PartyPEOIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | — |
| 85 | PartyPEOInternalFlag | INTERNAL_FLAG | — | — |
| 86 | PartyPEOJgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 87 | PartyPEOLanguageName | LANGUAGE_NAME | — | — |
| 88 | PartyPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 89 | PartyPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 90 | PartyPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 91 | PartyPEOMaritalStatus | MARITAL_STATUS | — | ✅ |
| 92 | PartyPEOMissionStatement | MISSION_STATEMENT | — | — |
| 93 | PartyPEONextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | — |
| 94 | PartyPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 95 | PartyPEOOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 96 | PartyPEOPartyId | PARTY_ID | 🔑 | ✅ |
| 97 | PartyPEOPartyName | PARTY_NAME | — | — |
| 98 | PartyPEOPartyNumber | PARTY_NUMBER | — | — |
| 99 | PartyPEOPartyType | PARTY_TYPE | — | — |
| 100 | PartyPEOPartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 101 | PartyPEOPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 102 | PartyPEOPersonFirstName | PERSON_FIRST_NAME | — | — |
| 103 | PartyPEOPersonLastName | PERSON_LAST_NAME | — | — |
| 104 | PartyPEOPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 105 | PartyPEOPersonMiddleName | PERSON_MIDDLE_NAME | — | — |
| 106 | PartyPEOPersonNameSuffix | PERSON_NAME_SUFFIX | — | — |
| 107 | PartyPEOPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 108 | PartyPEOPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 109 | PartyPEOPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 110 | PartyPEOPersonTitle | PERSON_TITLE | — | — |
| 111 | PartyPEOPersonalAddressFlag | PERSONAL_ADDRESS_FLAG | — | — |
| 112 | PartyPEOPersonalEmailFlag | PERSONAL_EMAIL_FLAG | — | — |
| 113 | PartyPEOPersonalPhoneFlag | PERSONAL_PHONE_FLAG | — | — |
| 114 | PartyPEOPostalCode | POSTAL_CODE | — | — |
| 115 | PartyPEOPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 116 | PartyPEOPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 117 | PartyPEOPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 118 | PartyPEOPreferredName | PREFERRED_NAME | — | — |
| 119 | PartyPEOPreferredNameId | PREFERRED_NAME_ID | — | — |
| 120 | PartyPEOPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | — |
| 121 | PartyPEOPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | — |
| 122 | PartyPEOPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | — |
| 123 | PartyPEOPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | — |
| 124 | PartyPEOPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | — |
| 125 | PartyPEOPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | — |
| 126 | PartyPEOPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | — |
| 127 | PartyPEOPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | — |
| 128 | PartyPEOPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | — |
| 129 | PartyPEOProvince | PROVINCE | — | — |
| 130 | PartyPEOSalutation | SALUTATION | — | — |
| 131 | PartyPEOSicCode | SIC_CODE | — | — |
| 132 | PartyPEOSicCodeType | SIC_CODE_TYPE | — | — |
| 133 | PartyPEOState | STATE | — | — |
| 134 | PartyPEOStatus | STATUS | — | — |
| 135 | PartyPEOThirdPartyFlag | THIRD_PARTY_FLAG | — | — |
| 136 | PartyPEOTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | — |
| 137 | PartyPEOUrl | URL | — | — |
| 138 | PartyPEOUserGuid | USER_GUID | — | — |
| 139 | PartyPEOValidatedFlag | VALIDATED_FLAG | — | — |
| 140 | PartyPEOYearEstablished | YEAR_ESTABLISHED | — | — |

### [[hz_person_profiles|HZ_PERSON_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonPEOActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | PersonPEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | PersonPEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | PersonPEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | PersonPEOAttribute12 | ATTRIBUTE12 | — | — |
| 6 | PersonPEOAttribute13 | ATTRIBUTE13 | — | — |
| 7 | PersonPEOAttribute14 | ATTRIBUTE14 | — | — |
| 8 | PersonPEOAttribute15 | ATTRIBUTE15 | — | — |
| 9 | PersonPEOAttribute16 | ATTRIBUTE16 | — | — |
| 10 | PersonPEOAttribute17 | ATTRIBUTE17 | — | — |
| 11 | PersonPEOAttribute18 | ATTRIBUTE18 | — | — |
| 12 | PersonPEOAttribute19 | ATTRIBUTE19 | — | — |
| 13 | PersonPEOAttribute2 | ATTRIBUTE2 | — | — |
| 14 | PersonPEOAttribute20 | ATTRIBUTE20 | — | — |
| 15 | PersonPEOAttribute21 | ATTRIBUTE21 | — | — |
| 16 | PersonPEOAttribute22 | ATTRIBUTE22 | — | — |
| 17 | PersonPEOAttribute23 | ATTRIBUTE23 | — | — |
| 18 | PersonPEOAttribute24 | ATTRIBUTE24 | — | — |
| 19 | PersonPEOAttribute25 | ATTRIBUTE25 | — | — |
| 20 | PersonPEOAttribute26 | ATTRIBUTE26 | — | — |
| 21 | PersonPEOAttribute27 | ATTRIBUTE27 | — | — |
| 22 | PersonPEOAttribute28 | ATTRIBUTE28 | — | — |
| 23 | PersonPEOAttribute29 | ATTRIBUTE29 | — | — |
| 24 | PersonPEOAttribute3 | ATTRIBUTE3 | — | — |
| 25 | PersonPEOAttribute30 | ATTRIBUTE30 | — | — |
| 26 | PersonPEOAttribute4 | ATTRIBUTE4 | — | — |
| 27 | PersonPEOAttribute5 | ATTRIBUTE5 | — | — |
| 28 | PersonPEOAttribute6 | ATTRIBUTE6 | — | — |
| 29 | PersonPEOAttribute7 | ATTRIBUTE7 | — | — |
| 30 | PersonPEOAttribute8 | ATTRIBUTE8 | — | — |
| 31 | PersonPEOAttribute9 | ATTRIBUTE9 | — | — |
| 32 | PersonPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 33 | PersonPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 34 | PersonPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 35 | PersonPEOAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 36 | PersonPEOAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 37 | PersonPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 38 | PersonPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 39 | PersonPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 40 | PersonPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 41 | PersonPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 42 | PersonPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 43 | PersonPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 44 | PersonPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 45 | PersonPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 46 | PersonPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 47 | PersonPEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 48 | PersonPEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 49 | PersonPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 50 | PersonPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 51 | PersonPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 52 | PersonPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 53 | PersonPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 54 | PersonPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 55 | PersonPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 56 | PersonPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 57 | PersonPEOCertReasonCode | CERT_REASON_CODE | — | — |
| 58 | PersonPEOCertificationLevel | CERTIFICATION_LEVEL | — | — |
| 59 | PersonPEOCleanlinessScore | CLEANLINESS_SCORE | — | — |
| 60 | PersonPEOComments | COMMENTS | — | — |
| 61 | PersonPEOCompletenessScore | COMPLETENESS_SCORE | — | — |
| 62 | PersonPEOContactRole | CONTACT_ROLE | — | — |
| 63 | PersonPEOCorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 64 | PersonPEOCreatedBy | CREATED_BY | — | — |
| 65 | PersonPEOCreatedByModule | CREATED_BY_MODULE | — | — |
| 66 | PersonPEOCreationDate | CREATION_DATE | — | — |
| 67 | PersonPEOCurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 68 | PersonPEOCurrencyCode | CURRENCY_CODE | — | — |
| 69 | PersonPEODataCloudStatus | DATA_CLOUD_STATUS | — | — |
| 70 | PersonPEODataConfidenceScore | DATA_CONFIDENCE_SCORE | — | — |
| 71 | PersonPEODateOfBirth | DATE_OF_BIRTH | — | — |
| 72 | PersonPEODateOfDeath | DATE_OF_DEATH | — | ✅ |
| 73 | PersonPEODeceasedFlag | DECEASED_FLAG | — | ✅ |
| 74 | PersonPEODeclaredEthnicity | DECLARED_ETHNICITY | — | ✅ |
| 75 | PersonPEODepartment | DEPARTMENT | — | — |
| 76 | PersonPEODepartmentCode | DEPARTMENT_CODE | — | — |
| 77 | PersonPEODoNotCallFlag | DO_NOT_CALL_FLAG | — | — |
| 78 | PersonPEODoNotContactFlag | DO_NOT_CONTACT_FLAG | — | — |
| 79 | PersonPEODoNotEmailFlag | DO_NOT_EMAIL_FLAG | — | — |
| 80 | PersonPEODoNotMailFlag | DO_NOT_MAIL_FLAG | — | — |
| 81 | PersonPEODuplicateIndicator | DUPLICATE_INDICATOR | — | — |
| 82 | PersonPEODuplicateScore | DUPLICATE_SCORE | — | — |
| 83 | PersonPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 84 | PersonPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 85 | PersonPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 86 | PersonPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 87 | PersonPEOEnrichmentScore | ENRICHMENT_SCORE | — | — |
| 88 | PersonPEOGender | GENDER | — | — |
| 89 | PersonPEOHeadOfHouseholdFlag | HEAD_OF_HOUSEHOLD_FLAG | — | — |
| 90 | PersonPEOHouseholdIncome | HOUSEHOLD_INCOME | — | — |
| 91 | PersonPEOHouseholdSize | HOUSEHOLD_SIZE | — | — |
| 92 | PersonPEOInternalFlag | INTERNAL_FLAG | — | — |
| 93 | PersonPEOJgzzFiscalCode | JGZZ_FISCAL_CODE | — | — |
| 94 | PersonPEOJobTitle | JOB_TITLE | — | — |
| 95 | PersonPEOJobTitleCode | JOB_TITLE_CODE | — | — |
| 96 | PersonPEOLastAssignedDate | LAST_ASSIGNED_DATE | — | — |
| 97 | PersonPEOLastContactDate | LAST_CONTACT_DATE | — | — |
| 98 | PersonPEOLastEnrichmentDate | LAST_ENRICHMENT_DATE | — | — |
| 99 | PersonPEOLastKnownGps | LAST_KNOWN_GPS | — | — |
| 100 | PersonPEOLastScoreUpdateDate | LAST_SCORE_UPDATE_DATE | — | — |
| 101 | PersonPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 102 | PersonPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 103 | PersonPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 104 | PersonPEOMaritalStatus | MARITAL_STATUS | — | — |
| 105 | PersonPEOMaritalStatusEffectiveDate | MARITAL_STATUS_EFFECTIVE_DATE | — | — |
| 106 | PersonPEONamedFlag | NAMED_FLAG | — | — |
| 107 | PersonPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 108 | PersonPEOOwnerPartyId | OWNER_PARTY_ID | — | — |
| 109 | PersonPEOPartyId | PARTY_ID | — | — |
| 110 | PersonPEOPartyNumber | PARTY_NUMBER | — | — |
| 111 | PersonPEOPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | — |
| 112 | PersonPEOPersonFirstName | PERSON_FIRST_NAME | — | ✅ |
| 113 | PersonPEOPersonInitials | PERSON_INITIALS | — | — |
| 114 | PersonPEOPersonLastName | PERSON_LAST_NAME | — | ✅ |
| 115 | PersonPEOPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | — |
| 116 | PersonPEOPersonMiddleName | PERSON_MIDDLE_NAME | — | ✅ |
| 117 | PersonPEOPersonName | PERSON_NAME | — | ✅ |
| 118 | PersonPEOPersonNameSuffix | PERSON_NAME_SUFFIX | — | ✅ |
| 119 | PersonPEOPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | — |
| 120 | PersonPEOPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | — |
| 121 | PersonPEOPersonProfileId | PERSON_PROFILE_ID | — | — |
| 122 | PersonPEOPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | — |
| 123 | PersonPEOPersonTitle | PERSON_TITLE | — | ✅ |
| 124 | PersonPEOPersonalIncome | PERSONAL_INCOME | — | — |
| 125 | PersonPEOPlaceOfBirth | PLACE_OF_BIRTH | — | ✅ |
| 126 | PersonPEOPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | — |
| 127 | PersonPEOPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | — |
| 128 | PersonPEOPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | — |
| 129 | PersonPEOPrimaryCustomerId | PRIMARY_CUSTOMER_ID | — | — |
| 130 | PersonPEOPrimaryCustomerRelationshipId | PRIMARY_CUST_RELATIONSHIP_ID | — | — |
| 131 | PersonPEORecencyScore | RECENCY_SCORE | — | — |
| 132 | PersonPEORegistrationStatus | REGISTRATION_STATUS | — | — |
| 133 | PersonPEORentOwnInd | RENT_OWN_IND | — | — |
| 134 | PersonPEOSalesAffinityCode | SALES_AFFINITY_CODE | — | — |
| 135 | PersonPEOSalesBuyingRoleCode | SALES_BUYING_ROLE_CODE | — | — |
| 136 | PersonPEOSalesProfileStatus | SALES_PROFILE_STATUS | — | — |
| 137 | PersonPEOSalesProfileType | SALES_PROFILE_TYPE | — | — |
| 138 | PersonPEOSalutation | SALUTATION | — | — |
| 139 | PersonPEOStatus | STATUS | — | — |
| 140 | PersonPEOSuffixOverriddenFlag | SUFFIX_OVERRIDDEN_FLAG | — | — |
| 141 | PersonPEOUniqueNameSuffix | UNIQUE_NAME_SUFFIX | — | — |
| 142 | PersonPEOValidityScore | VALIDITY_SCORE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
