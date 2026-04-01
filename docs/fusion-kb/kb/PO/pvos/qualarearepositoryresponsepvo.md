---
id: DOC-PO-PVO-QualAreaRepositoryResponsePVO
doc_type: system-doc
title: "QualAreaRepositoryResponsePVO — PVO Purchasing"
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
  - QualAreaRepositoryResponsePVO
  - qualarearepositoryresponsepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QualAreaRepositoryResponsePVO

## 📌 Visão Geral

Extrai respostas do repositório por área de qualificação, consolidando informações históricas de fornecedores. Suporta avaliação baseada em dados pré-existentes e reduz retrabalho de coleta.

**Caminho:** `FscmTopModelAM.PrcPoqPublicViewAM.QualAreaRepositoryResponsePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 577 | 7 | 2 | 577 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 137 atributos (137 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 128 atributos (128 BICC)
- [[poq_qual_areas_vl|POQ_QUAL_AREAS_VL]] — 23 atributos (23 BICC)
- [[poq_qual_area_questions|POQ_QUAL_AREA_QUESTIONS]] — 10 atributos (1 PKs, 10 BICC)
- [[poq_questions_vl|POQ_QUESTIONS_VL]] — 33 atributos (33 BICC)
- [[poq_response_repository|POQ_RESPONSE_REPOSITORY]] — 31 atributos (1 PKs, 31 BICC)
- [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]] — 215 atributos (215 BICC)

---

## ⚙️ Atributos

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SuppContactPartyAddress1 | ADDRESS1 | — | ✅ |
| 2 | SuppContactPartyAddress2 | ADDRESS2 | — | ✅ |
| 3 | SuppContactPartyAddress3 | ADDRESS3 | — | ✅ |
| 4 | SuppContactPartyAddress4 | ADDRESS4 | — | ✅ |
| 5 | SuppContactPartyAnalysisFy | ANALYSIS_FY | — | ✅ |
| 6 | SuppContactPartyAttribute1 | ATTRIBUTE1 | — | ✅ |
| 7 | SuppContactPartyAttribute10 | ATTRIBUTE10 | — | ✅ |
| 8 | SuppContactPartyAttribute11 | ATTRIBUTE11 | — | ✅ |
| 9 | SuppContactPartyAttribute12 | ATTRIBUTE12 | — | ✅ |
| 10 | SuppContactPartyAttribute13 | ATTRIBUTE13 | — | ✅ |
| 11 | SuppContactPartyAttribute14 | ATTRIBUTE14 | — | ✅ |
| 12 | SuppContactPartyAttribute15 | ATTRIBUTE15 | — | ✅ |
| 13 | SuppContactPartyAttribute16 | ATTRIBUTE16 | — | ✅ |
| 14 | SuppContactPartyAttribute17 | ATTRIBUTE17 | — | ✅ |
| 15 | SuppContactPartyAttribute18 | ATTRIBUTE18 | — | ✅ |
| 16 | SuppContactPartyAttribute19 | ATTRIBUTE19 | — | ✅ |
| 17 | SuppContactPartyAttribute2 | ATTRIBUTE2 | — | ✅ |
| 18 | SuppContactPartyAttribute20 | ATTRIBUTE20 | — | ✅ |
| 19 | SuppContactPartyAttribute21 | ATTRIBUTE21 | — | ✅ |
| 20 | SuppContactPartyAttribute22 | ATTRIBUTE22 | — | ✅ |
| 21 | SuppContactPartyAttribute23 | ATTRIBUTE23 | — | ✅ |
| 22 | SuppContactPartyAttribute24 | ATTRIBUTE24 | — | ✅ |
| 23 | SuppContactPartyAttribute25 | ATTRIBUTE25 | — | ✅ |
| 24 | SuppContactPartyAttribute26 | ATTRIBUTE26 | — | ✅ |
| 25 | SuppContactPartyAttribute27 | ATTRIBUTE27 | — | ✅ |
| 26 | SuppContactPartyAttribute28 | ATTRIBUTE28 | — | ✅ |
| 27 | SuppContactPartyAttribute29 | ATTRIBUTE29 | — | ✅ |
| 28 | SuppContactPartyAttribute3 | ATTRIBUTE3 | — | ✅ |
| 29 | SuppContactPartyAttribute30 | ATTRIBUTE30 | — | ✅ |
| 30 | SuppContactPartyAttribute4 | ATTRIBUTE4 | — | ✅ |
| 31 | SuppContactPartyAttribute5 | ATTRIBUTE5 | — | ✅ |
| 32 | SuppContactPartyAttribute6 | ATTRIBUTE6 | — | ✅ |
| 33 | SuppContactPartyAttribute7 | ATTRIBUTE7 | — | ✅ |
| 34 | SuppContactPartyAttribute8 | ATTRIBUTE8 | — | ✅ |
| 35 | SuppContactPartyAttribute9 | ATTRIBUTE9 | — | ✅ |
| 36 | SuppContactPartyAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 37 | SuppContactPartyAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 38 | SuppContactPartyAttributeDate10 | ATTRIBUTE_DATE10 | — | ✅ |
| 39 | SuppContactPartyAttributeDate11 | ATTRIBUTE_DATE11 | — | ✅ |
| 40 | SuppContactPartyAttributeDate12 | ATTRIBUTE_DATE12 | — | ✅ |
| 41 | SuppContactPartyAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 42 | SuppContactPartyAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 43 | SuppContactPartyAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 44 | SuppContactPartyAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 45 | SuppContactPartyAttributeDate6 | ATTRIBUTE_DATE6 | — | ✅ |
| 46 | SuppContactPartyAttributeDate7 | ATTRIBUTE_DATE7 | — | ✅ |
| 47 | SuppContactPartyAttributeDate8 | ATTRIBUTE_DATE8 | — | ✅ |
| 48 | SuppContactPartyAttributeDate9 | ATTRIBUTE_DATE9 | — | ✅ |
| 49 | SuppContactPartyAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 50 | SuppContactPartyAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 51 | SuppContactPartyAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | ✅ |
| 52 | SuppContactPartyAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | ✅ |
| 53 | SuppContactPartyAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 54 | SuppContactPartyAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 55 | SuppContactPartyAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 56 | SuppContactPartyAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 57 | SuppContactPartyAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 58 | SuppContactPartyAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 59 | SuppContactPartyAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 60 | SuppContactPartyAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 61 | SuppContactPartyCategoryCode | CATEGORY_CODE | — | ✅ |
| 62 | SuppContactPartyCeoName | CEO_NAME | — | ✅ |
| 63 | SuppContactPartyCertReasonCode | CERT_REASON_CODE | — | ✅ |
| 64 | SuppContactPartyCertificationLevel | CERTIFICATION_LEVEL | — | ✅ |
| 65 | SuppContactPartyCity | CITY | — | ✅ |
| 66 | SuppContactPartyComments | COMMENTS | — | ✅ |
| 67 | SuppContactPartyCountry | COUNTRY | — | ✅ |
| 68 | SuppContactPartyCounty | COUNTY | — | ✅ |
| 69 | SuppContactPartyCreatedBy | CREATED_BY | — | ✅ |
| 70 | SuppContactPartyCreatedByModule | CREATED_BY_MODULE | — | ✅ |
| 71 | SuppContactPartyCreationDate | CREATION_DATE | — | ✅ |
| 72 | SuppContactPartyCurrFyPotentialRevenue | CURR_FY_POTENTIAL_REVENUE | — | ✅ |
| 73 | SuppContactPartyDateOfBirth | DATE_OF_BIRTH | — | ✅ |
| 74 | SuppContactPartyDunsNumberC | DUNS_NUMBER_C | — | ✅ |
| 75 | SuppContactPartyEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 76 | SuppContactPartyEmployeesTotal | EMPLOYEES_TOTAL | — | ✅ |
| 77 | SuppContactPartyFiscalYearendMonth | FISCAL_YEAREND_MONTH | — | ✅ |
| 78 | SuppContactPartyGender | GENDER | — | ✅ |
| 79 | SuppContactPartyGroupType | GROUP_TYPE | — | ✅ |
| 80 | SuppContactPartyGsaIndicatorFlag | GSA_INDICATOR_FLAG | — | ✅ |
| 81 | SuppContactPartyHomeCountry | HOME_COUNTRY | — | ✅ |
| 82 | SuppContactPartyHqBranchInd | HQ_BRANCH_IND | — | ✅ |
| 83 | SuppContactPartyIdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | ✅ |
| 84 | SuppContactPartyIdenAddrPartySiteId | IDEN_ADDR_PARTY_SITE_ID | — | ✅ |
| 85 | SuppContactPartyInternalFlag | INTERNAL_FLAG | — | ✅ |
| 86 | SuppContactPartyJgzzFiscalCode | JGZZ_FISCAL_CODE | — | ✅ |
| 87 | SuppContactPartyLanguageName | LANGUAGE_NAME | — | ✅ |
| 88 | SuppContactPartyLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 89 | SuppContactPartyLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 90 | SuppContactPartyLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 91 | SuppContactPartyMaritalStatus | MARITAL_STATUS | — | ✅ |
| 92 | SuppContactPartyMissionStatement | MISSION_STATEMENT | — | ✅ |
| 93 | SuppContactPartyNextFyPotentialRevenue | NEXT_FY_POTENTIAL_REVENUE | — | ✅ |
| 94 | SuppContactPartyObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 95 | SuppContactPartyOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | ✅ |
| 96 | SuppContactPartyPartyId | PARTY_ID | — | ✅ |
| 97 | SuppContactPartyPartyName | PARTY_NAME | — | ✅ |
| 98 | SuppContactPartyPartyNumber | PARTY_NUMBER | — | ✅ |
| 99 | SuppContactPartyPartyType | PARTY_TYPE | — | ✅ |
| 100 | SuppContactPartyPartyUniqueName | PARTY_UNIQUE_NAME | — | ✅ |
| 101 | SuppContactPartyPersonAcademicTitle | PERSON_ACADEMIC_TITLE | — | ✅ |
| 102 | SuppContactPartyPersonFirstName | PERSON_FIRST_NAME | — | ✅ |
| 103 | SuppContactPartyPersonLastName | PERSON_LAST_NAME | — | ✅ |
| 104 | SuppContactPartyPersonLastNamePrefix | PERSON_LAST_NAME_PREFIX | — | ✅ |
| 105 | SuppContactPartyPersonMiddleName | PERSON_MIDDLE_NAME | — | ✅ |
| 106 | SuppContactPartyPersonNameSuffix | PERSON_NAME_SUFFIX | — | ✅ |
| 107 | SuppContactPartyPersonPreNameAdjunct | PERSON_PRE_NAME_ADJUNCT | — | ✅ |
| 108 | SuppContactPartyPersonPreviousLastName | PERSON_PREVIOUS_LAST_NAME | — | ✅ |
| 109 | SuppContactPartyPersonSecondLastName | PERSON_SECOND_LAST_NAME | — | ✅ |
| 110 | SuppContactPartyPersonTitle | PERSON_TITLE | — | ✅ |
| 111 | SuppContactPartyPostalCode | POSTAL_CODE | — | ✅ |
| 112 | SuppContactPartyPrefFunctionalCurrency | PREF_FUNCTIONAL_CURRENCY | — | ✅ |
| 113 | SuppContactPartyPreferredContactMethod | PREFERRED_CONTACT_METHOD | — | ✅ |
| 114 | SuppContactPartyPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | ✅ |
| 115 | SuppContactPartyPreferredName | PREFERRED_NAME | — | ✅ |
| 116 | SuppContactPartyPreferredNameId | PREFERRED_NAME_ID | — | ✅ |
| 117 | SuppContactPartyPrimaryEmailContactPtId | PRIMARY_EMAIL_CONTACT_PT_ID | — | ✅ |
| 118 | SuppContactPartyPrimaryPhoneAreaCode | PRIMARY_PHONE_AREA_CODE | — | ✅ |
| 119 | SuppContactPartyPrimaryPhoneContactPtId | PRIMARY_PHONE_CONTACT_PT_ID | — | ✅ |
| 120 | SuppContactPartyPrimaryPhoneCountryCode | PRIMARY_PHONE_COUNTRY_CODE | — | ✅ |
| 121 | SuppContactPartyPrimaryPhoneExtension | PRIMARY_PHONE_EXTENSION | — | ✅ |
| 122 | SuppContactPartyPrimaryPhoneLineType | PRIMARY_PHONE_LINE_TYPE | — | ✅ |
| 123 | SuppContactPartyPrimaryPhoneNumber | PRIMARY_PHONE_NUMBER | — | ✅ |
| 124 | SuppContactPartyPrimaryPhonePurpose | PRIMARY_PHONE_PURPOSE | — | ✅ |
| 125 | SuppContactPartyPrimaryUrlContactPtId | PRIMARY_URL_CONTACT_PT_ID | — | ✅ |
| 126 | SuppContactPartyProvince | PROVINCE | — | ✅ |
| 127 | SuppContactPartySalutation | SALUTATION | — | ✅ |
| 128 | SuppContactPartySicCode | SIC_CODE | — | ✅ |
| 129 | SuppContactPartySicCodeType | SIC_CODE_TYPE | — | ✅ |
| 130 | SuppContactPartyState | STATE | — | ✅ |
| 131 | SuppContactPartyStatus | STATUS | — | ✅ |
| 132 | SuppContactPartyThirdPartyFlag | THIRD_PARTY_FLAG | — | ✅ |
| 133 | SuppContactPartyTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | ✅ |
| 134 | SuppContactPartyUrl | URL | — | ✅ |
| 135 | SuppContactPartyUserGuid | USER_GUID | — | ✅ |
| 136 | SuppContactPartyValidatedFlag | VALIDATED_FLAG | — | ✅ |
| 137 | SuppContactPartyYearEstablished | YEAR_ESTABLISHED | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcceptedByAttribute1 | ATTRIBUTE1 | — | ✅ |
| 2 | AcceptedByAttribute10 | ATTRIBUTE10 | — | ✅ |
| 3 | AcceptedByAttribute11 | ATTRIBUTE11 | — | ✅ |
| 4 | AcceptedByAttribute12 | ATTRIBUTE12 | — | ✅ |
| 5 | AcceptedByAttribute13 | ATTRIBUTE13 | — | ✅ |
| 6 | AcceptedByAttribute14 | ATTRIBUTE14 | — | ✅ |
| 7 | AcceptedByAttribute15 | ATTRIBUTE15 | — | ✅ |
| 8 | AcceptedByAttribute16 | ATTRIBUTE16 | — | ✅ |
| 9 | AcceptedByAttribute17 | ATTRIBUTE17 | — | ✅ |
| 10 | AcceptedByAttribute18 | ATTRIBUTE18 | — | ✅ |
| 11 | AcceptedByAttribute19 | ATTRIBUTE19 | — | ✅ |
| 12 | AcceptedByAttribute2 | ATTRIBUTE2 | — | ✅ |
| 13 | AcceptedByAttribute20 | ATTRIBUTE20 | — | ✅ |
| 14 | AcceptedByAttribute21 | ATTRIBUTE21 | — | ✅ |
| 15 | AcceptedByAttribute22 | ATTRIBUTE22 | — | ✅ |
| 16 | AcceptedByAttribute23 | ATTRIBUTE23 | — | ✅ |
| 17 | AcceptedByAttribute24 | ATTRIBUTE24 | — | ✅ |
| 18 | AcceptedByAttribute25 | ATTRIBUTE25 | — | ✅ |
| 19 | AcceptedByAttribute26 | ATTRIBUTE26 | — | ✅ |
| 20 | AcceptedByAttribute27 | ATTRIBUTE27 | — | ✅ |
| 21 | AcceptedByAttribute28 | ATTRIBUTE28 | — | ✅ |
| 22 | AcceptedByAttribute29 | ATTRIBUTE29 | — | ✅ |
| 23 | AcceptedByAttribute3 | ATTRIBUTE3 | — | ✅ |
| 24 | AcceptedByAttribute30 | ATTRIBUTE30 | — | ✅ |
| 25 | AcceptedByAttribute4 | ATTRIBUTE4 | — | ✅ |
| 26 | AcceptedByAttribute5 | ATTRIBUTE5 | — | ✅ |
| 27 | AcceptedByAttribute6 | ATTRIBUTE6 | — | ✅ |
| 28 | AcceptedByAttribute7 | ATTRIBUTE7 | — | ✅ |
| 29 | AcceptedByAttribute8 | ATTRIBUTE8 | — | ✅ |
| 30 | AcceptedByAttribute9 | ATTRIBUTE9 | — | ✅ |
| 31 | AcceptedByAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 32 | AcceptedByAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 33 | AcceptedByAttributeDate10 | ATTRIBUTE_DATE10 | — | ✅ |
| 34 | AcceptedByAttributeDate11 | ATTRIBUTE_DATE11 | — | ✅ |
| 35 | AcceptedByAttributeDate12 | ATTRIBUTE_DATE12 | — | ✅ |
| 36 | AcceptedByAttributeDate13 | ATTRIBUTE_DATE13 | — | ✅ |
| 37 | AcceptedByAttributeDate14 | ATTRIBUTE_DATE14 | — | ✅ |
| 38 | AcceptedByAttributeDate15 | ATTRIBUTE_DATE15 | — | ✅ |
| 39 | AcceptedByAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 40 | AcceptedByAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 41 | AcceptedByAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 42 | AcceptedByAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 43 | AcceptedByAttributeDate6 | ATTRIBUTE_DATE6 | — | ✅ |
| 44 | AcceptedByAttributeDate7 | ATTRIBUTE_DATE7 | — | ✅ |
| 45 | AcceptedByAttributeDate8 | ATTRIBUTE_DATE8 | — | ✅ |
| 46 | AcceptedByAttributeDate9 | ATTRIBUTE_DATE9 | — | ✅ |
| 47 | AcceptedByAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 48 | AcceptedByAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 49 | AcceptedByAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | ✅ |
| 50 | AcceptedByAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | ✅ |
| 51 | AcceptedByAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | ✅ |
| 52 | AcceptedByAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | ✅ |
| 53 | AcceptedByAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | ✅ |
| 54 | AcceptedByAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | ✅ |
| 55 | AcceptedByAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | ✅ |
| 56 | AcceptedByAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | ✅ |
| 57 | AcceptedByAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | ✅ |
| 58 | AcceptedByAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 59 | AcceptedByAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | ✅ |
| 60 | AcceptedByAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 61 | AcceptedByAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 62 | AcceptedByAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 63 | AcceptedByAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 64 | AcceptedByAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 65 | AcceptedByAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 66 | AcceptedByAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 67 | AcceptedByBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 68 | AcceptedByCreatedBy | CREATED_BY | — | ✅ |
| 69 | AcceptedByCreationDate | CREATION_DATE | — | ✅ |
| 70 | AcceptedByDisplayName | DISPLAY_NAME | — | ✅ |
| 71 | AcceptedByEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 72 | AcceptedByEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 73 | AcceptedByFirstName | FIRST_NAME | — | ✅ |
| 74 | AcceptedByFullName | FULL_NAME | — | ✅ |
| 75 | AcceptedByHonors | HONORS | — | ✅ |
| 76 | AcceptedByKnownAs | KNOWN_AS | — | ✅ |
| 77 | AcceptedByLastName | LAST_NAME | — | ✅ |
| 78 | AcceptedByLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 79 | AcceptedByLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 80 | AcceptedByLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 81 | AcceptedByLegislationCode | LEGISLATION_CODE | — | ✅ |
| 82 | AcceptedByListName | LIST_NAME | — | ✅ |
| 83 | AcceptedByMiddleNames | MIDDLE_NAMES | — | ✅ |
| 84 | AcceptedByMilitaryRank | MILITARY_RANK | — | ✅ |
| 85 | AcceptedByNamInformation1 | NAM_INFORMATION1 | — | ✅ |
| 86 | AcceptedByNamInformation10 | NAM_INFORMATION10 | — | ✅ |
| 87 | AcceptedByNamInformation11 | NAM_INFORMATION11 | — | ✅ |
| 88 | AcceptedByNamInformation12 | NAM_INFORMATION12 | — | ✅ |
| 89 | AcceptedByNamInformation13 | NAM_INFORMATION13 | — | ✅ |
| 90 | AcceptedByNamInformation14 | NAM_INFORMATION14 | — | ✅ |
| 91 | AcceptedByNamInformation15 | NAM_INFORMATION15 | — | ✅ |
| 92 | AcceptedByNamInformation16 | NAM_INFORMATION16 | — | ✅ |
| 93 | AcceptedByNamInformation17 | NAM_INFORMATION17 | — | ✅ |
| 94 | AcceptedByNamInformation18 | NAM_INFORMATION18 | — | ✅ |
| 95 | AcceptedByNamInformation19 | NAM_INFORMATION19 | — | ✅ |
| 96 | AcceptedByNamInformation2 | NAM_INFORMATION2 | — | ✅ |
| 97 | AcceptedByNamInformation20 | NAM_INFORMATION20 | — | ✅ |
| 98 | AcceptedByNamInformation21 | NAM_INFORMATION21 | — | ✅ |
| 99 | AcceptedByNamInformation22 | NAM_INFORMATION22 | — | ✅ |
| 100 | AcceptedByNamInformation23 | NAM_INFORMATION23 | — | ✅ |
| 101 | AcceptedByNamInformation24 | NAM_INFORMATION24 | — | ✅ |
| 102 | AcceptedByNamInformation25 | NAM_INFORMATION25 | — | ✅ |
| 103 | AcceptedByNamInformation26 | NAM_INFORMATION26 | — | ✅ |
| 104 | AcceptedByNamInformation27 | NAM_INFORMATION27 | — | ✅ |
| 105 | AcceptedByNamInformation28 | NAM_INFORMATION28 | — | ✅ |
| 106 | AcceptedByNamInformation29 | NAM_INFORMATION29 | — | ✅ |
| 107 | AcceptedByNamInformation3 | NAM_INFORMATION3 | — | ✅ |
| 108 | AcceptedByNamInformation30 | NAM_INFORMATION30 | — | ✅ |
| 109 | AcceptedByNamInformation4 | NAM_INFORMATION4 | — | ✅ |
| 110 | AcceptedByNamInformation5 | NAM_INFORMATION5 | — | ✅ |
| 111 | AcceptedByNamInformation6 | NAM_INFORMATION6 | — | ✅ |
| 112 | AcceptedByNamInformation7 | NAM_INFORMATION7 | — | ✅ |
| 113 | AcceptedByNamInformation8 | NAM_INFORMATION8 | — | ✅ |
| 114 | AcceptedByNamInformation9 | NAM_INFORMATION9 | — | ✅ |
| 115 | AcceptedByNamInformationCategory | NAM_INFORMATION_CATEGORY | — | ✅ |
| 116 | AcceptedByNameType | NAME_TYPE | — | ✅ |
| 117 | AcceptedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 118 | AcceptedByOrderName | ORDER_NAME | — | ✅ |
| 119 | AcceptedByPersonId | PERSON_ID | — | ✅ |
| 120 | AcceptedByPersonNameId | PERSON_NAME_ID | — | ✅ |
| 121 | AcceptedByPreNameAdjunct | PRE_NAME_ADJUNCT | — | ✅ |
| 122 | AcceptedByPreviousLastName | PREVIOUS_LAST_NAME | — | ✅ |
| 123 | AcceptedBySuffix | SUFFIX | — | ✅ |
| 124 | AcceptedByTitle | TITLE | — | ✅ |
| 125 | SurrogEnteredByDisplayName | DISPLAY_NAME | — | ✅ |
| 126 | SurrogEnteredByEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 127 | SurrogEnteredByEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 128 | SurrogEnteredByPersonNameId | PERSON_NAME_ID | — | ✅ |

### [[poq_qual_areas_vl|POQ_QUAL_AREAS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualAreaActivationDate | ACTIVATION_DATE | — | ✅ |
| 2 | QualAreaCreatedBy | CREATED_BY | — | ✅ |
| 3 | QualAreaCreationDate | CREATION_DATE | — | ✅ |
| 4 | QualAreaExpirationReminderPeriod | EXPIRATION_REMINDER_PERIOD | — | ✅ |
| 5 | QualAreaExpirationReminderType | EXPIRATION_REMINDER_TYPE | — | ✅ |
| 6 | QualAreaGlobalFlag | GLOBAL_FLAG | — | ✅ |
| 7 | QualAreaInformationOnlyFlag | INFORMATION_ONLY_FLAG | — | ✅ |
| 8 | QualAreaLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | QualAreaLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | QualAreaLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | QualAreaLatestRevisionFlag | LATEST_REVISION_FLAG | — | ✅ |
| 12 | QualAreaObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | QualAreaOriginalQualAreaId | ORIGINAL_QUAL_AREA_ID | — | ✅ |
| 14 | QualAreaOwnerId | OWNER_ID | — | ✅ |
| 15 | QualAreaPrcBuId | PRC_BU_ID | — | ✅ |
| 16 | QualAreaQualAreaDescription | QUAL_AREA_DESCRIPTION | — | ✅ |
| 17 | QualAreaQualAreaId | QUAL_AREA_ID | — | ✅ |
| 18 | QualAreaQualAreaLevel | QUAL_AREA_LEVEL | — | ✅ |
| 19 | QualAreaQualAreaName | QUAL_AREA_NAME | — | ✅ |
| 20 | QualAreaQualAreaStatus | QUAL_AREA_STATUS | — | ✅ |
| 21 | QualAreaRevisionNumber | REVISION_NUMBER | — | ✅ |
| 22 | QualAreaStdsOrgCode | STDS_ORG_CODE | — | ✅ |
| 23 | QualAreaSubjectCode | SUBJECT_CODE | — | ✅ |

### [[poq_qual_area_questions|POQ_QUAL_AREA_QUESTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualAreaQuestionCreatedBy | CREATED_BY | — | ✅ |
| 2 | QualAreaQuestionCreationDate | CREATION_DATE | — | ✅ |
| 3 | QualAreaQuestionDisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 4 | QualAreaQuestionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | QualAreaQuestionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | QualAreaQuestionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | QualAreaQuestionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | QualAreaQuestionQualAreaId | QUAL_AREA_ID | — | ✅ |
| 9 | QualAreaQuestionQualAreaQuestionId | QUAL_AREA_QUESTION_ID | 🔑 | ✅ |
| 10 | QualAreaQuestionQuestionId | QUESTION_ID | — | ✅ |

### [[poq_questions_vl|POQ_QUESTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QuestionActivationDate | ACTIVATION_DATE | — | ✅ |
| 2 | QuestionAllowRespCommentFlag | ALLOW_RESP_COMMENT_FLAG | — | ✅ |
| 3 | QuestionAttachmentAllowedCode | ATTACHMENT_ALLOWED_CODE | — | ✅ |
| 4 | QuestionCreatedBy | CREATED_BY | — | ✅ |
| 5 | QuestionCreationDate | CREATION_DATE | — | ✅ |
| 6 | QuestionCriticalQuestionFlag | CRITICAL_QUESTION_FLAG | — | ✅ |
| 7 | QuestionDisplayPreferredRespFlag | DISPLAY_PREFERRED_RESP_FLAG | — | ✅ |
| 8 | QuestionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | QuestionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | QuestionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | QuestionLatestRevisionFlag | LATEST_REVISION_FLAG | — | ✅ |
| 12 | QuestionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | QuestionOriginalQuestionId | ORIGINAL_QUESTION_ID | — | ✅ |
| 14 | QuestionOwnerId | OWNER_ID | — | ✅ |
| 15 | QuestionPreferredResponseDate | PREFERRED_RESPONSE_DATE | — | ✅ |
| 16 | QuestionPreferredResponseDatetime | PREFERRED_RESPONSE_DATETIME | — | ✅ |
| 17 | QuestionPreferredResponseNumber | PREFERRED_RESPONSE_NUMBER | — | ✅ |
| 18 | QuestionPreferredResponseText | PREFERRED_RESPONSE_TEXT | — | ✅ |
| 19 | QuestionQuestionHint | QUESTION_HINT | — | ✅ |
| 20 | QuestionQuestionId | QUESTION_ID | — | ✅ |
| 21 | QuestionQuestionLevel | QUESTION_LEVEL | — | ✅ |
| 22 | QuestionQuestionName | QUESTION_NAME | — | ✅ |
| 23 | QuestionQuestionStatus | QUESTION_STATUS | — | ✅ |
| 24 | QuestionQuestionText | QUESTION_TEXT | — | ✅ |
| 25 | QuestionQuestionType | QUESTION_TYPE | — | ✅ |
| 26 | QuestionResponderType | RESPONDER_TYPE | — | ✅ |
| 27 | QuestionResponseRequiredFlag | RESPONSE_REQUIRED_FLAG | — | ✅ |
| 28 | QuestionResponseType | RESPONSE_TYPE | — | ✅ |
| 29 | QuestionRevisionNumber | REVISION_NUMBER | — | ✅ |
| 30 | QuestionStdsOrgCode | STDS_ORG_CODE | — | ✅ |
| 31 | QuestionSubjectCode | SUBJECT_CODE | — | ✅ |
| 32 | QuestionSupplierAttributeCode | SUPPLIER_ATTRIBUTE_CODE | — | ✅ |
| 33 | QuestionSupplierAttributeFlag | SUPPLIER_ATTRIBUTE_FLAG | — | ✅ |

### [[poq_response_repository|POQ_RESPONSE_REPOSITORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AggregateResponseFlag | AGGREGATE_RESPONSE_FLAG | — | ✅ |
| 2 | ResponseRepositoryAcceptanceDate | ACCEPTANCE_DATE | — | ✅ |
| 3 | ResponseRepositoryAcceptanceNote | ACCEPTANCE_NOTE | — | ✅ |
| 4 | ResponseRepositoryAcceptedBy | ACCEPTED_BY | — | ✅ |
| 5 | ResponseRepositoryBatchId | BATCH_ID | — | ✅ |
| 6 | ResponseRepositoryCreatedBy | CREATED_BY | — | ✅ |
| 7 | ResponseRepositoryCreationDate | CREATION_DATE | — | ✅ |
| 8 | ResponseRepositoryDataSourceId | DATA_SOURCE_ID | — | ✅ |
| 9 | ResponseRepositoryDataSourceType | DATA_SOURCE_TYPE | — | ✅ |
| 10 | ResponseRepositoryFirstSubmissionDate | FIRST_SUBMISSION_DATE | — | ✅ |
| 11 | ResponseRepositoryId | RESPONSE_REPOSITORY_ID | 🔑 | ✅ |
| 12 | ResponseRepositoryInternalRespondentId | INTERNAL_RESPONDENT_ID | — | ✅ |
| 13 | ResponseRepositoryLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | ResponseRepositoryLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | ResponseRepositoryLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | ResponseRepositoryMergeRequestId | MERGE_REQUEST_ID | — | ✅ |
| 17 | ResponseRepositoryObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | ResponseRepositoryOriginalQuestionId | ORIGINAL_QUESTION_ID | — | ✅ |
| 19 | ResponseRepositoryQuestionId | QUESTION_ID | — | ✅ |
| 20 | ResponseRepositoryRequestId | REQUEST_ID | — | ✅ |
| 21 | ResponseRepositoryResponderType | RESPONDER_TYPE | — | ✅ |
| 22 | ResponseRepositoryResponseArchiveDate | RESPONSE_ARCHIVE_DATE | — | ✅ |
| 23 | ResponseRepositoryResponseComments | RESPONSE_COMMENTS | — | ✅ |
| 24 | ResponseRepositoryResponseStatus | RESPONSE_STATUS | — | ✅ |
| 25 | ResponseRepositoryResponseSubmissionDate | RESPONSE_SUBMISSION_DATE | — | ✅ |
| 26 | ResponseRepositorySupplierContactPartyId | SUPPLIER_CONTACT_PARTY_ID | — | ✅ |
| 27 | ResponseRepositorySupplierId | SUPPLIER_ID | — | ✅ |
| 28 | ResponseRepositorySupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 29 | ResponseRepositorySurrogEnteredBy | SURROG_ENTERED_BY | — | ✅ |
| 30 | ResponseRepositorySurrogEntryDate | SURROG_ENTRY_DATE | — | ✅ |
| 31 | ResponseRepositorySurrogResponseFlag | SURROG_RESPONSE_FLAG | — | ✅ |

### [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SuppSiteAgingOnsetPoint | AGING_ONSET_POINT | — | ✅ |
| 2 | SuppSiteAgingPeriodDays | AGING_PERIOD_DAYS | — | ✅ |
| 3 | SuppSiteAllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | ✅ |
| 4 | SuppSiteAllowUnorderedReceiptsFlag | ALLOW_UNORDERED_RECEIPTS_FLAG | — | ✅ |
| 5 | SuppSiteAlwaysTakeDiscFlag | ALWAYS_TAKE_DISC_FLAG | — | ✅ |
| 6 | SuppSiteAmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | ✅ |
| 7 | SuppSiteApTaxRoundingRule | AP_TAX_ROUNDING_RULE | — | ✅ |
| 8 | SuppSiteAreaCode | AREA_CODE | — | ✅ |
| 9 | SuppSiteAttentionArFlag | ATTENTION_AR_FLAG | — | ✅ |
| 10 | SuppSiteAttribute1 | ATTRIBUTE1 | — | ✅ |
| 11 | SuppSiteAttribute10 | ATTRIBUTE10 | — | ✅ |
| 12 | SuppSiteAttribute11 | ATTRIBUTE11 | — | ✅ |
| 13 | SuppSiteAttribute12 | ATTRIBUTE12 | — | ✅ |
| 14 | SuppSiteAttribute13 | ATTRIBUTE13 | — | ✅ |
| 15 | SuppSiteAttribute14 | ATTRIBUTE14 | — | ✅ |
| 16 | SuppSiteAttribute15 | ATTRIBUTE15 | — | ✅ |
| 17 | SuppSiteAttribute16 | ATTRIBUTE16 | — | ✅ |
| 18 | SuppSiteAttribute17 | ATTRIBUTE17 | — | ✅ |
| 19 | SuppSiteAttribute18 | ATTRIBUTE18 | — | ✅ |
| 20 | SuppSiteAttribute19 | ATTRIBUTE19 | — | ✅ |
| 21 | SuppSiteAttribute2 | ATTRIBUTE2 | — | ✅ |
| 22 | SuppSiteAttribute20 | ATTRIBUTE20 | — | ✅ |
| 23 | SuppSiteAttribute3 | ATTRIBUTE3 | — | ✅ |
| 24 | SuppSiteAttribute4 | ATTRIBUTE4 | — | ✅ |
| 25 | SuppSiteAttribute5 | ATTRIBUTE5 | — | ✅ |
| 26 | SuppSiteAttribute6 | ATTRIBUTE6 | — | ✅ |
| 27 | SuppSiteAttribute7 | ATTRIBUTE7 | — | ✅ |
| 28 | SuppSiteAttribute8 | ATTRIBUTE8 | — | ✅ |
| 29 | SuppSiteAttribute9 | ATTRIBUTE9 | — | ✅ |
| 30 | SuppSiteAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 31 | SuppSiteAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 32 | SuppSiteAttributeDate10 | ATTRIBUTE_DATE10 | — | ✅ |
| 33 | SuppSiteAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 34 | SuppSiteAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 35 | SuppSiteAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 36 | SuppSiteAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 37 | SuppSiteAttributeDate6 | ATTRIBUTE_DATE6 | — | ✅ |
| 38 | SuppSiteAttributeDate7 | ATTRIBUTE_DATE7 | — | ✅ |
| 39 | SuppSiteAttributeDate8 | ATTRIBUTE_DATE8 | — | ✅ |
| 40 | SuppSiteAttributeDate9 | ATTRIBUTE_DATE9 | — | ✅ |
| 41 | SuppSiteAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 42 | SuppSiteAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 43 | SuppSiteAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 44 | SuppSiteAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 45 | SuppSiteAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 46 | SuppSiteAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 47 | SuppSiteAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 48 | SuppSiteAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 49 | SuppSiteAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 50 | SuppSiteAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 51 | SuppSiteAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 52 | SuppSiteAttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | ✅ |
| 53 | SuppSiteAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 54 | SuppSiteAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 55 | SuppSiteAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 56 | SuppSiteAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 57 | SuppSiteAttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | ✅ |
| 58 | SuppSiteAttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | ✅ |
| 59 | SuppSiteAttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | ✅ |
| 60 | SuppSiteAttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | ✅ |
| 61 | SuppSiteAutoCalculateInterestFlag | AUTO_CALCULATE_INTEREST_FLAG | — | ✅ |
| 62 | SuppSiteAutoTaxCalcFlag | AUTO_TAX_CALC_FLAG | — | ✅ |
| 63 | SuppSiteAutoTaxCalcOverride | AUTO_TAX_CALC_OVERRIDE | — | ✅ |
| 64 | SuppSiteB2bCommMethodCode | B2B_COMM_METHOD_CODE | — | ✅ |
| 65 | SuppSiteB2bSiteCode | B2B_SITE_CODE | — | ✅ |
| 66 | SuppSiteBankChargeBearer | BANK_CHARGE_BEARER | — | ✅ |
| 67 | SuppSiteBuyerManagedTransportFlag | BUYER_MANAGED_TRANSPORT_FLAG | — | ✅ |
| 68 | SuppSiteCarrierId | CARRIER_ID | — | ✅ |
| 69 | SuppSiteConsumptionAdviceFrequency | CONSUMPTION_ADVICE_FREQUENCY | — | ✅ |
| 70 | SuppSiteConsumptionAdviceSummary | CONSUMPTION_ADVICE_SUMMARY | — | ✅ |
| 71 | SuppSiteCountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 72 | SuppSiteCreateDebitMemoFlag | CREATE_DEBIT_MEMO_FLAG | — | ✅ |
| 73 | SuppSiteCreatedBy | CREATED_BY | — | ✅ |
| 74 | SuppSiteCreationDate | CREATION_DATE | — | ✅ |
| 75 | SuppSiteCustomerNum | CUSTOMER_NUM | — | ✅ |
| 76 | SuppSiteDaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | ✅ |
| 77 | SuppSiteDaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | ✅ |
| 78 | SuppSiteDefaultPaySiteId | DEFAULT_PAY_SITE_ID | — | ✅ |
| 79 | SuppSiteEceTpLocationCode | ECE_TP_LOCATION_CODE | — | ✅ |
| 80 | SuppSiteEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 81 | SuppSiteEffectiveSequence | EFFECTIVE_SEQUENCE | — | ✅ |
| 82 | SuppSiteEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 83 | SuppSiteEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 84 | SuppSiteEnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | ✅ |
| 85 | SuppSiteExcludeFreightFromDiscount | EXCLUDE_FREIGHT_FROM_DISCOUNT | — | ✅ |
| 86 | SuppSiteExcludeTaxFromDiscount | EXCLUDE_TAX_FROM_DISCOUNT | — | ✅ |
| 87 | SuppSiteFax | FAX | — | ✅ |
| 88 | SuppSiteFaxAreaCode | FAX_AREA_CODE | — | ✅ |
| 89 | SuppSiteFaxCountryCode | FAX_COUNTRY_CODE | — | ✅ |
| 90 | SuppSiteFobLookupCode | FOB_LOOKUP_CODE | — | ✅ |
| 91 | SuppSiteFreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | ✅ |
| 92 | SuppSiteGaplessInvNumFlag | GAPLESS_INV_NUM_FLAG | — | ✅ |
| 93 | SuppSiteGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | ✅ |
| 94 | SuppSiteGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | ✅ |
| 95 | SuppSiteGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | ✅ |
| 96 | SuppSiteGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | ✅ |
| 97 | SuppSiteGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | ✅ |
| 98 | SuppSiteGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | ✅ |
| 99 | SuppSiteGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | ✅ |
| 100 | SuppSiteGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | ✅ |
| 101 | SuppSiteGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | ✅ |
| 102 | SuppSiteGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | ✅ |
| 103 | SuppSiteGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | ✅ |
| 104 | SuppSiteGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | ✅ |
| 105 | SuppSiteGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | ✅ |
| 106 | SuppSiteGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | ✅ |
| 107 | SuppSiteGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | ✅ |
| 108 | SuppSiteGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | ✅ |
| 109 | SuppSiteGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | ✅ |
| 110 | SuppSiteGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | ✅ |
| 111 | SuppSiteGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | ✅ |
| 112 | SuppSiteGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | ✅ |
| 113 | SuppSiteGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | ✅ |
| 114 | SuppSiteGlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | ✅ |
| 115 | SuppSiteGlobalAttributeDate10 | GLOBAL_ATTRIBUTE_DATE10 | — | ✅ |
| 116 | SuppSiteGlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | ✅ |
| 117 | SuppSiteGlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | ✅ |
| 118 | SuppSiteGlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | ✅ |
| 119 | SuppSiteGlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | ✅ |
| 120 | SuppSiteGlobalAttributeDate6 | GLOBAL_ATTRIBUTE_DATE6 | — | ✅ |
| 121 | SuppSiteGlobalAttributeDate7 | GLOBAL_ATTRIBUTE_DATE7 | — | ✅ |
| 122 | SuppSiteGlobalAttributeDate8 | GLOBAL_ATTRIBUTE_DATE8 | — | ✅ |
| 123 | SuppSiteGlobalAttributeDate9 | GLOBAL_ATTRIBUTE_DATE9 | — | ✅ |
| 124 | SuppSiteGlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | ✅ |
| 125 | SuppSiteGlobalAttributeNumber10 | GLOBAL_ATTRIBUTE_NUMBER10 | — | ✅ |
| 126 | SuppSiteGlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | ✅ |
| 127 | SuppSiteGlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | ✅ |
| 128 | SuppSiteGlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | ✅ |
| 129 | SuppSiteGlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | ✅ |
| 130 | SuppSiteGlobalAttributeNumber6 | GLOBAL_ATTRIBUTE_NUMBER6 | — | ✅ |
| 131 | SuppSiteGlobalAttributeNumber7 | GLOBAL_ATTRIBUTE_NUMBER7 | — | ✅ |
| 132 | SuppSiteGlobalAttributeNumber8 | GLOBAL_ATTRIBUTE_NUMBER8 | — | ✅ |
| 133 | SuppSiteGlobalAttributeNumber9 | GLOBAL_ATTRIBUTE_NUMBER9 | — | ✅ |
| 134 | SuppSiteGlobalAttributeTimestamp1 | GLOBAL_ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 135 | SuppSiteGlobalAttributeTimestamp10 | GLOBAL_ATTRIBUTE_TIMESTAMP10 | — | ✅ |
| 136 | SuppSiteGlobalAttributeTimestamp2 | GLOBAL_ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 137 | SuppSiteGlobalAttributeTimestamp3 | GLOBAL_ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 138 | SuppSiteGlobalAttributeTimestamp4 | GLOBAL_ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 139 | SuppSiteGlobalAttributeTimestamp5 | GLOBAL_ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 140 | SuppSiteGlobalAttributeTimestamp6 | GLOBAL_ATTRIBUTE_TIMESTAMP6 | — | ✅ |
| 141 | SuppSiteGlobalAttributeTimestamp7 | GLOBAL_ATTRIBUTE_TIMESTAMP7 | — | ✅ |
| 142 | SuppSiteGlobalAttributeTimestamp8 | GLOBAL_ATTRIBUTE_TIMESTAMP8 | — | ✅ |
| 143 | SuppSiteGlobalAttributeTimestamp9 | GLOBAL_ATTRIBUTE_TIMESTAMP9 | — | ✅ |
| 144 | SuppSiteHoldAllPaymentsFlag | HOLD_ALL_PAYMENTS_FLAG | — | ✅ |
| 145 | SuppSiteHoldBy | HOLD_BY | — | ✅ |
| 146 | SuppSiteHoldDate | HOLD_DATE | — | ✅ |
| 147 | SuppSiteHoldFlag | HOLD_FLAG | — | ✅ |
| 148 | SuppSiteHoldFuturePaymentsFlag | HOLD_FUTURE_PAYMENTS_FLAG | — | ✅ |
| 149 | SuppSiteHoldReason | HOLD_REASON | — | ✅ |
| 150 | SuppSiteHoldUnmatchedInvoicesFlag | HOLD_UNMATCHED_INVOICES_FLAG | — | ✅ |
| 151 | SuppSiteInactiveDate | INACTIVE_DATE | — | ✅ |
| 152 | SuppSiteInspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | ✅ |
| 153 | SuppSiteInvoiceAmountLimit | INVOICE_AMOUNT_LIMIT | — | ✅ |
| 154 | SuppSiteInvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 155 | SuppSiteJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 156 | SuppSiteJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 157 | SuppSiteLastUpdateDate6 | LAST_UPDATE_DATE | — | ✅ |
| 158 | SuppSiteLastUpdateLogin6 | LAST_UPDATE_LOGIN | — | ✅ |
| 159 | SuppSiteLastUpdatedBy6 | LAST_UPDATED_BY | — | ✅ |
| 160 | SuppSiteLocationId | LOCATION_ID | — | ✅ |
| 161 | SuppSiteMatchOption | MATCH_OPTION | — | ✅ |
| 162 | SuppSiteModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 163 | SuppSiteObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | ✅ |
| 164 | SuppSiteOffsetTaxFlag | OFFSET_TAX_FLAG | — | ✅ |
| 165 | SuppSiteOffsetVatCode | OFFSET_VAT_CODE | — | ✅ |
| 166 | SuppSitePartySiteId | PARTY_SITE_ID | — | ✅ |
| 167 | SuppSitePayDateBasisLookupCode | PAY_DATE_BASIS_LOOKUP_CODE | — | ✅ |
| 168 | SuppSitePayGroupLookupCode | PAY_GROUP_LOOKUP_CODE | — | ✅ |
| 169 | SuppSitePayOnCode | PAY_ON_CODE | — | ✅ |
| 170 | SuppSitePayOnReceiptSummaryCode | PAY_ON_RECEIPT_SUMMARY_CODE | — | ✅ |
| 171 | SuppSitePayOnUseFlag | PAY_ON_USE_FLAG | — | ✅ |
| 172 | SuppSitePaySiteFlag | PAY_SITE_FLAG | — | ✅ |
| 173 | SuppSitePaymentCurrencyCode | PAYMENT_CURRENCY_CODE | — | ✅ |
| 174 | SuppSitePaymentHoldDate | PAYMENT_HOLD_DATE | — | ✅ |
| 175 | SuppSitePaymentPriority | PAYMENT_PRIORITY | — | ✅ |
| 176 | SuppSitePcardSiteFlag | PCARD_SITE_FLAG | — | ✅ |
| 177 | SuppSitePhone | PHONE | — | ✅ |
| 178 | SuppSitePhoneCountryCode | PHONE_COUNTRY_CODE | — | ✅ |
| 179 | SuppSitePhoneExtension | PHONE_EXTENSION | — | ✅ |
| 180 | SuppSitePrcBuId | PRC_BU_ID | — | ✅ |
| 181 | SuppSitePrimaryPaySiteFlag | PRIMARY_PAY_SITE_FLAG | — | ✅ |
| 182 | SuppSiteProgramApplicationId | PROGRAM_APPLICATION_ID | — | ✅ |
| 183 | SuppSiteProgramId | PROGRAM_ID | — | ✅ |
| 184 | SuppSiteProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 185 | SuppSitePurchasingHoldReason | PURCHASING_HOLD_REASON | — | ✅ |
| 186 | SuppSitePurchasingSiteFlag | PURCHASING_SITE_FLAG | — | ✅ |
| 187 | SuppSiteQtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | ✅ |
| 188 | SuppSiteQtyRcvTolerance | QTY_RCV_TOLERANCE | — | ✅ |
| 189 | SuppSiteReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | ✅ |
| 190 | SuppSiteReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | ✅ |
| 191 | SuppSiteReceivingRoutingId | RECEIVING_ROUTING_ID | — | ✅ |
| 192 | SuppSiteRequestId1 | REQUEST_ID | — | ✅ |
| 193 | SuppSiteRetainageRate | RETAINAGE_RATE | — | ✅ |
| 194 | SuppSiteRfqOnlySiteFlag | RFQ_ONLY_SITE_FLAG | — | ✅ |
| 195 | SuppSiteSellingCompanyIdentifier | SELLING_COMPANY_IDENTIFIER | — | ✅ |
| 196 | SuppSiteServiceLevel | SERVICE_LEVEL | — | ✅ |
| 197 | SuppSiteServicesToleranceId | SERVICES_TOLERANCE_ID | — | ✅ |
| 198 | SuppSiteShipViaLookupCode | SHIP_VIA_LOOKUP_CODE | — | ✅ |
| 199 | SuppSiteShippingControl | SHIPPING_CONTROL | — | ✅ |
| 200 | SuppSiteShippingNetworkLocation | SHIPPING_NETWORK_LOCATION | — | ✅ |
| 201 | SuppSiteSupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | ✅ |
| 202 | SuppSiteTaxCountryCode | TAX_COUNTRY_CODE | — | ✅ |
| 203 | SuppSiteTaxReportingSiteFlag | TAX_REPORTING_SITE_FLAG | — | ✅ |
| 204 | SuppSiteTelex | TELEX | — | ✅ |
| 205 | SuppSiteTermsDateBasis | TERMS_DATE_BASIS | — | ✅ |
| 206 | SuppSiteTermsId | TERMS_ID | — | ✅ |
| 207 | SuppSiteToleranceId | TOLERANCE_ID | — | ✅ |
| 208 | SuppSiteTpHeaderId | TP_HEADER_ID | — | ✅ |
| 209 | SuppSiteVatCode | VAT_CODE | — | ✅ |
| 210 | SuppSiteVatRegistrationNum | VAT_REGISTRATION_NUM | — | ✅ |
| 211 | SuppSiteVendorId | VENDOR_ID | — | ✅ |
| 212 | SuppSiteVendorSiteCode | VENDOR_SITE_CODE | — | ✅ |
| 213 | SuppSiteVendorSiteCodeAlt | VENDOR_SITE_CODE_ALT | — | ✅ |
| 214 | SuppSiteVendorSiteId | VENDOR_SITE_ID | — | ✅ |
| 215 | SuppSiteVendorSiteSpkId | VENDOR_SITE_SPK_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
