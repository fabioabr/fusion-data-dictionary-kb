---
id: DOC-PO-PVO-RepositoryResponsePVO
doc_type: system-doc
title: "RepositoryResponsePVO — PVO Purchasing"
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
  - RepositoryResponsePVO
  - repositoryresponsepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RepositoryResponsePVO

## 📌 Visão Geral

Disponibiliza respostas do repositório de qualificação para consulta, facilitando acesso a informações pré-registradas de fornecedores e agilizando novos processos de avaliação.

**Caminho:** `FscmTopModelAM.PrcPoqPublicViewAM.RepositoryResponsePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 296 | 3 | 1 | 296 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 137 atributos (137 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 128 atributos (128 BICC)
- [[poq_response_repository|POQ_RESPONSE_REPOSITORY]] — 31 atributos (1 PKs, 31 BICC)

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

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
