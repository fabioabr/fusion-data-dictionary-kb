---
id: DOC-PO-PVO-InitiativeSupplierPVO
doc_type: system-doc
title: "InitiativeSupplierPVO — PVO Purchasing"
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
  - InitiativeSupplierPVO
  - initiativesupplierpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InitiativeSupplierPVO

## 📌 Visão Geral

Extrai os fornecedores participantes de cada iniciativa de qualificação, com status individual e progresso. Permite acompanhamento do andamento por fornecedor em cada campanha de homologação.

**Caminho:** `FscmTopModelAM.PrcPoqPublicViewAM.InitiativeSupplierPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 351 | 4 | 1 | 351 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 137 atributos (137 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 124 atributos (124 BICC)
- [[poq_initiatives|POQ_INITIATIVES]] — 75 atributos (75 BICC)
- [[poq_initiative_suppliers|POQ_INITIATIVE_SUPPLIERS]] — 15 atributos (1 PKs, 15 BICC)

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
| 69 | SuppContactPartyCreatedBy3 | CREATED_BY | — | ✅ |
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
| 131 | SuppContactPartyStatus1 | STATUS | — | ✅ |
| 132 | SuppContactPartyThirdPartyFlag | THIRD_PARTY_FLAG | — | ✅ |
| 133 | SuppContactPartyTradingPartnerIdentifier | TRADING_PARTNER_IDENTIFIER | — | ✅ |
| 134 | SuppContactPartyUrl | URL | — | ✅ |
| 135 | SuppContactPartyUserGuid | USER_GUID | — | ✅ |
| 136 | SuppContactPartyValidatedFlag | VALIDATED_FLAG | — | ✅ |
| 137 | SuppContactPartyYearEstablished | YEAR_ESTABLISHED | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CanceledByAttribute1 | ATTRIBUTE1 | — | ✅ |
| 2 | CanceledByAttribute10 | ATTRIBUTE10 | — | ✅ |
| 3 | CanceledByAttribute11 | ATTRIBUTE11 | — | ✅ |
| 4 | CanceledByAttribute12 | ATTRIBUTE12 | — | ✅ |
| 5 | CanceledByAttribute13 | ATTRIBUTE13 | — | ✅ |
| 6 | CanceledByAttribute14 | ATTRIBUTE14 | — | ✅ |
| 7 | CanceledByAttribute15 | ATTRIBUTE15 | — | ✅ |
| 8 | CanceledByAttribute16 | ATTRIBUTE16 | — | ✅ |
| 9 | CanceledByAttribute17 | ATTRIBUTE17 | — | ✅ |
| 10 | CanceledByAttribute18 | ATTRIBUTE18 | — | ✅ |
| 11 | CanceledByAttribute19 | ATTRIBUTE19 | — | ✅ |
| 12 | CanceledByAttribute2 | ATTRIBUTE2 | — | ✅ |
| 13 | CanceledByAttribute20 | ATTRIBUTE20 | — | ✅ |
| 14 | CanceledByAttribute21 | ATTRIBUTE21 | — | ✅ |
| 15 | CanceledByAttribute22 | ATTRIBUTE22 | — | ✅ |
| 16 | CanceledByAttribute23 | ATTRIBUTE23 | — | ✅ |
| 17 | CanceledByAttribute24 | ATTRIBUTE24 | — | ✅ |
| 18 | CanceledByAttribute25 | ATTRIBUTE25 | — | ✅ |
| 19 | CanceledByAttribute26 | ATTRIBUTE26 | — | ✅ |
| 20 | CanceledByAttribute27 | ATTRIBUTE27 | — | ✅ |
| 21 | CanceledByAttribute28 | ATTRIBUTE28 | — | ✅ |
| 22 | CanceledByAttribute29 | ATTRIBUTE29 | — | ✅ |
| 23 | CanceledByAttribute3 | ATTRIBUTE3 | — | ✅ |
| 24 | CanceledByAttribute30 | ATTRIBUTE30 | — | ✅ |
| 25 | CanceledByAttribute4 | ATTRIBUTE4 | — | ✅ |
| 26 | CanceledByAttribute5 | ATTRIBUTE5 | — | ✅ |
| 27 | CanceledByAttribute6 | ATTRIBUTE6 | — | ✅ |
| 28 | CanceledByAttribute7 | ATTRIBUTE7 | — | ✅ |
| 29 | CanceledByAttribute8 | ATTRIBUTE8 | — | ✅ |
| 30 | CanceledByAttribute9 | ATTRIBUTE9 | — | ✅ |
| 31 | CanceledByAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 32 | CanceledByAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 33 | CanceledByAttributeDate10 | ATTRIBUTE_DATE10 | — | ✅ |
| 34 | CanceledByAttributeDate11 | ATTRIBUTE_DATE11 | — | ✅ |
| 35 | CanceledByAttributeDate12 | ATTRIBUTE_DATE12 | — | ✅ |
| 36 | CanceledByAttributeDate13 | ATTRIBUTE_DATE13 | — | ✅ |
| 37 | CanceledByAttributeDate14 | ATTRIBUTE_DATE14 | — | ✅ |
| 38 | CanceledByAttributeDate15 | ATTRIBUTE_DATE15 | — | ✅ |
| 39 | CanceledByAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 40 | CanceledByAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 41 | CanceledByAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 42 | CanceledByAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 43 | CanceledByAttributeDate6 | ATTRIBUTE_DATE6 | — | ✅ |
| 44 | CanceledByAttributeDate7 | ATTRIBUTE_DATE7 | — | ✅ |
| 45 | CanceledByAttributeDate8 | ATTRIBUTE_DATE8 | — | ✅ |
| 46 | CanceledByAttributeDate9 | ATTRIBUTE_DATE9 | — | ✅ |
| 47 | CanceledByAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 48 | CanceledByAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 49 | CanceledByAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | ✅ |
| 50 | CanceledByAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | ✅ |
| 51 | CanceledByAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | ✅ |
| 52 | CanceledByAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | ✅ |
| 53 | CanceledByAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | ✅ |
| 54 | CanceledByAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | ✅ |
| 55 | CanceledByAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | ✅ |
| 56 | CanceledByAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | ✅ |
| 57 | CanceledByAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | ✅ |
| 58 | CanceledByAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 59 | CanceledByAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | ✅ |
| 60 | CanceledByAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 61 | CanceledByAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 62 | CanceledByAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 63 | CanceledByAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 64 | CanceledByAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 65 | CanceledByAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 66 | CanceledByAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 67 | CanceledByBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 68 | CanceledByCreatedBy | CREATED_BY | — | ✅ |
| 69 | CanceledByCreationDate | CREATION_DATE | — | ✅ |
| 70 | CanceledByDisplayName | DISPLAY_NAME | — | ✅ |
| 71 | CanceledByEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 72 | CanceledByEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 73 | CanceledByFirstName | FIRST_NAME | — | ✅ |
| 74 | CanceledByFullName | FULL_NAME | — | ✅ |
| 75 | CanceledByHonors | HONORS | — | ✅ |
| 76 | CanceledByKnownAs | KNOWN_AS | — | ✅ |
| 77 | CanceledByLastName | LAST_NAME | — | ✅ |
| 78 | CanceledByLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 79 | CanceledByLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 80 | CanceledByLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 81 | CanceledByLegislationCode | LEGISLATION_CODE | — | ✅ |
| 82 | CanceledByListName | LIST_NAME | — | ✅ |
| 83 | CanceledByMiddleNames | MIDDLE_NAMES | — | ✅ |
| 84 | CanceledByMilitaryRank | MILITARY_RANK | — | ✅ |
| 85 | CanceledByNamInformation1 | NAM_INFORMATION1 | — | ✅ |
| 86 | CanceledByNamInformation10 | NAM_INFORMATION10 | — | ✅ |
| 87 | CanceledByNamInformation11 | NAM_INFORMATION11 | — | ✅ |
| 88 | CanceledByNamInformation12 | NAM_INFORMATION12 | — | ✅ |
| 89 | CanceledByNamInformation13 | NAM_INFORMATION13 | — | ✅ |
| 90 | CanceledByNamInformation14 | NAM_INFORMATION14 | — | ✅ |
| 91 | CanceledByNamInformation15 | NAM_INFORMATION15 | — | ✅ |
| 92 | CanceledByNamInformation16 | NAM_INFORMATION16 | — | ✅ |
| 93 | CanceledByNamInformation17 | NAM_INFORMATION17 | — | ✅ |
| 94 | CanceledByNamInformation18 | NAM_INFORMATION18 | — | ✅ |
| 95 | CanceledByNamInformation19 | NAM_INFORMATION19 | — | ✅ |
| 96 | CanceledByNamInformation2 | NAM_INFORMATION2 | — | ✅ |
| 97 | CanceledByNamInformation20 | NAM_INFORMATION20 | — | ✅ |
| 98 | CanceledByNamInformation21 | NAM_INFORMATION21 | — | ✅ |
| 99 | CanceledByNamInformation22 | NAM_INFORMATION22 | — | ✅ |
| 100 | CanceledByNamInformation23 | NAM_INFORMATION23 | — | ✅ |
| 101 | CanceledByNamInformation24 | NAM_INFORMATION24 | — | ✅ |
| 102 | CanceledByNamInformation25 | NAM_INFORMATION25 | — | ✅ |
| 103 | CanceledByNamInformation26 | NAM_INFORMATION26 | — | ✅ |
| 104 | CanceledByNamInformation27 | NAM_INFORMATION27 | — | ✅ |
| 105 | CanceledByNamInformation28 | NAM_INFORMATION28 | — | ✅ |
| 106 | CanceledByNamInformation29 | NAM_INFORMATION29 | — | ✅ |
| 107 | CanceledByNamInformation3 | NAM_INFORMATION3 | — | ✅ |
| 108 | CanceledByNamInformation30 | NAM_INFORMATION30 | — | ✅ |
| 109 | CanceledByNamInformation4 | NAM_INFORMATION4 | — | ✅ |
| 110 | CanceledByNamInformation5 | NAM_INFORMATION5 | — | ✅ |
| 111 | CanceledByNamInformation6 | NAM_INFORMATION6 | — | ✅ |
| 112 | CanceledByNamInformation7 | NAM_INFORMATION7 | — | ✅ |
| 113 | CanceledByNamInformation8 | NAM_INFORMATION8 | — | ✅ |
| 114 | CanceledByNamInformation9 | NAM_INFORMATION9 | — | ✅ |
| 115 | CanceledByNamInformationCategory | NAM_INFORMATION_CATEGORY | — | ✅ |
| 116 | CanceledByNameType | NAME_TYPE | — | ✅ |
| 117 | CanceledByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 118 | CanceledByOrderName | ORDER_NAME | — | ✅ |
| 119 | CanceledByPersonId | PERSON_ID | — | ✅ |
| 120 | CanceledByPersonNameId | PERSON_NAME_ID | — | ✅ |
| 121 | CanceledByPreNameAdjunct | PRE_NAME_ADJUNCT | — | ✅ |
| 122 | CanceledByPreviousLastName | PREVIOUS_LAST_NAME | — | ✅ |
| 123 | CanceledBySuffix | SUFFIX | — | ✅ |
| 124 | CanceledByTitle | TITLE | — | ✅ |

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
| 54 | InitiativeCanceledBy | CANCELED_BY | — | ✅ |
| 55 | InitiativeCanceledDate | CANCELED_DATE | — | ✅ |
| 56 | InitiativeCanceledReasonCode | CANCELED_REASON_CODE | — | ✅ |
| 57 | InitiativeCompletedDate | COMPLETED_DATE | — | ✅ |
| 58 | InitiativeCreatedBy | CREATED_BY | — | ✅ |
| 59 | InitiativeCreationDate | CREATION_DATE | — | ✅ |
| 60 | InitiativeDescription | DESCRIPTION | — | ✅ |
| 61 | InitiativeInitiativeId | INITIATIVE_ID | — | ✅ |
| 62 | InitiativeInitiativeNumber | INITIATIVE_NUMBER | — | ✅ |
| 63 | InitiativeInternalNote | INTERNAL_NOTE | — | ✅ |
| 64 | InitiativeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 65 | InitiativeLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 66 | InitiativeLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 67 | InitiativeLaunchDate | LAUNCH_DATE | — | ✅ |
| 68 | InitiativeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 69 | InitiativeOwnerId | OWNER_ID | — | ✅ |
| 70 | InitiativePrcBuId | PRC_BU_ID | — | ✅ |
| 71 | InitiativeQualModelId | QUAL_MODEL_ID | — | ✅ |
| 72 | InitiativeReuseActiveQualFlag | REUSE_ACTIVE_QUAL_FLAG | — | ✅ |
| 73 | InitiativeStatus | STATUS | — | ✅ |
| 74 | InitiativeTitle | TITLE | — | ✅ |
| 75 | InitiativeType | TYPE | — | ✅ |

### [[poq_initiative_suppliers|POQ_INITIATIVE_SUPPLIERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InitSupplierId | INIT_SUPPLIER_ID | 🔑 | ✅ |
| 2 | InitiativeSupplierCreatedBy | CREATED_BY | — | ✅ |
| 3 | InitiativeSupplierCreationDate | CREATION_DATE | — | ✅ |
| 4 | InitiativeSupplierInitiativeId | INITIATIVE_ID | — | ✅ |
| 5 | InitiativeSupplierInternalResponderId | INTERNAL_RESPONDER_ID | — | ✅ |
| 6 | InitiativeSupplierLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | InitiativeSupplierLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | InitiativeSupplierLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | InitiativeSupplierObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | InitiativeSupplierResponsePulledFlag | RESPONSE_PULLED_FLAG | — | ✅ |
| 11 | InitiativeSupplierSendIntQnnaireFlag | SEND_INT_QNNAIRE_FLAG | — | ✅ |
| 12 | InitiativeSupplierSendSuppQnnaireFlag | SEND_SUPP_QNNAIRE_FLAG | — | ✅ |
| 13 | InitiativeSupplierSuppContactPartyId | SUPP_CONTACT_PARTY_ID | — | ✅ |
| 14 | InitiativeSupplierSupplierId | SUPPLIER_ID | — | ✅ |
| 15 | InitiativeSupplierSupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
