---
id: DOC-PO-PVO-AssessmentPVO
doc_type: system-doc
title: "AssessmentPVO — PVO Purchasing"
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
  - AssessmentPVO
  - assessmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssessmentPVO

## 📌 Visão Geral

Extrai as avaliações (assessments) de fornecedores com critérios de pontuação, avaliador, data e vínculo com iniciativas. Permite gestão de desempenho de fornecedores e decisões baseadas em qualidade e risco.

**Caminho:** `FscmTopModelAM.PrcPoqPublicViewAM.AssessmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 565 | 4 | 1 | 562 | 99% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 137 atributos (137 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 252 atributos (252 BICC)
- [[poq_assessments|POQ_ASSESSMENTS]] — 97 atributos (1 PKs, 94 BICC)
- [[poq_initiatives|POQ_INITIATIVES]] — 79 atributos (79 BICC)

---

## ⚙️ Atributos

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssessSuppContPartyAddress1 | ADDRESS1 | — | ✅ |
| 2 | AssessSuppContPartyAddress2 | ADDRESS2 | — | ✅ |
| 3 | AssessSuppContPartyAddress3 | ADDRESS3 | — | ✅ |
| 4 | AssessSuppContPartyAddress4 | ADDRESS4 | — | ✅ |
| 5 | AssessSuppContPartyAnalysisFy | ANALYSIS_FY | — | ✅ |
| 6 | AssessSuppContPartyAttribute1 | ATTRIBUTE1 | — | ✅ |
| 7 | AssessSuppContPartyAttribute10 | ATTRIBUTE10 | — | ✅ |
| 8 | AssessSuppContPartyAttribute11 | ATTRIBUTE11 | — | ✅ |
| 9 | AssessSuppContPartyAttribute12 | ATTRIBUTE12 | — | ✅ |
| 10 | AssessSuppContPartyAttribute13 | ATTRIBUTE13 | — | ✅ |
| 11 | AssessSuppContPartyAttribute14 | ATTRIBUTE14 | — | ✅ |
| 12 | AssessSuppContPartyAttribute15 | ATTRIBUTE15 | — | ✅ |
| 13 | AssessSuppContPartyAttribute16 | ATTRIBUTE16 | — | ✅ |
| 14 | AssessSuppContPartyAttribute17 | ATTRIBUTE17 | — | ✅ |
| 15 | AssessSuppContPartyAttribute18 | ATTRIBUTE18 | — | ✅ |
| 16 | AssessSuppContPartyAttribute19 | ATTRIBUTE19 | — | ✅ |
| 17 | AssessSuppContPartyAttribute2 | ATTRIBUTE2 | — | ✅ |
| 18 | AssessSuppContPartyAttribute20 | ATTRIBUTE20 | — | ✅ |
| 19 | AssessSuppContPartyAttribute21 | ATTRIBUTE21 | — | ✅ |
| 20 | AssessSuppContPartyAttribute22 | ATTRIBUTE22 | — | ✅ |
| 21 | AssessSuppContPartyAttribute23 | ATTRIBUTE23 | — | ✅ |
| 22 | AssessSuppContPartyAttribute24 | ATTRIBUTE24 | — | ✅ |
| 23 | AssessSuppContPartyAttribute25 | ATTRIBUTE25 | — | ✅ |
| 24 | AssessSuppContPartyAttribute26 | ATTRIBUTE26 | — | ✅ |
| 25 | AssessSuppContPartyAttribute27 | ATTRIBUTE27 | — | ✅ |
| 26 | AssessSuppContPartyAttribute28 | ATTRIBUTE28 | — | ✅ |
| 27 | AssessSuppContPartyAttribute29 | ATTRIBUTE29 | — | ✅ |
| 28 | AssessSuppContPartyAttribute3 | ATTRIBUTE3 | — | ✅ |
| 29 | AssessSuppContPartyAttribute30 | ATTRIBUTE30 | — | ✅ |
| 30 | AssessSuppContPartyAttribute4 | ATTRIBUTE4 | — | ✅ |
| 31 | AssessSuppContPartyAttribute5 | ATTRIBUTE5 | — | ✅ |
| 32 | AssessSuppContPartyAttribute6 | ATTRIBUTE6 | — | ✅ |
| 33 | AssessSuppContPartyAttribute7 | ATTRIBUTE7 | — | ✅ |
| 34 | AssessSuppContPartyAttribute8 | ATTRIBUTE8 | — | ✅ |
| 35 | AssessSuppContPartyAttribute9 | ATTRIBUTE9 | — | ✅ |
| 36 | AssessSuppContPartyAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 37 | AssessSuppContPartyAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 38 | AssessSuppContPartyAttributeDate10 | ATTRIBUTE_DATE10 | — | ✅ |
| 39 | AssessSuppContPartyAttributeDate11 | ATTRIBUTE_DATE11 | — | ✅ |
| 40 | AssessSuppContPartyAttributeDate12 | ATTRIBUTE_DATE12 | — | ✅ |
| 41 | AssessSuppContPartyAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 42 | AssessSuppContPartyAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 43 | AssessSuppContPartyAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 44 | AssessSuppContPartyAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 45 | AssessSuppContPartyAttributeDate6 | ATTRIBUTE_DATE6 | — | ✅ |
| 46 | AssessSuppContPartyAttributeDate7 | ATTRIBUTE_DATE7 | — | ✅ |
| 47 | AssessSuppContPartyAttributeDate8 | ATTRIBUTE_DATE8 | — | ✅ |
| 48 | AssessSuppContPartyAttributeDate9 | ATTRIBUTE_DATE9 | — | ✅ |
| 49 | AssessSuppContPartyAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 50 | AssessSuppContPartyAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 51 | AssessSuppContPartyAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | ✅ |
| 52 | AssessSuppContPartyAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | ✅ |
| 53 | AssessSuppContPartyAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 54 | AssessSuppContPartyAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 55 | AssessSuppContPartyAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 56 | AssessSuppContPartyAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 57 | AssessSuppContPartyAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 58 | AssessSuppContPartyAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 59 | AssessSuppContPartyAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 60 | AssessSuppContPartyAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 61 | AssessSuppContPartyCategoryCode | CATEGORY_CODE | — | ✅ |
| 62 | AssessSuppContPartyCeoName | CEO_NAME | — | ✅ |
| 63 | AssessSuppContPartyCertReasonCode | CERT_REASON_CODE | — | ✅ |
| 64 | AssessSuppContPartyCertificationLevel | CERTIFICATION_LEVEL | — | ✅ |
| 65 | AssessSuppContPartyCity | CITY | — | ✅ |
| 66 | AssessSuppContPartyComments | COMMENTS | — | ✅ |
| 67 | AssessSuppContPartyCountry | COUNTRY | — | ✅ |
| 68 | AssessSuppContPartyCounty | COUNTY | — | ✅ |
| 69 | AssessSuppContPartyCreatedBy | CREATED_BY | — | ✅ |
| 70 | AssessSuppContPartyCreatedByModule | CREATED_BY_MODULE | — | ✅ |
| 71 | AssessSuppContPartyCreationDate | CREATION_DATE | — | ✅ |
| 72 | AssessSuppContPartyCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | ✅ |
| 73 | AssessSuppContPartyDateOfBirth | DATE_OF_BIRTH | — | ✅ |
| 74 | AssessSuppContPartyDunsNumberC | DUNS_NUMBER_C | — | ✅ |
| 75 | AssessSuppContPartyEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 76 | AssessSuppContPartyEmployeesTotal | EMPLOYEES_TOTAL | — | ✅ |
| 77 | AssessSuppContPartyFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | ✅ |
| 78 | AssessSuppContPartyGender | GENDER | — | ✅ |
| 79 | AssessSuppContPartyGroupType | GROUP_TYPE | — | ✅ |
| 80 | AssessSuppContPartyGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | ✅ |
| 81 | AssessSuppContPartyHomeCountry | HOME_COUNTRY | — | ✅ |
| 82 | AssessSuppContPartyHqBranchInd | HQ_BRANCH_IND | — | ✅ |
| 83 | AssessSuppContPartyIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | ✅ |
| 84 | AssessSuppContPartyIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | ✅ |
| 85 | AssessSuppContPartyInternalFlag | INTERNAL_FLAG | — | ✅ |
| 86 | AssessSuppContPartyJgzzFiscalCode | JGZZ_FISCAL_CODE | — | ✅ |
| 87 | AssessSuppContPartyLanguageName | LANGUAGE_NAME | — | ✅ |
| 88 | AssessSuppContPartyLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 89 | AssessSuppContPartyLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 90 | AssessSuppContPartyLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 91 | AssessSuppContPartyMaritalStatus | MARITAL_STATUS | — | ✅ |
| 92 | AssessSuppContPartyMissionStatement | MISSION_STATEMENT | — | ✅ |
| 93 | AssessSuppContPartyNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | ✅ |
| 94 | AssessSuppContPartyObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 95 | AssessSuppContPartyOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | ✅ |
| 96 | AssessSuppContPartyPartyId | PARTY_ID | — | ✅ |
| 97 | AssessSuppContPartyPartyName | PARTY_NAME | — | ✅ |
| 98 | AssessSuppContPartyPartyNumber | PARTY_NUMBER | — | ✅ |
| 99 | AssessSuppContPartyPartyType | PARTY_TYPE | — | ✅ |
| 100 | AssessSuppContPartyPartyUniqueName | PARTY_UNIQUE_NAME | — | ✅ |
| 101 | AssessSuppContPartyPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | ✅ |
| 102 | AssessSuppContPartyPersonFirstName | PERSON_FIRST_NAME | — | ✅ |
| 103 | AssessSuppContPartyPersonLastName | PERSON_LAST_NAME | — | ✅ |
| 104 | AssessSuppContPartyPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | ✅ |
| 105 | AssessSuppContPartyPersonMiddleName | PERSON_MIDDLE_NAME | — | ✅ |
| 106 | AssessSuppContPartyPersonNameSuffix | PERSON_NAME_SUFFIX | — | ✅ |
| 107 | AssessSuppContPartyPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | ✅ |
| 108 | AssessSuppContPartyPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | ✅ |
| 109 | AssessSuppContPartyPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | ✅ |
| 110 | AssessSuppContPartyPersonTitle | PERSON_TITLE | — | ✅ |
| 111 | AssessSuppContPartyPostalCode | POSTAL_CODE | — | ✅ |
| 112 | AssessSuppContPartyPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | ✅ |
| 113 | AssessSuppContPartyPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | ✅ |
| 114 | AssessSuppContPartyPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | ✅ |
| 115 | AssessSuppContPartyPreferredName | PREFERRED_NAME | — | ✅ |
| 116 | AssessSuppContPartyPreferredNameId | PREFERRED_NAME_ID | — | ✅ |
| 117 | AssessSuppContPartyPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | ✅ |
| 118 | AssessSuppContPartyPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | ✅ |
| 119 | AssessSuppContPartyPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | ✅ |
| 120 | AssessSuppContPartyPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | ✅ |
| 121 | AssessSuppContPartyPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | ✅ |
| 122 | AssessSuppContPartyPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | ✅ |
| 123 | AssessSuppContPartyPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | ✅ |
| 124 | AssessSuppContPartyPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | ✅ |
| 125 | AssessSuppContPartyPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | ✅ |
| 126 | AssessSuppContPartyProvince | PROVINCE | — | ✅ |
| 127 | AssessSuppContPartySalutation | SALUTATION | — | ✅ |
| 128 | AssessSuppContPartySicCode | SIC_CODE | — | ✅ |
| 129 | AssessSuppContPartySicCodeType | SIC_CODE_TYPE | — | ✅ |
| 130 | AssessSuppContPartyState | STATE | — | ✅ |
| 131 | AssessSuppContPartyStatus | STATUS | — | ✅ |
| 132 | AssessSuppContPartyThirdPartyFlag | THIRD_PARTY_FLAG | — | ✅ |
| 133 | AssessSuppContPartyTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | ✅ |
| 134 | AssessSuppContPartyUrl | URL | — | ✅ |
| 135 | AssessSuppContPartyUserGuid | USER_GUID | — | ✅ |
| 136 | AssessSuppContPartyValidatedFlag | VALIDATED_FLAG | — | ✅ |
| 137 | AssessSuppContPartyYearEstablished | YEAR_ESTABLISHED | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssessCanceledByAttribute1 | ATTRIBUTE1 | — | ✅ |
| 2 | AssessCanceledByAttribute10 | ATTRIBUTE10 | — | ✅ |
| 3 | AssessCanceledByAttribute11 | ATTRIBUTE11 | — | ✅ |
| 4 | AssessCanceledByAttribute12 | ATTRIBUTE12 | — | ✅ |
| 5 | AssessCanceledByAttribute13 | ATTRIBUTE13 | — | ✅ |
| 6 | AssessCanceledByAttribute14 | ATTRIBUTE14 | — | ✅ |
| 7 | AssessCanceledByAttribute15 | ATTRIBUTE15 | — | ✅ |
| 8 | AssessCanceledByAttribute16 | ATTRIBUTE16 | — | ✅ |
| 9 | AssessCanceledByAttribute17 | ATTRIBUTE17 | — | ✅ |
| 10 | AssessCanceledByAttribute18 | ATTRIBUTE18 | — | ✅ |
| 11 | AssessCanceledByAttribute19 | ATTRIBUTE19 | — | ✅ |
| 12 | AssessCanceledByAttribute2 | ATTRIBUTE2 | — | ✅ |
| 13 | AssessCanceledByAttribute20 | ATTRIBUTE20 | — | ✅ |
| 14 | AssessCanceledByAttribute21 | ATTRIBUTE21 | — | ✅ |
| 15 | AssessCanceledByAttribute22 | ATTRIBUTE22 | — | ✅ |
| 16 | AssessCanceledByAttribute23 | ATTRIBUTE23 | — | ✅ |
| 17 | AssessCanceledByAttribute24 | ATTRIBUTE24 | — | ✅ |
| 18 | AssessCanceledByAttribute25 | ATTRIBUTE25 | — | ✅ |
| 19 | AssessCanceledByAttribute26 | ATTRIBUTE26 | — | ✅ |
| 20 | AssessCanceledByAttribute27 | ATTRIBUTE27 | — | ✅ |
| 21 | AssessCanceledByAttribute28 | ATTRIBUTE28 | — | ✅ |
| 22 | AssessCanceledByAttribute29 | ATTRIBUTE29 | — | ✅ |
| 23 | AssessCanceledByAttribute3 | ATTRIBUTE3 | — | ✅ |
| 24 | AssessCanceledByAttribute30 | ATTRIBUTE30 | — | ✅ |
| 25 | AssessCanceledByAttribute4 | ATTRIBUTE4 | — | ✅ |
| 26 | AssessCanceledByAttribute5 | ATTRIBUTE5 | — | ✅ |
| 27 | AssessCanceledByAttribute6 | ATTRIBUTE6 | — | ✅ |
| 28 | AssessCanceledByAttribute7 | ATTRIBUTE7 | — | ✅ |
| 29 | AssessCanceledByAttribute8 | ATTRIBUTE8 | — | ✅ |
| 30 | AssessCanceledByAttribute9 | ATTRIBUTE9 | — | ✅ |
| 31 | AssessCanceledByAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 32 | AssessCanceledByAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 33 | AssessCanceledByAttributeDate10 | ATTRIBUTE_DATE10 | — | ✅ |
| 34 | AssessCanceledByAttributeDate11 | ATTRIBUTE_DATE11 | — | ✅ |
| 35 | AssessCanceledByAttributeDate12 | ATTRIBUTE_DATE12 | — | ✅ |
| 36 | AssessCanceledByAttributeDate13 | ATTRIBUTE_DATE13 | — | ✅ |
| 37 | AssessCanceledByAttributeDate14 | ATTRIBUTE_DATE14 | — | ✅ |
| 38 | AssessCanceledByAttributeDate15 | ATTRIBUTE_DATE15 | — | ✅ |
| 39 | AssessCanceledByAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 40 | AssessCanceledByAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 41 | AssessCanceledByAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 42 | AssessCanceledByAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 43 | AssessCanceledByAttributeDate6 | ATTRIBUTE_DATE6 | — | ✅ |
| 44 | AssessCanceledByAttributeDate7 | ATTRIBUTE_DATE7 | — | ✅ |
| 45 | AssessCanceledByAttributeDate8 | ATTRIBUTE_DATE8 | — | ✅ |
| 46 | AssessCanceledByAttributeDate9 | ATTRIBUTE_DATE9 | — | ✅ |
| 47 | AssessCanceledByAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 48 | AssessCanceledByAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 49 | AssessCanceledByAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | ✅ |
| 50 | AssessCanceledByAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | ✅ |
| 51 | AssessCanceledByAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | ✅ |
| 52 | AssessCanceledByAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | ✅ |
| 53 | AssessCanceledByAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | ✅ |
| 54 | AssessCanceledByAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | ✅ |
| 55 | AssessCanceledByAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | ✅ |
| 56 | AssessCanceledByAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | ✅ |
| 57 | AssessCanceledByAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | ✅ |
| 58 | AssessCanceledByAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 59 | AssessCanceledByAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | ✅ |
| 60 | AssessCanceledByAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 61 | AssessCanceledByAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 62 | AssessCanceledByAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 63 | AssessCanceledByAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 64 | AssessCanceledByAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 65 | AssessCanceledByAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 66 | AssessCanceledByAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 67 | AssessCanceledByBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 68 | AssessCanceledByCreatedBy | CREATED_BY | — | ✅ |
| 69 | AssessCanceledByCreationDate | CREATION_DATE | — | ✅ |
| 70 | AssessCanceledByDisplayName | DISPLAY_NAME | — | ✅ |
| 71 | AssessCanceledByEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 72 | AssessCanceledByEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 73 | AssessCanceledByFirstName | FIRST_NAME | — | ✅ |
| 74 | AssessCanceledByFullName | FULL_NAME | — | ✅ |
| 75 | AssessCanceledByHonors | HONORS | — | ✅ |
| 76 | AssessCanceledByKnownAs | KNOWN_AS | — | ✅ |
| 77 | AssessCanceledByLastName | LAST_NAME | — | ✅ |
| 78 | AssessCanceledByLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 79 | AssessCanceledByLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 80 | AssessCanceledByLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 81 | AssessCanceledByLegislationCode | LEGISLATION_CODE | — | ✅ |
| 82 | AssessCanceledByListName | LIST_NAME | — | ✅ |
| 83 | AssessCanceledByMiddleNames | MIDDLE_NAMES | — | ✅ |
| 84 | AssessCanceledByMilitaryRank | MILITARY_RANK | — | ✅ |
| 85 | AssessCanceledByNamInformation1 | NAM_INFORMATION1 | — | ✅ |
| 86 | AssessCanceledByNamInformation10 | NAM_INFORMATION10 | — | ✅ |
| 87 | AssessCanceledByNamInformation11 | NAM_INFORMATION11 | — | ✅ |
| 88 | AssessCanceledByNamInformation12 | NAM_INFORMATION12 | — | ✅ |
| 89 | AssessCanceledByNamInformation13 | NAM_INFORMATION13 | — | ✅ |
| 90 | AssessCanceledByNamInformation14 | NAM_INFORMATION14 | — | ✅ |
| 91 | AssessCanceledByNamInformation15 | NAM_INFORMATION15 | — | ✅ |
| 92 | AssessCanceledByNamInformation16 | NAM_INFORMATION16 | — | ✅ |
| 93 | AssessCanceledByNamInformation17 | NAM_INFORMATION17 | — | ✅ |
| 94 | AssessCanceledByNamInformation18 | NAM_INFORMATION18 | — | ✅ |
| 95 | AssessCanceledByNamInformation19 | NAM_INFORMATION19 | — | ✅ |
| 96 | AssessCanceledByNamInformation2 | NAM_INFORMATION2 | — | ✅ |
| 97 | AssessCanceledByNamInformation20 | NAM_INFORMATION20 | — | ✅ |
| 98 | AssessCanceledByNamInformation21 | NAM_INFORMATION21 | — | ✅ |
| 99 | AssessCanceledByNamInformation22 | NAM_INFORMATION22 | — | ✅ |
| 100 | AssessCanceledByNamInformation23 | NAM_INFORMATION23 | — | ✅ |
| 101 | AssessCanceledByNamInformation24 | NAM_INFORMATION24 | — | ✅ |
| 102 | AssessCanceledByNamInformation25 | NAM_INFORMATION25 | — | ✅ |
| 103 | AssessCanceledByNamInformation26 | NAM_INFORMATION26 | — | ✅ |
| 104 | AssessCanceledByNamInformation27 | NAM_INFORMATION27 | — | ✅ |
| 105 | AssessCanceledByNamInformation28 | NAM_INFORMATION28 | — | ✅ |
| 106 | AssessCanceledByNamInformation29 | NAM_INFORMATION29 | — | ✅ |
| 107 | AssessCanceledByNamInformation3 | NAM_INFORMATION3 | — | ✅ |
| 108 | AssessCanceledByNamInformation30 | NAM_INFORMATION30 | — | ✅ |
| 109 | AssessCanceledByNamInformation4 | NAM_INFORMATION4 | — | ✅ |
| 110 | AssessCanceledByNamInformation5 | NAM_INFORMATION5 | — | ✅ |
| 111 | AssessCanceledByNamInformation6 | NAM_INFORMATION6 | — | ✅ |
| 112 | AssessCanceledByNamInformation7 | NAM_INFORMATION7 | — | ✅ |
| 113 | AssessCanceledByNamInformation8 | NAM_INFORMATION8 | — | ✅ |
| 114 | AssessCanceledByNamInformation9 | NAM_INFORMATION9 | — | ✅ |
| 115 | AssessCanceledByNamInformationCategory | NAM_INFORMATION_CATEGORY | — | ✅ |
| 116 | AssessCanceledByNameType | NAME_TYPE | — | ✅ |
| 117 | AssessCanceledByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 118 | AssessCanceledByOrderName | ORDER_NAME | — | ✅ |
| 119 | AssessCanceledByPersonId | PERSON_ID | — | ✅ |
| 120 | AssessCanceledByPersonNameId | PERSON_NAME_ID | — | ✅ |
| 121 | AssessCanceledByPreNameAdjunct | PRE_NAME_ADJUNCT | — | ✅ |
| 122 | AssessCanceledByPreviousLastName | PREVIOUS_LAST_NAME | — | ✅ |
| 123 | AssessCanceledBySuffix | SUFFIX | — | ✅ |
| 124 | AssessCanceledByTitle | TITLE | — | ✅ |
| 125 | InitCanceledByAttribute1 | ATTRIBUTE1 | — | ✅ |
| 126 | InitCanceledByAttribute10 | ATTRIBUTE10 | — | ✅ |
| 127 | InitCanceledByAttribute11 | ATTRIBUTE11 | — | ✅ |
| 128 | InitCanceledByAttribute12 | ATTRIBUTE12 | — | ✅ |
| 129 | InitCanceledByAttribute13 | ATTRIBUTE13 | — | ✅ |
| 130 | InitCanceledByAttribute14 | ATTRIBUTE14 | — | ✅ |
| 131 | InitCanceledByAttribute15 | ATTRIBUTE15 | — | ✅ |
| 132 | InitCanceledByAttribute16 | ATTRIBUTE16 | — | ✅ |
| 133 | InitCanceledByAttribute17 | ATTRIBUTE17 | — | ✅ |
| 134 | InitCanceledByAttribute18 | ATTRIBUTE18 | — | ✅ |
| 135 | InitCanceledByAttribute19 | ATTRIBUTE19 | — | ✅ |
| 136 | InitCanceledByAttribute2 | ATTRIBUTE2 | — | ✅ |
| 137 | InitCanceledByAttribute20 | ATTRIBUTE20 | — | ✅ |
| 138 | InitCanceledByAttribute21 | ATTRIBUTE21 | — | ✅ |
| 139 | InitCanceledByAttribute22 | ATTRIBUTE22 | — | ✅ |
| 140 | InitCanceledByAttribute23 | ATTRIBUTE23 | — | ✅ |
| 141 | InitCanceledByAttribute24 | ATTRIBUTE24 | — | ✅ |
| 142 | InitCanceledByAttribute25 | ATTRIBUTE25 | — | ✅ |
| 143 | InitCanceledByAttribute26 | ATTRIBUTE26 | — | ✅ |
| 144 | InitCanceledByAttribute27 | ATTRIBUTE27 | — | ✅ |
| 145 | InitCanceledByAttribute28 | ATTRIBUTE28 | — | ✅ |
| 146 | InitCanceledByAttribute29 | ATTRIBUTE29 | — | ✅ |
| 147 | InitCanceledByAttribute3 | ATTRIBUTE3 | — | ✅ |
| 148 | InitCanceledByAttribute30 | ATTRIBUTE30 | — | ✅ |
| 149 | InitCanceledByAttribute4 | ATTRIBUTE4 | — | ✅ |
| 150 | InitCanceledByAttribute5 | ATTRIBUTE5 | — | ✅ |
| 151 | InitCanceledByAttribute6 | ATTRIBUTE6 | — | ✅ |
| 152 | InitCanceledByAttribute7 | ATTRIBUTE7 | — | ✅ |
| 153 | InitCanceledByAttribute8 | ATTRIBUTE8 | — | ✅ |
| 154 | InitCanceledByAttribute9 | ATTRIBUTE9 | — | ✅ |
| 155 | InitCanceledByAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 156 | InitCanceledByAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 157 | InitCanceledByAttributeDate10 | ATTRIBUTE_DATE10 | — | ✅ |
| 158 | InitCanceledByAttributeDate11 | ATTRIBUTE_DATE11 | — | ✅ |
| 159 | InitCanceledByAttributeDate12 | ATTRIBUTE_DATE12 | — | ✅ |
| 160 | InitCanceledByAttributeDate13 | ATTRIBUTE_DATE13 | — | ✅ |
| 161 | InitCanceledByAttributeDate14 | ATTRIBUTE_DATE14 | — | ✅ |
| 162 | InitCanceledByAttributeDate15 | ATTRIBUTE_DATE15 | — | ✅ |
| 163 | InitCanceledByAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 164 | InitCanceledByAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 165 | InitCanceledByAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 166 | InitCanceledByAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 167 | InitCanceledByAttributeDate6 | ATTRIBUTE_DATE6 | — | ✅ |
| 168 | InitCanceledByAttributeDate7 | ATTRIBUTE_DATE7 | — | ✅ |
| 169 | InitCanceledByAttributeDate8 | ATTRIBUTE_DATE8 | — | ✅ |
| 170 | InitCanceledByAttributeDate9 | ATTRIBUTE_DATE9 | — | ✅ |
| 171 | InitCanceledByAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 172 | InitCanceledByAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 173 | InitCanceledByAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | ✅ |
| 174 | InitCanceledByAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | ✅ |
| 175 | InitCanceledByAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | ✅ |
| 176 | InitCanceledByAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | ✅ |
| 177 | InitCanceledByAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | ✅ |
| 178 | InitCanceledByAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | ✅ |
| 179 | InitCanceledByAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | ✅ |
| 180 | InitCanceledByAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | ✅ |
| 181 | InitCanceledByAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | ✅ |
| 182 | InitCanceledByAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 183 | InitCanceledByAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | ✅ |
| 184 | InitCanceledByAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 185 | InitCanceledByAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 186 | InitCanceledByAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 187 | InitCanceledByAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 188 | InitCanceledByAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 189 | InitCanceledByAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 190 | InitCanceledByAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 191 | InitCanceledByBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 192 | InitCanceledByCreatedBy | CREATED_BY | — | ✅ |
| 193 | InitCanceledByCreationDate | CREATION_DATE | — | ✅ |
| 194 | InitCanceledByDisplayName | DISPLAY_NAME | — | ✅ |
| 195 | InitCanceledByEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 196 | InitCanceledByEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 197 | InitCanceledByFirstName | FIRST_NAME | — | ✅ |
| 198 | InitCanceledByFullName | FULL_NAME | — | ✅ |
| 199 | InitCanceledByHonors | HONORS | — | ✅ |
| 200 | InitCanceledByKnownAs | KNOWN_AS | — | ✅ |
| 201 | InitCanceledByLastName | LAST_NAME | — | ✅ |
| 202 | InitCanceledByLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 203 | InitCanceledByLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 204 | InitCanceledByLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 205 | InitCanceledByLegislationCode | LEGISLATION_CODE | — | ✅ |
| 206 | InitCanceledByListName | LIST_NAME | — | ✅ |
| 207 | InitCanceledByMiddleNames | MIDDLE_NAMES | — | ✅ |
| 208 | InitCanceledByMilitaryRank | MILITARY_RANK | — | ✅ |
| 209 | InitCanceledByNamInformation1 | NAM_INFORMATION1 | — | ✅ |
| 210 | InitCanceledByNamInformation10 | NAM_INFORMATION10 | — | ✅ |
| 211 | InitCanceledByNamInformation11 | NAM_INFORMATION11 | — | ✅ |
| 212 | InitCanceledByNamInformation12 | NAM_INFORMATION12 | — | ✅ |
| 213 | InitCanceledByNamInformation13 | NAM_INFORMATION13 | — | ✅ |
| 214 | InitCanceledByNamInformation14 | NAM_INFORMATION14 | — | ✅ |
| 215 | InitCanceledByNamInformation15 | NAM_INFORMATION15 | — | ✅ |
| 216 | InitCanceledByNamInformation16 | NAM_INFORMATION16 | — | ✅ |
| 217 | InitCanceledByNamInformation17 | NAM_INFORMATION17 | — | ✅ |
| 218 | InitCanceledByNamInformation18 | NAM_INFORMATION18 | — | ✅ |
| 219 | InitCanceledByNamInformation19 | NAM_INFORMATION19 | — | ✅ |
| 220 | InitCanceledByNamInformation2 | NAM_INFORMATION2 | — | ✅ |
| 221 | InitCanceledByNamInformation20 | NAM_INFORMATION20 | — | ✅ |
| 222 | InitCanceledByNamInformation21 | NAM_INFORMATION21 | — | ✅ |
| 223 | InitCanceledByNamInformation22 | NAM_INFORMATION22 | — | ✅ |
| 224 | InitCanceledByNamInformation23 | NAM_INFORMATION23 | — | ✅ |
| 225 | InitCanceledByNamInformation24 | NAM_INFORMATION24 | — | ✅ |
| 226 | InitCanceledByNamInformation25 | NAM_INFORMATION25 | — | ✅ |
| 227 | InitCanceledByNamInformation26 | NAM_INFORMATION26 | — | ✅ |
| 228 | InitCanceledByNamInformation27 | NAM_INFORMATION27 | — | ✅ |
| 229 | InitCanceledByNamInformation28 | NAM_INFORMATION28 | — | ✅ |
| 230 | InitCanceledByNamInformation29 | NAM_INFORMATION29 | — | ✅ |
| 231 | InitCanceledByNamInformation3 | NAM_INFORMATION3 | — | ✅ |
| 232 | InitCanceledByNamInformation30 | NAM_INFORMATION30 | — | ✅ |
| 233 | InitCanceledByNamInformation4 | NAM_INFORMATION4 | — | ✅ |
| 234 | InitCanceledByNamInformation5 | NAM_INFORMATION5 | — | ✅ |
| 235 | InitCanceledByNamInformation6 | NAM_INFORMATION6 | — | ✅ |
| 236 | InitCanceledByNamInformation7 | NAM_INFORMATION7 | — | ✅ |
| 237 | InitCanceledByNamInformation8 | NAM_INFORMATION8 | — | ✅ |
| 238 | InitCanceledByNamInformation9 | NAM_INFORMATION9 | — | ✅ |
| 239 | InitCanceledByNamInformationCategory | NAM_INFORMATION_CATEGORY | — | ✅ |
| 240 | InitCanceledByNameType | NAME_TYPE | — | ✅ |
| 241 | InitCanceledByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 242 | InitCanceledByOrderName | ORDER_NAME | — | ✅ |
| 243 | InitCanceledByPersonId | PERSON_ID | — | ✅ |
| 244 | InitCanceledByPersonNameId | PERSON_NAME_ID | — | ✅ |
| 245 | InitCanceledByPreNameAdjunct | PRE_NAME_ADJUNCT | — | ✅ |
| 246 | InitCanceledByPreviousLastName | PREVIOUS_LAST_NAME | — | ✅ |
| 247 | InitCanceledBySuffix | SUFFIX | — | ✅ |
| 248 | InitCanceledByTitle | TITLE | — | ✅ |
| 249 | OverridenByDisplayName | DISPLAY_NAME | — | ✅ |
| 250 | OverridenByEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 251 | OverridenByEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 252 | OverridenByPersonNameId | PERSON_NAME_ID | — | ✅ |

### [[poq_assessments|POQ_ASSESSMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssessmentAssessmentComments | ASSESSMENT_COMMENTS | — | ✅ |
| 2 | AssessmentAssessmentName | ASSESSMENT_NAME | — | ✅ |
| 3 | AssessmentAssessmentNumber | ASSESSMENT_NUMBER | — | ✅ |
| 4 | AssessmentAssessmentOutcome | ASSESSMENT_OUTCOME | — | ✅ |
| 5 | AssessmentAssessmentScore | ASSESSMENT_SCORE | — | ✅ |
| 6 | AssessmentAttribute1 | ATTRIBUTE1 | — | ✅ |
| 7 | AssessmentAttribute10 | ATTRIBUTE10 | — | ✅ |
| 8 | AssessmentAttribute11 | ATTRIBUTE11 | — | ✅ |
| 9 | AssessmentAttribute12 | ATTRIBUTE12 | — | ✅ |
| 10 | AssessmentAttribute13 | ATTRIBUTE13 | — | ✅ |
| 11 | AssessmentAttribute14 | ATTRIBUTE14 | — | ✅ |
| 12 | AssessmentAttribute15 | ATTRIBUTE15 | — | ✅ |
| 13 | AssessmentAttribute16 | ATTRIBUTE16 | — | ✅ |
| 14 | AssessmentAttribute17 | ATTRIBUTE17 | — | ✅ |
| 15 | AssessmentAttribute18 | ATTRIBUTE18 | — | ✅ |
| 16 | AssessmentAttribute19 | ATTRIBUTE19 | — | ✅ |
| 17 | AssessmentAttribute2 | ATTRIBUTE2 | — | ✅ |
| 18 | AssessmentAttribute20 | ATTRIBUTE20 | — | ✅ |
| 19 | AssessmentAttribute3 | ATTRIBUTE3 | — | ✅ |
| 20 | AssessmentAttribute4 | ATTRIBUTE4 | — | ✅ |
| 21 | AssessmentAttribute5 | ATTRIBUTE5 | — | ✅ |
| 22 | AssessmentAttribute6 | ATTRIBUTE6 | — | ✅ |
| 23 | AssessmentAttribute7 | ATTRIBUTE7 | — | ✅ |
| 24 | AssessmentAttribute8 | ATTRIBUTE8 | — | ✅ |
| 25 | AssessmentAttribute9 | ATTRIBUTE9 | — | ✅ |
| 26 | AssessmentAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 27 | AssessmentAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 28 | AssessmentAttributeDate10 | ATTRIBUTE_DATE10 | — | ✅ |
| 29 | AssessmentAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 30 | AssessmentAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 31 | AssessmentAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 32 | AssessmentAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 33 | AssessmentAttributeDate6 | ATTRIBUTE_DATE6 | — | ✅ |
| 34 | AssessmentAttributeDate7 | ATTRIBUTE_DATE7 | — | ✅ |
| 35 | AssessmentAttributeDate8 | ATTRIBUTE_DATE8 | — | ✅ |
| 36 | AssessmentAttributeDate9 | ATTRIBUTE_DATE9 | — | ✅ |
| 37 | AssessmentAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 38 | AssessmentAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 39 | AssessmentAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 40 | AssessmentAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 41 | AssessmentAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 42 | AssessmentAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 43 | AssessmentAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 44 | AssessmentAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 45 | AssessmentAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 46 | AssessmentAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 47 | AssessmentAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 48 | AssessmentAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | ✅ |
| 49 | AssessmentAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 50 | AssessmentAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 51 | AssessmentAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 52 | AssessmentAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 53 | AssessmentAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | ✅ |
| 54 | AssessmentAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | ✅ |
| 55 | AssessmentAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | ✅ |
| 56 | AssessmentAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | ✅ |
| 57 | AssessmentAutoEvaluatedFlag | AUTO_EVALUATED_FLAG | — | ✅ |
| 58 | AssessmentCanceledBy | CANCELED_BY | — | ✅ |
| 59 | AssessmentCanceledDate | CANCELED_DATE | — | ✅ |
| 60 | AssessmentCanceledReasonCode | CANCELED_REASON_CODE | — | ✅ |
| 61 | AssessmentCompletedDate | COMPLETED_DATE | — | ✅ |
| 62 | AssessmentCreatedBy | CREATED_BY | — | ✅ |
| 63 | AssessmentCreationDate | CREATION_DATE | — | ✅ |
| 64 | AssessmentCreationSource | CREATION_SOURCE | — | — |
| 65 | AssessmentEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 66 | AssessmentEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 67 | AssessmentEvalReadyDate | EVAL_READY_DATE | — | ✅ |
| 68 | AssessmentEvaluatedBy | EVALUATED_BY | — | — |
| 69 | AssessmentEvaluationDate | EVALUATION_DATE | — | ✅ |
| 70 | AssessmentEvaluationDueDate | EVALUATION_DUE_DATE | — | ✅ |
| 71 | AssessmentExpirationReminderPeriod | EXPIRATION_REMINDER_PERIOD | — | ✅ |
| 72 | AssessmentExpirationReminderType | EXPIRATION_REMINDER_TYPE | — | ✅ |
| 73 | AssessmentId | ASSESSMENT_ID | 🔑 | ✅ |
| 74 | AssessmentInitiativeId | INITIATIVE_ID | — | ✅ |
| 75 | AssessmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 76 | AssessmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 77 | AssessmentLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 78 | AssessmentLatestFlag | LATEST_FLAG | — | ✅ |
| 79 | AssessmentNoteToSupplier | NOTE_TO_SUPPLIER | — | ✅ |
| 80 | AssessmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 81 | AssessmentOrigAssessmentOutcome | ORIG_ASSESSMENT_OUTCOME | — | ✅ |
| 82 | AssessmentOrigAssessmentScore | ORIG_ASSESSMENT_SCORE | — | ✅ |
| 83 | AssessmentOverrideDate | OVERRIDE_DATE | — | ✅ |
| 84 | AssessmentOverrideReason | OVERRIDE_REASON | — | ✅ |
| 85 | AssessmentOverridenBy | OVERRIDEN_BY | — | ✅ |
| 86 | AssessmentOwnerId | OWNER_ID | — | ✅ |
| 87 | AssessmentPrcBuId | PRC_BU_ID | — | ✅ |
| 88 | AssessmentQualModelId | QUAL_MODEL_ID | — | ✅ |
| 89 | AssessmentSendIntQnnaireFlag | SEND_INT_QNNAIRE_FLAG | — | ✅ |
| 90 | AssessmentSendSuppQnnaireFlag | SEND_SUPP_QNNAIRE_FLAG | — | ✅ |
| 91 | AssessmentShowAssessmentQualFlag | SHOW_ASSESSMENT_QUAL_FLAG | — | ✅ |
| 92 | AssessmentShowAssessmtToSuppFlag | SHOW_ASSESSMT_TO_SUPP_FLAG | — | ✅ |
| 93 | AssessmentSourcingEligibilityCode | SOURCING_ELIGIBILITY_CODE | — | ✅ |
| 94 | AssessmentSuppContactPartyId | SUPP_CONTACT_PARTY_ID | — | ✅ |
| 95 | AssessmentSupplierId | SUPPLIER_ID | — | ✅ |
| 96 | AssessmentSupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 97 | ReassessQualificationFlag | REASSESS_QUALIFICATION_FLAG | — | — |

### [[poq_initiatives|POQ_INITIATIVES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InitiativeAssessmentEvalDueDate | ASSESSMENT_EVAL_DUE_DATE | — | ✅ |
| 2 | InitiativeAssessmentOwnerId | ASSESSMENT_OWNER_ID | — | ✅ |
| 3 | InitiativeAttribute1 | ATTRIBUTE1 | — | ✅ |
| 4 | InitiativeAttribute10 | ATTRIBUTE10 | — | ✅ |
| 5 | InitiativeAttribute11 | ATTRIBUTE11 | — | ✅ |
| 6 | InitiativeAttribute12 | ATTRIBUTE12 | — | ✅ |
| 7 | InitiativeAttribute13 | ATTRIBUTE13 | — | ✅ |
| 8 | InitiativeAttribute14 | ATTRIBUTE14 | — | ✅ |
| 9 | InitiativeAttribute15 | ATTRIBUTE15 | — | ✅ |
| 10 | InitiativeAttribute16 | ATTRIBUTE16 | — | ✅ |
| 11 | InitiativeAttribute17 | ATTRIBUTE17 | — | ✅ |
| 12 | InitiativeAttribute18 | ATTRIBUTE18 | — | ✅ |
| 13 | InitiativeAttribute19 | ATTRIBUTE19 | — | ✅ |
| 14 | InitiativeAttribute2 | ATTRIBUTE2 | — | ✅ |
| 15 | InitiativeAttribute20 | ATTRIBUTE20 | — | ✅ |
| 16 | InitiativeAttribute3 | ATTRIBUTE3 | — | ✅ |
| 17 | InitiativeAttribute4 | ATTRIBUTE4 | — | ✅ |
| 18 | InitiativeAttribute5 | ATTRIBUTE5 | — | ✅ |
| 19 | InitiativeAttribute6 | ATTRIBUTE6 | — | ✅ |
| 20 | InitiativeAttribute7 | ATTRIBUTE7 | — | ✅ |
| 21 | InitiativeAttribute8 | ATTRIBUTE8 | — | ✅ |
| 22 | InitiativeAttribute9 | ATTRIBUTE9 | — | ✅ |
| 23 | InitiativeAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 24 | InitiativeAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 25 | InitiativeAttributeDate10 | ATTRIBUTE_DATE10 | — | ✅ |
| 26 | InitiativeAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 27 | InitiativeAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 28 | InitiativeAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 29 | InitiativeAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 30 | InitiativeAttributeDate6 | ATTRIBUTE_DATE6 | — | ✅ |
| 31 | InitiativeAttributeDate7 | ATTRIBUTE_DATE7 | — | ✅ |
| 32 | InitiativeAttributeDate8 | ATTRIBUTE_DATE8 | — | ✅ |
| 33 | InitiativeAttributeDate9 | ATTRIBUTE_DATE9 | — | ✅ |
| 34 | InitiativeAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 35 | InitiativeAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 36 | InitiativeAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 37 | InitiativeAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 38 | InitiativeAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 39 | InitiativeAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 40 | InitiativeAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 41 | InitiativeAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 42 | InitiativeAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 43 | InitiativeAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 44 | InitiativeAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 45 | InitiativeAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | ✅ |
| 46 | InitiativeAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 47 | InitiativeAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 48 | InitiativeAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 49 | InitiativeAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 50 | InitiativeAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | ✅ |
| 51 | InitiativeAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | ✅ |
| 52 | InitiativeAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | ✅ |
| 53 | InitiativeAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | ✅ |
| 54 | InitiativeAutoAcceptResponsesFlag | AUTO_ACCEPT_RESPONSES_FLAG | — | ✅ |
| 55 | InitiativeAutoPopulateResponsesFlag | AUTO_POPULATE_RESPONSES_FLAG | — | ✅ |
| 56 | InitiativeCanceledBy | CANCELED_BY | — | ✅ |
| 57 | InitiativeCanceledDate | CANCELED_DATE | — | ✅ |
| 58 | InitiativeCanceledReasonCode | CANCELED_REASON_CODE | — | ✅ |
| 59 | InitiativeCompletedDate | COMPLETED_DATE | — | ✅ |
| 60 | InitiativeCreatedBy | CREATED_BY | — | ✅ |
| 61 | InitiativeCreationDate | CREATION_DATE | — | ✅ |
| 62 | InitiativeCreationSource | CREATION_SOURCE | — | ✅ |
| 63 | InitiativeDescription | DESCRIPTION | — | ✅ |
| 64 | InitiativeInitiativeId | INITIATIVE_ID | — | ✅ |
| 65 | InitiativeInitiativeNumber | INITIATIVE_NUMBER | — | ✅ |
| 66 | InitiativeInternalNote | INTERNAL_NOTE | — | ✅ |
| 67 | InitiativeLastOverdueReminderDate | LAST_OVERDUE_REMINDER_DATE | — | ✅ |
| 68 | InitiativeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 69 | InitiativeLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 70 | InitiativeLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 71 | InitiativeLaunchDate | LAUNCH_DATE | — | ✅ |
| 72 | InitiativeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 73 | InitiativeOwnerId | OWNER_ID | — | ✅ |
| 74 | InitiativePrcBuId | PRC_BU_ID | — | ✅ |
| 75 | InitiativeQualModelId | QUAL_MODEL_ID | — | ✅ |
| 76 | InitiativeReuseActiveQualFlag | REUSE_ACTIVE_QUAL_FLAG | — | ✅ |
| 77 | InitiativeStatus | STATUS | — | ✅ |
| 78 | InitiativeTitle | TITLE | — | ✅ |
| 79 | InitiativeType | TYPE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
