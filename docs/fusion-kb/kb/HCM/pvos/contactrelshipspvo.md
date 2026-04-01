---
id: DOC-HCM-PVO-ContactRelshipsPVO
doc_type: system-doc
title: "ContactRelshipsPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ContactRelshipsPVO
  - contactrelshipspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContactRelshipsPVO

## 📌 Visão Geral

Consolida relacionamentos de contato (dependentes, beneficiarios, emergencia) com dados pessoais. View Object principal para gestao de dependentes no HCM.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.ContactRelshipsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 191 | 4 | 3 | 73 | 38% |

---

## 🔗 Tabelas Relacionadas

- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 105 atributos (3 BICC)
- [[per_contact_relships_f|PER_CONTACT_RELSHIPS_F]] — 27 atributos (3 PKs, 21 BICC)
- [[per_persons|PER_PERSONS]] — 2 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 57 atributos (48 BICC)

---

## ⚙️ Atributos

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonDetailsPEOApplicantNumber | APPLICANT_NUMBER | — | — |
| 2 | PersonDetailsPEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | PersonDetailsPEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | PersonDetailsPEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | PersonDetailsPEOAttribute12 | ATTRIBUTE12 | — | — |
| 6 | PersonDetailsPEOAttribute13 | ATTRIBUTE13 | — | — |
| 7 | PersonDetailsPEOAttribute14 | ATTRIBUTE14 | — | — |
| 8 | PersonDetailsPEOAttribute15 | ATTRIBUTE15 | — | — |
| 9 | PersonDetailsPEOAttribute16 | ATTRIBUTE16 | — | — |
| 10 | PersonDetailsPEOAttribute17 | ATTRIBUTE17 | — | — |
| 11 | PersonDetailsPEOAttribute18 | ATTRIBUTE18 | — | — |
| 12 | PersonDetailsPEOAttribute19 | ATTRIBUTE19 | — | — |
| 13 | PersonDetailsPEOAttribute2 | ATTRIBUTE2 | — | — |
| 14 | PersonDetailsPEOAttribute20 | ATTRIBUTE20 | — | — |
| 15 | PersonDetailsPEOAttribute21 | ATTRIBUTE21 | — | — |
| 16 | PersonDetailsPEOAttribute22 | ATTRIBUTE22 | — | — |
| 17 | PersonDetailsPEOAttribute23 | ATTRIBUTE23 | — | — |
| 18 | PersonDetailsPEOAttribute24 | ATTRIBUTE24 | — | — |
| 19 | PersonDetailsPEOAttribute25 | ATTRIBUTE25 | — | — |
| 20 | PersonDetailsPEOAttribute26 | ATTRIBUTE26 | — | — |
| 21 | PersonDetailsPEOAttribute27 | ATTRIBUTE27 | — | — |
| 22 | PersonDetailsPEOAttribute28 | ATTRIBUTE28 | — | — |
| 23 | PersonDetailsPEOAttribute29 | ATTRIBUTE29 | — | — |
| 24 | PersonDetailsPEOAttribute3 | ATTRIBUTE3 | — | — |
| 25 | PersonDetailsPEOAttribute30 | ATTRIBUTE30 | — | — |
| 26 | PersonDetailsPEOAttribute31 | ATTRIBUTE31 | — | — |
| 27 | PersonDetailsPEOAttribute32 | ATTRIBUTE32 | — | — |
| 28 | PersonDetailsPEOAttribute33 | ATTRIBUTE33 | — | — |
| 29 | PersonDetailsPEOAttribute34 | ATTRIBUTE34 | — | — |
| 30 | PersonDetailsPEOAttribute35 | ATTRIBUTE35 | — | — |
| 31 | PersonDetailsPEOAttribute36 | ATTRIBUTE36 | — | — |
| 32 | PersonDetailsPEOAttribute37 | ATTRIBUTE37 | — | — |
| 33 | PersonDetailsPEOAttribute38 | ATTRIBUTE38 | — | — |
| 34 | PersonDetailsPEOAttribute39 | ATTRIBUTE39 | — | — |
| 35 | PersonDetailsPEOAttribute4 | ATTRIBUTE4 | — | — |
| 36 | PersonDetailsPEOAttribute40 | ATTRIBUTE40 | — | — |
| 37 | PersonDetailsPEOAttribute41 | ATTRIBUTE41 | — | — |
| 38 | PersonDetailsPEOAttribute42 | ATTRIBUTE42 | — | — |
| 39 | PersonDetailsPEOAttribute43 | ATTRIBUTE43 | — | — |
| 40 | PersonDetailsPEOAttribute44 | ATTRIBUTE44 | — | — |
| 41 | PersonDetailsPEOAttribute45 | ATTRIBUTE45 | — | — |
| 42 | PersonDetailsPEOAttribute46 | ATTRIBUTE46 | — | — |
| 43 | PersonDetailsPEOAttribute47 | ATTRIBUTE47 | — | — |
| 44 | PersonDetailsPEOAttribute48 | ATTRIBUTE48 | — | — |
| 45 | PersonDetailsPEOAttribute49 | ATTRIBUTE49 | — | — |
| 46 | PersonDetailsPEOAttribute5 | ATTRIBUTE5 | — | — |
| 47 | PersonDetailsPEOAttribute50 | ATTRIBUTE50 | — | — |
| 48 | PersonDetailsPEOAttribute6 | ATTRIBUTE6 | — | — |
| 49 | PersonDetailsPEOAttribute7 | ATTRIBUTE7 | — | — |
| 50 | PersonDetailsPEOAttribute8 | ATTRIBUTE8 | — | — |
| 51 | PersonDetailsPEOAttribute9 | ATTRIBUTE9 | — | — |
| 52 | PersonDetailsPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 53 | PersonDetailsPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 54 | PersonDetailsPEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 55 | PersonDetailsPEOAttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 56 | PersonDetailsPEOAttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 57 | PersonDetailsPEOAttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 58 | PersonDetailsPEOAttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 59 | PersonDetailsPEOAttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 60 | PersonDetailsPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 61 | PersonDetailsPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 62 | PersonDetailsPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 63 | PersonDetailsPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 64 | PersonDetailsPEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 65 | PersonDetailsPEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 66 | PersonDetailsPEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 67 | PersonDetailsPEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 68 | PersonDetailsPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 69 | PersonDetailsPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 70 | PersonDetailsPEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 71 | PersonDetailsPEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 72 | PersonDetailsPEOAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 73 | PersonDetailsPEOAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 74 | PersonDetailsPEOAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 75 | PersonDetailsPEOAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 76 | PersonDetailsPEOAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 77 | PersonDetailsPEOAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 78 | PersonDetailsPEOAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 79 | PersonDetailsPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 80 | PersonDetailsPEOAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 81 | PersonDetailsPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 82 | PersonDetailsPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 83 | PersonDetailsPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 84 | PersonDetailsPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 85 | PersonDetailsPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 86 | PersonDetailsPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 87 | PersonDetailsPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 88 | PersonDetailsPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 89 | PersonDetailsPEOCreatedBy | CREATED_BY | — | — |
| 90 | PersonDetailsPEOCreationDate | CREATION_DATE | — | — |
| 91 | PersonDetailsPEOEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 92 | PersonDetailsPEOEffectiveStartDate1 | EFFECTIVE_START_DATE | — | ✅ |
| 93 | PersonDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 94 | PersonDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 95 | PersonDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 96 | PersonDetailsPEOMailingAddressId | MAILING_ADDRESS_ID | — | — |
| 97 | PersonDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 98 | PersonDetailsPEOPersonId | PERSON_ID | — | — |
| 99 | PersonDetailsPEOPersonNumber | PERSON_NUMBER | — | ✅ |
| 100 | PersonDetailsPEOPrimaryEmailId | PRIMARY_EMAIL_ID | — | — |
| 101 | PersonDetailsPEOPrimaryNidId | PRIMARY_NID_ID | — | — |
| 102 | PersonDetailsPEOPrimaryNidNumber | PRIMARY_NID_NUMBER | — | — |
| 103 | PersonDetailsPEOPrimaryPhoneId | PRIMARY_PHONE_ID | — | — |
| 104 | PersonDetailsPEOStartDate | START_DATE | — | — |
| 105 | PersonDetailsPEOWaiveDataProtect | WAIVE_DATA_PROTECT | — | — |

### [[per_contact_relships_f|PER_CONTACT_RELSHIPS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContactRelationshipId | CONTACT_RELATIONSHIP_ID | 🔑 | ✅ |
| 2 | ContactRelshipsPEOBeneficiaryFlag | BENEFICIARY_FLAG | — | ✅ |
| 3 | ContactRelshipsPEOBondholderFlag | BONDHOLDER_FLAG | — | ✅ |
| 4 | ContactRelshipsPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 5 | ContactRelshipsPEOContactPersonId | CONTACT_PERSON_ID | — | ✅ |
| 6 | ContactRelshipsPEOContactType | CONTACT_TYPE | — | ✅ |
| 7 | ContactRelshipsPEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | ContactRelshipsPEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | ContactRelshipsPEODependentFlag | DEPENDENT_FLAG | — | ✅ |
| 10 | ContactRelshipsPEOEmergencyContactFlag | EMERGENCY_CONTACT_FLAG | — | ✅ |
| 11 | ContactRelshipsPEOEndLifeReasonId | END_LIFE_REASON_ID | — | — |
| 12 | ContactRelshipsPEOExistingPerson | EXISTING_PERSON | — | ✅ |
| 13 | ContactRelshipsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | ContactRelshipsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | ContactRelshipsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | ContactRelshipsPEOLegislationCode | LEGISLATION_CODE | — | — |
| 17 | ContactRelshipsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | ContactRelshipsPEOPersonId | PERSON_ID | — | ✅ |
| 19 | ContactRelshipsPEOPersonalFlag | PERSONAL_FLAG | — | ✅ |
| 20 | ContactRelshipsPEOPrimaryContactFlag | PRIMARY_CONTACT_FLAG | — | ✅ |
| 21 | ContactRelshipsPEORltdPerRsdsWDsgntrFlag | RLTD_PER_RSDS_W_DSGNTR_FLAG | — | ✅ |
| 22 | ContactRelshipsPEOSequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 23 | ContactRelshipsPEOStartLifeReasonId | START_LIFE_REASON_ID | — | — |
| 24 | ContactRelshipsPEOStatutoryDependent | STATUTORY_DEPENDENT | — | ✅ |
| 25 | ContactRelshipsPEOThirdPartyPayFlag | THIRD_PARTY_PAY_FLAG | — | ✅ |
| 26 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 27 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |

### [[per_persons|PER_PERSONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonPEODateOfBirth | DATE_OF_BIRTH | — | ✅ |
| 2 | PersonPEOPersonId | PERSON_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNamePEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | PersonNamePEOCreatedBy | CREATED_BY | — | — |
| 3 | PersonNamePEOCreationDate | CREATION_DATE | — | — |
| 4 | PersonNamePEODisplayName | DISPLAY_NAME | — | ✅ |
| 5 | PersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 6 | PersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | PersonNamePEOFirstName | FIRST_NAME | — | ✅ |
| 8 | PersonNamePEOFullName | FULL_NAME | — | ✅ |
| 9 | PersonNamePEOHonors | HONORS | — | ✅ |
| 10 | PersonNamePEOKnownAs | KNOWN_AS | — | ✅ |
| 11 | PersonNamePEOLastName | LAST_NAME | — | ✅ |
| 12 | PersonNamePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | PersonNamePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | PersonNamePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | PersonNamePEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 16 | PersonNamePEOListName | LIST_NAME | — | ✅ |
| 17 | PersonNamePEOMiddleNames | MIDDLE_NAMES | — | ✅ |
| 18 | PersonNamePEOMilitaryRank | MILITARY_RANK | — | ✅ |
| 19 | PersonNamePEONamInformation1 | NAM_INFORMATION1 | — | ✅ |
| 20 | PersonNamePEONamInformation10 | NAM_INFORMATION10 | — | ✅ |
| 21 | PersonNamePEONamInformation11 | NAM_INFORMATION11 | — | ✅ |
| 22 | PersonNamePEONamInformation12 | NAM_INFORMATION12 | — | ✅ |
| 23 | PersonNamePEONamInformation13 | NAM_INFORMATION13 | — | ✅ |
| 24 | PersonNamePEONamInformation14 | NAM_INFORMATION14 | — | ✅ |
| 25 | PersonNamePEONamInformation15 | NAM_INFORMATION15 | — | ✅ |
| 26 | PersonNamePEONamInformation16 | NAM_INFORMATION16 | — | ✅ |
| 27 | PersonNamePEONamInformation17 | NAM_INFORMATION17 | — | ✅ |
| 28 | PersonNamePEONamInformation18 | NAM_INFORMATION18 | — | ✅ |
| 29 | PersonNamePEONamInformation19 | NAM_INFORMATION19 | — | ✅ |
| 30 | PersonNamePEONamInformation2 | NAM_INFORMATION2 | — | ✅ |
| 31 | PersonNamePEONamInformation20 | NAM_INFORMATION20 | — | ✅ |
| 32 | PersonNamePEONamInformation21 | NAM_INFORMATION21 | — | ✅ |
| 33 | PersonNamePEONamInformation22 | NAM_INFORMATION22 | — | ✅ |
| 34 | PersonNamePEONamInformation23 | NAM_INFORMATION23 | — | ✅ |
| 35 | PersonNamePEONamInformation24 | NAM_INFORMATION24 | — | ✅ |
| 36 | PersonNamePEONamInformation25 | NAM_INFORMATION25 | — | ✅ |
| 37 | PersonNamePEONamInformation26 | NAM_INFORMATION26 | — | ✅ |
| 38 | PersonNamePEONamInformation27 | NAM_INFORMATION27 | — | ✅ |
| 39 | PersonNamePEONamInformation28 | NAM_INFORMATION28 | — | ✅ |
| 40 | PersonNamePEONamInformation29 | NAM_INFORMATION29 | — | ✅ |
| 41 | PersonNamePEONamInformation3 | NAM_INFORMATION3 | — | ✅ |
| 42 | PersonNamePEONamInformation30 | NAM_INFORMATION30 | — | ✅ |
| 43 | PersonNamePEONamInformation4 | NAM_INFORMATION4 | — | ✅ |
| 44 | PersonNamePEONamInformation5 | NAM_INFORMATION5 | — | ✅ |
| 45 | PersonNamePEONamInformation6 | NAM_INFORMATION6 | — | ✅ |
| 46 | PersonNamePEONamInformation7 | NAM_INFORMATION7 | — | ✅ |
| 47 | PersonNamePEONamInformation8 | NAM_INFORMATION8 | — | ✅ |
| 48 | PersonNamePEONamInformation9 | NAM_INFORMATION9 | — | ✅ |
| 49 | PersonNamePEONameType | NAME_TYPE | — | ✅ |
| 50 | PersonNamePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 51 | PersonNamePEOOrderName | ORDER_NAME | — | — |
| 52 | PersonNamePEOPersonId | PERSON_ID | — | — |
| 53 | PersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |
| 54 | PersonNamePEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | ✅ |
| 55 | PersonNamePEOPreviousLastName | PREVIOUS_LAST_NAME | — | ✅ |
| 56 | PersonNamePEOSuffix | SUFFIX | — | ✅ |
| 57 | PersonNamePEOTitle | TITLE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
