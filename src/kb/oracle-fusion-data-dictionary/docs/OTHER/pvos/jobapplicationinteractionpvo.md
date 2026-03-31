---
id: DOC-OTHER-PVO-JobApplicationInteractionPVO
doc_type: system-doc
title: "JobApplicationInteractionPVO — PVO Cross-Module"
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
  - JobApplicationInteractionPVO
  - jobapplicationinteractionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JobApplicationInteractionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Job Application Interaction. Acessa as tabelas: IRC_INTERACTIONS, PER_ALL_PEOPLE_F, PER_EMAIL_ADDRESSES (+2).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecruitingCommonAM.JobApplicationInteractionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 408 | 5 | 1 | 27 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[irc_interactions|IRC_INTERACTIONS]] — 15 atributos (1 PKs, 10 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 105 atributos (4 BICC)
- [[per_email_addresses|PER_EMAIL_ADDRESSES]] — 80 atributos (4 BICC)
- [[per_persons|PER_PERSONS]] — 84 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 124 atributos (7 BICC)

---

## ⚙️ Atributos

### [[irc_interactions|IRC_INTERACTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddedByPersonId | ADDED_BY_PERSON_ID | — | ✅ |
| 2 | ContextId | CONTEXT_ID | — | — |
| 3 | ContextTypeCode | CONTEXT_TYPE_CODE | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | InteractionDate | INTERACTION_DATE | — | ✅ |
| 7 | InteractionId | INTERACTION_ID | 🔑 | ✅ |
| 8 | InteractionPEOSubject | SUBJECT | — | — |
| 9 | InteractionTypeCode | INTERACTION_TYPE_CODE | — | ✅ |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | PersonId | PERSON_ID | — | ✅ |
| 15 | Text | TEXT | — | ✅ |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicantNumber | APPLICANT_NUMBER | — | ✅ |
| 2 | Attribute102 | ATTRIBUTE10 | — | — |
| 3 | Attribute112 | ATTRIBUTE1 | — | — |
| 4 | Attribute113 | ATTRIBUTE11 | — | — |
| 5 | Attribute122 | ATTRIBUTE12 | — | — |
| 6 | Attribute132 | ATTRIBUTE13 | — | — |
| 7 | Attribute142 | ATTRIBUTE14 | — | — |
| 8 | Attribute152 | ATTRIBUTE15 | — | — |
| 9 | Attribute162 | ATTRIBUTE16 | — | — |
| 10 | Attribute172 | ATTRIBUTE17 | — | — |
| 11 | Attribute182 | ATTRIBUTE18 | — | — |
| 12 | Attribute192 | ATTRIBUTE19 | — | — |
| 13 | Attribute202 | ATTRIBUTE20 | — | — |
| 14 | Attribute212 | ATTRIBUTE2 | — | — |
| 15 | Attribute213 | ATTRIBUTE21 | — | — |
| 16 | Attribute222 | ATTRIBUTE22 | — | — |
| 17 | Attribute232 | ATTRIBUTE23 | — | — |
| 18 | Attribute242 | ATTRIBUTE24 | — | — |
| 19 | Attribute252 | ATTRIBUTE25 | — | — |
| 20 | Attribute262 | ATTRIBUTE26 | — | — |
| 21 | Attribute272 | ATTRIBUTE27 | — | — |
| 22 | Attribute282 | ATTRIBUTE28 | — | — |
| 23 | Attribute292 | ATTRIBUTE29 | — | — |
| 24 | Attribute302 | ATTRIBUTE30 | — | — |
| 25 | Attribute311 | ATTRIBUTE31 | — | — |
| 26 | Attribute32 | ATTRIBUTE3 | — | — |
| 27 | Attribute321 | ATTRIBUTE32 | — | — |
| 28 | Attribute33 | ATTRIBUTE33 | — | — |
| 29 | Attribute34 | ATTRIBUTE34 | — | — |
| 30 | Attribute35 | ATTRIBUTE35 | — | — |
| 31 | Attribute36 | ATTRIBUTE36 | — | — |
| 32 | Attribute37 | ATTRIBUTE37 | — | — |
| 33 | Attribute38 | ATTRIBUTE38 | — | — |
| 34 | Attribute39 | ATTRIBUTE39 | — | — |
| 35 | Attribute40 | ATTRIBUTE40 | — | — |
| 36 | Attribute411 | ATTRIBUTE41 | — | — |
| 37 | Attribute42 | ATTRIBUTE4 | — | — |
| 38 | Attribute421 | ATTRIBUTE42 | — | — |
| 39 | Attribute43 | ATTRIBUTE43 | — | — |
| 40 | Attribute44 | ATTRIBUTE44 | — | — |
| 41 | Attribute45 | ATTRIBUTE45 | — | — |
| 42 | Attribute46 | ATTRIBUTE46 | — | — |
| 43 | Attribute47 | ATTRIBUTE47 | — | — |
| 44 | Attribute48 | ATTRIBUTE48 | — | — |
| 45 | Attribute49 | ATTRIBUTE49 | — | — |
| 46 | Attribute50 | ATTRIBUTE50 | — | — |
| 47 | Attribute52 | ATTRIBUTE5 | — | — |
| 48 | Attribute62 | ATTRIBUTE6 | — | — |
| 49 | Attribute72 | ATTRIBUTE7 | — | — |
| 50 | Attribute82 | ATTRIBUTE8 | — | — |
| 51 | Attribute92 | ATTRIBUTE9 | — | — |
| 52 | AttributeCategory2 | ATTRIBUTE_CATEGORY | — | — |
| 53 | AttributeDate102 | ATTRIBUTE_DATE10 | — | — |
| 54 | AttributeDate112 | ATTRIBUTE_DATE11 | — | — |
| 55 | AttributeDate122 | ATTRIBUTE_DATE12 | — | — |
| 56 | AttributeDate132 | ATTRIBUTE_DATE13 | — | — |
| 57 | AttributeDate142 | ATTRIBUTE_DATE14 | — | — |
| 58 | AttributeDate152 | ATTRIBUTE_DATE15 | — | — |
| 59 | AttributeDate17 | ATTRIBUTE_DATE1 | — | — |
| 60 | AttributeDate22 | ATTRIBUTE_DATE2 | — | — |
| 61 | AttributeDate32 | ATTRIBUTE_DATE3 | — | — |
| 62 | AttributeDate42 | ATTRIBUTE_DATE4 | — | — |
| 63 | AttributeDate52 | ATTRIBUTE_DATE5 | — | — |
| 64 | AttributeDate62 | ATTRIBUTE_DATE6 | — | — |
| 65 | AttributeDate72 | ATTRIBUTE_DATE7 | — | — |
| 66 | AttributeDate82 | ATTRIBUTE_DATE8 | — | — |
| 67 | AttributeDate92 | ATTRIBUTE_DATE9 | — | — |
| 68 | AttributeNumber102 | ATTRIBUTE_NUMBER10 | — | — |
| 69 | AttributeNumber112 | ATTRIBUTE_NUMBER1 | — | — |
| 70 | AttributeNumber113 | ATTRIBUTE_NUMBER11 | — | — |
| 71 | AttributeNumber122 | ATTRIBUTE_NUMBER12 | — | — |
| 72 | AttributeNumber132 | ATTRIBUTE_NUMBER13 | — | — |
| 73 | AttributeNumber142 | ATTRIBUTE_NUMBER14 | — | — |
| 74 | AttributeNumber152 | ATTRIBUTE_NUMBER15 | — | — |
| 75 | AttributeNumber162 | ATTRIBUTE_NUMBER16 | — | — |
| 76 | AttributeNumber172 | ATTRIBUTE_NUMBER17 | — | — |
| 77 | AttributeNumber182 | ATTRIBUTE_NUMBER18 | — | — |
| 78 | AttributeNumber192 | ATTRIBUTE_NUMBER19 | — | — |
| 79 | AttributeNumber202 | ATTRIBUTE_NUMBER20 | — | — |
| 80 | AttributeNumber22 | ATTRIBUTE_NUMBER2 | — | — |
| 81 | AttributeNumber32 | ATTRIBUTE_NUMBER3 | — | — |
| 82 | AttributeNumber42 | ATTRIBUTE_NUMBER4 | — | — |
| 83 | AttributeNumber52 | ATTRIBUTE_NUMBER5 | — | — |
| 84 | AttributeNumber62 | ATTRIBUTE_NUMBER6 | — | — |
| 85 | AttributeNumber72 | ATTRIBUTE_NUMBER7 | — | — |
| 86 | AttributeNumber82 | ATTRIBUTE_NUMBER8 | — | — |
| 87 | AttributeNumber92 | ATTRIBUTE_NUMBER9 | — | — |
| 88 | BusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 89 | CreatedBy3 | CREATED_BY | — | — |
| 90 | CreationDate3 | CREATION_DATE | — | — |
| 91 | EffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 92 | EffectiveStartDate1 | EFFECTIVE_START_DATE | — | ✅ |
| 93 | LastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 94 | LastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 95 | LastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 96 | MailingAddressId | MAILING_ADDRESS_ID | — | — |
| 97 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 98 | PersonId3 | PERSON_ID | — | — |
| 99 | PersonNumber | PERSON_NUMBER | — | ✅ |
| 100 | PrimaryEmailId | PRIMARY_EMAIL_ID | — | — |
| 101 | PrimaryNidId | PRIMARY_NID_ID | — | — |
| 102 | PrimaryNidNumber | PRIMARY_NID_NUMBER | — | — |
| 103 | PrimaryPhoneId | PRIMARY_PHONE_ID | — | — |
| 104 | StartDate1 | START_DATE | — | — |
| 105 | WaiveDataProtect | WAIVE_DATA_PROTECT | — | — |

### [[per_email_addresses|PER_EMAIL_ADDRESSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute103 | ATTRIBUTE10 | — | — |
| 2 | Attribute114 | ATTRIBUTE1 | — | — |
| 3 | Attribute115 | ATTRIBUTE11 | — | — |
| 4 | Attribute123 | ATTRIBUTE12 | — | — |
| 5 | Attribute133 | ATTRIBUTE13 | — | — |
| 6 | Attribute143 | ATTRIBUTE14 | — | — |
| 7 | Attribute153 | ATTRIBUTE15 | — | — |
| 8 | Attribute163 | ATTRIBUTE16 | — | — |
| 9 | Attribute173 | ATTRIBUTE17 | — | — |
| 10 | Attribute183 | ATTRIBUTE18 | — | — |
| 11 | Attribute193 | ATTRIBUTE19 | — | — |
| 12 | Attribute203 | ATTRIBUTE20 | — | — |
| 13 | Attribute214 | ATTRIBUTE2 | — | — |
| 14 | Attribute215 | ATTRIBUTE21 | — | — |
| 15 | Attribute223 | ATTRIBUTE22 | — | — |
| 16 | Attribute233 | ATTRIBUTE23 | — | — |
| 17 | Attribute243 | ATTRIBUTE24 | — | — |
| 18 | Attribute253 | ATTRIBUTE25 | — | — |
| 19 | Attribute263 | ATTRIBUTE26 | — | — |
| 20 | Attribute273 | ATTRIBUTE27 | — | — |
| 21 | Attribute283 | ATTRIBUTE28 | — | — |
| 22 | Attribute293 | ATTRIBUTE29 | — | — |
| 23 | Attribute303 | ATTRIBUTE30 | — | — |
| 24 | Attribute310 | ATTRIBUTE3 | — | — |
| 25 | Attribute410 | ATTRIBUTE4 | — | — |
| 26 | Attribute53 | ATTRIBUTE5 | — | — |
| 27 | Attribute63 | ATTRIBUTE6 | — | — |
| 28 | Attribute73 | ATTRIBUTE7 | — | — |
| 29 | Attribute83 | ATTRIBUTE8 | — | — |
| 30 | Attribute93 | ATTRIBUTE9 | — | — |
| 31 | AttributeCategory3 | ATTRIBUTE_CATEGORY | — | — |
| 32 | AttributeDate103 | ATTRIBUTE_DATE10 | — | — |
| 33 | AttributeDate113 | ATTRIBUTE_DATE11 | — | — |
| 34 | AttributeDate123 | ATTRIBUTE_DATE12 | — | — |
| 35 | AttributeDate133 | ATTRIBUTE_DATE13 | — | — |
| 36 | AttributeDate143 | ATTRIBUTE_DATE14 | — | — |
| 37 | AttributeDate153 | ATTRIBUTE_DATE15 | — | — |
| 38 | AttributeDate18 | ATTRIBUTE_DATE1 | — | — |
| 39 | AttributeDate23 | ATTRIBUTE_DATE2 | — | — |
| 40 | AttributeDate33 | ATTRIBUTE_DATE3 | — | — |
| 41 | AttributeDate43 | ATTRIBUTE_DATE4 | — | — |
| 42 | AttributeDate53 | ATTRIBUTE_DATE5 | — | — |
| 43 | AttributeDate63 | ATTRIBUTE_DATE6 | — | — |
| 44 | AttributeDate73 | ATTRIBUTE_DATE7 | — | — |
| 45 | AttributeDate83 | ATTRIBUTE_DATE8 | — | — |
| 46 | AttributeDate93 | ATTRIBUTE_DATE9 | — | — |
| 47 | AttributeNumber103 | ATTRIBUTE_NUMBER10 | — | — |
| 48 | AttributeNumber114 | ATTRIBUTE_NUMBER1 | — | — |
| 49 | AttributeNumber115 | ATTRIBUTE_NUMBER11 | — | — |
| 50 | AttributeNumber123 | ATTRIBUTE_NUMBER12 | — | — |
| 51 | AttributeNumber133 | ATTRIBUTE_NUMBER13 | — | — |
| 52 | AttributeNumber143 | ATTRIBUTE_NUMBER14 | — | — |
| 53 | AttributeNumber153 | ATTRIBUTE_NUMBER15 | — | — |
| 54 | AttributeNumber163 | ATTRIBUTE_NUMBER16 | — | — |
| 55 | AttributeNumber173 | ATTRIBUTE_NUMBER17 | — | — |
| 56 | AttributeNumber183 | ATTRIBUTE_NUMBER18 | — | — |
| 57 | AttributeNumber193 | ATTRIBUTE_NUMBER19 | — | — |
| 58 | AttributeNumber203 | ATTRIBUTE_NUMBER20 | — | — |
| 59 | AttributeNumber23 | ATTRIBUTE_NUMBER2 | — | — |
| 60 | AttributeNumber33 | ATTRIBUTE_NUMBER3 | — | — |
| 61 | AttributeNumber43 | ATTRIBUTE_NUMBER4 | — | — |
| 62 | AttributeNumber53 | ATTRIBUTE_NUMBER5 | — | — |
| 63 | AttributeNumber63 | ATTRIBUTE_NUMBER6 | — | — |
| 64 | AttributeNumber73 | ATTRIBUTE_NUMBER7 | — | — |
| 65 | AttributeNumber83 | ATTRIBUTE_NUMBER8 | — | — |
| 66 | AttributeNumber93 | ATTRIBUTE_NUMBER9 | — | — |
| 67 | BusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 68 | CreatedBy4 | CREATED_BY | — | — |
| 69 | CreationDate4 | CREATION_DATE | — | — |
| 70 | DateFrom | DATE_FROM | — | ✅ |
| 71 | DateTo | DATE_TO | — | ✅ |
| 72 | EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 73 | EmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 74 | EmailType | EMAIL_TYPE | — | — |
| 75 | LastUpdateDate4 | LAST_UPDATE_DATE | — | ✅ |
| 76 | LastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 77 | LastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 78 | MasteredInLdapFlag | MASTERED_IN_LDAP_FLAG | — | — |
| 79 | ObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 80 | PersonId4 | PERSON_ID | — | — |

### [[per_persons|PER_PERSONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute1 | ATTRIBUTE1 | — | — |
| 2 | Attribute10 | ATTRIBUTE10 | — | — |
| 3 | Attribute11 | ATTRIBUTE11 | — | — |
| 4 | Attribute12 | ATTRIBUTE12 | — | — |
| 5 | Attribute13 | ATTRIBUTE13 | — | — |
| 6 | Attribute14 | ATTRIBUTE14 | — | — |
| 7 | Attribute15 | ATTRIBUTE15 | — | — |
| 8 | Attribute16 | ATTRIBUTE16 | — | — |
| 9 | Attribute17 | ATTRIBUTE17 | — | — |
| 10 | Attribute18 | ATTRIBUTE18 | — | — |
| 11 | Attribute19 | ATTRIBUTE19 | — | — |
| 12 | Attribute2 | ATTRIBUTE2 | — | — |
| 13 | Attribute20 | ATTRIBUTE20 | — | — |
| 14 | Attribute21 | ATTRIBUTE21 | — | — |
| 15 | Attribute22 | ATTRIBUTE22 | — | — |
| 16 | Attribute23 | ATTRIBUTE23 | — | — |
| 17 | Attribute24 | ATTRIBUTE24 | — | — |
| 18 | Attribute25 | ATTRIBUTE25 | — | — |
| 19 | Attribute26 | ATTRIBUTE26 | — | — |
| 20 | Attribute27 | ATTRIBUTE27 | — | — |
| 21 | Attribute28 | ATTRIBUTE28 | — | — |
| 22 | Attribute29 | ATTRIBUTE29 | — | — |
| 23 | Attribute3 | ATTRIBUTE3 | — | — |
| 24 | Attribute30 | ATTRIBUTE30 | — | — |
| 25 | Attribute4 | ATTRIBUTE4 | — | — |
| 26 | Attribute5 | ATTRIBUTE5 | — | — |
| 27 | Attribute6 | ATTRIBUTE6 | — | — |
| 28 | Attribute7 | ATTRIBUTE7 | — | — |
| 29 | Attribute8 | ATTRIBUTE8 | — | — |
| 30 | Attribute9 | ATTRIBUTE9 | — | — |
| 31 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 32 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 33 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 34 | AttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 35 | AttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 36 | AttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 37 | AttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 38 | AttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 39 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 40 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 41 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 42 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 43 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 44 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 45 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 46 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 47 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 48 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 49 | AttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 50 | AttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 51 | AttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 52 | AttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 53 | AttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 54 | AttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 55 | AttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 56 | AttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 57 | AttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 58 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 59 | AttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 60 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 61 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 62 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 63 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 64 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 65 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 66 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 67 | BloodType | BLOOD_TYPE | — | — |
| 68 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 69 | CorrespondenceLanguage | CORRESPONDENCE_LANGUAGE | — | — |
| 70 | CountryOfBirth | COUNTRY_OF_BIRTH | — | — |
| 71 | CreatedBy1 | CREATED_BY | — | — |
| 72 | CreationDate1 | CREATION_DATE | — | — |
| 73 | DateOfBirth | DATE_OF_BIRTH | — | — |
| 74 | DateOfDeath | DATE_OF_DEATH | — | — |
| 75 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 76 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 77 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 78 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 79 | PartyId | PARTY_ID | — | — |
| 80 | PersonId1 | PERSON_ID | — | — |
| 81 | RegionOfBirth | REGION_OF_BIRTH | — | — |
| 82 | StartDate | START_DATE | — | — |
| 83 | TownOfBirth | TOWN_OF_BIRTH | — | — |
| 84 | UserGuid | USER_GUID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute101 | ATTRIBUTE10 | — | — |
| 2 | Attribute110 | ATTRIBUTE1 | — | — |
| 3 | Attribute111 | ATTRIBUTE11 | — | — |
| 4 | Attribute121 | ATTRIBUTE12 | — | — |
| 5 | Attribute131 | ATTRIBUTE13 | — | — |
| 6 | Attribute141 | ATTRIBUTE14 | — | — |
| 7 | Attribute151 | ATTRIBUTE15 | — | — |
| 8 | Attribute161 | ATTRIBUTE16 | — | — |
| 9 | Attribute171 | ATTRIBUTE17 | — | — |
| 10 | Attribute181 | ATTRIBUTE18 | — | — |
| 11 | Attribute191 | ATTRIBUTE19 | — | — |
| 12 | Attribute201 | ATTRIBUTE20 | — | — |
| 13 | Attribute210 | ATTRIBUTE2 | — | — |
| 14 | Attribute211 | ATTRIBUTE21 | — | — |
| 15 | Attribute221 | ATTRIBUTE22 | — | — |
| 16 | Attribute231 | ATTRIBUTE23 | — | — |
| 17 | Attribute241 | ATTRIBUTE24 | — | — |
| 18 | Attribute251 | ATTRIBUTE25 | — | — |
| 19 | Attribute261 | ATTRIBUTE26 | — | — |
| 20 | Attribute271 | ATTRIBUTE27 | — | — |
| 21 | Attribute281 | ATTRIBUTE28 | — | — |
| 22 | Attribute291 | ATTRIBUTE29 | — | — |
| 23 | Attribute301 | ATTRIBUTE30 | — | — |
| 24 | Attribute31 | ATTRIBUTE3 | — | — |
| 25 | Attribute41 | ATTRIBUTE4 | — | — |
| 26 | Attribute51 | ATTRIBUTE5 | — | — |
| 27 | Attribute61 | ATTRIBUTE6 | — | — |
| 28 | Attribute71 | ATTRIBUTE7 | — | — |
| 29 | Attribute81 | ATTRIBUTE8 | — | — |
| 30 | Attribute91 | ATTRIBUTE9 | — | — |
| 31 | AttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 32 | AttributeDate101 | ATTRIBUTE_DATE10 | — | — |
| 33 | AttributeDate111 | ATTRIBUTE_DATE11 | — | — |
| 34 | AttributeDate121 | ATTRIBUTE_DATE12 | — | — |
| 35 | AttributeDate131 | ATTRIBUTE_DATE13 | — | — |
| 36 | AttributeDate141 | ATTRIBUTE_DATE14 | — | — |
| 37 | AttributeDate151 | ATTRIBUTE_DATE15 | — | — |
| 38 | AttributeDate16 | ATTRIBUTE_DATE1 | — | — |
| 39 | AttributeDate21 | ATTRIBUTE_DATE2 | — | — |
| 40 | AttributeDate31 | ATTRIBUTE_DATE3 | — | — |
| 41 | AttributeDate41 | ATTRIBUTE_DATE4 | — | — |
| 42 | AttributeDate51 | ATTRIBUTE_DATE5 | — | — |
| 43 | AttributeDate61 | ATTRIBUTE_DATE6 | — | — |
| 44 | AttributeDate71 | ATTRIBUTE_DATE7 | — | — |
| 45 | AttributeDate81 | ATTRIBUTE_DATE8 | — | — |
| 46 | AttributeDate91 | ATTRIBUTE_DATE9 | — | — |
| 47 | AttributeNumber101 | ATTRIBUTE_NUMBER10 | — | — |
| 48 | AttributeNumber110 | ATTRIBUTE_NUMBER1 | — | — |
| 49 | AttributeNumber111 | ATTRIBUTE_NUMBER11 | — | — |
| 50 | AttributeNumber121 | ATTRIBUTE_NUMBER12 | — | — |
| 51 | AttributeNumber131 | ATTRIBUTE_NUMBER13 | — | — |
| 52 | AttributeNumber141 | ATTRIBUTE_NUMBER14 | — | — |
| 53 | AttributeNumber151 | ATTRIBUTE_NUMBER15 | — | — |
| 54 | AttributeNumber161 | ATTRIBUTE_NUMBER16 | — | — |
| 55 | AttributeNumber171 | ATTRIBUTE_NUMBER17 | — | — |
| 56 | AttributeNumber181 | ATTRIBUTE_NUMBER18 | — | — |
| 57 | AttributeNumber191 | ATTRIBUTE_NUMBER19 | — | — |
| 58 | AttributeNumber201 | ATTRIBUTE_NUMBER20 | — | — |
| 59 | AttributeNumber21 | ATTRIBUTE_NUMBER2 | — | — |
| 60 | AttributeNumber31 | ATTRIBUTE_NUMBER3 | — | — |
| 61 | AttributeNumber41 | ATTRIBUTE_NUMBER4 | — | — |
| 62 | AttributeNumber51 | ATTRIBUTE_NUMBER5 | — | — |
| 63 | AttributeNumber61 | ATTRIBUTE_NUMBER6 | — | — |
| 64 | AttributeNumber71 | ATTRIBUTE_NUMBER7 | — | — |
| 65 | AttributeNumber81 | ATTRIBUTE_NUMBER8 | — | — |
| 66 | AttributeNumber91 | ATTRIBUTE_NUMBER9 | — | — |
| 67 | BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 68 | CreatedBy2 | CREATED_BY | — | — |
| 69 | CreationDate2 | CREATION_DATE | — | — |
| 70 | DisplayName | DISPLAY_NAME | — | — |
| 71 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 72 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 73 | FirstName | FIRST_NAME | — | ✅ |
| 74 | FullName | FULL_NAME | — | ✅ |
| 75 | Honors | HONORS | — | — |
| 76 | KnownAs | KNOWN_AS | — | — |
| 77 | LastName | LAST_NAME | — | ✅ |
| 78 | LastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 79 | LastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 80 | LastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 81 | LegislationCode | LEGISLATION_CODE | — | — |
| 82 | ListName | LIST_NAME | — | — |
| 83 | MiddleNames | MIDDLE_NAMES | — | ✅ |
| 84 | MilitaryRank | MILITARY_RANK | — | — |
| 85 | NamInformation1 | NAM_INFORMATION1 | — | — |
| 86 | NamInformation10 | NAM_INFORMATION10 | — | — |
| 87 | NamInformation11 | NAM_INFORMATION11 | — | — |
| 88 | NamInformation12 | NAM_INFORMATION12 | — | — |
| 89 | NamInformation13 | NAM_INFORMATION13 | — | — |
| 90 | NamInformation14 | NAM_INFORMATION14 | — | — |
| 91 | NamInformation15 | NAM_INFORMATION15 | — | — |
| 92 | NamInformation16 | NAM_INFORMATION16 | — | — |
| 93 | NamInformation17 | NAM_INFORMATION17 | — | — |
| 94 | NamInformation18 | NAM_INFORMATION18 | — | — |
| 95 | NamInformation19 | NAM_INFORMATION19 | — | — |
| 96 | NamInformation2 | NAM_INFORMATION2 | — | — |
| 97 | NamInformation20 | NAM_INFORMATION20 | — | — |
| 98 | NamInformation21 | NAM_INFORMATION21 | — | — |
| 99 | NamInformation22 | NAM_INFORMATION22 | — | — |
| 100 | NamInformation23 | NAM_INFORMATION23 | — | — |
| 101 | NamInformation24 | NAM_INFORMATION24 | — | — |
| 102 | NamInformation25 | NAM_INFORMATION25 | — | — |
| 103 | NamInformation26 | NAM_INFORMATION26 | — | — |
| 104 | NamInformation27 | NAM_INFORMATION27 | — | — |
| 105 | NamInformation28 | NAM_INFORMATION28 | — | — |
| 106 | NamInformation29 | NAM_INFORMATION29 | — | — |
| 107 | NamInformation3 | NAM_INFORMATION3 | — | — |
| 108 | NamInformation30 | NAM_INFORMATION30 | — | — |
| 109 | NamInformation4 | NAM_INFORMATION4 | — | — |
| 110 | NamInformation5 | NAM_INFORMATION5 | — | — |
| 111 | NamInformation6 | NAM_INFORMATION6 | — | — |
| 112 | NamInformation7 | NAM_INFORMATION7 | — | — |
| 113 | NamInformation8 | NAM_INFORMATION8 | — | — |
| 114 | NamInformation9 | NAM_INFORMATION9 | — | — |
| 115 | NamInformationCategory | NAM_INFORMATION_CATEGORY | — | — |
| 116 | NameType | NAME_TYPE | — | — |
| 117 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 118 | OrderName | ORDER_NAME | — | — |
| 119 | PersonId2 | PERSON_ID | — | — |
| 120 | PersonNameId | PERSON_NAME_ID | — | — |
| 121 | PreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 122 | PreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 123 | Suffix | SUFFIX | — | — |
| 124 | Title | TITLE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
